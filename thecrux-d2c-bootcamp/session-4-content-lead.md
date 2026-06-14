[← Back to Student Handbook](student-handbook.md)

---

# Session 4: Content Lead

**Skill unlocked:** Subagents. Specialised teammates that run in their own context for big jobs. The Content Lead reads your chain, plans a calendar, drafts your priority pieces and writes marketplace listings, all in your voice, all in one run.

---

## What You'll Have After This Session

DEFAULT scope (recommended for the workshop slot, runs cleanly on Pro plan):

1. A 30-day content calendar in `my-work/content-lead/<today>-calendar.md`
2. 5 priority content pieces (the ones that ship in the first 14 days), in `my-work/content-lead/pieces/`
3. 2 marketplace listings (top SKU on Amazon + Flipkart), in `my-work/content-lead/marketplace/`
4. An index file pointing at the Top 5 reads

POWER scope (Max plan or take-home):
- Full 30-day calendar + 20 pieces + 10 marketplace listings (5 Amazon + 5 Flipkart)

Saturday's payoff moment lands in this session. The morning's interview turns into Monday-morning publishable content by the afternoon.

---

## Before You Start

You need:
- CLAUDE.md saved (Session 1)
- Latest Market Analyst report in `my-work/market-analyst/` (Session 2)
- Latest VoC report in `my-work/voice-of-customer/` (Session 2 or, ideally, the MCP-fed live one from Session 3)

If any of these are missing, the Content Lead will refuse to run and tell you which file is missing. That is correct behaviour: you do not want it inventing content.

---

## Step 1: What is a subagent (5 min)

Sessions 1 and 2 used slash commands and skills. They run in your main Claude conversation context. That is fine for single-step work.

Session 4's Content Lead is a **subagent**. It runs in its own context window. The orchestrator (your main Claude in the terminal) spawns it via the Task tool, the subagent does the heavy multi-step work in isolation, returns a summary, stops.

Why a subagent and not a skill: the Content Lead does multi-step work that benefits from its own context. It reads three sources, plans a 30-day calendar, drafts pieces, generates listings, runs a brand safety pass. That is too much for a single skill in your main thread.

The contrast:

| | Skills (Session 2) | Subagent (Session 4) |
|---|---|---|
| Context | Runs in main thread | Runs in isolated context |
| Job shape | Single-step playbook | Multi-step, multi-file work |
| When | Founder asks one thing | Founder asks for a deliverable that needs many files read and many files written |
| Example | "What are competitors doing?" | "Plan and draft a month of content for me" |

---

## Step 2: Pick scope (1 min)

Two scopes:

```
DEFAULT  (~5 min, low token cost, recommended for Pro plan)
         30-day calendar, 5 priority pieces (the ones that ship in the
         first 14 days), 2 marketplace listings (Amazon + Flipkart for
         top SKU).

POWER    (~15 min, high token cost, recommended for Max plan or a real
         launch run)
         30-day calendar, 20 pieces (full channel mix), 10 marketplace
         listings (5 Amazon A+ + 5 Flipkart).
```

For the workshop slot: **DEFAULT**. Even if you are on Max, DEFAULT is what runs cleanly in time. POWER is your take-home run on Monday for a real campaign launch.

Scope has to be in the spawn prompt itself. The subagent runs in its own context and cannot pause to ask you mid-run, so if you forget to set scope it falls back to DEFAULT. To run DEFAULT:

```
Spawn the Content Lead subagent with SCOPE=default. Plan a 30-day
content calendar and draft the priority pieces and marketplace listings
for my brand, reading from my latest market-analyst and voice-of-customer
reports.
```

To run POWER, swap `SCOPE=default` for `SCOPE=power`. The subagent's first line back to you names the scope it actually ran, so you will see immediately if it picked the wrong one.

---

## Step 3: Run the subagent (~5 min for DEFAULT)

Submit the spawn prompt with `SCOPE=default`. The subagent:

1. Reads CLAUDE.md
2. Reads the latest Market Analyst report
3. Reads the latest VoC report
4. Plans the 30-day calendar (lighter output, sets you up for POWER later)
5. Drafts the 5 priority pieces (Instagram captions and emails biased to your top VoC themes)
6. Writes 2 marketplace listings (Amazon A+ + Flipkart for your top SKU)
7. Runs the brand safety pass on every output
8. Saves everything to `my-work/content-lead/`
9. Writes the index file

While it runs, watch the run log. You see it reading your VoC themes, biasing the calendar to those themes, drafting captions that reference your customers' actual concerns.

When done, it hands back one summary message. Reply ✅ in the workshop chat.

---

## Step 4: Read the index, not the files (5 min)

Open the index:

```
my-work/content-lead/<today>-index.md
```

The index has:
- The Top 5 reads for the founder
- Coverage check (which themes, SKUs, channels got covered)
- Safety flags raised (count + which pieces have them)

**Read the index first, not every piece.** This is the most important habit for working with subagents. The Content Lead produced a pile of inventory; the index tells you what to actually read.

Open the Top 5 pieces called out in the index. Read those 5 carefully. Edit anything that does not sound like you (CLAUDE.md voice rules drive this; if multiple pieces feel off-voice, edit Section 7 of CLAUDE.md and re-run).

---

## Step 5: Address the safety flags (if any)

If your Content Lead raised safety flags, open each flagged piece. The safety section at the bottom names the specific issue:

- **Banned word**: replace with a phrase from CLAUDE.md "always" list, or strike
- **Regulated claim**: pull the lab report reference, or strike
- **Invented number**: replace with `{placeholder}` or pull the real number from Shopify
- **Customer quote not in VoC**: replace with a real one from the VoC report, or strike
- **Anti-positioning violation**: edit so the piece does not contradict CLAUDE.md Section 3

Better a flagged piece you reject than a takedown notice later. Treat the flags as a checklist, not as the subagent being wrong.

---

## Step 6: The expert roast (3 min)

The Content Lead ran. The brand safety pass ran. The pieces are publishable. Now we sharpen.

A roast is one extra prompt that names an expert lens and asks Claude to tear into a piece from that lens. Same Claude, same context, different role. It finds gaps the safety pass cannot see, because the safety pass is a rule list and a roast is judgment.

The prompt is generic. Fill in three slots: the file, the lens, and the stakes.

```
Read {path to one piece}. You are {a specific expert who would see this
piece in the wild}. Tear it apart. What is the weakest claim? What does
your reader skim past or stop trusting? What would a competitor or
regulator screenshot and use against the brand?

Return the top 3 findings. For each, name the slide or line, the
problem, and the one-line fix.
```

Worked example on the sample brand. The file is `examples/little-lab/my-work/content-lead/pieces/instagram-01-cradle-cap-carousel.md`. The lens is "a paediatric dermatologist who has seen 200 cradle cap consults this year". The stakes are an ASCI complaint. About 30 seconds after running, three findings come back:

- Slide 4 says "paediatrically reviewed for newborns". Reviewed by whom? Name the paediatrician or strike the phrase. As written, ASCI will ask the brand to substantiate it.
- Slide 5 timeline "Day 7: most cases clear" reads as a treatment outcome without a study. "Flakes loosen by Day 3" is observational and fine. "Most cases clear by Day 7" is an efficacy claim and is not.
- The "8 months of cradle cap, cleared in 4 days" testimonial is the strongest line in the post and the riskiest. A regulator reads it as a before-after claim. Pair it with an explicit "individual result, not typical" or strike the timeline numbers.

Edit the carousel in one turn, re-run the safety pass, save. The piece is meaningfully tighter than what the subagent produced.

Two reads to take away:

**The roast finds what the safety pass cannot.** The safety pass catches banned words and known regulated terms. A roast brings judgment. It knows what a paediatrician would push back on, because Claude has read a lot of paediatricians.

**The lens does the work.** For a baby brand, paediatrician. For an ad on Friday, media buyer who has seen 10,000 ads in the category. For a PDP, comparison shopper with four tabs open. Wrong lens, generic roast. Right lens, the post gets sharper in 30 seconds.

You do not need to roast your own pieces in the workshop slot. Save it for the take-home pass. We will use the same pattern on Sunday in Session 6 on ad copy, where the cost of skipping a roast is paid in money.

---

## What You Just Built

A real content batch on your real brand:
- Calendar for 30 days
- 5 pieces ready to schedule (or edit and schedule)
- 2 marketplace listings
- Brand safety flagged where it matters

Plus, more importantly, you saw the chain working end to end. CLAUDE.md feeds skills. Skills feed the subagent. The subagent ships the deliverable.

You also saw the expert roast pattern. One extra prompt, one named lens, a piece that is meaningfully sharper. We use it again on Sunday for ads.

The Content Lead is not a one-shot. Re-run it monthly for a fresh calendar. POWER scope when you have a real campaign launching. The teammate compounds.

---

## What's Next

Session 5 wires the Day-1 captain prompt: one prompt that reads everything you built today and tells you ONE specific piece to ship Monday morning. Short, sharp, declarative. Day 1's close.

[Continue to Session 5: Day 1 Integration →](session-5-integration.md)

---

## If You Get Stuck

| Symptom | Fix |
|---|---|
| Subagent refuses to run | It tells you which file is missing. Re-run that prerequisite session. |
| Output reads generic | CLAUDE.md voice rules section is thin. Edit Section 7 (add 5 specific "never" phrases), re-run. |
| 5 pieces all sound the same | VoC themes are weak (sample under 30 messages). Re-run after adding more data to your Drive folder. |
| Safety flags on every piece | Regulated category + every theme touches a claim. Read the flags as a "do not say without proof" list. |
| Marketplace listing has invented specs | Shopify MCP not connected, CLAUDE.md Section 4 was bracketed. Connect Shopify or fill Section 4 manually for top 3 SKUs, re-run. |
| Want to read every file in the workshop slot | Do not. Read the 5 in the index's Top 5 reads. Skim the rest later. The index is the entry point. |
| POWER ran out of context mid-way | Pro plan rate limit. Re-run with DEFAULT, take POWER home. |

For anything not on this list, raise hand in the workshop chat.
