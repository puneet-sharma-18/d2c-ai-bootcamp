# Modash data shape (teaching reference)

Modash is a creator-discovery platform with 250M+ Instagram, YouTube and TikTok profiles (1,000+ follower minimum). Brands query it through their dashboard or the Discovery / RAW APIs. Source: docs.modash.io and the public product pages on modash.io.

This file is the cheat sheet founders read before working with the sample data in `sample-creator-pool.json`. The JSON file mirrors the fields and naming that Modash itself exposes so the teaching beat lands when a founder later signs up.

## Search filters Modash exposes

Two layers. Influencer filters describe the *creator*. Audience filters describe the *people who follow that creator*. Most useful searches combine both.

### Influencer filters
- `follower_count` range
- `engagement_rate` (avg interactions / followers, last N posts)
- `country`, `city`
- `language`
- `bio_keywords` (free-text match on the creator's bio)
- `hashtags_used` (creator's own posts)
- `email_available` (whether Modash has parsed a contact email)
- `follower_growth_30d` (organic trend)
- `fake_follower_pct` (Modash's estimate of bots and inactive accounts in the creator's follower base)
- `categories` (Modash-assigned content categories: food, fashion, parenting, fitness, etc.)
- `brand_mentions` (other brands the creator has tagged, paid or organic)

### Audience filters
- `audience_country`, `audience_city`
- `audience_age` buckets
- `audience_gender`
- `audience_interests` (lifestyle/topic affinities)
- `audience_language`
- `audience_fake_follower_pct`
- `audience_reachability` (how many followers the creator actually reaches in the algorithm)

## Creator profile / report fields

When you click into a creator, Modash returns a fuller profile. The sample-creator-pool.json file uses these field names:

- `handle`, `platform`, `display_name`, `bio`, `url`, `country`, `city`, `languages`
- `tier` (`nano` 1k-10k, `micro` 10k-100k, `mid` 100k-500k, `macro` 500k-1M+, `mega` 1M+)
- `followers`, `following`, `media_count`
- `engagement_rate`, `avg_likes`, `avg_comments`, `avg_reel_views`
- `follower_growth_30d`, `fake_follower_pct`, `credibility_score` (= `1 - fake_follower_pct`, kept separately for skim-reading)
- `email_available`, `categories`, `top_hashtags`
- `audience`: `gender` split, `age` buckets, `geo_country`, `geo_city_top5`, `languages`, `interests`
- `brand_mentions_90d`, `paid_post_ratio_30d`, `recent_paid_collabs`
- `estimated_rate_inr` per deliverable type (Modash itself shows USD; we localise to INR for the cohort)
- `red_flags` (synthetic field we added for teaching, Modash surfaces the underlying signals but does not flag them as a list)
- `fit_notes` (synthetic field, single line on why the creator fits a bucket)

## How to read a creator profile (the teaching beat)

A creator can look great on follower count and still be a bad buy. Three checks before anything else:

1. **Credibility:** `fake_follower_pct` above 25% means a third of the followers are bots or inactive. Common in macros who bought growth. Filter < 20% as a default.
2. **Audience-niche fit:** `audience.geo_country` and `audience.age` matter more than the creator's own location. A Delhi creator with 60% Pakistan audience is useless to a brand shipping only inside India.
3. **Engagement context:** 3% ER on a 50k micro is healthy; 3% ER on a 5k nano is mediocre. The smaller the account, the higher the ER should be. Below 1.5% on a micro = stale or bought.

Then the buyer questions:
- What's the `paid_post_ratio_30d`? Above 50% and the audience tunes out sponsored content.
- What `brand_mentions_90d` show up? If a direct competitor is in there, walk away or wait out the exclusivity window.
- Does `recent_paid_collabs` include the engagement rate of those paid posts? Modash shows it. A creator whose organic ER is 6% but whose paid ER is 1.2% is selling a graveyard.

## Rate estimation

Modash gives an estimate based on tier, geography, platform and historical collabs. Treat it as a ceiling, not a floor. Indian creators almost always negotiate 20-40% below the listed estimate, especially for product-gifting or affiliate components. Rate-card benchmarks for the Indian market live in `rate-card-benchmarks-india.md`.
