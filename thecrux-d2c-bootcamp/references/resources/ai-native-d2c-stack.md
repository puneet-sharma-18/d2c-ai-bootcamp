[← Back to Resources](resources.md)

---

# AI-Native Operating Stack for an Indian D2C Brand

**Verified as of 2026-05-17.** Sources: vendor pages, founder community threads (r/D2C_India, Headway DPDP boards, GrowthSchool community), Shopify and Razorpay official changelogs, plus independent reviews from the four weeks of April 19 to May 17, 2026. Re-verify any price before a procurement decision.

This page is one of three siblings. [`ai-creative-stack.md`](ai-creative-stack.md) is the bench that produces pixels and audio. [`claude-skills-stack.md`](claude-skills-stack.md) is the skills bench you install into the orchestration layer. This page is the operating spine: commerce engine, support inbox, reviews, WhatsApp, lifecycle, attribution, fulfilment, marketplace ops, payments and the orchestration layer that ties them together.

If a founder asks "what stack do I run my brand on", point them here. If they ask "which model produces the Diwali poster", point them at the creative stack.

---

## The thesis

AI-native does not mean "buy SaaS with an AI button". Every dashboard tool has shipped an AI feature by mid-2026. Most of them are wrappers.

AI-native means the **founder's operating layer is an LLM with tools**, and the SaaS underneath becomes a data source. Claude Code (or a similar agent runtime) reads from Shopify, Gorgias, Klaviyo, Razorpay, Shiprocket via MCP. Skills like `voice-of-customer`, `growth-analyst`, `content-lead` and `performance-marketer` run on a schedule. The founder reviews indexes, not dashboards.

What that means when you pick SaaS:

1. **API-first.** If the tool has no public API, do not buy it. You cannot orchestrate what you cannot query.
2. **MCP support is a multiplier.** Shopify, Razorpay and Slack ship official MCP servers. Gorgias, Klaviyo and Triple Whale have community or partner MCPs. Tools with no MCP (and no plan to ship one) become friction.
3. **INR billing matters.** Anything you pay for monthly should ideally bill in INR. The FX, TCS and bank markup on USD subs adds up to ~6 to 8% over a year on a ₹2L/mo stack.
4. **One vendor per layer.** Two CRMs is a data-sync problem. Two attribution tools is a finger-pointing problem. Pick one per layer and commit.

Three tiers per category, same shape as the creative stack:

1. **Best:** top fit for an AI-orchestrated Indian D2C brand at ₹50L to ₹5Cr ARR.
2. **Efficient:** close enough on outcomes, half the price or simpler ops.
3. **Third:** picked for a specific niche the first two miss (enterprise scale, open-source, deep AI-native).

---

## 1. Commerce engine

Where the catalogue, checkout and order data lives. Everything else hangs off this.

| Tier | Tool | Why it wins now | India access | Cost |
|---|---|---|---|---|
| **Best** | **Shopify** | Deepest app ecosystem in India D2C, native Shopify MCP shipping in 2026 covers products, orders, customers, inventory, analytics. Sidekick handles SKU-level questions. Razorpay, Shiprocket, Judge.me, Klaviyo, WATI all have first-class integrations. | Yes. INR billing via Shopify India. UPI checkout standard. | Basic $25 ($29 with India ramp), Shopify $69, Advanced $299/mo. POS Pro add-on $89. |
| **Efficient** | **WooCommerce + WordPress** | Self-hosted, no per-transaction fee, full control over data residency (matters for DPDP). API is REST + ACF; MCP wrappers exist on GitHub. Trade-off: you own hosting, security, plugin compatibility. | Yes. Host on Hostinger, BlueHost India or AWS Mumbai. | Hosting ₹400 to ₹2000/mo. Plugins ₹0 to ₹3000/mo. |
| **Third** | **Saleor** (open-source headless) or **Medusa.js** | API-first by design, GraphQL native, made for teams that want to compose their own front-end (Next.js, Astro) and own the agent layer. Right pick when you have an engineer and want Claude Code to drive the storefront directly. | Self-host on AWS Mumbai, GCP Mumbai. | Infra $50 to $300/mo. |

**Sources:**
- Shopify MCP: https://shopify.dev/docs/api/mcp
- Shopify India pricing: https://www.shopify.com/in/pricing
- Saleor: https://saleor.io/
- Medusa: https://medusajs.com/

**Recent shake-ups:**
- **Shopify Sidekick** out of beta March 2026. Native to admin, answers ops questions ("which SKUs sold under 5 units last week and have over 50 units in stock").
- **Shopify Magic Studio** consolidated under Sidekick. Stop using "Magic" as a search term in docs; it points at deprecated tooling.
- **Shoptype** (Bengaluru-based, agentic commerce) raised Series A in April 2026, still pre-mature for a ₹30L/mo brand. Watch list, not buy list.

**Rule of thumb:** Shopify until you cross ₹5Cr ARR and you have an engineer who can own a headless rebuild. Switching cost dominates every other consideration before that.

---

## 2. Customer support inbox

Where tickets land. Quality of this layer decides repeat rate and review sentiment.

| Tier | Tool | Why it wins now | India access | Cost |
|---|---|---|---|---|
| **Best** | **Gorgias** | D2C-tuned, Shopify deeper than any other helpdesk, Auto-Respond AI clears 30 to 60% of tickets per public case studies (2026). Native Shopify order context in every ticket. MCP via partner integrations. | Yes. USD. | Starter $10/mo (50 tickets), Basic $60 (300), Pro $360, Advanced $900. |
| **Efficient** | **Chatwoot** (open-source) | Self-host or cloud, full API access, channels for email + WhatsApp + Instagram + web chat. Pair with an MCP wrapper and Claude Code drafts replies, you ship. Lower polish than Gorgias, half the cost or less. | Yes. Self-host on AWS Mumbai or use Chatwoot Cloud (USD). | Self-host: infra only. Cloud: $19/mo Hacker, $39 Startup, $99 Business. |
| **Third** | **Decagon** or **Lorikeet** (AI-native agents) | Autonomous resolution at 60 to 80% of tickets unattended, premium positioning. Decagon writes its own runbooks from your KB. Useful when ticket volume exceeds what a 2-person support team can review. | Yes. USD, enterprise contracts. | $2K to $15K/mo, custom. |

**Sources:**
- Gorgias India case studies: https://www.gorgias.com/blog/category/customer-stories
- Chatwoot: https://www.chatwoot.com/pricing
- Decagon: https://www.decagon.ai/
- Lorikeet: https://www.lorikeetcx.ai/

**Recent shake-ups:**
- **FreshDesk Freddy** AI add-on now bundled in Pro plan from Feb 2026. If you already pay for FreshDesk, the AI is free; quality lags Gorgias Auto-Respond.
- **Klart.ai** (Indian, AI-native) launched a D2C-focused agent in March 2026. Pre-revenue; useful to follow.
- **Zendesk Suite** raised entry pricing to $115/agent/mo in Feb 2026. Confirmed unfit for D2C velocity at that price.

**What to skip:**
- **HubSpot Service Hub** for D2C inbox. Built for B2B SaaS sales, wrong shape for 200-ticket-a-day food brand.
- **Generic shared inboxes** (Front, Help Scout) without Shopify-native order context. You will rewrite the same five reply templates every week.

**Rule of thumb:** Start with Chatwoot self-hosted if you have an engineer, Gorgias Basic if you do not. Move to Decagon-tier autonomous AI only when your ticket count crosses 500/week and your founder voice rules are written down clearly enough that an AI can hold them.

---

## 3. Reviews and UGC

Where social proof lives. Drives PDP conversion and feeds the Voice of Customer skill.

| Tier | Tool | Why it wins now | India access | Cost |
|---|---|---|---|---|
| **Best** | **Judge.me** | Indian-founded (acquired by Zapiet 2024), deepest Shopify integration, native review aggregation rich snippets, photo + video review prompts in WhatsApp and email. API and webhook coverage is complete. | Yes. USD billing, Indian cards work. | Free forever (basic), Awesome $15/mo (most needed features). |
| **Efficient** | **Loox** | Photo and video review specialist, on-site widget converts better than text-only walls. Less API depth than Judge.me, more visual polish out of the box. | Yes. USD. | Beginner $9.99, Studio $34.99, Growth $79.99/mo. |
| **Third** | **Okendo** or **Junip** | Deep segmentation, attribute filters (skin type, hair type, age), survey-driven UGC. Premium positioning, used by larger D2C brands once review volume crosses ~500/month. | Yes. USD. | Okendo $19 to $499/mo. |

**Sources:**
- Judge.me: https://judge.me/pricing
- Loox: https://loox.app/pricing
- Okendo: https://www.okendo.io/pricing

**Recent shake-ups:**
- **Judge.me + WhatsApp review request flow** launched native integration with WATI in March 2026. Indian D2C brands seeing 18 to 25% review-collection rate, vs 4 to 6% via email alone.
- **Loox AI Summary** auto-generates a one-line summary from photo reviews. Useful for PDP above-the-fold.

**Rule of thumb:** Judge.me on every Shopify store under ₹5Cr ARR. The cost gap to Loox or Okendo only justifies itself when you have explicit segmentation needs your VoC skill cannot already extract from raw review text.

---

## 4. WhatsApp Business (broadcasts + conversational commerce)

The single biggest retention channel in India D2C. If you ship to Tier-1 and Tier-2 cities, 30 to 50% of repeat orders flow through WhatsApp.

| Tier | Tool | Why it wins now | India access | Cost |
|---|---|---|---|---|
| **Best** | **WATI** | Largest Indian-founded WABA partner (~10,000 brands), Shopify and Razorpay native, drag-drop flow builder, broadcast at scale, native MCP shipping in Q3 2026. Standard for ₹1Cr to ₹20Cr ARR D2C. | Yes. Native INR. | Growth ₹2,499/mo, Pro ₹4,999, Business ₹9,999. Plus Meta conversation charges. |
| **Efficient** | **Interakt** | Indian, Shopify-deep, slightly cheaper than WATI, popular with newer brands. Flow builder is less mature. | Yes. INR. | Starter ₹999/mo, Growth ₹2,499, Advanced ₹3,499. Plus Meta conversation charges. |
| **Third** | **AiSensy** or **Gallabox** (Indian) **or Twilio** (custom build) | AiSensy and Gallabox priced lower than WATI for similar features. Twilio if you have an engineer and want to build a custom agent on top of WhatsApp Cloud API. | Yes. INR for AiSensy and Gallabox; USD for Twilio. | AiSensy ₹999 to ₹3,499/mo. Gallabox ₹1,500 to ₹5,000. Twilio pay-per-message. |

**Sources:**
- WATI: https://www.wati.io/pricing/
- Interakt: https://www.interakt.shop/pricing/
- AiSensy: https://www.aisensy.com/pricing
- Meta Business conversation pricing India: https://developers.facebook.com/docs/whatsapp/pricing

**Recent shake-ups:**
- **Meta Business pricing model changed Nov 2024**, now per-message in some categories. Re-check unit economics: marketing messages cost ₹0.70 to ₹0.95 each in India, utility messages ₹0.13 to ₹0.20.
- **WATI Auto-AI Replies** (Mar 2026) routes inbound messages to a GPT-4o-mini agent for L1 questions. Quality is decent; founder voice tuning is shallow.
- **WhatsApp Flows** (Meta native, no third party) gaining adoption for native in-WhatsApp checkout. Watch this, it may collapse the WABA-partner layer eventually.

**Rule of thumb:** WATI if you can afford it, Interakt or AiSensy if you cannot. Twilio only when an engineer is going to own a custom agent that does more than templates and broadcasts.

---

## 5. Lifecycle marketing (email + SMS + WhatsApp from one brain)

Where the win-back, replenishment and welcome flows run. The Retention Manager skill writes the templates, this layer ships them.

| Tier | Tool | Why it wins now | India access | Cost |
|---|---|---|---|---|
| **Best** | **Klaviyo** | D2C default, deepest Shopify integration, segmentation that actually works, predictive AI for churn risk and next-likely purchase. SMS bundled in the US, email-only in India. | Yes. USD. | Free up to 250 contacts, $20/mo at 500, $45 at 1500, $150 at 10K. Pricing scales by contact + send volume. |
| **Efficient** | **Mailmodo** (Indian-founded) | AMP emails (forms, carousels, polls inside the email), 2 to 4x click rates vs static HTML on right use cases. Cheaper than Klaviyo at every tier. AI workflow builder. | Yes. INR. | Lite ₹2,499/mo (10K contacts), Pro ₹4,999, Premium ₹9,999. |
| **Third** | **CleverTap** or **Customer.io** | CleverTap for brands with a mobile app (push notifications, in-app messaging are first-class). Customer.io for code-first teams that want event-based workflows. | Yes. CleverTap INR, Customer.io USD. | CleverTap from ₹14K/mo. Customer.io $100 entry. |

**Sources:**
- Klaviyo: https://www.klaviyo.com/pricing
- Mailmodo: https://www.mailmodo.com/pricing/
- CleverTap: https://clevertap.com/pricing/

**Recent shake-ups:**
- **Klaviyo AI Subject Lines + Send Time Optimization** rolled out to all paid tiers Feb 2026. Default-on. Measurable lift on open rates.
- **Mailmodo + WATI co-marketing** package launched April 2026. ₹6,500/mo bundle covers email + WhatsApp under one roof for sub-₹3Cr brands.
- **Wigzo** (Indian) was strong 2022 to 2024, lost share to Mailmodo through 2025. Verify roadmap before signing.

**What to skip:**
- **Mailchimp** for D2C. Built for newsletters, not flows. Segmentation is shallow, Shopify integration thin.
- **Generic ESPs** (SendGrid, Postmark) as a customer-facing marketing tool. They are transactional infrastructure, not lifecycle platforms.

**Rule of thumb:** Klaviyo if your founder voice and segmentation rules are mature and you want one tool to grow into. Mailmodo if INR billing matters and AMP emails fit your category (works well for food, fashion, beauty; less for B2B).

---

## 6. Attribution and analytics (the Growth Analyst's data layer)

Where the question "where did this revenue come from" gets answered. Feeds the Monday weekly brief.

| Tier | Tool | Why it wins now | India access | Cost |
|---|---|---|---|---|
| **Best** | **Lifesight** | Indian-founded, INR billing, MMM + multi-touch + incrementality testing in one. Native Shopify + Meta + Google + Razorpay connectors. Default for Indian D2C from ₹2Cr ARR upward. | Yes. INR. | Plans start ₹15K/mo, scale by ad spend. |
| **Efficient** | **Triple Whale** | US D2C consensus, Shopify-deep, real-time dashboards, AI insights via Moby agent. India founders use it widely despite USD billing. | Yes. USD. | Pro $129/mo entry, scales by Shopify GMV. |
| **Third** | **Polar Analytics** or **Northbeam** | Polar is the cheap Triple Whale alternative, Northbeam is the heavyweight attribution tool used by US 8-figure brands. Both useful at scale; overkill below ₹3Cr ARR. | Yes. USD. | Polar from $300/mo, Northbeam $1K+/mo. |

**Sources:**
- Lifesight: https://www.lifesight.io/pricing
- Triple Whale: https://www.triplewhale.com/pricing/
- Polar Analytics: https://www.polaranalytics.com/pricing
- Northbeam: https://www.northbeam.io/

**Recent shake-ups:**
- **Triple Whale Moby Agent** (Jan 2026) became a real conversational layer over your dashboards. "Which campaign drove the most new customers in Mumbai last week" works.
- **Lifesight MMM-Lite** for sub-₹2Cr brands launched Mar 2026 at ₹8K/mo entry. Lowers the floor on serious attribution by a lot.
- **iOS 17.4 + Android 14 privacy changes** continue to degrade pixel-only attribution. MMM and incrementality testing are the only durable answers.

**What to skip:**
- **GA4 alone.** Sampling and cross-device gaps make it untrustworthy for revenue decisions at D2C scale. Use GA4 as one input, never as the source of truth.
- **Hyros** for India. Strong tool, but India support and integrations lag US.

**Rule of thumb:** Triple Whale until ₹3Cr ARR, Lifesight from ₹3Cr upward. Below ₹50L/mo, your Shopify analytics + Meta Ads Manager + a clean spreadsheet is enough. Do not buy attribution before you have a problem to solve with it.

---

## 7. Fulfilment, warehousing and last mile

Where the box gets shipped. Affects gross margin and the support ticket volume.

| Tier | Tool | Why it wins now | India access | Cost |
|---|---|---|---|---|
| **Best** | **Shiprocket** | Largest courier aggregator in India, ~17 partners (Delhivery, Bluedart, DTDC, Ecom Express, India Post), Shopify-native, single integration covers prepaid + COD + reverse logistics. API and webhook coverage is complete. | Yes. INR. | Free plan (pay per shipment), Lite ₹999/mo, Pro ₹3,999. Plus per-shipment rates. |
| **Efficient** | **EasyEcom** or **Unicommerce** (multi-channel OMS + WMS) | If you sell on Shopify + Amazon + Flipkart + Zomato, you need a unified inventory and order layer above all of them. EasyEcom newer and INR-friendly, Unicommerce older and more enterprise. | Yes. INR. | EasyEcom from ₹3K/mo, Unicommerce custom (₹8K+/mo typical). |
| **Third** | **WareIQ** or **Pickrr** (full-stack fulfilment) | When you cross 200 orders/day and your founder is touching warehouse ops, move to dedicated warehouse + same-day fulfilment partner. WareIQ runs micro-warehouses near demand clusters. | Yes. INR. | Custom, ~₹40 to ₹70 per shipment depending on warehouse zone. |

**Sources:**
- Shiprocket: https://www.shiprocket.in/pricing/
- EasyEcom: https://www.easyecom.io/pricing
- Unicommerce: https://unicommerce.com/
- WareIQ: https://wareiq.com/

**Recent shake-ups:**
- **Shiprocket Quick** for hyperlocal same-day in 12 cities (Mar 2026). Useful for D2C brands testing quick commerce parallel to Zomato/Swiggy.
- **Delhivery + Shopify direct integration** (without aggregator) launched Q1 2026. Marginally better rates, worse multi-courier resilience. Use only if Delhivery is 90%+ of your shipments.

**Rule of thumb:** Shiprocket from day 1. Move to a dedicated OMS like EasyEcom only when you sell on 3+ channels and inventory desync becomes a real problem. Dedicated warehousing only past 200 orders/day.

---

## 8. Marketplace ops (Amazon, Flipkart, quick commerce)

The honest reality, per Bernie at yesterday's session: Amazon and Flipkart gatekeep their API/MCP access aggressively. The "founder is the bridge" pattern is the durable answer in 2026.

| Tier | Tool | Why it wins now | India access | Cost |
|---|---|---|---|---|
| **Best** | **Manual bridge** (founder + Claude Code + Google Drive folder) | Download Seller Central reports weekly, drop into a shared folder, Claude Code reads via filesystem and runs the Marketplace Editor skill. Lower friction than building against gatekept APIs. The output (revised listing copy, ads recommendations) gets pasted back manually. | Yes. Free. | ₹0. Founder's time. |
| **Efficient** | **SellerApp** (Indian) | Listing optimization, PPC management, keyword research for Amazon India. Pricing tuned for Indian sellers. Use when Amazon is 20%+ of your revenue. | Yes. INR. | Pro ₹4,000/mo, Professional ₹8,000, Enterprise custom. |
| **Third** | **Helium 10** or **Junglescout** | US-built, deeper Amazon-specific tooling (Black Box, Cerebro keyword research). Useful when Amazon US is also a market. Overkill if Amazon India is your only marketplace. | Yes. USD. | Helium 10 Starter $39/mo, Platinum $99, Diamond $279. |

**Sources:**
- SellerApp: https://www.sellerapp.com/pricing.html
- Helium 10: https://www.helium10.com/pricing/
- Amazon Selling Partner API (gated): https://developer-docs.amazon.com/sp-api/

**Recent shake-ups:**
- **Amazon SP-API access** continued tightening in 2025-26. New seller approval rejections are common; existing approvals get rate-limited without notice.
- **Flipkart Seller Hub API** still on closed beta as of May 2026. No MCP. Plan for manual downloads through at least 2027.
- **Zepto, Blinkit, Instamart Seller Centres** have spreadsheet-export UIs only. Same manual-bridge pattern applies.

**What to skip:**
- **Aggregator dashboards** (Browntape, GoFynd marketplace modules) that promise "single pane of glass for Amazon + Flipkart". They scrape rather than integrate; uptime is poor, reconciliation breaks at month-end.

**Rule of thumb:** Build the manual bridge first. Pay for SellerApp only when Amazon is 20%+ of revenue and you have a dedicated team member running the marketplace.

---

## 9. Payments and reconciliation

Where the cash actually moves. Affects reconciliation, refund speed and audit trail.

| Tier | Tool | Why it wins now | India access | Cost |
|---|---|---|---|---|
| **Best** | **Razorpay** | Indian, native UPI + cards + netbanking + EMI + international, deepest Shopify integration, MCP available since Q4 2025 covers payments, refunds, orders, settlements. Best-in-class checkout speed. | Yes. Native INR. | 2% per transaction (UPI 0.4 to 0.9% on most plans), no setup fee. |
| **Efficient** | **Cashfree** | Indian, similar feature set, slightly cheaper on Indian cards, weaker international. | Yes. INR. | 1.75% per transaction baseline. |
| **Third** | **Stripe** | Only when international revenue exceeds 30%. Strong dashboard, deep ecosystem, weak UPI. | Yes (Stripe India launched 2024). USD. | 2.9% + 30c international, 2% + ₹3 domestic India. |

**Sources:**
- Razorpay: https://razorpay.com/pricing/
- Razorpay MCP: https://razorpay.com/docs/api/mcp/
- Cashfree: https://www.cashfree.com/pricing/
- Stripe India: https://stripe.com/in/pricing

**Reconciliation:**
- **Zoho Books** for accounting + GST filing. INR billing, native Razorpay sync, MCP available for reading invoices and bank transactions. Default for sub-₹50Cr ARR Indian D2C.
- **Tally Prime** still standard for the CA layer; integrate via Tally Connector if your accountant insists.
- **Skip:** QuickBooks India (discontinued domestic plans Jan 2023), FreshBooks (no GST native).

**Recent shake-ups:**
- **Razorpay MCP** covers payments, settlements, refunds, customer data. This is the most important API in your stack to wire to Claude Code first.
- **UPI AutoPay** for subscriptions matured through 2025. If you sell consumables (paan, mukhwas, coffee), subscription is now operationally real, not theoretical.

**Rule of thumb:** Razorpay + Zoho Books is the default. Cashfree only if you can show 0.25%+ fee savings at your transaction profile. Stripe only when international is meaningful.

---

## 10. The orchestration layer (the spine itself)

This is the layer the bootcamp builds. Everything above is data sources; this is what reads them, decides what to do and produces founder-grade outputs.

| Tier | Tool | Why it wins now | India access | Cost |
|---|---|---|---|---|
| **Best** | **Claude Code + skills + agents + MCP** | Per-skill cost is low, sub-agent isolation prevents context bloat, file-based memory survives sessions, MCP standardises how SaaS plugs in. The bootcamp's full thesis. | Yes. USD. | Pro $20/mo, Max $100 to $200/mo at heavy usage. Anthropic API for headless on top. |
| **Efficient** | **ChatGPT Plus + Custom GPTs + Zapier MCPs** | Lower learning curve, weaker agent + tool composition, no native file-based memory equivalent. Better for solo founders who do not write any code. | Yes. USD. | Plus $20/mo, Team $30/seat. Zapier $20 to $99/mo for MCP server. |
| **Third** | **n8n** (visual workflow) or **LangGraph** (code-first agents) | When the workflow is fully deterministic and you want a visual DAG (n8n), or when you want production-grade agent code outside an IDE (LangGraph). Both are heavier lift than Claude Code; pick only if the use case demands it. | Yes. Self-host or cloud. | n8n self-host free; cloud ~$20/mo. LangGraph open-source. |

**Sources:**
- Claude Code: https://docs.claude.com/claude-code
- MCP spec: https://modelcontextprotocol.io/
- n8n: https://n8n.io/
- LangGraph: https://langchain-ai.github.io/langgraph/

**What makes this the AI-native layer (and not just "another SaaS"):**
- The agent reads from every other tool above, in their native API. It does not duplicate their data.
- Founder voice rules live in CLAUDE.md and brand-brain/voice-dna/, not inside any SaaS. They cannot be lost when you switch tools.
- Skills compose. The Voice of Customer skill reads from Gorgias (MCP), Judge.me (API), Google Business Profile (MCP). The Content Lead skill reads VoC's output. None of those tools talk to each other directly; the agent layer is the connective tissue.

**Rule of thumb:** Claude Code is the spine. Everything in sections 1 to 9 is a data source the spine reaches through MCP or API. Spend more time on this layer than on any individual SaaS pick below it.

---

## 11. End-to-end workflows (combine the layers)

Three pipelines a brand will run weekly once the stack is wired.

### Monday morning weekly brief

1. **Growth Analyst** (skill) wakes up at 0900 IST via scheduled hook.
2. Pulls revenue from **Shopify MCP**, settlements from **Razorpay MCP**, ad spend from **Meta + Google Ads** (via Lifesight or direct connectors), ticket volume from **Gorgias MCP**, review sentiment from **Judge.me API**, WhatsApp deliverability from **WATI** export.
3. Cross-checks against last week, last month and last quarter.
4. Writes an index file at `my-work/growth-analyst/<date>-monday-brief.md` with: top 3 wins, top 3 problems, the one decision the founder must make today.
5. Sends a Telegram message ("Monday brief is ready") and an email summary.
6. Founder reads the index, makes the call, replies to Telegram with the decision.

### Support to product loop (closing the VoC gap)

1. **Voice of Customer** (skill) runs every Wednesday.
2. Pulls last 7 days of **Gorgias tickets**, **Judge.me reviews**, **Instagram DMs** (via Meta MCP).
3. Clusters by theme (delivery, quality, pricing, packaging, taste), surfaces the top 5.
4. **Content Lead** (skill) reads VoC index, writes 3 to 5 social posts addressing the top 2 themes within 7 days.
5. **Performance Marketer** (skill) reads VoC index, drafts ad copy that answers the top objection.
6. Output lands in `my-work/content-lead/` and `my-work/performance-marketer/`. Founder reviews indexes only.

### Festival pre-launch (Diwali, Rakhi, wedding season)

1. 30 days out: **Captain** (skill) reads competitor pricing (Market Analyst), last festival's recon (Growth Analyst archive), customer pulse (VoC).
2. Outputs a festival plan: SKU rotation, projected demand, ad budget split.
3. **Content Lead** triggers the creative stack (see [`ai-creative-stack.md`](ai-creative-stack.md)) for 30 days of festive assets: Nano Banana Pro Devanagari posters, Flux 2 lifestyle, Kling 3.0 reels, Sarvam Bulbul V3 Hindi VO.
4. **Retention Manager** arms **WATI** broadcast flows for the campaign window.
5. **Ops Manager** confirms **Shiprocket** capacity, **EasyEcom** inventory levels, vendor stock buffers.
6. Festival launches. Captain runs daily during the campaign window, escalates only when something breaks pattern.

---

## 12. Access pattern (one account per layer, not ten)

| Account | Why one | India billing |
|---|---|---|
| **Shopify** | Commerce engine | INR |
| **Razorpay + Zoho Books** | Payments + reconciliation | INR |
| **Shiprocket** | Fulfilment | INR |
| **Gorgias or Chatwoot** | Support inbox | USD |
| **Judge.me** | Reviews | USD |
| **WATI** | WhatsApp | INR |
| **Klaviyo or Mailmodo** | Lifecycle marketing | USD (Klaviyo) or INR (Mailmodo) |
| **Lifesight or Triple Whale** | Attribution | INR (Lifesight) or USD (Triple Whale) |
| **Claude Code (Anthropic) + Claude Pro/Max** | Orchestration | USD |
| **Anthropic API** | Headless agent calls beyond Claude Code | USD |
| **Meta Business + Google Ads** | Paid channels | USD/INR |

For everything in the [creative stack](ai-creative-stack.md), default to **fal.ai** as the single creative-model account.

The right shape: one account per row above, no duplicates. Two of any of these (two CRMs, two analytics tools, two payment gateways) is a data-sync problem that compounds.

---

## 13. India-specific calls

- **DPDP Act** (Digital Personal Data Protection, enforcement window 2025-26): customer data should reside in India, vendors should sign DPAs. Shopify, Razorpay, Shiprocket, WATI, Judge.me, Lifesight all DPDP-aligned. Klaviyo, Gorgias, Triple Whale are US-hosted; document the transfer basis.
- **GST + e-invoicing:** Zoho Books and Tally remain the only practical choice for compliant GST filing. Razorpay generates GST-compliant invoices natively.
- **FSSAI for food brands, CDSCO for cosmetics + health, BIS for electronics:** these affect packaging and ad claims, not stack choice. The relevant rule lives in the brand-brain CLAUDE.md, not in any SaaS.
- **UPI is default:** any payment provider that does not have first-class UPI is unfit for Indian D2C in 2026. Stripe domestic India still trails Razorpay and Cashfree on UPI conversion.
- **Hindi-first customer support:** Gorgias and Chatwoot both work in multi-language; the agent layer (Claude Code) handles Hindi and Hinglish replies if your CLAUDE.md voice rules include Hindi samples. Sarvam Bulbul V3 is the right voice model when the reply goes audio (see creative stack section 4).
- **Quick commerce (Zomato, Swiggy, Zepto, Blinkit, Instamart) data:** all manual-export today. Plan the workflow around a Google Drive folder that Claude Code reads.
- **Founder bank account opening + GST + FSSAI + Trademark** all sit outside the stack. Use a service like Vakilsearch or Razorpay Rize for the legal layer; it is one-time, not recurring.

---

## 14. What to skip

| Tool / Category | Why skip (May 2026) |
|---|---|
| **All-in-one ecom builders** (Wix Stores, BigCommerce for India D2C) | Smaller app ecosystem than Shopify, weaker Indian payments and shipping integrations. Use Shopify or self-host. |
| **Salesforce + HubSpot** for D2C CRM | Built for B2B sales, wrong model for direct consumer. Use Klaviyo or Mailmodo. |
| **Mailchimp** as the lifecycle platform | Newsletter tool, not flow tool. Segmentation and Shopify integration too shallow. |
| **Zendesk Suite** | Enterprise pricing kills D2C velocity. Use Gorgias or Chatwoot. |
| **GA4 as the source of truth for revenue** | Sampling and cross-device gaps. Useful as one input, never the answer. |
| **Aggregator marketplace dashboards** (Browntape, GoFynd marketplace modules) | Scrape rather than integrate, brittle at scale. |
| **"AI-powered" SaaS bundles that wrap GPT-4o-mini and resell at 5x markup** | Cut the middleman; your Claude Code agent calls the model directly. |
| **Discord + Notion + Linear as the operating layer** | Useful for team coordination, not for running a brand. Founder voice + brand decisions belong in CLAUDE.md, not in a Notion workspace nobody reads. |
| **Custom CRM builds** before ₹10Cr ARR | The right CRM exists; the discipline to use it is what is missing. Build only when an off-the-shelf tool genuinely cannot handle your shape. |
| **Hyros for India attribution** | Strong tool, weak India support and integrations. Use Lifesight. |

---

## 15. The next twelve months (watch list)

- **Native Shopify agentic checkout** (Sidekick + Shop Pay agent flows): if it ships, the "ad to checkout" friction collapses. Watch Q3 2026.
- **Meta WhatsApp Flows + native commerce:** the WABA-partner layer (WATI, Interakt) may compress as Meta ships more native features.
- **Amazon SP-API access reform:** rumoured easing in Q3 2026 after seller pressure. Re-verify before assuming the manual bridge is permanent.
- **DPDP Act rules enforcement:** the operational rules under the Act are still landing as of May 2026. Expect tighter data-residency requirements for customer-facing tools.
- **MCP coverage:** Gorgias, Klaviyo, Triple Whale all on roadmap for official MCP servers in 2026. Will reduce the integration plumbing further.
- **Lifesight MMM-Lite + Mailmodo + WATI bundles:** Indian D2C is consolidating; expect more cross-vendor "starter bundles" priced under ₹15K/mo for sub-₹2Cr brands.
- **Claude Code itself:** the bootcamp framework. Watch for native scheduling, native team-mate spawning at the harness layer, broader MCP catalogue.

Track these. Do not switch your weekly pipeline to a tool in beta. Switch the month it is stable and 30% better than what you have.

---

## How this resource gets used in the workshop

- **Session 1 (Brand Brain):** the founder voice rules and category constraints in CLAUDE.md are what every layer above hangs off.
- **Session 3 (MCPs):** the specific MCP connections you wire are: Shopify, Razorpay, Gorgias, WATI, Judge.me. This page tells you which to prioritise.
- **Session 4 (Content Lead):** reads VoC output (from layer 2 + 3) and Market Analyst output, writes the calendar.
- **Session 6 (Performance Marketer):** reads attribution data (layer 6) and ads platforms, drafts creative briefs that flow into the [creative stack](ai-creative-stack.md).
- **Session 7 (Storefront + Marketplace):** writes the Shopify PDP and the manual-bridge workflow for Amazon/Flipkart.
- **Session 8 (Ops + Retention):** writes SOPs and WhatsApp templates that ship through WATI/Interakt and Klaviyo/Mailmodo.
- **Session 9 (Growth Analyst):** the Monday brief that pulls from every layer above.
- **Session 10 (Capstone):** wires the scheduled hooks so all of this runs on its own.

The bootcamp does not buy the SaaS for you. It teaches the agent layer that sits on top of whatever you have.

---

## Re-verification cadence

SaaS pricing and feature sets in the operational layer move on a 3 to 6 month cadence (vs 4 to 6 weeks for the creative models). This page is stamped **2026-05-17**. Re-verify before any contract or stack overhaul that touches more than one layer. The five pages to check first:

1. https://www.shopify.com/in/pricing (commerce baseline)
2. https://razorpay.com/pricing/ (payments)
3. https://www.wati.io/pricing/ (WhatsApp)
4. https://www.klaviyo.com/pricing (lifecycle benchmark)
5. r/D2C_India top-of-month threads (community sentiment, real-world breakage)

For creative model coverage, go to [`ai-creative-stack.md`](ai-creative-stack.md).
