# Sample data (ILLUSTRATIVE)

Every file in this folder is illustrative, typed or generated for the build and the evals. None is a real hospital's or company's metric catalog, discharge data, breakdown or scoring set, and the people named are invented. Use only to test `scripts/metric_check.py`.

- `metric_cards_illustrative.csv` four metric cards (one duplicate recomputed on a unit dashboard, one denominator in codes, one with no decision).
- `discharges_illustrative.csv` 180 generated discharge rows (seed 7) for `recompute`.
- `missed_calls_by_unit_illustrative.csv` a breakdown for `driver`.
- `use_case_scores_illustrative.json` RICE scores for three analytics use cases; one confidence is given as a fraction on purpose.
