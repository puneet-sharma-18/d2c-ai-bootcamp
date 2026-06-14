# Red-flag cheatsheet: read this before sending any outreach

A creator can look perfect on follower count and still cost the brand more than it makes back. Five reads, in order. If any one fails, the creator does not make the shortlist.

## 1. Credibility: is the audience real?

Look at `fake_follower_pct` and `credibility_score`.

| `fake_follower_pct` | Verdict |
|---|---|
| Under 10% | Clean. Proceed. |
| 10-20% | Normal. Proceed but discount the reach by the same %. |
| 20-30% | Yellow flag. Worth a smaller test post before a full deal. |
| Over 30% | Walk. Bought growth, dormant followers, or audience-buy farm. The reach math will not work. |

Bigger accounts have higher fake-follower rates as a rule. A 6-8% rate on a mega is exceptional. A 6-8% rate on a nano is the floor.

## 2. Audience geo: do they live where you ship?

Look at `audience.geo_country` and `audience.geo_city_top5`.

For an Indian D2C brand shipping inside India, the test is:

| `geo_country.IN` | Verdict |
|---|---|
| Over 80% | Strong. Most of the spend reaches a payable audience. |
| 60-80% | Acceptable if the rest is NRI in your target diaspora (US, UK, CA, AE). |
| Under 60% | Walk unless you have a global storefront. A "750k follower" Indian creator with 40% Pakistan + Bangladesh audience is a 450k creator for you. |

Cross-check `audience.geo_city_top5`. If 2 of 5 top cities are outside India and the brand does not ship there, the addressable reach is smaller than the headline.

## 3. Engagement context: is the engagement healthy for the tier?

ER thresholds are not constant. Smaller accounts must show higher ER.

| Tier | Healthy ER | Below this = stale or bought |
|---|---|---|
| Nano (1k-10k) | 6-12% | Under 4% |
| Micro (10k-100k) | 3-7% | Under 2% |
| Mid (100k-500k) | 2-5% | Under 1.5% |
| Macro (500k-1M) | 1-3% | Under 1% |
| Mega (1M+) | 0.8-2% | Under 0.7% |

Cross-check the paid-post ER vs the organic ER from `recent_paid_collabs`. If organic ER is 6% but paid ER is 1%, the audience tunes out sponsored content. Walk or negotiate a lower rate.

## 4. Saturation: is the audience tired of ads on this account?

Look at `paid_post_ratio_30d`.

| `paid_post_ratio_30d` | Verdict |
|---|---|
| Under 20% | Healthy. Audience still trusts the creator's recommendations. |
| 20-40% | Normal for a working creator. Proceed but expect average lift, not breakout. |
| 40-60% | Saturated. Audience expects sponsored content; convert rates drop. |
| Over 60% | Walk. The account is functioning as a paid placement channel; organic trust eroded. |

## 5. Competitor traps: is anyone in your category already in there?

Look at `brand_mentions_90d` and `recent_paid_collabs`.

Two questions:

1. **Has the creator posted for a direct competitor in the last 90 days?** If yes, you either wait the standard 60-day exclusivity-from-post window OR you negotiate a category-shifted format (your skincare brand's body lotion, not its face cream, if the competitor was face care). Walk if the competitor relationship is recurring (3+ posts in 6 months).
2. **Is your brand already mentioned organically?** If yes, this is the warm-lead creator. Start outreach here. The deal closes faster and cheaper because there's already affinity.

## The 30-second decision

After running the five checks, you should be able to say one of three things:

**SHORTLIST:** credibility green, geo green, ER healthy for tier, saturation under 30%, no competitor in last 90d (or competitor cleared 60+ days ago).

**TEST POST:** credibility yellow (10-20% fake), or saturation 30-40%, or competitor 60-90 days back. Commit to one reel before a multi-post deal. Pay full rate but limit scope.

**WALK:** any one of: credibility over 25% fake, IN audience under 60%, ER below tier floor, saturation over 50%, direct competitor in last 30 days.

## The three red-flag creators in the sample pool

Use these as the teaching cases for the discovery session.

| Creator | Why it's a teaching case |
|---|---|
| `cre_004` Layla Lifestyle | 720k followers but 38% fake, audience 38% non-India, paid post ratio 71%. Walk despite massive headline reach. |
| `cre_008` Wellness with R | 2.1M followers, the obvious VAHDAM / Sanfe / Joy pick, but 41% fake, 49% non-India, ER 0.9%, agency-gated. Best per-rupee miss in the dataset. |
| `cre_017` Toddler Diaries | 261k mid-tier kid creator. Looks like the obvious Tuco buy. ER falling 4% → 2.4% over 6 months, paid-post ratio 51%, fake rate 21%. The classic "test one reel before signing a multi-post" case. |
