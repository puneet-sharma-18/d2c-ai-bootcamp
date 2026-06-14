# Sample Inputs, The Paan Legacy

Sample raw data that simulates Module 3 (MCPs) live pulls for The Paan Legacy. Mirrors `examples/little-lab/sample-inputs/` in shape; differs in source mix (Zomato, Swiggy and WhatsApp Business dominate; no Amazon or Flipkart for this brand).

## Files

- `shopify-products.csv`. 6 SKUs with price, inventory, units sold last 28 and 90 days, conversion rate, rating, review count.
- `shopify-orders-28d.csv`. 28 days of order rollups (2026-04-15 to 2026-05-12) by channel and day. Channels: D2C site, WhatsApp Business, Zomato and Swiggy. Columns: date, channel, orders, revenue_inr, new_customers, repeat_customers, aov_inr. Week 4 totals match the 2026-05-12 Growth Analyst brief.
- `zomato-swiggy-reviews.csv`. 14 reviews from Zomato and Swiggy across April-May 2026. Mix of positive (heritage, spit-free) and negative (summer melt).
- `whatsapp-orders.md`. 5 sample WhatsApp Business threads covering pre-purchase clarification, allergen check, corporate gifting (5 months early), summer melt, repeat-buyer subscription ask.
- `meta-ads-spend.csv`. 28 days of Meta ad spend by campaign and day. Four campaigns: Heritage Ritual (best performer), Modern Cranberry (solid), Festival Gifting Dry Fruit Box (mid) and Summer Gifting Almond Delight Hot Cities (bleeding this week, launched late in Week 3). Columns: date, campaign_id, campaign_name, angle, spend_inr, impressions, clicks, conversions. Week 4 spend ₹1,55,000 and 384 conversions tie to the brief.
- `google-ads-spend.csv`. 28 days of Google Ads spend by campaign and day. Three campaigns: Brand Search, Non-brand Paan Search and Gifting Long-tail. Columns identical to meta-ads-spend.csv. Week 4 spend ₹19,100 and 78 conversions tie to the brief.

## Reconciling totals with the brief

The 2026-05-12 weekly brief reports headline orders of 1,034 and headline revenue of ₹7,82,000 for the week of 2026-05-06 to 2026-05-12. The four-channel CSV totals 1,008 orders and ₹7,82,000 for that week. The 26-order delta is the franchise outlet self-report (Mumbai BKC, Pune Koregaon Park, Delhi GK-I), which is not in any of the digital sources because there is no live POS integration. Franchise revenue (~₹35,000 for the week) is also excluded from the digital revenue total; the brief's per-channel table breaks it out separately.

Within the CSV, D2C site and WhatsApp Business share fulfilment and roll up to the brief's "D2C site" line: 520 + 92 = 612 orders, ₹4,00,200 + ₹69,000 = ₹4,69,200 revenue, matching the brief's "D2C site" row exactly.

## How to use as input

In the VoC skill: "I have a CSV at `examples/the-paan-legacy/sample-inputs/zomato-swiggy-reviews.csv` and WhatsApp threads at `whatsapp-orders.md`. Mine them."

Output should look like `my-work/voice-of-customer/2026-05-12-voc-report.md` in this same examples folder.

In the Growth Analyst skill, when the founder has no live Shopify, Meta or Google MCP yet: "I have sample inputs at `examples/the-paan-legacy/sample-inputs/shopify-orders-28d.csv`, `meta-ads-spend.csv` and `google-ads-spend.csv`. Treat these as the 28-day pulls. My unit economics are in `brand-brain/unit-economics.md`. Run the brief."

Output should look like `my-work/growth-analyst/2026-05-12-brief.md` plus the dashboard HTML in the same folder.
