# Vendor Email — Insulated Box Supplier (Summer Cold-Chain)
Use when: Onboarding a new insulated-packaging vendor before May 1 each year, OR placing the seasonal forecast order for May-September shipping volume.
Trigger: Fired from SOP-01 (Summer Shipping) Step 3.
Tone: Direct, forecasting-grade. The vendor needs numbers, not narrative. Short paragraphs.

## Subject lines (3 variants)
1. Insulated box order: May-Sep 2026 forecast + samples
2. Cold-chain packaging RFQ: {N} units, {dispatch_date}
3. Annual insulated-pack order, May to Sep, please quote

## Body

Hi {vendor-contact},

Writing with our summer 2026 insulated packaging forecast for The Paan Legacy.

### Volume forecast (May to September 2026)

| Month | Estimated units | High-temp pin codes (% of total) |
|---|---|---|
| May | ~{N} | ~30% |
| June | ~{N} | ~35% |
| July | ~{N} | ~35% |
| August | ~{N} | ~30% |
| September | ~{N} | ~20% |
| **Total Mar-Sep** | **~{N}** | **avg ~30%** |

Numbers are based on 2025 actuals adjusted for projected 2026 growth (~25% volume lift YoY).

### Specifications needed

- **Box size**: 200mm x 150mm x 60mm internal (fits one Almond Delight + one Dry Fruit Meetha Paan dual-pack)
- **Insulation**: EPS foam or equivalent, ~12mm wall thickness, R-value sufficient to hold 22°C internal for 36h at 38°C external
- **Gel pack pocket**: dedicated cavity for our 200g gel pack at the top of the box, not loose
- **Outer carton**: corrugated B-flute, FSSAI-approved food-contact certified
- **Print**: white outer, brand wordmark single-colour, no laminate finish (food-safe heat tolerance)
- **Tamper evidence**: brand-sticker seal on the lid edge

### Questions for your quote

1. Per-unit price at the volume tiers above. We are willing to commit to a 50% min-order with rolling delivery if it improves the per-unit price.
2. Lead time from PO to first batch delivery. We need our first 1,000 units in our warehouse by April 25 to have a clean May 1 cutover.
3. Gel pack supply: do you offer the 200g gel pack as a paired item, or do we source separately? Cost comparison either way please.
4. Returns of unused inventory at season end (October). What is your buy-back policy?
5. FSSAI-approved food-contact certification — please attach the certificate with your quote response.

### Our commitment

- We will issue a formal PO within 7 days of receiving your quote
- 50% advance on PO confirmation, 50% balance on final delivery
- Long-term: if 2026 works, we are open to a 3-year annual contract from 2027 with negotiated rate-lock

Please respond with a quote and lead-time confirmation within 7 working days. If you have any questions on specifications, call me directly: {founder_phone}.

Best
Puneet
Founder, The Paan Legacy

## What to attach
- Our previous-year purchase order (2025 reference, if applicable) for context on relationship history
- Photo of our current product packaging so the vendor can spec the internal fit
- FSSAI license + GST registration (vendor will ask)

## What NOT to write
- Do not commit to specific per-unit prices in writing before quote comparison (we are RFQ-ing 3 vendors in parallel)
- Do not name competing vendors in writing
- Do not commit to multi-year contract terms in the first email — keep that for the second round once price + quality are validated

## If they do not reply within 7 working days
- Phone call to the contact. If no answer, escalate to their sales head
- Move to vendor B (we always RFQ 3 vendors in parallel for this category, so vendor B is already in our pipeline)
- Adjust SOP-01 timeline: every 2-day vendor delay pushes our May 1 cutover by 2 days

## Personalisation depth
- `{vendor-contact}` — required
- `{N}` volume forecasts — required, must reflect actual Shopify + Zomato + Swiggy projection
- `{founder_phone}` — fixed

## Documentation
- Every insulated-box vendor interaction logged in `my-work/ops-manager/vendor-pipeline.md` (POWER scope)
- 3-vendor RFQ is the standard; never single-source for a seasonal-critical input

## Source
my-work/voice-of-customer/2026-05-12-voc-report.md → Theme 7 (summer freshness, 6% complaint rate without insulation, target <2% with it). my-work/growth-analyst/2026-05-12-brief.md → summer pin-code complaint alarm. SOP-01 Step 3 packing instruction depends on this vendor being live.
