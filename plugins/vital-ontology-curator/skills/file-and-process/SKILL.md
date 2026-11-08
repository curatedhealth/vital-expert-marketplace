---
name: file-and-process
description: >
  File public leads via curator_capture_lead, then steward-process into under_review tips
  with grain + VP bind. Never approve. Refuse private/client content for Shared Public.
license: Proprietary. VITAL Ontology Curator pack license.
compatibility: curator:capture for intake; curator:write for process.
metadata:
  level: CF04
  register_code: "CF-01.06.01.curator.file"
  verb: file
  capability: "[CHECK] Ontology enrichment — intake + process"
  mission: "Lead → under_review tip"
  agent: ontology-curator-agent
  tools: [curator_capture_lead, curator_process_lead, curator_identify_grain, curator_review_queue]
  version: "0.2.0"
  release_state: Pilot
  pack: "vital-ontology-curator"
  depth: curator-steward
---
# File and process

## Competent output
- Capture receipt with lead_id + dedupe key; process receipt with under_review record_id/version.
- Bound tips carry subject_family + subject_code + vp_code; unbound stays awaiting bind.
- Filing receipt template filled (`templates/filing-receipt.md`).

## Steps
| # | Step | Autonomy |
|---|---|---|
| 1 | Confirm public / open licence (EC-2) | agent alone |
| 2 | `curator_capture_lead` (batch ≤25) | agent alone |
| 3 | `curator_identify_grain` if subject unclear | agent alone |
| 4 | `curator_process_lead` → under_review | agent alone |
| 5 | Surface on `curator_review_queue` for named decide | human |

## Failure modes
| Failure | What you do |
| --- | --- |
| `non_public_source_refused` | Stop; do not file to Shared Public |
| `missing_vp_code` on process | Leave unbound or bind VP first |
| Duplicate dedupe | Report existing lead_id; do not invent a second tip |
| Empty quote | Refuse process — no fabricated source_quote |

## Hard rules
- No `curator_decide` from this skill.
- No catalogue writes. No Vital Verify on quote-check path.
