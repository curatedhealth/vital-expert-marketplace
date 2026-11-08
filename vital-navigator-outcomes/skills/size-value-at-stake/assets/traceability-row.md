# Traceability row (working matrix)

One row = one outcome–measure–option–benefit pathway (population × period). Do not sum raw rows for the board — reconcile the benefit register first.

| Field | Value |
|---|---|
| trace_id | TRC-### |
| decision_id | |
| job_id / job_executor | |
| outcome_id / outcome_statement | |
| priority_record_id | |
| measure_id / definition / unit | |
| population_scope / period | |
| baseline_record_id | or [GAP] |
| counterfactual_id / basis | |
| option_id | |
| effect_record_id (target/hypothesis/forecast/measured) | |
| benefit_id / type / mechanism | |
| realization_action | |
| monetary_value / cashable | |
| overlap_group_id / partition_note | |
| claim_state | baseline \| target \| forecast \| actual |
| evidence_status / verification_posture | |
| exhibit_calc_version / locked_calc_version | must match |
| human_disposition | Proceed / Investigate first / Handle it internally — human only |

Validators: TRC-V01…V10 via `scripts/traceability_check.py` (Lane A informed: LA-TEAL-19, LA-GOVUK-CASH, LA-BRM-EVAL).
