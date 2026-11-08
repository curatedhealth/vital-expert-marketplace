# Tools: cut-the-slop

## Offline (required for scoring / checks)
| Tool | Path | Use for | Never for |
|---|---|---|---|
| `substance_check.py` | `scripts/substance_check.py` | Validate/compute team-entered JSON | Inventing inputs; network |

## Live connectors (optional)
See plugin [`connectors.md`](../../../connectors.md). Cite when used; label **not tool-checked** when skipped on claim-bearing outputs.



## Invocation rule
Offline first. Exit 0 = pass; 1 = hard error. Soft issues → flags. Written 7 November 2026 (W2 uplift).
