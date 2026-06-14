# WhatsApp Template — Delivery Experience Check-in
Trigger: 3 days after delivery confirmation
Segment: All buyers, first delivery only (do not send on every order for repeat buyers)
Tone: Founder voice, conversational, no upsell
Allowed personalisation tokens: {first_name}, {sku_short_name}

## Body
Hi {first_name}, just checking your {sku_short_name} reached you and the bottle is intact. If something is off with the order or the delivery, hit reply and I'll personally fix it. If all good, please reply with a 👍 and I'll stop bothering you.

## CTA
👍 → close the check-in, log positive signal
Any text → routed to founder inbox (NOT auto-responded)

## When NOT to send
- Order had a known damage / wrong-item incident (handled by Ops separately)
- Customer is in the do-not-WhatsApp list
- Order was a re-purchase from a customer with 3+ previous orders (signal: established trust, do not over-message)

## Compliance
- Service conversation tier (post-purchase) — does not need promotional opt-in
- Reply triggers a 24-hour service window, normal Business Policy

## Source
my-work/voice-of-customer/2026-05-12-voc-report.md → Theme 7 (delivery friction) — surfaces Tier-2 issues early when customers respond to this check-in
