# WhatsApp Template — Replenishment Prompt (Meetha Paan / Almond Delight)
Trigger: 40 days after a Meetha Paan or Almond Delight order, no re-order, opted in to WhatsApp marketing
Segment: Repeat buyers, family-ritual persona
Tone: Founder voice. WhatsApp-warm. Founder's name signed.
Allowed personalisation tokens: {first_name}, {sku_short_name}

## Body
Hi {first_name}, Puneet here. The {sku_short_name} should be just about empty. Most family-ritual customers finish a box in 6 weeks of Sunday lunches. Reply YES if you would like the next box on the way. Reply STOP if not.

## CTA
"YES" → one-click reorder link sent in follow-up
"STOP" → do-not-WhatsApp list, founder notified

## When NOT to send
- Customer has already re-ordered in last 28 days
- Customer has an open support ticket
- Customer has opted out of WhatsApp marketing
- The Meetha Paan or Almond Delight is currently out of stock

## Compliance
- WhatsApp Business utility template (post-purchase reminder), service tier
- Opt-in required from order confirmation flow

## Source
my-work/voice-of-customer/2026-05-12-voc-report.md → Theme 5 (subscription friction) + repeat-buyer voice
