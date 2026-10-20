# Sample data (ILLUSTRATIVE)

Every file in this folder is illustrative, generated for the build and the evals. None is a real organization's data, rules or repair log, no row describes a real person, and the people named are invented. Use only to test `scripts/dq_check.py`.

- `encounters_v3_illustrative.csv` (80 rows) and `encounters_v4_illustrative.csv` (90 rows): heart failure encounters with planted faults (a sex code outside the allowed set, an orphan patient id, a BMI that does not recompute, a duplicated encounter id, an implausible age, a discharge before admission, NT-proBNP results dated after the index time; v4 adds more leak rows and new sex codes).
- `patients_illustrative.csv` the reference file for the relational check.
- `dq_rules_illustrative.json` the person's rules, written for v3 on 1 September 2026; DQ7 has no limit.
- `repair_log_illustrative.csv` owners, actions and versions for three checks, one of which passed in the v4 run.
- `results_v4_illustrative.json` the saved output of `run` on v4, input to `review`.
