# Email Template — First-Time-Buyer to Second-Purchase Nudge
Trigger: 21 days after first order, no second order
Segment: First-time buyers, all SKUs
Tone: Founder voice, no urgency tricks, no fake scarcity
Allowed personalisation tokens: {first_name}, {first_sku_name}, {suggested_next_sku}

## Subject line (3 variants)
1. {first_name}, where are you with the {first_sku_name}?
2. The SKU most parents add next
3. About 3 weeks in. Any feedback?

## Body
Hi {first_name},

Three weeks since your Little Lab order. You probably know by now whether the product worked for you. If it did not, write me back and tell me. Not a marketing question — a real one.

If it did, the SKU most parents in your situation add next is the {suggested_next_sku}. Here is why:

If you bought the Cradle Cap Balm, the Newborn Daily Lotion is the natural next step — same ingredient transparency thesis, fragrance free, the lotion most of our cradle cap parents start using on the rest of the body in the first 30 days.

If you bought the Newborn Daily Lotion, the Cradle Cap Balm is the next thing in the cabinet for the parents who later need it (about 60% of newborns get cradle cap in the first 12 weeks).

If you bought the 2-in-1 Bath and Hair Wash, the Newborn Daily Lotion is what most parents pair with it for the dry-after-bath patches.

Returning customers get a 12% bundle code if you want to pair anything: LL-PAIR-12. One-time use. No expiry. No follow-up email pushing you to use it.

Riya

## CTA
Three CTAs (one per scenario, with the linked PDP for the suggested_next_sku). Hard ask is "shop the {suggested_next_sku}". Soft ask is "reply with what worked / did not work".

## When NOT to send
- Customer already placed a second order
- Customer has an open complaint
- {suggested_next_sku} is currently out of stock — substitute with the third-most-likely next SKU

## Compliance
- Promotional category (discount code included). Footer: unsubscribe link.
- The 12% code must be a real working code in Shopify before send.

## Source
my-work/voice-of-customer/2026-05-12-voc-report.md → first-time-buyer voice + repeat-buyer voice. Cross-sell SKU mapping is from Shopify cohort signal (Cradle Cap Balm → Newborn Daily Lotion at 42% within 30 days). Confirm cohort numbers before publish.
