[← Back to Student Handbook](student-handbook.md)

---

# Resources for the D2C Founder Cohort

The workshop installs only what each session needs. Once you walk out, you will add more. This page is the short list focused on the operating stack of an Indian D2C brand: WhatsApp commerce, marketplaces, shipping, payments, accounting, compliance.

The rule: every resource on this page maps to a real operating surface of your brand. If a tool does not feed a teammate or a Monday decision, it does not belong in your stack yet. Productivity tools (docs, slides, calendars) are not on this list. You already have those.

---

## MCPs

MCPs are the plug that lets a teammate read live data. The workshop wires three in Session 3. The list below is the India D2C operating stack, in install order.

### Tier 1: wired during the workshop (Session 3)

| MCP | Feeds | Why |
|---|---|---|
| **Shopify** | Growth Analyst, Storefront Specialist, Retention Manager, Voice of Customer | Orders, products, customers, inventory, reviews if Judge.me or Loox is installed. The data spine of your D2C side. |
| **Google Drive** | Brand Brain, Content Lead, Performance Marketer | Shared brand assets, generated content, the brand-brain folder, creative drop folders for design agencies. |
| **Gmail** | Ops Manager, Voice of Customer | Vendor threads, customer support escalations, 3PL communication. Pull tickets into VoC, draft replies in Ops. |

### Tier 2: India D2C operating stack

These are the surfaces every Indian D2C brand actually operates on. None of them ship with the workshop. Add as your category demands.

| MCP / integration | Feeds | What it covers | Status (May 2026) |
|---|---|---|---|
| **Zoho Books** | Growth Analyst, Ops Manager | Indian accounting default. COGS, channel revenue, returns, GST. Your unit economics stop being a hand-maintained file once this is wired. | Official MCP, OAuth, connects in 2 min |
| **WATI / AiSensy / Interakt** | Retention Manager, Voice of Customer, Ops Manager | WhatsApp Business API gateway. The #1 retention and support channel for India D2C. Templates, broadcasts, conversation threads, COD confirmation flows. | Vendor-specific REST APIs. No official MCP yet. Use webhook-to-file pattern (see "When no MCP exists" below). |
| **Razorpay** | Growth Analyst, Ops Manager | Payment data, settlements, refunds, disputes, COD remittance. Shopify shows orders; Razorpay shows what actually settled. | Razorpay has a public API. Community MCP available; verify before installing. |
| **Shiprocket** | Ops Manager, Growth Analyst | Multi-3PL shipping aggregator most Indian D2C runs on. RTO rates, NDR (non-delivery report), zone-wise shipping cost. Critical for the brands losing 25 to 35% to RTO. | Public API, no official MCP. Webhook-to-file. |
| **Klaviyo** | Retention Manager, Performance Marketer | Email + SMS retention if you have moved past Shopify Email. Flow performance, segment counts, predictive LTV. | Community MCP. Verify before installing. |
| **Judge.me / Loox / Stamped** | Voice of Customer, Storefront Specialist | Product reviews and UGC, the raw material for VoC themes and PDP social proof. | Most expose data through Shopify, so the Shopify MCP often suffices. Direct MCPs are early. |

### Tier 3: marketplaces (CSV is the path for now)

The Indian marketplace operating surface is large and the MCP story is thin. The workshop covers this in `session-9-growth-analyst.md` under "Marketplace CSV ingestion (post-workshop add-on)".

| Marketplace | Feeds | Pattern |
|---|---|---|
| **Amazon Seller Central (India)** | Marketplace Editor, Growth Analyst | SP-API exists. No official Anthropic MCP. Weekly CSV export from Seller Central → drop in `brand-brain/marketplace-revenue.csv`. Growth Analyst picks it up. |
| **Flipkart Seller Hub** | Marketplace Editor, Growth Analyst | Marketplace API exists. No official MCP. Same CSV pattern. |
| **Meesho Supplier** | Marketplace Editor, Growth Analyst | API exists. CSV pattern. |
| **Quick commerce (Blinkit, Zepto, Swiggy Instamart)** | Marketplace Editor, Growth Analyst | Brand portals only, no API access for most brands. Manual CSV from the portal. |

### Tier 4: conditional, add only if the case applies

| MCP | Add when | Skip when |
|---|---|---|
| **Canva** | You run creative in Canva and want Performance Marketer to drop variations into your brand kit | You hand creative off to a Figma-based designer |
| **Figma** | You have an in-house designer or agency on Figma | You are solo on creative |
| **Fal.ai** | You generate product mockups, lifestyle imagery or hero shots with AI | You shoot real product photography only |
| **Tavily** | You want Market Analyst to pull live web search instead of working off your pre-work notes | You are happy with manual competitor refresh every two weeks |
| **Google Calendar** | You want the Captain's standing schedule (Mon brief, Wed Brand Brain refresh, daily VoC sweep) to appear on a real calendar your team sees | You operate solo and the schedule lives in Claude Code |

### What to skip, even though they look tempting

| MCP | Why to skip for now |
|---|---|
| **Meta Ads, Google Ads** | OAuth setup is fragile, scope is broad and Performance Marketer works fine reading your `brand-brain/meta-ads-90d.csv` export. Revisit once you have a paid-channel manager on the team. |
| **Stripe, Razorpay Magic Checkout dashboards** | The payment data you need for the Monday brief is settlements and refunds, which Razorpay's main API surfaces. Magic Checkout analytics is a once-a-month read, not Monday data. |
| **Instagram, X, LinkedIn** | The social MCPs read engagement metrics. Engagement is a vanity number for D2C. Treat social as a publishing surface (Content Lead writes, you post), not a data source. |
| **Generic "any database" MCPs** | You do not have a database. You have a Shopify store, a Razorpay account and a few CSVs. Direct integrations beat SQL connectors at this stage. |
| **Tally** | Older accounting tool, no MCP, file-based exports only. If you are on Tally, treat it like a marketplace: weekly CSV into the brand-brain folder. |

### When no MCP exists: the webhook-to-file pattern

For WhatsApp gateways, shipping APIs and any vendor that exposes webhooks but has no MCP:

1. Set up the vendor webhook to POST events to a simple receiver (a Cloudflare Worker, a free Pipedream flow, or a Make.com scenario).
2. The receiver writes each event to a file in your `brand-brain/<vendor>/` folder, one JSON per file, dated.
3. The relevant teammate (Voice of Customer, Ops Manager, Growth Analyst) reads the folder during its weekly run.

This is how Session 9's marketplace CSV pattern works. The same shape works for WhatsApp conversation logs, Shiprocket NDR events and Razorpay refund webhooks. No MCP server to maintain.

---

## Skills

The workshop installs eight teammate skills and three subagents. The list below is what to add on top, focused on the operating jobs Indian D2C founders actually face. For the full curated bench — every marketplace, the exact install commands, the context-cost discipline and a Best/Efficient/Third pick per job — see **[Claude Skills Stack](references/resources/claude-skills-stack.md)**.

### Built-in, no install needed

These ship with Claude Code or are one click in the skills library. Listed only when there is a D2C-specific reason to reach for them.

| Skill | D2C use |
|---|---|
| **xlsx** | Cohort tables, marketplace CSV reconciliation, unit econ spreadsheets. The Growth Analyst reads xlsx via this skill when your `brand-brain/unit-economics.md` is a spreadsheet, not markdown. |
| **canvas-design** | Festival creative (Diwali, Rakhi, Holi, Wedding season), sale posters, distributor handouts, packaging mockups. The Indian D2C calendar is festival-driven and this skill produces the on-brand static visuals fast. |
| **pdf** | FSSAI labels, CDSCO product specs, BIS test reports, supplier invoices, returns dispute evidence. Compliance and vendor work runs on PDFs. |
| **skill-creator** | Your 11th teammate. The day a new operational pattern emerges (e.g. RTO predictor, festival calendar planner), use this to build the skill yourself. See "Build your own" below. |

### Worth installing on day one

| Skill | D2C reason |
|---|---|
| **humanizer** | Strip AI tells from Content Lead and Performance Marketer output before publishing. Customers are getting sensitive to AI-feel copy, especially on heritage and craft categories. Removes em dashes, "in today's fast-paced world", over-symmetric "X not Y" hooks. |

### Skip

| Skill | Why |
|---|---|
| **Generic productivity skills** (docx, pptx, calendar planners) | You already use these tools. They do not feed a teammate. |
| **Generic design-language skills** (industrial-brutalist, neumorphism etc.) | Your brand has its own voice and visual system. Imported design languages override it. |
| **General-purpose orchestration skills** | The Captain pattern from Session 10 is your orchestrator. A second orchestrator fragments the system. |
| **Generic dev skills** (frontend-design, claude-api, code-review) | Useful if you have engineers. Not part of an India D2C founder's weekly workflow. Add them if a developer joins your team. |

---

## Build your own: D2C-specific teammates worth creating

The workshop ships ten teammates. The list below is what most cohorts end up building in the months after, using the `skill-creator` skill or by hand. None of these exist as installable skills today; they are operating jobs unique to Indian D2C.

| Proposed teammate | Job | Inputs | Output cadence |
|---|---|---|---|
| **Festival Calendar Planner** | Plans your 12-month creative, content and offer calendar around Indian festivals (Diwali, Rakhi, Holi, Onam, Pongal, Wedding season, Republic Day, Independence Day) and category-specific peaks (Mother's Day for baby skincare, Valentine's for gifting) | CLAUDE.md (category, customer base), Market Analyst report | One-time per year, refreshed quarterly |
| **WhatsApp Template Compliance Checker** | Validates a WhatsApp Business template against Meta's approval rules (no promotional in utility, opt-in language, button limits, variable formatting) before you submit it for approval | Draft template, Meta template policy reference | On every new template |
| **Marketplace Label Compliance Checker** | Checks marketplace listings against FSSAI (food), CDSCO (cosmetics, OTC), BIS (electronics, toys) and Legal Metrology (MRP, net quantity) rules before you go live | Listing draft, category, supporting lab reports | On every new SKU |
| **RTO Predictor** | Flags orders likely to return-to-origin before they ship, so customer service can call ahead. Common Indian D2C ranges are 25 to 35% RTO on COD. | Shiprocket + Shopify orders, customer history, pin-code blacklist | Daily, just before dispatch cutoff |
| **Influencer Audience-Fit Checker** | Vets an influencer's audience composition against your buyer persona (geography, age, language, prior brand mentions) before you sign a deal | Influencer profile, persona cards from Voice of Customer | On every shortlist |
| **GST + HSN Sanity Checker** | Verifies HSN codes on invoices, GST rates, place-of-supply rules for inter-state vs intra-state. Saves you from quarterly reconciliation pain. | Zoho Books export, invoice PDFs | Weekly |
| **Promo Stack Validator** | Checks every active discount, coupon and storefront promo for stacking conflicts that destroy margin (e.g. site-wide 15% + first-order 10% + free-shipping over ₹499) | Shopify promo rules, GoKwik / Simpl config | Before any new promo goes live |
| **COD-to-Prepaid Converter** | Drafts WhatsApp messages and dynamic discounts to convert high-RTO-risk COD orders to prepaid before shipping | RTO Predictor output, customer phone, WhatsApp gateway | Daily, triggered by RTO Predictor |

These are the next ten weeks of work after the workshop, not the next ten days. Build them one at a time, in order of which one would have saved you the most pain last quarter.

---

## How to install

### MCPs
Run `/mcp` inside Claude Code to see the catalog and connect via OAuth. Most Tier 1 and Tier 2 entries with an "Official MCP" status connect in under two minutes. For "Community MCP" entries, verify the source repo before installing, since these run with your account scope.

For webhook-to-file integrations: any free workflow tool that can accept a webhook and write to your Drive folder will do. Pipedream and Make.com both have free tiers that cover the volume an early-stage D2C generates.

### Skills
Built-in skills run automatically when relevant. No install. Just write the prompt that needs them ("turn this brief into a PowerPoint", "humanize this content piece") and Claude picks the right skill.

External skills install with `/plugin` or by dropping them into `.claude/skills/`. The repo's existing teammate skills live there; add new skills alongside them.

### Build-your-own teammate skills
Inside Claude Code, run the `skill-creator` skill. Pass it the job description from the table above. It produces a draft SKILL.md you then edit against the patterns in the workshop's existing skills.

---

## Where to look for more

- **[AI Creative Stack](references/resources/ai-creative-stack.md)**: the curated model bench for ad creatives (video, image, voice over, talking heads, text posters, music) with best, efficient and third-best picks per category and a platform matrix.
- **[AI-Native D2C Operating Stack](references/resources/ai-native-d2c-stack.md)**: the sibling resource for the operating spine: commerce engine, support inbox, reviews, WhatsApp, lifecycle, attribution, fulfilment, marketplace ops, payments and the Claude Code orchestration layer that ties them together.
- **[Claude Skills Stack](references/resources/claude-skills-stack.md)**: the third sibling — the curated skills bench. Which skills and plugins to discover and install from the Anthropic marketplaces (`anthropic-agent-skills`, `claude-plugins-official`, the demo and community marketplaces), the exact `/plugin` install mechanics, a Best/Efficient/Third pick per job mapped to the ten teammates, the context-cost discipline, and what to skip.
- **Claude Code MCP catalog**: `/mcp` shows every server available to your account.
- **Anthropic skills library**: `docs.anthropic.com/en/docs/claude-code/skills` (catalog of officially supported skills).
- **Third-party skill directories**: `skills.sh`, `claudemarketplaces.com`, `claudeskills.info` index thousands of community skills. Treat them as a search engine, not a trust signal — every install goes through the vetting gate in [Claude Skills Stack](references/resources/claude-skills-stack.md) before it touches the brand.
- **This repo's Power-ups sections**: every Day-2 module has a "Power-ups" block listing optional add-ons per teammate, sized for take-home runs.
- **Office hours**: Week 2 and Week 4 office hours (see Session 10) are the right venue to ask "should I add X" before installing.

---

## A note on stack discipline

Founders in this cohort consistently over-install in the two weeks after the workshop. Every new MCP, every new skill, costs you context (more autoload), token budget (more reads per turn) and surface area for things to break.

The rule that holds: install the next tool the day a teammate visibly cannot do its job without it. Not before. The ten teammates plus three Tier 1 MCPs is enough to run a 10Cr D2C brand on Claude Code. Everything on this page is an addition you earn by hitting the wall, not a starter pack.
