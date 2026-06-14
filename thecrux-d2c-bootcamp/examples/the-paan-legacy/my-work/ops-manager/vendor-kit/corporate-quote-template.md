# B2B Quote — Corporate Diwali Gifting (Standard Tier)
Use when: A corporate inquiry has cleared SOP-02 Step 3 (sample box delivered) and is requesting a formal quote for an order of 25 to 200 boxes.
Trigger: Fired from SOP-02 Step 4.
Tone: Direct, professional, no salesperson-speak. The HR or admin person reading this is comparing us to Karachi Bakery and Bombay Sweet Shop on a spreadsheet. The quote does the selling; the cover note does the relationship.

## Subject line
{company_name} Diwali 2026 — Quote and timeline ({box_count_estimate} boxes)

## Cover note (above the formal quote)

Hi {first_name},

Quote attached for {company_name}'s Diwali 2026 gifting. Two things to flag upfront before you open the numbers:

1. **The PO lock-in deadline is July 30.** Our production schedule for October delivery has a hard upstream constraint (custom packaging artwork to vendor by August 31, ingredient procurement 6 weeks before pack). Late confirmations between August 1-15 are possible at a 10% premium. After August 15 we will most likely have to say no.

2. **Our base price assumes our standard packaging.** Custom logo sleeves are a separate ₹40/box add-on for any order over 50 boxes. If you want a fully custom box (not a sleeve, the box itself), that is a separate conversation and we typically reserve it for orders over 200 boxes given the artwork and minimum-print costs.

Quote details below. Reply with any questions and I will respond within the same day during the work week.

Best
Puneet
Founder

---

## Formal quote

**To**: {first_name} {last_name}, {role}, {company_name}
**From**: The Paan Legacy
**Quote ID**: {quote-id}
**Quote date**: {date}
**Valid until**: {date+14}

### Order summary

| Line item | SKU mix per box | Qty boxes | Unit price (incl GST) | Subtotal |
|---|---|---|---|---|
| Diwali Gifting Box - Standard | 1 Almond Delight + 1 Dry Fruit Meetha Paan | {box_count} | ₹599 | ₹{subtotal} |
| Custom logo sleeve (optional) | — | {box_count} | ₹40 | ₹{sleeve_total} |
| Shipping (pan-India, insulated for high-temp lanes) | — | — | Included | ₹0 |
| **Total (incl GST)** | | | | **₹{grand_total}** |

### Payment terms

- 50% advance on PO confirmation. Wire transfer or RTGS to {bank-details}.
- 50% balance 7 working days before scheduled delivery date.
- Invoice will be raised in {company_name}'s name; GST {gst-number} on file.

### Delivery

- Confirmed delivery dates: October 10 to October 30, 2026 (Diwali window).
- Specific delivery date locked when PO is confirmed.
- Single delivery location or multiple? If multiple, please attach the address list with the PO and confirm if any location is in a high-temp pin code (we ship those in insulated boxes; no extra charge).

### What is included

- {box_count} boxes, each containing one Almond Delight (50g) and one Dry Fruit Meetha Paan (60g) hand-roasted in our small-batch kitchen
- Every box carries FSSAI license {license-number}, full ingredient list, allergen disclosure (tree nuts: almond, cashew)
- Tobacco-free certification visible on each box
- Standard "The Paan Legacy" outer packaging with the brand wordmark
- A 2-line personalised note from {company_name}'s leadership (text confirmed at PO stage)
- Pan-India shipping, insulated for May-September lanes

### What is NOT included

- Custom box design (artwork to print, separate quote)
- Hindi or other-language packaging (English-only at this price)
- Express delivery in under 5 days from dispatch
- Cold chain in metro lanes (we use room-temperature shipping for metro; insulated for high-temp lanes only)

### Compliance + safety

- FSSAI License: {license-number} (manufacturing) + {state-license} (state)
- Allergen disclosure on every box: contains tree nuts (almond, cashew); manufactured in a facility that handles sesame and dairy
- Each box is suitable from age 6+
- Tobacco-free, supari-free, eat-and-swallow product across the entire range

### Cancellation policy

- Full refund if cancelled 30+ days before scheduled delivery
- 50% refund (advance retained) if cancelled 15-29 days before delivery
- No refund if cancelled within 14 days of delivery (production already committed)

### Founder line

Direct line to founder for this account during the active engagement: {founder_phone}, {founder_email}. For day-to-day coordination after PO is confirmed: {coordinator_phone}, {coordinator_email}.

---

## Personalisation depth (placeholders to fill)
- `{first_name}`, `{last_name}`, `{role}`, `{company_name}` — required
- `{quote-id}` — auto-generated, must be unique (format: TPL-Q-2026-{NNN})
- `{box_count}` — required, integer
- `{subtotal}`, `{sleeve_total}`, `{grand_total}` — auto-computed (Sheets formula or in-house tooling)
- `{license-number}`, `{state-license}` — fixed, do not vary
- `{bank-details}` — fixed, internal Ops document
- `{founder_phone}`, `{founder_email}`, `{coordinator_phone}`, `{coordinator_email}` — fixed, vary only when team grows

## When NOT to use this template
- Orders under 25 boxes: use the standard D2C checkout with the bulk-discount code, no formal quote needed
- Orders over 200 boxes: handle as custom quote; this template is the floor, not the ceiling
- Wedding orders (different SKU mix, different timeline pressures) — use the wedding variant of this template (POWER scope, queued)
- Repeat corporate customers: skip the cover note's "lock-in deadline" paragraph (they already know)

## Compliance
- Every published number (price, FSSAI, GST) must be the current accurate figure
- Quote ID must be logged in `my-work/ops-manager/corporate-pipeline.md` (POWER scope) for tracking
- 14-day quote validity is the standard; do not extend beyond 30 days without re-checking ingredient costs

## Source
my-work/voice-of-customer/2026-05-12-voc-report.md → corporate-gifting persona, WhatsApp Thread 3 ({customer-G}, 80-box order). my-work/market-analyst/2026-05-12-intel-report.md → Karachi Bakery May 5 corporate launch sets the pace.
