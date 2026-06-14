# Sample Inputs, Little Lab

These files simulate what Module 3 (MCPs) would pull live from the founder's actual Shopify, Drive, Gmail, Meta Ads and Google Ads accounts. Use them for:

1. **Module 2** as a paste-in fallback if a founder's own review export is not ready.
2. **Module 3 demo** to show what the MCP-pulled data looks like before founders connect their own.
3. **Module 9 (Growth Analyst)** so founders without Shopify or ads MCPs connected still get a complete weekly dashboard.
4. **Catch-up** if a founder is behind on Module 3, they can paste the CSV path into the relevant skill to keep the chain moving.

## Voice of Customer inputs (Module 2)

- `shopify-products.csv`. 9 SKUs with price, inventory, units sold last 28 / 90 days, conversion rate, rating, review count. Simulates `mcp__shopify__search_products` plus an analytics pull.
- `reviews-export.csv`. 18 reviews across Amazon, D2C and Flipkart from April 15 to May 11 2026. Spans positive (cradle cap wins, ingredient transparency) and negative (2-in-1 wash lather, Tier-2 delivery delay).
- `support-tickets.csv`. 13 support tickets across email and WhatsApp, covering the same patterns plus pre-purchase friction (price, ingredient questions, bottle size).
- `gmail-support-threads.md`. 3 longer-form sample threads showing what `mcp__gmail__search_threads` returns once threads are stitched.

## Growth Analyst inputs (Module 9)

- `shopify-orders-28d.csv`. 28 days (2026-04-15 to 2026-05-12) of daily orders by channel. Channels: D2C, Amazon, Flipkart, Quick Commerce. Columns: `date, channel, orders, revenue_inr, new_customers, repeat_customers, aov_inr`. Week 4 totals reconcile to the brief at `my-work/growth-analyst/2026-05-12-brief.md`.
- `meta-ads-spend.csv`. Day-level Meta Ads spend by campaign and angle for the same 28-day window. Three angles: `problem-solver` and `social-proof` running the full window, `hero-sku-lifestyle` launching 2026-05-05 (this is the angle the brief flags). Columns: `date, campaign_id, campaign_name, angle, spend_inr, impressions, clicks, conversions`.
- `google-ads-spend.csv`. Day-level Google Ads spend for the same window. Two campaigns: `brand-search` and `shopping`. Columns: `date, campaign_id, campaign_name, spend_inr, impressions, clicks, conversions`.

The brand-brain file `examples/little-lab/brand-brain/unit-economics.md` is the founder-written 90-day view of CAC, LTV, AOV, margin and channel mix. The Growth Analyst skill reads that file first and uses the CSVs above as enrichment.

## How to use as input

In the VoC skill, paste:

> I have a CSV at `examples/little-lab/sample-inputs/reviews-export.csv` plus another at `support-tickets.csv`. Mine them.

The output should look like `my-work/voice-of-customer/2026-05-12-voc-report.md` in this same examples folder.

In the Growth Analyst skill, paste:

> Shopify, Meta and Google MCPs are not connected. Read `examples/little-lab/brand-brain/unit-economics.md` for the 90-day view and the CSVs at `examples/little-lab/sample-inputs/shopify-orders-28d.csv`, `meta-ads-spend.csv` and `google-ads-spend.csv` for the last 28 days. Generate the Monday brief and dashboard.

The output should match the shape of `my-work/growth-analyst/2026-05-12-brief.md`.
