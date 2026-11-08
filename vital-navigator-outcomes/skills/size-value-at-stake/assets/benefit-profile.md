# Benefit profile (value pathway)

Use one profile per distinct benefit. Informed by UK Teal Book Ch.19 benefits management (LA-TEAL-19). Cashable claims also need a realization action (GOV.UK Service Manual — LA-GOVUK-CASH).

**Warrant line (optional in pack):** Per UK Teal Book Ch.19 benefits management; cash claims require a documented realization mechanism (GOV.UK Service Manual).

| Field | Value | Notes |
|---|---|---|
| outcome_id | OUT-### | From discover-outcomes |
| job_id / job_executor | | Separate from beneficiary (LA-HBR-JOBMAP) |
| beneficiary / perspective | | Function vs enterprise |
| measure | | Operational variable |
| unit / denominator | | Active effort ≠ elapsed time |
| population_scope | | |
| measurement_period | | |
| observed_baseline_ref | | Starting point |
| counterfactual_ref | | BAU trajectory — must differ unless flat_bau_rationale |
| target | | Human-owned |
| timescale | | When benefits could materialize |
| benefit_owner | Named person | |
| assumptions | | List |
| dependencies | | List |
| risks | | List |
| benefit_type | capacity / expenditure / throughput / quality / risk / capability / strategic | |
| benefit_mechanism | How improvement becomes useful | |
| cashable | yes / no | |
| realization_action | Required if cashable | e.g. avoid overtime purchase |
| from_opportunity_score | **must be no** | ODI opportunity ≠ money (LA-STRAT-OPP) |

Offline check: `python3 scripts/value_check.py benefit_profile profile.json`  
Traceability: `python3 scripts/traceability_check.py rows.json`
