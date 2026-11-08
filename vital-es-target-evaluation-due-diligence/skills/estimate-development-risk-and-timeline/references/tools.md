# Tools: estimate-development-risk-and-timeline

## Offline (required for scoring / checks)
| Tool | Path | Use for | Never for |
|---|---|---|---|
| `pos_chain.py` | `scripts/pos_chain.py` | Offline validation / computation for this skill | Live network; inventing missing inputs; human-only opinions |
| `timeline_range.py` | `scripts/timeline_range.py` | Offline validation / computation for this skill | Live network; inventing missing inputs; human-only opinions |
| `tornado_inputs.py` | `scripts/tornado_inputs.py` | Offline validation / computation for this skill | Live network; inventing missing inputs; human-only opinions |

## Templates
- `templates/estimate.md`

## Live connectors (optional)
See plugin [`connectors.md`](../../../connectors.md). Cite when used; label **not tool-checked** when skipped on claim-bearing outputs. Never treat connectors as substitutes for pack sources.

## Invocation rule
Offline first. Exit 0 = pass; 1 = hard rule error; soft issues → flags / [CHECK] / [GAP]. Written 8 November 2026 (ON kit-parity uplift).
