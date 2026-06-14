[← Back to Student Handbook](student-handbook.md)

---

# Session 6: Performance Marketer

**Skill unlocked:** Parallel subagent dispatch from the orchestrator. Your main session (the same one that spawned a single Content Lead in Session 4) spawns 5 subagents at once, one per ad angle, then aggregates their results. The pattern fits any "do N independent variants" job.

---

## What You'll Have After This Session

Three scopes. Pick one based on your stage and ad history.

| Scope | Time | Output | Who it's for |
|---|---|---|---|
| STARTER | ~3 min | 2 Meta ads + 1 Google headline set + 1 creative brief, 1 angle | 0-1Cr or first-time ad runner. One shippable ad beats five drafts. |
| DEFAULT | ~5 min | 10 Meta ads + 6 Google headlines + 4 descriptions + 2 briefs, 2 angles | 1-50Cr with some ad history. Pro plan. The workshop-slot default. |
| POWER | ~15 min | 50+ Meta ads + 25+ Google headlines + 5 briefs, 5 angles, parallel | Take-home default for everyone after the workshop. Max plan strongly recommended (parallel dispatch hits Pro rate limits). |

Plus a separate one-off creative brief skill you can fire any time for a single campaign idea.

---

## Before You Start

You need:
- CLAUDE.md saved
- Latest Market Analyst report
- Latest VoC report (ideally MCP-fed from Session 3)
- Latest Content Lead index (so the ads do not duplicate organic content)
- `brand-brain/ads/` populated with 3 to 5 winning ad screenshots or exports (if you have ad history). The subagent reads these as anchors. If you have no history, it runs cold-start and says so in the index.
- `brand-brain/voice-dna/` populated with 1 to 3 founder voice samples. The subagent pulls 5 to 10 verbatim phrases and reuses them literally in the ad copy. This anchors tone better than abstract voice rules alone.
- For Step 5 (visuals): `FAL_KEY` in `.env` at the repo root. (Step 5a walks the `uv` install if you do not already have it.) Skip Step 5 entirely if you only want the copy.
- Optional for Step 5 image-to-image (`i2i`) and image-to-video (`i2v`): `brand-brain/visual-refs/` populated with 1 to 5 approved reference images — your best-converting hero shot, a brand mood board, a winning ad screenshot you want to remix. Any PNG, JPG or WebP works. If you want to remix an existing ad rather than start fresh, reuse `brand-brain/ads/` as the reference source — both folders are valid `--reference` inputs. If neither folder exists yet, only `t2i` and `poster` work; the modes that need a reference image will fail with a clear "reference not found" error.

If CLAUDE.md, Market Analyst, VoC or Content Lead is missing or older than today, the subagent refuses to run. That is correct behaviour. Missing `brand-brain/ads/` or `voice-dna/` is a flag, not a refusal.

---

## Step 1: The parallel-dispatch demo (5 min, watch the instructor)

The instructor runs this on their screen, NOT in your terminal:

```
Run the Performance Marketer at SCOPE=power. Fan out one subagent per
angle in parallel, all 5 angles at once, then aggregate the five folders
into one index.
```

The key word is *fan out*. In Session 4 your main session (the orchestrator) spawned one Content Lead subagent via the Task tool. Here it does the same thing five times in one go, pinning each spawn to a single angle with `ANGLES=N`. You see five subagents start almost together in the run log:

```
[Task] performance-marketer  ANGLES=1  (hero SKU) ...
[Task] performance-marketer  ANGLES=2  (problem-solver) ...
[Task] performance-marketer  ANGLES=3  (anti-positioning) ...
[Task] performance-marketer  ANGLES=4  (social proof) ...
[Task] performance-marketer  ANGLES=5  (competitor gap) ...
... 5 subagents running in parallel ...
```

Five subagents at once. Run sequentially this would take roughly 5x as long. The orchestrator waits for all five, then aggregates their summaries into one index.

One honest caveat: the run is only as fast as its slowest child, and on a Pro plan some of the five may queue instead of all firing at the same instant, which eats into the time saving. The win is real, but it is not a guaranteed clean 5x.

Why the subagent does not spawn the five itself: a subagent cannot spawn subagents (Claude Code caps nesting at one level). Parallel dispatch therefore lives at the orchestrator, the one session that sits above all the subagents. That is the whole point of the primitive.

Why we do not all run POWER in the slot: five parallel subagents is roughly 5x the token cost, and Pro plans hit rate limits. We run DEFAULT here. POWER is your take-home run, once your rate limit has refreshed and you have a real campaign launching.

Detailed teaching: `references/module-6-performance-marketer/ad-angle-parallelism.md`.

---

## Step 2: The 5 ad angles (3 min)

Five canonical D2C ad angles. The Performance Marketer in DEFAULT picks the 2 strongest for your brand; in POWER it runs all 5 in parallel.

| # | Angle | Anchored on | When it lands |
|---|---|---|---|
| 0 | Read winners | `brand-brain/ads/` (your existing winning ads) | Always, if you have ad history. The subagent enumerates the files, notes hook style, length, format and CTA, then uses the pattern as an anchor for the angles below. New variants either match the pattern (safer A/B) or break one axis on purpose (a fresh probe). Without this, your winning patterns get ignored and premium tone drifts. |
| 1 | Hero SKU | CLAUDE.md top SKU + USP | Almost always. Every brand has a hero. |
| 2 | Problem-solver | VoC top theme that names a pain point | When VoC has a theme with 10+ messages on the same problem. |
| 3 | Anti-positioning | CLAUDE.md "what we will never do" | When your anti-positioning is genuinely brand-specific (not category cliche). |
| 4 | Social proof | VoC verbatim quote + persona card | When you have a real specific quote (not "5-star testimonial"). |
| 5 | Competitor gap | Market Analyst content gap line | When the gap is observable on competitors' websites and matters to your persona. |

Detailed shapes for each angle with worked examples (Little Lab): `references/module-6-performance-marketer/ad-angle-templates.md`.

---

## Step 3: Run Performance Marketer (~5 min)

Pick your scope:

- **STARTER** if you have never run paid ads or your revenue is under 1Cr. Goal is one shippable ad.
- **DEFAULT** for the workshop slot and for 1-50Cr founders with some ad history.
- **POWER** as take-home homework, run after the workshop when a real campaign is brewing.

Scope and angle choices live in the spawn prompt itself. The subagent runs in its own context and cannot pause to ask you mid-run, so if you omit scope it falls back to DEFAULT and picks angles deterministically. To run DEFAULT:

```
Spawn the Performance Marketer subagent with SCOPE=default for my brand.
```

Swap `SCOPE=default` for `SCOPE=starter` or `SCOPE=power` as needed. To force specific angles (numbers from the 5-angle list in Step 2), append `ANGLES=` to the spawn prompt:

```
Spawn the Performance Marketer subagent with SCOPE=default and
ANGLES=1,5 for my brand.
```

Before angle selection, the subagent reads `brand-brain/ads/` and `brand-brain/voice-dna/`. It writes a short "winners pattern" note (dominant format, hook style, length, CTA, recurring phrase) and a list of 5 to 10 verbatim voice anchors, both visible in the run log so you can see what it is anchoring on.

If you did not pass `ANGLES=`, the subagent auto-picks: DEFAULT gets 2 (likely Hero SKU + one of Problem-solver or Competitor gap), STARTER gets 1 (usually Hero SKU), POWER runs all 5. The hand-back message names the chosen angles on the first line, and the index file lists them too. If the picks are wrong, re-run the spawn prompt with explicit `ANGLES=<list>`.

DEFAULT and STARTER run sequentially inside one subagent. POWER is fanned out by the orchestrator: one subagent per angle, all 5 in parallel, then the orchestrator aggregates the folders into one index. Output shape (DEFAULT):

```
my-work/performance-marketer/<today>-angle-1-<slug>/
  meta.md           (5 Meta ads)
  google.md         (3 Search headlines + 2 descriptions)
  creative-brief.md
my-work/performance-marketer/<today>-angle-2-<slug>/
  meta.md
  google.md
  creative-brief.md
my-work/performance-marketer/<today>-index.md
```

STARTER produces one angle folder with 2 Meta ads, 1 Google headline set, 1 brief. POWER produces five angle folders.

Reply with a check in the workshop chat when your output is saved.

### Voice-fidelity gate

After ad generation, eyeball each ad against your `brand-brain/voice-dna/` samples. Anything that drifts from the founder voice goes on a flagged list. Founder reviews tone of flagged ads before push to ad accounts. For premium brands, treat any flagged ad as "do not ship", rewrite by hand using the verbatim voice anchors the subagent surfaced in Step 1. For mass-market brands the bar is lower but the flag still earns a second pass.

---

## Step 4: Run the creative brief skill (~2 min)

The Performance Marketer subagent is for batch work. For one-off campaign ideas, use the lightweight `creative-brief` skill.

Try it:

```
Write a creative brief for a Mother's Day campaign on Instagram, around
our hero SKU.
```

The skill autoloads (description matches "creative brief"), reads CLAUDE.md and VoC, asks one clarifying question if needed, produces:

```
my-work/performance-marketer/briefs/<today>-mothers-day.md
```

The brief is ready to paste into Midjourney / DALL-E or hand to your design team. AI image prompt is at the bottom.

This is the lightweight tool. Use the subagent for batch, the skill for one-off briefs. They live alongside each other.

---

## Step 5: Generate the visuals (~3 min)

Every `creative-brief.md` produced in Steps 3 and 4 ends with an AI image prompt. This step turns those prompts into shippable assets via the `fal-image-gen` skill, so each ad ships with its own visual instead of a placeholder.

The skill picks the right model for the job:

| Brief surface | Mode | Model | Cost (May 2026) |
|---|---|---|---|
| Lifestyle, hero, product-in-scene (Meta feed, PDP) | `t2i` | Flux dev | ~$0.012 to $0.05 per image |
| Festive poster, sale card, anything with rendered text | `poster` | GPT Image 2 (OpenAI Images 2.0) | $0.04 to $0.35 per image |
| Variant of an approved hero in the same brand world | `i2i` | Flux dev i2i | ~$0.012 to $0.05 per image |
| Short ad video, reel hero, B-roll | `t2v` | Kling 3.0 Standard | ~$0.084 per second |
| Animate an approved still into 6s motion | `i2v` | Kling 3.0 Standard i2v | ~$0.084 per second |

We default video to Kling 3.0 (the "Efficient" tier in `ai-creative-stack.md`) rather than Veo 3.1 because Veo runs ~5x the cost and earns its keep only on the one hero asset per quarter. If a brief explicitly calls for Veo, the skill accepts `--model fal-ai/veo3.1` per-call. Same pattern for the poster: if the brand needs Devanagari typography at magazine quality, override with Nano Banana Pro (`--model fal-ai/gemini-3-pro-image`).

To swap a default permanently, edit `MODEL_DEFAULTS` near the top of `.claude/skills/fal-image-gen/fal_run.py`. Every Friday or after a new model release, re-check `ai-creative-stack.md` Section 1 (video), Section 2 (image) and Section 3 (poster) for the current Best/Efficient/Third tiers and update.

Detailed teaching: `references/module-6-performance-marketer/visual-prompt-templates.md` covers the 8 universal D2C shot templates (product hero, hands-and-craft, lifestyle, gifting, ingredient, founder, packaging, social tile), the 5 reel beats and how to fill every `{placeholder}` from CLAUDE.md. The Performance Marketer and `/creative-brief` both compose against this library. The social-tile template ships through `poster` mode; the other seven still templates ship through `t2i`.

### 5a. Install `uv` (one-time, ~30 sec)

The `fal-image-gen` script is a single Python file that declares its dependencies inline (PEP 723). `uv` is the runner that reads those declarations, creates a per-script venv on first call and installs `fal-client` automatically. After this one-time install, every `uv run` is instant.

- **macOS**: `brew install uv`
- **Windows**: `winget install --id=astral-sh.uv -e`
- **Anything else**: see https://docs.astral.sh/uv/getting-started/installation/

Skip if `uv --version` already prints a version. You also need a `FAL_KEY` line in `.env` at the repo root — get one at https://fal.ai/dashboard/keys.

### 5b. Run the generation

Scopes mirror Step 3:

| Scope | Variants per brief | Workshop DEFAULT total (2 briefs) | Rough cost |
|---|---|---|---|
| STARTER | 1 | 1 | ~$0.05 |
| DEFAULT | 2 (safer + bolder reading of the same brief) | 4 | ~$0.20 |
| POWER | 4 (different art directions of the same brief) | 20 across 5 angles | ~$1 |

To run:

```
Generate visuals for today's creative briefs at SCOPE=default.
```

Claude walks every brief in `my-work/performance-marketer/<today>-*/` plus the one-off brief from Step 4, then calls `fal-image-gen` once per variant. Aspect ratio comes from each brief: Meta feed = 4:5, story or reel cover = 9:16, square placement = 1:1. Mode comes from the brief's shot template: social tile (text-on-image) → `poster`; everything else with a still → `t2i`; when a brief asks for a variant of an existing approved hero (drop a new SKU into the same brand world) → `i2i` with that hero as `--reference`; reel hero or B-roll with motion → `t2v`; animate an approved still → `i2v`.

**One trap to know about i2i.** If the reference image has rendered text on it (a headline, a badge, a brand mark — common when remixing a competitor's ad), Flux dev i2i at low strength tries to *preserve* those letter shapes and produces garbled text. The fix is either to run i2i at `--strength 0.85` or higher (which drops the reference text cleanly so you composite real copy in Figma after), or to abandon the reference and use `--mode poster` (GPT Image 2) with the headline written verbatim into the prompt. SKILL.md "Strength knob and rendered text" has the worked example.

Output shape (DEFAULT):

```
my-work/performance-marketer/<today>-angle-1-<slug>/
  meta.md
  google.md
  creative-brief.md
  visuals/
    v1-safer.png
    v2-bolder.png
```

The index file from Step 3 gets a new `## Visuals` section listing each generated PNG so you can scan all variants in one place.

Reels are in the loop via `--mode t2v` and `--mode i2v` (Kling 3.0 Standard by default). Start every video test at `--duration 4s` and only re-render the winner at `--duration 6s` or `--duration 8s` — Kling charges per second. For the one hero ad per quarter where Veo's quality earns its price, append `--model fal-ai/veo3.1` to the call.

### Visual-fidelity gate

Eyeball each image against the brief's must-include and must-avoid lists, plus the "what we will never do" rules from CLAUDE.md (banned imagery, banned props, banned aesthetics). For premium brands, regenerate any image that drifts from brand mood — wrong palette, wrong era, props the brand has explicitly banned. One regeneration with a tightened prompt usually fixes it; if the third try still drifts, the brief itself is the problem, not the model.

---

## Step 6: Read the index, pick the ships (5 min)

Open `my-work/performance-marketer/<today>-index.md`. Walk the Top 5 reads. Identify:

- The single Meta ad ready to ship to your ad account this week (no flags, strong hook, clear creative brief, matching visual that survived the fidelity gate)
- The single Google search ad set ready to upload
- The brief most ready to hand to your design team (or the visual most ready to upload as-is)

Tell yourself: two angles, six ad files, two briefs. Do not edit all of them. Pick **one** Meta ad set and **one** Google ad set this week. Test, learn, re-run next week.

The Performance Marketer is not a one-shot creative agency. It is a weekly creative bench.

---

## What You Just Built

Real ad copy on your real brand, biased toward the angles your data says will land. Plus you saw the orchestrator-level parallel-dispatch primitive demonstrated. The POWER run is yours to take home; the pattern is yours to reuse for any "do N variants" job.

---

## What's Next

Session 7 connects the live read-write loop. Read live Shopify conversion data, find which PDP under-converts, rewrite, push to draft, measure. Plus a deeper marketplace pass than the Content Lead's first draft.

[Continue to Session 7: Storefront + Marketplace →](session-7-storefront-marketplace.md)

---

## Power-ups

Optional add-ons that extend this agent beyond the workshop hour. None are needed for the live build.

### Voice-fidelity gate (post-workshop add-on)

**What this fixes.** Voice drift in unattended POWER runs. When you generate 50+ ads across 5 angles without sitting next to the output, generic AI mush slips through. Eyeballing 50 ads is unrealistic.

**Who it's for.** Anyone running POWER scope take-home. Mandatory for premium brands where tone drift costs brand equity. Optional for mass-market brands.

**The build.** Adds a Step 5b to `performance-marketer.md` between brand-safety and index. The subagent scores each ad 1 to 5 against `brand-brain/voice-dna/` samples: does the ad reuse at least one verbatim "always" phrase, does the tone match the longest sample, does it avoid the banned-word patterns from voice rules. Anything 3 or below gets written to a `## SAFETY FLAGS` section at the bottom of the ad file with the ad ID, the score and the specific failure mode. Index counts flags. Parent surfaces flag count in hand-back so the founder reviews flags only, not every ad.

**How to know it worked.** Run on a known-bad set of generic AI ads, confirm flag count > 0. Run on existing winners from `brand-brain/ads/`, confirm flag count = 0.

**Failure modes.** Voice-DNA samples under 100 words give the rubric nothing to anchor on. Premium-brand calibration needs a stricter threshold (flag at 4 instead of 3). Hand-back protocol must surface flags to the orchestrator, not just save them silently.

**Build time.** 30 to 45 minutes.

---

## If You Get Stuck

| Symptom | Fix |
|---|---|
| Subagent refuses with "missing input" | Re-run the missing prerequisite session. |
| Ads sound generic | CLAUDE.md voice rules section is thin and `brand-brain/voice-dna/` has no verbatim samples. Add 2 to 3 founder samples to voice-dna/, re-run. The verbatim phrases anchor tone better than abstract rules. |
| 0-1Cr founder, no ad history, nothing in `brand-brain/ads/` | Run STARTER scope. The subagent treats it as cold start and says so in the index. Goal is one shippable ad to test, not coverage. Anchor on Hero SKU and the strongest VoC theme you have. |
| Premium brand, tone is non-negotiable | Make sure `brand-brain/voice-dna/` has 3+ samples and that `brand-brain/ads/` has your highest-tone existing winners. After the run, check the voice-fidelity flags first, not the brand-safety flags. Any ad scoring 3 or below: do not ship, rewrite by hand using the voice anchors. |
| Ads duplicate Session-4 organic content | Re-run with: "exclude themes already covered in my-work/content-lead/<date>-index.md". |
| Pro user hits rate limit | You tried POWER on Pro. Run DEFAULT. Run POWER on Monday after quota resets. |
| POWER had 1 child fail | The orchestrator aggregates the 4 that succeeded and flags the 1 that failed. Re-run just that angle later with a tighter prompt. |
| Compliance flags on every ad | Regulated category, every angle touches a claim. Read flags as a "what needs proof" list. Edit ads or get substantiation. |
| Winners pattern looks wrong | The subagent inferred patterns from `brand-brain/ads/` filenames or low-res screenshots. Tell it: "ignore the inferred winners pattern, re-run with this pattern instead: <one line>". |
| Step 5 errors with `uv: command not found` | Re-run Step 5a. After install, open a fresh terminal so `uv` is on your `PATH`. |
| Step 5 errors with `FAL_KEY not found` | Copy `.env.example` to `.env` at the repo root, paste your key from https://fal.ai/dashboard/keys, save. |

For anything not on this list, raise hand in the workshop chat.
