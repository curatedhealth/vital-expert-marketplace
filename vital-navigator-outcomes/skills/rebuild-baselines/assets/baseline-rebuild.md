# Baseline rebuild sheet

Never backcast. Provenance=gap ⇒ leave value blank.

| Metric | Unit | Period | Provenance | Class | Value/mid | Low | High | Source id | Source date |
|---|---|---|---|---|---|---|---|---|---|
| | | | extract / time_study / gap | | | | | | |

Provenance rules:
- extract / time_study → value + source_id + source_date required
- gap → no numeric value
- low/mid/high if used must satisfy low ≤ mid ≤ high and low ≠ high

Script: `python3 scripts/baseline_check.py baselines.json --json`
