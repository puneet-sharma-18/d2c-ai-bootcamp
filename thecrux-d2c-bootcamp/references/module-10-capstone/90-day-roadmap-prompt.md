# The 90-Day Roadmap Prompt

The Captain produces a 90-day operating roadmap as part of the Capstone DEFAULT run. This document explains the prompt the Captain uses internally, so founders can re-run it themselves quarterly without spawning the full Captain agent.

## When to use this directly

The Capstone Captain run does this once. Re-run it:

- **Quarterly** to refresh the 90-day plan with the last 90 days of compounded teammate data
- **After a major shift** (a fundraise, a category move, a co-founder departure, a 2x scale-up) when the prior plan no longer fits
- **When the founder feels lost** and needs to re-orient on what the 10 teammates are pointing at

For weekly orientation, use the Growth Analyst's Monday brief, not this prompt. The 90-day roadmap is a deeper, slower artifact.

## The prompt

```
You are the Captain. Read the index files for all 10 teammates plus
CLAUDE.md. Do NOT read raw teammate outputs.

Produce a 90-day operating roadmap for this brand, saved to
my-work/captain/<today>-90-day-roadmap.md.

Structure:

# 90-Day Operating Roadmap - <Brand>
Date: <YYYY-MM-DD>
Source indexes: <list of files read, with last-modified date for each>

## The brand in one paragraph
<from CLAUDE.md, in 4 to 5 sentences. Names brand, category, top SKUs,
primary persona, anti-positioning. Founder voice.>

## The state of the chain right now
<3 to 5 lines on what is strong and what is thin across the 10 teammates.
Be specific about which teammate's data quality is high and which is
thin. e.g. "VoC is strong (12 weeks of MCP-fed data, 600+ messages
processed). Market Analyst is mid (8 weeks, but only 3 competitors
tracked). Performance Marketer is thin (1 run, default scope, last
month).">

## Week 1 — what ships this week
For each item:
- Action (specific, not "improve X"): <what gets done>
- Owner teammate: <which teammate runs it>
- Expected outcome (measurable): <e.g. "lift Hero SKU PDP add-to-cart by 5
  to 10%">
- Risk if it does not happen: <one line, e.g. "Hero SKU CAC stays at
  ₹{510}, blended ROAS keeps falling">

(3 to 5 items, ranked by impact)

## Week 2 — what ships next week
(3 to 5 items, same shape)

## Week 3
(3 to 5 items)

## Week 4
(3 to 5 items)

## Month 2 — three priorities
1. <priority, with the teammate that owns the rhythm>
2. ...
3. ...

## Month 3 — three priorities
1. ...
2. ...
3. ...

## What this roadmap is NOT
- Not a budget plan. Spend lives in the Growth Analyst's brief.
- Not a hiring plan. Out of scope.
- Not a fundraising plan. Out of scope.
- Not a fixed contract. Re-run quarterly.

## Standing schedule (recommended)
| When | Who | What |
|---|---|---|
| Mon 09:00 | Growth Analyst | Weekly brief lands |
| Mon 09:30 | Market Analyst | Weekly competitor digest |
| Daily 11:00 | Voice of Customer | Daily alarm sweep |
| Wed 14:00 | Brand Brain | CLAUDE.md drift check |
| First of month | Content Lead | Next 30-day calendar |
| First of month | Performance Marketer | Ad hypothesis grid |

## The single cross-cutting recommendation for this week
<ONE specific cross-teammate action that no single teammate would have
surfaced alone. Cite the 3+ teammate indexes that justify it.>

## What I did not synthesise (gaps)
- Stale teammate outputs (>14 days old): <list>
- Cross-teammate questions that need raw data the indexes do not show: <list>
- Strategic questions the chain cannot answer (e.g. fundraising, hiring): <one line>

Hard rules for this roadmap:
- Every Week 1 item has an owner teammate. Vague items ("focus on
  retention") are not allowed; an item must be doable by one specific
  teammate.
- Every item has an expected outcome with a number where possible.
- The roadmap is realistic for the founder's 5 to 50Cr ARR scale. No
  "raise Series A" or "expand to USA" type items unless CLAUDE.md says so.
- No invented numbers, customer names, vendor names or system names.
- No em dashes.
```

## Customising the roadmap shape

Founders who want a different time horizon (e.g. 30-day or 6-month) can ask the Captain to produce that variant. The shape stays the same; only the time slices change.

For 30-day:
- Week 1 / 2 / 3 / 4 (replace Months 2 and 3)
- 3 to 5 items per week

For 6-month:
- Same Week 1 to 4
- Months 2, 3, 4, 5, 6 (replace Months 2 and 3 with the longer set)
- Each later month gets 2 to 3 priorities, getting fuzzier the further out

## What good looks like

A good 90-day roadmap has:

1. **Specificity at week 1, fuzziness at month 3.** Week 1 should read like a project plan; Month 3 should read like a direction. False precision at month 3 is a red flag (the world will change and the plan should adapt).

2. **Every owner is a real teammate.** No "marketing team will handle this". The 10 teammates own everything. If something does not have an owner, it does not belong in the roadmap.

3. **Items that compound.** The Week 1 PDP rewrite enables the Week 4 retention win-back which depends on a sharper VoC. The chain shows. If items are independent, the roadmap is just a to-do list, not a plan.

4. **Honest gaps.** The "What I did not synthesise" section is real and specific. A roadmap with no gaps is dishonest.

## What to do with the roadmap

1. Read it Sunday evening before the workshop closes (or on the metro after).
2. Pick the Week 1 item with the highest impact-to-effort ratio. Block 2 hours on Monday.
3. Run the relevant teammate, ship the action.
4. Move down the Week 1 list as time allows during the week.
5. Sunday: re-read the roadmap. Update Week 2 if the world has changed.
6. Re-run the Captain for the next 90-day roadmap in 90 days. Compare.

A founder who does this religiously for 4 quarters is running the brand on a system. The system gets sharper every quarter.

## What this is NOT

- **Not a guarantee.** The roadmap is a synthesis at one point in time. The world changes; the plan changes.
- **Not a substitute for taste.** The Captain reads what the teammates wrote. If the teammates wrote thin or wrong things, the roadmap is thin or wrong. Garbage in, garbage out.
- **Not the strategy.** The roadmap captures execution priorities. The strategy lives in CLAUDE.md (anti-positioning, voice rules, what we will never do). Edit CLAUDE.md for strategy shifts; re-run the roadmap to operationalise.
