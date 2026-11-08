---
name: bind-vp-and-subject
description: >
  Steward bind from UNBOUND lead/tip to subject_family+code and required vp_code.
  Bound tips without VP are refused (hard gate).
license: Proprietary. VITAL Ontology Curator pack license.
metadata:
  level: CF04
  register_code: "CF-01.06.01.curator.bind"
  verb: bind
  agent: ontology-curator-agent
  tools: [curator_identify_grain, curator_process_lead, curator_propose_change, curator_decide]
  version: "0.2.0"
  release_state: Pilot
  pack: "vital-ontology-curator"
---
# Bind VP and subject

## Competent output
- Unbound lead → bound tip with allowlisted `subject_family`, canonical `subject_code`, and non-empty `vp_code`.
- MEASURES link preserved (VP measures the subject family).
- Named decide for approve; catalogue untouched.

## Steps
| # | Step | Autonomy |
|---|---|---|
| 1 | Open unbound lead (`subject_family=unbound` or `UNBOUND_*`) | agent alone |
| 2 | `curator_identify_grain` → candidates | agent alone |
| 3 | Steward confirms family + code + VP | human |
| 4 | Process / propose with bound fields | agent alone |
| 5 | Named `curator_decide` | human only |

## Hard rules
- Bound without `vp_code` → `missing_vp_code` (KA-CUR-VP-01).
- Do not invent ontology catalogue rows to satisfy a bind.
