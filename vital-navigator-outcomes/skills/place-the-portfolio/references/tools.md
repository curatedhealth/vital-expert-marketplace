# Tools: place-the-portfolio

## Offline (required for scoring / checks)
| Tool | Path | Use for | Never for |
|---|---|---|---|
| `placement_check.py` | `scripts/placement_check.py` | Validate/compute team-entered JSON | Inventing inputs; network |

## Live connectors (optional)
See plugin [`connectors.md`](../../../connectors.md). Cite when used; label **not tool-checked** when skipped on claim-bearing outputs.

### Prefer-live: portfolio placement
When a Decide `brief_id` is open, call Ontology Navigator `portfolio_place` with team-entered candidates.
On connector failure or no brief: run `scripts/placement_check.py` and say once that the connector could not place.


## Invocation rule
Offline first. Exit 0 = pass; 1 = hard error. Soft issues → flags. Written 7 November 2026 (W2 uplift).

## C3 connector boundaries (7 November 2026)

| Tool | Schema | Never |
|---|---|---|
| `portfolio_place` | Required `brief_id`, `candidates[]` with declared fields (`outcome_id`, `governance_burden`, `id`/`option_id`, `name`/`label`/`title`) — **record write** under `4_options` | Undocumented `x`, `y`, `bubble_size`, thresholds; invented coordinates |
| `placement_check.py` | Offline validation of team-entered placement JSON + provenance | Beautify plot by inference |
| `methods_nav_compute` / grid locals | I8 Outcome fit × capacity (owner R2/R4), not consultancy GE axes | Quadrant → Proceed |

Catalog: `references/lane-a-sources-c3-2026-11-07.md` (LA-C3-008, 009, 014).
