---
name: file-and-process
description: >
  File Curator leads and run curator_process_lead (fetch → extract → figures → classify → grade →
  quote_check → propose). Stops at proposal-in-queue. Never calls curator_decide.
license: Proprietary. VITAL Outcome Navigator pack license.
compatibility: Requires curator:write. Live checks stop at queue.
metadata:
  level: CF04
  register_code: "CF-01.06.01.curator.process"
  verb: process
  capability: "[CHECK] Outcome Navigation — Curator steward side channel"
  mission: "Curator process to queue"
  agent: outcome-navigator-agent
  tools: [curator_capture_lead, curator_process_lead, curator_review_queue]
  version: "0.1.0"
  release_state: Draft
  pack: "vital-navigator-outcomes"
  depth: curator-steward
---
# File and process (Curator)

## What competent output looks like
- Leads accepted with lead_id; process outcome `proposed` or `gap_marked`.
- Review queue shows the proposal; no approved tip created by this skill.

## Steps
| # | Step | Tool |
|---|---|---|
| 1 | Capture or select lead_id | curator_capture_lead |
| 2 | Process through tools 3–9 | curator_process_lead |
| 3 | Confirm queue item | curator_review_queue |
| 4 | Hand to steward-decide (human) | none |

## Hard rules
- Process path **never** calls `curator_decide` (C11).
- Open licence only until D9.
