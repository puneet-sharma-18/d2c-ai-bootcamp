# D2C Workshop — Student Handbook

Welcome. Over this weekend you will hire, onboard and put to work ten AI teammates for your D2C brand. Not modules. Not exercises. Teammates with a job description, an inbox of work, a tool kit and a shipping bar.

By Sunday evening, every teammate is operational on YOUR brand, YOUR data and YOUR competitors. You walk out with a working command center and a 90-day operating plan.

This handbook is your map. Each session has its own file. Open one session at a time. Every prompt you need is inside the session file.

> **Lost?** Open the **[Reference site](site/index.html)** in your browser. It has the 2-day arc, every session card, the teammate roster, a skill catalog, a glossary and a full repo tour on one page.

---

## The arc

### Day 1 — Intelligence & Content (Saturday)

Four primitives, in order. Each one unlocks one teammate.

| Block | What it is | What you do with it |
|---|---|---|
| **CLAUDE.md** | A persistent profile of your brand, voice, products, customers | Drives the voice across every later build |
| **Skills** | Reusable playbooks Claude autoloads when relevant | The thing that turns Claude from a chat tool into teammates |
| **MCPs** | The plug that connects Claude to Shopify, Drive, Gmail | Lets your skills read live data, not just files on disk |
| **Subagents** | Specialised teammates that run in their own context for big jobs | Ship multi-piece deliverables (30-day calendar, 20 content pieces) |

By the end of Day 1 you can answer four questions cleanly: *What is in CLAUDE.md? What is a skill? What is an MCP? What is a subagent?* If you can, Day 2 is just doing.

### Day 2 — Growth & Operations (Sunday)

Five new advanced concepts braided into the existing primitives. Each one operationalises a layer of the brand.

| Block | What it is | What you ship |
|---|---|---|
| **Parallel dispatch** | Spawn 5 subagents in parallel | 50+ ad variations across 5 angles (Power) |
| **MCP-fed iteration** | Read live data, diagnose, rewrite, push to draft | Rewritten PDPs and marketplace listings |
| **Hooks and triggers** | When X happens, do Y | SOPs and retention messages tied to events |
| **Scheduled wake-ups** | Time-based hooks (every Monday 09:00) | Weekly Monday brief lands automatically |
| **Captain pattern** | A subagent that synthesises across all teammates | 90-day operating roadmap, cross-cutting weekly recommendation |

Plus the Capstone: all 10 teammates wired into one Command Center.

---

## The Roster

| # | Teammate | What they own | Day | Session |
|---|---|---|---|---|
| 01 | **Brand Brain** | Your AI Chief of Staff. Holds brand DNA, tone, products, customers. Every other teammate reads from them. | Sat | [Session 1](session-1-brand-brain.md) |
| 02 | **Market Analyst** | Tracks 3 to 5 competitors. Flags what is working in the category. | Sat | [Session 2](session-2-skills.md) |
| 03 | **Voice of Customer** | Mines reviews, tickets, WhatsApp chats for themes and persona signals. | Sat | [Session 2](session-2-skills.md) + [Session 3](session-3-mcps.md) |
| 04 | **Content Lead** | 30-day calendar, content pieces, marketplace listings. Brand safety pass on every output. | Sat | [Session 4](session-4-content-lead.md) |
| 05 | **Marketplace Editor** | Amazon A+ blocks, Flipkart copy. Goes deeper than Day-1's first pass. | Sun | [Session 7](session-7-storefront-marketplace.md) |
| 06 | **Performance Marketer** | 50+ ad variations across angles. Creative briefs for design or AI image tools. | Sun | [Session 6](session-6-performance-marketer.md) |
| 07 | **Storefront Specialist** | Shopify PDPs, landing pages, CRO. Reads live conversion data. | Sun | [Session 7](session-7-storefront-marketplace.md) |
| 08 | **Ops Manager** | Vendor kit, SOPs, returns analysis. Trigger-based playbooks. | Sun | [Session 8](session-8-ops-retention.md) |
| 09 | **Retention Manager** | WhatsApp + email retention flows. Customer segments. | Sun | [Session 8](session-8-ops-retention.md) |
| 10 | **Growth Analyst** | Weekly Monday brief. Unit economics. The one number that needs your attention. | Sun | [Session 9](session-9-growth-analyst.md) |
| — | **The Captain** | Cross-teammate synthesis. 90-day roadmap. The orchestrator. | Sun | [Session 10](session-10-capstone.md) |

---

## Day 1 sessions (Saturday)

| # | Session | Outcome |
|---|---|---|
| 0 | [Setup](session-0-setup.md) | Claude Code running in the terminal, repo cloned, ready to type |
| 1 | [Brand Brain](session-1-brand-brain.md) | CLAUDE.md filled in your voice, voice-test passed |
| 2 | [Skills](session-2-skills.md) | Market Analyst + Voice of Customer skills, two real reports in `my-work/` |
| 3 | [MCPs](session-3-mcps.md) | Shopify + Drive + Gmail connected, VoC re-run with live data |
| 4 | [Content Lead](session-4-content-lead.md) | 30-day calendar + priority content pieces + marketplace listings |
| 5 | [Day 1 Integration](session-5-integration.md) | Captain prompt run, one piece picked to ship Monday |

## Day 2 sessions (Sunday)

| # | Session | Outcome |
|---|---|---|
| 6 | [Performance Marketer](session-6-performance-marketer.md) | 10 ads + 6 Google headlines + 2 creative briefs (Default); 50+ ads (Power) |
| 7 | [Storefront + Marketplace](session-7-storefront-marketplace.md) | 2 PDPs rewritten + 5 CRO observations + 4 marketplace listings |
| 8 | [Ops + Retention](session-8-ops-retention.md) | 2 SOPs + 1 vendor template + 5 WhatsApp + 3 email + 2 segments |
| 9 | [Growth Analyst](session-9-growth-analyst.md) | Your first weekly Monday brief on your actual data |
| 10 | [Capstone](session-10-capstone.md) | 90-day operating roadmap + standing schedule recommended (or wired live on Max) |

## Add-on sessions

These sit outside the core 10. Run them when the brand needs the specific muscle. They read CLAUDE.md and the relevant Day-1 / Day-2 outputs the same way every other teammate does.

| # | Session | Outcome |
|---|---|---|
| 11 | [Influencer Scout](session-11-influencer-scout.md) | Shortlist of 5 creators from a Modash-shape pool + outreach + counter-offer scripts (Default); 10 creators + 4-week ladder + budget estimates (Power) |
| 12 | [Telegram Bot](session-telegram.md) | Your skills on your phone. DM the bot, it routes to Claude with full CLAUDE.md context. Lightweight demo with `/write-in-brand-voice`. |

---

## Before you start

Pre-work is at **thecrux.ai/prework-d2c**. If you have not done it yet, do it now. The founders who arrive with their `brand-brain/` folder ready (reviews, competitor notes, voice-DNA samples and the optional extras) walk out with reports based on real data. The founders who arrive cold spend Saturday morning catching up.

---

## During the workshop

- We work in **Claude Code in the terminal** for every live build. Power moves (skills, subagents, scheduled wake-ups, MCP debugging) are clearer there. **Antigravity** gets a 5-minute flip in Session 0 so you see the visual alternative. **Claude Desktop** gets a 2-minute mention. We use terminal for the rest.
- All ten teammates share one project folder. Brand Brain holds the global `CLAUDE.md`. Each teammate has their own definition you load when you switch context.
- You bring your data. We bring the system. By Sunday evening, the system runs without us.
- Two scopes everywhere: **DEFAULT** (sized for Pro plan, runs in the workshop slot) and **POWER** (Max plan or take-home). Pick at the start of every session.

## After the workshop

Re-run any teammate any week by opening their session file and following the steps. Each teammate compounds. Brand Brain gets richer. Market Analyst keeps tracking. Growth Analyst gets sharper as your data grows.

When you are ready to add more tools, open [`resources.md`](resources.md). It lists the MCPs and skills worth adding next, in priority order, with what to skip. Read it before you start installing servers you saw on a podcast.

Two follow-up sessions are scheduled at Week 2 and Week 4. Bring your three biggest blockers.

---

## Stuck?

Each session has its own troubleshooting at the bottom. Beyond that, raise hand: a TA pairs in within 60 seconds. The cohort goal is everyone shipping by Sunday evening.
