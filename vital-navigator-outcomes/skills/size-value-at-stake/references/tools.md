# Tools: size-value-at-stake

## Offline (required for scoring / checks)
| Tool | Path | Use for | Never for |
|---|---|---|---|
| `value_check.py` | `scripts/value_check.py` | `drivers` / `range` / `benefit_profile` / `layers` | Inventing magnitudes; ODI→money |
| `traceability_check.py` | `scripts/traceability_check.py` | TRC-V01…V10 pathway validators (LA-TEAL-19, LA-GOVUK-CASH) | Summing exclusive options; assistant disposition |

## Live connectors (optional)
See plugin [`connectors.md`](../../../connectors.md). Cite when used; label **not tool-checked** when skipped on claim-bearing outputs.



## Invocation rule
Offline first. Exit 0 = pass; 1 = hard error. Soft issues → flags. Written 7 November 2026 (W2 uplift).
