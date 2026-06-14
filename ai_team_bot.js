// ai_team_bot.js
// A minimal Telegram bot for the AI team. It forwards every message you send it
// straight to the `claude -p` CLI and replies with whatever Claude returns.
// There is NO command logic here on purpose — your Claude skills do all routing.
// Run it from this project folder so Claude inherits the CLAUDE.md context.
// --- SETUP ---
const { Telegraf } = require('telegraf');
const { execFile } = require('child_process');
// promisify turns callback-style execFile into one we can `await`, so the handler reads top-to-bottom.
const { promisify } = require('util');
const execFileAsync = promisify(execFile);
require('dotenv').config();
// Timestamped logger so a long Claude run never looks like a frozen terminal.
const ts = () => new Date().toTimeString().slice(0, 8);
const log = (label, msg) => console.log(`${ts()} ${label} | ${msg}`);
// First line of output: telegraf takes 200-500ms to load, so without this the terminal looks hung on boot.
log('boot', 'starting ai_team_bot.js');
const TOKEN = process.env.TELEGRAM_BOT_TOKEN;
const USER_ID = process.env.TELEGRAM_USER_ID;
// --- STARTUP VALIDATION ---
if (!TOKEN || TOKEN === 'your_bot_token_here') {
  console.error('ERROR: TELEGRAM_BOT_TOKEN is missing or still the placeholder. Set it in .env');
  process.exit(1);
}
if (!USER_ID || isNaN(Number(USER_ID))) {
  console.error(`ERROR: User ID must be a number like 1234567890, not a username like @john. Got: ${USER_ID}`);
  process.exit(1);
}
const AUTHORIZED = Number(USER_ID);
log('boot', `config valid. Authorized user: ${AUTHORIZED}`);
// --- CLAUDE INVOCATION ---
async function runClaude(message) {
  // execFile (not exec) skips the shell, so the message is one safe argument with no shell-injection risk.
  const { stdout } = await execFileAsync('claude', [
    '-p', message,
    '--dangerously-skip-permissions',
    '--allowedTools', 'Read,Write,Edit,Glob,Grep,Bash,Agent,WebSearch,WebFetch,mcp__ms365,mcp__gsuite',
  ], {
    cwd: __dirname,                 // run where this script lives so CLAUDE.md context is inherited
    timeout: 600000,                // 10 min: heavy skills like /market-analyst run multi-stage research
    maxBuffer: 10 * 1024 * 1024,    // raise the output cap so large skill replies aren't truncated/errored
    input: '',                      // suppresses claude's "no stdin data received" warning
  });
  return stdout.trim();
}
// Split text into <=size pieces without breaking mid-line (Telegram caps messages near 4096 chars).
function chunk(text, size) {
  const out = [];
  let buf = '';
  for (const line of text.split('\n')) {
    if (buf && buf.length + line.length + 1 > size) { out.push(buf); buf = ''; }
    buf += (buf ? '\n' : '') + line;
  }
  if (buf) out.push(buf);
  return out;
}
// Strip Markdown so replies read as a normal chat (Telegram shows raw **, #, ` otherwise).
function plain(text) {
  return text
    .replace(/```[a-z]*\n?/gi, '').replace(/```/g, '')  // code fences (keep the code inside)
    .replace(/`([^`]+)`/g, '$1')                         // inline `code`
    .replace(/^#{1,6}\s+/gm, '')                         // # headings
    .replace(/^\s*[-*+]\s+/gm, '• ')                     // bullet markers -> •
    .replace(/\*\*([^*]+)\*\*/g, '$1')                   // **bold**
    .replace(/\*([^\s*][^*\n]*?)\*/g, '$1')              // *italic*
    .replace(/\[([^\]]+)\]\(([^)]+)\)/g, '$1 ($2)')      // [text](url) -> text (url)
    .replace(/\n{3,}/g, '\n\n')                          // collapse big gaps
    .trim();
}
// --- TELEGRAF CONFIGURATION ---
// handlerTimeout must exceed the claude timeout, or telegraf abandons the handler before a slow skill finishes.
const bot = new Telegraf(TOKEN, { handlerTimeout: 600000 });
// bot.catch keeps one failed run from crashing the whole bot.
bot.catch((err, ctx) => {
  log('error', err.stack || String(err));
  ctx.reply('Something went wrong running that. Check the terminal logs.').catch(() => {});
});
// --- HANDLER ---
bot.on('text', async (ctx) => {
  if (ctx.from.id !== AUTHORIZED) return;   // the only auth check: ignore everyone but the configured user
  const text = ctx.message.text;
  log('inbound', `@${ctx.from.username || ctx.from.id}: ${text.slice(0, 80)}`);
  // sendChatAction('typing') shows the "typing..." bubble; Telegram clears it after ~5s so we re-send every 4s.
  const typing = setInterval(() => ctx.sendChatAction('typing').catch(() => {}), 4000);
  ctx.sendChatAction('typing').catch(() => {});
  // Heartbeat so heavy skills (2-5 min) don't look like a hang in the terminal.
  const start = Date.now(); log('claude', 'starting...');
  const beat = setInterval(() => log('claude', `still running (${Math.round((Date.now() - start) / 1000)}s elapsed)`), 15000);
  try {
    const out = await runClaude(text);
    clearInterval(typing); clearInterval(beat);
    const reply = plain(out) || '(claude returned no output)';
    log('claude', `done in ${((Date.now() - start) / 1000).toFixed(1)}s, ${reply.length} chars`);
    const chunks = chunk(reply, 4000);
    for (const c of chunks) await ctx.reply(c);
    log('reply', `sent (${reply.length} chars, ${chunks.length} chunk${chunks.length > 1 ? 's' : ''})`);
  } catch (err) {
    clearInterval(typing); clearInterval(beat);
    log('error', err.stack || String(err));
    await ctx.reply(`Error: ${err.message}`);
  }
});
// --- STARTUP ---
log('boot', 'connecting to Telegram...');
// onLaunch callback fires once the bot is connected (the launch() promise itself only resolves on shutdown).
bot.launch(() => {
  console.log(`AI Team bot ready. Authorized user: ${AUTHORIZED}. Press Ctrl+C to stop.`);
  // getMe confirms the token is valid before any DM arrives.
  bot.telegram.getMe().then((me) => log('boot', `connected as @${me.username}, cwd: ${__dirname}`));
});
// SIGINT/SIGTERM: stop cleanly on Ctrl+C so the bot deregisters its polling loop from Telegram.
process.once('SIGINT', () => bot.stop('SIGINT'));
process.once('SIGTERM', () => bot.stop('SIGTERM'));
