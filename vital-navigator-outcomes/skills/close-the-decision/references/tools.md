# Tools: close-the-decision

## Offline (required for scoring / checks)
| Tool | Path | Use for | Never for |
|---|---|---|---|
| `record_check.py` | `scripts/record_check.py` | Validate/compute team-entered JSON | Inventing inputs; network |

## Live connectors (optional)
See plugin [`connectors.md`](../../../connectors.md). Cite when used; label **not tool-checked** when skipped on claim-bearing outputs.



## Invocation rule
Offline first. Exit 0 = pass; 1 = hard error. Soft issues → flags. Written 7 November 2026 (W2 uplift).

## Lane A absorb (7 November 2026)
`record_check.py` — Record + authority/DQ checks (LA-BAIN-RAPID, LA-SDG-SIX). Catalog: plugin `references/lane-a-sources-c1-c2-2026-11-07.md`.
