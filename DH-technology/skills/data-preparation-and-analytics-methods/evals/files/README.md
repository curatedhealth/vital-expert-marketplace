# Sample data (ILLUSTRATIVE)

Every file in this folder is illustrative, typed or generated for the build and the evals. None is a real organization's cohort, feature dictionary, split, predictions or forecast, and no row describes a real person. Use only to test `scripts/prep_check.py`.

- `cohort_steps_illustrative.csv` cohort steps with a count that rises after linkage (C1) and a step without a rule (C2).
- `feature_dictionary_illustrative.csv` nine features, three with leakage flags, two with 45 CFR 92.210 inputs, one without source field or window.
- `split_illustrative.csv` 42 rows; two patients in both train and test; sites shared between development and test.
- `predictions_illustrative.csv` 300 encounters (100 train, 200 test) with a score and two groups whose outcome rates differ.
- `forecast_illustrative.csv` 18 months (12 history, 6 holdout) with a forecast and interval.
