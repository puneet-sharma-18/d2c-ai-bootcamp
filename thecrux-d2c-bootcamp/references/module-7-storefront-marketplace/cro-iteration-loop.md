# The CRO Iteration Loop

This document goes deeper than Module 7's BRIEF on the read-write iteration loop. Instructors read it before the demo. Power-plan founders read it if they want to run the loop more aggressively after the workshop.

## The shape of the loop

```
[1] Read live data        ← Shopify MCP, conversion rate, order count
       ↓
[2] Diagnose the gap      ← What does the page say vs. what do customers care about
       ↓
[3] Rewrite               ← PDP Writer skill, before / after
       ↓
[4] Push to draft         ← Shopify draft, NOT live
       ↓
[5] Founder review        ← Voice match, compliance check, founder approval
       ↓
[6] Publish to live
       ↓
[7] Wait 7 to 14 days     ← Conversion rate moves (or does not)
       ↓
[8] Re-run                ← Read new data, diagnose new gap
       ↓
   (back to [1])
```

This is different from the Day-1 skills which produced static reports. The PDP Writer is part of an ongoing loop, not a one-shot.

## Why the loop matters

A single rewrite is a guess. The data after 7 to 14 days tells you whether the guess was right. Without measurement you are running on opinion. The skill bakes measurement into the workflow by:

1. Reading live conversion rate before rewriting (so you know the baseline)
2. Saving before / after files (so the diff is visible)
3. Recommending a measurement window (7 days for high-traffic SKUs, 14 for low)
4. Re-reading conversion rate on the next run (so the loop is closed)

## How to run the loop after the workshop

A realistic Monday-morning routine for a founder who took this seriously:

### Week 1 (immediately after workshop)
- Run PDP Writer DEFAULT on 2 SKUs
- Push 1 to Shopify draft, review, publish
- Note the date and the baseline conversion rate

### Week 2
- Wait. Do not rewrite again.
- Look at the conversion rate trend in Shopify analytics. If it moved up, the rewrite worked.

### Week 3
- Re-run PDP Writer. The skill reads the new conversion rate.
- If conversion rate rose: keep the new copy, rewrite the next SKU.
- If conversion rate stayed flat: the rewrite did not work for this audience. Re-read the gap analysis. Maybe a different VoC theme should drive the next rewrite.
- If conversion rate fell: revert. Use Shopify's version history. Reflect on what changed (sometimes the rewrite was off-voice, sometimes the new copy mentioned a claim that needed substantiation).

### Week 4
- Rewrite a second SKU based on what worked / did not in Week 1.

### Month 2
- POWER scope: top 5 SKUs.

### Month 3
- Audit. Run the skill in audit mode. Compare current PDPs against the latest VoC themes (which have shifted). Decide which need a rewrite cycle next quarter.

## What measurement actually looks like

The metric that matters is **add-to-cart rate** for the PDP, not orders. Reasons:
- PDP copy controls add-to-cart, NOT post-cart conversion (cart abandonment is checkout's problem, not PDP's)
- Looking at "orders" lets checkout-flow noise mask PDP performance
- Add-to-cart is a tighter signal, moves faster, needs fewer days to be readable

If the skill cannot pull add-to-cart rate from Shopify MCP (some shops do not have analytics enabled), use these fallbacks:
- Sessions to PDP / orders for that SKU (proxy for add-to-cart)
- Average time on page (proxy for engagement)
- Bounce rate from PDP (proxy for hook quality)

## Avoiding the iteration trap

Three failure modes to watch for:

### 1. Rewriting too often
If you rewrite weekly, you cannot measure anything. Conversion rate needs 7 to 14 days to settle. Rewrite, wait, then rewrite the next SKU. Round-robin, not back-to-back.

### 2. Rewriting based on noise
A 10% change in conversion rate over 3 days is usually noise on small SKUs. Wait for the sample size to stabilise before declaring a rewrite worked or failed.

### 3. Forgetting voice compliance
A rewrite that lifts conversion 15% but uses a banned word from CLAUDE.md is not a win. The brand voice rules are non-negotiable. The skill flags this; do not override.

## When NOT to use this loop

This is a PDP / listing copy loop. It does NOT fix:
- Image quality (the visual budget belongs to a different process)
- Trust failures at checkout (different funnel stage)
- Out-of-stock issues (operations problem, not copy problem)
- Pricing mismatch with category (positioning problem, edit CLAUDE.md and revisit)

If the founder runs the loop 3 times and conversion does not move, the constraint is probably one of the above, not the copy. The CRO observations list the skill produces will name which constraint is suspect.

## Compounding

The loop compounds because:
- VoC gets richer every week (Module 3's MCPs feed it new data)
- CLAUDE.md gets sharper every refresh (founder adds learnings from what worked)
- Market Analyst tracks competitors moving over time
- The PDP Writer's gap analysis is therefore based on a more accurate picture each run

A founder who runs this loop monthly for 6 months has 6 generations of data-driven copy + a compounding understanding of what their customer actually responds to. That understanding is the moat.

## Reading further

- The PDP Writer skill: `.claude/skills/pdp-writer/SKILL.md`
- The Marketplace Editor skill: `.claude/skills/marketplace-editor/SKILL.md`
- The brand safety checklist (applies to every rewrite): `references/module-4-agents/brand-safety-checklist.md`
