# Intake

Ask for all missing items in one message. For each item, what happens if it is missing is stated.

| # | Input | If missing |
|---|---|---|
| 1 | The signed-off evidence register (register.json) from review-clinical-data-quality, with reviewer name and date | stop and route to review-clinical-data-quality (REQUIRES) |
| 2 | Buyer mode (bd or investor) and unit (asset, or company with the list of assets; each asset is run separately and rolled up) | ask; do not start |
| 3 | Markets in scope: US, EU, or both | ask; another market is a [GAP] |
| 4 | Current development phase and the next planned transition | ask; do not assume a phase |
| 5 | Indication class (one of the benchmark strata), modality, and whether patients are selected by a biomarker (patient preselection; a program that evaluates a new biomarker is not the benchmark's biomarker stratum: Wong 2019) | ask; a stratum the benchmark does not report is a [GAP], never interpolated |
| 6 | Investor mode: the capital plan to the next value inflection, if the team has one. BD mode: the deal structure under discussion | record "not yet set"; the implications then carry a gap |
| 7 | Who will own the final number (name and role) | record "not yet set"; the estimate stays UNSIGNED |
| 8 | The mechanism register from assess-scientific-validity-and-moa, if it exists | record "not yet set"; class and evidence-chain flags are then absent from the adjustment screen and the estimate says so |

Explicit don'ts: never assume a stratum, phase or market; never combine strata; never choose the final number; never state an EU approval probability (stated [GAP]).
Company unit: run one estimate per pipeline asset; the roll-up lists each asset's range side by side and never multiplies unrelated assets into one probability.
