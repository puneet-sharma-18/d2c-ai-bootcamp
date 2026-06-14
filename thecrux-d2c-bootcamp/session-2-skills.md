[← Back to Student Handbook](student-handbook.md)

---

# Session 2: Skills

**Skill unlocked:** The Claude Code skills system. You build one skill from scratch (Write in Brand Voice) and run two pre-shipped ones (Market Analyst, Voice of Customer). By the end you understand what a skill actually is, because you wrote one.

---

## What You'll Have After This Session

1. A `write-in-brand-voice` skill in `.claude/skills/` that you authored, version-controlled in your repo
2. A competitor intel report on YOUR 3 to 5 competitors, in `my-work/market-analyst/`
3. A Voice of Customer report on YOUR reviews and tickets, in `my-work/voice-of-customer/`
4. `frontend-design` and `document-skills` installed from the official Anthropic marketplace, ready for Sessions 6, 7 and 10
5. A working mental model for the three ways to acquire a skill: write your own, run pre-shipped, install from marketplace

---

## Before You Start

You need:
- CLAUDE.md saved (Session 1 done)
- Your `brand-brain/` folder from pre-work, especially `voice-dna/` (5 to 10 writing samples) for the skill you'll build
- Your `brand-brain/` folder from pre-work, with reviews (CSV, screenshots or paste), competitor notes and (optional) support tickets (or be ready to paste during the session). Full pre-work doc: thecrux.ai/prework-d2c.

If your VoC inputs are thin (under 30 messages), the skill still runs but the themes will be soft. Re-run after Session 3 (MCPs) when Drive and Gmail are connected.

**What sharp inputs look like.**

For Write in Brand Voice: 5 to 10 samples in `brand-brain/voice-dna/` (PDPs, emails, social posts, packaging copy). If you skipped that part of pre-work, the skill falls back to your homepage URL from CLAUDE.md Section 6, so it still works. The first run is sharper if you populated voice-dna.

For Market Analyst: the 3 to 5 competitor names already in Section 6 of CLAUDE.md, plus their homepage URLs paste-ready in your notes app. Optional but useful: one ad screenshot per competitor, one Amazon listing URL per competitor. Skill still runs without optionals; report is just less specific on paid and marketplace dimensions.

For Voice of Customer, in order of signal strength:

| Tier | Inputs |
|---|---|
| Strong | 100+ reviews CSV (Amazon Seller Central or Shopify export), 90-day support tickets CSV (Zoho / Freshdesk / Intercom), or 200 to 500 WhatsApp Business chats exported as .txt |
| Medium | 30 to 100 reviews pasted as text, 30 to 100 support emails in one doc, a team-maintained feedback spreadsheet |
| Weak | Under 30 messages, only positive reviews, or only one channel |

**Privacy.** Strip phone numbers, full email addresses and order IDs before pasting. The skill runs a privacy pass before saving, but do not paste raw PII into a chat thread your team can see. If you cannot strip in time, save the raw file to `resources/customer-data-raw.csv` (already gitignored) and point the skill at the file path.

---

## Step 1: Skills vs slash commands (5 min)

Session 1 used `/interview-me`. That is a **slash command**: you type its name, it loads. Explicit invocation.

A **skill** is different. You describe what you want, Claude reads the available skills, picks the one whose description matches, and loads it. You do not type the skill's name.

The contrast in one block:

```
> /interview-me
   (slash command, explicit invocation)

> "look at our top 3 competitors this week and tell me where they are beating us"
   (no command. Claude reads .claude/skills/, sees market-analyst's description
   matches, autoloads it.)
```

Both are playbooks. The slash command waits to be called. The skill volunteers when its description matches what you said.

Two skills are already provided in this repo (`.claude/skills/market-analyst/` and `.claude/skills/voice-of-customer/`). They autoload on the right prompts. You just have to ask normal questions. Before you run them, you are going to build one of your own so you understand what a skill actually is.

---

## Step 2: Build your first skill, `write-in-brand-voice` (~25 min)

The concept is more abstract than the file. A skill is a folder under `.claude/skills/<name>/` with a single `SKILL.md` inside it. The file has YAML frontmatter on top (`name` and `description`) and a body that tells Claude what to do. That's all. The description is the part that decides whether the skill autoloads.

You are going to write a skill that takes a draft or topic and rewrites it in your voice, reading from CLAUDE.md and your `brand-brain/voice-dna/` samples.

### 2a. Look at a real skill first (3 min)

Open `.claude/skills/market-analyst/SKILL.md` in your editor. Look at the top:

```yaml
---
name: market-analyst
description: Generate competitor intelligence reports for D2C brands. Analyze 3 to 5 competitors across pricing, positioning... Triggers on phrases like "analyze our competitors", "what is brand X doing", "competitor research"...
---
```

The `description` is the most important line in the whole file. When you type a prompt, Claude reads every skill's description and decides which one matches. Vague description, no autoload. Specific description with trigger phrases, autoload works.

Scroll the body briefly. It's instructions in plain English: "read these files in this order", "echo back the scope", "ask 'Look right?'". That's a skill. No magic.

### 2b. Create your skill file (10 min)

In Claude:

```
Create a new skill called write-in-brand-voice.
The description should make it autoload when I ask you to write, draft,
rewrite or polish any copy: emails, social posts, product blurbs, landing
page copy, customer replies. Include the trigger phrases that match how
I actually talk.

The body should:
1. Read CLAUDE.md (Section 4 voice rules, Section 5 customer)
2. Read 3 to 5 files from brand-brain/voice-dna/ that match the format
   I asked for. If voice-dna is empty, WebFetch the homepage URL from
   CLAUDE.md Section 6 as a fallback.
3. Confirm scope back to me before writing anything longer than one line
4. Apply never-words and anti-patterns from CLAUDE.md as hard filters
5. Show a "Sources used" footer with the actual file names so I know
   what shaped the output
6. Run a brand safety pass before showing me the draft

Keep it short. Under 80 lines. I want to read it end to end.
```

Claude writes the file. Open it in your editor and read it. Two things to check:

1. **The description.** Does it include trigger phrases that match how you actually talk? If you say "make this sound less corporate" but the description only lists "rewrite this", the autoload will fail. Edit the description to add your phrases.
2. **The body.** Does it read CLAUDE.md and `brand-brain/voice-dna/` in the right order? Does the "Sources used" footer step exist? If anything is off, edit it directly or ask Claude to fix it.

You may need 2 or 3 iterations. That's the lesson. A skill is a file you edit, not a black box.

### 2c. Test it (10 min)

Before testing, open your CLAUDE.md and confirm the brand voice rules section has at least 5 to 10 "never" words specific to your category. If the list is short or empty, the safety pass has nothing to bite on. Fix CLAUDE.md first, then come back.

Close the file. In Claude, do not type the skill's name. Just ask normally:

```
Write me an Instagram caption for our hero SKU. 80 to 100 words.
The angle is "what changed when we switched to <ingredient>".
```

You should see Claude autoload `write-in-brand-voice`. If it autoloads the wrong skill, or no skill at all, your description is too vague. Open the file, sharpen the description, retry.

When it runs, watch the source list at the bottom. It should name actual files from your `voice-dna/` folder (or your homepage URL if voice-dna was empty). If the output sounds generic, the founder asks the question the workshop is built around: which source was thin? Then fix that source.

Try one more, with your own banned words. Open CLAUDE.md, pick 3 or 4 words from your "never" list, and drop them into a corporate-sounding sentence. Ask Claude to rewrite it in your voice:

```
Rewrite this paragraph in our voice:
"<a sentence stuffed with 3 or 4 of your own banned words>"
```

If your banned words survive the rewrite, your skill's brand safety pass is not biting. Either the skill body does not read the never-list, or the never-list in CLAUDE.md is empty. Fix whichever is broken.

Reply ✅ in the workshop chat when your skill autoloads and produces copy that names its sources.

---

## Step 3: Run Market Analyst (~25 min)

In Claude:

```
Look at the competitors I named in CLAUDE.md. For each, gather what's
changed in the last 15 days on pricing, positioning, content cadence,
organic and paid presence. Tell me where they beat us and where we
beat them. Save the report to my-work/market-analyst/.
```

Claude autoloads the `market-analyst` skill. You will see it:

1. Read CLAUDE.md (especially Section 6, your competitor list)
2. Echo back the scope: which competitors, in which category, with which customer reference, and the timeframe (default: last 15 days)
3. Ask "Look right? (yes / change list / change scope / change timeframe)", confirm or adjust
4. Research each competitor inside the timeframe (with a one-line baseline so the report still reads standalone)
5. Save the report to `my-work/market-analyst/<today>-intel-report.md`
6. Offer a 3-option menu: done, rerun with edits, dig deeper on one competitor

While it runs (a few minutes), it will surface findings. You can interject ("Add Brand X who I noticed is now in our aisle") or let it complete. If the first read covers too much old ground, pick `rerun with edits` at the end and tighten the timeframe (e.g. "last 7 days").

When done, open the report:

```
Show me the executive read in 5 lines and the patterns across the set.
```

This is your competitive intel. Reply ✅ in the workshop chat when your report is saved.

---

## Step 4: Run Voice of Customer (~25 min)

In Claude:

```
Mine my customer reviews and support tickets from the last 15 days for
themes, sentiment and persona signals. The data is in my brand-brain
folder. Save the report to my-work/voice-of-customer/.
```

Claude autoloads the `voice-of-customer` skill. It will:

1. Read CLAUDE.md (especially Section 5, your customer)
2. Ask where the data is: pasted block, CSV file path, Drive folder, Gmail
3. Confirm volume and the timeframe ("I see ~67 messages from the last 15 days, mixing reviews and tickets. Right? (yes / change scope / change timeframe)"). If the inputs have no dates, it asks whether to filter by recency rank or skip the filter
4. Cluster into themes
5. Cut sentiment by SKU, by channel, by customer cohort
6. Build 2 to 3 persona cards from the actual data
7. Strip PII (phone numbers, full names, emails) before saving
8. Save to `my-work/voice-of-customer/<today>-voc-report.md`
9. Offer a 3-option menu: done, rerun with edits, dig deeper on one theme or persona

When done:

```
Show me the top 5 reads and the discrepancies-with-CLAUDE.md section.
```

The discrepancies section is the most valuable part. Wherever the data contradicts what you believe about your customer, the skill flags it with the message count. **Edit CLAUDE.md right now to fix any clear gap.** Do not "later". The next time you run any teammate, the updated CLAUDE.md changes the output.

Reply ✅ when your VoC report is saved.

---

## Step 5: Install two skills from the Anthropic marketplace (~5 min)

You built one skill yourself. Two more are sitting in this repo. The third way to acquire a skill is to install it off the shelf from a marketplace. You are going to install two now because they pay off later in this workshop.

- **`frontend-design`** gives Claude real design knowledge: layouts, typography, visual hierarchy. Session 7 (Storefront / Marketplace) produces sharper PDPs and landing page copy with this loaded. Your `write-in-brand-voice` skill also writes tighter web copy when this is active.
- **`document-skills`** is a bundle: `.pptx`, `.docx`, `.pdf`, `.xlsx`, plus design helpers. Session 6 (Performance Marketer) drops creative briefs as decks. Session 10 (Capstone) builds the founder pitch deck. Day-to-day, every contract, invoice and investor doc passes through these.

Both come from official Anthropic marketplaces, but they live in two separate repos. `frontend-design` is in `anthropics/claude-code`. `document-skills` is in `anthropics/skills`. You add both marketplaces once, then install each plugin from the right one. We are not using third-party directories in this workshop.

**Two ways to install. Pick whichever feels natural:**

**Option A, interactive menu (recommended for first-timers):**

Type `/plugin` by itself. Claude Code opens a menu. Add both `anthropics/claude-code` and `anthropics/skills`, then install `frontend-design` from the first and `document-skills` from the second.

**Option B, typed commands (faster if you know what you want):**

```
/plugin marketplace add anthropics/claude-code
/plugin marketplace add anthropics/skills
/plugin install frontend-design@claude-code-plugins
/plugin install document-skills@anthropic-agent-skills
```

After install, exit and restart Claude (`/exit` then `claude`). Plugins load at session start, so they will not work in the session where you installed them.

**Verify both are active:**

```
/frontend-design
```

Then ask Claude:

```
Confirm you have frontend-design and document-skills loaded. List what
document-skills gives you.
```

If Claude confirms both, you are set for the rest of the workshop. If not, `/exit` and restart Claude one more time.

**The frame.** You now know three ways to acquire a skill. Write one from scratch (Step 2). Run pre-shipped ones that came with the repo (Steps 3 and 4). Install from the official Anthropic marketplace (this step). Every skill you add makes Claude more useful for YOUR brand.

---

## What You Just Built

A skill of your own, two reports on your actual brand, and two marketplace skills installed for the rest of the workshop. The three repo skills are not single-use. You can re-run them any week. They get sharper as your data deepens, and `write-in-brand-voice` gets sharper every time you add a file to `brand-brain/voice-dna/`.

The skills also show the contrast that makes Claude Code different from a chat tool:
- ChatGPT can write good prompts but you re-paste them every time
- Claude Code's skills system means the playbook is permanent, version-controlled in your repo, autoloaded on the right intent

The first one you built is the proof that this is a thing you own. The two pre-shipped ones (Market Analyst, Voice of Customer) are reference depth, not magic. You can read their SKILL.md files, edit them, fork them. This is the thing competitors structurally cannot ship: a system that remembers your brand, your customers and your category across every conversation, that you can change yourself.

---

## What's Next

Session 3 connects Shopify, Drive and Gmail via MCPs. The same skills you just ran will read live data instead of paste-in. You will see the second run is visibly sharper than the first.

[Continue to Session 3: MCPs →](session-3-mcps.md)

---

## If You Get Stuck

| Symptom | Fix |
|---|---|
| Your `write-in-brand-voice` skill does not autoload | Open `.claude/skills/write-in-brand-voice/SKILL.md`. The description is too vague or missing the trigger phrases you actually use. Add 3 to 5 phrases from how you really talk and retry. |
| `/frontend-design` does not respond after install | You did not restart Claude. Plugins load at session start. `/exit` then `claude` to restart. Try again. |
| Output from `write-in-brand-voice` sounds generic | The voice samples are thin. Either `voice-dna/` is empty and the fallback URL is a generic homepage, or the samples you pasted are themselves AI-written. Add 2 to 3 raw samples (a real email you sent, a real caption) to `voice-dna/`. |
| Skill does not autoload (Market Analyst, VoC) | Type `@market-analyst` to invoke explicitly, or rephrase the prompt closer to "competitor research", "what is brand X doing", "where do we lose to competitors". |
| Market Analyst or VoC report covers too much old ground, reads like a generic profile | The timeframe was left at the 15-day default but you wanted tighter. At "Look right?", say `change timeframe` and set the window (e.g. "last 7 days"). Or pick `rerun with edits` from the menu at the end and tighten then. |
| Paste hits a token limit | Save the data to `resources/customer-data.csv`, point the skill at the file path. |
| VoC output sounds generic | Sample under 30 messages. Acknowledged limitation. Re-run after Session 3 with MCP-fed data. |
| Market Analyst output reads thin on paid ads | Meta Ad Library access not configured. The report flags the gap. Pick it up in Session 3 if you connect a Meta MCP, or take-home. |
| Compliance flags raised on every theme | Regulated category. Read the flags as "things customers say that need substantiation". That list is gold. |
| You see PII in the saved VoC report | Stop. Tell Claude "you missed PII in {section}, strip and re-save". The skill should have stripped it; if it did not, flag the gap. |

For anything not on this list, raise hand in the workshop chat.
