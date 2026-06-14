[← Back to Student Handbook](student-handbook.md)

---

# Session 0: Setup

**Skill unlocked:** Claude Code running in your terminal, on your laptop, ready to read and write your repo.

---

## What You'll Have After This Session

1. Claude Code installed and logged in
2. The workshop repo cloned to your laptop
3. A 5-minute look at VS Code (the visual alternative)
4. A 2-minute mention of Claude Desktop
5. Claude reading the files in your repo, ready for Session 1

---

## Before You Start

You should have completed the pre-work at **thecrux.ai/prework-d2c**. If you did, you have:

- Claude Code installed (npm or homebrew)
- The repo cloned at `thecrux-d2c-bootcamp/`
- Your Anthropic key set up (or `claude login` done)
- A `brand-brain/` folder with your reviews, competitor notes and (optional) support tickets

If any of this is missing, raise hand now. A TA pairs with you while the cohort moves on. You have 30 minutes; you will be caught up.

---

## Step 1: Open the terminal (1 min)

A terminal is just a chat surface. You type, it replies. The chat partner today is `claude`.

Open your terminal:
- **macOS**: Cmd-Space, type "Terminal", enter
- **Windows**: Open **PowerShell** (search "PowerShell" in the Start menu — the blue terminal).
- **Linux**: whatever terminal you have

You will see a `$` or `>` prompt. That is where you type.

---

## Step 2: Open the repo and start Claude (2 min)

```bash
cd ~/thecrux-d2c-bootcamp
ls
```

You should see folders: `.claude/`, `references/`, `examples/`, plus files like `student-handbook.md` and `CLAUDE.template.md`.

Now start Claude:

```bash
claude
```

You see Claude's welcome screen. You are now talking to Claude in the context of this repo.

Type:

```
What is in this repo? What are we doing today?
```

Claude reads `student-handbook.md` and the directory structure. The reply should mention the 11 sessions and the four primitives. This is the first "Claude knows what is going on" moment.

---

## Step 3: The VS Code flip (5 min)

**Visual Studio Code** is the visual alternative to Claude Code. Same Claude. Same files. Different surface.

It has:
- A visual file tree
- A chat panel (via the Claude Code extension)
- The same prompts you would run in terminal, just with a window

---

## Step 4: Claude Desktop (2 min)

There is also **Claude Desktop**, the chat app. Use it for short asks ("summarise this PDF", "draft a tweet"). It does not have skills, subagents or MCPs the way Claude Code does. We do not use it today.

You may have used Desktop already. You now know why we are not using it for the workshop. Move on.

---

## Step 5: Repo walk (5 min)

Back in your terminal:

```bash
ls
```

You see the Day 1 session files (`session-0-setup.md` through `session-5-integration.md`, plus the `session-telegram.md` add-on), the `student-handbook.md`, the `CLAUDE.template.md` and supporting folders. Open one:

```
Read session-1-brand-brain.md and tell me in 5 lines what Session 1 will produce.
```

Claude reads the session file and gives you the gist. You now know what is coming next.

Quick tour of the assets at the repo root:

```bash
ls .claude/
```

You see:
- `commands/` (slash commands you run by name, like `/interview-me`)
- `skills/` (skills Claude autoloads when relevant)
- `agents/` (subagents you spawn for big jobs)

These are the four primitives in physical form. We use them across the next 11 sessions.

---

## Step 6: The permission model (1 min)

Before you go further, notice how Claude has been behaving. When it wants to read a file, you let it read. When it wants to write, move or delete a file, it asks first. You approve, deny or modify the proposed action.

This is how Claude Code always works. It is not autopilot. It is a fast colleague who checks with you before acting. Today you will say yes a lot, and quickly. But the guardrail is always there.

If Claude does something you did not want, tell it. "No, do not change the price." "Roll back that edit." That is how you will work with it all weekend.

---

## Step 7: Confirm in chat (5 min buffer)

Reply ✅ in the workshop chat when:
- You see Claude running in `thecrux-d2c-bootcamp/`
- You can run `ls` and see the day-1 / day-2 / .claude folders

Stragglers get TA help. We start Session 1 when 100% of the cohort has confirmed.

---

## Want more reps before Session 1?

The [Hello Claude Practice Lab](hello-claude-practice-lab.md) walks you through reading files, creating documents, slash commands (`/cost`, `/context`, `/compact`, `/model`, `/rewind`), permissions, sandbox mode and workspace hygiene — using the little-lab sample data. Self-paced. Run it during a break, or come back to it after the workshop.

> **Checkpoint: Session 0 complete**
>
> - [ ] Terminal open, Claude Code running in `thecrux-d2c-bootcamp/`
> - [ ] You have seen VS Code (the visual alternative) and know why we run terminal today
> - [ ] You understand the permission model: Claude proposes, you approve
> - [ ] You can read Session 1 (Brand Brain) and know what's coming

---

## What's Next

Session 1 produces a CLAUDE.md in your voice. It is the file every later session reads first. Every minute we invest in Session 1 makes every later session sharper.

[Continue to Session 1: Brand Brain →](session-1-brand-brain.md)

---

## If You Get Stuck

| Symptom | Fix |
|---|---|
| `claude: command not found` | See `references/module-0-setup/troubleshooting.md` step 1 |
| `claude` runs but asks for API key every time | `claude login` opens a browser; sign in. See troubleshooting step 2. |
| Repo did not clone | Download as ZIP from the repo URL. See troubleshooting step 3. |
| On Windows, things behave weirdly | Make sure you are in **PowerShell** (not CMD), and that you opened it fresh after installing tools so PATH is current. |
| Claude says "I don't have access to read these files" | You are in the wrong directory. `cd ~/thecrux-d2c-bootcamp && claude`. |

For anything not on this list, see `references/module-0-setup/troubleshooting.md` or raise hand.
