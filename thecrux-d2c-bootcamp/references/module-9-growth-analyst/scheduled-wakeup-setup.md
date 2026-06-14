# Scheduled Wake-Up Setup

This document covers the time-based hook primitive: how it works in Claude Code, when to use it, and how to wire each of the canonical D2C operational rhythms.

## What ScheduleWakeup actually does

`ScheduleWakeup` is a Claude Code tool that defers a prompt to a future time. When the time arrives, Claude Code wakes itself up, runs the prompt, and writes the output to wherever the prompt directs.

The shape:

```
ScheduleWakeup(
  delaySeconds: <integer, seconds from now>,
  reason: <short string for telemetry>,
  prompt: <the prompt to run when the wake-up fires>
)
```

For recurring wake-ups, use `CronCreate`:

```
CronCreate(
  schedule: <cron string, e.g. "0 9 * * 1" for every Monday 09:00>,
  prompt: <the prompt to run on each fire>
)
```

The cron string is standard 5-field cron: minute, hour, day-of-month, month, day-of-week.

## When to use scheduled wake-ups

The pattern fits when:
- The cadence is calendar-shaped (Monday morning, daily 11am, first of the month)
- The work is short (under a few minutes per fire)
- The output goes somewhere the founder will see it (file, email, Telegram)
- The work does not need approval to proceed (writes a draft, not a live action)

The pattern does NOT fit when:
- The trigger is event-shaped (use a webhook or settings.json hook instead)
- The work is long-running (use a subagent dispatched at fire-time, with the cron just kicking it off)
- The action affects production data (humans approve before it runs, even if scheduled)

## The 4 canonical D2C wake-ups

The Capstone (Module 10) wires these for every founder. Documenting here for take-home reference.

### 1. Monday 09:00 — Growth Analyst weekly brief

```
CronCreate(
  schedule: "0 9 * * 1",
  prompt: "Run /growth-analyst DEFAULT for this brand. Save the brief to
my-work/growth-analyst/. Then send the headline + one alarm + recommended
action as a 4-line summary to <delivery: email or Telegram>. Include a
link / file path to the full brief."
)
```

Why Monday 09:00: most D2C founders set their week on Monday morning. The brief lands before they sit down.

Why a 4-line summary as the message: the full brief is one page, but the WhatsApp / email surface should not show a one-page document. Founders skim the 4 lines, click into the full brief if the alarm warrants it.

### 2. Monday 09:30 — Market Analyst weekly digest

```
CronCreate(
  schedule: "30 9 * * 1",
  prompt: "Run /market-analyst for the existing 3-5 competitors. Save to
my-work/market-analyst/. Compare against the most recent prior report.
Send a 3-line digest of any meaningful changes (pricing moves, new ads,
content shifts) to <delivery>. Skip if nothing notable changed; just say
'no changes worth flagging'."
)
```

Why 30 minutes after the Growth Analyst: founder has read the alarm by now, can correlate the Market Analyst observations with the alarm.

Why "skip if nothing changed": noise discipline. Most weeks competitors do nothing newsworthy. A digest that says "no changes" is more useful than a fake-busy "here are 5 things they did last week".

### 3. Daily 11:00 — Voice of Customer alarm sweep

```
CronCreate(
  schedule: "0 11 * * *",
  prompt: "Run /voice-of-customer in alarm-sweep mode for new tickets and
reviews from last 24 hours. Save to my-work/voice-of-customer/<date>-sweep.md.
Surface ONLY: high-severity tickets, high-emotion negative reviews,
mentions of regulators or specific competitors. If nothing crossed the
alarm threshold, say so in one line. Otherwise send the alarms to
<delivery> immediately."
)
```

Why daily not weekly: customer issues that compound (a rising "wrong size" cluster) are caught earlier with daily sweeps. Weekly is too slow for ops alarms.

Why 11:00: most overnight tickets have arrived by then; founder has opened the day's work.

Why alarm-sweep mode (not full VoC): the daily sweep is for alarms only, not full theme synthesis. Full VoC re-runs weekly via the Monday brief's cross-teammate inputs.

### 4. Wednesday 14:00 — Brand Brain refresh

```
CronCreate(
  schedule: "0 14 * * 3",
  prompt: "Read this week's outputs in my-work/. If any teammate output
contains a fact about the brand, customer or competitors that does NOT
match CLAUDE.md, propose an edit to CLAUDE.md. Do NOT write the edit;
draft it as a diff for the founder to approve. Save the diff to
my-work/brand-brain/<date>-proposed-edit.diff."
)
```

Why Wednesday: by mid-week, Monday's brief and Tuesday's content runs have generated outputs. Wednesday is when CLAUDE.md drift is visible.

Why "do not write the edit": CLAUDE.md is the source of truth. Auto-editing it without founder approval is a bad pattern. The wake-up proposes; the founder reviews and applies.

## Wiring delivery

The wake-up writes a file. To deliver to email or Telegram, the prompt itself must call the delivery tool.

For email: use the Gmail MCP (connected in Module 3). The prompt ends with:
```
... then use the Gmail MCP to draft an email to <founder@brand.com> with the
4-line summary as the body and the file path as a clickable link. Send the
draft (not save).
```

For Telegram: use the Telegram channel skill if configured. The prompt ends with:
```
... then send the 4-line summary to the configured Telegram channel using
the Telegram skill.
```

For founders who want both: the prompt sends to both.

## Failure modes

| Mode | What happens | Mitigation |
|---|---|---|
| Wake-up does not fire | Claude Code not running, machine asleep, internet down | Use a server-side scheduler (Composio, GitHub Actions) for production; ScheduleWakeup is for the founder's laptop |
| Wake-up fires but produces empty output | MCP rate limit, data not yet available | Skill notes the gap. Wake-up logs the empty run. Next fire usually succeeds. |
| Wake-up fires while founder is asleep | Founder did not realise their laptop was awake at 09:00 | Confirm the laptop sleep behaviour. On macOS, `caffeinate` or "Power adapter -> Prevent sleep" while plugged in. |
| Multiple wake-ups stacking | Founder set up overlapping schedules accidentally | List wake-ups via `CronList`; remove duplicates with `CronDelete`. |
| Wake-up fires but founder is on holiday | Founder away, brief lands in empty inbox, founder returns to 14 unread briefs | Add a vacation mode: founder can disable a single cron with `CronDelete` for the duration, re-add on return. Power: a vacation cron that disables others. |

## How to test a wake-up before relying on it

Test with a short delay before scheduling weekly:

```
ScheduleWakeup(
  delaySeconds: 120,
  reason: "test the Monday brief wake-up",
  prompt: "<the same prompt you would schedule weekly>"
)
```

In 2 minutes, the wake-up fires. Check:
- Did the brief land in `my-work/growth-analyst/`?
- Did the email or Telegram message arrive?
- Was the format right?

Iterate on the prompt until the test fires cleanly. Then schedule the weekly cron with confidence.

## What this is not

- **Not a job scheduler in the production sense.** ScheduleWakeup runs while Claude Code is running. For production-grade scheduling (runs even when the founder's laptop is closed), use a server (GitHub Actions cron, AWS EventBridge, Composio's scheduler).
- **Not transactional.** If a wake-up half-completes (writes the brief but fails to send the email), the next fire does not "resume". Each fire is independent.
- **Not infinite.** Cron entries persist across sessions but if the founder reinstalls Claude Code or moves machines, the cron entries are gone. Re-create from the Capstone setup if needed.

## Take-home setup

After the workshop, founders should:

1. Test each of the 4 canonical wake-ups with a 2-minute delay (Step above)
2. Schedule the weekly + daily versions with confidence
3. After 2 weeks, review what fired vs what was useful
4. Disable noisy wake-ups, sharpen useful ones

A good operating cadence emerges within 4 weeks.
