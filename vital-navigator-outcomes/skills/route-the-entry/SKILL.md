---
name: route-the-entry
description: >
  Open an Outcome Navigator session: classify top-down / middle-out / bottom-up entry, and hand off to Launch Navigator, due diligence/valuation, or READY when the question is out of scope. Not for framing the decision itself (frame-the-decision) or scoring.
license: Proprietary. VITAL Outcome Navigator pack license.
compatibility: >
  Offline on team-entered data. Connectors optional; without them label not tool-checked or [GAP].
metadata:
  level: CF04
  register_code: "CF-01.06.01.1.2.1"
  verb: route
  capability: "[CHECK] Outcome Navigation (Enterprise Strategy & Portfolio)"
  mission: "0 Entry"
  agent: outcome-navigator-agent
  atoms: [classify-text-labels, compose-draft]
  requires: []
  feeds: []
  tools: []
  version: "0.2.2"
  release_state: Draft
  pack: "vital-navigator-outcomes"
  depth: method-authored
---
# Route the entry

## What competent output looks like
- Entry path named: top-down, middle-out, or bottom-up.
- Next Outcome Navigator skill named — or a sibling plugin named with a stop.
- Not covered stated when relevant (Launch CF-04.01.09, deal thesis, MLR chairs).

## Entry paths
| Path | Signal | First next (enforced) | Then (shape-typical) |
|---|---|---|---|
| Top-down | Leader / portfolio / program question — where to place a bet | frame-the-decision | discover-outcomes → prioritize-outcomes → size → options |
| Middle-out | Work already running — too much activity, unclear value | frame-the-decision → size-value-at-stake before options | diagnose-value-leaks / discover-outcomes / review-the-portfolio |
| Bottom-up | Something underperforms — shortfall, objection, capacity bind | frame-the-decision → size-value-at-stake before options | diagnose-value-leaks / rebuild-baselines / design-the-trial |

Middle-out and bottom-up never jump straight to compare-options, place-the-portfolio, or design-the-trial: `routing_check.py` and `references/method.md` require frame then size first. Shape changes *which layers you walk*, not whether you frame.

## Sibling handoffs (stop — do not absorb)
| Topic | Route to |
|---|---|
| LEX gates, indication sequence, launch readiness | vital-launch-navigator |
| Deal thesis / asset valuation | due-diligence / valuation plugins |
| Promotional MLR board clearance | vital-mlr-review (READY) |

## Absorb rules (method pointers)

- Job versus solution at entry, WR-011 (job_executor) and WR-013 (start at execution): [references/method.md](references/method.md) § Lane A absorb — job vs solution at entry.
- Content checks in `scripts/routing_check.py`: existing skill ids only, route path frame-the-decision then size-value-at-stake for middle-out and bottom-up, launch/READY/DD vocabulary read from the ask text, family-to-sibling consistency.

## Steps
| # | Step | Atom / tool | Autonomy |
|---|---|---|---|
| 1 | Ask what is being decided and by whom | none | agent alone |
| 2 | Classify path or sibling handoff | classify-text-labels | agent alone |
| 3 | Owner confirms route | none | human only |
| 4 | Name next skill or stop | compose-draft | agent alone |

## Pick the task
| Task | Guide |
|---|---|
| Classify entry | `tasks/01-classify-entry.md` |
| Sibling handoff | `tasks/04-sibling-handoff.md` |


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
