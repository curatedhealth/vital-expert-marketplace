---
name: design-decision-exhibits
description: >
  Build the five locked Outcome Navigator exhibits from spine outputs: sensitivity tornado, value waterfall, options matrix, delivery dependency, portfolio placement. Markdown tables + mermaid; source ids required. Not for chart fairness (frame-exhibits-honestly) or board TOC assembly (compile-board-pack).
license: Proprietary. VITAL Outcome Navigator pack license.
compatibility: >
  Offline on team-entered data. Ontology Navigator, Decision Companion (FOCUSED),
  Verify and Curator add cited live data when present; otherwise label not tool-checked or [GAP].
metadata:
  level: CF04
  register_code: "[CHECK] pending capability register lane"
  verb: design
  capability: "[CHECK] Outcome Navigation (Enterprise Strategy & Portfolio)"
  mission: "6 Communication & Exhibits"
  agent: outcome-navigator-agent
  atoms: [compose-draft, compare-against-criteria]
  requires: []
  feeds: []
  tools: [scripts/exhibit_check.py]
  version: "0.2.2"
  release_state: Draft
  pack: "vital-navigator-outcomes"
  depth: method-authored
---
# Design decision exhibits

## Locked exhibit types (v0.2 — no open menu)
1. `sensitivity_tornado` — from run-weight-sensitivity / compare-options
2. `value_waterfall` — from size-value-at-stake / track-value-realized
3. `options_matrix` — from compare-options
4. `delivery_dependency` — from plan-the-delivery
5. `portfolio_placement` — from place-the-portfolio (with Launch Not-covered callout)

## What competent output looks like
- Only locked types; each series has source id and evidence class.
- Mermaid or table matches team-entered numbers only.
- `exhibit_check.py` exits 0.
- Portfolio placement states Launch CF-04.01.09 is out of scope.

## Steps
| # | Step | Atom / tool | Autonomy |
|---|---|---|---|
| 1 | Choose locked type from upstream outputs | none | agent alone |
| 2 | Fill template from team numbers | compose-draft | agent alone |
| 3 | exhibit_check.py | scripts/exhibit_check.py | agent alone |
| 4 | Owner accepts exhibit for pack | none | human only |

## Pick the task
| Task | Guide |
|---|---|
| Build one exhibit | `tasks/01-build-exhibit.md` |
| Validate | `tasks/04-validate-exhibit.md` |


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

`scripts/exhibit_check.py` reads the fields below. Content checks are primary and fail with no confess flag set; flags such as those listed in `references/gap-rules.md` are secondary. Exit 0 = ok, 1 = gaps, 2 = usage.

| Field | Shape | Required when |
|---|---|---|
| `owner` | named person | always |
| `exhibit_type` | one of five exhibit types | always |
| `title` | non-empty string | always |
| `question` | non-empty string | always (V-C6-EXH-01) |
| `series[].name, source_id, value` | string, string, non-null number | always (V-C6-EXH-02) |
| `baseline_required, baseline_present` | bool | value_waterfall |
| `locked` | bool, set by owner | before pack seal |

Illustrative shape only. Values are placeholders for the structure and are never live input:

```json
{
  "owner": "A. Rivera",
  "exhibit_type": "options_matrix",
  "title": "Options against team criteria",
  "question": "Which option scores highest on the team's own criteria?",
  "series": [{"name": "Option A", "source_id": "team-score-sheet", "value": 7}],
  "locked": true
}
```

Method sections: `references/method.md` (C6 validator-aligned method). Worksheet: `templates/worksheet.md`. Turn questions: `intake.md`, `references/facilitation.md`. Lane A cites: LA-C6-002, LA-C6-001 in `references/lane-a-sources-c6-2026-11-08.md` (rights unknown; no new ids).
