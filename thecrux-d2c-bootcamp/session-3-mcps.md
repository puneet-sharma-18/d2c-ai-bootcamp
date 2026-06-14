[← Back to Student Handbook](student-handbook.md)

---

# Session 3: MCPs

**Skill unlocked:** Live data. Shopify, Google Drive and Gmail connected so your skills read what is actually happening in your brand right now, not what you exported last week.

---

## What You'll Have After This Session

1. Shopify connector live, CLAUDE.md Section 4 updated from your live top SKUs
2. Gmail and Google Drive connectors live
3. A SKU truth check on disk — what you sell, what you say and what customers tell you, on one screen
4. The setup ready for Session 4 (Content Lead) and the rest of the weekend

---

## Before You Start

You need:
- CLAUDE.md saved (Session 1)
- One Market Analyst report and one VoC report in `my-work/` (Session 2)
- Owner or Staff-with-app-install permission on your Shopify store. If you are Staff only, get your founder colleague who is the Owner to be near you for 2 minutes.
- A Google Workspace account (or personal Gmail) you actually run the brand from. The account should have at least 30 to 50 support / customer threads from the last 90 days — that is what the live VoC re-run reads.

If you are not on Shopify (Wix / DTC.in / WooCommerce / custom), skip the Shopify MCP and use the manual CSV path described in the box below. Do Drive + Gmail as written. The rest of the weekend works the same way.

> **Not on Shopify?**
>
> What you lose without a Shopify MCP: live catalogue auto-refresh into CLAUDE.md Section 4, live order data for "top SKUs last 30 days", live inventory signal for Day 2's Operations Autopilot. What you keep: a populated Section 4 you paste once and refresh weekly; Market Analyst and VoC reports run fine; Content Lead (Session 4) runs fine on a slightly older catalogue.
>
> **Manual path.** Export your catalogue from your storefront admin (Wix: Admin → Products → Export. DTC.in: Admin → Catalogue → Download CSV. WooCommerce: WP Admin → Products → Export. Custom: ask your dev for a CSV with SKU name, category, price, inventory, last 30-day order count). Save as `resources/products-snapshot.csv`. Then prompt Claude:
>
> ```
> Read resources/products-snapshot.csv. Update CLAUDE.md Section 4 with the top 3 SKUs
> by last-30-day order count. Mark Section 4 with "Last refreshed: <today>"
> so I know to re-export weekly.
> ```
>
> Drive and Gmail connectors do not depend on Shopify. Follow Step 3 of this session exactly. They unlock the better VoC re-run for everyone.
>
> **Optional: Sheets MCP for auto-refresh.** If your product list lives in a Google Sheet, install the Google connector (Step 4 below) and point Claude at the Sheet URL. Gets you most of the Shopify auto-refresh experience.
>
> **Day 2.** Export orders weekly into `resources/orders-<week>.csv` for Operations Autopilot and Growth Analyst. Custom storefront with an in-house dev: scope a small MCP server in week-2 office hours. The Anthropic MCP SDK is a couple of hours of work.

---

## Step 1: What is an MCP (2 min)

```
[Claude Code]  <----MCP---->  [Shopify Admin API]
                                [Drive]
                                [Gmail]
```

An MCP (Model Context Protocol) is the connector that lets Claude read from and write to a system you already use. Without an MCP you paste your product list once, it goes stale next week. With an MCP, Claude reads live every time.

Three MCPs today: Shopify (catalogue, orders, customers), Drive (your reviews folder), Gmail (your support inbox).

---

## Step 2: Connect Shopify via Claude.ai web or Claude Desktop (5 min)

Shopify connects through the **Claude.ai web** or **Claude Desktop** connector. One-click OAuth from Settings → Connectors.

You will run the Shopify query in Claude.ai or Desktop, save the output as a snapshot in this repo, then Claude Code reads the snapshot. Two surfaces, one repo.

**Add the connector** (pick one):

- **Claude.ai web**: open https://claude.ai, sign in, click your profile (bottom-left) then **Settings** then **Connectors** then find Shopify then **Connect**. Sign in with the Owner account, pick the production store (not a dev or sandbox), approve scopes.
- **Claude Desktop**: install from https://claude.ai/download if needed. Open **Settings** then **Connectors** then **Add connector** then **Shopify**. Same OAuth flow.

Do not connect on both surfaces, pick one.

**Confirm in Claude Code.** In the terminal session at the repo root, run:

```
/mcp
```

You should see `shopify` in the list as connected, with your store domain. If you signed in to Claude Code with the same account you used in Claude.ai or Desktop, the connector is shared. If it does not show up, run `/mcp` again after 30 seconds (the account sync can lag), or sign in to Claude Code with the same account.

**Verify with a real query** in the same Claude.ai or Desktop session:

```
Read the products from Shopify. List the top 5 SKUs by orders in the
last 30 days. For each, give: name, current price, current inventory,
last 30-day order count. Output as a markdown table.
```

If you see a real table with real numbers, you are connected. If not, see the troubleshooting at the bottom.

**Save the snapshot** so Claude Code can read it. Ask Claude.ai or Desktop for a richer pull:

```
Pull from Shopify:
- Top 10 SKUs by last-30-day order count: name, category, price (INR),
  inventory, 30d orders
- Total orders last 30 days, last 90 days
- Top 10 customers by lifetime value (mask names to first name + last initial)

Format as one markdown document with three sections (Catalogue, Orders,
Customers). Add "Snapshot date: <today>" at the top.
```

Copy the full markdown output. Save it in this repo as `resources/shopify-snapshots/<today>-shopify.md` (create the folder first time).

**Update CLAUDE.md from the snapshot.** Back in Claude Code (terminal, repo root):

```
Read resources/shopify-snapshots/<today>-shopify.md. Update CLAUDE.md
Section 4 (Products) with the top 3 SKUs from the snapshot. Fill: SKU name,
category, current price (INR), one-line USP. Margin tier (low / mid / high)
is my call, mark it as TODO so I fill it later. Add a
"Source: resources/shopify-snapshots/<today>-shopify.md" line under Section 4.
```

Open CLAUDE.md and confirm Section 4 now has your real SKU names. Edit any USP that does not match your voice. Reply ✅ in the workshop chat.

Detailed walkthrough if anything fails: `references/module-3-mcps/mcp-setup-shopify.md`.

---

## Step 3: Connect Gmail and Google Drive (5 min)

Same path as Shopify. Add the **Gmail** and **Google Drive** connectors in Claude.ai (or Claude Desktop), Settings → Connectors. Sign in with the Google account you actually run the brand from (your @brand.com Workspace account, ideally). Approve scopes (Drive read access, Gmail read + draft).

Once connected, run `/mcp` in Claude Code (repo root) and confirm both `gmail` and `google-drive` show as connected. Same account sync as Shopify in Step 2.

Try Gmail with a couple of queries (in Claude Code, Claude.ai or Desktop — your call):

```
Search Gmail for "(refund OR exchange OR delivery) newer_than:90d".
How many threads matched? Show me the subject lines of the first 10.
```

```
Find the last 5 emails from any customer mentioning my brand name.
For each, give me the sender, date, and one-line gist.
```

Try Drive with a couple of queries:

```
List my 10 most recently modified Drive files. For each: name, type, last modified.
```

```
Find any Drive files with "brand" or "review" or "customer" in the name.
Show me the top 5 and a one-line summary of each.
```

Real counts, real names, real summaries — you are connected. Reply ✅ in the workshop chat.

You do not need to create a special folder in Drive. Whatever you already have (brand decks, review exports, support exports, vendor briefs) is what we will work with. If you have nothing in Drive yet, that is fine — Gmail alone is enough to make Voice of Customer come alive in the next step.

Detailed walkthrough: `references/module-3-mcps/mcp-setup-drive-gmail.md`.

---

## Step 4: SKU truth check — one prompt across all three (10 min)

Three connectors live. Now ask the question no single tool answers: where does what we sell, what we say and what they tell us actually agree, and where does it not.

In Claude Code (repo root), paste:

```
Run a "SKU truth check" for me.

1. From Shopify, pull my top 3 SKUs by orders in the last 30 days. For
   each: name, current price (INR), 30-day order count, 30-day revenue,
   current inventory.

2. From Gmail, for each SKU find threads newer_than:90d where the customer
   mentions the SKU name (or a close variant — e.g. "the serum" if the
   name is hard to type). Cluster what they say into:
   - what they love (top 1-2 themes)
   - what they complain about or return for (top 1-2)
   - what they ask before buying (top 1-2)

3. From CLAUDE.md Section 4 and any Drive doc that looks like a PDP,
   product brief or brand deck for that SKU (search Drive for "PDP",
   "brief", the SKU name), read what we officially claim.

4. Output one section per SKU:
   - The numbers (price, 30d orders, inventory)
   - What we claim (one line)
   - What customers love (1-2 lines)
   - What they complain about or are confused by (1-2 lines)
   - The mismatch or opportunity (one line — where our story and their
     experience diverge, or where they say something we should be saying)

Save as my-work/brand-brain/<today>-sku-truth-check.md
```

Open the saved file. Three things to look for:

1. **One SKU where customers buy for a different reason than we sell.** The PDP says "premium ingredients." Customer emails repeatedly say "thanks, the packaging finally feels like a gift." Your real USP, free.
2. **One SKU with a small recurring complaint.** Same packaging detail, same delivery question, same ingredient confusion in five threads. A 30-minute fix you did not know to make.
3. **One SKU where everything aligns.** Story, claim and customer voice all point the same way. That is the SKU to lean into for Meta ads next month.

This is the chain alive. Three connectors and one prompt produced a brief the founder could not have written in less than half a day, and could not have written at all without sitting with the customer voice.

The rest of the weekend, every teammate runs questions in this shape:
- Content Lead reads CLAUDE.md, the VoC, Market Analyst output and ships a 30-day calendar
- Storefront reads the SKU truth check and rewrites the PDP
- Retention reads top customers from Shopify and unresolved Gmail threads and drafts a win-back
- Growth Analyst stitches the Monday brief from all of the above

The chain on disk right now:

```
CLAUDE.md (Section 4 refreshed from Shopify)
resources/shopify-snapshots/<today>-shopify.md
my-work/market-analyst/<today>-intel.md (morning run)
my-work/voice-of-customer/<today>-voc-report.md (morning run)
my-work/brand-brain/<today>-sku-truth-check.md (this step)
```

Session 9 schedules this kind of cross-system query as a standing Monday brief. The Capstone wires the schedule for keeps.

---

## What You Just Built

Three live connections that turn every skill from a snapshot tool into ongoing intelligence. Voice of Customer reads the inbox every time it runs. Content Lead reads live SKUs. Retention reads live customers. The morning's paste-in runs are the last ones you ever have to do.

---

## What's Next

Session 4 spawns the Content Lead — your first subagent. It reads CLAUDE.md, your Market Analyst report, your VoC report and the SKU truth check from this session, plans a 30-day content calendar, drafts your priority pieces and writes marketplace listings.

[Continue to Session 4: Content Lead →](session-4-content-lead.md)

---

## If You Get Stuck

| Symptom | Fix |
|---|---|
| Shopify OAuth fails: "App not installed" | Your role is Staff. Have the Owner authorise from their device. 2 min. |
| Shopify connects but returns zero orders | You picked a dev / sandbox store. In Claude.ai or Desktop Settings → Connectors, disconnect Shopify and reconnect to the production store. |
| `/mcp` in Claude Code does not show the connector you added | Account sync lag. Wait 30 seconds, run `/mcp` again. Or quit and re-open Claude Code. Or confirm Claude Code is signed in with the same account as Claude.ai or Desktop. |
| Google OAuth blocked: "this app is not verified" | Click Advanced → Go to (unsafe). Or use a personal Gmail to test if your Workspace admin restricts. |
| Drive returns files you do not recognise | Wrong Google account. In Claude.ai or Desktop Connectors, disconnect Drive and reconnect with the right account. |
| Gmail search returns 200+ unrelated emails | Tighten: `to:support@<brand>.com newer_than:90d -from:no-reply` |
| Hit a rate limit on the first big query | Add a date scope: "last 7 days" or "last 30 days," not "all time." |
| SKU truth check returns empty Gmail sections for a SKU | Customers do not email using the SKU name. Re-run the prompt and tell it 1-2 nicknames per SKU ("the cream", "the 250ml pack"). |

For anything not on this list, raise hand in the workshop chat.
