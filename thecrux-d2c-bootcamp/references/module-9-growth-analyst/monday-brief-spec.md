# The Monday Brief Spec

This document annotates each section of the Monday brief with what it is for, why it is the shape it is, and what to watch for. Founders who want to customise the brief read this. Instructors reference it when coaching founders past common mistakes.

## The whole thing fits on one page

The brief is a focusing tool. If it does not fit on one page (or one phone screen), it has failed. The founder reads it on the metro on the way to the office on Monday morning, decides on the action, delegates or runs it during the day. Two pages = ignored.

The skill enforces one-page output. If the founder asks for "more detail", the answer is "ask follow-up questions in chat, but the brief stays one page".

## Section by section

### Headline

One sentence. The state of the business this week.

**Good headline**: "Revenue down 8% week on week, repeat rate up 2 points. The miss is in new-customer acquisition, not retention."

**Bad headline**: "This week was a mixed bag with some interesting data points."

The headline names the metric move and the operational implication. Founders read this even if they read nothing else.

### The one alarm

The single number that needs founder attention this week. The skill picks based on:
- ±10%+ move from prior week
- ±15%+ move from 4-week average
- Crossing a critical threshold (CAC > LTV, ROAS < 1, repeat rate < 15%)

Why one and not three: a brief with three alarms has zero alarms. The founder has time for one decision. Pick the one.

Format:
```
**<Metric name>** moved <direction> by <magnitude>: from <prior> to <current>.

<2 lines: what is driving it, what the data points to>

**Recommended action this week**: <one specific thing the founder should do
in the next 7 days, with the teammate that runs it>
```

The "recommended action" is the most important line. Without it, the alarm is just news. With it, the brief is a system that points at what to do next.

### Top 3 reads

Not "top 10". Three observations beyond the alarm. Each one cites the contributing teammate output. Examples:

- "VoC theme #2 (cradle cap) generated 15 of 67 tickets this week, up from 8 last week. See `my-work/voice-of-customer/<date>-voc-live.md`."
- "Market Analyst flagged Mother Sparsh launched a refill pack on Tuesday. Their refill is ₹{30} cheaper. See `my-work/market-analyst/<date>-intel.md`."
- "Content Lead's Tuesday Instagram caption (`pieces/instagram-03`) correlated with a 5% lift in PDP visits."

Three reads keep the founder oriented without overwhelming.

### Numbers (last 7 days)

The 7 metrics that go in every brief, in a table. Same metrics every week so the founder builds intuition.

| Metric | This week | Prior week | 4-week avg | Trend |
|---|---|---|---|---|
| Revenue | | | | |
| Orders | | | | |
| AOV | | | | |
| New customers | | | | |
| Repeat purchase rate | | | | |
| Total ad spend | | | | |
| Blended CAC | | | | |
| ROAS (blended) | | | | |

The 4-week average is the noise filter. Week-on-week alone is too noisy for D2C; 4-week average shows the real trend.

If a metric cannot be computed (Meta MCP not connected, COGS not in CLAUDE.md), the row says "no data" and the gap shows up in the "What the brief did NOT cover" section.

### Per channel

| Channel | Revenue | Orders | Spend | ROAS |
|---|---|---|---|---|
| D2C site | | | n/a | n/a |
| Amazon | | | | |
| Flipkart | | | | |
| Quick commerce | | | n/a | n/a |
| Meta ads | | | | |
| Google ads | | | | |

This is where the alarm often originates. A 22% blended CAC jump usually traces to one channel. The per-channel table makes the trace fast.

For founders who have many channels (e.g. 4 marketplaces + 3 ad channels), the skill picks the top 6 by absolute revenue. The rest are "Other" with a single line.

### Cross-teammate inputs that shaped this brief

This is the auditability section. Every other teammate's output gets a line if it influenced the brief. Founders use this to trust the brief's reasoning ("the alarm cites VoC theme X, which I can verify by opening the VoC report").

If no other teammate's output influenced the brief, this section says: "This week's brief is Shopify-only; VoC and Market Analyst did not surface anything that crossed a threshold."

### What the brief did NOT cover (gaps)

Honesty section. Lists what is missing because of MCP gaps or data gaps.

Example:
- "Meta ad performance: skipped (Meta MCP not connected). Connect via `claude mcp add meta-ads` to include this in next week's brief."
- "Gross margin: skipped (COGS not in CLAUDE.md Section 4 or Shopify variant cost). Add COGS per SKU to enable."

Founders use this section to plan their next-week setup investment. By week 4, the gaps section should be empty or near-empty.

### Cited sources

Every number traces to a source. The brief lists:
- Shopify MCP timestamp
- Meta MCP timestamp (if connected)
- Google MCP timestamp (if connected)
- Any teammate output cited (`my-work/voice-of-customer/<file>` etc.)

If a number does not have a source, it does not go in the brief.

## What to watch for as the brief evolves

### Week 1
The first brief is mostly "here is the baseline". No trend data. No prior brief to compare to. Founders can be disappointed; the brief is genuinely thinner. Coach: "Week 1 sets the comparison point. Week 4 is when this gets sharp."

### Week 4
4-week average becomes meaningful. Trends start to show. The "one alarm" becomes more reliable because the threshold logic has 4 weeks of context.

### Week 12
The brief should be visibly shaping the founder's week. If the founder is still surprised by the alarm every week, either:
- The alarm threshold logic needs tuning (skill is over-flagging)
- The founder is not running the recommended action and the same alarm keeps repeating

Both are fixable.

### Month 6
The brief is reading well-populated `my-work/` folders. VoC has 6 months of themes. Market Analyst has 6 months of competitor tracking. The cross-teammate citations get richer. The brief becomes more diagnostic ("CAC up because Meta auction shifted because of Mother Sparsh's spend ramp, observed in Market Analyst weeks 5-7").

This is the compounding the workshop promised.

## Customising the brief

Founders can edit `growth-analyst/SKILL.md` to:
- Change the alarm thresholds (e.g. ±5% instead of ±10% for a tighter brand)
- Add a custom metric (e.g. "subscriber count" for a brand running a subscription model)
- Change the format (Markdown -> HTML for richer email delivery)

The skill is a starting point, not a fixed spec. Founders own it.

## What this brief is NOT

- Not a board deck. Different audience, different cadence.
- Not a P&L. Accounting lives elsewhere.
- Not a CRM dashboard. Customer-level work lives in Retention Manager.
- Not a marketing report. Channel performance is here, but creative analysis is in Performance Marketer's outputs.

The Monday brief is the founder's weekly orientation tool. Everything else is somewhere else.
