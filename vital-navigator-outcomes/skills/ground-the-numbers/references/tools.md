# Tools: ground-the-numbers

## Offline (required for scoring / checks)
| Tool | Path | Use for | Never for |
|---|---|---|---|
| `grounding_check.py` | `scripts/grounding_check.py` | Validate/compute team-entered JSON | Inventing inputs; network |

## Live connectors (optional)
See plugin [`connectors.md`](../../../connectors.md). Cite when used; label **not tool-checked** when skipped on claim-bearing outputs.



## Invocation rule
Offline first. Exit 0 = pass; 1 = hard error. Soft issues → flags. Written 7 November 2026 (W2 uplift).

## Lane A absorb (7 November 2026)
`grounding_check.py` — Claims + ODI/cash refuses (LA-STRAT-OPP, LA-GOVUK-CASH). Catalog: plugin `references/lane-a-sources-c1-c2-2026-11-07.md`.
