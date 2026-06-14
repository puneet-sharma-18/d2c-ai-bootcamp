[← Back to Student Handbook](student-handbook.md)

---

# Session 7: Storefront + Marketplace

**Skill unlocked:** MCP-fed iteration. Skills that read live Shopify conversion data, diagnose the gap between what the page says and what customers care about, and rewrite to close the gap. Plus a deeper marketplace pass than the Content Lead's first draft.

---

## What You'll Have After This Session

DEFAULT scope:

1. 2 PDPs rewritten (your lowest-converting top SKUs), with before / after files
2. 5 CRO observations on your storefront, each with impact / effort estimates
3. 4 marketplace listings (top 2 SKUs × Amazon + Flipkart)
4. Index files for both teammates

POWER scope (Max plan or take-home):
- 5 PDPs + 1 landing page + 15+ CRO observations + 10 marketplace listings + competitor marketplace audit

---

## Before You Start

You need:
- CLAUDE.md saved
- Latest Market Analyst report
- Latest VoC report (ideally MCP-fed)
- Shopify MCP connected (Session 3) — or be ready to paste PDP content if you are on a non-Shopify storefront

If you are not on a marketplace (Amazon / Flipkart), skip Step 4. Run only the PDP Writer.

---

## Step 1: The read-write loop (5 min)

Sessions 1 to 6 had skills that produced static reports. Session 7's skills do something different: they are part of an **iteration loop**.

```
[1] Read live data        ← Shopify MCP, conversion rate, order count
       ↓
[2] Diagnose the gap      ← What does the page say vs. what customers care about
       ↓
[3] Rewrite               ← PDP Writer skill
       ↓
[4] Push to draft         ← Shopify draft, NOT live
       ↓
[5] Founder review        ← Voice match, compliance, founder approval
       ↓
[6] Publish to live
       ↓
[7] Wait 7 to 14 days     ← Conversion rate moves (or does not)
       ↓
[8] Re-run                ← Read new data, diagnose new gap
       ↓
   (back to [1])
```

The loop is what compounds. A single rewrite is a guess. The data after 7 to 14 days tells you whether the guess was right.

Detailed teaching: `references/module-7-storefront-marketplace/cro-iteration-loop.md`.

---

## Step 2: Run the PDP Writer (DEFAULT) (~10 min)

In Claude:

```
/pdp-writer
```

The skill autoloads, asks scope. Type `default`.

It picks the 2 lowest-converting SKUs from your top 5. (Why: rewriting low-converting-but-high-traffic SKUs has the biggest absolute lift. Not the lowest-traffic ones.) Confirm with `yes` or override.

For each SKU, the skill:

1. Reads the current PDP via Shopify MCP
2. Saves the BEFORE state to `my-work/storefront-specialist/<today>-<sku>-before.md`
3. Writes a 5-line gap analysis (current page vs VoC themes vs Market Analyst gaps)
4. Rewrites the page (title, hero, bullets, description, FAQ, image alt text)
5. Saves the AFTER state
6. Writes 5 CRO observations on your overall storefront
7. Runs the brand safety pass

Open the BEFORE and AFTER side by side. The diff is what you actually changed. The gap analysis tells you why.

Reply ✅ when your PDPs are rewritten.

---

## Step 3: Push to draft (3 min)

When the skill is done, it asks:

> "Want me to push the top 1 PDP to Shopify as a draft via MCP?"

Type `yes`. The skill writes to Shopify DRAFT (not live). The founder reviews in the Shopify admin and publishes when ready.

**Critical**: even though the MCP can write live, every push goes to DRAFT first. You approve before publishing. Shopify keeps version history; if anything goes wrong, you revert.

---

## Step 4: Run the Marketplace Editor (DEFAULT) (~10 min)

If you are on Amazon and / or Flipkart, run:

```
/marketplace-editor
```

Skill autoloads, asks scope. Type `default`.

The marketplace shopper is NOT the D2C shopper. The skill knows this. Differences:

| | D2C site shopper | Marketplace shopper |
|---|---|---|
| Time on page | ~90 sec | ~25 sec |
| What they trust | The brand | This listing's reviews |
| Decision driver | Story + ingredients | Specs + reviews + Prime / Plus + price |

The skill picks 2 SKUs by marketplace orders, rewrites Amazon A+ + Flipkart for each. 4 outputs total in DEFAULT.

For each SKU's folder:
- `amazon-aplus.md` — title, 5 bullets, hero text, 3 modules, backend keywords, image briefs
- `flipkart.md` — title, 5 highlights, description, specifications

Reply ✅ when both listings are saved.

---

## Step 5: The marketplace-vs-D2C contrast (5 min)

Open your Amazon A+ AND your Shopify PDP for the same SKU side by side. Read both for 30 seconds each. The differences should be visible:

- Marketplace title is denser, packs the searchable attributes
- Marketplace bullets address worry-from-comparison-shopping
- D2C bullets address brand belief
- Marketplace specs are exhaustive
- D2C copy is selective

Most founders write one set of copy and paste it everywhere. That is the conversion gap. The two skills know the difference.

---

## Step 6: Pick the top observation, ship the fix (5 min)

Open `my-work/storefront-specialist/<today>-cro-observations.md`. Read the 5 observations.

Pick the top one by **impact / effort**. The skill ranks them; trust the ranking unless you see something obviously wrong.

Plan to ship this fix this week. Measure for 7 days. Re-run the skill next week. The conversion-rate movement will tell you whether the fix worked.

This is the iteration loop in practice. You are not running it once; you are starting it.

---

## What You Just Built

Two real PDPs rewritten on your actual store, queued in Shopify draft for review. Plus marketplace listings ready to upload. Plus the CRO observation list that points at the next 5 things to test.

More importantly, you saw the iteration loop. The skills are not one-shot; they are weekly. The data tells you whether the rewrites worked, and the next rewrite is data-informed.

---

## What's Next

Session 8 hires Ops Manager + Retention Manager. SOPs, vendor templates, WhatsApp retention flows, customer segments. Plus the new primitive: hooks and triggers.

[Continue to Session 8: Ops + Retention →](session-8-ops-retention.md)

---

## If You Get Stuck

| Symptom | Fix |
|---|---|
| Skill cannot read PDP | Shopify MCP not connected, or you are on non-Shopify. Paste the PDP content from clipboard, skill works on the paste. |
| Conversion rate "no data" in MCP | Shopify analytics scope not granted at OAuth. Re-auth with `read_analytics`. |
| Rewrite reads like the original | VoC themes thin OR CLAUDE.md voice rules thin. Sharpen one or both, re-run. |
| Marketplace bullets too long | Skill ignored char limits. Re-run with: "enforce 250 char per bullet hard". |
| Compliance flags on every Amazon bullet | Regulated category + Amazon's restricted-words list. Read flags as the do-not-use list. |
| Pushed to live by accident | Revert in Shopify admin (versions are kept). Push to DRAFT only next time, approve manually. |

For anything not on this list, raise hand in the workshop chat.
