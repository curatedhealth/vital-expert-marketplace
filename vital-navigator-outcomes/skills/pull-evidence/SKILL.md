---
name: pull-evidence
description: >
  Read approved Curator evidence for a value driver or measure via curator_evidence_for_driver /
  curator_evidence_get. Cite {record_id, version, grade} only. Empty store → [GAP], never invent tips.
  Not for Verify claim checks (handoff-verify) and not for writing into Curator.
license: Proprietary. VITAL Outcome Navigator pack license.
compatibility: Requires vcur_ Ontology Curator connector for live tips; offline → label not tool-checked / [GAP].
metadata:
  level: CF04
  register_code: "CF-01.06.01.curator.pull"
  verb: pull
  capability: "[CHECK] Outcome Navigation — Curator steward side channel"
  mission: "Curator evidence read"
  agent: outcome-navigator-agent
  atoms: []
  requires: []
  feeds: [size-value-at-stake, ground-the-numbers]
  tools: [curator_evidence_for_driver, curator_evidence_get]
  version: "0.1.0"
  release_state: Draft
  pack: "vital-navigator-outcomes"
  depth: curator-steward
---
# Pull evidence (Curator)

## What competent output looks like
- Figures only from approved / stale / gap_marked Curator tips.
- Every figure carries `{record_id, version, grade}`.
- Empty result is `[GAP]` — never a fabricated tip or secondary paraphrase presented as measured.

## Steps
| # | Step | Tool | Autonomy |
|---|---|---|---|
| 1 | Confirm workspace_id + subject (vd_code) | none | agent alone |
| 2 | Call curator_evidence_for_driver | Curator read | agent alone |
| 3 | Optionally curator_evidence_get for one record | Curator read | agent alone |
| 4 | Present range / grades; mark [GAP] where missing | none | agent alone |

## Hard rules
- Navigator tools stay readers (tools 16–17). Do not call decide / capture / process from this skill.
- Do not redistribute Lane A verbatim quotes into buyer chrome; paraphrase or cite tip ids only.
