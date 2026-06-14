# Little Lab — Worked Example Across All 10 Teammates

This folder is a canonical run-through of the entire D2C workshop on a fictional brand: **Little Lab**, a baby skincare D2C brand at ARR ~₹4.2Cr. Every artefact a founder produces during the weekend lives in `my-work/` in their own repo. This folder mirrors that exact shape after a full run.

**Brand and all numbers are fictional**, designed to feel real (Mumbai/Bengaluru personas, Mother Sparsh and Mom's Co as competitors, plausible review patterns, plausible Shopify metrics). Do not cite any of this in a real founder's deck.

## Two purposes

1. **Instructor flash asset.** During each module, the instructor can open the matching folder to show "this is what a good output looks like" before founders run the skill on their own data.
2. **Catch-up fallback.** A founder running 30 minutes behind can copy the relevant subfolder into their own `my-work/` and continue with the chain. They lose personalisation for that module but the chain stays alive for downstream modules.

## Map of artefacts to modules

| Module | Files |
|---|---|
| 1 — Brand Brain | (see `references/module-1-brand-brain/little-lab.example.md` at repo root) |
| 2 — Skills | `my-work/market-analyst/2026-05-12-intel-report.md`, `my-work/voice-of-customer/2026-05-12-voc-report.md` |
| 3 — MCPs | `sample-inputs/shopify-products.csv`, `sample-inputs/reviews-export.csv`, `sample-inputs/gmail-support-threads.md` |
| 4 — Content Lead | `my-work/content-lead/` (calendar, 3 sample pieces, 2 marketplace listings, index) |
| 5 — Day-1 Integration | `my-work/captain/2026-05-12-day-1-summary.md` |
| 6 — Performance Marketer | `my-work/performance-marketer/` (2 angle folders, 1 creative brief, index) |
| 7 — Storefront + Marketplace | `my-work/storefront-specialist/` (1 PDP rewrite, CRO list, index), `my-work/marketplace-editor/` (1 Amazon A+, 1 Flipkart, index) |
| 8 — Ops + Retention | `my-work/ops-manager/` (2 SOPs, vendor template, index), `my-work/retention-manager/` (5 WhatsApp, 3 email, 2 segments, index) |
| 9 — Growth Analyst | `my-work/growth-analyst/2026-05-12-brief.md` |
| 10 — Capstone | `my-work/captain/2026-05-19-90-day-roadmap.md`, `my-work/captain/2026-05-19-summary.md` |

## DEFAULT scope only

These samples are sized for the Pro plan workshop slot (DEFAULT). POWER-scope variants are not included because they double token cost without changing pedagogy. A founder on Max plan can scale the DEFAULT sample shape up trivially.

## Conventions

- Dates are absolute (`2026-05-12`) so the sample reads as a real run on that Saturday/Sunday weekend.
- All numbers are concrete (not `{placeholder}`). They are still fictional. The header of each file says "fictional Little Lab data" so no one ports them into a real founder's deck.
- Indexes are paired with raw outputs in every Day-2 folder, per the "indexes only at synthesis time" rule (`DAY-2.md:10`).
- File-naming convention matches the SKILL.md and agent definitions exactly.

## How to use mid-workshop

If a founder is behind in Module 4:
```bash
cp -r examples/little-lab/my-work/content-lead my-work/
```
They now have the Content Lead output for Little Lab. Module 5's integration prompt still works (it just runs on Little Lab's data, not theirs). They flag this in chat and catch up on Sunday morning.
