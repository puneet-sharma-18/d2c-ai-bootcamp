# Connect Shopify (via Claude.ai web or Claude Desktop)

We connect Shopify through the **Claude.ai web app** or **Claude Desktop** connector. One-click OAuth from Settings → Connectors.

You will run Shopify queries in Claude.ai or Claude Desktop, save the output as a snapshot file in this repo, then Claude Code reads the snapshot for the rest of the weekend.

## What you need

- Owner or Staff-with-app-install permission on your primary Shopify store
- A Claude.ai account signed in on the web, OR Claude Desktop installed
- 5 minutes

## Step 1. Add the Shopify connector

**Option A — Claude.ai web (recommended)**

1. Open https://claude.ai in your browser, sign in.
2. Click your profile (bottom-left) then **Settings**.
3. Open **Connectors**.
4. Find **Shopify** in the list. Click **Connect**.
5. A Shopify OAuth tab opens. Sign in with the Owner account, pick your primary store (not a dev or sandbox), approve the requested scopes (products, orders, customers, inventory).
6. Back in Claude.ai, the Shopify connector shows as connected with your store domain.

**Option B — Claude Desktop**

1. Open Claude Desktop. If you do not have it, install from https://claude.ai/download.
2. **Settings** then **Connectors** then **Add connector** then **Shopify**.
3. Same OAuth flow as above.

Either surface works. Pick one. Do not connect on both, you will confuse the OAuth state.

## Step 2. Confirm in Claude Code

Open a Claude Code session in the repo root and run:

```
/mcp
```

You should see `shopify` listed as connected with your store domain. Claude Code shares connectors with the Claude.ai account you are signed in with, so once you connect in Claude.ai or Desktop, the same connector shows up here.

If `shopify` is not in the list:
- Wait 30 seconds and run `/mcp` again, the account sync can lag.
- Confirm Claude Code is signed in with the same account you used for Claude.ai or Desktop. Run `claude login` if not.
- Re-open Claude Code (`Ctrl-D` to quit, then `claude` again) so it picks up the fresh connector state.

## Step 3. Verify with a real query

In the same Claude.ai or Claude Desktop session, paste this prompt:

```
Read the products from Shopify. List the top 5 SKUs by orders in the last 30 days.
For each, give: name, current price, current inventory, last 30-day order count.
Output as a markdown table.
```

You should see a real table with your SKUs and real numbers. If you see "I don't have access to Shopify data," go back to Connectors and re-authorise.

## Step 4. Save the snapshot to the repo

Still in Claude.ai or Desktop, ask for a richer pull and a markdown export:

```
Pull from Shopify:
- Top 10 SKUs by last-30-day order count: name, category, price (INR), inventory, 30d orders
- Total orders last 30 days, last 90 days
- Top 10 customers by lifetime value (name masked to first name + last initial)

Format as a single markdown document with three sections (Catalogue, Orders, Customers).
Add a "Snapshot date" line at the top with today's date.
```

Copy the full markdown output. In Claude Code (terminal), save it:

```bash
# in the repo root
mkdir -p resources/shopify-snapshots
# paste the markdown into this file, save and close
nano resources/shopify-snapshots/$(date +%Y-%m-%d)-shopify.md
```

Or in your editor: create `resources/shopify-snapshots/YYYY-MM-DD-shopify.md` and paste.

## Step 5. Point Claude Code at the snapshot

Back in Claude Code (terminal, repo root):

```
Read resources/shopify-snapshots/<today>-shopify.md. Update CLAUDE.md Section 4
(Products) with the top 3 SKUs from the snapshot. Fill: SKU name, category,
current price (INR), one-line USP. Margin tier (low / mid / high) is my call,
mark it as TODO so I fill it later.

Add a "Source: resources/shopify-snapshots/<today>-shopify.md" line under
Section 4 so we know when it was last refreshed.
```

Open CLAUDE.md and confirm Section 4 has your real SKU names. Edit any USP that is off.

## Step 6. The weekly refresh pattern

Once a week (or before any session that needs fresh numbers):

1. Open Claude.ai or Claude Desktop, run the Step 3 prompt again.
2. Save the new output as `resources/shopify-snapshots/<new-date>-shopify.md`.
3. In Claude Code: "Read the latest file in resources/shopify-snapshots/ and refresh CLAUDE.md Section 4."

This is the loop. Two surfaces, one repo, no flaky CLI auth.

## Other things you can ask Shopify in Claude.ai or Desktop

Once the connector is live in the web or desktop app, ask anything:

- `Show me the 10 customers with the highest lifetime value over the last 12 months.`
- `Find products with inventory below 20 units.`
- `Pull last week's orders and group by SKU.`
- `Show me products that have not been reordered in 60 days.`

When the answer matters for a workshop step, save it into `resources/shopify-snapshots/` so the rest of the weekend's skills can read it.

## Stuck?

| Symptom | Fix |
|---|---|
| Connectors page does not show Shopify | You are on a free plan with no connector access. Upgrade to Pro for the weekend, downgrade after. |
| OAuth tab shows "App not installed" | Your role is Staff. Have the Owner authorise from their device once. |
| Connector connects but returns zero orders | You picked a dev or sandbox store. Disconnect, re-connect, pick the production store. |
| Top SKUs list shows products you do not recognise | Same as above. Wrong store. |
| Hits a rate limit on the first big query | Scope the prompt: "last 7 days" or "last 30 days," not "all time." |
| Asked Claude Code to query Shopify directly | Claude Code does not have the connector. Run the query in Claude.ai or Desktop, save the snapshot, then point Claude Code at the file. |

## Why this path

The Claude.ai and Desktop connector is the official Shopify integration with one-click OAuth and a re-auth UI you can use any time. You query Shopify in Claude.ai or Desktop, save snapshots to the repo, and Claude Code reads them — the rest of the weekend's skills work from the snapshot. Drive and Gmail still go through Claude Code MCP (see `mcp-setup-drive-gmail.md`).
