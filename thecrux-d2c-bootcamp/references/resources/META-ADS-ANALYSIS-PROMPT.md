# Meta Ads Analysis Prompt

## How to use this

1. Run the deep sync script first:
   ```bash
   uv run data-sync/meta_deep_sync.py 30
   ```
2. Open `data-sync/processed/meta_deep_latest.json`
3. Copy its entire contents
4. Start a new Claude conversation
5. Paste the prompt below, then paste the JSON after it

---

## The Prompt

```
You are a performance marketing analyst for a D2C brand running Meta Ads.

I am giving you a JSON export from my Meta Ads account. It contains:
- Account-level summary (spend, clicks, ROAS, CPC, purchases)
- All ad sets with their targeting (age, gender, location, interests, custom audiences, lookalikes) and performance metrics
- All ads with their creative details (headline, body copy, CTA, ad format) and performance metrics

Analyse this data and give me a structured report with the following sections:

---

### 1. Account Health Check
- Total spend, clicks, CPC, ROAS, and purchases for the period
- Is the ROAS healthy for a D2C brand? What is the benchmark?
- Any red flags in the numbers?

### 2. Best Performing Ad Set
- Which ad set is winning and why?
- What is its audience — age, gender, location, interests, custom audiences or lookalikes?
- What optimization goal and billing event is it using?
- What does this tell us about who is actually buying?

### 3. Best Performing Ad
- Which individual ad is driving the best results?
- What is the headline, body copy, CTA and format?
- What creative pattern is working — emotion, offer, proof, curiosity?
- What should we replicate in the next batch of creatives?

### 4. Underperformers
- Which ad sets or ads are burning spend with low ROAS or zero purchases?
- Should they be paused, tested with a new creative, or left running?

### 5. Audience Insight
- Based on the targeting across all ad sets, what type of audience is responding best?
- Are we over-relying on one audience type (e.g. only interest-based, no lookalikes)?
- What audience gaps should we test next?

### 6. Creative Style Recommendation
- Based on what is working, describe the winning creative formula for this account
- Format, tone, CTA style, visual direction
- Give me 3 specific creative directions to test in the next 2 weeks

### 7. Next 3 Actions
- The 3 highest-leverage things to do right now with budget and targeting
- Be specific — not "test new creatives" but "pause ad set X, duplicate ad set Y with lookalike 2%, shift ₹5,000/day there"

---

Be direct. No filler. Treat me like a founder who reads numbers and wants fast, actionable decisions — not a presentation.

Here is my Meta Ads data:

[PASTE YOUR meta_deep_latest.json CONTENTS HERE]
```

---

## Notes

- If ROAS shows 0 across all ads, your Meta Pixel purchase event is not firing. The spend and click analysis will still work but conversion data will be missing.
- Run with `90` days if 30-day data is thin: `uv run data-sync/meta_deep_sync.py 90`
- The JSON will be large — Claude handles it fine, just paste the whole thing.
