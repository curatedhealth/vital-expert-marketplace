---
name: collect-apqc-benchmark
description: >
  Lane A — collect APQC/PH process benchmarks with a complete material scope card into Curator tips
  (process_performance / process_maturity). Incomplete scope stays on the named queue; never fast-track.
license: Proprietary. VITAL Ontology Curator pack license.
compatibility: Requires curator:write for propose; open sources only for Shared Public.
metadata:
  level: CF04
  register_code: "CF-01.06.01.curator.apqc"
  verb: collect
  capability: "[CHECK] Ontology enrichment — APQC/PH lane"
  mission: "Process benchmark tips with scope card"
  agent: ontology-curator-agent
  tools: [curator_identify_grain, curator_capture_lead, curator_propose_change, curator_review_queue]
  version: "0.2.0"
  release_state: Pilot
  pack: "vital-ontology-curator"
  depth: curator-lane-a
---
# Collect APQC benchmark (Lane A)

## Competent output
- Tip grain: `subject_family=ph` + PH `subject_code` × process VP × `value_kind` × `process_performance|process_maturity` × provenance.
- `body.apqc` material floor (code-enforced for fast-track): **formula**, **unit**, **normalization_basis**.
- Recommended: `pcf_element_id`, `peer_group`, `period_label`, `measurement_point`, inclusions/exclusions.
- Open / licence-allowed source only on Shared Public. Catalogue PH fields never overwritten.

## Steps
| # | Step | Autonomy |
|---|---|---|
| 1 | Confirm PH subject + VP via `curator_identify_grain` / watch list | agent alone |
| 2 | Fill worksheet `templates/apqc-measurement-worksheet.md` | agent alone |
| 3 | Capture open source → propose tip with full `body.apqc` | agent alone |
| 4 | If material scope missing → leave under_review for named decide; **do not** call fast-track | agent alone |
| 5 | Named human decides (`curator_decide`) | human only |

## Hard rules
- Missing formula / unit / normalization_basis → `apqc_scope_incomplete` on fast-track eligibility (KA-CUR-APQC-01).
- Never invent peer-group or cycle-time figures.
- Never write tip values into catalogue `current_value` / maturity.
