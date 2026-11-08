# Tools: prioritize-outcomes

## Offline (required for scoring / checks)
| Tool | Path | Use for | Never for |
|---|---|---|---|
| `outcome_priority_check.py` | `scripts/outcome_priority_check.py` | Validate/compute team-entered JSON | Inventing inputs; network |

## Live connectors (optional)
See plugin [`connectors.md`](../../../connectors.md). Cite when used; label **not tool-checked** when skipped on claim-bearing outputs.



## Invocation rule
Offline first. Exit 0 = pass; 1 = hard error. Soft issues → flags. Written 7 November 2026 (W2 uplift).

## Lane A absorb (7 November 2026)
`outcome_priority_check.py` — Compute opportunity I+max(0,I-S); evidence_scope; Strategyn warrant. Catalog: plugin `references/lane-a-sources-c1-c2-2026-11-07.md`.
