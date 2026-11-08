# Tools: evaluate-market-opportunity-and-competitive-position

## Offline (required for scoring / checks)
| Tool | Path | Use for | Never for |
|---|---|---|---|
| `market_check.py` | `scripts/market_check.py` | Offline validation / computation for this skill | Live network; inventing missing inputs; human-only opinions |
| `validate_register.py` | `scripts/validate_register.py` | Offline validation / computation for this skill | Live network; inventing missing inputs; human-only opinions |

## Templates
- `templates/market-register.md`

## Live connectors (optional)
See plugin [`connectors.md`](../../../connectors.md). Cite when used; label **not tool-checked** when skipped on claim-bearing outputs. Never treat connectors as substitutes for pack sources.

## Invocation rule
Offline first. Exit 0 = pass; 1 = hard rule error; soft issues → flags / [CHECK] / [GAP]. Written 8 November 2026 (ON kit-parity uplift).
