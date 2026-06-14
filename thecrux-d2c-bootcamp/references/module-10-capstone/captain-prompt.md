# The Captain Prompt — Cross-cutting questions

This is the prompt the founder runs when they have a question that no single teammate can answer alone. The Captain reads INDEX files only and synthesises across the 10 teammates.

Use this for:
- "Should we launch SKU X this week?"
- "Should we match the competitor's price drop?"
- "Why is repeat purchase rate stuck?"
- "Where should I spend the next ₹{N} of ad budget?"
- "Is this customer complaint a one-off or a pattern?"

Do NOT use for:
- Questions a single teammate can answer (run the teammate directly)
- Generative tasks (write content, design ads, etc.)
- Anything time-sensitive (the Captain is thoughtful, not fast)

## The prompt

Paste this into Claude Code:

```
Spawn the Captain subagent. I have a cross-cutting question that needs
synthesis across teammates.

My question: <your question, in one or two sentences>

Read the index files for all 10 teammates plus CLAUDE.md. Do NOT read
any raw teammate output (no piece files, no SOPs, no individual ads).

Then answer in this exact shape:

## My read
<2 to 4 lines: the most likely answer, with confidence level (high /
medium / low)>

## Why I think this (cite all teammates whose indexes contributed)
- From CLAUDE.md: <one line>
- From <teammate>: <one line, cite file>
- From <teammate>: <one line, cite file>
(only include teammates whose index actually informed the answer)

## What would change my mind
<one to two specific signals that would shift the answer. e.g. "if VoC
sweep tomorrow shows the complaint cluster doubled, I would shift from
'one-off' to 'pattern'.">

## What I cannot answer from indexes
<honest gaps. If the question needs raw data the indexes do not surface,
say so and recommend which teammate to drill into.>

## Recommended action
<one specific action, with the teammate that runs it, and the expected
outcome>

Save this synthesis to my-work/captain/<date>-<question-slug>.md.
```

## How to read the response

The Captain's response has a specific shape because cross-cutting questions are different from teammate-level questions. The shape forces:

1. **A read with confidence.** Not "it depends". A specific answer plus how confident the system is.
2. **Citations that you can verify.** Every line that contributes to the answer names which teammate's index it came from. If you doubt the answer, open that index, check the line.
3. **Falsifiability.** "What would change my mind" tells you what evidence to look for in the next week. Without this, the answer is unfalsifiable and not useful.
4. **Honesty about limits.** Indexes are summaries. If the question needs raw data, the Captain says so rather than inventing.
5. **Action, not just analysis.** Every Captain answer ends with one specific action. The Captain is not a strategy consultant; it is a synthesis tool that points at the next move.

## When the Captain refuses to answer

The Captain will refuse (or heavily caveat) if:

- 3+ teammate indexes are stale (older than 14 days)
- The question depends on data the indexes do not summarise (e.g. "what was customer X's last order" needs raw Shopify, not the Growth Analyst brief)
- The question is generative ("write me an ad") rather than synthesis-driven

In each case, the Captain redirects:
- Stale indexes → re-run the stale teammates first
- Raw data needed → run the relevant teammate directly with a focused prompt
- Generative → spawn the right teammate (Content Lead, Performance Marketer, etc.)

This redirect is the right behaviour. The Captain is not a swiss army knife; it is a synthesis tool with a specific shape.

## Worked examples

### Example 1: "Should we launch the bundle SKU this week?"

Captain reads indexes. Likely synthesis:

```
## My read
Hold the launch by 1 week. Confidence: medium-high.

## Why I think this
- From CLAUDE.md: bundle is the cross-sell SKU, depends on hero SKU trust
- From Growth Analyst: hero SKU CAC is up 22% this week, repeat rate flat
- From VoC: top theme this week is "delivery speed"; new customers are
  worried about a 2-SKU bundle arriving intact
- From Performance Marketer: ads for the bundle would compete with the
  hero SKU's recovery campaign

## What would change my mind
If hero SKU CAC normalises by Friday AND the delivery theme falls below
top 5, launch on schedule.

## What I cannot answer from indexes
The bundle's actual margin economics are not in any index. Open Shopify
to check whether bundle margin is high enough to absorb the worse CAC
environment.

## Recommended action
Hold the bundle launch announcement. Run Performance Marketer DEFAULT to
drop one social-proof ad for the hero SKU. Re-run Captain next Monday.
```

### Example 2: "Why is repeat purchase rate stuck at 12%?"

```
## My read
Two contributors: SKU 2 (Cradle Cap Balm) is single-use, naturally
limits repeat. AND SKU 1 (Newborn Daily Lotion) replenishment cadence
is too long for a "habit" purchase. Confidence: medium.

## Why I think this
- From Retention Manager: 60-day-lapsed segment is dominated by
  Cradle Cap Balm first-time buyers (single-use SKU, expected behaviour)
- From VoC: review themes for SKU 1 mention "lasts 3 months", which is
  longer than most baby skincare replenishment habits form around
- From Market Analyst: competitors push subscription on SKU 1 with 15%
  discount, we do not have a subscription offering yet

## What would change my mind
If we ship a subscription product for SKU 1 and repeat rate does not
move in 60 days, the constraint is something else.

## What I cannot answer from indexes
Customer-level cohort decay curves are not in indexes. Pull from Shopify
directly.

## Recommended action
Two-part. Retention Manager: ship the replenishment WhatsApp template
for SKU 1 (already drafted). Storefront Specialist: rewrite the
Newborn Daily Lotion PDP to add a subscription option. Watch for 60 days.
```

## Cadence of running the Captain

Recommended:
- **Weekly**: pick one cross-cutting question Sunday evening, run the Captain, read the answer Monday morning alongside the Growth Analyst brief.
- **Mid-week**: when something surprising surfaces (a competitor announcement, a customer alarm, an inventory issue), run the Captain to synthesise across teammates before deciding.
- **Quarterly**: run the 90-day roadmap update. Compare to the previous roadmap. Note what shipped, what slipped, what changed.

Avoid:
- Running the Captain daily on the same question. It re-reads the same indexes; the answer changes only when the indexes change.
- Asking the Captain to "do X" instead of "synthesise about X". The Captain reads, it does not produce content.

## What this prompt is NOT

- Not a coaching session. The Captain answers the question; it does not run a brainstorm.
- Not a forecasting tool. "Will we hit ₹{X}Cr by Q4?" needs a financial model, not the Captain.
- Not a replacement for thinking. The Captain points; you decide.
