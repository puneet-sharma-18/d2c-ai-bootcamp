---
name: fal-image-gen
description: Generate real images and short videos via fal.ai. Use when the founder needs a shippable asset (ad creative, PDP hero, reel, packaging mockup, animated hero) instead of Claude's HTML slop. Triggers on phrases like "generate an image", "make me a creative", "draw a hero shot", "render the ad", "generate a video", "animate this", "make a reel". This is a thin caller. The agent invoking it is responsible for brand-aware prompt composition.
---

You are the fal-image-gen skill. You wrap a Python script that calls fal.ai. Five modes: text-to-image (FLUX.2 pro, default), poster with legible text and graphics (GPT Image 2), image-to-image variation (Nano Banana edit, default), text-to-video (Kling 3.0 Standard) and image-to-video (Kling 3.0 Standard i2v). Every default is overridable with `--model`. You do not compose prompts or apply brand voice. You take a prompt, an output path and a few format flags, and you produce a real file on disk. Slop is not an option here.

The video default is Kling 3.0 Standard (~$0.084/sec) rather than Veo 3.1 (~$0.40/sec Standard) because the Performance Marketer pipeline runs many variants — Veo's price only earns its keep on the one hero asset per quarter. Pass `--model fal-ai/veo3.1` when you want the hero. The poster mode exists because Flux and Kling cannot render legible copy on the image; GPT Image 2 (OpenAI Images 2.0) is the right tool for festive posters, sale cards and anything where text is part of the artwork.

## When to use

Any task that needs an actual image or short video file on disk. Examples:
- Generating an ad creative (still or 6-8s video) from a Performance Marketer brief
- A PDP hero shot for the Storefront teammate (use `t2i`)
- A festive poster, sale card or banner where text is part of the image (use `poster`)
- A reel cover image or animated reel for the Content Lead's calendar
- Animating an approved hero shot into a 6s vertical video for paid social
- A one-off "show me what X would look like" exploration

Mode picking:
- **t2i (FLUX.2 pro, default)** — frontier photography-style lifestyle, hero shots, product-in-scene. Renders some text, so drop magazine/brand names from style refs or they leak onto the image. Budget option: `--model fal-ai/flux/dev` (~$0.025/MP, cannot render text). Photoreal AND legible text in one pass: `--model fal-ai/nano-banana-pro`.
- **poster (GPT Image 2)** — festive creatives with rendered headlines, sale cards, anything with text or graphic shapes as part of the artwork. ~99% text accuracy per the WaveSpeed comparison. English and Indic in-image text both work. Devanagari renders cleanly; for other Indic scripts (Tamil, Bengali, Punjabi, etc.) overlay text in Figma or Canva.
- **i2i (Nano Banana edit, default)** — prompt-driven edit of a reference: fan out variants of an approved hero, match a brand mood board across new SKUs, apply a winning ad's look to a different product, and (unlike Flux i2i) keep label/headline text legible. Note: the default model is prompt-driven and ignores `--strength` (see below). Premium edit: `--model fal-ai/nano-banana-pro/edit`. Strength-knob style transfer: `--model fal-ai/flux/dev/image-to-image`.
- **t2v (Kling 3.0)** — short ad video, reel hero, B-roll. Native audio.
- **i2v (Kling 3.0)** — animate an approved still into 6-8s motion. Best for organic motion (steam, parallax, light shifts).

Do NOT use t2v/i2v for: schematic diagrams or flowcharts. The video model is best at organic motion; rendered text on video is unreliable. For typography-first creatives, generate the still in `poster` mode and animate later if needed.

## Prerequisites

1. `FAL_KEY` available, either in a `.env` file at the repo root or exported in the shell. Recommended path: copy `.env.example` to `.env` and paste the key there. The script auto-loads `.env` from the current working directory; a shell `export` overrides anything in the file.
2. `uv` installed (one-time). macOS: `brew install uv`. Windows: `winget install --id=astral-sh.uv -e`. Anything else: https://docs.astral.sh/uv/getting-started/installation/. `fal-client` is declared in the script's PEP 723 inline metadata, so `uv run` creates a per-script venv and installs it on first call. No `pip install` step.

If `FAL_KEY` is missing the script's stderr names exactly what to fix. If `uv` is missing, the `uv run` command itself errors with an install hint.

## Invocation

The script lives at `.claude/skills/fal-image-gen/fal_run.py`. Call it via Bash.

### Image (default — lifestyle, hero, product-in-scene)

```bash
uv run .claude/skills/fal-image-gen/fal_run.py \
  --prompt "<the full image prompt, brand-aware>" \
  --output "<path/to/output.png>" \
  --aspect <1:1|4:5|9:16|16:9|3:4>
```

Defaults: `--mode t2i`, `--aspect 1:1`, `--model fal-ai/flux-2-pro`. Budget downgrade: `--model fal-ai/flux/dev`.

### Poster with legible text and graphics (GPT Image 2)

```bash
uv run .claude/skills/fal-image-gen/fal_run.py \
  --mode poster \
  --prompt "<headline copy in quotes, layout description, brand palette, banned-imagery exclusions>" \
  --output "<path/to/output.png>" \
  --aspect 4:5 \
  --quality high
```

Defaults: `--aspect 1:1`, `--quality high`, `--model openai/gpt-image-2`. Allowed aspects: `1:1`, `4:5`, `3:4`, `9:16`, `16:9`. Allowed qualities: `auto`, `low`, `medium`, `high`. Use `low` or `medium` when burning through 20+ poster variants for A/B; bump to `high` on the winner.

Prompt shape for poster mode is different from `t2i`. Put the headline in quotes so GPT Image 2 renders it verbatim ("Eat, do not spit." or "ऑनलाइन पान"). Describe layout and typography mood — "block sans-serif, centered, lower third"; "ornate Devanagari title at top, ingredient list bottom-left". Devanagari in-image works; for Tamil, Telugu, Bengali, Punjabi, Gujarati, Odia, Malayalam, Kannada, overlay the script in a real design tool over an AI background.

### Image-to-image variation (i2i)

```bash
uv run .claude/skills/fal-image-gen/fal_run.py \
  --mode i2i \
  --reference "<path or URL to source image>" \
  --prompt "<what should change: new SKU on the same brass plate, same light, same composition>" \
  --output "<path/to/variant.png>" \
  --strength 0.75
```

Defaults: `--model fal-ai/nano-banana/edit`. The reference can be a local file (uploaded to fal automatically) or a public URL. Aspect inherits from the reference. IMPORTANT: the default edit model (Nano Banana / Gemini family) is prompt-driven and has NO strength knob, so `--strength` is IGNORED for it — describe the change in the prompt instead (e.g. "leave the label as a blank panel", "swap the SKU, keep the brass plate and light"). `--strength` only applies when you override to a Flux i2i model (`--model fal-ai/flux/dev/image-to-image`), where 0.0 returns the reference unchanged and 1.0 ignores it; the strength/rendered-text guidance below is Flux-specific.

For **text-free references** (mood boards, product photos, hero shots without overlaid copy), 0.65 to 0.85 is the sweet spot for "keep the brand look, change the subject"; 0.90 to 0.95 is "take the palette as inspiration, generate fresh." If the reference has rendered headlines, brand marks or badges, the rule changes — see **Strength knob and rendered text** below.

**Where to keep reference images.** Any local path works, but the project convention is `brand-brain/visual-refs/` for persistent visual anchors (approved hero shots, brand mood boards, winning ad screenshots a founder wants to remix). Use `brand-brain/ads/` when the reference *is* a previously-winning ad — that folder is already a Performance Marketer prerequisite. Inter-step references (an image generated earlier in the same session) live in their `my-work/performance-marketer/<date>-*/visuals/` folder; pass that path directly. A public URL also works if the reference is hosted (Shopify CDN, etc.) — fal fetches it without an upload step.

#### Strength knob and rendered text

When the reference image has overlaid copy (a headline, a brand mark, a badge, a swooping arrow with a label), `--strength` interacts with text non-obviously. Flux dev cannot render legible copy at any strength, but at low strengths it *tries to preserve* the reference's letter shapes:

| `--strength` | Behaviour on a text-bearing reference |
|---|---|
| 0.85 to 0.95 | Reference text and graphic overlays are correctly **dropped**. Output is a clean photo in the reference's brand world without inherited copy. Composite real text in Figma after. |
| 0.50 to 0.80 | Model tries to **preserve** reference text shapes. Output reads as gibberish — looks like the source from across the room, falls apart on inspection. |
| below 0.50 | Heavy reference influence; gibberish text gets worse and the image content largely echoes the source. |

**Worked example in this repo.** Source: `brand-brain/visual-refs/nasher_miles_ad.jpg` — a Nasher Miles ad with a rendered "Always Room For More" headline, brand mark, swooping purple arrow and "ANTWERP Collection ✈️" pill tag. Three runs from one source, in `my-work/performance-marketer/2026-05-17-test-i2i/visuals/`:

- `v1-strength-085.png` — i2i, `--strength 0.85`, prompt translates to a Paan-brand grandmother scene. Reference text and arrow correctly dropped. Clean.
- `v2-nasher-variant-standing.png` — i2i, `--strength 0.65`, same Nasher Miles brand world (purple suitcase, meadow, arrow shape) preserved beautifully — but the headline reads `Arenda Room / Far More`. Flux holding onto letter shapes it cannot render.
- `v3-poster-nasher-text.png` — `--mode poster` (GPT Image 2), no reference, prompt-only. Headline `Always Room For More` renders cleanly, two-color treatment intact, brand mark and pill tag legible.

**Decision rule.** If the reference has rendered copy you want preserved in the output: use `--mode poster` with the headline written verbatim into the prompt, and accept that you lose the `--reference` channel (poster is text-to-image in this implementation). If you want a clean photo and will composite text in Figma later: use `--mode i2i` at `--strength 0.85` or higher. Cost difference is small (~$0.012 i2i Flux vs ~$0.04 to $0.35 poster GPT Image 2) — if rendered text is part of the ad, the cost premium is the point.

Use i2i when:
- You have an approved hero image and want variants for 3 other SKUs that match the brand world
- A brand mood board is the single source of truth and every new asset must visually rhyme with it
- A winning Meta ad's composition tested well; you want the same composition with a different product

Do not use i2i to edit text on a poster — Flux dev does not preserve copy reliably. For that workflow, override the model to `openai/gpt-image-2` (the conversational-editing path is in the future-expansion list below).

### Video from text (t2v)

```bash
uv run .claude/skills/fal-image-gen/fal_run.py \
  --mode t2v \
  --prompt "<full video prompt: subject, motion, light, mood, banned-imagery exclusions>" \
  --output "<path/to/output.mp4>" \
  --aspect 9:16 \
  --duration 6s
```

Defaults: `--aspect 9:16`, `--duration 6s`, audio on, `--model fal-ai/kling-video/v3/standard/text-to-video`. Allowed aspects: `16:9`, `9:16`, `auto` (Veo-only; Kling rejects `auto`, pass `16:9` or `9:16` explicitly). Allowed durations: `4s`, `6s`, `8s`. Pass `--no-audio` to mute. Pass `--negative-prompt "..."` for explicit exclusions.

For the one hero asset per quarter where Veo's quality earns its price, override the model:

```bash
uv run .claude/skills/fal-image-gen/fal_run.py \
  --mode t2v --model fal-ai/veo3.1 \
  --prompt "..." --output ./hero.mp4 \
  --aspect 9:16 --duration 6s --resolution 1080p
```

`--resolution` (720p/1080p/4k) is Veo-only. Kling Standard runs at 1080p ceiling and ignores the flag.

### Video from an image (i2v)

```bash
uv run .claude/skills/fal-image-gen/fal_run.py \
  --mode i2v \
  --reference "<path or URL to source image>" \
  --prompt "<what should happen: subtle steam rising, gentle parallax, light shift>" \
  --output "<path/to/output.mp4>" \
  --aspect 9:16 \
  --duration 6s
```

Defaults: `--aspect auto` (inherits the source image's ratio for Veo; Kling rejects `auto`, pass `16:9` or `9:16`), `--duration 6s`, audio on, `--model fal-ai/kling-video/v3/standard/image-to-video`. The reference can be a local file (uploaded to fal automatically) or a public URL. Source should be 720p or higher in 16:9 or 9:16. Keep the motion prompt small and physical — i2v handles organic motion (steam, drift, parallax, fabric, light shifts) better than dramatic action.

Reference image location follows the same convention as i2i: `brand-brain/visual-refs/` for persistent brand anchors, `my-work/performance-marketer/<date>-*/visuals/` for stills generated earlier in the pipeline, or any public URL.

## Output

On success, prints one JSON line to stdout. Image:
```json
{"output": "hero.png", "mode": "t2i", "model": "fal-ai/flux/dev", "aspect": "4:5", "fal_url": "https://..."}
```

Poster:
```json
{"output": "diwali.png", "mode": "poster", "model": "openai/gpt-image-2", "aspect": "4:5", "quality": "high", "fal_url": "https://..."}
```

i2i:
```json
{"output": "variant.png", "mode": "i2i", "model": "fal-ai/flux/dev/image-to-image", "aspect": "1:1", "strength": 0.75, "fal_url": "https://..."}
```

Video:
```json
{"output": "reel.mp4", "mode": "t2v", "model": "fal-ai/kling-video/v3/standard/text-to-video", "aspect": "9:16", "duration": "6s", "audio": true, "fal_url": "https://..."}
```

The asset is saved at `--output` (PNG for t2i and poster, MP4 for video). The `fal_url` is the original fal-hosted URL (useful for debugging or sharing without redownload).

On failure, prints JSON to stderr and exits non-zero. Read the error to know what to fix.

## Configuration — changing which model a mode points at

Two places, depending on how permanent the swap is:

1. **One-off override** — pass `--model fal-ai/<slug>` (or `--model openai/<slug>`) at call time. Example: `--model fal-ai/veo3.1` to call Veo instead of Kling for a hero ad.
2. **Change the default** — edit the `MODEL_DEFAULTS` dict near the top of `.claude/skills/fal-image-gen/fal_run.py`. Each mode (`t2i`, `poster`, `i2i`, `t2v`, `i2v`) maps to one slug. Swap targets vetted by the team are listed inline in the comment above the dict; ai-creative-stack.md is the source of truth for which model wins each job in May 2026.

Common swap targets:

| Mode | Current default | Upgrade target | When to swap |
|---|---|---|---|
| `t2i` | `fal-ai/flux-2-pro` | `fal-ai/nano-banana-pro` (photoreal + legible text) or `fal-ai/nano-banana-2` (fast/cheap) | Hero shot that must carry small legible copy, or the best image we ship. Budget downgrade: `fal-ai/flux/dev`. |
| `poster` | `openai/gpt-image-2` | `fal-ai/nano-banana-pro` (Nano Banana Pro) | Devanagari festive creatives, or when you want a photo-real poster rather than a graphic one |
| `i2i` | `fal-ai/nano-banana/edit` | `fal-ai/nano-banana-pro/edit` (premium) or `openai/gpt-image-2/edit` (masked headline/price edit) | Premium edit fidelity, or surgical masked edits. Strength-knob Flux style transfer: `fal-ai/flux/dev/image-to-image`. |
| `t2v` | `fal-ai/kling-video/v3/standard/text-to-video` | `fal-ai/veo3.1` | One hero ad per quarter; Veo's $0.40/sec is ~5x Kling. Worth it for YouTube hero, not weekly Meta variants. |
| `i2v` | `fal-ai/kling-video/v3/standard/image-to-video` | `fal-ai/veo3.1/image-to-video` | Same rule — hero only |

If the param shape differs for a new model (e.g. Nano Banana Pro), the script may need an additional `build_*_args` branch. The existing branches show the pattern: read the model slug, pick the right argument map.

## Brand-aware prompts (caller's job)

This skill is dumb on purpose. The caller composes the prompt. A good prompt for a D2C brand bakes in:
- The specific SKU and its hero ingredients
- Brand mood and palette (from CLAUDE.md or `brand-brain/creative-direction.md`)
- The format target (ad, reel cover, PDP)
- Banned imagery as natural-language exclusions inside the prompt itself ("no tobacco, no spitting, no stained surfaces")

A bad prompt is generic ("a paan product photo"). A good prompt is specific ("Hand-rolled meetha paan on a brass plate, warm afternoon kitchen light, shallow depth of field, rose petals and slivered almonds visible, no tobacco, no spitting, no stained surfaces").

Canonical library: `references/module-6-performance-marketer/visual-prompt-templates.md`. Any caller composing a brand-aware prompt (the Performance Marketer agent, the `/creative-brief` skill, future visual-generating teammates) should pick one of the 8 shot templates and fill placeholders from CLAUDE.md rather than composing from scratch.

## Operating principles

- **One asset per call.** No batching. The caller loops if it needs multiple variants.
- **No prompt rewriting.** What the caller passes is what fal gets.
- **No retries.** Fal failures bubble up. The caller decides whether to retry.
- **No cost tracking.** Founders check the fal dashboard for billing. Video is meaningfully more expensive than image — start tests at `--duration 4s --resolution 720p` and scale up only on the winner.
- **PNG for image, MP4 for video.** Output format is determined by mode; the caller picks a file extension that matches.
- **Never silently install `uv`.** If the `uv run` call fails with `command not found`, surface the error to the founder, quote the install command from the Prerequisites section above, and ask permission before running it — even if the session is in `acceptEdits` or `bypassPermissions` mode. Installing a system tool is the founder's call.

## Future expansion (not yet built)

- `--mode poster-edit` for GPT Image 2's multi-turn edit on an existing poster ("change the price to 299, keep the layout"); will accept multiple `--reference` images per the model's up-to-16-input support
- `--check` mode for a vision-model brand-safety pass on a generated asset
- Batch-and-judge: generate N variants, run a vision-model rubric pass, return the best

These will be added when the loop proves it produces shippable output on real brand prompts.
