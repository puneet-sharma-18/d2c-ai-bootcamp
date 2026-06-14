# SOP — Summer Shipping (May to September)
Owner: founder (Puneet), until delegated to ops freelancer
Trigger: Daily, automatic for any order shipping between May 1 and September 30 to any of the high-temp pin codes (currently: Delhi, Lucknow, Ahmedabad, Hyderabad, Nagpur, Jaipur, Indore).
First time vs steady state: First time needs the courier negotiation and the insulated-box vendor onboarding. Steady state is the per-order checklist.

## When to use this
VoC theme 7 surfaced summer melt at 5-8% complaint rate. SKUs at risk: Almond Delight (saffron + gulkand), Dry Fruit Meetha Paan (any chocolate-coated dry fruit), Granola Goodness (oat + chocolate flecks). Safe summer SKUs: Meetha Paan core, Herbal Mukhwas, Masala Cranberry.

## The 6-step playbook (per order)

1. **Pin-code check at order placement** (auto, 0 sec). Shopify trigger flags any order to a high-temp pin code in May-September. Tag added: "summer-insulated".

2. **SKU compatibility check** (auto, 0 sec). If "summer-insulated" tag AND any SKU in {Almond Delight, Dry Fruit Meetha, Granola} is in cart, fire the customer-side notification: "Your order ships in our insulated summer box. Adds 1 day in transit, ₹0 extra to you."

3. **Packing instruction** (per order, 2 min). Insulated box + gel pack (frozen 4h before pack). Note on the manifest: "Summer pack, Pin {NNNNNN}, dispatch by 11am tomorrow latest."

4. **Courier choice** (per order, 0 sec auto). Switch from {courier-A} default to {courier-B} for summer-insulated lanes — {courier-B} has cold-chain capability at +₹40/box. Cost absorbed by us, not passed to customer.

5. **Customer pre-delivery message** (24h before delivery, auto). WhatsApp: "Your insulated box is out for delivery tomorrow. Please refrigerate within 2 hours of receiving. Eat within 7 days."

6. **Post-delivery check-in** (3 days after delivery, auto). WhatsApp: "Quick check — did your box arrive intact and stay cool? Reply 🟢 if all good. Any concerns and I will personally fix." Surfaces summer-melt complaints at the 5-8% rate documented in VoC theme 7.

## Decision points
- **Step 4**: courier switch is the cost decision. Founder calibrates based on monthly summer order volume vs the ₹40/box delta. At 2026 volume (~120 summer-pin orders/month), the ₹4,800/month cost is justified by the VoC theme retirement.

## Templates referenced
- `vendor-kit/insulated-box-vendor.md` (not in DEFAULT scope; POWER)
- WhatsApp templates: `my-work/retention-manager/whatsapp/02-delivery-checkin.md` (adapted for the summer variant)

## Escalation
- If post-delivery check-in surfaces 2+ melt complaints in any week: trigger SOP variant "summer pause" — temporarily delist Almond Delight, Dry Fruit Meetha, Granola from high-temp pin codes for the rest of the week. Founder decides per cycle.
- If a customer publicly posts a melt complaint (Instagram, Twitter, Google review): pull to top of queue, founder responds within 4 hours with apology + refund + a "we are switching the courier for your lane" message.

## Done definition
- Every summer-insulated order ships with the gel pack and the customer notification
- Post-delivery check-in fires; complaints below 3% on summer lanes
- Monthly review with the 3PL on Tier-2 summer SLA
