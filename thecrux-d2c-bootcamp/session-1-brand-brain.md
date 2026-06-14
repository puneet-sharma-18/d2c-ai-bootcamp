[← Back to Student Handbook](student-handbook.md)

---

# Session 1: Brand Brain

**Skill introduced:** Your AI Chief of Staff. A persistent profile of your brand, voice, products, customers, competitors and compliance rules in `CLAUDE.md`. Every other teammate in the workshop reads this file first.

---

## What You'll Have After This Session

1. A populated `CLAUDE.md` in your voice, covering 7 sections: who you are, brand basics, story, products, customer, competitors, channels and voice rules
2. A persona snapshot Claude uses to personalise every later session
3. A voice test scored 4 or 5 out of 5 (3 with a sharpening plan for week-2 office hours)
4. For house-of-brands founders: a `HOUSE.md` parent plus a sub-brand `CLAUDE.md` you will deep-work for the rest of the weekend

This is the load-bearing session of the weekend. `CLAUDE.md` is what makes Market Analyst's report sound like your category, what makes Voice of Customer's themes match your customer, what makes the Content Lead's 30-day calendar read like your brand and not generic D2C content. Spend the time here.

---

## Before You Start

Open your terminal in `thecrux-d2c-bootcamp/` with Claude running.

### Drop your pre-work files into `brand-brain/`

Your pre-work files live wherever you saved them while doing **thecrux.ai/prework-d2c** (likely `~/Downloads/` or a folder on your desktop). Copy them into `brand-brain/` now.

Easiest way (works on Mac, Windows WSL and Linux): open two windows side by side. Your file manager (Finder, Explorer, Files) on one side, the `thecrux-d2c-bootcamp/brand-brain/` folder on the other. Drag the pre-work files across.

Prefer the terminal? From the repo root:

```bash
cp ~/Downloads/prework/*.md brand-brain/
cp ~/Downloads/prework/*.csv brand-brain/
cp -r ~/Downloads/prework/voice-dna brand-brain/
cp -r ~/Downloads/prework/ads brand-brain/
```

Adjust the path on the left if your pre-work files are somewhere else. If you only have some of the 8 files, copy what you have. `/brand-brain` will work with 3 or more.

### Check what landed

```
ls brand-brain/
```

You should see (from pre-work):

- `positioning.md` (one paragraph: voice, audience, wedge, competitors)
- `products.csv` (10 to 20 SKUs)
- `nominated-skus.md` (5 SKUs and 1 landing page URL for later sessions)
- `competitors.md` (one line per competitor explaining why they matter)
- `reviews.md` (20+ pasted reviews)
- `unit-economics.md` (90-day numbers by channel)
- `ads/` folder (3 to 5 screenshots of recent Meta or Google ads)
- `voice-dna/` folder (5 to 10 samples: PDPs, emails, social posts, packaging copy)

If `brand-brain/` is still empty or has fewer than 3 of these, that's fine. Skip to [Path B](#path-b-interview-me-interview-mode) and use `/interview-me` instead.

Optional but useful: a quick scan of `references/module-1-brand-brain/little-lab.example.md` to see what a fully populated `CLAUDE.md` looks like.

---

## Pick Your Path (30 seconds)

Two commands. Pick the one that describes your state right now.

| Command | When to run it | Time |
|---|---|---|
| `/brand-brain` | You have 3+ of the 8 pre-work artifacts in `brand-brain/`. Claude drafts from your files and interviews any gaps. | 15 to 20 min |
| `/interview-me` | Your `brand-brain/` folder is empty or thin, OR you'd rather walk all 7 sections by question without any folder ingest. | ~30 min |

Both produce the same `CLAUDE.md`. Same 7 sections. Same voice test. Same save behaviour.

If you run `/brand-brain` and it says "Not enough source material, run `/interview-me` instead", just switch commands. No drama.

The next part of this walkthrough splits into two paths. Read the one you're on. Both paths converge again at the **Voice test** section below.

---

# Path A: `/brand-brain` (ingest mode)

Read this section if your `brand-brain/` folder has at least 3 of the 8 artifacts. Otherwise skip to [Path B](#path-b-interview-me-interview-mode).

## A1. Inventory (1 min)

Type `/brand-brain` in your terminal. Claude runs an inventory of `brand-brain/`:

```
Inventoried brand-brain/:
  found  positioning.md      (147 words)
  found  products.csv        (18 SKUs across 1 brand)
  found  competitors.md      (4 competitors)
  found  reviews.md          (24 reviews)
  found  voice-dna/          (7 samples)
  empty  unit-economics.md
  empty  ads/
  empty  nominated-skus.md

5 of 8 artifacts present.
```

Claude proposes a mode:

> "You have 5 of 8 pre-work artifacts. I'll draft your CLAUDE.md from these and interview the 3 gaps. Sound right? (yes / draft only)"

Pick:

- `yes`. Most founders. Draft what is there, interview the rest. One pass, end with a complete CLAUDE.md.
- `draft only`. Skip gap questions entirely. Missing sections become TODO. Choose this if you'd rather come back to fill TODOs after seeing other sessions run.

If your inventory scores 0 to 2, `/brand-brain` refuses and points you at `/interview-me`. Switch commands.

## A2. Structure check (2 min)

Claude asks two short questions. Both shape every section that follows.

**Q1: Single brand or house of brands?**

If Claude sees multiple brand names in `products.csv` or `voice-dna/`, it asks. If house: Claude writes a `HOUSE.md` for the parent, asks you to nominate ONE sub-brand to deep-work this weekend, and writes `CLAUDE.md` for that sub-brand only. You replicate the pattern Monday for the others.

If sub-lines under one brand, or only one brand name in your artifacts: skipped silently.

**Q2: Online-only or omnichannel?**

If `unit-economics.md` has rows for offline retail, wholesale, quick commerce or store sales above ~10% of revenue, Claude asks. If omnichannel: Section 2 gets an offline % field; Section 7 gets an offline channel block. The Monday brief in Session 9 will then read or flag offline revenue explicitly.

If online-only: skipped silently.

## A3. Draft from artifacts (5 to 10 min)

Claude now walks the 7 sections. For each, it shows a DRAFT extracted from your `brand-brain/` files and asks you to confirm or edit.

Example Section 3 (Story) draft:

```
DRAFT from positioning.md:
  Why this brand exists: "Premium luggage built for the new Indian
  traveller who refuses to compromise on design or price."

  Anti-positioning: "We will never compete on cheapest. We will
  never compromise on warranty."

Source: brand-brain/positioning.md, lines 4 to 7.

Confirm? (yes / edit / re-extract)
```

Three responses you can give:

- `yes`. Capture and move on.
- `edit` and tell Claude what to change.
- `re-extract`. Claude re-reads the source file looking for what it missed.

For sections without source data (hybrid mode only), Claude switches to interview mode for that section:

```
Section 5 (Customer): I do not see persona data in brand-brain/.
Let me ask 4 questions to fill this.

Q1: One sentence on your primary customer. Who buys most?
```

Mixed flow. Most sections take a confirm or one edit. Sections without source take 3 to 4 questions each.

After each section, Claude shows the captured answers and asks "Looks right? (yes / edit / skip-to-next-section)".

## A4. Continue to Voice Test

Once Section 7 is confirmed, jump to the [**Voice test**](#voice-test-both-paths) section below.

---

# Path B: `/interview-me` (interview mode)

Read this section if your `brand-brain/` folder is empty, has fewer than 3 artifacts, or you simply want to walk every section by question.

## B1. Run the interview (1 min to start, ~30 to complete)

Type `/interview-me` in your terminal. Claude says:

> "We are building one file together. CLAUDE.md. Every other teammate reads this file before doing their work. Ready?"

Type `ready` (or `go` or `yes`). The interview begins.

You do not need to remember what to do. The playbook walks you through 7 sections, one field at a time.

## B2. Section 1 and persona snapshot (5 min)

Claude asks one question at a time. Examples:

> Name: who is filling this in?
> e.g. Riya Shah, founder

Type your answer. Short is fine.

After Section 1 (4 fields: Name, Role, Brand, Identity), Claude shows your persona snapshot:

> "Persona: Founder, {Brand}, {Category}, {Stage}, {Geography}."

Confirm or adjust. From here on, every question Claude asks uses your category's vocabulary.

## B3. The "why this matters" demo (90 seconds)

Before continuing, Claude shows one concrete before / after pair:

- Without `CLAUDE.md`: a generic 3-line Instagram caption announcing a hypothetical SKU launch
- With `CLAUDE.md`: the same caption, written for your persona snapshot, in your category's vocabulary

You should see the difference. The "with" version uses words you would use.

Claude says: "That is the difference. Now we build yours." Type `go`.

## B4. Sections 2 to 7 (20 to 25 min)

Claude walks the remaining sections, one question at a time:

| Section | Fields | Captures |
|---|---|---|
| 2. Brand basics | name, tagline, category, stage, founder voice | Who you are at scale |
| 3. Story | why this brand exists, anti-positioning | Your differentiation |
| 4. Products | top 3 SKUs (paste-in for now, refreshed via Shopify MCP in Session 3) | What you sell |
| 5. Customer | primary persona, secondary, discovery, retention | Who buys |
| 6. Competitors | 3 to 5 brands with where they beat us and where we beat them | The category |
| 7. Channels and voice rules | channels, ad spend, "always" and "never" phrases, compliance | Operating rules |

Useful commands at any point:

- `skip` leaves the field as TODO, moves on
- `draft it`. Claude drafts based on what you have told it; you edit
- `example`. Claude shows one personalised example
- `back`. Go back to the previous field

After each section, Claude echoes your answers and asks "Looks right?". Confirm or edit.

Once Section 7 is confirmed, continue to the **Voice test** below.

---

# Voice Test (both paths)

BEFORE saving, Claude runs the voice test. Same drill for both paths.

> "Voice test before we save."

Claude drafts a 3-line Instagram caption announcing a hypothetical product drop, using only your CLAUDE.md sections. Then asks:

> "Score it 1 to 5. 1 = not me, 5 = sounds exactly like me. What would you tighten?"

Rubric:

| Score | Meaning |
|---|---|
| 1 | Not me. Reads like any brand in the category. |
| 2 | Generic with one or two words I would use. |
| 3 | Close but off. A customer who knows my brand would notice. |
| 4 | Sounds like me. A few words I would change. |
| 5 | Sounds exactly like me. I could ship this Monday. |

If 3 or below, Claude asks which section needs tightening. Almost always Section 3 (Story) or Section 7 (voice rules). On Path A, if voice-dna/ exists and tone is the weakness, Claude offers to re-pull "always" and "never" phrases from voice-dna/ directly.

Cap at two iterations. If still under 4, save anyway. A 3 is workable for Day 1.

See the canonical session-1 file (`session-1-brand-brain.md`) for worked examples scored at 1, 3 and 5.

---

# Save (1 min)

Claude shows the full proposed CLAUDE.md as one code block. Asks:

> "Ready to save this as CLAUDE.md? (yes / edit which section?)"

Type `yes`. Claude writes `CLAUDE.md`.

For house-of-brands founders on Path A, Claude also writes `HOUSE.md` and saves your nominated sub-brand's `CLAUDE.md`. The other sub-brands become take-home replication.

Reply ✅ in the workshop chat.

---

## What You Just Built

`CLAUDE.md` is now the ground truth for every later session. Open it any time. Edit one line if a later build's output feels off. The file is yours; you own it.

The teammates that depend on it:

- Market Analyst (Session 2) reads it for the brand and competitor anchors
- Voice of Customer (Session 2) reads it for the customer the founder thinks they have
- Content Lead (Session 4) reads it for voice rules on every piece
- Performance Marketer (Session 6) reads it for anti-positioning in ad copy. On Path A, it also re-reads `voice-dna/` and `ads/` directly for tone and winning hooks.
- Growth Analyst (Session 9) reads it for channel mix and offline %. On Path A, it also reads `unit-economics.md` directly for the Monday brief.

Every later teammate reads CLAUDE.md first.

---

## What's Next

Session 2 builds two skills (Market Analyst and Voice of Customer) that read CLAUDE.md and produce real reports on your competitors and your customers.

[Continue to Session 2: Skills →](session-2-skills.md)

---

## If You Get Stuck

| Symptom | Path | Fix |
|---|---|---|
| Inventory says 0 to 2 of 8 artifacts | A | `/brand-brain` refuses and points at `/interview-me`. Switch commands. ~30 min instead of 15. Same destination. |
| Multi-brand question is confusing | A | If your products share one Instagram handle, one customer service number and one warranty, you are one brand. If each has its own, you are a house. |
| Section 3 (Story) feels generic even after re-extract | A | Tell Claude: "Pull from voice-dna/ instead of positioning.md for this section." |
| House-of-brands flow picked the wrong sub-brand | A | Re-run with: "Deep-work {brand name} instead." Claude regenerates `CLAUDE.md` for that sub-brand. `HOUSE.md` stays. |
| `products.csv` is missing | A | Type the names and prices of your top 3 SKUs in chat. Claude writes the CSV for you. Five-minute fix. |
| `unit-economics.md` is missing | A | Session 9 will run on sample data; paste real numbers Monday. Note the gap in CLAUDE.md Section 7. |
| Voice test scores 2 or 3 after two edits | both | Save it. 3 is workable. Sharpen in week-2 office hours after you have real outputs from later sessions to learn from. |
| Frozen on Section 3 ("why this brand exists") | B | Tell Claude: "Use this as a starting point: {the version you would tell a friend over a drink}." Edit later. |
| Section 6 (Competitors) eats too long | B | Use `draft it` with 3 obvious competitor names. Market Analyst in Session 2 does the actual research. |
| Section 4 (Products) wants all 14 SKUs | both | Top 3 by revenue. The rest gets filled by Shopify MCP in Session 3. |
| Compliance section feels overwhelming | both | This is the field that protects every Content Lead output later. Spend 2 to 3 minutes here, not 30 seconds. |
| `/brand-brain` or `/interview-me` not recognised | both | Run `claude` from the repo root: `cd ~/thecrux-d2c-bootcamp && claude`. The slash commands live in `.claude/commands/`. |

For anything not on this list, raise hand in the workshop chat.

---

## Appendix: The slash command spec (for instructors)

Two separate commands. Each does one thing.

- `/brand-brain` at `.claude/commands/brand-brain.md`. Ingest-first. Reads the folder, drafts what it can, interviews the gaps. Requires at least 3 of 8 artifacts.
- `/interview-me` at `.claude/commands/interview-me.md`. Pure interview. Walks all 7 sections by question. No folder dependency.

Both produce the same `CLAUDE.md`. Same 7-section template. Same voice test. Same save behaviour.

**`/brand-brain` flow:**

1. **Inventory**. `ls brand-brain/` and classify each file by presence and size. Score 6 to 8 suggests `draft only`; 3 to 5 suggests `hybrid`; 0 to 2 refuses and redirects to `/interview-me`.
2. **Structure detection**. Signal-driven. Multi-brand from `products.csv`; omnichannel from `unit-economics.md`. Asks only when signals fire.
3. **Per-section flow**.
   - INGEST: extract from named source file, show draft with line-level citations, accept `yes` / `edit` / `re-extract`.
   - INTERVIEW (hybrid mode only): ask the 3 to 5 questions for that section.
   - DRAFT-ONLY mode skips interview. Missing sections become TODO with instructions to re-run after adding the file, or run `/interview-me`.
4. **Voice test**. Invariant. Same 1 to 5 rubric. Cap at two iterations.
5. **Save**. Write `CLAUDE.md` always. Write `HOUSE.md` if multi-brand mode triggered.

**Instructor-only flags on `/brand-brain`:**

- `--debug` shows extraction confidence per field
- `--draft-only` forces draft mode and skips gap questions
- `--rebuild` re-runs ingest on an existing `CLAUDE.md` (useful mid-weekend after adding files)

There is no `--interview-only` flag. For pure interview, run `/interview-me` instead.

**Expected timings:**

| Command | Founder profile | Time |
|---|---|---|
| `/brand-brain` draft-only | Full pre-work | 10 to 15 min |
| `/brand-brain` (draft + interview) | Partial pre-work | 15 to 20 min |
| `/interview-me` | Thin or no pre-work | 30 to 40 min |
