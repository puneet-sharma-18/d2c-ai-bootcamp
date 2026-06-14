# Hooks and Triggers — The Teaching

This document goes deeper than Module 8's BRIEF on the new primitive. Instructors read it before the live demo. Founders read it after the workshop when wiring hooks to their actual tools.

## The four trigger types

A trigger is the condition that fires an action. Four kinds, in order from easiest to hardest to wire:

### 1. Time-based triggers (cron / ScheduleWakeup)

The simplest. "Every Monday at 09:00, do X." No external system needed.

In Claude Code:
- The `ScheduleWakeup` tool defers a prompt to a future time
- `CronCreate` sets up a recurring schedule

Used in Module 9 to schedule the Growth Analyst's Monday brief.

### 2. Tool-call hooks (settings.json)

Fire when Claude Code itself does something. "When the Stop event fires, run X." "When a file is written to my-work/, do Y."

In Claude Code: `settings.json` (project level: `.claude/settings.json`, user level: `~/.claude/settings.json`).

Example shape:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "command",
            "command": "echo \"$(date): wrote $TOOL_FILE_PATH\" >> ~/.claude-files.log"
          }
        ]
      }
    ]
  }
}
```

Reads: when any Write tool call completes, append to a log file.

Used in Module 8's teaser. Used at Capstone for "when /captain runs, log the recommendation".

### 3. External webhook triggers (third-party systems)

Fire when something happens in Shopify, Gmail, support tool, payment processor, etc. These tools push an event to a URL you give them.

To wire: you need a webhook receiver. Three paths:
- **Composio MCP**: connects many SaaS tools and fires Claude actions on events. The cleanest path.
- **Make / Zapier**: classic no-code automation, can call a Claude Code prompt via API.
- **Custom server**: if you have a developer, a 30-line server that receives webhooks and triggers Claude.

Examples:
- Shopify webhook: "inventory updated" → fires when stock changes → Composio routes to Claude → Claude runs `/ops-manager` if inventory low
- Support webhook: Zoho or Freshdesk fires when a ticket arrives → Claude triages

These are take-home in this workshop. Documented here, wired by founders after.

### 4. Database / data-state triggers (polling)

When you want to fire on "60 days since last order" or "customer hit ₹10K LTV", there is no event to listen to. You poll the database periodically and fire when the condition flips.

Two paths:
- **Time-based poll**: ScheduleWakeup fires every Monday, Claude reads Shopify, finds customers crossing the threshold, queues the retention action. Cheap, easy.
- **Real-time stream**: needs a database trigger or change-data-capture stack. Heavy. Out of scope unless you have a data team.

Used in Module 10 to schedule the Retention Manager's daily check-in (which customers crossed thresholds yesterday).

## What hooks should NOT do

Five things to keep out of hook handlers:

1. **Send messages without founder approval.** Hook fires → drafts a WhatsApp message → notifies founder → founder hits send. Never auto-send.
2. **Touch money.** No hook fires a refund, a discount creation, a vendor payment. Money moves only through human approval.
3. **Modify production data without a draft.** Same rule as Module 7's PDP push: hooks write to draft, not live.
4. **Spam the founder.** A hook that fires too often becomes noise. Set thresholds. "Inventory below 20" not "every inventory change".
5. **Run for too long.** Hook handlers should finish in under 60 seconds. Long-running work goes via subagent dispatch, not in the hook itself.

## The Capstone wire-up

Module 10 (Capstone) wires four time-based triggers:

| When | What |
|---|---|
| Monday 09:00 | Run Growth Analyst weekly brief |
| Monday 09:30 | Run Market Analyst weekly digest |
| Daily 11:00 | Voice of Customer alarm sweep (high-severity tickets, high-emotion reviews) |
| Wednesday 14:00 | Brand Brain refresh (CLAUDE.md from the week's outputs) |

These are the universal hooks that work for every founder regardless of their tool stack. Tool-specific hooks (Shopify webhooks, retention triggers based on customer DB) are documented in the take-home pack and wired after the workshop.

## Compounding via hooks

The reason to invest in hooks at all: the system gets smarter every week.

Without hooks:
- Founder must remember to run /market-analyst every Monday
- Founder must remember to check VoC themes
- Founder must remember to look at returns rates
- Most weeks, the founder forgets at least 1 of these

With hooks:
- Monday brief lands automatically (Module 10 wires this)
- VoC daily sweep flags only the alarms (Module 10 wires this)
- Founder is freed from "remembering to check" and can spend the energy on "deciding what to do about what surfaced"

A founder who never wires hooks gets the same value as a founder who runs every skill manually every week. A founder who wires the time-based hooks at Capstone, then adds tool-specific hooks in week 2 office hours, is running a system that compounds while they sleep.

## A simple way to start

Do not try to wire all four trigger types in week 1. Order:

1. **Week 1 (after workshop)**: nothing. Run skills manually. Build the habit.
2. **Week 2**: wire the Monday morning brief. ScheduleWakeup is the easiest entry point.
3. **Week 3**: wire one tool-specific hook (Shopify low-inventory webhook is the highest-impact one). Use Composio or Make.
4. **Week 4**: wire one customer-DB trigger (60-day win-back). Time-based polling is simpler than real-time streaming.
5. **Month 2**: review what fired vs what was useful. Disable the noisy hooks. Add the missing one.

## Reading further

- Module 9: scheduled wake-ups for the Growth Analyst weekly brief
- Module 10 (Capstone): standing schedule wired across all 10 teammates
- Composio CLI documentation for tool-specific webhooks
- Claude Code settings.json reference for tool-call hooks
