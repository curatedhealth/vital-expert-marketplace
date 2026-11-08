---
name: compile-board-pack
description: >
  Compile the Outcome Navigator execution communication pack: Board Report TOC, Endorse/Mandate/Supply/Hold requests, embedded exhibits, evidence appendix, mapped to the shared 10-part decision record (non-gate). Requires integrity + honest exhibits first. Packet-assembly discipline adapted from READY mlr-board-prep — no M/L/R chairs, never approve. Not for taking the decision or signing.
license: Proprietary. VITAL Outcome Navigator pack license.
compatibility: >
  Offline on team-entered data. Ontology Navigator, Decision Companion (FOCUSED),
  Verify and Curator add cited live data when present; otherwise label not tool-checked or [GAP].
metadata:
  level: CF04
  register_code: "CF-01.06.01.5.1.1"
  verb: compile
  capability: "[CHECK] Outcome Navigation (Enterprise Strategy & Portfolio)"
  mission: "6 Communication & Exhibits"
  agent: outcome-navigator-agent
  atoms: [compose-draft]
  requires: []
  feeds: []
  tools: [scripts/board_pack_check.py, Navigator decide_prepare_signoff]
  version: "0.2.2"
  release_state: Draft
  pack: "vital-navigator-outcomes"
  depth: method-authored
---
# Compile board pack

## What competent output looks like
- Board report with Endorse / Mandate / Supply / Hold table.
- Shared record parts 1–10 filled or each missing part listed [GAP]; signature status prepared or blocked — never signed.
- Result vocabulary: Proceed / Investigate first / Handle it internally (not Launch gate verdicts).
- ≥1 locked exhibit embedded after frame-exhibits-honestly.
- Integrity: ground-the-numbers + cut-the-slop + verify_status (`verified` or `not tool-checked`).
- `board_pack_check.py` exits 0.

## Who you are while doing this work
Outcome Decision Lead assembling the pack. You prepare; two named humans sign outside this skill.

## Pick the task
| Task | Guide |
|---|---|
| Assemble TOC + requests | `tasks/01-assemble-pack.md` |
| Map 10-part record | `tasks/04-map-record.md` |
| Seal check | `tasks/05-seal-check.md` |

## Steps
| # | Step | Atom / tool | Autonomy |
|---|---|---|---|
| 1 | Confirm integrity + exhibits upstream | none | agent alone |
| 2 | Assemble board-report + requests | compose-draft | agent alone |
| 3 | Map/fill 10-part record gaps | compose-draft | agent with review |
| 4 | board_pack_check.py | scripts/board_pack_check.py | agent alone |
| 5 | Name two signers (one decider) | none | human only |
| 6 | Prepare sign-off if Navigator present | decide_prepare_signoff | agent alone |


## Depth notes (Draft enrichment — 7 November 2026)

This skill was enriched beyond lint scaffolding. Treat the following as binding method:

1. **Intake first** — one message; list [GAP]s; never fill from memory.
2. **Human gates** — scores, weights, choices, attestations, and signatures are human-only.
3. **Offline scripts** — compute only on team-entered numbers; refuse otherwise.
4. **Patterns** — see `references/patterns.md` for refuse/repair shapes.
5. **Grounding** — see `references/grounding-register.md`; passages in `verbatim-passages.json` are adapted peer methods tagged [CHECK] until primary sources are pinned.
6. **Integrity path for IC output** — ground-the-numbers → cut-the-slop → handoff-verify → exhibits honestly framed → compile-board-pack.
7. **Sibling boundaries** — Launch, DD/valuation, READY are handoffs, not absorbed work.
8. **GenAI** — optional vertical overlay (examples, DC05 tools), not the skill’s identity.

## Worked facilitation micro-script

- Restate the decision in one sentence and name the owner (or stop).
- Show what is known vs [GAP].
- Run the offline check if this skill has a script.
- Present options or draft; ask **one** human question that unblocks the next store.
- Name the next Outcome Navigator skill or a sibling handoff.

## Anti-goals

- Do not claim production readiness from folder completeness alone.
- Do not mark records signed.
- Do not use Launch gate verdict vocabulary unless handing off to Launch Navigator.

## Method anchoring
Outcome Navigator under Enterprise Strategy & Portfolio. Teaching examples are shape only. GenAI is a vertical overlay, not a scope limit.

## Connectors
| Connector | Use for | Never for | Without it |
|---|---|---|---|
| Ontology Navigator | decide/catalogue on team-entered numbers; prepare sign-off | scoring or signing for a person | offline templates + scripts |
| Decision Companion | dissent / premortem optional | naming a winner | task lists |
| Verify | claim checks via handoff-verify | inventing figures | not tool-checked |
| Curator | evidence tips | inventing when empty | [GAP] |

## Quality bar
People decide. Exhibits carry source ids. Board packs embed integrity posture. Assistant never signs.

## Refuse table
| Request | Response |
|---|---|
| “Just pick one” | Refuse; present options; human chooses |
| “Invent a baseline” | Refuse; rebuild-baselines or [GAP] |
| “Mark it signed” | Refuse; prepare only |
| “Skip Verify” on claim-bearing pack | Allow only with explicit **not tool-checked** label |
| Launch gate / MLR approve | Stop; sibling handoff |

## C6 check-script input: required JSON fields (C6 Phase 1, 8 November 2026)

`scripts/board_pack_check.py` reads the fields below. Content checks are primary and fail with no confess flag set; flags such as those listed in `references/gap-rules.md` are secondary. Exit 0 = ok, 1 = gaps, 2 = usage.

| Field | Shape | Required when |
|---|---|---|
| `owner, record_parts_complete` | named person, bool | always |
| `ground_the_numbers, cut_the_slop` | bool | always |
| `integrity_revisions {ground, cut, verify or verify_fallback, frame}` | non-empty strings, comparable ids such as r4 | always (V-C6-PACK-03) |
| `last_material_edit_rev` | revision id | when any material edit occurred |
| `verify_status` | verified or not tool-checked | always |
| `exhibits[] {id, type, locked}` | list; at least one locked | always |
| `prior_challenges, pack_challenges` | lists of ids | V-C6-PACK-01 when earlier challenge exists |
| `seal_requested, approved_by` | bool, named non-AI person | V-C6-PACK-04 when a seal is requested |
| `close_vocabulary` | Proceed, Investigate first, Handle it internally | optional |

Illustrative shape only. Values are placeholders for the structure and are never live input:

```json
{
  "owner": "A. Rivera",
  "record_parts_complete": true,
  "ground_the_numbers": true, "cut_the_slop": true,
  "verify_status": "not tool-checked",
  "integrity_revisions": {"ground": "r1", "cut": "r2", "verify_fallback": "r3", "frame": "r4"},
  "last_material_edit_rev": "r1",
  "exhibits": [{"id": "E1", "type": "options_matrix", "locked": true}],
  "prior_challenges": ["CH1"], "pack_challenges": ["CH1"],
  "close_vocabulary": "Investigate first"
}
```

Method sections: `references/method.md` (C6 validator-aligned method). Worksheet: `templates/worksheet.md`. Turn questions: `intake.md`, `references/facilitation.md`. Lane A cites: LA-C6-004, LA-C6-006 in `references/lane-a-sources-c6-2026-11-08.md` (rights unknown; no new ids).
