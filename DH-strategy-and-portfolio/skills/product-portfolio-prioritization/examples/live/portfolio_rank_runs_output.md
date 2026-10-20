Output of scripts/portfolio_rank.py on the files named, run 20 October 2026. Inputs are illustrative or live test inputs, never a person's judgment.

## mcda examples/live/mcda_partner_options.json (check against a saved live response)
Input label: Trimmed copy of a live VITAL Digital Health Library response, 19 October 2026. Fields kept as returned; long lists shortened where marked. Scores, weights and RICE inputs are illustrative inputs typed for the measurement, not a person's numbers.

Ranking on the person's weights and scores (EVIDEM weighted sum, 0 to 100):

| Rank | Item | Value | Largest contribution |
|---|---|---|---|
| 1 | Behavioral health group practice network | 77.50 | buyer_access (35.00) |
| 2 | Regional health-system reseller | 63.75 | buyer_access (26.25) |
| 3 | EHR marketplace listing | 62.50 | compliance_fit (25.00) |

Check against the tool's own values:
- Behavioral health group practice network: tool 77.5 ; recomputed 77.50 ; same
- Regional health-system reseller: tool 63.75 ; recomputed 63.75 ; same
- EHR marketplace listing: tool 62.5 ; recomputed 62.50 ; same

The ranking is arithmetic on the person's numbers, not a decision.

## swap examples/live/analytics_mcda_segments_illustrative.json (reproduces the 0.36 and 0.04 swap points recorded by the go-to-market build)
Input label: Scores and weights are illustrative test inputs written for this build, not a person's judgment.

Where the ranking would flip (one weight moved, the others kept in proportion):

| Pair (higher first) | Criterion | Current weight | Swap at |
|---|---|---|---|
| DE statutory insured, insomnia (DiGA prescription) over US Medicare behavioral health practices (DMHT codes) | payer_route | 0.35 | 0.04 |
| DE statutory insured, insomnia (DiGA prescription) over US Medicare behavioral health practices (DMHT codes) | reachability | 0.25 | no swap between 0 and 1 |
| DE statutory insured, insomnia (DiGA prescription) over US Medicare behavioral health practices (DMHT codes) | evidence_fit | 0.25 | no swap between 0 and 1 |
| DE statutory insured, insomnia (DiGA prescription) over US Medicare behavioral health practices (DMHT codes) | competition | 0.15 | 0.36 |
| US Medicare behavioral health practices (DMHT codes) over US self-insured employers | payer_route | 0.35 | no swap between 0 and 1 |
| US Medicare behavioral health practices (DMHT codes) over US self-insured employers | reachability | 0.25 | no swap between 0 and 1 |
| US Medicare behavioral health practices (DMHT codes) over US self-insured employers | evidence_fit | 0.25 | no swap between 0 and 1 |
| US Medicare behavioral health practices (DMHT codes) over US self-insured employers | competition | 0.15 | no swap between 0 and 1 |

Closest call: DE statutory insured, insomnia (DiGA prescription) over US Medicare behavioral health practices (DMHT codes) swaps if competition moves from 0.15 to 0.36.
Weights are the person's; a swap point is a test of their weights, not a proposal to change them.

## rice examples/live/rice_confidence_fraction.json (confidence scale trap)
| Item | Reach | Impact | Confidence sent | Recomputed score (confidence as percent) | Tool score | Note |
|---|---|---|---|---|---|---|
| Co-sell pilot with group practice network | 400 | 2 | 0.5 | 1.3333 | 1.3333 | confidence sent as a fraction; the tool reads percent and divides by 100 again (register N5): resend as a percent |
| EHR marketplace listing | 1500 | 0.5 | 0.8 | 1.5000 | 1.5 | confidence sent as a fraction; the tool reads percent and divides by 100 again (register N5): resend as a percent |
| Reseller onboarding kit | 250 | 1 | 0.8 | 2.0000 | 2 | confidence sent as a fraction; the tool reads percent and divides by 100 again (register N5): resend as a percent |

Reach, impact, confidence and effort are the person's estimates; RICE ranks them, it does not decide.

## mcda, swap and capacity on examples/sample-data (illustrative portfolio)
Input label: ILLUSTRATIVE: programs, criteria, weights and 0 to 4 scores written for this build to show the method. They are not any company's data or judgment.

Ranking on the person's weights and scores (EVIDEM weighted sum, 0 to 100):

| Rank | Item | Value | Largest contribution |
|---|---|---|---|
| 1 | Program A: insomnia DTx label expansion | 85.00 | evidence_readiness (25.00) |
| 2 | Program B: anxiety DTx pivotal study | 72.50 | unmet_need (30.00) |
| 3 | Program C: clinician dashboard add-on | 65.00 | evidence_readiness (18.75) |
| 4 | Program D: pediatric ADHD prototype | 60.00 | unmet_need (30.00) |

The ranking is arithmetic on the person's numbers, not a decision.
Input label: ILLUSTRATIVE: programs, criteria, weights and 0 to 4 scores written for this build to show the method. They are not any company's data or judgment.

Where the ranking would flip (one weight moved, the others kept in proportion):

| Pair (higher first) | Criterion | Current weight | Swap at |
|---|---|---|---|
| Program A: insomnia DTx label expansion over Program B: anxiety DTx pivotal study | unmet_need | 0.30 | 0.53 |
| Program A: insomnia DTx label expansion over Program B: anxiety DTx pivotal study | evidence_readiness | 0.25 | no swap between 0 and 1 |
| Program A: insomnia DTx label expansion over Program B: anxiety DTx pivotal study | regulatory_path_clarity | 0.15 | no swap between 0 and 1 |
| Program A: insomnia DTx label expansion over Program B: anxiety DTx pivotal study | strategic_fit | 0.20 | 0.47 |
| Program A: insomnia DTx label expansion over Program B: anxiety DTx pivotal study | capacity_fit | 0.10 | no swap between 0 and 1 |
| Program B: anxiety DTx pivotal study over Program C: clinician dashboard add-on | unmet_need | 0.30 | 0.18 |
| Program B: anxiety DTx pivotal study over Program C: clinician dashboard add-on | evidence_readiness | 0.25 | 0.42 |
| Program B: anxiety DTx pivotal study over Program C: clinician dashboard add-on | regulatory_path_clarity | 0.15 | 0.35 |
| Program B: anxiety DTx pivotal study over Program C: clinician dashboard add-on | strategic_fit | 0.20 | 0.06 |
| Program B: anxiety DTx pivotal study over Program C: clinician dashboard add-on | capacity_fit | 0.10 | 0.18 |
| Program C: clinician dashboard add-on over Program D: pediatric ADHD prototype | unmet_need | 0.30 | 0.36 |
| Program C: clinician dashboard add-on over Program D: pediatric ADHD prototype | evidence_readiness | 0.25 | 0.17 |
| Program C: clinician dashboard add-on over Program D: pediatric ADHD prototype | regulatory_path_clarity | 0.15 | 0.06 |
| Program C: clinician dashboard add-on over Program D: pediatric ADHD prototype | strategic_fit | 0.20 | 0.33 |
| Program C: clinician dashboard add-on over Program D: pediatric ADHD prototype | capacity_fit | 0.10 | no swap between 0 and 1 |

Closest call: Program C: clinician dashboard add-on over Program D: pediatric ADHD prototype swaps if unmet_need moves from 0.30 to 0.36.
Weights are the person's; a swap point is a test of their weights, not a proposal to change them.
| Order | Item | Decision (the person's) | Capacity use (FTE) | Running total of continue items |
|---|---|---|---|---|
| 1 | Program A: insomnia DTx label expansion | continue | 5 | 5.0 |
| 2 | Program B: anxiety DTx pivotal study | continue | 7 | 12.0 |
| 3 | Program C: clinician dashboard add-on | continue | 3 | 15.0 |
| 4 | Program D: pediatric ADHD prototype | delay | 4 |  |

Capacity named: 14 FTE. Continue items use 15.0 FTE.
First continue item past the named capacity: Program C: clinician dashboard add-on.

## swap --scores on examples/sample-data/portfolio_scores_illustrative.json (one-point score changes; run 20 October 2026)
Input label: ILLUSTRATIVE: programs, criteria, weights and 0 to 4 scores written for this build to show the method. They are not any company's data or judgment.

One-point score changes that tie or reverse each adjacent pair (one score moved by 1, within 0 to 4):

| Pair (higher first) | Values | Gap | Change | Effect of one point | Result |
|---|---|---|---|---|---|
| Program A: insomnia DTx label expansion over Program B: anxiety DTx pivotal study | 85.00 / 72.50 | 12.50 | no single one-point change | largest 7.50 | holds |
| Program B: anxiety DTx pivotal study over Program C: clinician dashboard add-on | 72.50 / 65.00 | 7.50 | Program B: anxiety DTx pivotal study unmet_need from 4 to 3 | 7.50 | tie |
| Program B: anxiety DTx pivotal study over Program C: clinician dashboard add-on | 72.50 / 65.00 | 7.50 | Program C: clinician dashboard add-on unmet_need from 2 to 3 | 7.50 | tie |
| Program C: clinician dashboard add-on over Program D: pediatric ADHD prototype | 65.00 / 60.00 | 5.00 | Program C: clinician dashboard add-on unmet_need from 2 to 1 | 7.50 | reverses |
| Program C: clinician dashboard add-on over Program D: pediatric ADHD prototype | 65.00 / 60.00 | 5.00 | Program C: clinician dashboard add-on evidence_readiness from 3 to 2 | 6.25 | reverses |
| Program C: clinician dashboard add-on over Program D: pediatric ADHD prototype | 65.00 / 60.00 | 5.00 | Program D: pediatric ADHD prototype evidence_readiness from 1 to 2 | 6.25 | reverses |
| Program C: clinician dashboard add-on over Program D: pediatric ADHD prototype | 65.00 / 60.00 | 5.00 | Program C: clinician dashboard add-on strategic_fit from 2 to 1 | 5.00 | tie |
| Program C: clinician dashboard add-on over Program D: pediatric ADHD prototype | 65.00 / 60.00 | 5.00 | Program D: pediatric ADHD prototype strategic_fit from 3 to 4 | 5.00 | tie |

Scores are the person's; a one-point change is a test of their scores, not a proposed score.
