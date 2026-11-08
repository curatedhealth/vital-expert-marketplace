# Tools: route-the-entry

## Offline (required for scoring / checks)
| Tool | Path | Use for | Never for |
|---|---|---|---|
| `routing_check.py` | `scripts/routing_check.py` | Validate/compute team-entered JSON | Inventing inputs; network |

## Live connectors (optional)
See plugin [`connectors.md`](../../../connectors.md). Cite when used; label **not tool-checked** when skipped on claim-bearing outputs.



## Invocation rule
Offline first. Exit 0 = pass; 1 = hard error. Soft issues → flags. Written 7 November 2026 (W2 uplift).

## Lane A absorb (7 November 2026)
`routing_check.py` — Family/shape + job≠solution (LA-HBR-JOBMAP). Catalog: plugin `references/lane-a-sources-c1-c2-2026-11-07.md`.
