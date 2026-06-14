# Module 11: Influencer Scout (add-on)

Teaching dataset for the influencer discovery + negotiation session. The data is synthetic but shaped to mirror what Modash (modash.io) actually returns, so anything a founder learns to read here transfers to the real platform on day one of a paid subscription.

## What's in this folder

| File | What it is |
|---|---|
| `modash-data-shape.md` | Field-by-field cheat sheet. What each Modash filter and profile field means. Read this first. |
| `sample-creator-pool.json` | 40 synthetic Indian creators across 11 brand buckets. The dataset the skill, the session and the founder all work against. |
| `rate-card-benchmarks-india.md` | INR rate ranges per tier per platform, multipliers for usage rights, what discounts the brand can earn. |
| `negotiation-playbook.md` | The five must-spec contract items, deliverable menu, counter-offer scripts, walk-away signals. |
| `red-flag-cheatsheet.md` | One-page decision tree for the discovery half. The five checks in order. |
| `README.md` (this file) | Index, bucket map, how the data was built. |

The skill `.claude/skills/influencer-scout/SKILL.md` and the founder-facing `session-11-influencer-scout.md` at the repo root both read this folder.

## Bucket → brand → creator map

Every D2C brand in the May 2026 cohort has at least three plausible-fit creators in the pool. Cross-bucket creators (e.g. a wellness creator who fits VAHDAM and Sanfe) appear once but list every relevant bucket in their `buckets` field.

| Bucket | Cohort brands | Creators in pool |
|---|---|---|
| `coffee` | Blue Tokai | 001, 002, 003, 004 (+ red flag) |
| `tea_wellness` | VAHDAM | 005, 006, 007, 008 (+ red flag), 015, 018, 031, 038 |
| `premium_apparel_lifestyle` | Nicobar, Miss Chase | 009, 010, 011, 012, 036, 037, 038 |
| `travel_luggage` | Nasher Miles | 013, 014, 015, 036 |
| `kids` | Tuco Kids | 014, 016, 017 (+ red flag), 018, 040 |
| `femcare` | Sanfe | 017, 019, 020, 021, 038, 040 |
| `body_care_skincare` | Eora, RSH Global (Joy/Karis/Orimii) | 007, 020, 022, 023, 024, 025, 037 |
| `rte_food` | Home Kouzina | 026, 027, 028, 039 |
| `clean_farm_food` | Red Otter Farms | 028, 029, 030, 031, 039 |
| `beauty_cosmetics` | Looks21 | 011, 012, 023, 032, 033 |
| `b2b_linkedin` | Spectra, Berries Advisory, TheFoundersFin, Inephos, Progressive Lifestyles | 034, 035 |

Two cohort members map differently:
- **Progressive Lifestyles** is a B2B brand-management company for beauty + fashion brands (Carlton London Beauty, Barry M, Treehut, Daniel Klein, Mark Maddox). They use the dataset twice: once to find influencers for the brands they manage (beauty + apparel buckets), once for B2B founder-voice content (b2b_linkedin bucket).
- **Looks21** is bucketed as beauty/cosmetics based on its Amazon and Naaptol footprint and the Fashion21 Cosmetics lineage. If they self-identify as fashion-first instead, the apparel bucket creators 011 / 012 / 036 / 037 also fit.

## How the dataset is composed (so it teaches, not just demos)

Every creator has a teaching role on top of being a plausible buy:

1. **Bullseye fits:** most creators are a clean shortlist candidate for at least one brand. They organically mention the brand or sit precisely in its audience.
2. **Red-flag teaching cases:** creators 004 (Layla), 008 (Rhea), and 017 (Aditi) look like the obvious big-reach buys and are deliberately broken. Used in the session's "why follower count is a trap" beat.
3. **Tier coverage:** nano (9 creators), micro (16), mid (13), macro/mega (2). The session teaches founders to ladder a campaign across tiers, not just buy a macro and hope.
4. **Cross-bucket creators:** 007, 015, 018, 028, 031, 036, 037, 038 fit multiple brands. The session uses these to teach negotiation leverage (creator gets multiple offers, founder needs differentiated ask).
5. **Format coverage:** Instagram (32), YouTube (6), LinkedIn (2). Rate cards localised to INR.
6. **Competitor traps:** several creators have run paid for direct competitors in the last 90 days. Founders learn to read `brand_mentions_90d` and `recent_paid_collabs` before reaching out.

## What's NOT in the dataset (deliberate)

- No real names, no scraped handles. Synthetic by design.
- No paid contact emails / DMs. The dataset is for reading and decisioning; outreach copy is written in the negotiation half of the session.
- No US/EU-only creators except where a brand specifically needs diaspora reach (VAHDAM, Nasher Miles).
- No comment sentiment, no story metrics, no DM response time. Modash exposes these; this dataset deliberately stops at the fields a founder makes a yes/no decision on, to keep the teaching pass under 90 minutes.

## Worked examples on the two canonical brands

Both example brands now have a shortlist + index that instructors can flash during the session:

- `examples/little-lab/my-work/influencer-scout/2026-05-13-shortlist.md` and `2026-05-13-index.md`. Little Lab is the clean bucket-match case: `body_care_skincare` + `kids` cross-bucket, 5 creators laddered nano to mid, one walk recommendation (cre_017 Toddler Diaries, the vanity-metric mid-tier trap), total commit ₹2.71L.
- `examples/the-paan-legacy/my-work/influencer-scout/2026-05-13-shortlist.md` and `2026-05-13-index.md`. The Paan Legacy is the harder no-direct-bucket case: no paan-native creator exists in the 40-creator pool, so the shortlist composes three adjacencies (ritual-wellness, festive-food, B2B-Diwali) into a campaign. Total commit ₹2.24L for the September-October window.

Both worked examples use the brevity convention (top 2 creators in full detail, 3-5 compact) so the files stay flashable in a workshop slot.

## Pending touches (not yet wired)

1. Real Modash MCP. The skill currently reads `sample-creator-pool.json`. When a Modash MCP becomes available, swap the JSON read for a live API call in `.claude/skills/influencer-scout/SKILL.md` Step 1.
2. Modash auto-tracking of post performance after publish. Currently the session asks the founder to track manually for 14 days. Once Modash MCP is live, the skill can be re-run with post metrics auto-pulled.
