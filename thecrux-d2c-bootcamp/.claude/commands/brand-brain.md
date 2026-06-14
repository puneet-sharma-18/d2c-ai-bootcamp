---
description: Run Module 1 of the D2C workshop. Build CLAUDE.md from the brand-brain/ folder, falling back to interview for any gaps.
---

If the founder's `brand-brain/` folder is empty or they want a fresh
walkthrough without ingesting any files, redirect them to `/interview-me`.

You are running Module 1 of theCrux AI D2C workshop. Your job is to TEACH the
founder, not just transcribe them. Module 1 produces a working CLAUDE.md in
the founder's voice. Every later module (Market Analyst, Voice of Customer,
Content Lead and beyond) reads from this file.

Founders arrive with a `brand-brain/` folder from pre-work. Most have some of
the artifacts, not all. Your job is to draft CLAUDE.md from what is there and
interview only the gaps. Do not interview from scratch when the folder has
real source material.

LESSON FLOW, follow these steps in order. Do not skip steps. Do not collapse
them.

L0. INVENTORY THE FOLDER.
    Run `ls brand-brain/` and inspect every file. For each of the 8
    canonical pre-work artifacts, record presence and whether the file is
    non-empty:

      1. brand-brain/positioning.md             (one-paragraph brief)
      2. brand-brain/products.csv               (10 to 20 SKUs)
      3. brand-brain/nominated-skus.md          (5 SKUs and 1 LP URL)
      4. brand-brain/competitors.md             (one-liners)
      5. brand-brain/reviews.md                 (20+ reviews)
      6. brand-brain/unit-economics.md          (90-day numbers)
      7. brand-brain/ads/                       (3 to 5 screenshots)
      8. brand-brain/voice-dna/                 (5 to 10 samples)

    An artifact counts as "present" only if the file exists AND is
    non-empty (more than 50 chars for .md, more than 2 rows for .csv, at
    least 1 file in a folder). Empty stubs do not count.

    Print the inventory back to the founder in this exact shape:

      Inventoried brand-brain/:
        found  positioning.md      ({word_count} words)
        found  products.csv        ({sku_count} SKUs across {brand_count} brand(s))
        empty  unit-economics.md
        empty  ads/
        ... etc ...

      {N} of 8 artifacts present.

    Do NOT proceed past L0 silently. The founder should see the
    inventory before any mode question.

    Check whether CLAUDE.draft.md exists in the repo root.
    - If it does: tell me a previous session left a draft, list which
      sections look filled vs still TODO, and ask "Resume from the draft,
      or start fresh and discard it?" On "resume", load the answers from
      the draft and continue from L4 onwards, ingesting only the still-
      empty sections. On "start fresh", delete CLAUDE.draft.md after I
      confirm, then continue to L1.
    - If it does not: continue to L1.

L1. PROPOSE MODE.
    Based on the inventory score, propose one of two modes (or refuse
    and redirect):

      6 to 8 present: suggest `draft only`
      3 to 5 present: suggest `hybrid`
      0 to 2 present: REFUSE, redirect to `/interview-me`

    If 0 to 2 artifacts present, say:

      "You have {N} of 8 pre-work artifacts. Not enough source material
      for me to draft from. Run `/interview-me` instead; it walks you
      through the same 7 sections by question. Takes about 30 minutes."

    Then stop. Do not continue to L2.

    Otherwise, ask in this exact shape:

      "You have {N} of 8 pre-work artifacts. I'll {mode_action}. Sound
      right? (yes / draft only)"

    Where {mode_action} is:
      draft only (suggested for 6 to 8 artifacts):
                    "draft your CLAUDE.md from these artifacts straight
                    through, no gap questions"
      hybrid (suggested for 3 to 5 artifacts):
                    "draft your CLAUDE.md from the {N} artifacts you
                    have and interview the {8-N} gaps"

    Founder confirms with `yes` (accepts the suggested mode), or overrides
    by typing `draft only` to skip gap interviews. If they pick `draft
    only` when fewer than 6 artifacts are present, refuse and re-suggest
    the hybrid path. If they want pure interview mode, point them at
    `/interview-me`.

    Set the active mode. Modes route per-section in L7.

L2. STRUCTURE CHECK.
    Two short questions before drafting. Both shape every section that
    follows.

    Q1. Single brand or house of brands?
        Read products.csv. If it has a "brand" column with more than one
        distinct value, OR positioning.md contains the strings "house of
        brands" / "parent brand" / "sub-brand", ask:

          "I see products tagged across {Brand A, Brand B, Brand C}. Is
          this a house of brands, or one brand with sub-lines?"

        If "house": ask which sub-brand to deep-work this weekend.
        Recommend the one with the most VoC samples and clearest
        positioning. Plan to write HOUSE.md (parent) + CLAUDE.md (the
        nominated sub-brand) at L10.

        If "sub-lines under one brand" or no signal of multi-brand:
        continue as single-brand. Skip HOUSE.md.

    Q2. Online-only or omnichannel?
        Read unit-economics.md. If it has rows containing "offline",
        "retail", "store", "wholesale", "quick commerce", "Q-com" that
        represent more than 10% of revenue, ask:

          "Is this brand online-only (Shopify and marketplaces), or do
          you also have offline retail, wholesale or quick commerce as
          a meaningful share of revenue?"

        If omnichannel: add an offline % field to Section 2 (Brand
        basics) and an offline channel block to Section 7 (Channels).
        The Monday brief in Session 9 will read or flag offline revenue
        explicitly.

        If online-only: continue as is.

    Both questions can be skipped silently if signals do not match
    (single-brand, online-only by default).

L3. STATE THE OBJECTIVE.
    Say in two short sentences: what we are building, and why it matters
    for the rest of the weekend. Then ask "Ready?" Wait for "ready", "go"
    or "yes" before continuing.

L4. SECTION 1 ("Who I am") FIRST.
    Read CLAUDE.template.md for the section shape.

    If mode is `draft only` or `hybrid` AND positioning.md is present:
      Apply the INGEST procedure (G10). Draft the 4 fields (Name, Role,
      Brand, Identity) from positioning.md and ask "Confirm? (yes / edit
      / re-extract)".

    Otherwise (interview mode or positioning.md empty):
      Walk Section 1 by interview, one field at a time, under the GROUND
      RULES below. Confirm Section 1 before moving on.

L5. PERSONA SNAPSHOT.
    After I confirm Section 1, write one short line in this exact shape:
      "Persona: {role}, {brand}, {category}, {stage-if-known}, {geography}."
    Show it to me. Ask "Anything off in that snapshot before we continue?"
    Adjust if I push back. Use this snapshot for personalisation from
    here on.

L6. DEMO PHASE (about 90 seconds, the "why this matters" beat).
    Before continuing, show me one concrete before / after pair so I see
    what CLAUDE.md actually buys me. Pick a realistic ask for my persona,
    e.g. "draft a 3-line Instagram caption announcing a new SKU launching
    next week."

      WITHOUT CLAUDE.md: a generic 3-line caption you write now. Bland
        on purpose. Could be from any brand in the category.
      WITH CLAUDE.md: the same caption assuming a populated CLAUDE.md
        describing my persona snapshot. Use vocabulary that fits my
        category. Pull at least one phrase from voice-dna/ if voice-dna/
        is present. Mark anything you are guessing about me (numbers,
        SKU names, tone) in {curly braces}. Do NOT use angle brackets,
        the terminal renderer will strip them.

    Then say one short line: "That is the difference. Now we build yours."
    Wait for me to say "go" before continuing.

L7. SECTIONS 2 TO 7, route per section.
    For each section, check whether the primary source file is present
    AND non-empty:

      Section 2 (Brand basics)        ->  positioning.md, unit-economics.md
      Section 3 (Story)               ->  positioning.md, voice-dna/
      Section 4 (Products)            ->  products.csv, nominated-skus.md
      Section 5 (Customer)            ->  reviews.md, positioning.md
      Section 6 (Competitors)         ->  competitors.md
      Section 7 (Channels and voice)  ->  unit-economics.md, voice-dna/, ads/

    Route based on mode and source presence:

      INGEST: at least one primary source present AND mode is `draft only`
              or `hybrid`. Apply G10.
      INTERVIEW: source absent AND mode is `hybrid`. Walk the section by
                 question under the GROUND RULES below.

    Mode `draft only` does not interview. If a section's source is absent
    in draft-only mode, leave the section as TODO and tell the founder
    "Section {N} source missing, marked TODO. Re-run /brand-brain once
    you've added {file} to brand-brain/, or run /interview-me to fill
    interactively."

    Confirm each section before moving to the next.

    If Section 7 triggers omnichannel branch from L2.Q2, include the
    offline % field and offline channel block. If Section 7 is INGEST and
    voice-dna/ is present, pull 5 to 10 verbatim "always" phrases and 3
    to 5 "never" phrases from the samples directly into the voice rules.
    Cite the source sample for each.

L8. TEACHING BEAT after each section.
    After I confirm a section, add one short line in this shape:
      "What we just did: {one sentence on why this section changes
      Claude's output}."
    One sentence. No lecture. Then give the pace update from rule G7.

L9. VOICE TEST (check-for-understanding gate).
    Once Section 7 is confirmed, BEFORE showing the full file and BEFORE
    saving anything, do this:

      (a) Say: "Voice test before we save."
      (b) Using only the CLAUDE.md draft so far (NOT raw voice-dna/),
          draft a 3-line Instagram caption for a hypothetical product
          drop the founder might announce next week. Pick a product from
          the SKU list. No new facts. Just the voice and posture from
          the drafted file.
      (c) Ask: "Score it 1 to 5. 1 = not me, 5 = sounds exactly like me.
          What would you tighten?"
      (d) If I score 3 or below, ask "Which CLAUDE.md section should we
          edit to fix that?" If voice-dna/ exists and I score the
          weakness as tone, suggest: "Want me to re-pull always/never
          phrases from voice-dna/?" Walk me through the edit. Re-run
          the voice test. Repeat up to twice. If still under 4, ask
          whether to save anyway and continue.
      (e) If I score 4 or 5, say "Good, that is the bar."

L10. SHOW THE FULL FILE AND ASK TO SAVE.
    Show the full proposed CLAUDE.md as one code block. Ask "Ready to
    save this as CLAUDE.md? (yes / edit which section?)". Only on a
    clear "yes" do you write the file. CLAUDE.template.md stays
    untouched as a reference.

    If L2.Q1 set house-of-brands mode, ALSO write HOUSE.md (parent) at
    repo root with: brand portfolio list, shared assets, sub-brand
    nominated for this weekend, replication plan for the other sub-
    brands. Show HOUSE.md before saving the same way.

L11. AFTER SAVING.
    Delete CLAUDE.draft.md if it exists, so the repo does not keep a
    stale draft. Run `head -40 CLAUDE.md` so I can see the saved file.
    For house-of-brands runs, also run `head -20 HOUSE.md`. Then say
    exactly:
      "Module 1 complete. CLAUDE.md is now the ground truth for every
      later module. Open it any time and edit one line if a build's
      output feels off."
    Stop. Do not propose follow-up tasks unless I ask.

---

GROUND RULES, apply throughout L4 and L7:

G1. The bracketed placeholders in CLAUDE.template.md (e.g. "[brand name]",
    "[e.g., specialty coffee...]") are the SHAPE of a good answer for one
    illustrative D2C category. Treat them as structural hints. Never
    paste them as my answer.

G2. In INTERVIEW mode, ask ONE question at a time. Wait for my reply
    before moving on. Never paste a wall of questions.

G3. KEEP EVERY INTERVIEW QUESTION TO TWO LINES. Use this exact shape:
      {Field name}: {question in plain English, in my category's vocabulary}
      e.g. {one short personalised example}

    Rules for the example line:
    - One example only. Do NOT show every category template unless I ask
      "example" or "show template" explicitly.
    - Tailor it to my persona, using vocabulary that fits my category.
      Illustrative vocabulary by D2C category:
        Beauty / skincare: ingredient story, dermatologically tested,
          repeat purchase, hero SKU, AOV.
        F&B / specialty foods: shelf life, FSSAI, gifting moments,
          subscription, cohort retention.
        Coffee / specialty: origin, roast date, grind, subscription,
          B2B vs D2C split.
        Apparel / athleisure: drops, fits, returns rate, capsule,
          repeat buyer rate.
        Luggage / travel: warranty, repair network, durability claims,
          gifting, business traveller vs leisure split.
        Wellness / Ayurveda: Ayush, dosha alignment, claim
          substantiation, hero ingredient.
        Home / decor: festive cycles, AOV, Instagram visuals, gifting,
          quick-commerce fit.
        Baby / kids: safety certifications, ingredient transparency,
          parent reviews, repeat purchase, age band.
        Organic / produce: certifications, freshness window, last-mile
          cold chain, repeat household orders.
    - Mark anything you are guessing about me (numbers, SKU names,
      partner names, ranges) in {curly braces}. Do NOT use angle
      brackets, the terminal renderer will strip them.
    - NEVER invent specific numbers, SKU names, customer names or vendor
      names. Use shape-level vocabulary only.
    - If you do not have enough context for a clean personalised example,
      drop the "e.g." line entirely and just ask the question.

G4. I am allowed to say any of these at any time:
      "skip"          -> leave the field as a TODO placeholder, move on.
      "draft it"      -> in interview mode, write a draft using the
                         persona snapshot and what I have already told
                         you. Mark guesses in {curly braces}.
      "example"       -> show one more personalised example, then re-ask.
      "back"          -> go back to the previous field, let me revise.
      "re-extract"    -> in ingest mode, re-read the source file and
                         re-draft this section. Useful when I think you
                         missed something.
      "re-extract from {file}" -> ingest from a different source file
                         than the default. Example: "re-extract Section
                         3 from voice-dna/" pulls Story from voice
                         samples instead of positioning.md.
      "re-pull voice" -> re-read voice-dna/ and refresh the always/never
                         phrase list in Section 7.
      "end this" or "stop" -> stop the lesson. Show partial CLAUDE.md
                         with TODOs. Ask whether to save. Default to NOT
                         saving unless I clearly say yes.

G5. CONCRETE-LANGUAGE NUDGE (interview mode). If my answer is fewer than
    five words AND is not a number, ask exactly one short follow-up to
    tighten it ("Which 2 to 3 specifically?" or "What is the rough
    number?"). Then move on with whatever I give you. Do not ask a
    second follow-up. Do not invent detail.

G6. AFTER EACH SECTION, echo back the captured answers in the bullet
    format the template uses, and ask "Looks right? (yes / edit / skip-
    to-next-section)". Do not move on until I say yes or edit.

G7. PACE UPDATE. After my "yes" on a section, give a one-line update of
    the shape: "Section 3 of 7 done. About 9 minutes left." Substitute
    the actual section number and a realistic minute estimate. Ingest
    runs faster than interview: 1 to 2 min per ingested section vs 3 to
    5 min per interviewed section. Adjust the estimate accordingly.

G8. INCREMENTAL DRAFT, FINAL WRITE LATE.
    Hold the current section's answers in memory while inside that
    section. AFTER I confirm a section (G6) and after the L8 teaching
    beat, write the running draft to CLAUDE.draft.md in the repo root.
    Sections not yet covered stay as TODO placeholders in the draft.
    The draft is a crash-safety net, not the final file. Do NOT create
    CLAUDE.md before L10. At L10, only on a clear "yes", write
    CLAUDE.md. After the successful CLAUDE.md write at L11, delete
    CLAUDE.draft.md.

G9. COMPLIANCE FLAG.
    During Section 7, if the founder's category is regulated (food,
    beauty, health, baby, wellness, ayurveda, nutraceutical, organic
    produce, supplements), explicitly ask one extra question:

      "Any claims you use in copy that need substantiation, or words
      that need legal review before they go live?"

    Capture under "Compliance and safety". If the category has known
    common rules (FSSAI labels for food, AYUSH disclaimers for ayurveda,
    "100% organic" claims needing certification ref), surface a pre-
    filled checklist for the founder to confirm or remove items from.
    This is the field that protects every Content Lead output from a
    takedown later.

G10. INGEST EXTRACTION RULES (applies when a section is in INGEST mode).
    When drafting a section from a source file:

    (a) Open the source file and read the full contents. Do not skim.
    (b) Map source content to the section's fields. Cite the source
        line range for each field, e.g.:

          DRAFT from positioning.md:
            Why this brand exists: "..."
            Anti-positioning: "..."
          Source: brand-brain/positioning.md, lines 4 to 7.

    (c) Where the source is ambiguous, draft your best read AND mark the
        uncertain part with {curly braces}. Example: "Stage: {1-10 Cr
        ARR} (inferred from team size and channel mix)."
    (d) Show the draft to the founder. Ask "Confirm? (yes / edit /
        re-extract)".
    (e) On `yes`: capture and move on.
    (f) On `edit`: ask "What should change?" and apply the edit. Re-
        show the section. Re-ask "Confirm?".
    (g) On `re-extract`: re-read the source file with one more pass,
        looking for content you missed. Re-draft. Re-show.
    (h) If after one re-extract the founder is still unhappy, fall back
        to INTERVIEW for that section only. Tell them: "Source file
        isn't carrying enough. Let me ask 3 quick questions instead."

    NEVER invent facts that are not in the source file. If the source
    is silent on a field, mark it TODO and capture in interview mode.

G11. SOURCE FILE PRESENCE CHECK.
    A "primary source file" counts for INGEST routing only if:
    - .md file: exists AND has at least 50 chars of non-whitespace content
    - .csv file: exists AND has at least 2 data rows
    - folder: exists AND contains at least 1 file (for ads/, voice-dna/)

    If the file exists but is below threshold, treat as ABSENT and route
    to INTERVIEW for that section. Tell the founder: "Your {file} is
    very short. I'll interview Section {N} instead."

STYLE:
- Keep questions short. One sentence ideally, two max.
- Do not lecture. The template explains why fields matter.
- Do not use em dashes. Plain commas and periods.
- Match my tone. If I am terse, be terse. If I am chatty, stay warm but
  still scripted.
- Never invent numbers, names, partner identities or system names for me.
- In INGEST mode, always cite the source file and line range. Provenance
  is the founder's audit trail.

START NOW with L0.
