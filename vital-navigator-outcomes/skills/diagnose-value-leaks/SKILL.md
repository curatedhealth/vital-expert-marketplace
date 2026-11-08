---
name: diagnose-value-leaks
description: >
  Pre-frame screen of where value may leak (delay, rework, unused capacity, quality escape, missed adoption). Categories only with evidence class; never invent magnitudes. Feeds frame-the-decision. Not for sizing money value (size-value-at-stake).
license: Proprietary. VITAL Outcome Navigator pack license.
compatibility: >
  Offline on team-entered data. Connectors optional; without them label not tool-checked or [GAP].
metadata:
  level: CF04
  register_code: "[CHECK] pending capability register lane"
  verb: diagnose
  capability: "[CHECK] Outcome Navigation (Enterprise Strategy & Portfolio)"
  mission: "0 Entry"
  agent: outcome-navigator-agent
  atoms: [compose-draft]
  requires: []
  feeds: []
  tools: [scripts/leak_screen.py]
  version: "0.2.2"
  release_state: Draft
  pack: "vital-navigator-outcomes"
  depth: method-authored
---
# Diagnose value leaks

## Categories (locked)
delay · rework · unused_capacity · quality_escape · missed_adoption · other

## What competent output looks like
- Each leak has category + evidence class (M/V/H) or owner attests “none”.
- No invented $ or % magnitudes — those wait for size-value-at-stake with baselines.
- leak_screen.py exits 0.

## Absorb rules (method pointers)

- Step-level probes without invented dollars; WR-012: [references/method.md](references/method.md) § Lane A absorb — step-level probes without invented $ (job-map steps are a scaffold, not gates).
- Evidence-first leak screen and closed codes: § C5 absorb — evidence-first leak screen.
- `scripts/leak_screen.py` reads the leak wording: figures quoted in prose need a source, mandatory inspection called waste is refused, activity counts are not impact, `who` must name who bears the loss, headroom needs demand evidence.

## Steps
| # | Step | Atom / tool | Autonomy |
|---|---|---|---|
| 1 | Elicit candidate leaks | none | agent alone |
| 2 | Classify + evidence class | compose-draft | agent with review |
| 3 | leak_screen.py | scripts/leak_screen.py | agent alone |
| 4 | Owner attests list or “none” | none | human only |


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
