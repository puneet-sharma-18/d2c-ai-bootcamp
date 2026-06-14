[← Back to Student Handbook](student-handbook.md)

---

# Session 9: Growth Analyst

**New skill this session:** Scheduled wake-ups. Time-based hooks that fire automatically. Plus your weekly Growth Dashboard, built as three artifacts: a markdown brief, a JSON data sidecar and a self-contained HTML dashboard. The brief is your Monday read. The dashboard is built ONCE and lives forever; every week after, only the JSON changes and the page refreshes the numbers on its own. Lands every Monday at 09:00 with the single number that needs your attention this week.

---

## What You'll Have After This Session

DEFAULT scope. Four files in `my-work/growth-analyst/`:

- `<today>-brief.md`. The weekly canonical brief. Headline, the one alarm, top 3 reads, numbers table, channels table, recommended action.
- `<today>-index.md`. Small pointer file other teammates cite when they need this week's numbers.
- `data/numbers.json`. Data sidecar. Same numbers as the brief, in machine-readable form. Archive copy at `data/archive/<today>-numbers.json` so trend history survives.
- `dashboard.html`. Self-contained dashboard. Built ONCE on the first run, then it stays put. Every Monday after, only the JSON and the brief refresh. You open the same HTML file, hit refresh in the browser, the new numbers paint in.

Plus the brief shape internalised, and an understanding of how scheduled wake-ups work.

POWER scope (take-home for everyone, Max plan recommended):
- Same artifact set
- Scheduled wake-up wired live. Every Monday at 09:00 the brief and `data/numbers.json` regenerate on their own. `dashboard.html` is unchanged. A short ping (headline, one alarm, link to the HTML) lands in your email or Telegram.

Everyone runs DEFAULT in this slot. POWER is the take-home run, once you have a quiet evening to wire the schedule for real. Session 10's Capstone wires the standing schedule for everyone (including Pro plan), so even without running POWER you walk out scheduled.

---

## The three-stage shape

Before we run anything, name the shape. The skill moves through three stages, and the artifact set above maps cleanly onto them.

1. **Collect.** Read `CLAUDE.md`, `brand-brain/unit-economics.md`, the previous teammate indexes from `my-work/`, and pull live numbers from Shopify, Meta and Google MCPs if they are connected. If a primary source is missing, fall back to the matching file in `examples/` (more on this below).
2. **Analyze.** Pick the metric set by revenue stage, compute the one alarm, write `<today>-brief.md`, write `data/numbers.json` from the same pass and emit `<today>-index.md` as a pointer.
3. **Render.** On the FIRST RUN only, build `dashboard.html` against `design.md` at the repo root. On every subsequent run, the HTML is left alone. The page reads `data/numbers.json` on load, so refreshing the tab is enough to see this week's numbers.

This separation matters. The truth lives in `data/numbers.json` and the brief. The HTML is just a view. You can rebuild the view any time you want without touching the data, and you can refresh the data every week without touching the view.

---

## Before You Start

You need:
- CLAUDE.md saved. Section 2 should state your revenue stage (0-1Cr, 1-10Cr, 10-50Cr, 50-100Cr, 100Cr+) and, if you sell offline, the offline revenue %.
- `brand-brain/unit-economics.md` from pre-work. This is the PRIMARY source for CAC, LTV, AOV, gross margin and channel mix. The skill trusts your numbers before reaching for live data.
- Shopify MCP connected (Session 3), used as enrichment on top of your unit-economics file.
- Latest VoC and Market Analyst reports (used as cross-teammate inputs in the brief).
- `design.md` at the repo root. Don't move it, don't delete it. The dashboard build reads it once on the first run.

If any of those are missing, the skill still runs. See the sample-data fallback below.

If you have Meta Ads or Google Ads MCPs connected, the brief gets richer. Most founders skip these in the workshop and add them take-home. The brief explicitly notes the gap.

If you sell on Amazon, Flipkart, Tata Cliq or any marketplace without an MCP, paste your CSV export into the chat after the skill spawns. The agent will merge marketplace revenue into the per-channel table. Otherwise the brief shows D2C only and notes the gap. For 50Cr+ brands this matters, marketplace is 30 to 50% of revenue. Auto-ingestion build is sketched at the bottom under Power-ups.

### Sample-data fallback (a first-class path)

Most founders reach this session with at least one input thin. The skill handles it on purpose. It does NOT bail out and it does NOT invent numbers silently.

- **`brand-brain/unit-economics.md` missing or empty.** Reads `examples/little-lab/brand-brain/unit-economics.md` (or `examples/<your-brand-slug>/brand-brain/unit-economics.md` if a slug-matched folder exists).
- **Shopify, Meta Ads or Google Ads MCP not connected.** Reads `examples/little-lab/sample-inputs/shopify-orders-28d.csv`, `meta-ads-spend.csv` and `google-ads-spend.csv`. Each missing MCP gets added to a `missing` list in `numbers.json` so the dashboard can render a "not connected" badge per channel.
- **Both gone.** Brief still renders the full shape. Every number reads from sample data.

The brief's headline opens with a sample-data disclosure: "This dashboard is built from sample data because X, Y, Z were missing. Replace with your own by [one short instruction per gap]." The dashboard also paints a prominent banner above the hero with the same reasons. You see the full shape end to end, plus exactly what is missing and how to plug it in. The brief is either honestly running on your data, or it is loudly running on sample data.

---

## design.md is the visual source of truth

The repo has `design.md` at the root. That is your design system: the single source of truth for colors, type, spacing, components and motion. The dashboard build prompt reads it in full on the first run and applies it everywhere. The prompt does not name a palette, repeat hex codes or mention the system by name. If tomorrow you swap `design.md` for a different system and re-run the build prompt, the same dashboard renders in a different visual language. The data does not move. The view re-paints.

For this session you do not edit `design.md`. Just know it is there and that your dashboard inherits from it.

---

## Step 1: The "one alarm" demo (8 min)

The brief shape changes with revenue stage. Three stage examples follow. Same skill, same one-alarm bar. Different metrics, different threshold rules.

### Example 1. Stage A. 0-1Cr (first 10 customers)

CAC is unreliable at this volume. The alarm reads from absolute counts and a single-cohort look.

```
## Headline
14 orders last week, 4 this week. Two of the four cited the same
shipping delay. First-time-to-repeat rate steady at 18% on a base of 22.

## The one alarm
**Orders dropped from 14 to 4** week on week. Two customers complained
about the same shipping delay (3-5 day promise, took 8). Not a CAC
problem. A fulfilment problem masquerading as an acquisition problem.

**Recommended action this week**: Call your 3PL today. Re-set the
shipping promise on the PDP to 5-8 days until you can hit 3-5
reliably. Re-run /voice-of-customer on Sunday to check if the
complaint theme drops.
```

Stage A logic: percentage moves on 4 vs 14 orders are noise. Absolute counts plus the VoC theme are the read.

### Example 2. Stage C. 100Cr+ omnichannel (65% offline)

Blended revenue can hide the actual move. The online vs offline split is mandatory in the brief.

```
## Headline
Total revenue up 2% week on week. Online down 11%, offline up 9%. The
blended number is the wrong number to read this week.

## The one alarm
**Online revenue moved down 11%** (₹{X} to ₹{Y}), while offline moved
up 9%. The blended +2% would have hidden it. The online drop sits
entirely in Tata Cliq, where the home page placement we held last
week rotated out. D2C site held flat.

**Recommended action this week**: Re-negotiate Tata Cliq placement
with your account manager today. Run /performance-marketer to push
Meta spend up by 15% on the SKUs that lost shelf at Tata Cliq, to
recover the channel mix.
```

Stage C logic: blended +2% would have read as "steady". The online/offline split exposes the real move.

### Example 3. Stage B. 50Cr+ mature ad spend

Standard 7-metric brief. The threshold rules fire on percentage moves.

```
## Headline
Revenue flat, but blended CAC up 22%. The miss is in Meta, not
retention.

## The one alarm
**Blended CAC** moved up 22%: from ₹{420} to ₹{510}.

Spend stayed flat, conversions fell. The fall correlates with the
"100% safe" ad set we shipped Tuesday, which Meta flagged for review
and served less. Founder's unit-economics.md sets target CAC at ₹{440}
so this is materially over.

**Recommended action this week**: Pause the flagged ad set today.
Re-run /performance-marketer to draft 3 replacement variations using
the social-proof angle (which converted at the previous CAC).
Expected to bring blended CAC back under ₹{450} by next Monday.
```

One brief. One number. One action. That is the bar at every stage.

---

## Step 2: Run Growth Analyst (DEFAULT) (~3 min)

In Claude:

```
/growth-analyst
```

Skill autoloads, asks scope. Type `default`.

The skill works through the three stages from earlier in this session.

**Collect.** Reads `CLAUDE.md`, `brand-brain/unit-economics.md`, `brand-brain/positioning.md`, Shopify/Meta/Google MCPs and the latest teammate indexes from `my-work/`. Any missing primary source falls back to the equivalent file under `examples/little-lab/` and gets flagged in the brief.

**Analyze.** Picks the metric set by revenue stage:
- **0-1Cr:** orders 7d, orders 28d, first-time-to-repeat rate, top complaint theme, top channel, AOV. No CAC alarm (volume too thin).
- **1-50Cr:** standard 7 (revenue, trend WoW, trend vs 4w avg, AOV, CAC, repeat rate, ROAS by channel).
- **50Cr+:** standard 7 plus channel mix mandatory. If CLAUDE.md Section 2 has an offline %, online vs offline is split out.

Picks the ONE alarm using stage-aware thresholds:
- 0-1Cr: absolute counts, single-cohort reads, repeat complaint themes
- 1-50Cr: ±10% WoW, ±15% vs 4w avg or critical threshold cross (CAC > LTV, ROAS < 1, repeat < 15%)
- 50Cr+: above, plus mandatory channel-mix check (5pp move in any channel share, 3pp move in online vs offline)

Then writes the brief, `data/numbers.json`, the archive copy and the index pointer.

**Render.** First run only: the skill builds `dashboard.html` against `design.md`. Subsequent weeks skip this. The HTML reads `data/numbers.json` via fetch() on every page load, so refreshing the page shows the new week's numbers.

To force a rebuild (e.g. you edited `design.md` and want the dashboard to re-paint in the new system), delete `dashboard.html` and re-run.

---

## Step 3: Open your dashboard (5 min)

The dashboard fetches `data/numbers.json` from a relative path. Opening the HTML by double-clicking it gives you a `file://` URL and most browsers block fetch() over `file://`. You will see "Could not load data/numbers.json".

The fix is one line. Serve the folder over a local HTTP server.

```
cd my-work/growth-analyst
python3 -m http.server 8000
```

Open `http://localhost:8000/dashboard.html` in your browser. The page loads, the numbers paint in, the chart draws. Leave the terminal running for the rest of the session.

Read the page in order, top to bottom:

1. **Sample-data banner** (only if you ran on sample data). Names the missing inputs and the steps to replace them.
2. **Headline.** One sentence at the top of the page, state of the business this week.
3. **The one alarm.** Visually emphasised block. The metric, the magnitude, the two-line context, the recommended action.
4. **KPI tiles.** 4 tiles for Stage A, 6 for Stage B and C. Each tile shows this week, prior week, WoW delta.
5. **4-week trend chart.** One Chart.js line of the alarm metric. Visual confirmation of the direction.
6. **Top 3 reads.** Three observations beyond the alarm, each citing a contributing teammate.
7. **Numbers table.** The 7 metrics, this week vs prior vs 4-week avg.
8. **Per-channel table.** D2C, Amazon, Flipkart, Quick commerce, Meta, Google. Channels in the `missing` list show a "not connected" badge.
9. **Cross-teammate inputs.** Which other teammates' outputs shaped this dashboard, with file paths that resolve to clickable links.
10. **Gaps.** What the dashboard did NOT cover, with each metric and the founder-vs-live delta if any.

You should be able to name your "one number" out loud after looking at the page for 10 seconds. If you cannot, the dashboard has more than one alarm and the skill needs to compress.

---

## Step 4: The cross-teammate read (3 min)

Scroll to the "Cross-teammate inputs" section. This is what separates this dashboard from a Looker or Metabase board.

Look at it. Each line cites another teammate's output:
- A VoC theme that appeared in 20%+ of this week's tickets
- A competitor move flagged by Market Analyst as relevant to your alarm
- A Content Lead piece that shipped this week, if it correlates with a metric move
- An ad change from Performance Marketer, if it correlates with CAC

This is the chain made measurable. Each teammate did its job; the Growth Analyst weighs the impact. A Looker board shows numbers. This dashboard shows numbers and the cross-teammate work that produced them.

---

## Step 5: The scheduled wake-up demo (5 min, watch the instructor)

The instructor shows the wake-up wiring on their screen:

```
/growth-analyst with scope POWER
```

The skill produces the same artifact set as DEFAULT, then asks:

> "Where should the Monday ping land?"

Pick email or Telegram. Confirm Monday 09:00 IST default time. Only the headline, the one alarm and a link to the dashboard HTML go in the message itself, so the ping stays short.

The skill calls `ScheduleWakeup` and `CronCreate`. The cron entry gets created. Next Monday at 09:00, this fires whether the founder is at their laptop or not. The skill regenerates the brief, refreshes `data/numbers.json`, archives the prior week's JSON and sends the ping. **It does NOT rebuild `dashboard.html`.** That file was built once and is left alone. You open the same URL, the page fetches the fresh JSON and paints the new numbers.

Detailed teaching: `references/module-9-growth-analyst/scheduled-wakeup-setup.md`. Brief format spec: `references/module-9-growth-analyst/monday-brief-spec.md`.

---

## Step 6: The Capstone hand-off (2 min)

Session 10 (Capstone, in 30 min) wires the standing schedule for everyone, including Pro plan founders. You walk out with:

1. The standing schedule for ALL teammates (Mon 09:00 brief, Mon 09:30 market digest, daily VoC sweep, Wed 14:00 CLAUDE.md refresh)
2. The Captain prompt that calls across all 10 teammates
3. The 90-day operating roadmap, personalised to your brand

Take a 5-minute stretch.

---

## What You Just Built

Your first Growth Dashboard on your actual data (or honest sample data, with the gaps named). The brief sits at the top of the page; that is the design. The dashboard is a focusing tool first, a visual surface second.

Compare with what you used to do on a Monday morning: Shopify dashboard in one tab, Meta Ads Manager in another, Amazon Seller Central in a third, the support inbox in a fourth, WhatsApp on your phone. The Growth Dashboard collapses all of that into one HTML file with the brief at the top. The cross-teammate citations are why this works.

The architecture is the lesson too. Data and view are separated. `data/numbers.json` carries the truth, regenerated every Monday. `dashboard.html` is the view, built once, refreshed by reloading the page. Edit `design.md` and re-run the build prompt, the data does not move. Re-run the analyze stage, the view re-paints on the next refresh.

You also saw the scheduled wake-up primitive. Time-based hooks are the simplest and most universal. Most operational rhythms are calendar-shaped (Monday brief, daily VoC sweep, monthly content calendar). Schedule them once, they run forever.

---

## What's Next

The Capstone. All 10 teammates wired into one Command Center. The 90-day operating roadmap personalised to your brand. The standing schedule recommended (or wired live if you are on Max). Day 2's close.

[Continue to Session 10: Capstone →](session-10-capstone.md)

---

## Power-ups

Optional add-ons that extend this skill beyond the workshop hour. None are needed for the live build.

### Marketplace CSV ingestion (post-workshop add-on)

**What this fixes.** Monday brief excludes Amazon, Flipkart, Tata Cliq when no marketplace MCP is connected. For brands where marketplace is 30 to 50% of revenue, the brief silently underrepresents the business and the alarm logic fires on the wrong base.

**Who it's for.** 50Cr+ brands with active marketplace presence and no SP-API or Flipkart Seller MCP yet. Amazon, Tata Cliq, Flipkart sellers especially.

**The build.** Step 1 of `growth-analyst/SKILL.md` adds reads for `brand-brain/marketplace-revenue.csv` (date, channel, revenue, orders, ad_spend) and `brand-brain/meta-ads-90d.csv`. Normalizer maps platform-specific CSV headers to the schema (Amazon Seller Central, Flipkart Seller Hub and Tata Cliq each ship different columns). Merged into the per-channel table in the analyze stage. Founder exports CSV weekly, drops in folder, brief picks it up automatically.

**How to know it worked.** Marketplace channel rows appear in the per-channel table with non-zero revenue. Total revenue in the brief matches the founder's mental number within 5%.

**Failure modes.** Platforms update column names without notice and the normalizer breaks silently. Date ranges mismatch across platforms so the WoW comparison reads the wrong week. Currency mixing (Amazon US vs IN exports). Returns netting confusion (gross vs net revenue).

**Build time.** 30 to 45 minutes for the base. More as edge cases surface per platform.

---

## If You Get Stuck

| Symptom | Fix |
|---|---|
| Browser shows "Could not load data/numbers.json" | You opened `dashboard.html` by double-clicking and got a `file://` URL. fetch() is blocked over `file://`. Run `python3 -m http.server 8000` from `my-work/growth-analyst/` and open `http://localhost:8000/dashboard.html`. |
| Dashboard loads but every number is blank | `data/numbers.json` did not get written, or it has a schema mismatch with the HTML. Open the JSON file directly in the browser to confirm it is valid JSON. If valid, re-run the skill with: "regenerate data/numbers.json against the current schema in the SKILL.md". |
| Sample-data banner showing when you expected real data | Skill could not find `brand-brain/unit-economics.md` or your MCPs. Read the banner, plug the named gaps, re-run. The banner names exactly which inputs were missing. |
| `python3` command not found | Use `python -m http.server 8000` instead. On Windows, `py -m http.server 8000`. Any local HTTP server on the folder works. |
| Brief has many "no data" lines | Meta and Google MCPs not connected and no sample CSVs in your example folder. Either connect the MCPs or rely on the bundled `examples/little-lab/sample-inputs/` files. Note as a gap to plug take-home. |
| Alarm picks a vanity metric (total revenue, total followers) | Threshold logic off. Re-run with: "alarm should be on a metric tied to unit economics or repeat rate, not absolute revenue". |
| ScheduleWakeup not available in your Claude Code | Older version. Update Claude Code. Fall back to a calendar reminder plus manual run if update fails. |
| Brief is too long | Re-run with explicit "compress to one page; cut everything except headline, alarm, action, numbers table, channels table". |
| You are unfamiliar with CAC, ROAS, AOV | The brief defines each metric. Focus on the alarm and the action; the metric definitions are reference. |
| `brand-brain/unit-economics.md` is missing or empty | Skill falls back to `examples/little-lab/brand-brain/unit-economics.md` and flags the gap in the brief's headline. Take-home: fill in CAC, LTV, AOV, gross margin, channel mix using the pre-work template. |
| Dashboard re-rendered with the old design after you edited `design.md` | The skill skips the build when `dashboard.html` already exists. Delete the file and re-run; on the next run it rebuilds against the updated `design.md`. |
| Alarm reads a percentage move on a 0-1Cr brand with single-digit orders | Wrong threshold rules fired. Re-run with: "this is a 0-1Cr brand, use Stage A rules from the skill: absolute counts, no CAC alarm, single-cohort look". |
| Offline-heavy brand gets a blended trend that hides the move | CLAUDE.md Section 2 missing the offline %. Add the split (e.g. "65% offline retail, 35% online"). Re-run. Brief will then break out online vs offline. |

For anything not on this list, raise hand in the workshop chat.

---

## Appendix: Restyle the Dashboard and Add a Chatbot

Two optional upgrades you can run take-home. The first reskins the dashboard to a new design system. The second adds a natural-language chatbot that answers questions about your data with text and charts.

---

### A. Restyle the dashboard with a new design.md

The dashboard reads `design.md` at the repo root on first build. To restyle it, swap the file and rebuild.

**Step 1. Pick a design system.**

Browse https://getdesign.md for pre-built systems. Each one ships a `DESIGN.md` with colors, type, spacing, components and do's/don'ts. Some examples:

| System | Aesthetic | Command |
|---|---|---|
| Genesis | Editorial precision, indigo + white | `npx getdesign@latest add genesis` |
| Cohere | Enterprise AI, deep green + coral, flat | `npx getdesign@latest add cohere` |
| Linear | Minimal, purple accent, dark mode ready | `npx getdesign@latest add linear` |
| Stripe | Clean, blue-black, dense data tables | `npx getdesign@latest add stripe` |

Or bring your own `design.md` from any source.

**Step 2. Download and replace.**

```bash
# Download (creates a folder with the system name)
npx getdesign@latest add cohere

# Replace the repo root design.md
cp cohere/DESIGN.md ./design.md
```

**Step 3. Delete the old dashboard and rebuild.**

The skill skips the build when `dashboard.html` already exists. Delete it first:

```bash
rm my-work/growth-analyst/dashboard.html
```

Then in Claude:

```
Rebuild my-work/growth-analyst/dashboard.html using the updated design.md
at the repo root. Read design.md in full. Apply its colors, type scale,
spacing, radii, shadows and component patterns. The data file is at
my-work/growth-analyst/data/numbers.json. Every number renders from fetch(),
no inline data values.
```

Or re-run `/growth-analyst` with scope `default`. Since `dashboard.html` is gone, it rebuilds automatically.

**Step 4. Verify.**

```bash
cd my-work/growth-analyst && python3 -m http.server 8000
```

Open `http://localhost:8000/dashboard.html`. The same data, new visual language.

---

### B. Add a chatbot to the dashboard

The chatbot lets you ask natural-language questions about your data directly inside the dashboard. It sends your question plus the full dataset (numbers.json, the weekly brief, and all raw CSVs) to an LLM via OpenRouter. When a chart would help, the model returns a chart spec and the frontend renders it inline.

**What you need:**
- An OpenRouter API key (instructor will provide one for the workshop, or get your own at https://openrouter.ai/keys)
- Python 3 with `requests` and `python-dotenv` installed (`pip3 install requests python-dotenv`)

**Step 1. Ask Claude to add the chatbot.**

In Claude:

```
Add a chatbox to my-work/growth-analyst/dashboard.html. When I type a
natural language query it should answer my question with data and charts
where relevant, based on the dataset the dashboard is built on.

Use OpenRouter as the LLM provider. Create a server.py that:
- Serves the dashboard static files
- Has a /api/chat endpoint that proxies to OpenRouter
- Sends the full dataset (numbers.json, the brief, and all CSVs from
  examples/<brand>/sample-inputs/) as context with every query
- Uses the model anthropic/claude-sonnet-4

Create a .env file with a placeholder for OPENROUTER_API_KEY.
Style the chatbox to match design.md at the repo root.
```

Claude will produce:
- `my-work/growth-analyst/server.py` -- Python server with static files + `/api/chat` endpoint
- `.env` file with `OPENROUTER_API_KEY=sk-or-v1-your-key-here`
- Updated `dashboard.html` with a chat panel (floating button, message history, suggestion chips, inline chart rendering)

**Step 2. Add your OpenRouter API key.**

Edit `my-work/growth-analyst/.env`:

```
OPENROUTER_API_KEY=sk-or-v1-paste-your-real-key-here
```

The instructor will share a key during the session. For take-home use, create your own at https://openrouter.ai/keys.

**Step 3. Start the server.**

```bash
cd my-work/growth-analyst
python3 server.py
```

You should see:

```
Growth Dashboard running at http://localhost:8000/dashboard.html
Model: anthropic/claude-sonnet-4
API key: configured
```

**Step 4. Use the chatbot.**

Open `http://localhost:8000/dashboard.html`. Click the `?` button in the bottom-right corner. The chat panel opens with four starter suggestions:

- "Which Meta campaign should I pause?"
- "Revenue by channel this week"
- "CAC trend over 4 weeks"
- "Top SKU by orders"

Click one or type your own question. The model sees the full dataset on every call and can compute aggregations, compare channels, explain trends and return charts inline. Conversation history is preserved so you can ask follow-ups.

**Example questions that work well:**

```
What is my most profitable ad campaign?
Show me daily order trends for the last 28 days
Compare D2C vs Zomato revenue and AOV
If I pause META-004, what happens to blended CAC?
Which day of the week gets the most orders?
Break down Meta spend by campaign angle
What is my Google ads CAC vs Meta ads CAC?
```

**Step 5. Troubleshooting.**

| Symptom | Fix |
|---|---|
| "Set OPENROUTER_API_KEY in .env" error | Edit `.env` with your real key. Restart `server.py`. |
| "Could not reach the server" in chatbox | `server.py` is not running. Start it with `python3 server.py`. |
| Chat responds but no charts render | The model did not include a chart block. Rephrase with "show me a chart of..." to nudge it. |
| `ModuleNotFoundError: No module named 'dotenv'` | Run `pip3 install python-dotenv`. |
| OpenRouter API error 401 | API key is invalid or expired. Check `.env`. |
| OpenRouter API error 429 | Rate limited. Wait 30 seconds and try again. |
| Slow responses (>15 seconds) | Normal for the first call. Subsequent calls with conversation history may be slower due to the large context. |

---

### C. Combining both upgrades

You can restyle the dashboard first, then add the chatbot, or do them in either order. The chatbot styles are added to whatever design system the dashboard is using, and Claude will match them to the active `design.md` tokens.

If you restyle AFTER adding the chatbot, delete `dashboard.html` and ask Claude to rebuild it with the chatbot included:

```
Rebuild my-work/growth-analyst/dashboard.html using the updated design.md.
Keep the chatbox functionality that calls /api/chat on server.py. Style
everything to match the new design.md.
```
