[← Back to Student Handbook](student-handbook.md)

---

# Add-on Session: Telegram Bot

> **Prerequisite:** Session 2 (Skills) complete. You have `/write-in-brand-voice` installed and working in Claude Code.

---

## What You Unlock

A Telegram bot that routes every message to your skills. `/write-in-brand-voice` and any skill you add later, all from a DM on your phone. Plain-English questions work too, answered with full CLAUDE.md context.

---

## How This Works (2 min, read don't type)

The bot is a ~40-line Node.js process. It does one thing: when a Telegram message arrives, it runs `claude -p "<message>"` as a subprocess and sends the output back to Telegram. That is it.

**All the intelligence lives in your skills.** The bot does not know what `/write-in-brand-voice` does. It does not have a prompt for any specific skill. It just forwards the message and returns the response.

**Why this matters:**

- Every new skill you build drops into your phone immediately. No bot code to update.
- Bot code stays under 60 lines. If something breaks, it is readable.
- The "Claude figures out what the user means" lesson transfers to Telegram. No hardcoded command list.

---

## Step 1: Create Your Telegram Bot

If you did this in pre-work, you have both values ready. Skip to Step 2.

On your phone:

1. Open Telegram, search for **@BotFather** (blue verified checkmark).
2. Send `/start`, then `/newbot`.
3. Name it (e.g., "My AI Team"). Username must end in `bot`.
4. Copy the **bot token** BotFather gives you. Looks like `7123456789:AAH...`.
5. Search **@userinfobot**, send `/start`, copy your numeric **user ID** (looks like `1234567890`).

> **User ID must be a number, not a @username.** This is the #1 crash in past cohorts. `@yourname` does not work. `1234567890` does.

Get both values to your laptop. Telegram Web at web.telegram.org works well.

---

## Step 2: Create .env

In Claude Code:

```
Create a .env file in this directory with my Telegram credentials:
TELEGRAM_BOT_TOKEN=<paste your bot token>
TELEGRAM_USER_ID=<paste your numeric user ID>

Also create a .gitignore that excludes .env if it doesn't already.
```

Replace the placeholders with your real values.

---

## Step 3: Generate the Bot

This is the whole bot. Short, declarative, no baked-in prompts.

```
Build a minimal Node.js Telegram bot at ai_team_bot.js.

SETUP (which Node libraries the bot depends on):
- Reads TELEGRAM_BOT_TOKEN and TELEGRAM_USER_ID from .env using dotenv
- Uses telegraf library
- Runs from this project directory so claude -p inherits CLAUDE.md context

STARTUP VALIDATION (catch the two most common .env mistakes before the bot boots):
- If token is missing or equals "your_bot_token_here", print a clear error and exit
- If user ID is missing or not a number, print:
    "ERROR: User ID must be a number like 1234567890, not a username like @john. Got: [value]"
  and exit

HANDLER (what happens when a Telegram message arrives):
- Ignore all messages from anyone except the configured user ID
- For every text message (slash command or plain text), forward the entire raw message to claude -p
- No per-command branching. No custom prompts. The skills handle routing.

CLAUDE INVOCATION (how the bot runs the claude CLI as a subprocess for each message):
- Use promisified execFile (async, not sync) with a 600 second (10 min) timeout.
  Heavier skills like /market-analyst run multi-stage research and can take
  3-5 minutes; 180s is not enough.
- Pass input: '' in execFile options to suppress the "no stdin data received" warning.
- Command shape:
    claude -p "<message>" --dangerously-skip-permissions \
      --allowedTools "Read,Write,Edit,Glob,Grep,Bash,Agent,WebSearch,WebFetch,mcp__ms365,mcp__gsuite"
- cwd = directory where the script lives

TELEGRAF CONFIGURATION (framework-level timeout and error handling):
- Create Telegraf with handlerTimeout 600000 (must exceed the claude timeout above)
- Register bot.catch() to log errors and reply with a simple error message, so one bad run
  does not kill the whole bot

OUTPUT (how the reply reaches Telegram):
- Show typing indicator via sendChatAction('typing') on a 4-second repeating interval while
  claude runs. Clear the interval when claude returns.
- If output is longer than 4000 characters, chunk at line boundaries and send as multiple
  messages.
- Send each chunk as plain text. Telegram will show claude's Markdown as-is (raw ** and - are
  readable enough for a founder bot; formatting can be added later if needed).

LOGGING (to terminal). Give the operator continuous visual feedback so a long
claude run doesn't look like a hang. Every line starts with a short timestamp
(HH:MM:SS) and a word-label ("inbound", "claude", "reply", "error") so the
stream is scannable. No emojis, no ANSI color, cross-platform safe.
- As early as possible (right after the require()s complete, BEFORE loading
  env vars or validating): log "starting ai_team_bot.js" with the word-label
  "boot". Without this, `node ai_team_bot.js` looks frozen for the 200-500ms
  while telegraf loads and students wonder if it's hung.
- After validation passes: log "config valid. Authorized user: <id>" so the
  operator sees the env checks succeeded before any network work begins.
- Right before bot.launch(): log "connecting to Telegram...". bot.launch() can
  take several seconds on a slow link, and without this line the terminal
  goes silent during that wait.
- Do NOT `await bot.launch()`. In long-polling mode telegraf's launch() promise
  stays pending for the entire life of the bot — it only resolves on shutdown —
  so any logging placed after `await bot.launch()` never runs and the terminal
  looks permanently stuck on "connecting to Telegram..." even though the bot is
  actually connected and answering DMs. Call bot.launch() WITHOUT awaiting it,
  and attach a .catch() to it so a fatal polling error (e.g. 409 Conflict) is
  still logged instead of becoming an unhandled rejection.
- After calling bot.launch() (not awaited): print "AI Team bot ready. Authorized
  user: <id>. Press Ctrl+C to stop." Then `await bot.telegram.getMe()` — unlike
  launch(), this is an ordinary request that resolves immediately — and log the
  connected bot's @username plus the working directory. This confirms the token
  is valid before any DM arrives.
- On each inbound message: log timestamp, username, first 80 chars
  ("inbound | @you: /write-in-brand-voice").
- When claude starts: log "claude | starting...". Start a 15-second heartbeat
  that logs "claude | still running (Ns elapsed)" until the subprocess returns.
  This is critical for heavier skills like /market-analyst (2-5 min) so the
  founder does not Ctrl+C a working bot.
- When claude returns: log total duration in seconds and the character count
  ("claude | done in 38.2s, 1847 chars").
- After replying to Telegram: log the char count and chunk count
  ("reply   | sent (1847 chars, 1 chunk)").
- On errors: log the full stack trace prefixed with "error".

COMMENTS (make the file walkthrough-friendly for a non-engineering audience):
- Top of file: a 2-4 line block comment explaining what this bot does in plain
  English (forwards every Telegram message to `claude -p`, skills do the routing).
- Section headers as single-line comments that mirror the sections above
  ("// --- SETUP ---", "// --- HANDLER ---", etc.) so participants can trace
  the code back to the prompt they pasted.
- One-line comments above any line using jargon participants will ask about:
  promisify, execFile, handlerTimeout, sendChatAction, bot.catch, getMe,
  maxBuffer, SIGINT. Explain WHY the line is there, not WHAT it does.
- Skip comments on self-evident lines (variable reads, the validation
  if-blocks that already print clear error messages). More comments hurt,
  not help.

Also create package.json with telegraf and dotenv as dependencies.
Keep the whole bot under 100 lines (code stays tight; good comments make up the rest).
```

When Claude is done, check the generated file. Should be short. If it is over 120 lines, ask Claude to trim.

### What this prompt actually says

If the prompt above reads like a foreign language, here's the one-line tour. You don't need to understand every line of code Claude generates. You need to know which section to point at when something breaks.

- **SETUP**: two Node libraries. `telegraf` talks to Telegram. `dotenv` reads secrets from `.env` so the bot token is never hardcoded.
- **STARTUP VALIDATION**: catches the two failures past cohorts hit most. A missing or placeholder token, and a user ID typed as `@username` instead of the number.
- **HANDLER**: for every message from you, pass the raw text to `claude -p`. No hardcoded command list. Your skills (`/write-in-brand-voice`, `/brand-brain`, etc.) do the routing.
- **CLAUDE INVOCATION**: run `claude -p "<message>"` as a subprocess. 10-minute timeout because heavier skills like `/market-analyst` legitimately take 3-5 minutes. `--allowedTools` tells that subprocess which tools it may use (files, search, MCP connectors).
- **TELEGRAF CONFIGURATION**: framework timeout plus a global error handler so one bad run does not kill the whole bot.
- **OUTPUT**: show "typing..." on Telegram while waiting, then chunk long replies as plain text (Telegram caps messages at 4096 characters).
- **LOGGING**: live activity stream in your terminal so you can see the bot thinking instead of staring at silence.

### The natural-language version

> **"Wait, can't I just describe this to Claude in plain English?"**
>
> Yes, and you should in your own work. But natural-language prompts usually take 2-3 iterations to converge. First pass almost works. Second pass fixes the timeout. Third fixes the chunking. For a bootcamp where everyone needs a working bot by the end of the session, we've pre-iterated for you. The prompt above is what a curated, production-ready version looks like after those rounds.

The natural-language version you could have written yourself looks something like this:

```
Build me a minimal Node.js Telegram bot at ai_team_bot.js. Read
TELEGRAM_BOT_TOKEN and TELEGRAM_USER_ID from .env. When my user DMs it,
run `claude -p "<message>"` as a subprocess and send the output back.
Ignore everyone else. Chunk long responses under Telegram's 4096-char
limit. Show a typing indicator while claude runs. Log what's happening
so I can see it working. Add comments a non-engineer can follow.
```

Paste that and you'll get a bot. Probably working. Probably missing the 10-minute timeout for heavier skills, the 15-second terminal heartbeat during long runs, the `getMe()` sanity check at startup, the Markdown-to-Telegram conversion that keeps replies from arriving as raw `**`, the graceful SIGINT shutdown that prevents the next launch from hitting a `409 Conflict`. Each of those gaps is a lesson paid for with a failed demo in a past cohort.

**The takeaway.** Natural-language prompts are the right default. Talk to Claude when you're building something new. Curate the prompt when you already know what a good output looks like, or when you need the same output to land on 15 laptops at the same time. Both are real skills. Today we gave you the curated version so you'd finish the session with a working bot, not a half-working one.

---

## Step 4: Install and Run

> **OPEN A NEW TERMINAL WINDOW. DO NOT RUN THIS INSIDE CLAUDE CODE.**
>
> The bot runs as its own long-running process. It cannot share a terminal with Claude Code.
>
> - **Mac:** Cmd+Space, type **Terminal**, press Enter
> - **Windows:** Win key, type **PowerShell** or **Command Prompt**, Enter

In the new terminal:

```bash
cd ~/thecrux-d2c-bootcamp
npm install telegraf dotenv
node ai_team_bot.js
```

Expected output (the second line confirms your bot token actually works):

```
[14:02:11] boot    | starting ai_team_bot.js
[14:02:11] boot    | config valid. Authorized user: 1234567890
[14:02:11] boot    | connecting to Telegram...
[14:02:12] boot    | AI Team bot ready. Authorized user: 1234567890. Press Ctrl+C to stop.
[14:02:12] boot    | Connected as @mybot. Working dir: /Users/you/thecrux-d2c-bootcamp
```

Once you DM the bot, the terminal will show a running activity log, inbound message, "claude | starting...", a 15-second heartbeat while claude works, then the final duration and reply size. Watch that stream so you know the bot is alive. Lightweight skills like `/write-in-brand-voice` return in seconds; heavier ones like `/market-analyst` can take 2-5 minutes.

**Leave this terminal window alone.** This is your bot. Closing it kills the bot.

---

## Step 5: Test From Your Phone

DM your bot on Telegram.

**Test 1: General message**

```
What are our top 3 SKUs and who buys them?
```

Should reflect your CLAUDE.md: brand basics, top SKUs, primary persona. If this works, the bot + CLAUDE.md wiring is correct.

**Test 2: Your Write-in-Brand-Voice skill**

```
/write-in-brand-voice draft a 2-line Instagram caption announcing
that Diwali gifting pre-orders are now open
```

You should get a caption in The Paan Legacy voice (heritage-rooted, plain-spoken, no banned words like "premium" or "gourmet"). This proves skills invoked via `claude -p` work end-to-end.

**Test 3: A question you have not explicitly coded**

```
Where should I focus content this week given Diwali pre-orders open soon?
```

No specific skill handles this. The bot forwards the plain-text message to Claude, and Claude gives a thoughtful answer using your CLAUDE.md context. This confirms the bot handles non-slash messages the same way as slash ones: raw passthrough.

---

## Troubleshooting, Telegram Bot

| Problem | Fix |
|---------|-----|
| Bot crashes on startup with "User ID must be a number" | Your `.env` has `@username` instead of the numeric user ID. Go back to @userinfobot and get the number. |
| `npm install` fails on Windows | Make sure you are in a regular PowerShell or CMD window, not inside Claude Code. If Node is missing, install from nodejs.org. |
| Bot starts but does not respond to phone messages | Check your user ID. The bot ignores everyone except the configured ID. Send a message, check your terminal log. If nothing logs, your user ID in `.env` does not match your phone's ID. |
| `409 Conflict: terminated by other getUpdates request` | Another poller is running against this token. An old `node ai_team_bot.js` is probably still alive in another terminal. Kill it. |
| Typing indicator appears, no response comes | Claude may be taking a long time. Heavier skills like `/market-analyst` commonly run 2-5 minutes. Wait it out. If the bot terminal logs `code: 143` (SIGTERM), your execFile timeout is too low, raise it to 600000 and restart. |
| Response is cut off | Bot should auto-chunk at 4000 chars. If it does not, ask Claude: "Fix the chunking in ai_team_bot.js." |
| `claude: command not found` from bot terminal | Claude CLI is not on PATH in the shell where you ran `node`. Open a fresh terminal and run `which claude` (Mac) or `where claude` (Windows). Then use the full path in the bot script, or fix your PATH. |
| Terminal stuck on "connecting to Telegram..." — "AI Team bot ready" / "Connected as @..." never print | The bot is almost certainly connected and working — DM it to confirm. This happens when the generated code does `await bot.launch()`: in long-polling mode that promise never resolves, so every line after it is skipped. Ask Claude: "In ai_team_bot.js, don't `await bot.launch()` — call it without await (with a `.catch()`) and run `getMe()` separately." |

> **Checkpoint: Bot on your phone**
>
> - [ ] `.env` has bot token and numeric user ID
> - [ ] `ai_team_bot.js` runs without errors
> - [ ] General messages reflect CLAUDE.md context
> - [ ] `/write-in-brand-voice` produces a caption in The Paan Legacy voice
> - [ ] Non-slash questions get thoughtful answers

---

**Next:** [Student Handbook →](student-handbook.md)
