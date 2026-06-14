# WhatsApp Template — Delivery Experience Check-in (Summer Variant)
Trigger: 3 days after delivery confirmation
Segment: All first-time buyers + summer-insulated orders to high-temp pin codes
Tone: Founder voice, no upsell
Allowed personalisation tokens: {first_name}, {sku_short_name}

## Body
Hi {first_name}, quick check — did your {sku_short_name} arrive intact and stay cool? Reply 🟢 if all good. Reply with details if anything is off and I will personally fix it.

## CTA
🟢 → close, log positive signal, summer-pin lane SLA tracked
Any text → routed to founder inbox + Ops watchlist

## When NOT to send
- Damaged order already flagged by Ops
- Customer in do-not-WhatsApp list
- Repeat buyer with 3+ orders to non-summer-pin codes (over-messaging)

## Compliance
- Service tier (post-purchase check)
- Reply triggers 24-hour service window per WhatsApp Business Policy

## Source
my-work/voice-of-customer/2026-05-12-voc-report.md → Theme 7 (summer freshness) + Ops Manager SOP-01 step 6
