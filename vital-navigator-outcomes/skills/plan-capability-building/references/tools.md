# Tools: plan-capability-building

## Offline (required for scoring / checks)
| Tool | Path | Use for | Never for |
|---|---|---|---|
| `build_plan_check.py` | `scripts/build_plan_check.py` | Validate/compute team-entered JSON | Inventing inputs; network |

## Live connectors (optional)
See plugin [`connectors.md`](../../../connectors.md). Cite when used; label **not tool-checked** when skipped on claim-bearing outputs.



## Invocation rule
Offline first. Exit 0 = pass; 1 = hard error. Soft issues → flags. Written 7 November 2026 (W2 uplift).

## C4 payload flags (7 November 2026)
`build_plan_check.evaluate` refuses: `ai_maturity_percent` / `replace_gaps_with_maturity`, `waive_mlr` / `training_waives_mandatory`, `scale_before_capability`, `attendance_only_acceptance`, plan `owner_provenance=ai` / `invented_vendor`, plan `acceptance=attendance_only`. Register + human owners/dates remain required; no maturity % substitute.
