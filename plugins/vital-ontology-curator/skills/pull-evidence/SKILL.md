---
name: pull-evidence
description: >
  Pull approved (and optionally under_review) Curator tips for a subject via
  curator_evidence_for_driver / curator_evidence_get. Empty store = [GAP], never invent.
license: Proprietary. VITAL Ontology Curator pack license.
compatibility: curator:read.
metadata:
  level: CF04
  register_code: "CF-01.06.01.curator.pull"
  verb: pull
  capability: "[CHECK] Ontology enrichment — evidence read"
  mission: "Subject-scoped tip pull"
  agent: ontology-curator-agent
  tools: [curator_evidence_for_driver, curator_evidence_get, curator_enrichment_metrics]
  version: "0.2.0"
  release_state: Pilot
  pack: "vital-ontology-curator"
  depth: curator-steward
---
# Pull evidence

## Competent output
- For non-VD subjects: pass `subject_family` + `subject_code` (legacy `vd_code` alone misses PH/JT/CF tips).
- Cite `{record_id, version, grade}` only. Pending ≠ measured.
- Evidence pull report template filled when packing a brief.

## Steps
| # | Step | Autonomy |
|---|---|---|
| 1 | Resolve subject_family + subject_code (or vd_code for VD lane) | agent alone |
| 2 | `curator_evidence_for_driver` | agent alone |
| 3 | Optional `curator_evidence_get` for history | agent alone |
| 4 | If count=0 → report **[GAP]** | agent alone |
| 5 | Never invent figures | agent alone |

## Failure modes
| Failure | What you do |
| --- | --- |
| Only `vd_code` for a PH tip | Retry with subject_family=ph + subject_code |
| Empty result | [GAP] — do not backfill from memory |
| Under_review returned in wrong band | Keep labeled pending, not M |

## Hard rules
- Navigator/Curator readers only — no decide/capture from this skill.
