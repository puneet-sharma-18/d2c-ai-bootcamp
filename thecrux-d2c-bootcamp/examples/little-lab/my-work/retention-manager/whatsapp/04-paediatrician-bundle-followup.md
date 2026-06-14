# WhatsApp Template — Paediatrician-Referred Customer Bundle Follow-up
Trigger: 14 days after first order AND order included Cradle Cap Balm AND CRM tag = "paediatrician-referred"
Segment: Paediatrician-referred persona (high LTV, VoC theme 6)
Tone: Founder voice. This segment buys on trust; do not break it with a discount push.
Allowed personalisation tokens: {first_name}, {paediatrician_name_if_known}

## Body
Hi {first_name}, hope the Cradle Cap Balm has been working. {paediatrician_name_if_known} has been a friend of the brand for a while, so I wanted to personally say thanks for trusting the referral. If your baby is in the newborn-to-3-month window, the Newborn Daily Lotion is what most parents move to next — same ingredient transparency, no fragrance. Want me to send a sample sachet with your next order? No charge, just so you can try.

## CTA
Reply YES → free sample added to next order workflow
Reply NO → log "not interested in cross-sell at this time", no follow-up for 90 days

## When NOT to send
- Customer is not actually paediatrician-referred (CRM tag missing or unconfirmed)
- Paediatrician name placeholder cannot be filled — drop the name entirely rather than write {placeholder}
- Customer's first order was the Newborn Daily Lotion (no cross-sell to itself)

## Compliance
- Service conversation tier (post-purchase follow-up)
- The paediatrician relationship is the founder's; do not use a name without prior consent recorded in the panel

## Source
my-work/voice-of-customer/2026-05-12-voc-report.md → Theme 6 + persona card "Paediatrician-referred parent 32-42". Cross-sell rate for this segment is ~40% higher than D2C-only buyers.
