# Telegram Bot — Formatting Fix Prompt

Your Telegram replies are showing raw Markdown (literal `**`, `#`, and `` ` ``)
instead of reading like a normal chat. This prompt fixes that.

## How to use
1. Open Claude Code **inside your bot's project folder** (where `ai_team_bot.js` lives).
2. Copy everything between the two lines below and paste it into Claude.
3. Let it make the change, then restart your bot.

---

⬇️⬇️⬇️ START COPYING FROM HERE ⬇️⬇️⬇️

My Telegram bot (ai_team_bot.js) forwards messages to `claude -p` and sends the
reply back to Telegram. Problem: Claude's output is Markdown, so replies show up
with literal **double asterisks**, # heading marks, and `backticks` instead of
reading like a normal chat.

Fix it by stripping the Markdown to clean plain text BEFORE sending to Telegram.
Do NOT use Telegram's parse_mode / Markdown mode — its parser is strict and crashes
on unbalanced * or _. Stripping is safer.

Steps:
1. Add a helper function called plain(text) that returns the text with Markdown removed:
   - remove ``` code fences but keep the code inside
   - `inline code`        -> inline code   (drop the backticks)
   - # / ## / ### headings -> drop the leading # marks
   - bullet markers (-, *, +) at line start -> turn into "• "
   - **bold**             -> bold
   - *italic*             -> italic
   - [text](url)          -> text (url)
   - collapse 3+ blank lines down to 2
   - .trim() the result
   IMPORTANT: don't mangle identifiers like mcp__ms365 — only strip real emphasis.

2. In the message handler, run Claude's output through plain() BEFORE chunking and
   sending, e.g.  const reply = plain(out) || '(claude returned no output)';
   Then chunk and send `reply` instead of the raw output, and use reply.length in
   the log lines so the char count matches what was actually sent.

3. Keep everything else in the bot exactly as it is. After the change, syntax-check
   with `node --check ai_team_bot.js`, then show me a quick before/after test proving
   **bold**, # headings, and `code` come out clean while mcp__ms365 stays intact.

⬆️⬆️⬆️ TILL HERE — COPY AND PASTE IN CLAUDE ⬆️⬆️⬆️

---

## After it's done
- Stop your old bot first (`Ctrl+C` in its terminal). Running two copies of the
  same bot crashes both with a `409 Conflict` error.
- Start it fresh: `node ai_team_bot.js`
- DM your bot something with formatting (e.g. "3 bullet points with a bold header")
  and check the reply now reads like a normal message.
