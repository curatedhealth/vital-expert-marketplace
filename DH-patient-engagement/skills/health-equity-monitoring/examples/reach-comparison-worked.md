# Worked run: A2 Reach and outcome comparison, then B1 review

Run of 19 October 2026. The program, the counts and the rules are illustrative: the counts are in `examples/sample-data/rpm_equity_illustrative.csv`, written for this example and labeled illustrative; they are not real data. The script output and the connector outputs are real.

## The request

"Our remote blood pressure monitoring program ran 1 July to 30 September 2026. Reached means enrolled and sent at least one reading in the first 30 days; outcome means blood pressure measured at 90 days and under the control target we use. Here are counts by language, age band and SVI band (we mapped home tracts to the U.S. SVI database). Our small-cell rule is 11. Compare against English, 45 to 64, and the lowest SVI band. Our rule: reach in every subgroup at least 0.85 of the reference. Owner for language is Ana Ruiz's enrollment team; nobody owns age yet. Is a published review of digital hypertension programs in disparity populations relevant context?"

## Calls made

1. `python scripts/equity_compare.py examples/sample-data/rpm_equity_illustrative.csv --min-cell 11 --reference "preferred language=English" --reference "age band=45-64" --reference "SVI band (US database)=0 to 0.25"` (local)
2. `literature.search_literature {query: "digital health intervention engagement disparities race ethnicity income older adults", filters: {date_from: "2020-01-01"}, limit: 6}` (counted; `examples/live/search_literature.json`)
3. `verify.qualify_source {doi: "10.1001/jamanetworkopen.2023.56070"}` then `verify.check_claim` twice, once with the claim in the passage's direction and once negated (counted; `examples/live/verify_katz.json`)

## Script output (verbatim)

Small-cell rule (the person's): counts from 1 to 10 suppressed.
Aggregate counts only. No verdicts: whether a difference matters is the person's rule.

## preferred language
Eligible 2400, reached 1455; not recorded: 174 of eligible (7.2%). Reference: English.

| Subgroup | Eligible | Reached | Reach rate (95% CI) | Diff vs ref (pp) | Ratio | Share of eligible / of reached | Outcome met / measured | Outcome rate (95% CI) | Outcome diff (pp) | Suppression |
|---|---|---|---|---|---|---|---|---|---|---|
| English (reference) | 1500 | 1020 | 68.0% (65.6 to 70.3) |  |  | 62.5% / 70.1% | 480 / 800 | 60.0% (56.6 to 63.3) |  |  |
| Spanish | 560 | 290 | 51.8% (47.6 to 55.9) | -16.2 | 0.762 | 23.3% / 19.9% | 112 / 210 | 53.3% (46.6 to 60.0) | -6.7 |  |
| Vietnamese | suppressed | suppressed | suppressed |  |  |  | suppressed | suppressed |  | complementary |
| Other | suppressed | suppressed | suppressed |  |  |  | suppressed | suppressed |  | primary |
| Not recorded | 174 | 96 | 55.2% (47.8 to 62.4) |  |  | 7.2% / 6.6% | 40 / 70 | 57.1% (45.5 to 68.1) |  |  |

## age band
Eligible 2400, reached 1455; not recorded: 0 of eligible (0.0%). Reference: 45-64.

| Subgroup | Eligible | Reached | Reach rate (95% CI) | Diff vs ref (pp) | Ratio | Share of eligible / of reached | Outcome met / measured | Outcome rate (95% CI) | Outcome diff (pp) | Suppression |
|---|---|---|---|---|---|---|---|---|---|---|
| 18-44 | 520 | 360 | 69.2% (65.1 to 73.0) | +5.6 | 1.088 | 21.7% / 24.7% | 160 / 280 | 57.1% (51.3 to 62.8) | -1.8 |  |
| 45-64 (reference) | 1100 | 700 | 63.6% (60.8 to 66.4) |  |  | 45.8% / 48.1% | 330 / 560 | 58.9% (54.8 to 62.9) |  |  |
| 65-74 | 520 | 280 | 53.8% (49.5 to 58.1) | -9.8 | 0.846 | 21.7% / 19.2% | 110 / 200 | 55.0% (48.1 to 61.7) | -3.9 |  |
| 75 and over | 260 | 115 | 44.2% (38.3 to 50.3) | -19.4 | 0.695 | 10.8% / 7.9% | 49 / 76 | 64.5% (53.3 to 74.3) | +5.5 |  |

## SVI band (US database)
Eligible 2400, reached 1455; not recorded: 50 of eligible (2.1%). Reference: 0 to 0.25.

| Subgroup | Eligible | Reached | Reach rate (95% CI) | Diff vs ref (pp) | Ratio | Share of eligible / of reached | Outcome met / measured | Outcome rate (95% CI) | Outcome diff (pp) | Suppression |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 to 0.25 (reference) | 640 | 450 | 70.3% (66.7 to 73.7) |  |  | 26.7% / 30.9% | 220 / 350 | 62.9% (57.7 to 67.8) |  |  |
| 0.25 to 0.50 | 610 | 390 | 63.9% (60.0 to 67.6) | -6.4 | 0.909 | 25.4% / 26.8% | 180 / 300 | 60.0% (54.4 to 65.4) | -2.9 |  |
| 0.50 to 0.75 | 580 | 330 | 56.9% (52.8 to 60.9) | -13.4 | 0.809 | 24.2% / 22.7% | 140 / 250 | 56.0% (49.8 to 62.0) | -6.9 |  |
| 0.75 to 1 | 520 | 260 | 50.0% (45.7 to 54.3) | -20.3 | 0.711 | 21.7% / 17.9% | suppressed | suppressed |  | complementary (outcome only) |
| Not recorded | 50 | 25 | 50.0% (36.6 to 63.4) |  |  | 2.1% / 1.7% | suppressed | suppressed |  | primary (outcome only) |

Notes:
- preferred language: 'Vietnamese' suppressed as a complement so that 'Other' cannot be derived from the total.
- SVI band (US database): outcome for '0.75 to 1' suppressed as a complement.

## Output (short mode, A2 then B1)

**Answer.** Against your rule (reach at least 0.85 of the reference), five subgroups miss: Spanish (ratio 0.762; 51.8 percent, interval 47.6 to 55.9, against English 68.0), age 65 to 74 (0.846, just under your line; its interval, 49.5 to 58.1, spans the 54.1 percent your rule requires, so whether to act is your call) and 75 and over (0.695; 44.2 percent against 63.6), and SVI bands 0.50 to 0.75 (0.809) and 0.75 to 1 (0.711). Vietnamese and "Other" languages are not measurable under your small-cell rule. Language is not recorded for 7.2 percent of eligible.

**Hypotheses to test (yours to decide).**
- Spanish, change: onboarding in English only reaches enrollment but not first transmission; confirm from where in the funnel Spanish speakers drop (dropout versus nonusage, PE-102).
- 75 and over, change: device setup barrier; note the outcome among those reached is 64.5 percent against 58.9 for the reference, so the gap is reach, not the outcome among those reached. Confirm from setup-step counts.
- SVI bands, measurement or change: check whether the eligibility list includes people the program could not contact; confirm from the eligibility rule.

**Follow-up.** Language: Ana Ruiz's enrollment team (yours). Age: owner not named; who owns it? SVI: owner not named. Next period: not set; which period will you score next? The questions stay open until your rule is met and you close them.

**Published context.** Katz et al. 2024 (doi:10.1001/jamanetworkopen.2023.56070), a systematic review and meta-analysis of 28 studies, reports a systolic difference of -4.24 mm Hg at 6 months in disparity populations (abstract, Results; Verify tier gold). It is about blood pressure in other programs, not about reach in yours, and is not a target. Verify returned "supported" for this claim and also for its negation from the same passage, so the passage was read by hand to confirm the direction (register item N3). The library labeled this record `design: "other"`.

**Stops.** No public statement that the program reached these groups or closed a gap; nothing to a payer or regulator as evidence of reach without the accountable owner.

**Record.** Equity review draft on illustrative counts. Uncleared.

Full version available on request.

(Short mode word count, excluding the calls list and the script output: about 400.)
