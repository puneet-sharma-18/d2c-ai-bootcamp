# Customer Email — Stockout Apology + Restock ETA (Hero SKU)
Use when: A top-5 SKU is out of stock AND the customer has bought it in the last 90 days AND they are NOT already on the waitlist.
Trigger: Fired from SOP-02 (Stockout Response) Step 5.
Tone: Founder voice, honest, no marketing-speak. The customer is feeling the gap, not the ad copy.

## Subject lines (3 variants)
1. Cradle Cap Balm is out of stock. Restock {date}. Sorry.
2. {first_name}, the SKU you bought is out of stock
3. Quick note about your Cradle Cap Balm

## Body

Hi {first_name},

Wanted to write this myself rather than have it go through an autoresponder.

The Cradle Cap Balm 50ml is out of stock as of {date}. Restock is scheduled for {restock_date}. That is {days_to_restock} days from now. I know that is a longer gap than either of us would want.

Why it happened: demand on this SKU has grown faster than our production cadence over the last 8 weeks. We hand-roast the ingredients in small batches and we deliberately do not over-produce. This time we underestimated by about {N} units. The fix is in the next production run, not in compromising on the small-batch approach.

What I can offer in the meantime:

1. **First dibs when we restock**. I have added you to the priority list. You will get a WhatsApp 24 hours before the public restock email goes out.

2. **Alternative SKU**. If your baby's cradle cap is active right now, the Newborn Daily Lotion sometimes helps as a temporary measure for mild cases (it does not have the named active, so it is not a true substitute, just a gentler holding pattern). If the cradle cap is more advanced, I would honestly recommend calling your paediatrician for a short-term prescription option rather than waiting for our restock.

3. **A discount when we are back**. {discount_code} for 12% off your next Cradle Cap Balm order, valid 30 days from the restock date. One-time use.

If you have questions about what to do for your baby between now and {restock_date}, hit reply on this email and I will personally write back. I read every reply.

Best
Riya
Founder

P.S. If you want to be removed from the priority list (because you found another solution or your baby has aged out of needing it), reply with "REMOVE" and I will take you off.

## CTA
- Reply with a question → founder personal response
- Reply "REMOVE" → drop from priority list
- Click the discount code → cart pre-loaded for the restock notification email later

## When NOT to send
- Customer is already on the active waitlist (different template for them — they get the WhatsApp ping, not this email)
- Customer is the recipient of a gift order, not the buyer (the gift purchaser gets this, not the receiver)
- Customer has an open returns / refund ticket on this SKU
- Customer has explicitly unsubscribed from marketing

## Compliance
- Service category technically (post-purchase relationship maintenance). Unsubscribe link in footer.
- The discount code must be a real working code in Shopify before send. If the code is not yet live, mark as `{discount_code_placeholder}` and the founder fills before send.
- "I read every reply" must remain true. Once founder volume makes this impossible, swap to "Our team reads every reply" — do not break the promise.

## Personalisation depth
- `{first_name}` — required
- `{restock_date}` — required, must be a real committed date from the co-packer
- `{days_to_restock}` — auto-computed from the dates
- `{N}` units underestimated — optional, fill if the actual number is not embarrassing
- `{discount_code}` — required, real working code

## Source
my-work/voice-of-customer/2026-05-12-voc-report.md → repeat-buyer voice (the Cradle Cap Balm buyers are the most loyal segment; a stockout without communication breaks trust faster than the stockout itself)
