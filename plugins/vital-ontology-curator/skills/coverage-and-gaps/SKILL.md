---
name: coverage-and-gaps
description: >
  Report enrichment coverage via curator_enrichment_metrics using the declared watch
  scope pack (required_vp_code rows). File planned gap leads; never invent figures.
license: Proprietary. VITAL Ontology Curator pack license.
compatibility: curator:read for metrics; curator:write for planned gap filing.
metadata:
  level: CF04
  register_code: "CF-01.06.01.curator.coverage"
  verb: measure
  capability: "[CHECK] Ontology enrichment — coverage"
  mission: "Declared scope-pack coverage and gap leads"
  agent: ontology-curator-agent
  tools: [curator_enrichment_metrics, curator_watch_list, curator_planned_run]
  version: "0.2.1"
  release_state: Pilot
  pack: "vital-ontology-curator"
  depth: curator-coverage
---
# Coverage and gaps

## Competent output
- Declared scope pack upserted (`templates/enrichment-scope-pack.example.json`).
- Metrics expose `coverage_ratio`, `declared_scope_pack_total`, `coverage_denominator=declared_watch_scope_pack`.
- Gaps filed as planned leads — never invented tip values.

## Steps
| # | Step | Autonomy |
|---|---|---|
| 1 | Upsert scope pack via `curator_watch_list` (`required_vp_code` or note `scope_pack=1`) | agent alone |
| 2 | Call `curator_enrichment_metrics` | agent alone |
| 3 | Report `coverage_ratio` + family breakdown | agent alone |
| 4 | `curator_planned_run` dry_run then file gaps | agent alone |
| 5 | Never invent figures; never claim live catalogue % | agent alone |

## Hard rules
- Denominator = **declared watch scope pack**, not ontology catalogue row count.
- Bulk APQC mass import and catalogue projection remain owner HITL.
