---
name: classify-incoming
description: >
  Classify web / RAG / attachment sightings into Curator lead cards (URL, quote, location,
  proposed VD/VP, measure_kind, public flag). Refuse private or client content for the shared queue.
  Does not approve evidence.
license: Proprietary. VITAL Outcome Navigator pack license.
compatibility: Offline classification OK; capture requires curator:capture / write path.
metadata:
  level: CF04
  register_code: "CF-01.06.01.curator.classify"
  verb: classify
  capability: "[CHECK] Outcome Navigation — Curator steward side channel"
  mission: "Curator intake classify"
  agent: outcome-navigator-agent
  atoms: [classify-text-labels]
  tools: [curator_capture_lead]
  version: "0.1.0"
  release_state: Draft
  pack: "vital-navigator-outcomes"
  depth: curator-steward
---
# Classify incoming (Curator)

## What competent output looks like
- Lead card: URL/DOI, exact quote, location, proposed subject, measure_kind, value_kind, public_flag.
- Private / client documents refused for shared queue (EC-2).
- Unbound subject stays `UNBOUND_WEB` (or similar) until a steward binds VD/VP — never force-bind.

## Steps
| # | Step | Autonomy |
|---|---|---|
| 1 | Screen public vs private URL / attachment | agent alone |
| 2 | Extract quote + location only if present (never invent) | agent alone |
| 3 | Suggest VD/VP when clear; else leave unbound | agent alone |
| 4 | File via curator_capture_lead when authorized | agent alone |
| 5 | Owner reviews queue later | human only |

## Hard rules
- No auto-approve. No Verify on Curator quote-check path.
- Strip client/user/run identity before shared-queue leads.
