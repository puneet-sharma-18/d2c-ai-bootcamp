# Visual prompt templates - D2C creative library

Shared library for any teammate composing AI image prompts: the `creative-brief` skill, the `performance-marketer` agent, future storefront and marketplace teammates. Brand-agnostic by design. Placeholders are filled from the brand's `CLAUDE.md`.

The library exists because each teammate was composing prompts ad-hoc, which produced inconsistent output and did not transfer across brands. With this library, a Paan brand and a baby-skincare brand get the same shot-type taxonomy, the same camera language and the same negative prompt, with only the brand-specific slots changing.

## How to use

1. Read `CLAUDE.md` for the brand
2. Pick the shot template that matches the brief's surface (see mapping below)
3. Fill every `{placeholder}` from `CLAUDE.md`. If a placeholder has no clear source, ask the founder one targeted question. Do not invent.
4. Append the universal negative prompt
5. Hand the result to `fal-image-gen`

Each composed prompt is one paragraph. One shot per prompt. Do not stack two shot types in a single prompt.

## The core template

Every image prompt fills the same eight slots, in this order:

```
A {subject} {action}, {setting}, {lighting}, shot on {camera + lens},
{composition}, in the style of {reference}, {one_emotion} mood,
{aspect_ratio}
```

What changes between brands is what gets dropped into each slot, not the slot itself.

## Mapping surface to shot

| Surface | Shot template | fal-image-gen mode |
|---|---|---|
| Meta feed ad | Product hero OR Lifestyle in-use | `t2i` |
| Meta story or reel cover | Lifestyle in-use OR Founder portrait | `t2i` |
| Square placement | Product hero | `t2i` |
| PDP hero (Shopify) | Product hero | `t2i` |
| Banner with headline added in post | Social tile 8a | `t2i` |
| Festive poster with rendered headline | Social tile 8b | `poster` |
| Packaging mockup or "what you get" image | Packaging mockup | `t2i` |
| Origin or how-it's-made post | Hands-and-craft | `t2i` |
| Festive or gifting ad | Gifting or occasion | `t2i` (or `poster` if the box label is the focus) |
| Ingredient education post | Ingredient story | `t2i` |
| Founder reel cover or About page hero | Founder portrait | `t2i` |
| Variant of an approved hero in the same brand world | (reuse any shot above) | `i2i` |
| Reel video, ad hero | The 5 reel beats below | `t2v` |
| Animate an approved still | (reuse any shot above) | `i2v` |

If the surface is not listed, pick the closest match and note the substitution in the brief's "Why this shot" line.

## The 8 universal shots

### 1. Product hero
The default for PDPs, feed ads and any "this is the product" moment.

```
A {product} resting on {surface_matching_brand_world},
{key_ingredient_or_material} scattered around it,
{lighting_direction} window light, shot on Hasselblad H6D 100mm macro f/2.8,
top-down composition, in the style of {editorial_reference},
{one_emotion} mood, 4:5
```

Use when the founder wants the product as the unmistakable subject.

### 2. Hands-and-craft
For "how it's made" content. Sells process and care without claims.

```
Close-up of {persona_hands} {making_action} {product_component},
soft side light from {direction}, shot on 50mm f/1.4,
shallow depth of field, in the style of {documentary_photographer},
reverent mood, 1:1
```

Use when the brand has a craft story the category usually skips.

### 3. Lifestyle in-use
The candid moment of use. Best for story ads and reel covers.

```
{persona_description} {using_product} in {natural_setting_for_category},
{time_of_day} light, candid posture, shot on 35mm f/2.0,
in the style of Kinfolk magazine, {emotion} mood, 4:5
```

Use when the brand needs to show the persona, not the product.

### 4. Gifting or occasion
For festive ads, corporate gifting, wedding-season pushes.

```
{product_packaging} opened mid-frame, {occasion_context_props} around it,
overhead light from soft north window, shot on 50mm f/4,
in the style of Cereal magazine, {emotion} mood, 1:1
```

Use during Diwali, weddings, Christmas, Eid, Rakhi or any moment the box itself becomes the gift.

### 5. Ingredient story
Single-ingredient close-up. Sells the "why this is different" without text.

```
Single {key_ingredient} isolated on {complementary_texture},
raking side light, shot on 100mm macro,
in the style of Bon Appetit ingredient series, reverent mood, 1:1
```

Use when the brand has one ingredient worth a full frame.

### 6. Founder portrait
The face behind the brand. About page, founder reels, trust ads.

```
{founder_first_name}, founder of {brand}, {natural_environment_to_brand},
three-quarter portrait, soft window light from left, shot on 85mm f/1.4,
in the style of Platon portrait series, direct mood, 4:5
```

Use when trust is the conversion blocker.

### 7. Packaging mockup
"This is what arrives." Hands holding the unboxed item.

```
{product_packaging} held in hand against {brand_world_background},
{time_of_day} light, shot on 50mm f/2.0,
in the style of Monocle product features, {emotion} mood, 1:1
```

Use for ads selling the unboxing experience.

### 8. Social tile (with headline space)
Posters, billboards, banners. Two flavours depending on whether the model should render the headline itself.

**8a. Negative-space tile** (text added in Figma or Canva over the image). Use Flux via `t2i` mode.

```
{product} positioned lower-right third of frame,
negative space upper-left for headline copy, even soft daylight,
shot on 50mm f/5.6, flat composition,
in the style of muji catalogue, calm mood, 4:5
```

**8b. Typography-first poster** (headline rendered by the model). Use GPT Image 2 via `poster` mode. Put the headline in quotes so the model renders it verbatim. Devanagari, English and most Indic scripts work; for Tamil, Bengali, Punjabi, Gujarati, Odia, Malayalam, Kannada, fall back to 8a and overlay in a real design tool.

```
Headline "{headline_verbatim_in_quotes}" rendered in {typography_mood}
at upper-third of frame, {product} positioned lower half,
{brand_world_background}, {one_emotion} mood, 4:5
```

For 8b, pull `{headline_verbatim_in_quotes}` from the brief's hook line or the brand's verbatim phrases in `brand-brain/voice-dna/`. `{typography_mood}` examples: "block sans-serif white", "ornate Devanagari title in gold", "hand-lettered serif". Never use "elegant", "premium" or "stunning" as typography descriptors.

Use 8a when text will be added over the image in post. Use 8b when the brand calendar is festival-heavy and you need 10+ posters a week without a designer in the loop.

## The 5 reel beats

`fal-image-gen` is text-to-image only today. These beats define what each still in a reel storyboard should be, so a reel editor (or future text-to-video skill) has a structured shot list.

```
{shot_type} of {subject_action}, {camera_move} over {duration_seconds},
{lens}, {lighting}, in the style of {film_reference},
audio: {sound_design}, {aspect_ratio} {framerate}
```

The 5 beats every D2C reel storyboard needs at least one of:

1. **Make it.** Hands crafting the product. Slow push-in, 3 seconds, 50mm macro.
2. **Use it.** The moment of consumption or wear. Static hold, 2 seconds, 35mm.
3. **Open it.** Unboxing close-up. Overhead static or slow rotate, 2 seconds, 50mm.
4. **Founder line.** Founder talking to camera, ambient sound only, no background music. 5 to 8 seconds, 50mm.
5. **Before and after.** State change where the category allows (skincare, fitness, food prep). 2 + 2 seconds, hard cut between.

A 15-second reel typically chains 3 to 4 of these. A 30-second reel chains all 5.

## Reading CLAUDE.md for placeholders

| Placeholder | Where in CLAUDE.md to look |
|---|---|
| `{product}` | Section 4 product table. Describe the product's defining **visual form**, not its name. Wrong: "Almond Delight paan". Right: "hand-folded paan parcel from a glossy dark green betel leaf, filling visible at the open edge". The model knows what a betel leaf is; it does not know what "Almond Delight" looks like. This applies to every category. Wrong: "Glow Serum". Right: "amber glass dropper bottle with a black pipette". Wrong: "Morning Granola". Right: "loose cluster of toasted oats, almond slivers and dried cranberry". |
| `{brand_world}` | Section 3 anti-positioning + Section 4 ingredients + Section 7 voice rules. Synthesise into a one-line visual universe ("brass and wood with rose petals", "linen and botanicals on travertine", "concrete and steel"). |
| `{persona_hands}` | Section 5 customer. Age, gender, life stage. Match the hands to the persona, not the founder. |
| `{persona_description}` | Section 5 customer. One line describing who they are, not what they do. |
| `{reference_aesthetic}` | Section 7 voice rules + the competitor table's "where we beat them" column. Pick 2 to 3 magazines or photographers that share the brand's anti-positioning, never direct competitors. |
| `{emotion}` | Brand voice's "always" words. Pick one. Quiet, reverent, tender, defiant, calm, joyful, exact. Never "premium" or "beautiful". |
| `{banned_visuals}` | Section 3 anti-positioning + Section 7 "never" rules. These become explicit exclusions in the prompt. |
| `{key_ingredient}` | Section 4 product table. Use the named ingredient from the SKU's USP line. |
| `{founder_first_name}` | Section 1 founder identity. |
| `{brand}` | Section 2 brand basics. |

If three or more placeholders have no clear source, the brand's CLAUDE.md is too thin for visual generation. Tell the founder which sections to expand before composing.

## Universal negative prompt

Append to every prompt before sending to `fal-image-gen` (Flux, SDXL, Ideogram all respect this):

```
no text, no watermark, no logo, no extra fingers, no plastic skin,
no oversaturation, no stock-photo lighting,
no white background unless specified,
{banned_visuals_from_claude_md}
```

`{banned_visuals_from_claude_md}` is the brand-specific exclusion list. For Paan: "no tobacco, no spitting, no stained surfaces". For a baby brand: "no stock baby photos, no soft-focus pastels, no leafy backgrounds". Pull verbatim from the brand's "never" rules.

## Language that lands with the model

Diffusion models read material and form better than they read names. When a placeholder pulls a culturally-specific or brand-coined term from CLAUDE.md, translate it to plain visual terms before slotting in.

| Term in CLAUDE.md | What to write in the prompt |
|---|---|
| brass thali | polished brass plate, warm golden reflective surface |
| terracotta diya | small fired-clay oil lamp, matte rust-orange surface |
| Banarasi silk backdrop | deep red woven silk with gold zari thread border |
| Marwari haveli interior | warm sandstone arches, ochre walls, low brass light |
| Goan pao | rustic bread roll with crackled golden crust |

The pattern: name the material, the colour, the form. The model converges fast on those three. Brand-coined product names ("Almond Delight", "Glow Serum") never land; they only describe to humans. Always translate.

## Operating principles

- **One shot per prompt.** Stacking templates produces confused output.
- **Light first, subject second.** "Soft side light from a north window" outperforms "good lighting" every time.
- **Camera specs sell realism.** "Shot on Phase One IQ4, 80mm f/2.0" beats "professional photo". Flux and Ideogram both respond.
- **Reference real photographers and magazines.** Specific names ground the model. Avoid "cinematic", "premium", "beautiful". These are dead words.
- **One emotion word.** Quiet, reverent, tender, defiant. Not "amazing" or "stunning".
- **Banned visuals go in the prompt literally.** Do not assume the model knows what the brand will not show.
- **If the third regeneration still drifts, the brief is wrong.** Fix the brief or the CLAUDE.md, not the prompt.
