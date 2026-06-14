# WhatsApp Template — Replenishment Prompt (Cradle Cap Balm)
Trigger: 35 days after a Cradle Cap Balm 50ml order, no re-order, not opted out of WhatsApp marketing
Segment: First-time and repeat buyers, Cradle Cap Balm cohort
Tone: Founder voice. WhatsApp-warm, not promotional-corporate.
Allowed personalisation tokens: {first_name}, {sku_short_name}, {discount_code} (optional)

## Body
Hi {first_name}, Riya here from Little Lab. Your Cradle Cap Balm should be just about running out — most parents finish the 50ml in 5 to 6 weeks of twice-daily use. Reply YES if you'd like me to ship a replacement. If you'd rather not, reply STOP and I'll take you off these notes.

## CTA
"YES" → triggers a one-click reorder flow link (sent in the follow-up message)
"STOP" → adds to do-not-WhatsApp list, founder notified

## When NOT to send
- Customer has already re-ordered Cradle Cap Balm in last 28 days (Shopify check before send)
- Customer has an open support ticket
- Customer has opted out of WhatsApp marketing
- Cradle Cap Balm is currently out of stock (do not promise what we cannot ship)

## Compliance
- WhatsApp Business Policy: this is a utility template (post-purchase reminder), eligible for the lower-cost service-conversation tier
- Opt-in required from order confirmation flow
- "STOP" handler must be wired in WATI / Interakt config

## Source
my-work/voice-of-customer/2026-05-12-voc-report.md → Theme 5 (subscription / re-order friction, 8% of mentions)
