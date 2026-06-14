# D2C Marketplace Sample Data

Backup dataset for the Claude for D2C bootcamp. Use when MCP / live API access is not available.

## Fictional brand context

**Auruh** is a D2C skincare brand listed on Amazon India and Flipkart. 5 SKUs:

| Internal SKU   | Product                          | MRP (INR) |
|----------------|----------------------------------|-----------|
| AUR-FW-100     | Vitamin C Face Wash 100ml        | 599       |
| AUR-SS-50      | Mineral Sunscreen SPF 50, 50ml   | 749       |
| AUR-LB-15      | Tinted Lip Balm 3-pack           | 449       |
| AUR-BL-200     | Body Lotion 200ml                | 549       |
| AUR-HO-100     | Cold-Pressed Hair Oil 100ml      | 399       |

Data window: April 2026.

## File index

### Amazon (`amazon/`)
| File | Real-world source | What it shows |
|------|---|---|
| `orders.json` | SP-API `GET /orders/v0/orders` | 30 days of orders, status, value, geography. PII masked as on real API. |
| `sales-and-traffic-report.json` | SP-API Reports `GET_SALES_AND_TRAFFIC_REPORT` | Sessions, page views, conversion rate, buy box % per ASIN per day. The single highest-leverage report for D2C. |
| `inventory.json` | SP-API FBA Inventory `getInventorySummaries` | FBA stock with fulfillable, reserved, inbound. |
| `ads-search-terms.json` | Ads API Sponsored Products search term report | Search term level spend, sales, ACOS, conversions. |
| `settlement-report.json` | SP-API Reports `GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE` | Per-transaction breakdown of fees, commission, shipping, net payout. |
| `brand-analytics-search-terms.json` | Brand Analytics Top Search Terms (Brand Registry only) | Top searches in category with click share and conversion share by ASIN. |
| `returns-report.json` | SP-API Reports `GET_FBA_FULFILLMENT_CUSTOMER_RETURNS_DATA` | Returns with reason codes. |

### Flipkart (`flipkart/`)
| File | Real-world source | What it shows |
|------|---|---|
| `orders.json` | Flipkart Marketplace API `POST /orders/search` | Flipkart order item list with FSN, SKU, status. |
| `listings.json` | Marketplace API `GET /listings/v3/locations/{loc}/skus` | Listing state, price, stock. |
| `settlement.json` | Seller Hub Settlement Report (CSV-equivalent JSON) | Commission, collection fee, fixed fee, shipping fee per order item. |
| `returns.json` | Marketplace API returns | Customer returns and RTO with reason codes. |
| `pla-ads-report.json` | Flipkart Ads (PLA) reports | Sponsored Products campaign performance. |

## Embedded patterns to coach attendees toward

These are the "aha" moments Claude should find when given the data:

1. **AUR-SS-50 has a listing problem.** Sales & Traffic shows 4x the page views of AUR-FW-100 but a third of the conversion. Hypothesis: weak A+ content, missing reviews, MRP positioning.
2. **AUR-LB-15 is about to stock out on Amazon and overstocked on Flipkart.** Amazon FBA fulfillable is 47 units with 12-day sell-through. Flipkart has 380 units with 90-day cover. Inventory rebalance opportunity.
3. **Ads on AUR-HO-100 are bleeding money.** Search term report shows high spend on "baby hair oil" and "ayurvedic hair oil" with ACOS > 80%. Need negative keywords.
4. **AUR-BL-200 has a 14% return rate** with reason codes clustering on "leaked in transit" and "broken". Packaging problem, not product.
5. **Flipkart commission on AUR-LB-15 is 28%** vs Amazon 15%. Settlement-level margin gap is wider than visible at the top line.
6. **Brand Analytics shows "natural sunscreen india" with high search frequency rank but Auruh ranks #14.** Organic SEO opportunity that ads can't fix.
7. **Customer PII is masked on both platforms.** Use this to teach why D2C brands need a parallel website for retention.

## Suggested bootcamp flow

1. Drop the entire `d2c-marketplace-samples/` folder into the working directory.
2. Ask Claude: *"You are my D2C analyst. Read the marketplace data in this folder and tell me what to fix this week, in priority order."*
3. Watch Claude triangulate across Sales & Traffic + Ads + Returns + Settlement.
4. Follow up: *"What does my unit economics look like by SKU after marketplace fees?"* — forces a join across orders and settlement.
5. Closing exercise: *"Write me an inventory transfer recommendation between Amazon FBA and Flipkart for the next two weeks."*

## What this dataset deliberately omits

- Customer PII (matches real API behaviour since 2020)
- Real ASINs / FSNs (these are synthetic but well-formed)
- Multi-marketplace consolidation (no Meesho / Myntra / Nykaa here, keep it focused)
- Live ad bidding data (Marketing Stream / streaming endpoints)

## If you want to attempt MCP live instead

There is no official Amazon SP-API or Flipkart MCP server. Community options exist on GitHub but auth setup (LWA refresh tokens, Flipkart OAuth) takes 30+ minutes and tends to fail mid-demo. Recommended: have this static dataset open in a second window as the fallback.
