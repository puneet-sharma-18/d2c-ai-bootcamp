# Meta Ads Sync — Prework Setup (Mac + Windows)

Connect your Meta ad account and pull its data into local JSON, so the Performance Marketer and Growth Analyst sessions have real numbers to work with.

**Time needed:** ~15 minutes
**Do this before:** Day 1 of the bootcamp

**You'll end with:** a `.env` holding a read-only Meta token, a live export from your ad account in `data-sync/processed/`, and a one-paste analyst report from Claude.

> Each command is shown for **both** Mac/Linux and **Windows**. Run only the block for **your** machine. Windows uses **PowerShell** (the blue terminal — search "PowerShell" in the Start menu). Don't mix the two: Mac uses `python3`/`/` paths, Windows uses `python`/`\` paths.

---

## The shape of it

```
  Meta Business Manager  ->  System User token (never expires, ads_read only)
        |
        v   token + ad account id live in .env (in the repo root)
   data-sync/meta_sync.py        ->  quick health check (account totals + campaigns)
   data-sync/meta_deep_sync.py   ->  full export (ad sets + targeting + ads + creative)
        |
        v   writes JSON
   data-sync/processed/meta_deep_latest.json
        |
        v   paste into a fresh Claude chat with the analyst prompt
   7-section performance report
```

Both scripts already live in the repo at `data-sync/`. You don't create or paste any code — you only add your credentials and run them.

> ### Option B — skip the token, use the Meta Ads MCP (paid Claude plan)
>
> If you're on a paid Claude plan (Pro / Max / Team / Enterprise), there's a ~2-minute alternative to the token + scripts below: connect the **official Meta Ads MCP** and let Claude read your account live.
>
> 1. Go to **claude.ai → Settings → Connectors** (`claude.ai/customize/connectors`)
> 2. Click **Add custom connector** (Meta Ads is not in the built-in directory — you add it by URL)
> 3. **Name:** `Meta Ads` · **URL:** `https://mcp.facebook.com/ads` → **Add**
> 4. Click **Connect** on the new connector → log in with your **Meta Business Manager** account in the browser → grant access to the ad accounts you want
> 5. In Claude Code, run `/mcp` to confirm the connector shows as connected, then just ask: *"list my Meta ad accounts"* / *"pull last 30 days for ad account X"*
>
> **Trade-offs vs the token sync (Option A, the rest of this doc):**
> - ✅ Faster setup, no `.env`, no scripts, always live
> - ⚠️ Needs a paid plan; everyone on the team needs their own connector
> - ⚠️ It returns data **into the chat** — it does **not** write `data-sync/processed/*.json`. Sessions that read those files (Performance Marketer, Growth Analyst) still expect the JSON, so if you go MCP-only you'll ask Claude to fetch live each time instead of pointing it at a file.
> - ⚠️ Connect it **via claude.ai** as above — adding it directly in the CLI (`claude mcp add … mcp.facebook.com/ads`) currently fails OAuth from Claude Code.
>
> For the bootcamp's downstream sessions, the token sync (Option A) is the more reliable default because it produces the JSON files the teammates read. Use the MCP if you just want a fast live look.

---

## Before you start

- The **bootcamp repo cloned** at `~/thecrux-d2c-bootcamp` (Mac) / `$HOME\thecrux-d2c-bootcamp` (Windows). You did this in Session 0 prework.
- A **Meta Business Manager** account with at least one ad account assigned to you, and **admin access** to that Business Manager (needed to create a System User in Step 2).
- An ad account that **has run ads** — a brand-new empty account gives empty reports (paused historical data is fine).
- **`uv` installed** — the scripts declare their Python dependencies inline (PEP 723), so `uv` installs them on first run. No `pip`, no virtualenv, no activation step.
  - **Mac:** `brew install uv`
  - **Windows (PowerShell):** `winget install --id=astral-sh.uv -e`
  - Verify with `uv --version`. (If `winget` is missing, get uv from <https://docs.astral.sh/uv/getting-started/installation/>.)
- Your **Facebook password handy** — Meta may make you re-authenticate during token generation.

> **Why `uv` and not a virtualenv?** A virtualenv has to be re-activated in every new terminal, and forgetting that is the #1 cause of `ModuleNotFoundError`. `uv run` has no activation step — it reads the dependencies from the top of the script and handles them for you.

---

## Step 1 — Open a terminal in the repo (1 min)

**Mac / Linux:**
```bash
cd ~/thecrux-d2c-bootcamp
```

**Windows (PowerShell):**
```powershell
cd $HOME\thecrux-d2c-bootcamp
```

Confirm you're in the right place and the scripts exist:

**Mac / Linux:**
```bash
ls data-sync/meta_sync.py data-sync/meta_deep_sync.py
```

**Windows (PowerShell):**
```powershell
dir data-sync\meta_sync.py, data-sync\meta_deep_sync.py
```

If you see both paths, you're set. If not, you're not in the repo root — `cd` into it and try again.

The `.gitignore` already excludes `.env`, `data-sync/raw/` and `data-sync/processed/`, so your token and ad data never get committed.

---

## Step 2 — Get your Meta token + ad account ID (8 min)

We use a **System User token**: it never expires and is scoped to read-only ad data. This is the correct token for analytics — set it once and you never touch it again for the whole bootcamp.

> If you also need WhatsApp / Instagram **publishing** later (Session 8, the Telegram session, Composio), that needs a *different, broader* token — see the [Appendix](#appendix--publishing-token--business-id-whatsapp--instagram) at the bottom. Don't try to make one token do both.

### 2A — Create a System User and generate the token

1. Go to **business.facebook.com**
2. **Business Settings** (left sidebar) -> **Users** -> **System Users**
3. **Add** -> create a System User
   - **Name:** `bootcamp-sync` (or anything self-describing)
   - **Role:** Employee access is enough — Admin not needed
4. Click your new System User -> **Add Assets** -> **Ad Accounts** -> select the account you want -> grant **"View performance"**
5. Back on the System User page -> **Generate New Token**
   - **App:** pick any app (or create one called "D2C Bootcamp")
   - **Token expiration:** Never
   - **Permissions:** tick **`ads_read`** only
6. **Copy the token immediately** — Meta shows it once. It starts with `EAA...` and is ~200 characters.

> **⚠️ The #1 mistake:** generating the token *before* assigning the ad account in step 4. The token works but returns "no ad accounts." If your first sync in Step 4 comes back empty, this is almost always why.

### 2B — Get your Ad Account ID

1. Open **adsmanager.facebook.com** on the account you want
2. In the URL bar you'll see `...?act=1234567890&...`
3. Copy **just the number** — no `act_` prefix (the script adds it)

### 2C — Create your `.env` file

Create a file named exactly `.env` in the repo root, containing:
```
META_ACCESS_TOKEN=PASTE_YOUR_TOKEN_HERE
META_AD_ACCOUNT_ID=PASTE_YOUR_ID_HERE
```

Quick create, then edit it to paste your real values:

**Mac / Linux:**
```bash
printf 'META_ACCESS_TOKEN=PASTE_YOUR_TOKEN_HERE\nMETA_AD_ACCOUNT_ID=PASTE_YOUR_ID_HERE\n' > .env
```

**Windows (PowerShell):**
```powershell
"META_ACCESS_TOKEN=PASTE_YOUR_TOKEN_HERE","META_AD_ACCOUNT_ID=PASTE_YOUR_ID_HERE" | Set-Content .env
```

Now open `.env` in any text editor, replace the two placeholders, and save.

> **⚠️ Windows: make sure the file is named `.env`, not `.env.txt`.** Notepad sometimes adds `.txt`. In PowerShell, run `dir` — you should see `.env` exactly. The `Set-Content` command above creates it correctly.

---

## Step 3 — Basic sync (doubles as your connection test) (1 min)

Run the basic sync. It pulls your account first, so if the token or account ID is wrong, it fails immediately with a readable error.

**Mac / Linux:**
```bash
uv run data-sync/meta_sync.py 7
```

**Windows (PowerShell):**
```powershell
uv run data-sync\meta_sync.py 7
```

**Pass** looks like:
```
Pulling Meta Ads data (7 days)...
Meta sync done -> Spend: Rs.39,044 | ROAS: 2.4x | Clicks: 11790 | CPC: Rs.3.31
```

If nothing ran in the last 7 days, it auto-falls back to all-time data. That's intentional — better than an empty file.

**If it fails:**

| Message contains | Cause | Fix |
|---|---|---|
| `Invalid OAuth access token` | Typo / extra space / expired | Re-copy the token into `.env`, no whitespace |
| `(#100) Object does not exist` | Ad account not assigned to System User | Redo Step 2A.4 (assign the asset) |
| `(#200) ... does not have permission` | Missing `ads_read` scope | Regenerate the token with the scope ticked |
| `Missing META_ACCESS_TOKEN...` | `.env` not found / misnamed | Check the file is `.env` (not `.env.txt`) in the repo root |
| `ModuleNotFoundError` / `uv: command not found` | `uv` not installed | Install uv (see "Before you start"), open a fresh terminal |

Pass this before moving on.

> **Checkpoint — connected**
> - [ ] System User created, ad account assigned with View performance
> - [ ] `ads_read` token + ad account ID (no `act_`) in `.env`
> - [ ] basic sync prints your account name and totals

---

## Step 4 — Deep sync (the one that matters) (1 min)

The basic sync gives account totals. For real analysis — best ad set, best ad, targeting, creative — run the deep sync. It pulls the whole tree: account -> campaigns -> ad sets (with targeting) -> ads (with creative).

**Mac / Linux:**
```bash
uv run data-sync/meta_deep_sync.py 30
```

**Windows (PowerShell):**
```powershell
uv run data-sync\meta_deep_sync.py 30
```

**Expected:**
```
Pulling Meta Ads deep data (30 days)...
  Window resolved: last_30d
  Fetching campaigns...
    2 campaigns
  Fetching ad sets (with targeting)...
    3 ad sets
  Fetching ads (with creative)...
    10 ads
Deep sync done [last_30d] -> Spend: INR 1,17,200 | ROAS: 2.6x | Clicks: 35,400 | CPC: INR 3.31 | 2 campaigns / 3 adsets / 10 ads
  -> data-sync/processed/meta_deep_latest.json
```

> **Day windows:** 7, 14, 28, 30, 90 (anything else defaults to 7). Use 90 if 30-day data is thin.

> **Don't add per-entity enrichment loops** (e.g. fetching the underlying post for every boosted ad). The deep sync makes ~6 calls per run on purpose. Meta flags fan-out patterns and can rate-limit or suspend the token.

> **Checkpoint — data flowing**
> - [ ] deep sync writes `data-sync/processed/meta_deep_latest.json`
> - [ ] that JSON has `campaigns`, `adsets` (with `targeting`), and `ads` (with `creative`)

---

## Step 5 — Analyse with Claude

The repo has a ready-made analyst prompt at **`references/resources/META-ADS-ANALYSIS-PROMPT.md`**. It produces a 7-section report: account health, best ad set, best ad, underperformers, audience insight, creative recommendation, and the next 3 actions.

1. Copy the export to your clipboard:
   - **Mac:** `pbcopy < data-sync/processed/meta_deep_latest.json`
   - **Windows (PowerShell):** `Get-Content data-sync\processed\meta_deep_latest.json -Raw | Set-Clipboard`
   - *(Or open the file in an editor and Cmd/Ctrl+A, Cmd/Ctrl+C.)*
2. Open a **fresh Claude chat** (clean context = unbiased read).
3. Paste the prompt from `META-ADS-ANALYSIS-PROMPT.md`, then paste the JSON after it.
4. **If your account ran traffic-objective campaigns** (no purchase events), add this line at the top first:
   > Note: this account ran traffic-objective campaigns (no purchase events). ROAS = 0 is a tracking artifact, not real performance. Focus on CPC, CTR, and the actions in account_insights.

---

## Daily use (after setup)

Open a terminal, then:

**Mac / Linux:**
```bash
cd ~/thecrux-d2c-bootcamp
uv run data-sync/meta_sync.py 7
uv run data-sync/meta_deep_sync.py 30
pbcopy < data-sync/processed/meta_deep_latest.json
```

**Windows (PowerShell):**
```powershell
cd $HOME\thecrux-d2c-bootcamp
uv run data-sync\meta_sync.py 7
uv run data-sync\meta_deep_sync.py 30
Get-Content data-sync\processed\meta_deep_latest.json -Raw | Set-Clipboard
```

**Output files:**
- `data-sync/raw/meta_YYYY-MM-DD.json` — dated history (one per run)
- `data-sync/processed/meta_latest.json` — last basic sync (overwritten)
- `data-sync/processed/meta_deep_latest.json` — last deep sync (overwritten)

---

## Connecting a *different* client

You don't rebuild anything:

1. In Business Settings -> System Users -> your sync user -> **Add Assets** -> assign the new ad account (View performance)
2. Edit `META_AD_ACCOUNT_ID` in `.env` to the new account number
3. Re-run `meta_sync.py` with the new ID, then sync

One System User can hold many ad accounts, so the same token usually works — you only swap the account ID.

---

## Troubleshooting

| Symptom | What's happening | Fix |
|---|---|---|
| `uv: command not found` | uv not installed / not on PATH | Install uv (see "Before you start"), open a fresh terminal |
| `Invalid OAuth access token` | Typo / extra whitespace | Re-paste the token into `.env` |
| `.env` not found / `Missing ...` | File misnamed `.env.txt` (Windows) | Rename to exactly `.env` in the repo root |
| Empty `campaigns` array | No campaigns *or* account not assigned | Re-check Step 2A.4 |
| All ROAS = 0 | Account ran TRAFFIC campaigns (no purchase event) | Not a bug — look at `actions[]` for leads/views |
| Some ads have empty `creative.body` | Boosted page posts — copy lives on the post | Acceptable. Don't enrich per-ad (rate-limit risk) |
| Falls back to `maximum` every run | No spend in the requested window | Use a larger window (90) or accept the fallback |

---

## Security

- [ ] `.env` is in `.gitignore` (it is, from the repo) — never commit it
- [ ] Never paste the token into Slack, screenshots, or GitHub issues
- [ ] If a token leaks: Business Settings -> System Users -> regenerate (the old one dies instantly)
- [ ] One System User per project — don't share tokens across integrations

---

## Appendix — Publishing token + Business ID (WhatsApp / Instagram)

The System User token above is **read-only** (`ads_read`) and ads-only — correct for the sync, and safe to keep forever. But a few later sessions (WhatsApp via Composio, Instagram, the Telegram session) need to **publish**, which requires a broader token. Generate that one **separately** — don't replace your sync token.

1. Go to **developers.facebook.com/apps** -> your app -> **Tools** -> **Graph API Explorer**
2. Set token type to **Page Access Token**, authenticate, and add the permissions you need, e.g.:
   - `pages_read_engagement`, `pages_manage_posts`
   - `instagram_basic`, `instagram_content_publish`
   - `whatsapp_business_messaging`
   - `leads_retrieval`
3. **Generate Access Token**, then extend it: **Tools -> Access Token Debugger** -> paste -> **Debug** -> **Extend Access Token**. The extended token lasts ~90 days (set a reminder ~85 days out to regenerate).
4. Get your **Business ID** for Composio/WhatsApp:
   ```bash
   curl -X GET "https://graph.facebook.com/v23.0/me/businesses" \
     -H "Authorization: Bearer YOUR_PUBLISHING_TOKEN"
   ```
   Pick the right business from the list and add the relevant lines to `.env`:
   ```
   META_PUBLISH_TOKEN=EAA...your extended publishing token
   META_BUSINESS_ID=780751577208701
   ```

Keep the two tokens distinct: `META_ACCESS_TOKEN` (never-expires, read-only, for the sync) and `META_PUBLISH_TOKEN` (~90 days, broad, for publishing).

---

*Same pattern works for any ad platform: token in `.env`, narrow scope, sync to JSON, analyse with Claude. Once Meta is done, Google / LinkedIn / TikTok are just translation.*
