# Connect Gmail and Google Drive (via Claude.ai web or Claude Desktop)

Same path as Shopify: add the connector once in Claude.ai or Claude Desktop, then Claude Code picks it up via the shared account.

## What you need

- A Google account (Workspace preferred, personal Gmail also works)
- 5 minutes

## Step 1. Add the Gmail and Drive connectors

**Option A — Claude.ai web (recommended)**

1. Open https://claude.ai, sign in.
2. Click your profile (bottom-left) then **Settings** then **Connectors**.
3. Find **Gmail** in the list. Click **Connect**. OAuth opens in a new tab — sign in with the Google account you actually run the brand from (your @brand.com Workspace account, ideally). Approve scopes (read messages, draft messages — not send).
4. Back in Connectors, find **Google Drive**. Click **Connect**. OAuth opens — sign in with the same Google account. Approve read access.
5. Both rows show as connected.

**Option B — Claude Desktop**

1. Open Claude Desktop. If you do not have it, install from https://claude.ai/download.
2. **Settings** then **Connectors** then **Add connector** then **Gmail**. Same OAuth flow as above.
3. Repeat for **Google Drive**.

Pick one surface. Do not connect on both.

## Step 2. Confirm in Claude Code

Open a Claude Code session at the repo root and run:

```
/mcp
```

You should see `gmail` and `google-drive` listed as connected. Claude Code shares connectors with the Claude.ai account you are signed in with, so connecting in Claude.ai or Desktop is enough.

If either is missing:
- Wait 30 seconds and run `/mcp` again, account sync can lag.
- Confirm Claude Code is signed in with the same account. Run `claude login` if not.
- Re-open Claude Code (`Ctrl-D`, then `claude`) so it picks up the fresh state.

## Step 3. Try Gmail

A couple of queries to confirm Gmail works and to feel out the surface:

```
Search Gmail for "(refund OR exchange OR delivery) newer_than:90d".
How many threads matched? Show me the subject lines of the first 10.
```

```
Find the last 5 emails from any customer mentioning my brand name.
For each, give me the sender, date, and one-line gist.
```

Real counts and real subjects — you are connected.

## Step 4. Try Drive

```
List my 10 most recently modified Drive files. For each: name, type, last modified.
```

```
Find any Drive files with "brand" or "review" or "customer" in the name.
Show me the top 5 and a one-line summary of each.
```

Real files, real names — Drive is connected.

You do not need to create a special folder for the workshop. Whatever you have in Drive (brand decks, exports, vendor briefs) is what the teammates will work with.

## Step 5. Other things you can now do

These are not workshop steps, but the connectors give you these capabilities for the rest of the weekend:

- `Pull the last 20 messages from <vendor>@<their-brand>.com and tell me where the next shipment stands`
- `Find every customer who emailed twice without a reply in the last 30 days and draft a follow-up`
- `Read the brand brief from Drive and check whether our website hero matches it`
- `Summarise the top complaint themes from support emails this week`

Gmail can draft replies but cannot send without your explicit yes per draft. Drive is read-only.

## Stuck?

| Symptom | Fix |
|---|---|
| Connectors page does not show Gmail or Drive | Free plan without connector access. Upgrade to Pro for the weekend, downgrade after. |
| OAuth fails with "access blocked: this app is not verified" | Click "Advanced" then "Go to ... (unsafe)" — the connector app is the unverified one, not malicious. Or test on personal Gmail if your Workspace admin restricts unverified apps. |
| Gmail returns 200+ unrelated threads | Tighten: `to:support@<brand>.com newer_than:90d -from:no-reply` |
| Drive shows files you do not recognise | You signed in with the wrong Google account. In Claude.ai or Desktop Connectors, disconnect and reconnect with the right account. |
| Workspace admin blocks third-party apps | Ask admin to whitelist the connector, or fall back to personal Gmail for the workshop. |

## Privacy note

Drive is read-only. Gmail can draft but cannot send without your yes. You can revoke access any time at myaccount.google.com → Security → Third-party apps with account access.

Anything saved to `my-work/` is your data on your laptop. The Voice of Customer skill strips PII (phone, email, full name, order ID) before saving. Verify on your first run by opening the saved report and searching for any phone number you know is in the source. If you find one, flag it and re-run.
