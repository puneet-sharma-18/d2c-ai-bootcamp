[← Back to Student Handbook](student-handbook.md)

---

# Session 10: Capstone

**Skill unlocked:** The Captain pattern + the standing schedule. A subagent that synthesises across all 10 teammates by reading INDEX files only, plus 4 canonical scheduled wake-ups that turn the system into a Monday-morning operating cadence.

This is the close of the workshop.

---

## What You'll Have After This Session

DEFAULT scope:

1. A 90-day operating roadmap personalised to your brand, in `my-work/captain/<today>-90-day-roadmap.md`
2. A one-page Captain summary
3. The standing schedule recommended (4 canonical wake-ups, ready to wire take-home)
4. A clear Monday-morning action

POWER scope (Max plan, with TA support if needed):
- Same outputs
- 4 wake-ups wired live via cron
- Delivery configured (email or Telegram)
- Test fire of one wake-up before walking away

---

## Before You Start

You need outputs from all 10 teammates in `my-work/`:

```
my-work/market-analyst/<date>-intel-report.md
my-work/voice-of-customer/<date>-voc-report.md
my-work/content-lead/<date>-index.md
my-work/performance-marketer/<date>-index.md
my-work/storefront-specialist/<date>-index.md
my-work/marketplace-editor/<date>-index.md
my-work/ops-manager/<date>-index.md
my-work/retention-manager/<date>-index.md
my-work/growth-analyst/<date>-brief.md
plus CLAUDE.md
```

Most of you will have 8 to 10 of these. Founders missing 2+ get pushed to Day-3 office hours; the Captain still produces a useful roadmap with the available indexes and flags the gaps.

---

## Step 1: State of the chain (5 min)

In your terminal:

```bash
ls -la my-work/*/
```

Visual confirmation of which teammates have produced output. Count what you have. Reply ✅ in the workshop chat with how many teammates show output.

If you are missing 3+, name the gaps aloud. We close them in office hours; the Capstone runs anyway.

---

## Step 2: Run the Captain (DEFAULT) (~5 min)

Scope and wire-up choices live in the spawn prompt. The subagent runs in its own context and cannot pause to ask you mid-run, so if you omit scope it falls back to DEFAULT.

In Claude:

```
Spawn the Captain subagent with SCOPE=default.
```

To run POWER (take-home, after the workshop), include the delivery channel for the wake-ups:

```
Spawn the Captain subagent with SCOPE=power and DELIVERY=email.
```

`DELIVERY` can be `email`, `telegram` or `both`. Optional extras: `MONDAY_TIME=09:00` (default), `TIMEZONE=IST` (default). If you run POWER without DELIVERY, the Captain produces the cron commands as a manual checklist instead of wiring them live, so nothing schedules without your explicit choice of channel.

The subagent:
1. Reads CLAUDE.md
2. Reads ONLY the index files for all 10 teammates (never the raw outputs — this is the load-bearing rule that keeps the Captain light enough to run weekly)
3. Builds a state-of-the-chain table (which teammates are fresh, which are stale)
4. Produces the 90-day operating roadmap
5. Produces the one-page summary
6. Recommends the standing schedule

Outputs land in:

```
my-work/captain/<today>-90-day-roadmap.md
my-work/captain/<today>-summary.md
```

Reply ✅ when both files are saved.

---

## Step 3: Read the roadmap (10 min)

Open `my-work/captain/<today>-90-day-roadmap.md`. Read in this order:

### Read 1: The brand in one paragraph

Founder voice from CLAUDE.md, picked up by the Captain. Should sound like you. If it does not, your CLAUDE.md drifted; note for week-2 office hours.

### Read 2: The state of the chain right now

Names what is strong and what is thin across the 10 teammates. Honest about where data quality is high vs thin. This shapes how much weight to put on the roadmap.

### Read 3: Week 1 — what ships this week

3 to 5 specific items, each with:
- Action (specific, not "improve X")
- Owner teammate (which of your 10 runs it)
- Expected outcome (measurable)
- Risk if it does not happen

This is the most important section. Pick ONE Week 1 item. The one with highest impact / lowest effort. Plan to ship it Monday.

### Read 4: Weeks 2 to 4

Lighter than Week 1. Items get fuzzier the further out you read. That is correct; the world will change.

### Read 5: Months 2 and 3

Three priorities each. These are directional, not specific. Re-run the roadmap quarterly to refresh.

### Read 6: The cross-cutting recommendation for this week

ONE specific cross-teammate action that no single teammate would have surfaced alone. Cites 3+ teammates' outputs that justify it.

Example shape: "VoC theme #2 is rising. Market Analyst flags competitors have no SKU here. Performance Marketer should ship a problem-solver angle ad, Content Lead should bias next week's calendar, Storefront Specialist should rewrite the related PDP. This is a 3-teammate move; no single teammate would have proposed it."

This is what the Captain is for. The synthesis no individual teammate produces.

### Read 7: What the Captain did not synthesise (gaps)

Honest section. Stale teammate outputs, questions that need raw data the indexes do not summarise, strategic questions outside scope.

---

## Step 4: The standing schedule

Open `references/module-10-capstone/standing-schedule.md`. The 4 canonical wake-ups:

| When | Who | What |
|---|---|---|
| Mon 09:00 | Growth Analyst | Weekly brief lands in your email or Telegram |
| Mon 09:30 | Market Analyst | Weekly competitor digest |
| Daily 11:00 | Voice of Customer | Daily alarm sweep |
| Wed 14:00 | Brand Brain | Refresh CLAUDE.md from the week's outputs |

These are the universal wake-ups that work for every founder regardless of tool stack.

**If you are on Pro plan**: Take this home. The wire-up is a 5-minute task; the file has ready-to-paste cron entries. Do it Monday morning before your first Monday brief lands.

**If you are on Max plan and want it wired live now**: Raise hand. A TA pairs with you in the last 15 minutes of this slot. Wire at least the Monday brief and the daily VoC sweep; the other two can be take-home.

---

## Step 5: The three Capstone hand-counts (3 min)

Three questions. Take them seriously.

1. **Does my CLAUDE.md voice rules section feel right?** Should be yes for most. If no, that is the file to sharpen first thing next week.

2. **Did the Captain's cross-cutting recommendation surprise me (i.e. I did not already know this synthesis)?** This is the test of the workshop. If yes, the chain is working. If no, your data was thin and the Captain could not surprise. Re-run after deepening 2 specific teammates next week.

3. **Can I name the ONE thing I will do Monday morning?** Should be yes. If no, the roadmap did not land yet. Pair with a TA before you leave.

---

## Step 6: Close (1 min)

The workshop's close, one line:

> "You did not finish a course this weekend. You hired a team. They report to work Monday morning. The first brief lands at 09:00 IST. Read it on the metro. Decide what to do. Reply in week-2 office hours with what shipped."

That is it. Step away. Eat something.

---

## What You Just Built

A Command Center.

Friday before the workshop you opened: Shopify dashboard, Meta Ads Manager, Amazon Seller Central, support inbox, WhatsApp.

Monday after the workshop you open: your email or Telegram, where the Monday brief has landed. The brief tells you the one number that needs your attention this week. Daily at 11:00, the VoC sweep flags any rising customer issues. Wednesday afternoon, Brand Brain proposes any CLAUDE.md edits the week's data implies.

You decide what to do about what surfaced. The system does the surfacing.

---

## What's Next

You are done with the workshop. Two follow-up office hours scheduled at week 2 and week 4. Bring your three biggest blockers.

In week 1, do not optimise. Do not re-run every teammate. Pick the one Week 1 item from your roadmap, ship it, measure for 7 days. Compounding starts in week 2.

For weekly cross-cutting questions ("should we launch SKU X this week?", "should we match the competitor's price drop?"), use the Captain prompt at `references/module-10-capstone/captain-prompt.md`. The Captain is your Sunday-evening synthesis tool.

For quarterly roadmap refresh, re-run the prompt at `references/module-10-capstone/90-day-roadmap-prompt.md`.

For everything else: open the relevant teammate's session file, follow the steps. They are yours forever.

When a teammate starts asking for data you cannot give it (Calendar, Slack, Notion, Zoho, Canva), open [`resources.md`](resources.md). It lists the MCPs and skills worth adding next, in priority order, with what to skip. The rule of thumb: install the next tool the day a teammate visibly cannot do its job without it.

---

## If You Get Stuck

| Symptom | Fix |
|---|---|
| Captain refuses with "missing inputs" | More than 5 teammates have no output. Run the missing teammates in DEFAULT scope quickly OR run Captain anyway with the gaps explicitly noted. |
| Captain output too generic | Indexes are thin (most ran DEFAULT, sample sizes small). Re-run after week 2 when more data has accumulated. |
| Captain reads raw outputs by accident | Re-run with explicit "read indexes only, never piece files or SOP files". |
| Cannot decide on a Monday action | Roadmap has too many Week 1 items. Pick the one with highest impact / lowest effort. Save the rest for Week 2. |
| Schedule wake-up not firing on Max | Cron entry not created OR Claude Code not running. List crons via `CronList`. Verify entry. Confirm Claude Code is running on your laptop at fire time. |
| Email delivery from wake-up fails | Gmail MCP not connected, or scope insufficient. Re-auth Gmail with `gmail.compose` scope. |

For anything not on this list, raise hand in the workshop chat.
