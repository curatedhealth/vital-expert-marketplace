# Script runs (illustrative data)

Run on 19 October 2026. Input files in `evals/files/` are invented for testing and labeled illustrative.

```
python3 scripts/trial_ops_metrics.py sites evals/files/dct_participants_illustrative.csv --targets evals/files/site_targets_illustrative.csv --as-of 2026-10-19 --rules evals/files/rules_illustrative.json
```

# Trial execution metrics by site

Input: files/dct_participants_illustrative.csv (one row per participant). As of: 2026-10-19. Targets and rules are the person's; no verdict without a rule.

| Site | Enrolled | Target | % of target | Per month | Retention % | Withdrawn | Lost | Deviations (important) | Dev. per participant | Completeness % | Completeness by arm % |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Berlin | 22 | 24 | 91.7 | 2.9 | 90.9 | 1 | 1 | 11 (0) | 0.5 | 95.0 | A 95.7; B 94.5 |
| Boston | 21 | 24 | 87.5 | 2.95 | 100.0 | 0 | 0 | 11 (0) | 0.52 | 77.0 | A 81.4; B 71.3 |
| Denver | 9 | 16 | 56.2 | 1.63 | 88.9 | 0 | 1 | 8 (3) | 0.89 | 89.2 | A 89.7; B 88.5 |
| Munich | 13 | 20 | 65.0 | 2.09 | 76.9 | 2 | 1 | 8 (1) | 0.62 | 93.5 | A 93.7; B 93.2 |
| All sites | 65 | 84 | 77.4 | [GAP] | 90.8 | 3 | 3 | 38 (4) | 0.58 | 88.2 | A 89.5; B 86.7 |

## Your rules

| Site | Rule (your words) | Value | Result | Owner |
|---|---|---|---|---|
| Berlin | At least 85% of enrolled participants retained at each site | 90.9 | pass | Clinical Operations lead |
| Boston | At least 85% of enrolled participants retained at each site | 100.0 | pass | Clinical Operations lead |
| Denver | At least 85% of enrolled participants retained at each site | 88.9 | pass | Clinical Operations lead |
| Munich | At least 85% of enrolled participants retained at each site | 76.9 | miss | Clinical Operations lead |
| Berlin | Primary endpoint data at least 90% complete per site | 95.0 | pass | Data Management |
| Boston | Primary endpoint data at least 90% complete per site | 77.0 | miss | Data Management |
| Denver | Primary endpoint data at least 90% complete per site | 89.2 | miss | Data Management |
| Munich | Primary endpoint data at least 90% complete per site | 93.5 | pass | Data Management |
| Berlin | No more than 1 important deviation per 10 participants | 0.0 | pass | QA |
| Boston | No more than 1 important deviation per 10 participants | 0.0 | pass | QA |
| Denver | No more than 1 important deviation per 10 participants | 0.33 | miss | QA |
| Munich | No more than 1 important deviation per 10 participants | 0.08 | pass | QA |
| All sites | Arms within 5 points on completeness | 2.8 | pass | owner not named |

```
python3 scripts/trial_ops_metrics.py clocks evals/files/trial_dates_illustrative.json
```

# Registration and results clocks

As of 2026-10-19. Dates are the person's; whether each rule applies is the call of the owner the person names for registration, or owner not named.

| Clock | Date | Position at as-of | Row | Note |
|---|---|---|---|---|
| ICMJE: registration at or before first patient consent | 2024-03-09 | submitted 2024-03-25 (16 days after the date) | CV132 |  |
| US 42 CFR 11.24: registration within 21 calendar days after first enrollment | 2024-03-31 | submitted 2024-03-25 (on or before the date) | CV141 |  |
| US 42 CFR 11.44(a): results no later than 1 year after primary completion date | 2026-09-30 | not recorded as submitted; date passed 19 days before as-of | CV145 |  |
| US 42 CFR 11.64: registration information updated at least every 12 months | 2026-11-02 | not yet due; 14 days from as-of | CV149 |  |
| US 42 CFR 11.64: recruitment status updated within 30 days of a change | 2026-10-01 | not recorded as submitted; date passed 18 days before as-of | CV149 |  |
| EU CTR Art 37: end-of-trial notification in DE within 15 days | 2026-10-16 | not recorded as submitted; date passed 3 days before as-of | CV151 | Applies to trials under Regulation (EU) No 536/2014 (CVB7). |
| WHO joint statement (funder pledge, not law): summary results within 12 months of primary completion | 2026-09-30 | not recorded as submitted; date passed 19 days before as-of | CV140 |  |
| WHO joint statement (indicative): journal publication within 24 months of study completion | 2027-09-30 | not yet due; 346 days from as-of | CV140 | The statement anchors publication to study completion; primary completion used here as given. |
