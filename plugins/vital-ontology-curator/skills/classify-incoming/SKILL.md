---
name: classify-incoming
description: >
  Classify web / RAG / attachment sightings into Curator lead cards (URL, quote, location,
  proposed subject/VP, measure_kind, public flag). Refuse private or client content for the shared queue.
  Does not approve evidence.
license: Proprietary. VITAL Ontology Curator pack license.
compatibility: Offline classification OK; capture requires curator:capture / write path.
metadata:
  level: CF04
  register_code: "CF-01.06.01.curator.classify"
  verb: classify
  capability: "[CHECK] Ontology enrichment — intake classify"
  mission: "Curator intake classify"
  agent: ontology-curator-agent
  atoms: [classify-text-labels]
  tools: [curator_capture_lead, curator_identify_grain]
  version: "0.2.0"
  release_state: Pilot
  pack: "vital-ontology-curator"
  depth: curator-steward
---
# Classify incoming (Curator)

## Competent output
- Lead card: URL/DOI, exact quote, location, proposed subject_family/code, measure_kind, value_kind, public_flag.
- Private / client documents refused for shared queue (EC-2 / KA-CUR-PRIV-01).
- Unbound subject stays `UNBOUND_WEB` (or similar) until a steward binds — never force-bind.
- Use worksheets in `templates/` (lead-card, quality-check).

## Steps
| # | Step | Autonomy |
|---|---|---|
| 1 | Screen public vs private URL / attachment | agent alone |
| 2 | Extract quote + location only if present (never invent) | agent alone |
| 3 | `curator_identify_grain` when subject unclear | agent alone |
| 4 | Suggest family/VP when clear; else leave unbound | agent alone |
| 5 | File via curator_capture_lead when authorized | agent alone |
| 6 | Owner reviews queue later | human only |

## Failure modes
| Failure | What you do |
| --- | --- |
| Private / client doc | Refuse shared queue; hold client-run if authorized |
| No quote in source | Do not invent; mark structure/gap lead |
| Bound without VP | Leave unbound or obtain VP before propose (KA-CUR-VP-01) |
| APQC signal without scope | Capture ok; flag scope incomplete for process/decide |

## Hard rules
- No auto-approve. No Verify on Curator quote-check path.
- Strip client/user/run identity before shared-queue leads.
