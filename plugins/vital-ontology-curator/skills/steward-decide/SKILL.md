---
name: steward-decide
description: >
  Named-human curator_decide on open proposals (approve / reject / edit / retire / stale).
  person_name must be a real human (R1/C11). Fast-track only under owner-stamped rule.
license: Proprietary. VITAL Ontology Curator pack license.
compatibility: curator:write; proposal_id required.
metadata:
  level: CF04
  register_code: "CF-01.06.01.curator.decide"
  verb: decide
  capability: "[CHECK] Ontology enrichment — named decide"
  mission: "HITL tip lifecycle"
  agent: ontology-curator-agent
  tools: [curator_review_queue, curator_decide, curator_fast_track_evaluate, curator_fast_track_sample]
  version: "0.2.0"
  release_state: Pilot
  pack: "vital-ontology-curator"
  depth: curator-steward
---
# Steward decide

## Competent output
- Open proposal → decided with `decided_by` = named human; tip tip-state advanced.
- Steward ruling template (`templates/steward-ruling.md`) filled when rejecting/editing.
- APQC incomplete / ODI mismatch never fast-tracked (code-enforced); named approve still allowed with reason.

## Steps
| # | Step | Autonomy |
|---|---|---|
| 1 | `curator_review_queue` — pick proposal / tip | agent alone |
| 2 | Check grain + scope cards (APQC/ODI) | agent alone |
| 3 | If fast-track eligible + rule active → evaluate (optional) | agent alone |
| 4 | Else `curator_decide` with person_name + reason | human name required |
| 5 | Confirm tip tip-state + proposal status | agent alone |

## Failure modes
| Failure | What you do |
| --- | --- |
| Missing `proposal_id` | Create proposal wrapping under_review tip first |
| `person_name` is a model/tool | Refuse — C11 |
| Fast-track `apqc_scope_incomplete` | Leave on named queue or complete scope then re-eval |
| Sample selected | Owner sample pass/fail via `curator_fast_track_sample` |

## Hard rules
- Named human only. No auto-approve without owner-stamped rule.
- Catalogue projection still withheld — decide tips only.
