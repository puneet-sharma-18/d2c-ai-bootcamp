# WhatsApp Template — Pre-Purchase Allergen Clarification (Auto-Suggested Reply)
Trigger: Customer message contains keywords (allergy, nut, sesame, celiac, gluten, dairy) — auto-suggested for founder to confirm
Segment: All pre-purchase WhatsApp inbound
Tone: Honest, direct. No glossing over allergen risks.
Allowed personalisation tokens: {first_name}, {sku_in_question}

## Body
Hi {first_name}, thanks for asking before buying. We list every ingredient by name, not "may contain". Here is what I can tell you about {sku_in_question} allergens:

{sku-specific block to be filled by founder, but template hints below}

If your allergy is severe / anaphylactic, please err on the side of choosing a different SKU. Honest answer is better than a sale.

## SKU allergen blocks (founder picks one)
- **Meetha Paan**: Contains fennel, rose, gulkand. No tree nuts. No dairy. No gluten.
- **Almond Delight**: Contains tree nuts (almond) and saffron. No dairy. No gluten in the paan itself.
- **Masala Cranberry**: Contains tree nuts (almond), sesame seeds. No dairy. No gluten.
- **Dry Fruit Meetha Paan**: Contains tree nuts (almond, cashew), raisins. Trace dairy possible in the gulkand sourcing. No gluten.
- **Granola Goodness**: Contains tree nuts, oats (NOT certified gluten-free), seeds. Dairy in some batches (whey-coated dry fruit), check current batch.
- **Herbal Mukhwas**: Contains sesame, fennel, coriander seed. No tree nuts. No dairy. No gluten.

## CTA
"OKAY" / specific SKU name → send PDP link + payment
"DIFFERENT SKU PLEASE" → recommend safe-for-them SKU
Silence → log inquiry, no follow-up

## When NOT to send
- Inquiry is from a B2B / corporate customer (different intake flow)
- The allergen mentioned is something we cannot confirm honestly (e.g. cross-contamination questions) — escalate to founder, do not auto-respond

## Compliance
- Service tier (pre-purchase product question)
- Allergen claims must reflect the current batch's actual ingredient sourcing; the WhatsApp bot uses the latest ingredient sourcing log

## Source
my-work/voice-of-customer/2026-05-12-voc-report.md → Theme 6 (allergen and ingredient questions, 9%) + WhatsApp Thread 2 (celiac case study)
