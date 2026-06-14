# The 20-piece content breakdown

This document defines what good looks like for each of the 20 pieces the Content Lead subagent produces. Founders read it once before reviewing the output. The subagent reads it as part of its system prompt context.

## The 20 pieces

| Channel | Count | File pattern | Length |
|---|---|---|---|
| Instagram caption | 8 | `pieces/instagram-NN-<topic>.md` | 80-150 words |
| Email | 4 | `pieces/email-NN-<topic>.md` | subject + 200-400 word body |
| Reel script | 4 | `pieces/reel-NN-<topic>.md` | 30-second beat sheet |
| Long-form blog | 2 | `pieces/blog-NN-<topic>.md` | 800-1200 words |
| Newsletter | 2 | `pieces/newsletter-NN-<topic>.md` | 300-500 words |

## What good looks like by channel

### Instagram caption

- Opens with a hook that is not a question. "Drop alert.", "We tested this for 6 weeks.", "The one ingredient we will not use."
- Uses two of the founder's "always" phrases naturally
- Uses zero banned words
- Has one specific number, one named SKU, or one named source from VoC
- Ends with a soft CTA, not "buy now"

Bad: "Discover our amazing new collection that will elevate your skincare routine ✨"
Good: "Drop alert. {Ferment-Bright serum}, six weeks of formulation, one ingredient we will not list because legal needs to clear it. Wait list link in bio."

### Email

- Subject line: 6-9 words, specific
- Pre-header: 50 chars max, complements the subject (does not repeat it)
- Opening line: not "Hi {name}". Address the reader's problem in one sentence.
- Body: 200-400 words, one idea, one CTA
- The CTA is one button, one link. Not three.

Bad subject: "Don't miss our amazing summer sale!"
Good subject: "We are out of {hero SKU} in 3 sizes already"

### Reel script (30 seconds)

Beat sheet, not a script. Reels are visual. The Content Lead writes:

```
HOOK (0-3s): One line. What stops the scroll?
SETUP (3-12s): The problem or context.
PAYOFF (12-25s): The thing the brand does about it.
CTA (25-30s): What the viewer does next.
```

For each beat: one line of dialogue or VO + one line of what is on screen.

### Long-form blog (800-1200 words)

- One thesis. One. Not three.
- Founder voice, not corporate blog voice. First person if CLAUDE.md says so.
- Has one expert claim, one customer quote (from VoC, real, attributed to {persona-1}), one practical takeaway
- No section that is just SEO filler
- Ends with one specific next step the reader can take, not "if you have any questions, reach out"

### Newsletter section

- Standalone read, not "click here for more"
- 300-500 words on one topic
- Three things: the observation, the founder's take, what we are doing about it
- Sign-off matches the founder's actual sign-off

## Marketplace listings

Five Amazon A+ blocks and five Flipkart copy variants, one per top SKU. See `.claude/agents/content-lead.md` Step 4 for the structure. Length and field rules:

### Amazon A+ block

- Hero text: 60 chars, the SKU's one-line USP
- Module 1: 250 words max, image + body. Address the top customer concern from VoC for this SKU.
- Module 2: 5 feature highlights, one line each, lifted from CLAUDE.md USPs
- Module 3: 150 words, brand story callback. Founder voice.
- Backend keywords: 5 keywords, no commas, lifted from Market Analyst report's top organic keywords if available

### Flipkart copy

- Title: 200 chars max, includes the brand name, the SKU name, the size or pack count, and one filter-friendly attribute (e.g. "vegan", "fragrance-free", "small batch")
- Highlights: exactly 5 bullet points, one line each, lifted from CLAUDE.md USPs and VoC themes
- Description: 300-500 words, can be more conversational than Amazon
- Specifications: pulled from CLAUDE.md Section 4 + Shopify MCP if available; never invented

## What the Content Lead does NOT produce

- **Image briefs.** The subagent writes a 1-line image hint per piece (e.g. "Image: hero SKU on a kitchen counter with morning light"). Full image generation or photo briefs are the Performance Marketer's job on Day 2.
- **Paid ad copy.** Performance Marketer module on Day 2.
- **PDPs and landing pages.** Storefront Specialist module on Day 2.
- **Email automation flows.** Retention Manager module on Day 2.

This narrowness is a feature. Content Lead ships content. That is the job.

## How to read a Content Lead output

Founders ask "where do I start with 30 files?". Tell them:

1. Open `my-work/content-lead/<date>-index.md`. The Top 5 reads section names the 5 files to read first.
2. Open those 5 files. Edit anything that does not sound like you. (If everything sounds wrong, the issue is CLAUDE.md, not these files. Edit Section 7 of CLAUDE.md and re-run Content Lead next week.)
3. Schedule the first 5 to ship over the next 14 days.
4. Skim the remaining 15 + 10 marketplace listings in the next 24 hours. Use them as a starting library, not a finished product.

The Content Lead is not a Monday-morning replacement for your content team. It is a weekly head start.
