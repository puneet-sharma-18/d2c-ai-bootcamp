# Captain (Day 1) — One Monday recommendation

This is the prompt you run at the close of Day 1, and any Monday morning after. It synthesises across the four primitives you built today (CLAUDE.md, Skills, MCPs, Content Lead subagent) and gives you one specific piece of content to ship this week, with the chain of reasoning that justifies it.

You can save the output to `my-work/captain-day-1.md` if you want to keep a record. Default behaviour is to read in main context and act.

## The prompt

Paste the block below into Claude Code in your repo:

```
You are the Captain for my D2C brand. Your job is to read everything I built
today and give me ONE specific recommendation for what to ship Monday morning.

Read in this order, then synthesise:

1. CLAUDE.md (the brand brain). Note the brand voice, top SKUs, primary
   customer, anti-positioning, and any compliance flags.
2. The most recent file in my-work/market-analyst/. Note the "content gap we
   can attack" and the executive read.
3. The most recent file in my-work/voice-of-customer/. Note the top 2 themes
   and any persona discrepancies with CLAUDE.md.
4. my-work/content-lead/<latest>-index.md. Note the Top 5 reads and any
   safety flags raised on those pieces.

Then output, in this exact shape:

---

## Ship Monday

**Piece**: <full path to the file in my-work/content-lead/pieces/ or marketplace/>

**Why this one** (4 lines, one source per line):
- From VoC: <theme name and frequency, e.g. "ingredient questions, 12 of 67 messages">
- From Market Analyst: <gap or observation that this piece exploits>
- From CLAUDE.md: <which voice rule, anti-positioning beat or product positioning aligns>
- From Content Lead: <what makes this piece in particular the top read; cite the index>

**What it costs to skip**:
<2 lines. The window of opportunity. When does this read go stale.>

**What to edit before you ship**:
<List any {placeholder} fields, any safety flags to address, any line that
needs founder input. Specific. By line number if possible.>

**The honest read**:
<2 to 3 lines. What this recommendation does not capture. What you, the
founder, know that the system does not. If you have a different instinct
about what to ship, what would change in the chain to make the system agree
with your instinct next week.>

---

Hard rules:
- Pick ONE piece. Not two. Not "and also consider...".
- Cite all four sources. If you cannot cite one, say which file is missing
  or thin, and pick the best piece you can with what you have.
- Do not invent themes, numbers, gaps or quotes that are not in the source
  files.
- Do not write the post for me. The Content Lead drafted it. Your job is
  to point.
- No em dashes.
```

## How to read the output

Three reads, in order:

### Read 1. The chain

Look at the four "From" lines. Each one cites a file you saw built today. If you can trace each line back to its source file in 30 seconds, the system is wired correctly. If any line feels generic or unsourced, the corresponding input is thin. Note it. We sharpen tomorrow.

### Read 2. The honest read

This is the most valuable part. The captain is asked explicitly to flag what it does not know. If the honest read says "your VoC sample was 28 messages, the themes are signals not patterns", that is true. Re-run VoC with MCP-fed data after Module 3 and the captain's reads get sharper.

If the honest read says "you, the founder, know things this system does not", that is also true. Use the captain as the second opinion, not the verdict. If you disagree with the recommendation, ask: "what would change in the chain to make the captain agree with my instinct next week?" The answer is almost always: edit one section of CLAUDE.md, or add one type of data to the VoC inputs.

### Read 3. The piece itself

Open the file the captain pointed to. Read it once. Edit any line that does not sound like you. Fill any {placeholder}. Address any safety flag. Then queue it to ship next week.

If the piece is wrong (genuinely off-brand, factually incorrect, doesn't fit), the issue is rarely the Content Lead. The issue is upstream:

- The voice is off → CLAUDE.md Section 7 needs work
- The fact is wrong → CLAUDE.md Section 4 (Products) or Section 6 (Competitors) needs work
- The theme is irrelevant → VoC inputs were thin, or the wrong file was read

Edit the upstream file, re-run Content Lead, re-run the captain. The system gets sharper every week.

## When to re-run

This prompt is designed to be re-run every Monday morning, automatically (Capstone session sets up the schedule). The output you get on a Monday in week 6 is sharper than the output you get today, because:

- CLAUDE.md has been edited based on what worked and what did not
- VoC has 8 weeks of fresh customer messages instead of one paste
- Market Analyst has tracked the same competitors for 8 weeks, surfacing changes you would otherwise miss
- Content Lead has shipped 4 to 5 calendars, building a library of what your customers actually engage with

The captain compounds. That is the point.

## What this prompt is NOT

- It is not an autonomous publisher. It points; you ship.
- It is not a strategy document. It is a Monday-morning entry point.
- It is not a full-week plan. It is one piece, this week. Tomorrow's plan, next week's plan, and the 90-day plan are separate Capstone outputs (Day 2, Sunday 16:15).
