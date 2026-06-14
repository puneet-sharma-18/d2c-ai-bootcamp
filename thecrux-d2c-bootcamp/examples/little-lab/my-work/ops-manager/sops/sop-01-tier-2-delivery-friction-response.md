# SOP — Tier-2 Delivery Friction Response
Owner: founder (Riya), until delegated to ops freelancer
Trigger: 3+ support tickets in any 7-day window citing delayed delivery from non-metro pin codes, OR a single ticket comparing our delivery time unfavourably to a named competitor.
First time vs steady state: First time needs the courier review and the rate negotiation. Steady state is just the customer communication.

## When to use this
VoC theme 7 is the recurring pattern: Tier-2 customers see Mamaearth arrive in 3 days while ours takes 7+. The product is fine, the experience is not. This SOP runs when the friction surfaces, applies the playbook, and updates the VoC theme status.

## The 7-step playbook

1. **Triage the ticket(s)**. (5 min) Open the support tickets. Confirm the pattern: same hub, same courier, same pin-code prefix. If only 1 ticket, do not run the SOP yet — log to watchlist.

2. **Pull the route data**. (10 min) Run via Shopify MCP: `mcp__shopify__list_orders` filtered by the affected pin code range, last 30 days. Get the courier name, the average transit time, the SLA in our 3PL contract.

3. **Customer apology + replacement / refund**. (20 min) Send the apology template `templates/courier-delay-apology.md` to each affected customer. Replace, refund, or offer free reshipment per the customer's choice. Do not automate this — the founder personally signs at this volume.

4. **Vendor escalation**. (15 min) Send the courier escalation template `vendor-kit/courier-escalation.md` to the 3PL account manager. Specify: pin-code range, ticket count, comparison to {courier-A vs courier-B}, our SLA expectation, the deadline.

5. **Decision point**. (varies) Founder decides: switch courier back for this lane, accept the slower pace as a known constraint and communicate it on the PDP, OR escalate to a higher-tier 3PL contract. Decision criteria:
   - Switch back if: ticket volume > 5/week AND CSAT impact ≥ 1.0 stars on affected SKUs
   - Communicate constraint if: volume manageable AND alternative courier costs ≥ 30% more
   - Higher tier 3PL if: lane is strategic AND volume justifies (>200 orders/month from the affected region)

6. **Update the PDP / cart messaging**. (10 min) If the decision is "communicate the constraint", the Storefront Specialist updates the cart-page delivery estimate for affected pin codes. See CRO Observation 2 in `my-work/storefront-specialist/2026-05-13-cro-observations.md`.

7. **Update VoC watch**. (5 min) Mark VoC theme 7 status in the next VoC re-run — either "resolved (courier switched)" or "active, communicated". Next VoC run picks up the trend.

## Decision points
- **Step 5** is the only founder-grade decision. The other steps are checklists.

## Templates referenced
- `templates/courier-delay-apology.md` (customer-facing)
- `vendor-kit/courier-escalation.md` (3PL-facing)

## Escalation
- If the 3PL does not respond within 48h to the escalation, founder calls the account manager directly. No SOP for that — the relationship is the founder's.
- If a customer ticket includes a public review threat ("I will leave this on Amazon"), pull that ticket to the top of the queue and respond within 4 hours.

## Done definition
- All affected customers acknowledged within 24h
- 3PL responded with corrective action or refusal
- Founder has made the Step 5 decision
- VoC watch flag updated
- If a public review was already posted: a brand response posted within 48h

## SAFETY FLAGS
- No customer phone number, full name, or order ID saved in this SOP. Templates use {placeholders} that the founder fills at send time.
- The decision criteria in Step 5 are illustrative. Founder calibrates the thresholds to her actual ticket volume and margin tolerance.
