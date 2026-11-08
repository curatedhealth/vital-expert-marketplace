# Tools: frame-the-decision

## Offline (required for scoring / checks)
| Tool | Path | Use for | Never for |
|---|---|---|---|
| `frame_check.py` | `scripts/frame_check.py` | Purpose/scope/perspective; authority + group rule; Driver≠Decide (LA-SDG-FRAME, LA-BAIN-RAPID, LA-DACI) | Assigning Decide; inventing owners |
| `sizing_check.py` | `scripts/sizing_check.py` | Validate/compute team-entered sizing scores | Inventing inputs; network |

## Live connectors (optional)
See plugin [`connectors.md`](../../../connectors.md). Cite when used; label **not tool-checked** when skipped on claim-bearing outputs.



## Invocation rule
Offline first. Exit 0 = pass; 1 = hard error. Soft issues → flags. Written 7 November 2026 (W2 uplift).
