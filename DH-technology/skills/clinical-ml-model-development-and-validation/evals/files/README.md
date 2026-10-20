# Eval files

ILLUSTRATIVE files written for these evals by the build script (fixed seed). Not real patients, sites or models. The same files are in `examples/sample-data/`.

- `dataset_manifest_illustrative.csv`: record_id, patient_id, site, date, split, sex, age_band (2,003 records)
- `test_predictions_illustrative.csv`: id, site, sex, age_band, y, p (603 locked test rows)
- `acceptance_criteria_illustrative.json`: the person's operating threshold, acceptance criteria and fairness criterion, written 1 October 2025
- `decision_rules_illustrative.csv`: a three-decision-point rule table for a sleep program
