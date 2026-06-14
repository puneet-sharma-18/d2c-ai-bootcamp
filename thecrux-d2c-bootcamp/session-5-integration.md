[← Back to Student Handbook](student-handbook.md)

---

# Session 5: Day 1 Integration

**Skill unlocked:** The captain pattern. One prompt that reads everything you built today across all four primitives and tells you ONE specific piece to ship Monday morning, with the chain of reasoning that justifies it.

---

## What You'll Have After This Session

1. The Day-1 captain output: one specific Monday-morning recommendation with sources cited across CLAUDE.md, Market Analyst, VoC and Content Lead
2. A clear sense of which one piece to ship next week
3. The mental model for how the four primitives work as one system

This is the close of Day 1. Short, sharp. By the end you should be able to point at the file you will ship next week.

---

## Before You Start

You need everything from Sessions 1 to 4:
- CLAUDE.md saved
- A Market Analyst report
- A VoC report (paste-in or MCP-fed)
- A Content Lead index

If any of those are thin or missing, the captain output will reflect that. Honestly is the design.

---

## Step 1: The captain idea (2 min)

A "captain prompt" is a top-level prompt that synthesises across all the layers below it. It is not a new kind of object. It is a prompt you run in main context that:

- Reads CLAUDE.md (Session 1)
- Reads the latest Market Analyst report (Session 2)
- Reads the latest VoC report (Session 2 or 3)
- Reads the latest Content Lead index (Session 4)
- Synthesises one decision-grade recommendation

Without a captain prompt, you have 30+ files and no entry point on Monday morning. With a captain prompt, you have one question to ask every week: *what is the most important thing for me to ship?*

---

## Step 2: Run the captain (5 min)

Open `references/module-5-integration/captain-day-1.prompt.md`. Copy the prompt block (everything inside the triple backticks) and paste it into Claude.

Claude reads the four files and produces output in this exact shape:

```
## Ship Monday

**Piece**: <full path to a file in my-work/content-lead/pieces/ or marketplace/>

**Why this one** (4 lines, one source per line):
- From VoC: <theme name and frequency>
- From Market Analyst: <gap or observation this piece exploits>
- From CLAUDE.md: <which voice rule, anti-positioning beat or product positioning aligns>
- From Content Lead: <what makes this piece in particular the top read>

**What it costs to skip**:
<2 lines>

**What to edit before you ship**:
<list of placeholders, safety flags, lines needing founder input>

**The honest read**:
<2 to 3 lines on what this recommendation does NOT capture>
```

Wait for the output. Read it.

---

## Step 3: Read the chain (5 min)

Three reads, in order:

### Read 1: The chain

Look at the four "From" lines. Each one cites a file you saw built today. Can you trace each line back to its source file in 30 seconds? If yes, the system is wired correctly. If any line feels generic or unsourced, the corresponding input is thin.

### Read 2: The honest read

This is the most valuable section. The captain is asked to flag what it does not know. If it says "your VoC sample was 28 messages, themes are signals not patterns" — that is real. Re-run VoC after Session 3 with MCP-fed data and the captain's reads get sharper.

If it says "you, the founder, know things this system does not" — also real. Use the captain as a second opinion, not the verdict.

### Read 3: The piece itself

Open the file the captain pointed at. Read it once. Edit any line that does not sound like you. Fill any `{placeholder}`. Address any safety flag. Then queue it to ship next week.

If the piece is wrong (off-brand, factually incorrect, doesn't fit), the issue is rarely the Content Lead. The issue is upstream:

- Voice off → CLAUDE.md Section 7 needs work
- Fact wrong → CLAUDE.md Section 4 (Products) or Section 6 (Competitors)
- Theme irrelevant → VoC inputs were thin

Edit the upstream file, re-run Content Lead, re-run the captain. The system gets sharper every week.

---

## Step 4: The three close-of-day questions (3 min)

Ask yourself three questions honestly:

1. Did my CLAUDE.md voice test score 4 or 5?
2. Is at least one piece in my Content Lead output something I would actually post next week?
3. Did the captain output today tell me something I did not already know?

Question 3 is the test of Day 1. If the answer is no, your CLAUDE.md or VoC is too thin. Sharpen tomorrow morning before adding the new teammates. Sleep well.

---

## What You Just Built

A working chain. Four primitives, one synthesis. You can re-run this captain prompt any Sunday evening; it gives you Monday's pointer.

You also have proof that the system works. The morning's interview turned into an afternoon's specific Monday-morning recommendation, with the sources cited. That is the workshop's promise, delivered before dinner on Saturday.

---

## What's Next — Day 2

Day 2 hires the other 6 teammates:
- Performance Marketer (50+ ad variations + creative briefs)
- Storefront Specialist (PDPs + landing pages + CRO)
- Marketplace Editor (Amazon A+ + Flipkart, deeper than today's draft)
- Ops Manager (vendor kit + SOPs + WhatsApp templates)
- Retention Manager (email + WhatsApp flows)
- Growth Analyst (weekly Monday brief)

Plus the Capstone (Sun 16:30): the whole thing wired into one Command Center with a 90-day roadmap and a standing schedule that runs without you typing.

By Sunday evening, today's captain prompt becomes a captain that runs every Monday morning automatically. Day 2 makes Day 1 automatic.

_Day 2 (Sessions 6–10, plus the Influencer Scout add-on) continues in the full bootcamp._

---

## If You Get Stuck

| Symptom | Fix |
|---|---|
| Captain output is "ship your hero SKU's caption" | One input is thin. Trace which: it is almost always VoC sample size. |
| Captain recommends a piece flagged for safety | Re-run with explicit "exclude any piece with safety flags". |
| Captain conflicts with your instinct | Working as intended sometimes. Use the captain as a second opinion, not the verdict. Ask: "what would change in the chain to make the captain agree with my instinct next week?" |
| Captain refuses, says it cannot find files | Path mismatch (you ran sessions out of order, or your `my-work/` is empty). List `my-work/` and confirm files exist with today's date. |

For anything not on this list, raise hand.
