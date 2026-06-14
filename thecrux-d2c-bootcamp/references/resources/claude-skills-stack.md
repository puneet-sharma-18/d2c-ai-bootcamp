[← Back to Resources](resources.md)

---

# Claude Skills Stack for an Indian D2C Brand

**Verified as of 2026-06-06.** Sources: Claude Code official docs, the `anthropics/skills` and `anthropics/claude-plugins-official` repos, the in-app `/plugin` catalog, plus independent founder and marketing skill directories surveyed in the four weeks of May 9 to June 6, 2026. Marketplace contents and install commands move fast; re-verify before you add anything new.

This page is the third sibling of [`ai-creative-stack.md`](ai-creative-stack.md) and [`ai-native-d2c-stack.md`](ai-native-d2c-stack.md).

- The **creative stack** is the bench that produces pixels and audio.
- The **operating stack** is the SaaS spine the brand runs on (commerce, support, payments, fulfilment).
- This page is the **skills bench**: the playbooks you install into Claude Code so the orchestration layer (section 10 of the operating stack) actually knows how to do the work.

If a founder asks "which model makes the Diwali poster", point them at the creative stack. If they ask "what stack do I run my brand on", point them at the operating stack. If they ask **"what should I install into Claude so it works like a team and not a chatbot"**, this is the page.

---

## The thesis

A skill is the cheapest leverage in the whole stack. A model call costs money per token. A SaaS seat costs money per month. A skill costs almost nothing to install and turns a generic Claude into one that already knows your category, your compliance wall and your house style. The workshop builds ten teammate skills by hand. This page is what you bolt on around them, off the shelf.

Three rules decide every install:

1. **Install by the job, not by the hype.** There are thousands of skills in public marketplaces now. You need maybe fifteen. A skill earns its place when a teammate visibly cannot do its job without it, not because a thread called it "the 25 skills every founder needs".
2. **Context is the real price, not money.** Every installed skill and plugin costs context every single turn it can autoload, plus token budget every time it fires. Claude Code now shows a **Context cost** estimate in the `/plugin` detail pane before you install, so you can see exactly how many tokens a plugin adds to every request. Read that number. A bundle of 48 skills you use twice a year is a tax on every conversation you have.
3. **Own the ones that hold your brand. Rent the rest.** The skills that encode your voice, your customer and your compliance rules (`write-in-brand-voice`, the ten teammates, your `brand-guidelines`) live in your repo, version-controlled, yours forever. The skills that do generic mechanical work (turn this into a deck, extract this PDF, humanise this copy) are commodities you install and forget.

Three tiers per category, same shape as the sibling pages:

1. **Best:** the right install for an AI-orchestrated Indian D2C brand running the ten-teammate system.
2. **Efficient:** lighter context cost or simpler, when the Best tier is more than the job needs.
3. **Third:** picked for a specific job the first two miss (build-your-own, no-MCP vendors, the no-terminal founder).

Every skill below is real and installable as of June 2026 unless flagged `[verify]`.

---

## How a skill actually reaches Claude (the three doors)

Session 2 taught the three ways to acquire a skill. This is the same frame, with the marketplace mechanics filled in.

1. **Write your own.** A folder under `.claude/skills/<name>/` with one `SKILL.md`. Frontmatter (`name`, `description`) plus a body of plain-English instructions. The `description` is what decides autoload. This is how the ten teammates and your `write-in-brand-voice` skill exist.
2. **Run pre-shipped.** Skills already sitting in the repo (`.claude/skills/market-analyst/`, `voice-of-customer/`, `write-in-brand-voice/`). They autoload on the right prompt. No install.
3. **Install from a marketplace.** A **plugin** is the distribution format; a **skill** is the content. A plugin bundles one or more skills, and optionally commands, sub-agents, hooks and MCP servers. When you install a plugin you get every skill inside it.

The install loop, verified against the current docs:

```
/plugin marketplace add anthropics/skills        # register a catalog (no install yet)
/plugin                                            # open the manager: Discover / Installed / Marketplaces / Errors
/plugin install document-skills@anthropic-agent-skills
/reload-plugins                                    # activate without restarting
```

Things the docs make explicit and most founders miss:

- **Marketplace ≠ install.** Adding a marketplace only registers the catalog. You still pick each plugin. Think app store vs downloading an app.
- **The detail pane tells you the cost before you commit.** It shows a **Context cost** estimate, a **Last updated** date, and a **Will install** list of every command, agent, skill, hook and MCP/LSP server the plugin adds. Read all three before you press install. A stale "last updated" or a fat context cost is a reason to walk away.
- **Scope matters.** Install at **user** scope (you, everywhere), **project** scope (everyone on this repo, written to `.claude/settings.json`) or **local** scope (you, this repo only). For a cohort repo your whole team shares, project scope keeps everyone in sync.
- **Skills inside plugins are namespaced.** A plugin called `commit-commands` exposes `/commit-commands:commit`. Your hand-written repo skills are not namespaced.
- **Trust is on you.** Plugins run arbitrary code with your privileges. Anthropic curates the official marketplace and screens the community one, but third-party marketplaces are unscreened. Only add sources you trust.

---

## The marketplaces that matter for a D2C founder

You do not need fifteen marketplaces. Four cover everything this page recommends.

| Marketplace | Add it with | What it gives you | Trust |
|---|---|---|---|
| **`claude-plugins-official`** | Auto-available; `/plugin marketplace add anthropics/claude-plugins-official` if missing | Anthropic-curated directory. Connectors (Slack, Notion, Linear, Asana, Atlassian, Figma, Airtable), dev workflow plugins, `code-review`, `claude-md-management`, `claude-code-setup`, `context7`, `brightdata`. | Curated by Anthropic. |
| **`anthropic-agent-skills`** (`anthropics/skills`) | `/plugin marketplace add anthropics/skills` | The official Skills repo. `document-skills` (pptx, xlsx, docx, pdf), `canvas-design`, `brand-guidelines`, `mcp-builder`, `skill-creator`, `web-artifacts-builder`, `webapp-testing`, `internal-comms`, `theme-factory`, `algorithmic-art`. | Anthropic-authored. |
| **`claude-code-plugins`** (`anthropics/claude-code`, the demo marketplace) | `/plugin marketplace add anthropics/claude-code` | Example plugins, including **`frontend-design`** — the one Session 2 installs from here. | Anthropic-authored. |
| **`claude-community`** (`anthropics/claude-plugins-community`) | `/plugin marketplace add anthropics/claude-plugins-community` | Third-party plugins that passed Anthropic's automated validation and safety screening, each pinned to a commit SHA. | Screened, not authored, by Anthropic. |

Everything else (founder packs, marketing-skill libraries on random GitHub repos) is an **unscreened third-party marketplace**. Useful as an idea library, but read the `SKILL.md` before you let it touch customer-facing copy. Treat any marketplace you cannot read end to end as a borrowed power tool, not a trusted teammate.

---

## Discovery directories (skills.sh and the aggregator sites)

There is a difference founders trip over. A **marketplace** is the thing `/plugin marketplace add` consumes — a GitHub repo (or git URL) with a `marketplace.json`, which you install plugins *from*. A **directory** is a website that indexes thousands of skills scraped from public GitHub so you can *find* one, then go add its underlying repo. The four trusted marketplaces above are where you **install**. The directories below are where you **discover**. A directory is a search engine, not a trust signal.

| Directory | What it is | Scale / curation | D2C verdict |
|---|---|---|---|
| **skills.sh** | Public directory of free community skills with a leaderboard ranked by total installs and "trending" filters. Ships a companion `skills-sh-marketplace` skill so Claude can search and pull from it inside a session. | Thousands, community-ranked, low curation | Best for **discovery by popularity**. Obey the install-count floor (below). The in-session install skill is convenient and a footgun — vet before you enable. |
| **claudemarketplaces.com** | Largest community-curated catalogue of skills, plugins and MCP servers, updated daily from GitHub. ~200k monthly visitors, 20k+ skills indexed. | Large, browse-by-category, light curation | Best **browse-by-category** catalogue (frontend, marketing, ops…). Always click through to the source repo before installing. |
| **claudeskills.info** | Free directory of 600+ skills including the official Anthropic set plus community submissions. No paid tier. | Mid-size, includes official | Clean place to **find the official skills** and well-known community ones. Lowest-risk of the directories. |
| **SkillsMP (skillsmp.com) / LobeHub** | Index hundreds of thousands of `SKILL.md` files scraped from public GitHub, searchable by keyword, role and creator. | Huge (800k+), minimal curation | Use **only with the full vetting gate**. Enormous reach, near-zero screening — never the path for a customer-facing or credentialed skill. |
| **Agensi (agensi.io)** | Positions as a security-scanned skills marketplace; installs via a `curl` command, some paid tiers. | Curated, scan-claimed | The **"someone else vetted it"** lane. Useful when you want a safety screen you did not run yourself — but verify the scan claims rather than trusting the label. |

**Sources:** [skills.sh explained](https://learnaiwithmariah.com/guides/claude-skills-marketplace/) • [skills.sh manager](https://mcpmarket.com/tools/skills/skills-sh-marketplace-manager) • [claudemarketplaces.com](https://claudemarketplaces.com/) • [claudeskills.info](https://claudeskills.info/) • [skillsmp.com](https://skillsmp.com/) • [lobehub.com/skills](https://lobehub.com/skills) • [Best AI agent skill marketplaces 2026 (Agensi)](https://www.agensi.io/learn/best-ai-agent-skills-marketplaces-2026)

**The vetting gate — run every third-party skill through this before it touches your brand:**

1. **Install-count floor.** The skills.sh community rule of thumb: anything under ~1,000 installs is risky. Popularity is a discovery signal, not a safety guarantee, but a near-zero count plus an unknown author is an easy no.
2. **Known publisher.** Anthropic, a named company (Vercel, Shopify, Razorpay), or a developer with a real public profile and history. No profile, no install.
3. **Last-updated recency.** Stale skills drift out of step with Claude and the tools they wrap. The `/plugin` detail pane shows the date.
4. **Read the `SKILL.md` end to end.** What files does it touch, what commands does it run, does it make network calls, does it ask for keys. If you cannot read it, you cannot trust it.
5. **Check the Context cost** in the `/plugin` pane before you enable it (see section 11).
6. **Brand-safety gate (the founder-specific one).** Never let an unvetted skill write customer-facing copy, handle PII, or hold credentials. For a food, wellness or baby brand, an unvetted skill that drafts a health claim is a **compliance risk**, not just a code risk — it can put an unsubstantiated claim on a live PDP. The FSSAI claim wall in CLAUDE.md does not protect you from a skill that bypasses your `write-in-brand-voice` safety pass.

**Rule of thumb:** Use a directory as a search engine to *find* a skill, then install it from its real source repo with `/plugin marketplace add owner/repo` and put it through the gate. Order of preference, always: Anthropic-authored → community-screened (`claude-community`) → high-install, named-publisher third-party. For a solo or early-stage founder, you will rarely need to leave the four trusted marketplaces at all — the directories are for the month you hit a wall no first-party skill covers.

---

## 1. Deliverables you hand to a human (decks, sheets, docs, labels)

The work product that leaves Claude as a file someone else opens: a pitch deck, a distributor sheet, a vendor contract, an FSSAI label PDF. This is the highest-frequency install for a founder and the one Session 2 already sets up.

| Tier | Skill / bundle | Why it wins now | Install |
|---|---|---|---|
| **Best** | **`document-skills`** bundle (`anthropic-agent-skills`) | Four production-grade skills in one plugin: **`pptx`** (investor and distributor decks, the Session 10 capstone deck), **`xlsx`** (unit economics, cohort tables, marketplace CSV reconciliation), **`docx`** (vendor contracts, SOPs, investor memos), **`pdf`** (read FSSAI labels, CDSCO specs, BIS reports, supplier invoices; fill and extract forms). | `/plugin install document-skills@anthropic-agent-skills` |
| **Efficient** | A single skill from the bundle | If you only ever build decks, the whole bundle is context you do not need. The skills install individually in some catalogs; otherwise install the bundle and lean on the one you use. Context cost is the deciding factor. | per-skill where available |
| **Third** | **`doc-coauthoring`** + **`internal-comms`** (`anthropic-agent-skills`) | Long-form collaborative documents (a brand book, a 12-month plan) and polished internal announcements (a price-change memo to your distributors, a festival-readiness note to the team). | `/plugin install …@anthropic-agent-skills` |

**Sources:** [anthropics/skills](https://github.com/anthropics/skills) • [Claude Code: discover & install plugins](https://code.claude.com/docs/en/discover-plugins)

**Rule of thumb:** Install `document-skills` on day one (Session 2 does this). It is the one bundle whose every component a D2C founder touches monthly: the deck, the unit-econ sheet, the contract, the compliance PDF.

---

## 2. On-brand visual craft (so output does not look generic)

The difference between a PDP that converts and one that reads "made by AI" is design knowledge. These skills give Claude taste and, more importantly, **your** taste.

| Tier | Skill | Why it wins now | Install |
|---|---|---|---|
| **Best** | **`frontend-design`** (`claude-code-plugins`) + **`brand-guidelines`** (`anthropic-agent-skills`) | `frontend-design` gives Claude real layout, typography and hierarchy knowledge (Session 2 installs it; Session 7 PDPs and landing pages get sharper). `brand-guidelines` lets you encode your colours, type, logo rules and never-words once, so every visual output respects the brand system instead of inventing a new one each time. | `/plugin install frontend-design@claude-code-plugins` and `…brand-guidelines@anthropic-agent-skills` |
| **Efficient** | **`canvas-design`** (`anthropic-agent-skills`) | Fast on-brand static visuals: festival creatives (Diwali, Rakhi, Holi, wedding season), sale posters, distributor handouts, packaging mockups. The Indian D2C calendar is festival-driven; this turns a brief into a visual quickly. Pairs with the [creative stack](ai-creative-stack.md) for the hero pixels. | `/plugin install canvas-design@anthropic-agent-skills` |
| **Third** | **`theme-factory`** / **`web-artifacts-builder`** (`anthropic-agent-skills`) | `theme-factory` generates a cohesive visual theme you reuse across assets. `web-artifacts-builder` builds self-contained interactive HTML — an ingredient explorer, a gifting configurator, a size guide — that lives on or beside the PDP. | `/plugin install …@anthropic-agent-skills` |

**Sources:** [anthropics/skills](https://github.com/anthropics/skills) • [claude.com/plugins](https://claude.com/plugins)

**Devanagari and Indian-script caveat:** none of these skills render legible Devanagari or regional scripts inside a generated image. That is a model-level limit covered in the [creative stack](ai-creative-stack.md) (Nano Banana Pro is the only model with a primary-source Devanagari claim). Generate the background here, layer compliance and festival text in a real compositor. Never let a skill render your FSSAI number, MRP or net quantity.

**Rule of thumb:** `frontend-design` + `brand-guidelines` is the pair that pays for itself. Skip imported design-language skills (industrial-brutalist, neumorphism, generic "make it beautiful" packs) — your brand already has a visual system, and an imported aesthetic overrides it. The power-design skills (`impeccable`, `ui-ux-pro-max`, `interface-design`) are real and strong, but they are for a team with a designer; below that, the pair above is enough.

---

## 3. Copy quality and de-AI-ing

Customers in heritage and craft categories are now allergic to AI-feel copy. These skills protect the thing your brand sells: a human voice.

| Tier | Skill | Why it wins now | Install |
|---|---|---|---|
| **Best** | **`write-in-brand-voice`** (you build it, Session 2) | Reads CLAUDE.md voice rules and `brand-brain/voice-dna/`, applies your never-words as hard filters, runs a brand-safety pass, names its sources. Nothing off the shelf knows your voice. This is the one copy skill you must own, not rent. | hand-written in `.claude/skills/` |
| **Efficient** | **`humanizer`** | Strips the AI tells before anything publishes: em-dash overuse, "in today's fast-paced world", over-symmetric "X, not Y" hooks, the rule-of-three filler, inflated symbolism. Run it on every Content Lead and Performance Marketer output. Already recommended day-one in [`resources.md`](resources.md). | community / direct skill |
| **Third** | **Marketing skill packs** (e.g. `coreyhaines31/marketingskills`, `alirezarezvani/claude-skills`) | Large third-party libraries of copywriting, landing-page, launch and SEO playbooks. Useful as a frameworks library (StoryBrand, Hook Model, JTBD). | `/plugin marketplace add coreyhaines31/marketingskills` |

**Sources:** [Top 8 Claude skills for founders (Snyk)](https://snyk.io/articles/top-8-claude-skills-entrepreneurs-startup-founders-solopreneurs/) • [Best marketing skills 2026 (Composio)](https://composio.dev/content/best-marketing-skills)

**The order of operations that matters:** generate in `write-in-brand-voice`, then pass through `humanizer`. Never the reverse, and never let a third-party marketing pack write the final customer-facing line — those packs carry a generic American-startup register that will fight your heritage voice. Use them for structure (what sections a launch email needs), not for the words.

**Rule of thumb:** Own `write-in-brand-voice`, install `humanizer`, and treat every external marketing pack as a checklist, not a ghostwriter.

---

## 4. Storefront, PDP and web (the Storefront Specialist's bench)

| Tier | Skill | Why it wins now | Install |
|---|---|---|---|
| **Best** | **`frontend-design`** (`claude-code-plugins`) | Design-quality PDP and landing-page structure. The same skill from section 2, doing double duty: Session 7 produces sharper storefront copy and layout with it loaded. | `/plugin install frontend-design@claude-code-plugins` |
| **Efficient** | **`web-artifacts-builder`** (`anthropic-agent-skills`) | Ships interactive storefront pieces without an engineer: a "build your gifting box" configurator, an ingredient-origin map, a paan-vs-supari explainer. Self-contained HTML you can hand to your Shopify theme. | `/plugin install web-artifacts-builder@anthropic-agent-skills` |
| **Third** | **`webapp-testing`** (`anthropic-agent-skills`) or **`playwright-cli`** | Dogfood the live storefront: does the PDP render, does add-to-cart fire, does the COD form submit, does the festival banner show on mobile. QA the thing customers actually touch before you spend on ads driving to it. | `/plugin install webapp-testing@anthropic-agent-skills` |

**Sources:** [anthropics/skills](https://github.com/anthropics/skills) • [discover-plugins](https://code.claude.com/docs/en/discover-plugins)

**Rule of thumb:** The Shopify **data** comes through the Shopify MCP (see [`resources.md`](resources.md) and [`ai-native-d2c-stack.md`](ai-native-d2c-stack.md)). These skills are the **craft** layer on top — they make the page good, the MCP makes it true. You need both.

---

## 5. Research and intelligence (Market Analyst, Voice of Customer)

| Tier | Skill | Why it wins now | Install |
|---|---|---|---|
| **Best** | **`deep-research`** | Fans out parallel web searches, fetches sources, cross-checks claims and writes a cited report. The right engine behind Market Analyst when you want a real competitive landscape, not a single-pass profile. | community / direct skill |
| **Efficient** | **`reddit-research`** | Mines Reddit (r/IndianFood, r/india, category subs) for unfiltered sentiment, complaints and the language real buyers use. Feeds Voice of Customer with the words customers actually say. | direct skill |
| **Third** | **`brightdata`** plugin (`claude-plugins-official`) | Structured web extraction and search at scale when you need to monitor competitor pricing or listings on a schedule. Heavier than you need below ₹3Cr ARR; reach for it when manual competitor refresh stops scaling. | `/plugin install brightdata-plugin@claude-plugins-official` |

**Sources:** [claude-plugins-official directory](https://github.com/anthropics/claude-plugins-official) • [discover-plugins](https://code.claude.com/docs/en/discover-plugins)

**Rule of thumb:** `deep-research` for the quarterly category deep-dive, `reddit-research` for the monthly sentiment pulse, and your Market Analyst / Voice of Customer teammates as the standing interpreters that read both into a brief. Live web scraping is a tool you add when a teammate hits the wall, not a starter install.

---

## 6. Build your own and keep the system healthy (the meta layer)

The highest-leverage skills are the ones that make more skills and keep the existing ones sharp. This is the layer that turns a one-time workshop into a system that compounds.

| Tier | Skill | Why it wins now | Install |
|---|---|---|---|
| **Best** | **`skill-creator`** (`anthropic-agent-skills`) | Your 11th teammate-maker. The day a new operating pattern appears (RTO predictor, festival calendar planner, GST sanity checker — see the build-your-own table in [`resources.md`](resources.md)), this writes a draft `SKILL.md` you then edit. Teaches the Agent Skills spec as it goes. | `/plugin install skill-creator@anthropic-agent-skills` |
| **Efficient** | **`claude-md-management`** (`claude-plugins-official`) | Audits and improves CLAUDE.md — your brand brain, the file every teammate reads first. As the brand grows, this keeps it tight, current and non-contradictory instead of letting it rot into a wall of stale facts. | `/plugin install claude-md-management@claude-plugins-official` |
| **Third** | **`mcp-builder`** (`anthropic-agent-skills`) | Wraps a vendor that has no official MCP — WATI, Shiprocket, Interakt, a quick-commerce portal — into one Claude can read. The single most valuable skill for an Indian D2C founder, because half the operating stack has no MCP yet (see the operating stack, sections 4, 7, 8). | `/plugin install mcp-builder@anthropic-agent-skills` |

**Sources:** [skill-creator SKILL.md](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md) • [claude-plugins-official](https://github.com/anthropics/claude-plugins-official)

**Also useful:** **`claude-code-setup`** (`claude-automation-recommender`) analyses your repo and recommends which hooks, skills, agents and MCPs to add — a good once-a-quarter "what am I missing" pass.

**Rule of thumb:** `skill-creator` and `claude-md-management` are the two that make every future month cheaper. `mcp-builder` is the India-specific unlock — it is how you get live WhatsApp and shipping data into a teammate without waiting for the vendor to ship an MCP.

---

## 7. Connectors-as-plugins (the bridge to the MCP page)

The `claude-plugins-official` marketplace ships **external-integration plugins** that bundle a pre-configured MCP server, so you connect a tool without hand-editing config. For a D2C founder the relevant ones are a small set; the rest are engineer tools.

| Plugin | Feeds | Use it when |
|---|---|---|
| **`slack`** | Ops Manager, the Captain | Your team coordinates in Slack and you want the Monday brief or an escalation to land there. |
| **`notion`** | Brand Brain, Content Lead | Your SOPs, content calendar or brand wiki live in Notion. |
| **`airtable`** | Ops Manager, Growth Analyst | You run vendor, inventory or influencer data in Airtable bases. |
| **`figma`** | Storefront Specialist, Performance Marketer | You have a designer or agency on Figma and want Claude to read the file. |

**Sources:** [discover-plugins: external integrations](https://code.claude.com/docs/en/discover-plugins) • [claude-plugins-official](https://github.com/anthropics/claude-plugins-official)

**Do not duplicate the MCP page.** The core commerce connectors — **Shopify, Google Drive, Gmail, Razorpay, Klaviyo** — and the webhook-to-file pattern for no-MCP vendors are covered in the Skills/MCPs sections of [`resources.md`](resources.md) and in [`ai-native-d2c-stack.md`](ai-native-d2c-stack.md). This row is only the plugin-packaged connectors that overlap a founder's weekly workflow. Skip the rest of the official directory: the `aws-*`, `*-lsp`, `bigquery`, `cockroachdb`, `sentry`-class plugins are for software teams, not a paan brand.

---

## 8. The adjacent ecosystem (the no-terminal path and the idea libraries)

Two things exist next to the Claude Code skills world that a founder will hear about. Treat them honestly.

**Claude for Small Business (the Claude.ai app, not Claude Code).** Anthropic shipped a small-business product with a set of pre-built skills — payroll planning, bookkeeping reconciliation, business insights, marketing campaigns, employee onboarding — plus one-click connectors to QuickBooks, Stripe, Square, PayPal, Gmail, Google Drive, Calendar, Microsoft 365, Docusign, Slack, Canva and Webflow. `[verify current skill list and India connector support]`

- **When it fits:** a founder who will not open a terminal and wants finance, admin and basic marketing handled inside a chat app with native connectors.
- **The trade-off:** you do not get version-controlled, brand-owned skills. Your voice rules, compliance wall and the ten-teammate system live in *your* repo in the Claude Code path; in the app, you rent Anthropic's generic skills. For an Indian D2C brand, the connector list also skews US (QuickBooks, not Zoho Books; Square, not Razorpay) — check India support before you lean on it.

**Third-party founder / marketing skill libraries.** `coreyhaines31/marketingskills` (full marketing lifecycle), `alirezarezvani/claude-skills` (48 skills across seven bundles), `wondelai/skills` (product/strategy frameworks), `founder-skills` and similar repos. These are genuine idea libraries.

- **When it fits:** you want a structural checklist for a job you have not done before (a Product Hunt-style launch, a landing-page teardown, a pricing model).
- **The trade-off:** unscreened, generic-voiced, and high context cost if you install a whole bundle. Read the `SKILL.md`, lift the structure, and never wire one straight into customer-facing output. They are reference, not teammates.

**Sources:** [Claude for Small Business (Inc.)](https://www.inc.com/ben-sherry/anthropics-newest-claude-feature-is-here-to-help-small-business-owners-with-their-pain-points/91343926) • [Top 8 founder skills (Snyk)](https://snyk.io/articles/top-8-claude-skills-entrepreneurs-startup-founders-solopreneurs/) • [Best marketing skills (Composio)](https://composio.dev/content/best-marketing-skills)

---

## 9. The install list, mapped to the ten teammates

The whole page, condensed to what each teammate gains. Install in this order; stop when a teammate can do its job.

| Teammate | Skill that sharpens it | Marketplace |
|---|---|---|
| **Brand Brain** | `claude-md-management`, `brand-guidelines` | official / agent-skills |
| **Market Analyst** | `deep-research`, `brightdata` | direct / official |
| **Voice of Customer** | `reddit-research` | direct |
| **Content Lead** | `write-in-brand-voice` (own), `humanizer`, `canvas-design` | own / direct / agent-skills |
| **Marketplace Editor** | `document-skills` (xlsx, pdf) | agent-skills |
| **Performance Marketer** | `frontend-design`, `canvas-design` + the [creative stack](ai-creative-stack.md) | claude-code-plugins / agent-skills |
| **Storefront Specialist** | `frontend-design`, `web-artifacts-builder`, `webapp-testing` | claude-code-plugins / agent-skills |
| **Ops Manager** | `mcp-builder`, `document-skills` (pdf, docx), `slack`/`airtable` | agent-skills / official |
| **Retention Manager** | `mcp-builder` (WhatsApp gateway), `write-in-brand-voice` | agent-skills / own |
| **Growth Analyst** | `document-skills` (xlsx, pptx) | agent-skills |
| **The Captain (orchestrator)** | `skill-creator`, `claude-code-setup` | agent-skills / official |

This is roughly a dozen distinct installs. That is the whole bench. If your list is growing past twenty, you are collecting, not equipping.

---

## 10. End-to-end workflows (combine the skills)

### Capstone pitch deck from the brand brain

1. **Growth Analyst** pulls the numbers (Shopify MCP, Razorpay MCP) into an `xlsx` via `document-skills`.
2. **`write-in-brand-voice`** drafts the narrative in the founder's register; **`humanizer`** strips the tells.
3. **`brand-guidelines`** enforces colours, type and logo rules; **`pptx`** (`document-skills`) builds the deck.
4. Output: an investor or distributor deck that reads like the brand, not like a template.

### Festival creative batch (Diwali, Rakhi, wedding season)

1. **Content Lead** plans the calendar; **`canvas-design`** lays out the poster set on-brand.
2. The hero pixels come from the [creative stack](ai-creative-stack.md) (Nano Banana Pro for Devanagari, Flux 2 for lifestyle).
3. **`brand-guidelines`** keeps every variant in the system; compliance text (FSSAI, MRP) layered in a real compositor, never model-rendered.
4. Output: 8–12 festival variants in an afternoon, each on-brand and compliant.

### Wire a no-MCP vendor so a teammate can read it

1. **`mcp-builder`** wraps the WATI (or Shiprocket) REST API into an MCP server.
2. **Retention Manager** (or Ops Manager) now reads live WhatsApp / shipping data instead of a pasted export.
3. **`skill-creator`** builds the standing teammate that runs on it (e.g. an RTO Predictor).
4. Output: a vendor with no official MCP becomes a live data source for the weekly run.

### Build the eleventh teammate

1. Pick the job from the build-your-own table in [`resources.md`](resources.md) (RTO Predictor, Festival Calendar Planner, GST Sanity Checker…).
2. **`skill-creator`** drafts the `SKILL.md`; you edit the `description` against how you actually talk and the body against the existing teammates.
3. Test the autoload, sharpen the description, commit it to the repo.
4. Output: a permanent, version-controlled teammate that did not exist this morning.

---

## 11. Context-cost discipline (the rule that keeps this fast)

This is the section the sibling pages do not need and this one cannot skip, because skills have a cost that is invisible until it hurts.

- **Every enabled skill and plugin is read on the turns it can autoload.** Twenty installed skills is twenty descriptions Claude weighs on every prompt, plus the full body each time one fires. The `/plugin` detail pane's **Context cost** estimate is the number to watch.
- **Bundles are the trap.** A 48-skill founder pack you installed for one landing-page template taxes every conversation. Install the single skill if the catalog allows it; if not, weigh the bundle's whole cost against the one job.
- **Disable beats uninstall for seasonal skills.** `/plugin disable <name>@<marketplace>` parks a skill (e.g. a festival-only `canvas-design` push) without losing it; re-enable when the season returns. `/reload-plugins` applies the change live.
- **Audit quarterly.** Run `/plugin list` and `claude-code-setup`. Anything you have not used in a quarter, disable. The ten teammates plus the dozen installs on this page is a complete bench; everything else is earned by hitting a wall.

**The discipline in one line:** install the skill the day a teammate visibly cannot do its job without it. Not before. The same rule the operating stack and `resources.md` end on, because over-installing is the failure mode every cohort hits in week two.

---

## 12. What to skip

| Skill / category | Why skip (June 2026) |
|---|---|
| **Generic design-language skills** (industrial-brutalist, neumorphism, "make it stunning" packs) | Your brand has its own visual system. An imported aesthetic overrides it. Use `brand-guidelines` + `frontend-design`. |
| **Whole 40-to-50-skill founder/marketing bundles** | Context tax on every turn for skills you use twice a year. Lift the structure, install the one you actually need. |
| **A second orchestrator skill** | The Captain (Session 10) is your orchestrator. A second one fragments the system and competes for the same prompts. |
| **Dev-only plugins** (`*-lsp`, `code-review`, `aws-*`, `cockroachdb`, `sentry`, `pr-review-toolkit`) | Built for software teams. Zero weekly use for a paan brand. Add only if a developer joins and works in this repo. |
| **Third-party packs you cannot read end to end** | Plugins run arbitrary code with your privileges. Unreadable source touching customer copy or credentials is a no. |
| **Skills installed straight from a directory without the vetting gate** | skills.sh, SkillsMP and the aggregator sites index unscreened public GitHub. Discovery ≠ safety. Run every one through the six-point gate before it touches the brand. |
| **Marketing packs as ghostwriters** | Generic register fights a heritage voice. Use for checklists, not the final line. |
| **Anything with a stale "Last updated"** | An abandoned skill drifts out of date with Claude and the tools it wraps. The detail pane shows the date; respect it. |

---

## 13. India-specific calls

- **`mcp-builder` is the binding India unlock.** Half the operating stack — WhatsApp gateways (WATI, Interakt, AiSensy), Shiprocket, quick-commerce portals — has no official MCP in 2026. `mcp-builder` is how you get them into a teammate. Prioritise it over almost any creative skill.
- **`document-skills` `pdf` is your compliance workhorse.** FSSAI labels, CDSCO specs, BIS reports, Legal Metrology declarations, supplier invoices, returns-dispute evidence — the Indian regulatory layer runs on PDFs.
- **`document-skills` `xlsx` over any dashboard skill.** Marketplace reconciliation (Amazon, Flipkart, Meesho, quick-commerce) is CSV-export-and-read for the foreseeable future (see operating stack, section 8). `xlsx` reads those exports directly.
- **Claude for Small Business connectors skew US.** QuickBooks not Zoho Books, Square not Razorpay. Verify India support before relying on the app path; the Claude Code + MCP path covers Indian tools better.
- **Devanagari and regional scripts:** no skill renders them legibly inside an image. Background from a skill, script overlaid in a compositor. Model-level coverage is in the [creative stack](ai-creative-stack.md).

---

## 14. How this resource gets used in the workshop

- **Session 1 (Brand Brain):** `claude-md-management` and `brand-guidelines` keep the file every teammate reads sharp and enforce the visual system.
- **Session 2 (Skills):** installs `frontend-design` and `document-skills` — the day-one baseline this page builds on. The three doors to a skill are taught here.
- **Session 3 (MCPs):** `mcp-builder` is how you extend past the three wired MCPs to India's no-MCP vendors.
- **Session 4 (Content Lead):** `write-in-brand-voice` + `humanizer` + `canvas-design` produce the calendar's copy and creatives.
- **Session 6 (Performance Marketer) & 7 (Storefront):** `frontend-design`, `web-artifacts-builder`, `webapp-testing` and the [creative stack](ai-creative-stack.md) ship the ads and pages.
- **Session 10 (Capstone):** `skill-creator` builds the eleventh teammate; `document-skills` (`pptx`) builds the founder deck; `claude-code-setup` audits the whole system.

The workshop installs the baseline. This page is the bench you grow into, one earned install at a time.

---

## Re-verification cadence

Marketplace catalogues and install commands move on a 2 to 4 week cadence — faster than the SaaS operating stack, in the same range as the creative models. This page is stamped **2026-06-06**. Re-verify before you add anything customer-facing or anything that handles credentials. The four canonical pages to check first:

1. [code.claude.com/docs/en/discover-plugins](https://code.claude.com/docs/en/discover-plugins) (install mechanics, official marketplace)
2. [github.com/anthropics/skills](https://github.com/anthropics/skills) (the official Skills repo and its current list)
3. [github.com/anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) (the curated plugin directory)
4. [claude.com/plugins](https://claude.com/plugins) (the in-browser catalog) and the `/plugin` Discover tab in your own session
5. [skills.sh](https://skills.sh/) and [claudemarketplaces.com](https://claudemarketplaces.com/) (the community pulse — what founders outside the official catalogue are actually installing, with the vetting gate applied)

For the SaaS spine these skills run on, go to [`ai-native-d2c-stack.md`](ai-native-d2c-stack.md). For the models they call, go to [`ai-creative-stack.md`](ai-creative-stack.md).
