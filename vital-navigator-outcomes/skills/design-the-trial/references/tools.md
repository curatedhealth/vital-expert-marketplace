# Tools: design-the-trial

## Offline (required for scoring / checks)
| Tool | Path | Use for | Never for |
|---|---|---|---|
| `trial_check.py` | `scripts/trial_check.py` | Validate/compute team-entered JSON | Inventing inputs; network |

## Live connectors (optional)
See plugin [`connectors.md`](../../../connectors.md). Cite when used; label **not tool-checked** when skipped on claim-bearing outputs.



## Invocation rule
Offline first. Exit 0 = pass; 1 = hard error. Soft issues → flags. Written 7 November 2026 (W2 uplift).

## C4 payload flags (7 November 2026)
`trial_check.evaluate` refuses: `ai_sets_target`, `ich_gcp_protocol` / `write_clinical_protocol`, `premortem_skips_trial` / `premortem_proves_success`, `auto_scale_on_target` / `certify_investment_success`, post-result criteria change without `criteria_revision_ref`, `nonclinical_waives_gxp` / `privacy`, `ai_hypothesis_as_observed`, `measure.target_provenance=ai`. Optional `require_decision_link` adds V-C4-TRL-02 problem when `decision_to_inform` empty.
