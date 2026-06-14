# The Standing Schedule

The 4 canonical scheduled wake-ups that turn the system into a Monday-morning operating cadence. Paste these into the Capstone POWER run, or set them up yourself in week 2.

Every wake-up below assumes the founder's timezone is IST. Adjust for other timezones via the `TZ=` prefix or the cron entry's timezone setting.

## 1. Monday 09:00 — Growth Analyst weekly brief

```
CronCreate(
  schedule: "0 9 * * 1",
  timezone: "Asia/Kolkata",
  prompt: "Run /growth-analyst DEFAULT for this brand. Save the brief to
my-work/growth-analyst/<today>-brief.md. Then use the Gmail MCP to draft
an email to <founder-email> with the headline, the one alarm, the
recommended action, and a link to the full brief file. Send the draft
(do NOT save as draft only). Subject line: 'Monday brief - <Brand> -
<today>'.",
  reason: "weekly Monday brief"
)
```

Optional: replace Gmail with Telegram delivery if the founder prefers Telegram.

## 2. Monday 09:30 — Market Analyst weekly digest

```
CronCreate(
  schedule: "30 9 * * 1",
  timezone: "Asia/Kolkata",
  prompt: "Run /market-analyst for the existing 3-5 competitors. Save to
my-work/market-analyst/<today>-intel-report.md. Compare against the most
recent prior report. Send a 3-line digest to the same delivery channel
as the Monday brief, covering only meaningful changes (pricing moves,
new ads, content shifts, new SKU launches). If nothing notable changed,
send 'no changes worth flagging this week'. Subject: 'Market digest -
<Brand> - <today>'.",
  reason: "weekly competitor digest"
)
```

## 3. Daily 11:00 — Voice of Customer alarm sweep

```
CronCreate(
  schedule: "0 11 * * *",
  timezone: "Asia/Kolkata",
  prompt: "Run /voice-of-customer in alarm-sweep mode. Read tickets and
reviews from last 24 hours via the Drive and Gmail MCPs. Save to
my-work/voice-of-customer/<today>-sweep.md. Surface ONLY: high-severity
tickets (containing 'refund', 'wrong', 'broken', 'never received', or
similar), high-emotion negative reviews (1-2 stars with detailed
complaint), mentions of regulators (FSSAI, CDSCO, Ayush) or specific
named competitors. If nothing crossed the alarm threshold, send a
one-line message saying so. Otherwise send the full alarm list to the
delivery channel immediately.",
  reason: "daily VoC alarm sweep"
)
```

## 4. Wednesday 14:00 — Brand Brain refresh

```
CronCreate(
  schedule: "0 14 * * 3",
  timezone: "Asia/Kolkata",
  prompt: "Read the index files in my-work/ from this week. Compare
facts in those indexes against CLAUDE.md (brand basics, products,
customer, competitors, voice rules). If any teammate output names a
fact that does NOT match CLAUDE.md, propose an edit. Do NOT write the
edit; draft it as a unified diff and save to
my-work/brand-brain/<today>-proposed-edit.diff. Send a notification to
the delivery channel: 'CLAUDE.md edit proposed: <one-line summary>.
Review and apply at <file-path>'. If no drift detected, send: 'CLAUDE.md
in sync this week'.",
  reason: "weekly CLAUDE.md drift check"
)
```

## After scheduling: confirm and verify

After the 4 `CronCreate` calls, run:

```
CronList()
```

Confirm 4 entries. Save the cron IDs to `my-work/captain/standing-schedule-config.md`:

```markdown
# Standing Schedule - Activated <date>

| Cron ID | Schedule | Description |
|---|---|---|
| <id-1> | Mon 09:00 IST | Growth brief |
| <id-2> | Mon 09:30 IST | Market digest |
| <id-3> | Daily 11:00 IST | VoC alarm sweep |
| <id-4> | Wed 14:00 IST | CLAUDE.md drift check |
```

## Test fire before relying on the schedule

Before walking away from a freshly wired schedule, test ONE of the wake-ups with a 2-minute delay:

```
ScheduleWakeup(
  delaySeconds: 120,
  reason: "test the Monday brief wake-up",
  prompt: "<the same prompt as the cron above for Monday brief>"
)
```

Wait 2 minutes. Confirm:
- The brief landed at `my-work/growth-analyst/<today>-brief.md`
- The email or Telegram message arrived
- The format is right

If the test passes, the cron entries above will work the same way each week. If the test fails, the cron entries will fail the same way each week. Fix the failing pieces before relying on the schedule.

## Optional: 5th and 6th wake-ups

If the founder wants more, two additional canonical patterns:

### Monthly content calendar refresh

```
CronCreate(
  schedule: "0 10 1 * *",
  timezone: "Asia/Kolkata",
  prompt: "Spawn the Content Lead subagent in DEFAULT scope. Plan the
next 30-day calendar starting from the first of next month. Save to
my-work/content-lead/<today>-calendar.md and produce the index. Send a
one-line summary to the delivery channel.",
  reason: "monthly content calendar"
)
```

### Monthly Performance Marketer hypothesis grid

```
CronCreate(
  schedule: "0 11 1 * *",
  timezone: "Asia/Kolkata",
  prompt: "Spawn the Performance Marketer subagent in DEFAULT scope.
Run the 2 strongest angles for the brand based on this month's VoC and
Market Analyst. Save to my-work/performance-marketer/. Send the index's
Top 5 reads to the delivery channel.",
  reason: "monthly ad hypothesis grid"
)
```

## Deactivating the schedule

For vacation, illness or any reason the founder wants to pause:

```
CronList()
```

For each entry to pause:

```
CronDelete(<cron-id>)
```

Re-create from this file when the founder is ready to resume.

## What this schedule does NOT do

- Does NOT auto-publish anything. Every action that touches customers, vendors or money goes through founder approval.
- Does NOT replace the founder's calendar discipline. The schedule produces inputs; the founder still needs to read them and act.
- Does NOT compound forever without maintenance. The MCPs occasionally need re-auth, the prompts occasionally need refinement. Plan a 30-minute schedule audit every quarter.

## What this schedule does

Reduces the founder's "remembering to check" load to zero for the 4 most important operational rhythms. Frees the founder to spend Monday morning DECIDING instead of GATHERING.

That is the whole point.
