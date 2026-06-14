#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["fal-client"]
# ///
"""Minimal fal.ai image and video generator.

Modes:
- t2i (text-to-image, default): Flux dev (lifestyle, hero, product-in-scene)
- poster (text-to-image with legible text): GPT Image 2 (festive posters, sale cards, anything with rendered copy on the image)
- i2i (image-to-image): Flux dev (style-anchored variation; aspect inherits from reference)
- t2v (text-to-video): Kling 3.0 Standard with native audio
- i2v (image-to-video): Kling 3.0 Standard image-to-video (animates an input image)

To change which model a mode points at, edit MODEL_DEFAULTS below, or pass
--model fal-ai/<slug> at call time to override for a single run.

Usage:
    # FAL_KEY in .env at repo root, or exported in shell

    # Still image (default)
    uv run fal_run.py --prompt "..." --output ./hero.png --aspect 4:5

    # Poster with legible text and graphics (GPT Image 2)
    uv run fal_run.py --mode poster --prompt "..." --output ./diwali.png \\
      --aspect 4:5 --quality high

    # Image variation anchored on a reference (style/composition)
    uv run fal_run.py --mode i2i --prompt "..." \\
      --reference ./brand-mood.png --output ./variant.png --strength 0.75

    # Video from text
    uv run fal_run.py --mode t2v --prompt "..." --output ./reel.mp4 \\
      --aspect 9:16 --duration 6s

    # Video from an existing image
    uv run fal_run.py --mode i2v --prompt "subtle steam, gentle parallax" \\
      --reference ./hero.png --output ./reel.mp4 --duration 6s

Prints one JSON line to stdout on success. Non-zero exit on failure.
"""

import argparse
import json
import os
import sys
import urllib.request


def load_env_file(path: str = ".env") -> None:
    """Load KEY=VALUE pairs from a .env file in the current working directory.

    Does nothing if the file is missing. Does not overwrite vars already set
    in the process env (CLI export wins over .env).
    """
    if not os.path.exists(path):
        return
    with open(path) as f:
        for raw in f:
            line = raw.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, value = line.partition("=")
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            if key and key not in os.environ:
                os.environ[key] = value


IMAGE_ASPECT_MAP = {
    "1:1": "square_hd",
    "9:16": "portrait_16_9",
    "16:9": "landscape_16_9",
    "4:5": {"width": 1024, "height": 1280},
    "3:4": {"width": 1024, "height": 1365},
}

# GPT Image 2 wants pixel dims as multiples of 16; 1365 (Flux 3:4) is not.
POSTER_ASPECT_MAP = {
    "1:1": "square_hd",
    "9:16": "portrait_16_9",
    "16:9": "landscape_16_9",
    "4:5": {"width": 1024, "height": 1280},
    "3:4": {"width": 1024, "height": 1376},
}
POSTER_QUALITIES = ["auto", "low", "medium", "high"]

VIDEO_ASPECTS = ["16:9", "9:16", "auto"]
VIDEO_DURATIONS = ["4s", "6s", "8s"]
VIDEO_RESOLUTIONS = ["720p", "1080p", "4k"]

# To swap a default model, edit the slug here. Per-call override: pass --model.
# Defaults upgraded 2026-06-07 from flux-dev to the balanced tier (prices vetted on fal model pages):
#   t2i  lifestyle / photoreal:        fal-ai/flux-2-pro  (~$0.03 first MP +$0.015/extra; budget: fal-ai/flux/dev ~$0.025/MP)
#   t2i  photoreal + legible text:     fal-ai/nano-banana-pro  (~$0.15/img, --model override; or nano-banana-2 ~$0.08/1K)
#   poster (headline is the artwork):  openai/gpt-image-2  (~$0.21 high@1K; best fine typography)
#   i2i  style / edit variant:         fal-ai/nano-banana/edit  (~$0.039/img, keeps text legible)
#        premium edit: fal-ai/nano-banana-pro/edit (~$0.15/img) ; masked headline/price edit: openai/gpt-image-2/edit
#   Video hero (expensive): fal-ai/veo3.1 (~$0.40/sec) ; default cheap: fal-ai/kling-video/v3/standard/* (~$0.084/sec)
# Param-shape notes (build_image_args / build_i2i_args branch on the slug):
#   Gemini / Nano-Banana t2i use aspect_ratio (not image_size). FLUX.2 uses image_size but has NO num_images.
#   Gemini / Nano-Banana / GPT-Image EDIT models use image_urls (a list) and have NO strength knob.
MODEL_DEFAULTS = {
    "t2i": "fal-ai/flux-2-pro",
    "poster": "openai/gpt-image-2",
    "i2i": "fal-ai/nano-banana/edit",
    "t2v": "fal-ai/kling-video/v3/standard/text-to-video",
    "i2v": "fal-ai/kling-video/v3/standard/image-to-video",
}


def fail(msg: str, **extra) -> int:
    payload = {"error": msg}
    payload.update(extra)
    print(json.dumps(payload), file=sys.stderr)
    return 1


def build_image_args(args):
    if args.aspect not in IMAGE_ASPECT_MAP:
        return None, fail(
            f"aspect '{args.aspect}' not supported for t2i",
            allowed=list(IMAGE_ASPECT_MAP.keys()),
        )
    # Gemini / Nano Banana Pro family take aspect_ratio (a string) + resolution,
    # not Flux's image_size {width,height} dict. Same --aspect values map straight
    # across (1:1, 4:5, 3:4, 9:16, 16:9 are all valid aspect_ratio values).
    model = (args.model or "").lower()
    if "nano-banana" in model or "gemini" in model:
        return {
            "prompt": args.prompt,
            "aspect_ratio": args.aspect,
            "num_images": 1,
        }, None
    # FLUX.2 family takes image_size but has no num_images field.
    if "flux-2" in model:
        return {
            "prompt": args.prompt,
            "image_size": IMAGE_ASPECT_MAP[args.aspect],
        }, None
    # FLUX.1 dev and similar: image_size + num_images.
    return {
        "prompt": args.prompt,
        "image_size": IMAGE_ASPECT_MAP[args.aspect],
        "num_images": 1,
    }, None


def build_poster_args(args):
    if args.aspect not in POSTER_ASPECT_MAP:
        return None, fail(
            f"aspect '{args.aspect}' not supported for poster",
            allowed=list(POSTER_ASPECT_MAP.keys()),
        )
    return {
        "prompt": args.prompt,
        "image_size": POSTER_ASPECT_MAP[args.aspect],
        "num_images": 1,
        "quality": args.quality,
    }, None


def build_i2i_args(args, fal_client):
    if not args.reference:
        return None, fail("--reference (path or URL to source image) is required for i2i")
    if args.reference.startswith(("http://", "https://")):
        image_url = args.reference
    else:
        if not os.path.exists(args.reference):
            return None, fail(f"reference image not found: {args.reference}")
        try:
            image_url = fal_client.upload_file(args.reference)
        except Exception as e:
            return None, fail(f"reference upload failed: {e}")
    # Gemini / Nano-Banana edit models and GPT Image 2 edit take image_urls (a list)
    # and have NO strength knob; the edit is driven entirely by the prompt. Aspect
    # defaults to "auto" (inherits from the reference), so it is not passed.
    model = (args.model or "").lower()
    if any(k in model for k in ("nano-banana", "gemini", "gpt-image")):
        arguments = {
            "prompt": args.prompt,
            "image_urls": [image_url],
            "num_images": 1,
        }
        if "gpt-image" in model:
            arguments["quality"] = args.quality
        return arguments, None
    # Flux i2i: single image_url + strength knob.
    return {
        "prompt": args.prompt,
        "image_url": image_url,
        "strength": args.strength,
        "num_images": 1,
    }, None


def build_video_args(args, fal_client):
    if args.aspect not in VIDEO_ASPECTS:
        return None, fail(
            f"aspect '{args.aspect}' not supported for video",
            allowed=VIDEO_ASPECTS,
        )
    model_lower = args.model.lower()
    is_kling = "kling" in model_lower
    is_veo = "veo" in model_lower

    if is_kling and args.aspect == "auto":
        return None, fail(
            "Kling does not accept aspect='auto'; pass --aspect 16:9 or 9:16 explicitly",
        )

    arguments = {
        "prompt": args.prompt,
        "aspect_ratio": args.aspect,
        # Kling: integer-seconds string ("6"). Veo: seconds-with-suffix ("6s").
        "duration": args.duration.rstrip("s") if is_kling else args.duration,
        "generate_audio": not args.no_audio,
    }
    # Veo accepts resolution; Kling Standard ignores it (1080p ceiling).
    if is_veo:
        arguments["resolution"] = args.resolution
    if args.negative_prompt:
        arguments["negative_prompt"] = args.negative_prompt

    if args.mode == "i2v":
        if not args.reference:
            return None, fail("--reference (path or URL to source image) is required for i2v")
        if args.reference.startswith(("http://", "https://")):
            arguments["image_url"] = args.reference
        else:
            if not os.path.exists(args.reference):
                return None, fail(f"reference image not found: {args.reference}")
            try:
                arguments["image_url"] = fal_client.upload_file(args.reference)
            except Exception as e:
                return None, fail(f"reference upload failed: {e}")
    return arguments, None


def extract_url(result, mode):
    if mode in ("t2i", "poster", "i2i"):
        images = result.get("images") or []
        if not images:
            return None, fail("no images in fal response", response=result)
        url = images[0].get("url")
        if not url:
            return None, fail("missing url in fal image", image=images[0])
        return url, None
    video = result.get("video") or {}
    url = video.get("url")
    if not url:
        return None, fail("no video url in fal response", response=result)
    return url, None


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate an image or video via fal.ai")
    parser.add_argument("--prompt", required=True, help="Text prompt")
    parser.add_argument("--output", required=True, help="Output file path (.png for t2i, .mp4 for video)")
    parser.add_argument(
        "--mode", default="t2i", choices=["t2i", "poster", "i2i", "t2v", "i2v"],
        help="Generation mode. Default t2i. Use 'poster' for legible text and graphics (GPT Image 2). Use 'i2i' for style-anchored variation on an existing image.",
    )
    parser.add_argument(
        "--aspect", default=None,
        help="Aspect ratio. t2i and poster: 1:1, 4:5, 3:4, 9:16, 16:9 (default 1:1). Video: 16:9, 9:16, auto (default 9:16 for t2v, auto for i2v). Ignored for i2i (inherits from reference).",
    )
    parser.add_argument("--model", default=None, help="Override model slug.")
    parser.add_argument("--reference", help="i2i and i2v: path or URL to source image.")
    parser.add_argument(
        "--strength", type=float, default=0.85,
        help="i2i only: how much to transform the reference. 0.0=identity, 1.0=ignore reference. Default 0.85 (anchors on reference style/composition; pass 0.95 for Flux's default heavier transformation).",
    )
    parser.add_argument(
        "--duration", default="6s", choices=VIDEO_DURATIONS,
        help="Video duration. Default 6s.",
    )
    parser.add_argument(
        "--resolution", default="1080p", choices=VIDEO_RESOLUTIONS,
        help="Video resolution. Default 1080p. Veo only; Kling Standard ignores this (1080p ceiling).",
    )
    parser.add_argument(
        "--quality", default="high", choices=POSTER_QUALITIES,
        help="Poster mode only: GPT Image 2 quality tier. Default high. 'low' or 'medium' for cheap variant testing.",
    )
    parser.add_argument("--no-audio", action="store_true", help="Disable generated audio (video modes only).")
    parser.add_argument("--negative-prompt", help="Negative prompt (video modes).")
    args = parser.parse_args()

    if args.aspect is None:
        args.aspect = {"t2i": "1:1", "poster": "1:1", "i2i": "1:1", "t2v": "9:16", "i2v": "auto"}[args.mode]
    if args.model is None:
        args.model = MODEL_DEFAULTS[args.mode]
    if not 0.0 <= args.strength <= 1.0:
        return fail(f"--strength must be between 0.0 and 1.0, got {args.strength}")

    load_env_file()

    if not os.environ.get("FAL_KEY"):
        return fail(
            "FAL_KEY not found",
            hint="Set FAL_KEY in .env at repo root, or export it in your shell. Get a key at https://fal.ai/dashboard/keys",
        )

    try:
        import fal_client
    except ImportError:
        return fail(
            "fal-client not installed",
            hint="Run the script via `uv run` so PEP 723 metadata auto-installs deps: uv run .claude/skills/fal-image-gen/fal_run.py ...",
        )

    if args.mode == "t2i":
        arguments, err = build_image_args(args)
    elif args.mode == "poster":
        arguments, err = build_poster_args(args)
    elif args.mode == "i2i":
        arguments, err = build_i2i_args(args, fal_client)
    else:
        arguments, err = build_video_args(args, fal_client)
    if err is not None:
        return err

    try:
        result = fal_client.subscribe(args.model, arguments=arguments, with_logs=False)
    except Exception as e:
        return fail(f"fal call failed: {e}")

    url, err = extract_url(result, args.mode)
    if err is not None:
        return err

    output_dir = os.path.dirname(os.path.abspath(args.output)) or "."
    try:
        os.makedirs(output_dir, exist_ok=True)
        with urllib.request.urlopen(url) as src, open(args.output, "wb") as dst:
            dst.write(src.read())
    except Exception as e:
        return fail(f"download failed: {e}", url=url)

    out = {
        "output": args.output,
        "mode": args.mode,
        "model": args.model,
        "aspect": args.aspect,
        "fal_url": url,
    }
    if args.mode == "poster":
        out["quality"] = args.quality
    if args.mode == "i2i" and "flux" in args.model.lower():
        out["strength"] = args.strength
    if args.mode in ("t2v", "i2v"):
        out["duration"] = args.duration
        if "veo" in args.model.lower():
            out["resolution"] = args.resolution
        out["audio"] = not args.no_audio
    print(json.dumps(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
