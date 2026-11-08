---
name: steward-decide
description: >
  Named-human Curator decide on open proposals (approve / reject / edit). v1 allowlist: Hicham only.
  API/build keys must not type a human name (C11); use a user-bound key. Records dissent.
license: Proprietary. VITAL Outcome Navigator pack license.
compatibility: Requires curator:write and a human session. Never use service-key impersonation.
metadata:
  level: CF04
  register_code: "CF-01.06.01.curator.decide"
  verb: decide
  capability: "[CHECK] Outcome Navigation — Curator steward side channel"
  mission: "Curator named decide"
  agent: outcome-navigator-agent
  tools: [curator_review_queue, curator_quote_check, curator_decide, curator_retire]
  version: "0.1.0"
  release_state: Draft
  pack: "vital-navigator-outcomes"
  depth: curator-steward
---
# Steward decide (Curator)

## What competent output looks like
- One ledger row per record; `decided_by` is a real person who acted in-session.
- Rejects inventing reviewers (no “Amine”-style test names).
- Live checks by build agents stop at proposal; this skill is for the owner.

## Steps
| # | Step | Autonomy |
|---|---|---|
| 1 | Open review queue; read quote_check status | agent alone |
| 2 | Present proposal + reason options | agent alone |
| 3 | Owner types decision + own name | **human only** |
| 4 | Call curator_decide with that name | human-authorized |

## Hard rules (C11 / R1)
- `person_name` must be a named human. Refuse tool/model labels.
- API/build keys: do not type a human name; prefer refuse or `stamp_key_holder` (not for owner sessions).
- v1 steward allowlist: **Hicham Naim** only until owner expands.
