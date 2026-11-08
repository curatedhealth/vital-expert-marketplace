---
name: run-weight-sensitivity
description: >
  Show option rank swaps under one-way weight swings using team-entered weights and totals only. Distinct from Launch Navigator launch-scenario tornados. Feeds design-decision-exhibits. Not for changing weights without the team or choosing a winner.
license: Proprietary. VITAL Outcome Navigator pack license.
compatibility: >
  Offline on team-entered data. Connectors optional; without them label not tool-checked or [GAP].
metadata:
  level: CF04
  register_code: "CF-01.06.01.3.4.1"
  verb: run
  capability: "[CHECK] Outcome Navigation (Enterprise Strategy & Portfolio)"
  mission: "3 Intelligence Core"
  agent: outcome-navigator-agent
  atoms: [compare-against-criteria, rank-by-consequence]
  requires: []
  feeds: []
  tools: [scripts/sensitivity_exhibit.py]
  version: "0.2.3"
  release_state: Draft
  pack: "vital-navigator-outcomes"
  depth: method-authored
---
# Run weight sensitivity

## What competent output looks like
- Base rank from team totals; each swung rank labeled stable or swaps listed.
- Weights and swing bands set by people — script never invents them.
- Output ready for sensitivity_tornado exhibit.

## Steps
| # | Step | Atom / tool | Autonomy |
|---|---|---|---|
| 1 | Confirm locked weights/totals from compare-options | none | human only |
| 2 | Define swing set (team) | none | human only |
| 3 | sensitivity_exhibit.py | scripts/sensitivity_exhibit.py | agent alone |
| 4 | Draft tornado for design-decision-exhibits | compose-draft | agent alone |


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

## Read before you start

- references/facilitation.md (question table, eight-rule shape) before the first turn
- references/gap-rules.md (Rule-ID SSOT; V-C3-SEN-01 to 05) before writing a gap or a refusal
- references/method.md and references/method-standards.md before defining the swing set
- scripts/sensitivity_exhibit.py for the content checks (model fields, frozen scores and anchors, diagnostic wording, robustness claims) and the offline envelope

VP-ON-C3 verbatim candidates: `reuse_cleared: owner_internal_pack_yes` (Option A, internal method only; `diligence/OWNER_HITL_TRIAGE_C3_VP_REUSE_2026-11-08.md`). Not marketing/chrome. Landing optional.

## Method anchoring
Outcome Navigator. Teaching examples are shape only. GenAI is one vertical.

## Connectors
| Connector | Use for | Never for | Without it |
|---|---|---|---|
| Ontology Navigator | context | deciding for the person | offline worksheets |
| Sibling plugins | handoff targets | absorbing their work | name plugin and stop |
| Verify / Curator | later integrity / evidence | at entry routing | n/a |

## Quality bar
Route honestly. Do not absorb Launch, DD, Valuation or READY work. People own scores and baselines.

## Refuse table
| Request | Response |
|---|---|
| “Just pick one” | Refuse; present options; human chooses |
| “Invent a baseline” | Refuse; rebuild-baselines or [GAP] |
| “Mark it signed” | Refuse; prepare only |
| “Skip Verify” on claim-bearing pack | Allow only with explicit **not tool-checked** label |
| Launch gate / MLR approve | Stop; sibling handoff |

## Competent output (assessable)
- Every number is team-entered or `[GAP]`; never invented.
- Human gates name the deciding role; assistant does not score, weight, choose or sign.
- Offline scripts run only on supplied inputs; soft issues become flags.
- Deliverable uses the skill templates; open items listed; next skill or sibling handoff named.
- Not covered work (Launch / DD / READY chairs) is refused with a named route.

## Method anchoring
Each judgement cites a method-standards id (MS-*) or is marked `[CHECK]`. Failure modes are screened before release of claim-bearing text.

## Connector use
Offline first. Live connectors, when used, are cited with access date. Claim-bearing packs without Verify are labeled **not tool-checked**.

## Quality bar (release of this skill's draft)
1. Intake gaps visible
2. Tasks complete in order
3. Script exit 0 or explained flags
4. Examples' teaching figures not copied live
5. Governance human gates respected
