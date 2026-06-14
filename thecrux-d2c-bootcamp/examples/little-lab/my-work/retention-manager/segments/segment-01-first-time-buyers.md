# Segment — First-Time Buyers

## Definition (rule)
Customers with exactly 1 lifetime order, AND first order placed in last 90 days, AND opted in to email marketing.

## Size estimate
~620 customers (from Shopify cohort pull on 2026-05-13). This is the largest reachable segment.

## What this segment cares about
From VoC persona "Mumbai/Bengaluru metro mom, 30-36, technical-aware":
- The product solving the specific problem they bought it for (cradle cap, dry patches, bath crying)
- Whether the price was justified
- Reassurance that they did the right thing (ingredient list confirms the choice)
- A reason to come back for a second SKU

## Templates that fire for this segment
- `email/01-welcome-first-purchase.md` — Day 7 after order
- `email/02-post-purchase-day7-cradle-cap.md` — Day 7, SKU-specific (Cradle Cap Balm only; other SKUs need parallel templates)
- `email/03-first-time-to-second-purchase.md` — Day 21
- `whatsapp/02-delivery-checkin.md` — Day 3 after delivery

## How to retarget if needed
- Meta Custom Audience: upload email list. Use for "Welcome video" creative (Performance Marketer Angle 1 — problem solver, since 60% of first-time buyers came in for a specific problem).
- Google Customer Match: same list. Use for branded keyword bidding to prevent competitor poaching at the second-purchase decision.

## Source
my-work/voice-of-customer/2026-05-12-voc-report.md → first-time-buyer voice in cohort cuts
