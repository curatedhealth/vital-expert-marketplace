---
name: enrich-record
description: >
  Inject approved Curator tips into a decision brief as measured (M) only when
  {record_id, version, grade} exist. Pending / under_review stay labeled pending.
  Attach APQC/ODI cards when present. Leave explicit [GAP]s.
license: Proprietary. VITAL Ontology Curator pack license.
compatibility: Works offline on tip ids already returned; live pull via pull-evidence.
metadata:
  level: CF04
  register_code: "CF-01.06.01.curator.enrich"
  verb: enrich
  capability: "[CHECK] Ontology enrichment — brief injection"
  mission: "Brief enrichment from Curator tips"
  agent: ontology-curator-agent
  tools: [curator_evidence_for_driver, curator_evidence_get]
  version: "0.2.0"
  release_state: Pilot
  pack: "vital-ontology-curator"
  depth: curator-steward
---
# Enrich record (Curator → brief)

## Competent output
- Three bands: **approved** · **under review** · **gap**.
- Only approved tips receive label **M** (measured). Pending never presented as measured.
- When `body.apqc` / `body.odi` exist, surface material fields (formula/unit/normalization; I/S/opp).
- Citations use tip ids, not invented secondary quotes.

## Steps
| # | Step | Autonomy |
|---|---|---|
| 1 | Collect tip ids from pull-evidence / prior run | agent alone |
| 2 | Map into brief sections (value at stake, assumptions, process, preference) | agent alone |
| 3 | Mark pending vs approved vs [GAP]; attach scope cards | agent alone |
| 4 | Owner accepts brief before seal | human only |

## Failure modes
| Failure | What you do |
| --- | --- |
| Pending tip labeled M | Demote to pending band |
| Missing APQC material on process tip | Note incomplete scope; do not invent |
| ODI opp ≠ Ulwick | Flag mismatch; do not “fix” the number silently |

## Hard rules
- `assert_no_pending_as_measured`: pending ≠ M.
- No Lane A quote redistribution in Marketplace chrome.
- No catalogue overwrite from this skill.
