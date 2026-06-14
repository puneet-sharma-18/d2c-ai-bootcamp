# Brand Safety Checklist

Every piece of content the Content Lead produces is checked against this list before saving. Failures get appended to the piece file as `## SAFETY FLAGS` with the specific issue named. The piece is saved anyway. The founder reviews flags before publishing.

This is intentionally defensive. Better a flagged piece you reject than a takedown notice or a customer complaint later.

## The seven checks

### 1. Banned words

Every piece is scanned against the "Never" list in CLAUDE.md Section 7. The list typically includes:

- Generic AI tells the founder hates: "elevate", "unlock", "leverage", "delve", "navigate" (as a metaphor), "in today's fast-paced world", "game-changer"
- Category cliches the brand rejects: e.g. "premium" for a value brand, "natural" for a clean-label brand that prefers "single-origin"
- Words that break the founder's voice: e.g. "synergy" for a casual brand

Flag: any banned word that appears in the piece, with the exact line.

### 2. Regulated claims

Every piece is scanned against CLAUDE.md compliance section. If the brand operates in food, beauty, health, baby, wellness, ayurveda or nutraceutical categories, certain claims need substantiation:

- **Food / FSSAI**: "preservative-free", "no added sugar", "high protein", "fortified with X", "Y% RDA"
- **Beauty**: "dermatologically tested", "clinically proven", "anti-ageing", "hypoallergenic", "results in N days"
- **Health / wellness**: any "treats", "cures", "prevents", "boosts immunity", "burns fat" claim
- **Baby**: "100% safe", "doctor-recommended", any age claim that needs back-up
- **Ayurveda / Ayush**: any traditional claim that needs Ayush registration to make in commercial copy

Flag: any claim that needs proof, with a note "needs substantiation. Pull from your lab report or strike from copy."

### 3. Invented numbers

Every statistic, comparison or percentage is checked against:
- CLAUDE.md (does it appear there)
- The Market Analyst report (does it appear there)
- The Voice of Customer report (does it appear there)
- The Shopify MCP data (does it match orders, inventory, customer count)

If a number does not trace back to one of those sources, it is flagged.

Examples that get flagged:
- "Loved by 10,000+ customers" (unless CLAUDE.md says so or Shopify confirms)
- "30% better than the leading brand" (unless Market Analyst sourced it)
- "We donate 5% of every sale" (unless CLAUDE.md says so)

Flag: any number with no source. Replace with {placeholder} or strike.

### 4. Customer quote authenticity

Every customer quote in a piece must trace to `my-work/voice-of-customer/`. The Content Lead is not allowed to invent testimonials.

If a piece uses a quote, the safety check confirms:
- The quote text matches a verbatim line in the VoC report
- The persona attribution matches the persona card in the VoC report
- PII is stripped (no full name, no phone, no email, no order ID)

Flag: any quote that cannot be traced. Replace with a real one or strike.

### 5. Tone and voice consistency

The piece should read like the founder, not like a generic D2C voice. The check:

- Does the piece use at least one "Always" phrase from CLAUDE.md naturally?
- Does the piece avoid all "Never" phrases?
- Is the reading age in the range CLAUDE.md set?
- Does the closing match the founder's typical sign-off (if applicable)?

Flag: tone shift. Note which dimension drifted (e.g. "Reading age is Class 12, CLAUDE.md says Class 8. Simplify.").

### 6. Anti-positioning

The piece should not contradict the "What we will never do" line in CLAUDE.md Section 3.

Examples of contradictions:
- Brand says "we will never compete on price" → piece runs a discount headline
- Brand says "we never claim what we cannot prove" → piece makes a clinical claim without substantiation
- Brand says "we never use stock imagery" → piece's image hint says "stock photo of [thing]"

Flag: anti-positioning violation, quote the line from Section 3, name the conflict.

### 7. Channel format compliance

The piece respects the format rules of its channel:

- Instagram caption: 80-150 words, one CTA
- Amazon A+ hero: 60 chars max
- Flipkart title: 200 chars max
- Reel script: actual 30-second beat structure
- Email subject: 9 words max

Flag: format violation, name the spec.

## Format of a SAFETY FLAGS section

When a piece fails one or more checks, the Content Lead appends to the bottom of the piece file:

```markdown
## SAFETY FLAGS

1. **Banned word** in line "Discover our amazing new collection". "Amazing" is on
   the Never list in CLAUDE.md Section 7. Replace with a specific word from the
   Always list, or strike.

2. **Regulated claim** in line "Clinically tested for sensitive skin". Needs lab
   report reference. Pull from your dermatology report or strike "clinically
   tested".

3. **Invented number** in line "Trusted by 50,000 mothers across India". No
   source. Replace with the real customer count (Shopify MCP can pull this) or
   strike.
```

The founder reads these before publishing, fixes or strikes, and ships.

## What the safety pass does NOT cover

- **Legal review for trademarks, copyright, third-party brand mentions.** Out of scope. The founder's legal counsel reviews before any large-scale paid promotion.
- **Platform-specific policy compliance** (Meta ad policy, Amazon listing policy, Flipkart restricted words list). Per-platform pre-flight is the Performance Marketer module's job on Day 2 for paid, and the Marketplace Editor's job for marketplace listings.
- **SEO keyword density and search intent alignment.** Out of scope for content quality pass. Day 2 has a Storefront Specialist module that handles SEO.

The Content Lead's safety pass is about brand integrity and compliance gates that must hold across all 20 pieces. The deeper layers belong to other teammates.
