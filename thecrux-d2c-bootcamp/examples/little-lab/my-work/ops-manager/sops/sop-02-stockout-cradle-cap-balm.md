# SOP — Stockout Response (Hero Problem-Solver SKU)
Owner: founder, until delegated to ops freelancer
Trigger: Inventory drops below 30 units on Cradle Cap Balm 50ml (LL-CCB-050) AND last 30-day order count > 80 (hero-SKU criterion). Trigger applies for any SKU meeting both conditions.
First time vs steady state: First time defines the comms tree; steady state is the checklist.

## When to use this
Cradle Cap Balm is the trust-entry SKU. A stockout signals "they cannot keep up with demand" to a paediatrician-referred parent, and turns into a brand-trust problem fast. Other top SKUs (Newborn Daily Lotion, 2-in-1 Wash) trigger this SOP too — the cradle cap is the worst case.

## The 8-step playbook

1. **Stock check** (5 min). Run `mcp__shopify__get_inventory_levels`. Confirm current on-hand. Cross-check the WMS / 3PL inventory if separate.

2. **Recent burn rate** (5 min). Pull last 7-day units sold and last 14-day units sold. If 7-day > 1.5x of 14-day average, the burn is accelerating; tighten the response.

3. **Restock ETA** (10 min). Call the vendor / contract manufacturer. Get the date. If date > 14 days, escalate to founder for decision on alternate manufacturing.

4. **Landing page note** (10 min). Update the Cradle Cap Balm PDP top bar with: "Currently out of stock. Restock by {date}. Enter your email for first dibs." Save the form responses to a Drive folder.

5. **Email to recent buyers** (15 min). Send the template `templates/stockout-apology-and-eta.md` to anyone who bought Cradle Cap Balm in the last 90 days but is not on the waitlist. Goal: stay in front of repeat buyers so they do not try a competitor mid-gap.

6. **WhatsApp broadcast** (5 min). Send a 2-sentence WhatsApp to the Cradle Cap Balm tagged segment in the Retention Manager segment list (`my-work/retention-manager/segments/`). "Quick note from Riya. Our Cradle Cap Balm is restocking by {date}. Reply YES to get the first ping."

7. **Performance Marketer pause** (5 min). Pause all Meta and Google ads pointing to the Cradle Cap Balm PDP. They will run out of stock and waste spend. Reuse the budget on Newborn Daily Lotion creative (the next-best SKU that converts the same persona).

8. **Restock comms** (10 min, at restock). When inventory returns: notify the waitlist first, then send an "We are back" email to recent buyers, then restart paid ads. NOT before — the waitlist gets the first 48 hours.

## Decision points
- **Step 3**: if ETA > 14 days, founder decides whether to absorb the gap, escalate to alternate manufacturing, or run a temporary bundle (Newborn Daily Lotion + sample-size Cradle Cap Balm) to keep the trust-entry alive.
- **Step 7**: if the founder has invested ad budget on Cradle Cap Balm-specific creative this week, pause is non-negotiable. Even one day of spend on a stock-out PDP is wasted.

## Templates referenced
- `templates/stockout-apology-and-eta.md`
- WhatsApp broadcast text is in `my-work/retention-manager/whatsapp/replenishment-prompt.md` (variant for stockout context)

## Escalation
- If vendor ETA slips by more than 5 days from the originally communicated date, founder personally calls the vendor and renegotiates timeline.
- If the waitlist exceeds 200 names, that is itself a signal the SKU is underpriced or under-distributed. Founder reviews with Growth Analyst next Monday.

## Done definition
- Inventory restored to safe level (>50 units)
- Waitlist notified
- Recent buyers notified
- Ads restarted
- Next 30-day burn rate forecast updated in `my-work/ops-manager/` for re-order trigger calibration
