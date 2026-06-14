# D2C Workshop — Student Repo (Draft)

This is the student-facing repo for theCrux AI D2C workshop. The structure ties each Claude Code primitive (terminal, CLAUDE.md, skills, MCPs, subagents, parallel dispatch, MCP-fed iteration, hooks, scheduled wake-ups, the Captain pattern) to a specific landing-page deliverable on thecrux.ai/d2c.

Founders read `student-handbook.md` and the per-session `session-N-NAME.md` files at the root. Instructor materials (day-level master maps, per-module BRIEFs) live in a separate private repo.

**Lost in the repo?** Open [`site/index.html`](site/index.html) in any browser. It is a single-page reference with the 2-day arc, every session card, the teammate roster, a skill catalog, a glossary and a full repo tour.

## Layout

```
thecrux-d2c-bootcamp/
├── README.md                                you are here
├── student-handbook.md                      FOUNDER master map (start here)
├── session-0-setup.md ... session-10-capstone.md   per-session files (11 total)
├── session-11-influencer-scout.md             add-on session (influencer discovery + negotiation)
├── CLAUDE.template.md                       the file Session 1 fills
├── resources.md                             curated tools and links for the workshop
├── site/
│   ├── index.html                           single-page repo reference (start here when lost)
│   └── sessions.html                        per-session flowcharts
├── .claude/
│   ├── commands/
│   │   ├── interview-me.md                  /interview-me slash command (Session 1, interview-first)
│   │   └── brand-brain.md                   /brand-brain slash command (Session 1, file-ingest-first)
│   ├── skills/
│   │   ├── market-analyst/SKILL.md          (Session 2)
│   │   ├── voice-of-customer/SKILL.md       (Session 2)
│   │   ├── write-in-brand-voice/SKILL.md    (Session 2, the one founders author themselves)
│   │   ├── creative-brief/SKILL.md          (Session 6)
│   │   ├── fal-image-gen/SKILL.md           (Session 6, fal.ai image and short-video generator)
│   │   ├── pdp-writer/SKILL.md              (Session 7)
│   │   ├── marketplace-editor/SKILL.md      (Session 7)
│   │   ├── ops-manager/SKILL.md             (Session 8)
│   │   ├── retention-manager/SKILL.md       (Session 8)
│   │   ├── growth-analyst/SKILL.md          (Session 9)
│   │   └── influencer-scout/SKILL.md        (Session 11, add-on)
│   └── agents/
│       ├── content-lead.md                  (Session 4 subagent)
│       ├── performance-marketer.md          (Session 6 parallel-dispatch parent)
│       └── captain.md                       (Session 10 cross-teammate orchestrator)
├── references/                              per-session deep-dive walkthroughs and canonical prompts
│   ├── module-0-setup/troubleshooting.md
│   ├── module-1-brand-brain/little-lab.example.md
│   ├── module-3-mcps/                       Shopify, Drive, Gmail setup walkthroughs
│   ├── module-4-agents/                     content types, brand safety checklist
│   ├── module-5-integration/captain-day-1.prompt.md
│   ├── module-6-performance-marketer/       ad angle parallelism, visual prompt templates
│   ├── module-7-storefront-marketplace/cro-iteration-loop.md
│   ├── module-8-ops-retention/hooks-and-triggers.md
│   ├── module-9-growth-analyst/             scheduled wake-up + Monday brief spec
│   ├── module-10-capstone/                  Captain prompt, 90-day roadmap, standing schedule
│   ├── module-11-influencer-scout/          Modash data shape, sample creator pool, rate card, negotiation playbook (add-on)
│   └── resources/                           AI creative stack, operating stack, tool deep-dives
└── examples/
    ├── little-lab/                          worked baby-skincare brand
    └── the-paan-legacy/                     worked gourmet-paan brand
```

## The 10 teammates and what they own

| # | Teammate | Day | Skill or agent | What they own |
|---|---|---|---|---|
| 01 | Brand Brain | Day 1 / Module 1 | `/interview-me` slash command + `CLAUDE.md` | Brand DNA, voice rules, compliance |
| 02 | Market Analyst | Day 1 / Module 2 | `/market-analyst` skill | Competitor intel, pricing, content cadence |
| 03 | Voice of Customer | Day 1 / Module 2 + 3 | `/voice-of-customer` skill | Themes, sentiment, persona cards |
| 04 | Content Lead | Day 1 / Module 4 | `content-lead` subagent | 30-day calendar, content pieces, marketplace listings |
| 05 | Marketplace Editor | Day 2 / Module 7 | `/marketplace-editor` skill | Amazon A+ blocks, Flipkart copy |
| 06 | Performance Marketer | Day 2 / Module 6 | `performance-marketer` subagent + `/creative-brief` skill | Ad variations across angles, creative briefs |
| 07 | Storefront Specialist | Day 2 / Module 7 | `/pdp-writer` skill | Shopify PDPs, landing pages, CRO observations |
| 08 | Ops Manager | Day 2 / Module 8 | `/ops-manager` skill | SOPs, vendor kit, returns analysis |
| 09 | Retention Manager | Day 2 / Module 8 | `/retention-manager` skill | WhatsApp + email retention flows, segments |
| 10 | Growth Analyst | Day 2 / Module 9 | `/growth-analyst` skill | Weekly Monday brief, unit economics |
| — | The Captain | Day 2 / Module 10 | `captain` subagent | Cross-teammate synthesis, 90-day roadmap |

## Primitives catalog

What lives in `.claude/`, grouped by primitive. Use this to find a teammate by the slash command you type.

### Slash commands (`.claude/commands/`)

| Command | Session | What it does |
|---|---|---|
| `/interview-me` | Session 1 | Module 1 in interview mode. Walks the founder section by section and writes `CLAUDE.md` from scratch. |
| `/brand-brain` | Session 1 | Module 1 in file-ingest mode. Reads `brand-brain/` first, then interviews only for the gaps. |

### Skills (`.claude/skills/`)

| Skill | Session | What it does |
|---|---|---|
| `/market-analyst` | Session 2 | Competitor intel report across pricing, positioning, content cadence and paid presence. |
| `/voice-of-customer` | Session 2 | Mines reviews, support tickets and chats for themes, sentiment and persona cards. |
| `/write-in-brand-voice` | Session 2 | The skill the founder authors themselves. Writes short-form copy using CLAUDE.md voice rules and `brand-brain/voice-dna/` samples. |
| `/creative-brief` | Session 6 | One-page brief that turns a Performance Marketer angle into a prompt the design tool can act on. |
| `/fal-image-gen` | Session 6 | Calls fal.ai to render real images and short videos (Flux, GPT Image 2, Kling, Veo). Used by the Performance Marketer for ad creative. |
| `/pdp-writer` | Session 7 | Rewrites Shopify PDPs and landing pages using live conversion data, VoC themes and competitor context. |
| `/marketplace-editor` | Session 7 | Rewrites Amazon A+ blocks and Flipkart listings using marketplace conversion data and reviews. |
| `/ops-manager` | Session 8 | Produces SOPs, vendor email templates, returns analyses and escalation playbooks. |
| `/retention-manager` | Session 8 | WhatsApp templates, email lifecycle flows, customer segments and re-engagement playbooks. |
| `/growth-analyst` | Session 9 | Weekly Monday brief, unit economics and dashboard observations. |
| `/influencer-scout` | Session 11 (add-on) | Modash-fed creator discovery, rate card and negotiation script. |

### Subagents (`.claude/agents/`)

| Subagent | Session | What it does |
|---|---|---|
| `content-lead` | Session 4 | 30-day content calendar plus a batch of pieces in one Task call. The first subagent founders meet. |
| `performance-marketer` | Session 6 | Parallel-dispatch parent. Fans out across 3 to 5 ad angles, each angle generating creative brief plus ad variants. |
| `captain` | Session 10 | Reads every teammate's index files (not raw outputs) and produces the 90-day roadmap at Capstone. |

## Status

**Day 1 instructor shape**: complete. 6 modules, 4 primitive assets at root, 1 canonical example (Little Lab).

**Day 2 instructor shape**: complete. 5 modules + Capstone, 11 primitive assets at root.

**Student handbook**: complete. `student-handbook.md` master + 11 `session-N-NAME.md` files at the repo root, written second-person to the founder.

**Pending (optional)**: example index files for Day-2 teammates so instructors have something concrete to flash and the Capstone Captain has something to chew on if a founder runs it before completing every module.

## Two design rules baked into every Day-2 module

### Rule 1: Index files, not raw outputs
Every teammate produces an index file (~500 tokens). The Captain at Capstone reads ONLY indexes (10 files, ~10K tokens). Never raw outputs. Keeps token cost manageable on Pro plan.

### Rule 2: Default vs Power scope
Every skill and subagent asks the founder to pick scope at the start. DEFAULT is sized for Pro plan and the workshop slot. POWER is for Max plan or take-home. Same teaching beat either way.

## Canonical samples: two worked brands across all 10 teammates

Two brands, fully worked, parallel structure. Use as instructor flash assets and as catch-up data for founders who fall behind.

- **Little Lab** (`examples/little-lab/`) — fictional baby skincare brand. Cosmetic category, CDSCO compliance, Amazon + Flipkart-heavy distribution, paediatrician-trust positioning.
- **The Paan Legacy** (`examples/the-paan-legacy/`) — real-brand-illustrative-numbers gourmet paan brand (thepaanlegacy.com). Food category, FSSAI compliance, Zomato + Swiggy-first distribution, heritage-meets-modernity positioning, corporate Diwali B2B funnel.

The contrast is deliberate: same 10-teammate framework, two very different category shapes. Instructors flash one brand for the cohort majority, switch to the other to show the framework holds across categories. Sample raw inputs (Shopify CSV, reviews export, support threads) live in each brand's `sample-inputs/` and double as Module 2 / Module 3 paste-in fallbacks.

## Reference

- **Pre-work** (canonical, send to founders before Saturday): **thecrux.ai/prework-d2c**
- Landing page: `thecrux-ai-d2c-workshop/landing-page/v3.html`
- Predecessor repo: `thecrux-ai-d2c-workshop/student-repo-v2/`
- Interview pattern source: `~/cardekho-sea-foundations/.claude/commands/interview-me.md`
- Student handbook shape reference: `~/cardekho-sea-foundations/student-handbook.md` and per-session files
- Canonical example brand: `references/module-1-brand-brain/little-lab.example.md` (Little Lab, baby skincare, fictional) + `examples/little-lab/` (full worked run across all 10 teammates)
