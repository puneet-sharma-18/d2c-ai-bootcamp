# Unit Economics, Little Lab (90-day view)

Written by the founder during pre-work. These are my numbers from running the business, not pulled live from Shopify. The Growth Analyst skill should trust this file first and use live MCP data as enrichment on top.

## Headline

We are at roughly ₹56 lakh trailing 4-week revenue, growing low single digits week on week. Margin is healthy at the SKU level, the watch metric is blended CAC because Meta has been creeping up over the last 30 days and I have not yet pinned down whether it is creative fatigue or audience saturation.

## AOV

Overall blended AOV: **₹797** (trailing 4-week average). This week landed at ₹805.

By channel (trailing 90 days, founder estimate, Shopify-adjusted):

- D2C site: ₹810 to ₹820. Free shipping kicks in at ₹699 so most carts cross that line.
- Amazon: ₹790 to ₹810. A bit lower because the diaper rash and nappy cleanser SKUs sell as singles there more often.
- Flipkart: ₹795 to ₹820. Similar shape to Amazon. Smaller volume so noisier.
- Quick Commerce (Blinkit, Zepto, Instamart): ₹780 to ₹810. Single-SKU pickups dominate, but the impulse-buy lotion runs lift it.

## Gross margin

Overall blended gross margin: roughly **62%** at the unit level before fulfilment and platform fees. After fulfilment and Amazon/Flipkart take rates the contribution margin sits closer to 38 to 42%.

By SKU (rough estimate, COGS not yet locked in CLAUDE.md, so these are my best read from invoices over the last quarter):

| SKU | Price | COGS estimate | Gross margin |
|---|---|---|---|
| LL-NDL-200 (Newborn Daily Lotion 200ml) | ₹549 | ₹195 | 64% |
| LL-CCB-050 (Cradle Cap Balm 50ml) | ₹449 | ₹138 | 69% |
| LL-BHW-250 (Bath and Hair Wash 250ml) | ₹599 | ₹245 | 59% |
| LL-DRC-030 (Diaper Rash Cream 30ml) | ₹329 | ₹118 | 64% |
| LL-COM-200 (Cold-pressed Massage Oil 200ml) | ₹599 | ₹260 | 57% |
| LL-NPC-150 (Nappy Cleanser 150ml) | ₹289 | ₹115 | 60% |
| LL-TBW-300 (Toddler Body Wash 300ml) | ₹499 | ₹200 | 60% |
| LL-NTB-050 (Night-time Balm 50ml) | ₹499 | ₹160 | 68% |
| LL-SUN-050 (Sun Mineral Sunscreen SPF30 50ml) | ₹649 | ₹290 | 55% |

Cradle Cap Balm is the margin star. It is also the strongest converter (3.1% CR on Shopify) so when paid leans into it the unit economics work hard. Sunscreen is the thinnest margin SKU because the mineral filter pricing has not come down yet.

## CAC

Target blended CAC: **₹440** over the 90-day horizon. That number is set by the contribution margin math, second-order LTV and the rate I can keep new-customer acquisition healthy without burning runway.

Current blended CAC: **₹495** this week (up from ₹420 the prior week, per Growth Analyst brief 2026-05-12). The 4-week average is sitting at ₹456. The 90-day average is closer to ₹440, so this week is the outlier, not the norm.

Channel reads:

- D2C (paid acquisition via Meta and Google): blended CAC ~₹520 to ₹620 depending on the angle mix. Meta is the swing variable. The "Hero SKU lifestyle" angle that launched May 5 is the immediate cause of the spike, ROAS 1.4x against a 2.4x to 2.6x baseline on the older angles.
- Amazon: marketplace CAC is murkier because Amazon Ads attribution is not clean. Rough estimate ₹250 to ₹300 per new customer when you exclude organic discovery, which most people land via.
- Flipkart: similar to Amazon, slightly higher because lower volume and worse ad efficiency.
- Quick Commerce: not running paid here yet. CAC effectively ~₹0 marginal because all sales come through the platform's discovery. The cost shows up as platform commission instead, around 25 to 30% take rate.

## LTV

12-month rolling LTV estimate: **₹2,150 per acquired customer.** This is a rough estimate. I am pulling from Shopify's repeat customer data plus my own tracker that pings the warehouse for repeat orders by customer email. The 12-month horizon is the cleanest because the baby care category has a natural 12 to 18 month buyer lifecycle (kid grows out of newborn stage, parent re-buys for next stage, then often churns to a different brand).

Shopify says ₹1,980 for the 12-month cohort but I think the truth is ₹2,150 once you fold in marketplace cross-purchases (a D2C customer who later buys on Amazon, where I cannot stitch the identity). Will tighten this once we run the full 12-month cohort pull in Module 9 POWER mode.

LTV to CAC ratio at target: ₹2,150 / ₹440 = 4.9x. At this week's CAC of ₹495, the ratio is 4.3x. Both are healthy. The alarm fires if blended CAC crosses ₹540 sustained for 3 weeks, because the ratio drops below 4x and reinvestment slows.

## Channel mix (90-day, % of revenue)

- D2C site: **~55%**
- Amazon: **~30%**
- Flipkart: **~8%**
- Quick Commerce: **~7%**

This week's split (per Growth Analyst brief 2026-05-12) is D2C ₹8.15L, Amazon ₹4.45L, Flipkart ₹1.19L, Quick Commerce ₹1.04L. That maps to 55%, 30%, 8%, 7% almost exactly, so the 90-day view is holding.

## Repeat purchase rate

90-day rolling repeat purchase rate: **~26%** of orders in any given week come from customers who have purchased at least once before. This is rough estimate because Shopify's definition (any prior order) is broader than what I track internally (prior order in last 180 days).

This week the brief shows 28%, prior week was 27%. The direction is right. The Cradle Cap Balm is a one-and-done problem solver so it does not drive repeat, but the Daily Lotion and Massage Oil do. The repeat number should keep drifting up as the lotion and oil cohorts mature.

## Notes and uncertainties

- COGS per SKU is my best estimate from invoices. I have not yet sat down with the CFO to lock the standard cost cards. Next month's plan. Once locked I will update CLAUDE.md Section 4 and re-derive margins here.
- LTV is the softest number on this page. The Shopify 12-month pull is queued. I expect ₹2,150 to shift by ±15%.
- CAC for Amazon and Flipkart is hand-waved. True marketplace CAC needs a cohort study I have not run yet.
- Quick Commerce contribution margin after platform commission is something I have not modelled cleanly. The 25 to 30% take rate hurts on the lower-priced SKUs (Diaper Rash Cream, Nappy Cleanser) more than the higher-priced ones.
- Cross-channel halo (a Meta ad that drives an Amazon purchase) is unattributable in my current stack. I assume it is real and probably worth 10 to 15% on Meta ROAS, but I do not bake it into the unit economics here.
