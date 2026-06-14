[← Back to Session 0: Setup](session-0-setup.md)

---

# Hello Claude Practice Lab (Optional)

**Skill unlocked:** file reading, file creation, file editing, slash commands, permissions, workspace hygiene, conversation flow

---

## What You'll Build

- [ ] Read and explore real D2C brand files using Claude Code
- [ ] Create new documents and clean up messy ones
- [ ] Master the slash commands and controls that make you fast
- [ ] Set up a clean workspace habit that prevents headaches later
- [ ] Learn the prompting patterns that get great results (and the ones that don't)

## The big idea

Claude Code reads, writes and edits files on your machine. You tell it what you need in plain language, it does the work, you stay in control.

## Learning Goals

- **Read and comprehend** — See how Claude reads entire files, connects information across documents, and answers questions about your brand content
- **Create and edit** — Experience Claude writing new files and improving existing ones, with you approving every change
- **Control the tool** — Learn the slash commands, permissions and shortcuts that keep your workflow smooth
- **Organize your workspace** — Build the folder hygiene habit that prevents the #1 source of confusion with Claude Code

## Getting Started

This lab uses the **Little Lab** sample brand that ships in `examples/little-lab/`. Little Lab is a baby skincare D2C brand; the `sample-inputs/` folder has reviews, support tickets, Gmail threads and a Shopify product list — what your own brand data will look like by Session 3.

You should already have Claude Code running in `thecrux-d2c-bootcamp/` from Session 0. Confirm:

```bash
pwd
```

You should see a path ending in `thecrux-d2c-bootcamp`. If not, `cd` back to it and run `claude`.

We will write all lab outputs to `my-work/practice/` so they do not collide with the real teammate folders you build later.

---

## Part 1: First Flight — Read and Explore

The goal here is simple: see Claude read and understand your files. Not just list them — actually comprehend what's inside.

### Step 1: Read a single file

Start by asking Claude to read Little Lab's review export.

```
Read examples/little-lab/sample-inputs/reviews-export.csv and give me a 5-line summary
of what customers are saying. Group it by what's working vs what's not.
```

Claude will read the file and summarise — the cradle cap balm wins, the ingredient transparency praise, the 2-in-1 wash lather complaints, the Tier-2 delivery delay frustration. Notice it does not just quote rows back. It synthesises.

### Step 2: Explore the whole folder

Now ask Claude to look at everything.

```
Look at every file in examples/little-lab/sample-inputs/ and tell me what data is here.
What can I learn about this brand from these files?
```

Claude will sweep through the reviews CSV, the support tickets CSV, the Gmail threads and the Shopify products CSV — and give you a map of the brand's customer voice and product mix. Different files, same patterns.

### Step 3: Ask a cross-file question

This is where it gets interesting. Ask something that requires connecting dots across files.

```
The reviews for SKU LL-BHW-250 mention the product "doesn't lather." Cross-check this
against support-tickets.csv and gmail-support-threads.md. How often does this pattern
show up? What is the customer actually worried about?
```

Claude will link the negative reviews ("Doesn't lather at all. Coming from Sebamed this feels like water.") to the matching support ticket ("Is this product working?") and the longer Gmail thread where the customer asks if the bottle is defective. The pattern is consistent: customers conditioned on SLS-based shampoos are reading "no lather" as "broken product." A single insight that lives across three files, surfaced in seconds.

> **What just happened?** You did not copy-paste anything. You did not open a single file yourself. Claude read a folder of brand data, understood the business context — a baby skincare brand where some SKUs land hard (cradle cap balm, recommended by paediatricians) and others (the SLS-free 2-in-1 wash) get misread as defective — and answered a question that required synthesising across documents. This is what "AI-assisted work" actually looks like.

### Step 4: Beyond files — Claude talks to your computer

Here's where it gets really interesting. Claude Code does not just read files — it can access your underlying operating system. It can run terminal commands, inspect your system, and answer questions about your actual machine.

Try these — one at a time:

**Check your battery health:**

```
Show me the health of my battery — current charge, cycle count, and overall condition
```

Claude will run the appropriate system command, read the output, and explain it in plain English. No googling for terminal commands. No Stack Overflow.

**Find what's straining your computer:**

```
Which services are consuming the most CPU right now? Is anything straining my computer?
```

**Search across your system:**

```
Search my system and find my user profile — where are my documents, downloads, desktop?
Give me a map of my home directory.
```

**Check your downloads folder:**

```
How much space is my Downloads folder taking up? What are the biggest files in there?
```

**Find duplicates:**

```
Are there any duplicate files in my Downloads folder? Files with the same name or
same size that might be copies.
```

**Audit your applications:**

```
What software or applications got installed on my computer in the past 90 days?
```

```
What are the applications on my computer that I haven't used in the last 90 days?
```

This one's gold for a digital cleanup. Claude will find the apps collecting dust.

> **What just happened?** Claude is not a chatbot trapped in a text box. It has access to your operating system. It can run any terminal command, read the output and explain it. You did not need to know a single terminal command — you asked in plain English and Claude figured out the right commands to run. This is the real power: Claude as your system-aware assistant.
>
> **A note on permissions:** Claude asks permission before running system commands, just like it does for file edits. Always read what it is proposing to run. For these exercises, everything is safe — but the habit of reviewing before approving matters.

---

## Part 2: Claude Takes Action — Create and Edit

Reading is impressive. But now we let Claude write. This is where you'll see the permission model in action — Claude proposes changes, and you decide whether to approve them.

### Step 1: Create a new document

Ask Claude to produce something new from the review data.

```
Create a file at my-work/practice/customer-themes.md with a clean, one-page customer
voice summary based on examples/little-lab/sample-inputs/reviews-export.csv. Group into:
"What's working", "What's not working", "Pre-purchase friction". Add a verbatim customer
quote for each point.
```

Claude will draft the file and show you what it wants to write. You'll see a prompt asking you to approve the file creation. Read what it is proposing, then approve. (Claude will create the `my-work/practice/` folder if it does not exist — that is where your lab outputs live, separate from your real teammate work.)

### Step 2: Improve an existing document

The Gmail thread responses are functional but not on-brand. Ask Claude to strengthen one.

```
Read examples/little-lab/sample-inputs/gmail-support-threads.md. Take Thread 1 (the
lather question) and rewrite the support team's response. Acknowledge the Sebamed
comparison directly, explain why SLS-free formulations do not lather, and turn the
moment into a brand-building reply. Keep it warm, short, and never apologetic about
the formulation choice.
```

Claude will show you the proposed edits. Pay attention — it is modifying an existing file. You can see exactly what changes it wants to make before you say yes.

### Step 3: Clean up messy data

The support tickets CSV is flat — every ticket gets equal weight. Ask Claude to organise it.

```
Read examples/little-lab/sample-inputs/support-tickets.csv and create an organised
version at my-work/practice/tickets-prioritised.md. Group by urgency (respond today /
this week / FYI), tag each with category (delivery / product confusion / pre-purchase /
positive followup), and flag any pattern that repeats across more than two tickets.
```

### Step 4: Undo it — Reverting changes

You just watched Claude edit a file. But what if you did not like the changes? What if Claude went too far, or you want the original back?

This is where `/rewind` comes in. It is your undo button — not just for the conversation, but for the files too.

Try it now:

```
/rewind
```

You will see a list of previous points in your conversation. Use the arrow keys to pick the moment *before* Claude edited `gmail-support-threads.md` (Step 2). When you select it, Claude will ask if you want to **also undo the file changes** made after that point. Say yes.

Now check the file:

```
Read examples/little-lab/sample-inputs/gmail-support-threads.md — is this the original
version or the edited one?
```

It is back to the original. The edits are gone. You just time-travelled.

**When to use `/rewind`:**
- Claude edited a file and you do not like the result
- You went down the wrong path three prompts ago and want to back up
- You approved something by accident and want to undo it

**`/rewind` vs `/clear`:** `/clear` wipes your conversation but leaves files as they are. `/rewind` goes back to a specific point and can undo file changes too. `/rewind` is surgical; `/clear` is a reset.

> **What just happened?** Claude created a new file, edited an existing one, transformed messy ticket data into something structured — and then you learned to undo it all. Every change Claude makes is reversible. You are never locked in. The permission model means Claude proposes and you approve. `/rewind` means even after you approve, you can take it back. You are always in control.

---

## Part 3: Your Control Panel — Commands, Permissions, and Workspace

Now that you know Claude can read and write, let's learn the full control panel. This is what separates someone who "uses Claude" from someone who is *fast* with Claude.

### Essential Slash Commands

Try each of these right now:

**`/help` — See everything available:**

```
/help
```

This shows you every command Claude Code supports. Scan it. You do not need to memorise it — just know it is there.

**`/cost` — Check your session spend:**

```
/cost
```

Shows token usage for this session. Good habit to build.

**`/usage` — Check your plan limits:**

```
/usage
```

This is different from `/cost`. `/cost` shows this session's tokens. `/usage` shows your overall plan limits and rate status — how much of your daily or weekly quota you've used. Check this if Claude suddenly feels slow (you might be rate-limited).

**`/context` — See what's eating your context:**

```
/context
```

This shows a visual grid of your context window — how much is filled, what's taking space. When Claude starts feeling "forgetful" or slow, this tells you why. If it's nearly full, time to `/compact` or `/clear`.

**`/compact` — Compress your conversation:**

```
/compact
```

This summarises your conversation history to free up context space. Claude keeps the key points but drops the verbose details. Use this when your context grid looks full.

**`/clear` — Fresh start:**

```
/clear
```

Wipes the conversation completely. Claude forgets everything. Use this when Claude seems confused, when you are switching tasks, or when you want a clean slate. Your files are untouched.

**`/model` — Switch models or adjust effort:**

```
/model
```

This lets you switch between different Claude models. You will see a list — use arrow keys to select. Some models also support **effort levels** (use left/right arrows to adjust).

**Try this experiment** to see the difference:

First, ask Claude a question at normal settings:

```
Based on examples/little-lab/sample-inputs/reviews-export.csv and support-tickets.csv,
what is the single biggest growth risk for this brand right now?
```

Note the answer and how long it took. Now switch to a faster, lighter model:

```
/model
```

Select **Haiku** (the fastest model) from the list. Then ask the exact same question. You will notice: Haiku answers in a fraction of the time, but the analysis is shallower. It might catch the obvious risk (the 2-in-1 wash lather complaints) but miss the nuance — that the Sebamed/Mamaearth switching pattern means churn risk is in customer mental models, not the product itself.

Now switch back:

```
/model
```

Select **Sonnet** or **Opus** (whichever you started with).

**The mental model:**
- **Haiku** — Fast, cheap. Great for quick lookups, simple formatting, "what's in this file?" questions
- **Sonnet** — Balanced. Good default for most work
- **Opus** — Most thorough. Use for complex analysis, cross-file reasoning, important deliverables

You do not need to switch models constantly. But knowing you CAN is powerful — especially when you are burning through your daily quota on simple tasks Haiku could handle.

**`/doctor` — Self-diagnose problems:**

```
/doctor
```

If something feels broken — Claude won't launch, commands don't work, connections fail — run `/doctor`. It checks your installation, settings and connectivity and tells you what's wrong.

### Understanding Permissions

When Claude wants to read a file, create a file, edit a file or run a command, it asks you first. This is the permission model. You have already seen it in Part 2.

Check your current permission settings:

```
/permissions
```

You will see what Claude is currently allowed to do. There are different levels:

- **Ask every time** — Claude asks permission for each action (default for most things)
- **Allow for this session** — You approve once, Claude can repeat similar actions without asking again
- **Always allow** — Permanent permission for this type of action in this project

For now, stick with the defaults. As you get comfortable, you'll learn when it makes sense to give broader permissions.

> **Tip:** When Claude asks permission and you see the options, look carefully. You might see "Allow once", "Allow for session", or "Always allow". During this workshop, "Allow once" or "Allow for session" is fine. Don't "Always allow" until you're confident about what you are approving.

### Sandbox Mode — The Safety Net

```
/sandbox
```

Sandbox mode restricts Claude from making changes to your file system. It can read files and answer questions, but it cannot create, edit or delete anything. Think of it as "read-only mode."

**When to use sandbox:**
- When you are exploring files and do not want accidental changes
- When you are working with important files and want to be extra careful
- When you just want to ask questions without Claude touching anything

Toggle it on, ask a question, toggle it off when you are ready to let Claude take action again.

### Keyboard Controls

| Key | What it does |
|-----|-------------|
| `Escape` | Cancel Claude mid-response |
| `Ctrl+C` | Hard stop / exit Claude |

Try this now — ask Claude something long and hit `Escape` while it is responding:

```
Write me a very detailed 2000-word analysis of the entire Little Lab review corpus
```

Hit `Escape` after a few seconds. Claude stops immediately. Nothing gets saved. You are in control.

### Multi-turn Conversations

Claude remembers your conversation. You do not need to repeat yourself. Try this sequence:

```
Summarise the top 3 customer concerns from examples/little-lab/sample-inputs/reviews-export.csv
```

Wait for the response. Then:

```
Now do the same thing but for support-tickets.csv
```

Claude knows "the same thing" means "summarise the top 3 customer concerns." It carries context forward. This is how you work fast — build on previous responses instead of starting from scratch.

### Correcting Claude

If Claude gives you something that's not quite right, do not re-prompt from zero. Just redirect:

```
Make it shorter — one line per concern, no explanations
```

Or be specific about what to change:

```
No, drop the third point and add something about the Tier-2 delivery delays instead
```

Claude takes direction well. Treat it like a sharp colleague who drafted something — you'd say "change this part," not repeat the whole brief.

> **What just happened?** You now know the full control panel: commands to check usage (`/cost`, `/usage`, `/context`), commands to manage your session (`/clear`, `/compact`), commands to control Claude (`/model`, `/permissions`, `/sandbox`), and commands to troubleshoot (`/doctor`). Plus keyboard controls and multi-turn conversations. You are not a passenger any more — you are the pilot.

---

## Part 4: The Gotcha Guide — Best Practices

This is the part that saves you frustration for the rest of the weekend.

### Workspace Hygiene — The #1 Habit

**The rule: always run Claude inside `thecrux-d2c-bootcamp/`. Never from your home directory or desktop.**

Why this matters:
- Claude reads files in your current directory. If you are in your home folder, it might read things you do not want it to.
- Each project folder can have its own `CLAUDE.md` (you build yours in Session 1), giving Claude different context for different projects.
- When something goes wrong, the first question is always "where am I?" — `pwd` — and a clean structure makes the answer obvious.

**The habit:** Before starting any Claude session:

```bash
pwd                          # Where am I?
cd ~/path/to/thecrux-d2c-bootcamp   # Go there if you are not already
claude                       # Then start Claude
```

You will thank yourself later. Every "file not found" error and every "Claude is reading the wrong files" confusion almost always traces back to running from the wrong directory.

### Do This, Not That

**1. Be specific, not vague**

Bad prompt:

```
Look at the csv
```

Good prompt:

```
Read examples/little-lab/sample-inputs/reviews-export.csv and flag any rating-3-or-lower
review that mentions a competitor brand by name. I want to know which competitors my
unhappy customers are comparing me against.
```

Try both. See the difference in what you get back.

**2. Give context — it changes everything**

Without context:

```
Summarise the lather complaints
```

With context:

```
Summarise the lather complaints across reviews and support tickets. I am the founder
of Little Lab, a baby skincare brand. SLS-free formulation is a deliberate choice tied
to ingredient transparency. I want to know: how big is this issue, and is the problem
the product or the customer's expectation?
```

The second prompt gives Claude a lens. It knows what matters to you. Try both and compare the outputs.

**3. Iterate, do not restart**

When Claude gives you a draft that's 80% right, do not write a brand new prompt. Build on it:

```
Good, but make the recommendation section more decisive. I do not want "consider" —
I want "we should do X because Y."
```

```
Add a one-paragraph risk section at the end.
```

```
Make the tone match Little Lab's voice — paediatrician-credible, not babying the parent.
```

Each follow-up is a 5-second prompt that gets you closer. Restarting from scratch wastes context and time.

**4. Use /clear when Claude seems stuck**

If Claude starts repeating itself, giving circular answers, or seems confused — do not keep pushing. Clear and start fresh.

```
/clear
```

**5. Check your directory — always**

If Claude says it cannot find a file:

```
pwd
```

You should see your `thecrux-d2c-bootcamp` directory. If you do not, `cd` back to it. Ninety percent of "Claude cannot read my file" problems are directory problems.

**6. Approve carefully**

When Claude proposes a file edit, read what it is changing. Especially when it is modifying existing files. If something looks off, say so — "Do not change the price column, only update the description."

### Commands to Avoid (For Now)

Claude Code has many slash commands. Some are powerful but not relevant yet — they will be covered in later sessions. **Do not worry about these today:**

| Command | Why to skip it for now |
|---------|----------------------|
| `/hooks` | Covered in Session 8 (Ops + Retention) |
| `/mcp` | Covered in Session 3 (MCPs) |
| `/agents` | Covered in Session 4 (Content Lead subagent) |
| `/skills` | Covered in Session 2 |
| `/review`, `/pr-comments` | Developer / code review tools, not relevant for this workshop |
| `/init` | Creates a CLAUDE.md — you do this properly in Session 1 via `/interview-me` |

If you accidentally type one of these, no harm done. Just `/clear` and move on.

### Commands You Should Never Approve

Claude can propose terminal commands to interact with your computer. Most are safe, but some are destructive. **If Claude proposes any of these, stop and think before approving:**

| Command | What it does | Why it's dangerous |
|---------|-------------|-------------------|
| `rm -rf` / `rm -r` | Deletes files or folders permanently | No recycle bin. Gone forever. |
| `sudo ...` | Runs anything as administrator | Full system access. One wrong command can break your OS. |
| `chmod 777` | Opens file permissions to everyone | Security risk — makes files readable/writable by anyone. |
| `mv` to unknown locations | Moves files somewhere | You might lose track of where your file went. |
| `curl ... \| bash` | Downloads and runs code from the internet | Executes unknown code on your machine. Never do this blindly. |
| `kill -9` / `killall` | Force-stops applications | Can cause data loss in apps that have not saved. |
| `diskutil` / `dd` | Low-level disk operations | Can erase or corrupt your entire drive. |
| `defaults write` | Changes macOS system settings | Can break system behaviour in subtle, hard-to-undo ways. |
| Any command you do not understand | — | If Claude proposes a command and you do not know what it does, **ask Claude to explain it first**. |

Claude is powerful and generally safe — the permission model means nothing runs without your approval. But your approval is only as good as your attention. The golden rule: **When in doubt, ask Claude: "What exactly will this command do? Is it reversible?" before approving.**

> **What just happened?** You now have the workspace habit (always work inside `thecrux-d2c-bootcamp/`), six prompting rules, you know which commands to use now vs later, and you know which terminal commands to watch out for. These patterns apply to every session for the rest of the weekend.

---

## What You Built

- [x] Read files and answered cross-file questions about a real D2C brand
- [x] Created new documents from existing content
- [x] Edited and improved drafts with Claude proposing and you approving
- [x] Understood permissions (`/permissions`) and sandbox mode (`/sandbox`)
- [x] Used keyboard controls: `Escape` to cancel, `Ctrl+C` to stop
- [x] Practiced multi-turn conversations and correcting Claude
- [x] Compared bad prompts vs good prompts
- [x] Learned workspace hygiene — always work in `thecrux-d2c-bootcamp/`

---

## Take It Home

### Quick Reference — Slash Commands

**Session management:**

| Command | What it does | When to use it |
|---------|-------------|----------------|
| `/help` | Shows all commands | When you forget what's available |
| `/clear` | Wipes conversation | When Claude is confused or you are switching tasks |
| `/compact` | Compresses context | When conversation is long and Claude is slowing down |

**Monitoring and awareness:**

| Command | What it does | When to use it |
|---------|-------------|----------------|
| `/cost` | Session token usage | To track this session's spend |
| `/usage` | Plan limits and rate status | To check if you are rate-limited |
| `/context` | Visual context grid | To see how full your context window is |

**Control:**

| Command | What it does | When to use it |
|---------|-------------|----------------|
| `/model` | Switch model or effort level | When you want faster or deeper responses |
| `/permissions` | View/change permission settings | To check what Claude can do |
| `/sandbox` | Toggle read-only mode | When you want to explore without changes |
| `/doctor` | Diagnose problems | When something feels broken |
| `/rewind` | Undo conversation and file changes | When you want to roll back |

### Quick Reference — Keyboard Controls

| Key | What it does |
|-----|-------------|
| `Escape` | Cancel current response |
| `Ctrl+C` | Hard stop / exit |

### The Workspace Rule

```
Always: cd into thecrux-d2c-bootcamp → claude
Never: run claude from ~ or Desktop
```

### The 6 Prompting Rules

1. **Be specific** — Tell Claude exactly what you want, not just what to look at
2. **Give context** — Who are you, what brand, what matters to you
3. **Iterate** — Build on responses, do not restart from scratch
4. **Clear when stuck** — `/clear` is your reset button
5. **Check your directory** — `pwd` solves most "file not found" problems
6. **Approve carefully** — Read the changes before you say yes

---

## If You Finish Early

**Try these stretch prompts to push further:**

```
Read every CSV in examples/little-lab/sample-inputs/ and write a 1-page "Customer Voice"
brief at my-work/practice/customer-voice-brief.md. Cover: top 3 things working, top 3
things not, the single SKU that needs the most attention right now, and one
"pre-purchase friction" insight a content marketer could turn into a landing page.
```

```
Read examples/little-lab/sample-inputs/reviews-export.csv and shopify-products.csv.
For each SKU, calculate: average rating, share of negative reviews, and units sold
in the last 28 days. Flag any SKU where rating is high but units are low — those
are the ones content could rescue.
```

```
Compare patterns across reviews-export.csv, support-tickets.csv and gmail-support-threads.md.
Are there any customer concerns that show up in two channels but not the third? Those
are the ones you would miss if you only read one source.
```

```
Read examples/little-lab/sample-inputs/gmail-support-threads.md and draft a response
template for the "lather concern" pattern. The template should never apologise for
the SLS-free choice but should make the customer feel heard. Save it at
my-work/practice/lather-response-template.md.
```

---

> **Key Takeaway:** Claude Code is not magic and it's not a search engine. It's a capable collaborator that reads your files, understands your context, and does the work — with you making every decision. The better you communicate what you need, the better it performs. That's the skill you just started building.
