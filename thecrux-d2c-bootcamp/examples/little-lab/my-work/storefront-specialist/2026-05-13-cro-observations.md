# CRO Observations — Little Lab Storefront — 2026-05-13

## Observation 1: PDP banned-word audit
- **Where**: All 9 SKU pages
- **The issue**: 4 of 9 PDPs use "natural" or "gentle" or "premium" — all on CLAUDE.md ban list (Section 7 voice rules).
- **Evidence**: Manual scan of Shopify product descriptions. Newborn Daily Lotion: "gently nourishes". 2-in-1 Wash: "natural ingredients". Diaper Rash Cream: "premium plant-derived". Massage Oil: "natural cold-pressed".
- **Suggested fix**: Bulk find-and-replace pass, replace each banned word with an ingredient-specific or sourced phrase. e.g. "natural ingredients" → "12 named ingredients".
- **Impact estimate**: Medium (brand-voice consistency, slight conversion lift on the technical-parent persona)
- **Effort**: Day

## Observation 2: Cart abandonment driven by shipping clarity
- **Where**: Cart page, particularly Tier-2 pin codes
- **The issue**: Cart abandonment is 41% for 2-in-1 Wash and 35% blended. VoC theme 7 (Tier-2 delivery delay) shows customers in Tier-2 hesitate after seeing the delivery date.
- **Evidence**: Shopify MCP cart abandonment by SKU + VoC support tickets (12 of 28 mention delivery timeline). 6 of those 12 are pre-purchase WhatsApp.
- **Suggested fix**: Show estimated delivery date for the entered pin code prominently in cart, BEFORE checkout. Add a "we are working on this" note for non-metro pin codes — VoC theme shows customers value the transparency more than the speed.
- **Impact estimate**: High (Tier-2 is ~30% of orders and 60% of cart abandons)
- **Effort**: Week (Shopify app required or custom liquid edit)

## Observation 3: Trust signals on PDP are below the fold
- **Where**: All SKU pages
- **The issue**: Paediatric panel mention, certifications, and the "14-day refund" line are all below the fold. The technical-parent persona scans the top of the page in ~10 seconds; if these are not visible, they bounce.
- **Evidence**: VoC theme 2 (ingredient transparency, 16%) + theme 6 (paediatrician channel, 13%) point at trust as a decision driver. Current PDP structure buries the proof.
- **Suggested fix**: Move the paediatric panel mention to a horizontal trust strip directly under the hero image. Add the refund policy as a chip near the Add-to-Cart button.
- **Impact estimate**: High (top-of-funnel decision-driver visibility)
- **Effort**: Day

## Observation 4: Reviews on PDP are too few, too clustered
- **Where**: All SKU pages
- **The issue**: PDPs show ~5 reviews each, all 4 to 5 stars, no temporal distribution. Looks curated and therefore suspect.
- **Evidence**: D2C reviews: 28 total in last 30 days, distributed across 4 SKUs. The Newborn Daily Lotion shows 5 reviews; we have 14 mentions in VoC.
- **Suggested fix**: Pull all real reviews onto the page, show negative reviews too (the 2-star 2-in-1 wash reviews are credibility-building, not credibility-destroying). Filter by date, show the most recent first.
- **Impact estimate**: Medium (trust signal, especially for first-time visitors)
- **Effort**: Day (Shopify app or theme edit)

## Observation 5: No paediatrician-referred buyer path
- **Where**: Site-wide, no dedicated landing
- **The issue**: 13% of VoC mentions are paediatrician-referred. They are a distinct persona with distinct intent (they want to verify the active and the dose), but the current site has no path that serves them.
- **Evidence**: VoC theme 6 (paediatrician channel) + persona card "Paediatrician-referred parent 32-42". Repeat-purchase rate for this segment is ~40% higher than D2C-only.
- **Suggested fix**: Build /paediatricians page with: the active and % per SKU, the review panel, the trade pricing form, the clinic order tracker. Link from PDP "For paediatricians" chip and from email signature.
- **Impact estimate**: High (segment is small but highest LTV)
- **Effort**: Week (page + workflow)

## Sources cited
- Shopify MCP at 2026-05-13 11:42 IST
- my-work/voice-of-customer/2026-05-12-voc-report.md
- my-work/market-analyst/2026-05-12-intel-report.md
