---
name: enrich-record
description: >
  Inject approved Curator tips into a decision brief as measured (M) only when {record_id, version, grade}
  exist. Pending / under_review stay labeled pending — never as measured. Leave explicit [GAP]s.
license: Proprietary. VITAL Outcome Navigator pack license.
compatibility: Works offline on tip ids already returned; live pull via pull-evidence.
metadata:
  level: CF04
  register_code: "CF-01.06.01.curator.enrich"
  verb: enrich
  capability: "[CHECK] Outcome Navigation — Curator steward side channel"
  mission: "Brief enrichment from Curator"
  agent: outcome-navigator-agent
  tools: [curator_evidence_for_driver, curator_evidence_get]
  version: "0.1.0"
  release_state: Draft
  pack: "vital-navigator-outcomes"
  depth: curator-steward
---
# Enrich record (Curator → brief)

## What competent output looks like
- Three bands in the brief: **approved** · **under review** · **gap**.
- Only approved tips receive label **M** (measured). Pending never presented as measured.
- Citations use tip ids, not invented secondary quotes.

## Steps
| # | Step | Autonomy |
|---|---|---|
| 1 | Collect tip ids from pull-evidence / prior run | agent alone |
| 2 | Map into brief sections (value at stake, assumptions, …) | agent alone |
| 3 | Mark pending vs approved vs [GAP] | agent alone |
| 4 | Owner accepts brief before seal | human only |

## Hard rules
- `assert_no_pending_as_measured`: pending ≠ M.
- No Lane A quote redistribution in Marketplace chrome.
