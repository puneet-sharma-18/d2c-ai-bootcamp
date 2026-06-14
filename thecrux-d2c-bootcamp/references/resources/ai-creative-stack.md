[← Back to Resources](resources.md)

---

# AI Creative Stack for D2C Ads

**Verified as of 2026-05-16.** Sources: vendor pages, Reddit (r/StableDiffusion, r/SunoAI, r/ElevenLabs, r/aivideo, r/midjourney, r/marketing), X.com and independent reviews from the four weeks of April 18 to May 16, 2026. Source URLs are linked inline below; re-verify any price before a procurement decision.

This page is one of three siblings. [`ai-native-d2c-stack.md`](ai-native-d2c-stack.md) covers the operating spine (commerce, support, reviews, WhatsApp, lifecycle, attribution, fulfilment, orchestration). [`claude-skills-stack.md`](claude-skills-stack.md) covers the skills you install into Claude Code to run all of it. This page covers the creative bench that produces pixels and audio.

The Performance Marketer and Content Lead teammates compose briefs. They do not produce the final pixel. This page is the curated list of models that produce the actual shippable asset: a video, a poster, a voice over, a founder talking head.

The rule: pick by the job, not by the brand. The same Indian D2C founder will run Nano Banana Pro for the Diwali poster, Flux 2 for the PDP, Kling 3.0 for the Reel hero, Sarvam Bulbul V3 for the Hindi VO and Sync.so Lipsync-2-Pro for the dubbed founder reel. One model rarely covers a campaign end to end.

Three tiers per category:

1. **Best**: top output quality, cost is not the decision criterion.
2. **Efficient**: close enough to Best on quality, three to ten times cheaper, fits a daily creative pipeline.
3. **Third**: picked for a specific job the first two miss (Indian faces, regional languages, vector output, open weights, lip-sync on real footage).

Every model below is reachable from India in May 2026 unless flagged otherwise. Pricing is the vendor's published number as of mid-May 2026, before forex and bank markup.

---

## 1. Video ads (Reels, YouTube, Display)

| Tier | Model | Why it wins now | India access | Cost |
|---|---|---|---|---|
| **Best** | **Google Veo 3.1** | Native synced audio + dialogue, broadcast-grade color, best prompt adherence in side-by-sides per WaveSpeed and r/aivideo. Hero brand films. | Yes. Google AI Plus India ₹1,250/mo (Dec 2025 launch) covers Gemini Veo 3.1. | $0.40/sec Standard, $0.15/sec Fast, $0.05/sec Lite (Vertex/Gemini API). fal/Replicate from ~$0.10/sec Fast. |
| **Efficient** | **Kling 3.0** (Kuaishou) | Released Feb 7, 2026 (renamed from "Kling 2.5/2.6"). r/aivideo consensus for "footage that looks filmed not generated". Native audio + multi-shot in O3 tier. | Yes. fal.ai, Replicate, Kuaishou web. | fal API $0.084/sec Std, $0.112/sec Pro. Subs $6.99-$25.99/mo entry. |
| **Third** | **MiniMax Hailuo 02 Pro** | Cheapest "good enough" for variant testing. $0.28 per 1080p 10-sec clip. Used to burn 20-50 hook variants before promoting winners. | Yes. fal.ai, MiniMax direct. | fal $0.08/sec Pro 1080p, $0.045/sec Std 768p. |

**Sources:**
- Veo 3.1 pricing: https://www.veo3gen.app/blog/veo-3-1-pricing-plans
- Veo 3.1 India: https://www.truefan.ai/blogs/google-veo-availability-india-2026
- Kling 3.0 release: https://blog.fal.ai/kling-3-0-is-now-available-on-fal/
- Comparison: https://wavespeed.ai/blog/posts/seedance-2-0-vs-kling-3-0-sora-2-veo-3-1-video-generation-comparison-2026/
- Hailuo 02: https://ucstrategies.com/news/hailuo-02-1080p-ai-video-at-0-28-specs-benchmarks-pricing-2026/

**Honourable mentions (May 2026):**
- **Seedance 2.0** (ByteDance, Dreamina) gaining ground for stylised cuts. https://aivideobootcamp.com/blog/ai-video-generators-ranked-2026/
- **Wan 2.7** (Alibaba, Apache 2.0, released Apr 1-6, 2026). Four-model open-source suite with reference-to-video + voice cloning. Self-host if brand-asset control matters. https://www.cliprise.app/news/wan-2-7-video-release
- **Runway Gen-4 Aleph**, **Luma Ray 2**, **Pika 2.2** all credible, none currently in any tier above for an India D2C founder.

**Recent shake-ups:**
- **Sora 2 consumer app sunset on Apr 26, 2026.** API live until Sep 24, 2026. https://www.glbgpt.com/hub/openai-sora-2-availability/ India: not officially available, requires VPN + non-Indian card. https://www.glbgpt.com/hub/openai-sora-2-availability-in-india-how-to-access-sora-2-today/
- **Veo 4 watch:** Google I/O on May 19-20, 2026 is the consensus reveal window. Not announced as of May 16. [unverified until I/O]

**Rule of thumb:** Start every video test at the Efficient tier in 720p, 4 seconds. Only upgrade the winner to Best in 1080p, 8 seconds. Veo at full settings costs more per second than a freelance editor.

---

## 2. Image ads (lifestyle, hero, product-in-scene)

| Tier | Model | Why it wins now | India access | Cost |
|---|---|---|---|---|
| **Best** | **Nano Banana Pro** (Gemini 3 Pro Image) | Launched March 2026. r/midjourney and Pixeldojo writeups: 4K skin texture, individual hair strands, broadcast portrait quality. The new default for PDP hero and editorial product-in-scene. | Yes. Gemini app, Google One AI Premium INR billing, Vertex/Gemini API takes Indian cards. | $0.134/image standard, $0.24/4K via API. AI Premium $20/mo. |
| **Efficient** | **Flux 2 family** (Black Forest Labs) | Released Nov 25, 2025. Tiers: Max, Pro, Flex, Dev, Klein. Multi-reference identity stability + brand-color hex codes. Flux 2 Dev is the only tier with LoRA fine-tune support. **Flux 1.1 Pro Ultra is deprecated.** | Yes. fal.ai, Replicate, WaveSpeed. | fal $0.07 Max, $0.06 Flex, $0.03 Pro, $0.012 Dev. |
| **Third** | **Seedream 4.5** (ByteDance) + **Flux 2 Dev with Desi Mocha LoRA** | Seedream tuned on Asian-face data, better Indian-face defaults than Midjourney or Nano Banana out of the box. Desi Mocha LoRA on Civitai (April 2025, v3) is the repeatable Indian-persona route. | Yes. fal, RunComfy, ImagineArt. | Per-MP pricing similar to Flux Pro. Desi Mocha LoRA free on Civitai. |

**Sources:**
- Nano Banana Pro: https://blog.google/technology/ai/nano-banana-pro/ and https://pixeldojo.ai/nano-banana-2-skin-texture-realistic
- Flux 2: https://bfl.ai/models/flux-2 and https://wavespeed.ai/blog/posts/flux-2-complete-guide-2026/
- Seedream 4.5: https://seed.bytedance.com/en/seedream4_5
- Desi Mocha LoRA: https://civitai.com/models/681060/desi-mocha-lora-for-indian-south-asian-faces-flux-1d-experimental

**Recent shake-ups (Apr 18 to May 16, 2026):**
- **Midjourney V8.1** shipped Apr 30, 2026. 2K HD native, 4-5x faster, returns to V7 aesthetic after V8.0 was called "broken" on r/midjourney. Still no API. Indian-face bias remains documented. https://felloai.com/midjourney-v8-1-review/
- **GPT Image 2 (OpenAI Images 2.0)** shipped Apr 21, 2026. Reasoning before drawing, 4096x4096, up to 16 reference images, Indic-script in-image (Hindi, Bengali). API $0.04 to $0.35/image; Batch API halves cost. https://openai.com/index/introducing-chatgpt-images-2-0/
- **Krea 2 (K2)** launched May 12, 2026. Krea's first in-house foundation model, moodboard-driven style, 15 sec generation. https://www.krea.ai/krea-2
- **HiDream-O1-Image** (early May 2026, open weights). Highest-ranked open-weights model on the Artificial Analysis arena. Watch for self-hosted ad pipelines. https://huggingface.co/HiDream-ai/HiDream-O1-Image

**Rule of thumb:** Build a brand LoRA on Flux 2 Dev once, using 15 to 25 photos of your hero SKUs. Every PDP and ad image from then on runs through that LoRA at $0.012/image. Reserve Nano Banana Pro for the four to eight hero shots per quarter where the extra texture justifies the price.

---

## 3. Text posters and typography ads (festive, sale, quote cards)

This category is separate because lifestyle image models cannot render legible text. The Indian D2C calendar is festival-heavy (Diwali, Rakhi, Wedding season, Pongal, Onam, Republic Day) and most of those creatives are typography-first.

| Tier | Model | Why it wins now | India access | Cost |
|---|---|---|---|---|
| **Best** | **Nano Banana Pro** (Gemini 3 Pro Image) | The only mainstream model with primary-source vendor claim to legible **Devanagari, Chinese, Arabic, Cyrillic** in-image. "Best model for creating images with correctly rendered and legible text directly in the image." Magazine-quality typography per April-May reviewers. | Yes (same as above). | $0.134 std, $0.24 4K. |
| **Efficient** | **Ideogram 3.0** | Still the workhorse for English-script festive posters and sale banners. ~90-95% text accuracy vs Midjourney's 30-40%. Conversational tweaks via Ideogram Canvas. | Yes. ideogram.ai, Segmind. | Turbo $0.03, Default $0.06, Quality $0.09. |
| **Third** | **Recraft V4** | Only model producing native SVG with editable paths. Critical when one Diwali creative ships as Meta 1:1, Amazon 1500x300, Zomato 16:9 and a print standee. Tops HF Text-to-Image Arena over MJ V8 and Flux. | Yes. recraft.ai. | ~$0.04/image, Pro $25/mo. |

**Conversational-editing pick: GPT Image 2** (released Apr 21, 2026). Text accuracy reportedly jumped to ~99%. Multi-turn edits via Responses API: "change the price to 299, keep the layout" works. Catch: every reference image bills at high-fidelity input rate, iterative workflows run 2-3x the quoted cost. https://wavespeed.ai/blog/posts/gpt-image-2-pricing-2026/

**Devanagari and Indian script rendering**
- **Nano Banana Pro** is the only model with a primary-source vendor claim for legible Devanagari. https://blog.google/innovation-and-ai/products/nano-banana-pro/
- **GPT Image 2** claims strong Indic in-image text but no Devanagari-specific benchmark surfaced.
- **Tamil, Telugu, Bengali, Punjabi, Gujarati, Odia, Malayalam, Kannada:** no model reliably renders legible output as of May 2026. Plan to layer text in Figma or Canva over an AI background. [unverified for any current model]

**Sources:**
- Ideogram 3.0: https://about.ideogram.ai/3.0 and https://blog.segmind.com/ideogram-3-0-on-segmind-features-api-pricing-and-use-cases/
- Recraft V4: https://www.recraft.ai/blog/what-makes-recraft-the-best-ai-image-generator-with-text
- GPT Image 2: https://developers.openai.com/api/docs/models/gpt-image-2

**Rule of thumb:** For Devanagari festive creatives, Nano Banana Pro. For English-script daily poster pipeline, Ideogram. For marketplace banner resizing across formats, Recraft V4 SVG. The three together cover 90% of typography work.

---

## 4. Voice over and dubbing

| Tier | Model | Why it wins now | India access | Cost |
|---|---|---|---|---|
| **Best** | **ElevenLabs v3** (GA Feb 2, 2026) | Out of alpha. 70+ languages, audio tags ([excited], [sighs], [whispers]), Text-to-Dialogue. Voice cloning: IVC from 1-5 min, **PVC needs 30 min minimum for founder-grade output**. | Yes, USD billing, Indian cards. | API ~$0.10/1K chars Multilingual, ~$0.05/1K chars Flash. Plans Free, Starter $5, Creator $22, Pro $99, Scale $330. |
| **Efficient** | **Cartesia Sonic-3** (Oct 2025, current May 2026) | 90ms model latency, ~190ms end-to-end. 42 languages. Voice clone from 3-sec clip. Blind A/B tests favoured Sonic-2 over ElevenLabs Flash 61.4% to 38.6%; Sonic-3 extends the lead at lower cost. The "30 reel cuts a week" workhorse. | Yes, USD. | Growth plan ~$49/mo for ~250K credits. |
| **Third** | **Sarvam Bulbul V3** (released Feb 5, 2026) | **The right call for Hindi, Tamil, Telugu, Bengali, Marathi, Kannada, Gujarati, Punjabi, Odia, Malayalam, Indian-English.** Josh Talks blind A/B (500+ annotators): "clear top performer across all competitors" at 8 kHz, competitive with ElevenLabs v3 in full-band. Genuine native Indic prosody, not transliterated English. | Yes, native INR billing. | ₹30 per 10,000 chars (₹0.003/char, ~one-third of ElevenLabs Multilingual). |

**Sources:**
- ElevenLabs v3 GA: https://elevenlabs.io/docs/changelog/2026/2/2 and review https://inworld.ai/resources/elevenlabs-v3-review
- Cartesia Sonic-3: https://docs.cartesia.ai/build-with-cartesia/tts-models/latest and https://aws.amazon.com/about-aws/whats-new/2026/02/cartesia-sonic-3-on-sagemaker-jumpstart/
- Sarvam Bulbul V3: https://www.sarvam.ai/blogs/bulbul-v3 and https://yourstory.com/ai-story/sarvam-ai-bulbul-v3
- Bulbul vs ElevenLabs honest comparison: https://medium.com/@LakshmiNarayana_U/indias-bulbul-wants-to-out-sing-elevenlabs-i-put-it-to-the-test-985533177223

**Recent shake-ups:**
- **Hume Octave 2** (early May 2026). ~100ms latency, 15-sec clone, "roughly half ElevenLabs' price." More emotional, less stable; better for character VO than 30-sec hard-sell ads. https://www.hume.ai/blog/octave-2-launch
- **Smallest.ai AWAAZ** (Indian). 5-sec clone, 200ms streaming, strong Hindi/Tamil. Worth piloting alongside Sarvam if you need 5-sec cloning. https://smallest.ai/text-to-speech
- **OpenAI gpt-4o-mini-tts** holds at ~$0.015/min for placeholder VO. No cloning, 13 fixed voices. Useful for scratchpad only.

**Honest Sarvam vs ElevenLabs call:**
- **Pure Hindi, Marathi, Bengali, Tamil** that does not sound like an English speaker reading transliterated script: **Bulbul V3 wins.** Both Josh Talks third-party study and independent Medium tester (Lakshmi Narayana U) confirm this.
- **Hinglish (Mumbai/Pune/Bengaluru women 32-48)** code-switching: **ElevenLabs v3 PVC** on the founder's own voice handles it better than Bulbul, which is purer Indic.
- **Founder voice in English-dominant content:** ElevenLabs v3 PVC, 3 hours of clean studio source for the clone.

**Rule of thumb:** Build three voice assets day one. Founder's cloned voice in ElevenLabs PVC (English + Hinglish). One neutral male and one neutral female Sarvam Bulbul V3 voice for pure-Indic regional dubs. Cartesia Sonic-3 as the daily ad VO crank. Every ad pulls from these slots.

---

## 5. Talking heads and avatars

Three different jobs hide inside "talking head". Treat them separately. **Note: the leader has flipped since January.** Hedra Character-3 is now the Best for studio avatars on naturalness, with HeyGen Avatar IV in the Efficient slot.

### 5a. Studio avatars (founder body double, multilingual scale)

| Tier | Model | Why | Cost |
|---|---|---|---|
| **Best** | **Hedra Character-3** | One photo + audio. Phoneme-accurate lip-sync with auto blinks, gaze shifts, brow raises. "Wins on naturalness at the syllable level" vs HeyGen's over-articulation per lipsync.com benchmark. 720p ceiling and stiff full-body motion are the trade-offs. | Free 300 credits, then $15 Basic / $30 Creator / $75 Pro. |
| **Efficient** | **HeyGen Avatar IV** | 175+ languages, 1080p, best multilingual dubbing of an existing avatar. Avatar IV burns 20 credits/min, Creator plan's 200 credits = ~10 min. India pricing page exists. | Creator $29/mo (₹2.4K), Business $99, Pro $149. |
| **Third** | **Captions / Mirage Studio** | Rebranded Sept 2025. "One selfie to AI twin." 28+ languages, integrated TTS + voice clone + auto-edit. Output occasionally robotic; useful when you want one app from selfie to ad. | Credit-based, opaque pricing. |

**Sources:** https://www.hedra.com/pricing • https://lipsync.com/compare/heygen-vs-hedra • https://help.heygen.com/en/articles/11269603-heygen-avatar-iv-complete-guide • https://www.heygen.com/en-in/pricing • https://techcrunch.com/2025/09/04/captions-rebrands-as-mirage-expands-beyond-creator-tools-to-ai-video-research/

**HeyGen credit-policy backlash:** loudest open thread on the HeyGen community forum in April-May 2026; Creator users hit the 200-credit Avatar IV cap fast. Plan budget accordingly. https://community.heygen.com/public/forum/boards/product-feedback-and-requests-3gx/posts/avatar-iv-pricing-makes-it-hard-to-scale-for-creators-5lp669gwv6

### 5b. Lip-sync on real footage (dub the founder's own video into Hindi)

| Tier | Model | Why | Cost |
|---|---|---|---|
| **Best** | **Sync.so Lipsync-2-Pro** | New 2026 standard. 4K, studio-grade close-ups. Independent benchmark: only tool that clears ≥92% bilabial-closure accuracy needed for Hindi plosives. Free API tier. | $5/min web, $0.083/sec API. Standard lipsync-2 at $3/min. |
| **Efficient** | **fal.ai sync-lipsync v2** | Same Sync engine billed via fal. Avoid a second subscription if already on fal. (Older v1.9 still listed at $0.70/min.) | $3/min v2, $5/min v2/pro on fal. |
| **Third** | **Captions AI Lip Sync** (in Mirage) | 28+ languages, subscription-bundled. Weaker than Sync on close-ups and Devanagari aspirate visemes. | Inside Mirage subscription. |

**Sources:** https://sync.so/pricing • https://sync.so/lipsync-2-pro • https://aiadoptionagency.com/sync-so-lipsync-2-pro-the-new-standard-for-studio-grade-ai-lip-sync/ • https://fal.ai/models/fal-ai/sync-lipsync/v2

### 5c. UGC-style synthetic creator ads (Meta-grade)

| Tier | Tool | Why | Cost |
|---|---|---|---|
| **Best** | **Arcads** | 200+ digital actors, closest to filmed UGC in side-by-sides. Built for performance marketers running $500+/mo on Meta. Raised $16M in 2025. | Starter $110/mo (10 videos), Creator $220/mo (20 videos), ~$11/video. No free trial. |
| **Efficient** | **Creatify** | "Delivers 85-90% of Arcads' quality at 60-70% of the price" per ezUGC. Product-URL-to-ad workflow for fast variant testing. 700+ avatars, Batch mode. | Free 10/mo watermarked, Starter $19, Pro $49. |
| **Third** | **Hypernatural** | Script/blog/podcast to short-form. Narration scores higher on naturalness than peers, weaker as a founder-face UGC engine. Better for branded shorts. | Free 100 lifetime credits, Creator $19/mo (500 credits), Pro $34/mo (1,500). |

**Sources:** https://www.arcads.ai/ • https://www.ezugc.ai/blog/arcads-ai • https://creatify.ai/pricing • https://hypernatural.ai/pricing

**India access (all of section 5):** HeyGen, Synthesia, Hedra, Sync.so, Captions/Mirage, Arcads, Creatify, fal.ai all work from Indian IPs without VPN. HeyGen has a localised India pricing page. **Indian face quality remains the binding constraint** across Western avatars: only Sync 2 Pro and Hedra Character-3 clear the ≥92% bilabial-closure / <80ms viseme-drift bar in independent Indian-dubbing-studio testing. https://www.truefan.ai/blogs/lip-sync-accuracy-benchmark-india

**Rule of thumb:** Record once, ship five ways. A 2-minute founder studio recording becomes a Hedra Character-3 avatar (multi-language ads), a Sync.so Lipsync-2-Pro source clip (dubbed reels), and ElevenLabs PVC training data. The same 30 minutes of effort feeds three pipelines.

---

## 6. Music and jingles

| Tier | Model | Why it wins now | India access | Cost |
|---|---|---|---|---|
| **Best** | **Suno v5.5** ("Omni" / "Voices", March 2026) | r/SunoAI consensus pick for full-song quality. Voices update lets Pro/Premier clone the lead singer. Strongest on Bollywood/Hindi vocal per Indian creators. Full commercial rights on paid plans. | Yes, USD card. No native INR/UPI yet [unverified]. | Pro $10/mo (2,500 credits, ~500 songs), Premier $30/mo (10K credits + Suno Studio). |
| **Efficient** | **ElevenLabs Eleven Music** (iOS launch Apr 2026, API live) | Cleared for commercial use through **Merlin + Kobalt + SourceAudio** licensing. The only model where legal does not get nervous about an ad jingle. Modular section-regen. Same subscription covers VO. | Yes, USD. | $0.50/min generated audio via API; Pro $29/mo covers music + voice. |
| **Third** | **Beatoven.ai** (Indian-founded) | Mood-based instrumental beds, designed for licensable background scoring. Founder from a sitar gharana family. The right pick for raga-tinted PDP video beds and reel underscores. Instrumental only. | Native Indian company, INR billing. | Creator $2.50/mo, Visionary $16.66/mo. |

**Royalty critical note:** Every ad jingle that touches Meta or YouTube must have clean commercial rights. Suno Pro/Premier grant full commercial rights (retained after cancellation for songs made while subscribed). ElevenLabs Eleven Music licenses through majors. Beatoven royalty-free on paid plans. **Udio downloads are currently disabled** (UMG Oct 2025 + Warner Nov 2025 + Merlin Dec 2025 + Kobalt Jan 2026 deals); the walled-garden architecture blocks export. Effectively unusable for ads until licensed launch ships.

**Sources:**
- Suno: https://www.aitooldiscovery.com/guides/suno-ai-reddit and https://suno.com/pricing
- ElevenLabs Music licensing: https://www.billboard.com/pro/elevenlabs-ai-music-model-merlin-kobalt-licenses-details/
- Eleven Music pricing: https://help.elevenlabs.io/hc/en-us/articles/37821528996497-How-much-does-Eleven-Music-cost
- Beatoven: https://www.beatoven.ai/pricing
- Udio walled garden: https://www.chartlex.com/blog/business/udio-umg-walled-garden-explained-2026

**Recent shake-ups:**
- **Google Lyria 3 Pro** (announced Mar 25, 2026). Up to 3-min tracks, structure-aware (intro/verse/chorus). Available via Vertex AI, Gemini API, Google AI Studio. Now also powers Riffusion's reborn Producer.ai. https://techcrunch.com/2026/03/25/google-launches-lyria-3-pro-music-generation-model/
- **Stable Audio 2.5** (enterprise positioning). 3-min in seconds, fully licensed training set, live on fal.ai. Marketed for ads/podcasts/trailers. https://stability.ai/news-updates/stability-ai-introduces-stable-audio-25-the-first-audio-model-built-for-enterprise-sound-production-at-scale

**Bollywood and Indian instrumentation:** Suno is the consensus pick for Hindi vocal output. Prompt guidance from Indian creators: tag genre as "Bollywood" or "Hindi pop", name instruments explicitly (tabla, dhol, sitar, harmonium, bansuri), write lyrics in Devanagari for cleaner pronunciation. Caveat: vocals "smear" on dense Hindi consonant clusters; keep jingle lines short. https://www.soundverse.ai/blog/article/best-hindi-ai-song-generators

**Rule of thumb:** Generate three 15-second brand jingles in Suno Pro, route the lead vocal through Eleven Music for the licensed master, and use Beatoven for pure instrumental beds. Royalty-free stock music is a tell on a brand that should have its own sonic identity.

---

## 7. Platform matrix (which stack ships which platform)

| Platform | Static ad | Video ad | Voice over | Notes |
|---|---|---|---|---|
| **Meta Reels** | n/a | Kling 3.0 + Sync Lipsync-2-Pro for dubs | ElevenLabs v3 (Hinglish), Sarvam Bulbul V3 (Indic) | 9:16, 6-9s sweet spot |
| **Meta Feed (image)** | Flux 2 + Ideogram 3 text overlay | n/a | n/a | 4:5 best, 1:1 fallback |
| **Meta Stories** | Recraft V4 (vertical poster) | Hailuo 02 Pro (cheap variants) | Sarvam Bulbul V3 | 9:16, 5-15s |
| **YouTube ads** | n/a | Veo 3.1 (hero) + Kling 3.0 (variants) | ElevenLabs v3 PVC founder voice | 16:9, 15-60s |
| **YouTube Shorts** | n/a | Kling 3.0 + Sarvam VO | Sarvam Bulbul V3 | 9:16, under 60s |
| **Google Display** | Recraft V4 (multi-size banner SVG) | n/a | n/a | Vector output saves rework |
| **Google Performance Max** | Flux 2 + Recraft V4 (mix) | Veo 3.1 + Kling 3.0 (mix) | ElevenLabs + Sarvam | PMax needs 5-15 assets per format |
| **Amazon listings (A+ content)** | Nano Banana Pro (lifestyle) + GPT Image 2 (callouts) | Veo 3.1 (product hero video) | ElevenLabs v3 (English) | Amazon is strict on rendered-text accuracy |
| **Flipkart listings** | Recraft V4 (banner) + Nano Banana Pro (festive Devanagari) | Kling 3.0 | Sarvam Bulbul V3 | Flipkart category banners reward festive aesthetics |
| **Zomato / Swiggy** | Flux 2 + Ideogram (price + claim text) | n/a (mostly static) | n/a | Tile size and price legibility decide CTR |
| **WhatsApp Status / Catalogue** | Recraft V4 (square) | Hailuo 02 (short, low cost) | Sarvam Bulbul V3 | Design for 480p compression reality |
| **PDP hero (Shopify)** | Nano Banana Pro or Flux 2 Max | Veo 3.1 i2v (animate the hero) | n/a | One image, render it best |
| **Email hero** | Flux 2 + Ideogram text | n/a | n/a | 600px width target |
| **Influencer brief / mood board** | Nano Banana Pro or Midjourney V8.1 | n/a | n/a | Direction setting, not shipping |

---

## 8. India-specific calls

- **Indian faces:** Midjourney V8.1's bias remains documented (defaults to lighter skin, Western features per Rest of World and Bloomberg analyses). For Indian persona shots, default to **Seedream 4.5** or **Flux 2 Dev + Desi Mocha LoRA** for control. **Nano Banana Pro** also handles Indian faces better than Midjourney out of the box.
- **Indian languages voice:** **Sarvam Bulbul V3** for Hindi, Tamil, Telugu, Bengali, Marathi, Kannada, Gujarati, Punjabi, Odia, Malayalam. ElevenLabs v3 PVC for Hinglish where code-switching matters.
- **Devanagari in posters:** **Nano Banana Pro** is the only model with a primary vendor claim for legible Devanagari. Ideogram and Flux fail this test.
- **Tamil, Telugu, Bengali, Punjabi, Gujarati, Odia, Malayalam, Kannada scripts in posters:** no model currently renders legible output. Overlay text in Figma or Canva.
- **Compliance copy on ads (FSSAI numbers, MRP, net quantity, CDSCO, BIS):** Indian compliance text must be readable. Generate background in Flux 2 or Nano Banana Pro, overlay compliance text in a real design tool. Never let the model render compliance fields.
- **INR billing:** Native INR billing on **Sarvam, Beatoven, Google One AI Premium, HeyGen India page, Adobe Creative Cloud**. Everyone else bills USD; Indian cards work, add 2-3% FX + TCS.
- **Sora 2 is not available in India.** Skip from your stack until OpenAI relaxes regional restrictions.

---

## 9. End-to-end workflows (combine the models)

These are three pipelines a D2C creative team will run weekly. Each combines three to four models from the tables above.

### Founder talking head Reel, multi-language

1. Founder records one 90-second English clip in a quiet room (no studio).
2. Clip becomes:
   - **Hedra Character-3** trained on the clip, endless variants in English, Hindi, Tamil
   - **Sync.so Lipsync-2-Pro** with the original clip + ElevenLabs/Sarvam dubbed audio, real founder dubbed
   - **ElevenLabs v3 PVC** trained on the same clip (use 3 hours of clean audio, not 90 sec, for founder-grade output), narrated B-roll ads
3. Output: 15-20 Reels per week from one recording session.

### Festival poster batch (Diwali, Rakhi, Wedding season)

1. **Flux 2 Pro or Nano Banana Pro** generates the warm festive background (no text in prompt).
2. **Nano Banana Pro** generates the Devanagari overlay variant; **Ideogram 3.0** for English-only overlay.
3. Composite in Canva or Photoshop: Flux/NBP background, NBP/Ideogram text layer, brand logo, FSSAI compliance fields.
4. Output: 8-12 poster variants in an afternoon, each suited to a different SKU or audience cut.

### Premium Meta hero campaign (one big ad, 50 variants)

1. **Veo 3.1** produces the 8-second hero video with native audio. One asset, premium quality.
2. **Kling 3.0** produces 5-8 variant cuts (different angle, different B-roll, same script).
3. **Hailuo 02 Pro** produces 20-30 cheap test variants for early A/B (hook test, thumbnail test).
4. **ElevenLabs v3 PVC** generates the English/Hinglish VO. **Sarvam Bulbul V3** generates the Hindi, Tamil, Marathi VO. **Sync.so Lipsync-2-Pro** lip-syncs the Veo hero into each language.
5. Output: 1 hero + 50+ test variants ready for Meta's automatic placements.

---

## 10. Access pattern (one account each, not ten)

| Account | Why one | India billing |
|---|---|---|
| **fal.ai** | Single pay-as-you-go covers Flux 2, Kling 3.0, Hailuo 02, Hedra, Sync.so, Recraft, Seedream, Wan 2.7 and most of the Efficient tier | USD, Razorpay or card |
| **Google AI Premium / Vertex** | Veo 3.1, Nano Banana Pro, Imagen 4 Fast, Lyria 3 Pro | INR ₹1,250/mo for AI Premium; USD on Vertex API |
| **OpenAI** | GPT Image 2, gpt-4o-mini-tts, ChatGPT Plus for brief composition | USD |
| **ElevenLabs** | Voice cloning (PVC), multilingual TTS, Eleven Music | USD, Razorpay in some plans |
| **Sarvam AI** | Indian-language TTS, native INR | INR |
| **Midjourney** | Mood imagery (Discord/web only) | USD |
| **Ideogram** | English-script text-in-image, festive posters | USD |
| **Recraft** | Vector + brand-kit marketplace banners | USD |
| **Suno** | Music and jingles | USD |
| **Hedra** | Founder avatar | USD |
| **Sync.so** | Lip-sync existing footage | USD |
| **Arcads or Creatify** | UGC-style ads (only when ad budget justifies it) | USD |

The fal.ai single account replaces eight separate logins. Default to fal first, add direct accounts only when the direct vendor unlocks a tier fal does not host.

---

## 11. What to skip

| Tool | Why skip (May 2026) |
|---|---|
| **Udio** | Downloads disabled since the UMG/Warner/Merlin/Kobalt settlement chain. Walled garden architecture blocks export. Effectively unusable for ads until licensed launch. |
| **Sora 2 (consumer)** | App sunset Apr 26, 2026. Not available in India. API live but Veo 3.1 / Kling 3.0 cover the job. |
| **Flux 1.1 Pro Ultra** | Deprecated by Flux 2 (Nov 25, 2025). Use Flux 2 tier of choice. |
| **PlayHT Play 3.0** | Trustpilot and G2 in 2026 flag billing complaints and queue-time quality issues. Skip as primary. |
| **Synthesia 2.0** | Enterprise pricing kills it for D2C velocity. Use only if compliance/SOC2 requires it. |
| **Tavus** | Real-time conversational only. Wrong shape for pre-rendered ad pre-rolls. |
| **Generic "AI ad generator" SaaS bundles** (Jasper "ad mode", copy.ai "ads") | They wrap weaker underlying models. The teammates compose briefs; the models above produce the output. Cut the middleman. |
| **Canva Magic Design as the production default** | Useful for one-off founder edits. Not a pipeline. Production lives in Flux 2 + Nano Banana Pro + Ideogram + a real compositor. |
| **Stability AI hosted SDXL** | Flux 2 has overtaken SDXL on every benchmark. Use Flux 2 unless a specific SDXL LoRA already exists. |
| **Free-tier-only voice tools** (Speechify free, TTSMaker) | Wrong robot. Customer-facing audio needs ElevenLabs, Cartesia or Sarvam. |
| **Aggregator marketplaces (RunComfy, AICreatorz)** | Higher per-call price, worse uptime, same models you can hit at fal.ai or Replicate directly. |

---

## 12. The next twelve months (watch list)

- **Veo 4** (expected at Google I/O on May 19-20, 2026). 4K, longer durations rumoured. Re-verify the day after I/O.
- **Wan 2.7 ecosystem** (Apache 2.0, Apr 1-6, 2026 release). LoRA fine-tunes for self-hosted brand pipelines are likely the next D2C unlock for teams with a GPU budget.
- **Krea 2 (K2)** (launched May 12, 2026). First Krea foundation model. Watch how fast their aesthetic catches up with Flux 2.
- **HiDream-O1-Image** (early May 2026, open weights). Top-ranked open-weights model on Artificial Analysis. Watch for self-hosted ad pipelines.
- **Suno v6 watch.** v5.5 is current; community expects a v6 announcement in mid-2026.
- **Real-time avatar** (Tavus, Hedra Live) as a customer support layer, not an ad layer.
- **LoRA training as a managed service.** fal.ai and Replicate both moving toward "upload 20 brand photos, get a model." Will eat a chunk of the Civitai market.

Track these. Do not switch your weekly pipeline to a model in beta. Switch the week it is stable and 30% better than what you have.

---

## How this resource gets used in the workshop

- **Performance Marketer** (Session 6) composes the brief, then this page tells you which model the brief should ship through.
- **Content Lead** (Session 4) plans the calendar, then this page tells you which model produces the 30 days of assets.
- **Storefront Specialist** (Session 7) writes the PDP, then this page tells you how the PDP hero gets shot without a photographer.
- **Influencer Scout** (Session 11) shortlists creators, then this page tells you how to test a creator's script in Arcads before signing a deal.

Every other piece of the workshop is the brief. This page is the bench.

---

## Re-verification cadence

Model releases move on a 4-6 week cadence. This page is stamped **2026-05-16**. Re-verify before any contract, procurement decision or campaign worth more than ₹50K of spend. The four canonical pages to check first:

1. https://fal.ai/models (most efficient-tier models live here)
2. https://blog.google/ (Veo, Nano Banana Pro, Imagen, Lyria announcements)
3. https://elevenlabs.io/docs/changelog (voice + music updates)
4. r/StableDiffusion + r/aivideo + r/SunoAI top-of-week threads (community sentiment)
