---
name: collect-odi-preference
description: >
  Lane C — collect JT ODI importance/satisfaction/opportunity tips with body.odi card.
  Opportunity must equal I + max(I − S, 0). Mismatch refuses fast-track.
license: Proprietary. VITAL Ontology Curator pack license.
compatibility: Requires curator:write; open preference sources only for Shared Public.
metadata:
  level: CF04
  register_code: "CF-01.06.01.curator.odi"
  verb: collect
  capability: "[CHECK] Ontology enrichment — ODI/JT lane"
  mission: "Preference / ODI tips with Ulwick opportunity"
  agent: ontology-curator-agent
  tools: [curator_identify_grain, curator_propose_change, curator_review_queue]
  version: "0.2.0"
  release_state: Pilot
  pack: "vital-ontology-curator"
  depth: curator-lane-c
---
# Collect ODI preference (Lane C)

## Competent output
- Tip grain: `subject_family=jt` + JT code × ODI VP × stakeholder value_kind × `odi_*` measure_kind.
- `body.odi`: importance, satisfaction, opportunity, sample_n, segment, instrument.
- Opportunity math (Ulwick / KA-CUR-ODI-01): `I + max(I − S, 0)` — use `scripts/opportunity_score.py`.

## Steps
| # | Step | Autonomy |
|---|---|---|
| 1 | Bind JT subject + ODI VP | agent alone |
| 2 | Record I / S / opportunity + sample metadata | agent alone |
| 3 | Verify opportunity with `opportunity_score.py` before propose | agent alone |
| 4 | Propose tip; named decide for approve | human for decide |

## Hard rules
- Wrong opportunity vs Ulwick → `odi_opportunity_mismatch` (not fast-track eligible).
- Never invent survey N or segment.
- Never overwrite catalogue `odi_*` fields from tips.
