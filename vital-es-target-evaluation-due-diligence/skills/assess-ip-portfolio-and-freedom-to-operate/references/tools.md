# Tools: assess-ip-portfolio-and-freedom-to-operate

## Offline (required for scoring / checks)
| Tool | Path | Use for | Never for |
|---|---|---|---|
| `exclusivity_dates.py` | `scripts/exclusivity_dates.py` | Offline validation / computation for this skill | Live network; inventing missing inputs; human-only opinions |
| `validate_register.py` | `scripts/validate_register.py` | Offline validation / computation for this skill | Live network; inventing missing inputs; human-only opinions |

## Templates
- `templates/exclusivity-register.md`

## Live connectors (optional)
See plugin [`connectors.md`](../../../connectors.md). Cite when used; label **not tool-checked** when skipped on claim-bearing outputs. Never treat connectors as substitutes for pack sources.

### Orange Book / Purple Book reading rule (S22)
When a person or fetch reads FDA Orange Book or Purple Book pages: record URL + date read; treat rows as **listings and exclusivity postings** only (VP-C-140..142). Do **not** feed listing presence into any clearance, validity, or FTO field. Form FDA 3542 is a listing-process fact (VP-C-143), not a validity proof.

## Invocation rule
Offline first. Exit 0 = pass; 1 = hard rule error; soft issues → flags / [CHECK] / [GAP]. Written 8 November 2026 (ON kit-parity uplift).
