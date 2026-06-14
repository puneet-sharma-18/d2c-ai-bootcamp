[← Back to Student Handbook](student-handbook.md)

---

# Session 8: Ops + Retention

**Skill unlocked:** Hooks and triggers. Skills can fire automatically when an event happens, not only when you remember to run them. Today we set the templates; Sessions 9 and 10 wire the schedules.

---

## What You'll Have After This Session

DEFAULT scope:

1. 2 SOPs for the most-needed operational gaps (based on your VoC support-ticket clusters)
2. 1 vendor email template for your most-used vendor communication moment
3. 5 WhatsApp retention templates for the top 5 retention moments
4. 3 email templates for lifecycle stages
5. 2 customer segments with definitions

POWER scope (Max plan or take-home):
- 5 SOPs + full Vendor Kit + Returns analysis + Escalation Playbook + 10+ WhatsApp templates + 6 email lifecycle flows + full RFM segmentation

---

## Before You Start

You need:
- CLAUDE.md saved
- Latest VoC report (ideally with support-ticket source split, from MCP-fed Session 3)
- Shopify MCP connected (helps Ops Manager pull return rates and inventory)
- A WhatsApp Business platform already running (WATI / Interakt / Gallabox / Twilio). Without one, you get the templates but cannot ship them yet.

---

## Step 1: The trigger framing (5 min)

Sessions 1 to 7 have been founder-initiated: you type `/skill-name` or spawn a subagent. That is manual mode.

The advanced mode is to wire some skills to fire automatically when something changes:

```
EVENT          TRIGGER                              ACTION
-----          -------                              ------
Shopify        Inventory of SKU X drops below 20    Run /ops-manager → stockout SOP
                                                    Alert founder on Telegram
Calendar       Every Monday at 09:00                Run /growth-analyst weekly brief
                                                    Send to founder's email
Customer       60 days since last order             Run /retention-manager → win-back
DB                                                  Queue WhatsApp draft for founder review
Support        Ticket count for "wrong size"        Run /ops-manager → quality SOP
                spikes 3x in 7 days                  Alert ops team
```

These are hooks. Today we write the templates that fire when triggers hit. Session 9 schedules the simplest trigger (time). Session 10 wires the standing schedule across all 10 teammates.

Detailed teaching: `references/module-8-ops-retention/hooks-and-triggers.md`.

---

## Step 2: Run Ops Manager (DEFAULT) (~10 min)

In Claude:

```
/ops-manager
```

Skill autoloads, asks scope. Type `default`.

The skill picks 2 SOPs based on:
- Your VoC support-ticket clusters (if "where is my order" is the top cluster, the Stockout SOP is in)
- Your Shopify return rate per SKU (if any SKU is over 8% return rate, the Returns SOP is in)
- Your current pain (it asks if not obvious from data)

Plus 1 vendor email template — the one you use most often given your current pain.

Confirm picks. The skill writes:

```
my-work/ops-manager/sops/<sop-1>.md
my-work/ops-manager/sops/<sop-2>.md
my-work/ops-manager/vendor-kit/<template-1>.md
my-work/ops-manager/<today>-index.md
```

Each SOP has: trigger, 5-9 step playbook, decision points, escalation, done definition. Each vendor template has: subject lines, body with placeholders, what to attach, what to do if no reply.

Reply ✅ when saved.

---

## Step 3: Run Retention Manager (DEFAULT) (~10 min)

In Claude:

```
/retention-manager
```

Skill autoloads, asks scope. Type `default`.

The skill produces:

| Output | Count | Where |
|---|---|---|
| WhatsApp templates | 5 | `my-work/retention-manager/whatsapp/` |
| Email templates | 3 | `my-work/retention-manager/email/` |
| Customer segments | 2 | `my-work/retention-manager/segments/` |

The 5 canonical retention moments DEFAULT covers:
1. Order confirmation
2. Delivery experience check-in (3 days post-delivery)
3. Replenishment prompt (timed to your SKU's consumption window)
4. Win-back (60 days no order, was a 2+ order customer)
5. First-time-to-second-purchase nudge (21 days after first order)

The 2 DEFAULT segments:
1. First-time buyers (last 90 days)
2. Repeat buyers (2 to 5 orders)

Each template has: trigger, segment, tone (from CLAUDE.md), allowed personalisation tokens, body in your voice, CTA, when NOT to send, compliance notes.

Reply ✅ when saved.

---

## Step 4: The two contrasts (5 min)

### Contrast 1: WhatsApp vs email voice

Open your WhatsApp post-purchase template and your email post-purchase template. Same customer, same moment. They read differently:
- WhatsApp is shorter, conversational, 1 CTA, no signoff
- Email has space for the founder voice paragraph and a "if anything goes wrong, reply" line
- Reading age can be the same; the SHAPE of the message differs

### Contrast 2: SOP vs marketing copy

Open one of your SOPs and your Day-1 Content Lead Instagram caption for the same product. They read very differently:
- SOP is internal ops documentation: trigger, steps, decision points, done definition
- Caption is external: hook, story, CTA
- Same brand voice runs through both, but the structure serves the audience

The skills know which audience they are writing for. You write one set of copy and paste it everywhere = the conversion gap and the ops gap both.

---

## Step 5: The hook teaser (5 min, watch the instructor)

The instructor shows ONE live hook setup on their `.claude/settings.json`:

```json
{
  "hooks": {
    "Stop": [
      {
        "matcher": "*",
        "hooks": [
          {"type": "command", "command": "echo 'Session ended at $(date)' >> ~/.claude-sessions.log"}
        ]
      }
    ]
  }
}
```

A trivial example, but the same shape works for: when /ops-manager runs, send me a Telegram message; when a file is written to my-work/, summarise it.

Session 10 (Capstone) wires the meaningful hooks. This is the teaser.

---

## What You Just Built

Two real operational documentation sets:
- SOPs that are trigger-explicit (not "stockout" but "inventory drops below 20 units AND last 30-day order count > 50")
- Retention templates with explicit segment + trigger + compliance per template
- Customer segments your retention tool can use as targeting rules

You also saw the trigger framing. Skills get more useful when they fire on their own. Today is the templates; Session 10 wires the schedule.

---

## What's Next

Session 9 builds the Growth Analyst — your weekly Monday brief. Plus the new primitive: scheduled wake-ups. The Monday brief lands automatically every Monday at 09:00 because Claude Code wakes itself up.

[Continue to Session 9: Growth Analyst →](session-9-growth-analyst.md)

---

## If You Get Stuck

| Symptom | Fix |
|---|---|
| SOP reads generic | VoC support tickets thin or paste-only. Re-run after MCP-fed VoC has more data. |
| WhatsApp template sounds AI | CLAUDE.md voice rules section 7 is thin. Add 5 phrases you actually use on WhatsApp, re-run. |
| Compliance flags on every retention template | Regulated category. The flags ARE the value. Read them as a legal-review checklist. |
| You do not have a WhatsApp Business platform | Take-home: WATI / Interakt / Gallabox starter plan, ~₹2K/month. The templates are ready when you sign up. |
| Returns analysis empty | Shopify return reasons not populated, OR Shopify MCP not connected. Skip in DEFAULT. |
| Segment SQL too complex for your tool | Skill produces both natural-language definition AND SQL. Use whichever your tool accepts. |

For anything not on this list, raise hand in the workshop chat.
