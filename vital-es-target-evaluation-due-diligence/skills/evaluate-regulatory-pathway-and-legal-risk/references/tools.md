# Tools: evaluate-regulatory-pathway-and-legal-risk

## Offline (required for scoring / checks)
| Tool | Path | Use for | Never for |
|---|---|---|---|
| `validate_pathway.py` | `scripts/validate_pathway.py` | Offline validation / computation for this skill | Live network; inventing missing inputs; human-only opinions |

## Templates
- `templates/pathway-and-risk.md`

## Live connectors (optional)
See plugin [`connectors.md`](../../../connectors.md). Cite when used; label **not tool-checked** when skipped on claim-bearing outputs. Never treat connectors as substitutes for pack sources.

## Invocation rule
Offline first. Exit 0 = pass; 1 = hard rule error; soft issues → flags / [CHECK] / [GAP]. Written 8 November 2026 (ON kit-parity uplift).
