[← Back to Student Handbook](student-handbook.md)

---

# Session 11 (add-on): Influencer Scout

**Skill unlocked:** Reading a Modash-shape creator dataset, building a shortlist that holds up to a five-point red-flag check, and drafting outreach and counter-offer copy that closes Indian creator deals 20-30% below the platform estimate without burning the relationship.

This session is an add-on, not part of the core 10. It assumes you already shipped Session 1 (CLAUDE.md), Session 2 (Market Analyst, Voice of Customer), and ideally Session 4 (Content Lead). If you have not, run those first; the Influencer Scout skill reads them.

---

## What You'll Have After This Session

DEFAULT scope:

1. A shortlist of 5 creators that match your brand bucket, with the read-out of why each fits
2. A five-point red-flag check on each, with a SHORTLIST / TEST POST / WALK verdict
3. A first outreach email per creator, anchored to a realistic INR rate
4. A counter-offer script per creator, ready if they come back at platform-listed rate
5. Index file for the Captain (Session 10) to read in your weekly synthesis

POWER scope (Max plan or take-home):
- 10 creators laddered across nano / micro / mid tiers
- A 4-week campaign calendar with seeding, amplification, measurement, renewal phases
- Budget estimated at three negotiation outcomes (anchor, mid, walk)

---

## Before You Start

You need:
- CLAUDE.md saved (Session 1)
- Ideally: Market Analyst report (Session 2) and Voice of Customer themes (Session 2)
- The reference pool already lives in your repo at `references/module-11-influencer-scout/`. No Modash subscription required for the workshop.

You do NOT need:
- A real Modash account. You will be reading sample data that mirrors the Modash field shape. Everything you learn here transfers to the platform on day one if you subscribe later.
- Existing creator relationships. The session teaches the read and the negotiation; the founder sends the outreach manually.

---

## Step 1: The two-question frame (3 min)

Most founders pick influencers by typing their brand into Instagram search and DMing whoever shows up. That is how budgets evaporate.

The Influencer Scout asks two questions in order. Both have to land before any outreach.

```
[1] Does this creator's audience match my customer?
       ↓
[2] Does this creator's content respect my brand voice?
       ↓
   If both yes → shortlist
   If either no → walk
```

The five-point red-flag check (next step) is how you answer question 1 with data, not vibes.

Detailed teaching: `references/module-11-influencer-scout/red-flag-cheatsheet.md`.

---

## Step 2: The five red-flag checks (5 min)

Read the cheatsheet before running the skill. Five checks in order. Any one fails, the creator does not make the shortlist:

| # | Check | What kills the deal |
|---|---|---|
| 1 | Credibility | `fake_follower_pct` over 25% |
| 2 | Audience geo | India audience under 60% (if you only ship India) |
| 3 | Engagement for tier | ER below the tier floor (under 4% for nano, under 2% for micro, under 1.5% for mid) |
| 4 | Saturation | `paid_post_ratio_30d` over 50% |
| 5 | Competitor traps | Direct competitor in `recent_paid_collabs` inside the last 30 days |

The skill applies these automatically. Reading them once first means you understand what the skill is checking, not just trusting its output.

---

## Step 3: Run the Influencer Scout (DEFAULT) (~10 min)

In Claude:

```
/influencer-scout
```

The skill autoloads, asks scope. Type `default`.

It will:

1. Read your CLAUDE.md (Session 1)
2. Read your latest VoC + Market Analyst files if present
3. Map your brand to one or two buckets in the sample pool (coffee, tea_wellness, premium_apparel_lifestyle, etc.)
4. Print the mapping back to you in 5 lines
5. Pause for your confirmation

Confirm with `yes, go`, or adjust the mapping with `adjust X`, or re-derive with `different bucket`.

Reply ✅ when the mapping is confirmed.

---

## Step 4: Read the shortlist (5 min)

Open `my-work/influencer-scout/<today>-shortlist.md`.

You will see 5 creators, each with:

- **Why this creator:** 3-5 line read on the fit
- **The fit on the brand DNA:** audience, voice, price tier, engagement health
- **The five red-flag checks:** pass / yellow / fail on each, with the numbers
- **Decision:** SHORTLIST / TEST POST / WALK
- **Rate anchor:** platform estimate, your counter, the walk price
- **First outreach email:** ready to paste into Gmail
- **Counter-offer script:** ready if they push back at platform rate

The skill will deliberately surface creators across tiers. The five-figure-rupee micro is usually the right first buy, not the lakh-rupee mid. Trust the rank.

---

## Step 5: Pick one creator to act on this week (5 min)

Pick the top WARM-LEAD creator if there is one, a creator who already mentions your brand organically in `brand_mentions_90d`. Warm leads close 30-40% faster and 15-20% cheaper than cold outreach.

If no warm lead, pick the highest-fit SHORTLIST creator from the top of the file.

What you do this week:

1. Copy the **first outreach email** from the file
2. Paste into Gmail or your CRM, change nothing
3. Send manually (the skill will never auto-send)
4. If the creator replies with the platform-listed rate, paste the **counter-offer script**
5. If they accept the counter, draft a one-page contract using the standard clauses from `references/module-11-influencer-scout/negotiation-playbook.md`

You are not running the whole campaign in this session. You are starting one conversation.

---

## Step 6: The marketplace-vs-creator copy contrast (5 min)

Open the creator's most recent organic post (from their handle on Instagram or YouTube) AND your own latest content from the Content Lead (Session 4) side by side.

The voice difference is the point. The creator's voice is the creator's voice. Your job is to give them a clean brief on the message, your three key claims, your compliance flags, the disclosure language, and let the voice be theirs.

Founders who write the script for the creator get refusals or stiff posts that underperform. Founders who give a brief and let go get the creator's actual audience trust. The difference is 2-4x conversion on the same spend.

---

## Step 7: Plan the 4-week ladder (POWER only) (~10 min)

If you ran POWER scope, open `my-work/influencer-scout/<today>-campaign-4week.md`.

The plan ladders the campaign:

- **Week 1:** seed 3 nano creators with gifting only + sign 2 micro for one reel each
- **Week 2:** 1 mid-tier dedicated post + re-use Week-1 creatives as paid ads
- **Week 3:** measurement window, no new posts, decide who to renew
- **Week 4:** renew the highest-performer or rotate to a warm-bench creator

The point of the ladder is that nano + micro produce 70% of the conversion at 20% of the cost when sequenced right. The mid-tier post amplifies what the nano + micro already validated.

Most founders skip the ladder, buy one macro, and learn the hard way.

---

## What You Just Built

A shortlist that holds up to data scrutiny. An outreach email per creator that you can send today. A counter-offer ready for the rate pushback that will come. A negotiation playbook you can reuse for the next ten campaigns, not just this one.

If you ran POWER, you also have a campaign calendar that paces spend instead of compressing it into one big macro post.

---

## What's Next

If you came here from the Capstone (Session 10), this was your add-on. The Captain in Session 10 already reads `my-work/influencer-scout/<date>-index.md` if you generated one, it shows up in the weekly synthesis.

If you came here mid-workshop, return to the session you paused on. The Influencer Scout is one of several Day-2 add-ons; it does not block Sessions 8, 9 or the Capstone.

---

## If You Get Stuck

| Symptom | Fix |
|---|---|
| Skill says "no bucket match" | Your CLAUDE.md does not name a clear product category. Add a one-line "category: X" to Section 1 of CLAUDE.md and re-run. |
| Skill shortlists only macros | Your brand DNA is over-stating reach goals. Add audience tier (Tier-1 / Tier-2 / pan-India) to CLAUDE.md. |
| All 5 creators get yellow / fail | The bucket is right but the audience filter is tight. Re-run with one less audience constraint (drop the age skew, keep geography). |
| Outreach draft sounds generic | The skill did not have enough brand voice in CLAUDE.md Section 3 (voice rules). Add 3-5 voice rules and re-run. |
| Counter-offer script anchors too low | You can override: edit the rate-anchor line in the shortlist file and ask the skill to regenerate the script at the new number. |
| Modash MCP says "not connected" | The skill runs against the sample pool until Modash MCP is configured. Sample pool is sufficient for this workshop session. |

For anything not on this list, raise hand in the workshop chat.
