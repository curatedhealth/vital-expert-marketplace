# Link-by-link check: StepClear (illustrative app: CRA lessons plus rewards for negative screens, outpatient stimulant and opioid use) (illustrative: invented product, plan and thresholds, written for testing the skill)

Command: `python3 scripts/link_check.py --plan evals/files/check_plan_illustrative.json --data evals/files/cohort_illustrative.csv --version 2.3` (run 20 October 2026 on the illustrative files; the illustrative request gives no data cut, so none is passed and the script says so).

- Version: 2.3; rows used 16; rows of other versions excluded 2
- Data cut: not given; ask the person (never supply today’s date); plan set 2026-06-01, data read before the plan: False
- 4 of 4 measurable links met against the person's thresholds. Not a quality score.

| Link | Type | Measure | n | Missing | Value | Result | Basis |
|---|---|---|---|---|---|---|---|
| L1 | delivered | Reward granted only after a negative screen (software fidelity log) | 16 | 0 | 1.0 | met | >= 0.99 |
| L2 | used | Core lessons completed per week, weeks 1 to 12 | 16 | 0 | 3.362 | met | >= 3 |
| L3 | changed | Coping score change, baseline to week 12 | 15 | 1 | 0.393 | met | >= 0.3 |
| L5 | changed | Craving rating at week 12 (added after the data were seen) | 16 | 0 | 2.875 | not scored | measure not named in advance (TM57, DOI 10.1037/hea0000161) |
| L4 | outcome | Abstinent in weeks 9 to 12 (missing screens not imputed) | 15 | 1 | 0.6 | met | >= 0.4 |

Level note: L5 reads one column (craving_w12); it is a level at that time point, not a change. A 'drop' or 'rise' cannot be computed from this file without a baseline column.

## Subgroups the person named (context; same thresholds)

| Subgroup | Link | n | Missing | Value | Result |
|---|---|---|---|---|---|
| primary opioid use | L1 | 6 | 0 | 1.0 | met |
| primary opioid use | L2 | 6 | 0 | 3.283 | met |
| primary opioid use | L3 | 6 | 0 | 0.367 | met |
| primary opioid use | L4 | 5 | 1 | 0.2 | missed |
| primary stimulant use | L1 | 10 | 0 | 1.0 | met |
| primary stimulant use | L2 | 10 | 0 | 3.41 | met |
| primary stimulant use | L3 | 9 | 1 | 0.411 | met |
| primary stimulant use | L4 | 10 | 0 | 0.8 | met |

## Not measurable ([GAP], not scored)
- L0 (changed): Rewards strengthen motivation to stay abstinent; no measure in the plan

## Second run: version 2.2 (shows the reading note)

`python3 scripts/link_check.py --plan evals/files/check_plan_illustrative.json --data evals/files/cohort_illustrative.csv --version 2.2`

- Version: 2.2; rows used 2; rows of other versions excluded 16
- Data cut: not given; ask the person (never supply today’s date); plan set 2026-06-01, data read before the plan: False
- 0 of 4 measurable links met against the person's thresholds. Not a quality score.

| Link | Type | Measure | n | Missing | Value | Result | Basis |
|---|---|---|---|---|---|---|---|
| L1 | delivered | Reward granted only after a negative screen (software fidelity log) | 2 | 0 | 0.5 | missed | >= 0.99 |
| L2 | used | Core lessons completed per week, weeks 1 to 12 | 2 | 0 | 1.75 | missed | >= 3 |
| L3 | changed | Coping score change, baseline to week 12 | 2 | 0 | 0.05 | missed | >= 0.3 |
| L5 | changed | Craving rating at week 12 (added after the data were seen) | 2 | 0 | 5.5 | not scored | measure not named in advance (TM57, DOI 10.1037/hea0000161) |
| L4 | outcome | Abstinent in weeks 9 to 12 (missing screens not imputed) | 2 | 0 | 0.0 | missed | >= 0.4 |

Level note: L5 reads one column (craving_w12); it is a level at that time point, not a change. A 'drop' or 'rise' cannot be computed from this file without a baseline column.

Reading note: L1 (delivery or use) missed. Later links cannot separate an ineffective mechanism from failed delivery (CS32, DOI 10.1007/s10488-010-0319-7; TM92, DOI 10.1136/bmj.h1258).

## Subgroups the person named (context; same thresholds)

| Subgroup | Link | n | Missing | Value | Result |
|---|---|---|---|---|---|
| primary opioid use | L1 | 1 | 0 | 0.0 | missed |
| primary opioid use | L2 | 1 | 0 | 2.0 | missed |
| primary opioid use | L3 | 1 | 0 | 0.0 | missed |
| primary opioid use | L4 | 1 | 0 | 0.0 | missed |
| primary stimulant use | L1 | 1 | 0 | 1.0 | met |
| primary stimulant use | L2 | 1 | 0 | 1.5 | missed |
| primary stimulant use | L3 | 1 | 0 | 0.1 | missed |
| primary stimulant use | L4 | 1 | 0 | 0.0 | missed |

## Not measurable ([GAP], not scored)
- L0 (changed): Rewards strengthen motivation to stay abstinent; no measure in the plan
