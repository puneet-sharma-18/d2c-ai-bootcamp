# Vendor Email — Co-packer Batch Quality Concern
Use when: a batch returned from the contract manufacturer fails the in-house QC check (texture, fragrance trace, active concentration off-spec, label print issue) AND the affected SKU is one of our top 5 by volume.
Tone: professional, direct, founder-grade. The co-packer has a long memory; the tone in this email shapes the next 12 months of the relationship.

## Subject lines (3 variants)
1. Batch {batch-id} QC fail: action needed by {date}
2. {SKU name} batch quality concern — call this week?
3. QC variance on {batch-id}: holding from dispatch pending review

## Body

Hi {plant-manager-name},

Writing to flag a QC issue on Batch {batch-id} of {SKU name}, manufactured on {date}.

Specifically:
- {Observation 1: e.g. "Active concentration on Cradle Cap Balm tested at 0.84% vs spec 1.0% w/w (sample size N=12, our in-house Karl Fischer titration)"}
- {Observation 2: e.g. "Fragrance trace detected in 6 of 50 sampled bottles. Our spec is fragrance-free; FTIR scan attached"}
- {Observation 3: e.g. "Label adhesive lift on 11 of 50 sampled bottles; storage at 28°C accelerates"}

We are holding the batch from dispatch pending your team's review. Quantity held: {units}.

Two questions:
1. Root cause analysis from your end on each of the above. Was the variance batch-specific (one shift, one run) or process-systemic (formulation drift, raw-material substitution)? We need this in writing before we accept any replacement.
2. The path to remediation. Options as I see them: (a) full batch rework at your cost, (b) full batch reject + replacement batch within {N} days, (c) partial release of the units that test within spec + reject the rest. I lean (b) for the active variance specifically since it affects regulatory compliance.

I would like a call Thursday or Friday this week to walk through the root cause and lock the path. Can your QA lead and your plant manager both attend?

If we cannot resolve this within 14 days, we will need to talk about the next quarter's production plan and our backup contract manufacturer options. I would rather not. Hoping we resolve this fast.

Best
Riya
Founder, Little Lab

## What to attach
- The in-house QC test results as a single-page PDF (active % readings, fragrance FTIR scan if relevant, adhesive-lift photos)
- The batch-id manifest and the affected lot numbers as a CSV
- Our original product spec document (re-sent so there is no ambiguity on the comparison baseline)

## What NOT to write
- Do not name a competing contract manufacturer in writing. The "backup CM options" line is the position; the names belong in a phone call.
- Do not threaten escalation to FSSAI on first written round. That is the absolute last resort and never written until the relationship is past saving.
- Do not include customer complaint quotes verbatim — describe the operational symptom (units affected, % out of spec) in the language of QC, not in the language of customer reviews.
- Do not commit to a specific remediation choice in writing before the call. Keep options open.

## If they do not reply within 48h
- Phone call to the plant manager. If no answer, call the founder/promoter directly per the contract manufacturer agreement escalation matrix.
- The held batch stays held. Do not release any unit from a failed QC batch under time pressure, even if we are stocking out on the SKU. Stockout SOP-02 fires for that.

## Documentation
- Every batch QC concern logged in `my-work/ops-manager/batch-quality-log.md` (POWER scope file)
- This template is the v1 vendor-grade communication; founder personally reviews until 3 successful uses, then delegates to ops freelancer
