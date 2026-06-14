# The 5 Ad Angles

The Performance Marketer subagent uses these 5 canonical D2C ad angles. Each angle anchors on a specific input from the Day-1 chain. This document defines what each angle looks like, what makes it land, and what to avoid.

In DEFAULT scope, the subagent picks the 2 strongest angles for your brand. In POWER scope, all 5 run in parallel.

## Angle 1 — Hero SKU

**What it is.** The flagship-product ad. Names the SKU, names its USP, asks for the click.

**Anchored on**: CLAUDE.md Section 4 top SKU + its one-line USP.

**Lands when**: the founder has a clear hero (Pareto: 30%+ of revenue from one SKU) and a USP that survives a 5-second read.

**Avoid**: turning this into a generic "buy our stuff" ad. The hero angle is about the ONE thing that makes the hero SKU different from every other SKU in the category.

**Little Lab example**:
```
Newborn Daily Lotion. We list every ingredient on the bottle, top to
bottom, with the % w/w where the regulator allows it. The other "natural"
brands hide it. Pick the one that does not.
```

## Angle 2 — Problem-solver

**What it is.** Names a specific customer problem (from VoC), shows the SKU as the answer.

**Anchored on**: the top theme in `my-work/voice-of-customer/<date>.md` that names a pain point.

**Lands when**: VoC has a theme with 10+ messages mentioning the same problem. The customer recognises themselves in the ad.

**Avoid**: making up the problem. If VoC theme #1 is "delivery speed" and you write a "feel good" lifestyle ad, the customer does not connect. Use the actual top theme.

**Little Lab example** (VoC theme #2 = "cradle cap"):
```
Three weeks of cradle cap. You tried coconut oil, you tried baby brush,
you read four blogs. Cradle Cap Balm names the active and lists the % w/w.
Two-week course. Done.
```

## Angle 3 — Anti-positioning

**What it is.** Names what the brand will never do, lets the customer fill in why.

**Anchored on**: CLAUDE.md Section 3 "what we will never do" line.

**Lands when**: the anti-positioning is genuinely brand-specific (not a category cliche). Strong anti-positioning is the most distinctive ad copy you can write because no competitor can run the same line.

**Avoid**: generic "no parabens, no sulphates" lists that every competitor runs. Pick the SPECIFIC thing this brand will not do that competitors actually do.

**Little Lab example**:
```
We will never use the word "natural" on a Little Lab label. The category
ruined it. Read the ingredient list instead. Top to bottom. That is the
test.
```

## Angle 4 — Social proof

**What it is.** Real customer quote, real persona, real situation. Lets the customer self-identify.

**Anchored on**: VoC verbatim quote + persona card.

**Lands when**: the quote is specific (mentions the SKU, the problem, the result, in the customer's own words). Generic "5-star" testimonials do not move purchase intent.

**Avoid**: fabricated quotes, stock-photo testimonials, or quotes too polished to be real. The voice of customer skill saves real quotes; use those, attributed to the persona ({customer-A} from VoC) not to a fake name.

**Little Lab example**:
```
"I returned three other brands. This one shipped with a paper insert
listing every ingredient and the lab report number. Trust closed in 30
seconds." — Mumbai mom, 32, second-time buyer.

Newborn Daily Lotion. The one that prints the receipt.
```

(The quote is from VoC. The attribution is the persona card, not a name.)

## Angle 5 — Competitor gap

**What it is.** Names a category-wide gap (without naming a competitor by name in paid copy, which most platforms restrict). The customer recognises which brand the gap belongs to.

**Anchored on**: Market Analyst report's "content gap we can attack" line, plus the "where they beat us / where we beat them" table.

**Lands when**: the gap is true, observable on competitors' websites, and matters to the persona.

**Avoid**: naming a competitor directly in copy (Meta and Google block comparative claims that name another brand). Use category-level language ("most natural baby brands", "the leading category players") that the customer can map themselves.

**Little Lab example**:
```
Most "natural" baby brands print 3 ingredients on the front and bury 18
on the back. Little Lab prints all 21, in order, with %s where the
regulator allows. The label is the proof.
```

## How the subagent picks 2 angles in DEFAULT scope

The Performance Marketer subagent in DEFAULT scope picks the 2 angles most likely to land for this specific founder. The decision tree:

1. **Angle 1 (Hero SKU) is almost always picked.** Every D2C brand has a hero, and the hero ad is the workhorse.
2. **The second angle is one of 2, 3, 5**, picked by:
   - If VoC top theme has 15+ messages naming a specific problem → **Angle 2**
   - If Market Analyst flagged a clear, exploitable content gap → **Angle 5**
   - If neither is strong but CLAUDE.md anti-positioning is sharp → **Angle 3**
3. **Angle 4 (Social proof) is rarely picked in DEFAULT** because it needs strong VoC AND a quote that maps cleanly to a persona. POWER runs it for breadth; DEFAULT skips for token discipline.

The subagent announces its 2 picks before producing. Founder can override.

## What each angle's folder looks like

After the subagent runs (DEFAULT or POWER), each angle gets a folder:

```
my-work/performance-marketer/<date>-angle-<N>-<slug>/
  meta.md           # 5 (default) or 10+ (power) Meta ad variations
  google.md         # 3 + 2 (default) or 5 + 3 (power) Google ads
  creative-brief.md # 1 brief for the design team or AI image tool
```

In POWER, all 5 angle folders exist. The parent's `<date>-index.md` lists them with the Top 5 reads.

## What the subagent does NOT produce

- **Display ads (banner ads on third-party sites).** Different format, different platforms. Out of scope.
- **YouTube TrueView scripts.** Long-form video. The Reel script in Day 1's Content Lead is the closest existing artifact; YouTube long-form is take-home.
- **Influencer briefs.** Different shape. Future module if cohort demand surfaces.
- **Programmatic / DSP buys.** Out of scope.

The Performance Marketer ships Meta + Google ad copy + briefs. That is the job.
