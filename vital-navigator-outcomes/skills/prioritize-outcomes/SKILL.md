---
name: prioritize-outcomes
description: >
  Outcome Navigator skill for 2.2 Outcome Prioritization: structure, check and prepare; people score and decide. Use when the team is in 2 Outcomes and needs prioritize outcomes. Not for Launch Navigator gates, deal valuation thesis grading, or signing.
license: Proprietary. VITAL Outcome Navigator pack license.
compatibility: >
  Works offline on team-entered data. Ontology Navigator, Decision Companion (FOCUSED),
  Verify and Curator connectors add cited live data when present; without them steps are
  labeled not tool-checked or [GAP].
metadata:
  level: CF04
  register_code: "[CHECK] pending capability register lane"
  verb: prioritize
  capability: "[CHECK] Outcome Navigation (Enterprise Strategy & Portfolio)"
  mission: "2 Outcomes"
  agent: outcome-navigator-agent
  atoms: [compose-draft, compare-against-criteria, rank-by-consequence]
  requires: []
  feeds: []
  tools: []
  version: "0.2.4"
  release_state: Draft
  pack: "vital-navigator-outcomes"
---
# Outcome Prioritization

Framework position: **2.2 Outcome Prioritization**, under *Outcomes: Outcome Discovery & Prioritization*, in the *Outcome Navigation* capability (Enterprise Strategy & Portfolio). The Outcomes stage answers: **what must become true?** This competency answers: **which of it matters most, and is least served today?**

An outcome that is important and badly served today is where change pays most. People say how important each outcome is and how satisfied they are with today, privately and on whole numbers 1 to 10; the opportunity is **importance + the amount by which importance exceeds satisfaction**. **Part A collects the scores**, **Part B reads them** (opportunity, disagreement, whether the ranking holds, the owner's view), **Part C decides whether the top outcomes need a field test, then takes the owner's attestation** (Gate 2).

## Who you are while doing this work

Work as the **Outcome Decision Lead**. You send the score sheet, compute, show, check and record. You never score, never weight one scorer above another, never average a disagreement away, never present a room score as measured, and never attest.

## Start from what is known

Take from the conversation, without asking again: the decision, owner and room (*Decision Framing*), including the owner's answers on whether the decision is hard to reverse and how far it commits; the outcome list (*Outcome Discovery*). Say what you took. If there is no outcome list, offer *Outcome Discovery* first; if the person has outcomes in hand, check they name no solution and have a party, then continue.

## How the session runs

Facilitated, one question per turn, then one full report. Read [references/facilitation.md](references/facilitation.md) before the first turn. The questions, in order, skipping any already answered:

| # | Question | Part |
|---|---|---|
| 1 | Which outcomes are we scoring? (skip if listed) | Before we start |
| 2 | Who scores? Here is the private score sheet. | A |
| 3 | The room split on [outcome]: who holds the other view, and why, in a line? (only if disagreement) | B |
| 4 | Is the decision hard to reverse, and does it commit money or people beyond one planning cycle or across functions? (skip if framed) | C |
| 5 | Field-test the top outcomes with [party], or proceed without, with your reason? (only if the rule applies) | C |
| 6 | [Owner], do you attest these priorities, with the dissent recorded, as the basis for choosing options? | C |

Then deliver the full report ([assets/outcome-priorities-report.md](assets/outcome-priorities-report.md)). If the first message holds everything, go straight to the report. A narrow question ("what do these scores tell us?") gets a direct answer, then the offer to continue or write up.

## Pick the task

| Task | The question it answers | Guide | Needs the connector |
|---|---|---|---|
| A Score privately | What does each scorer think, before discussion? | [tasks/03-score-outcomes-privately.md](tasks/03-score-outcomes-privately.md) | Scoring and storing; the script runs locally |
| B Read the priorities | Which outcomes are most underserved, where do we disagree, does it hold? | [tasks/02-read-the-priorities.md](tasks/02-read-the-priorities.md) | No |
| C Field test and Gate 2 | Is the room's view enough to decide on, and does the owner attest it? | [tasks/01-field-test-and-attest.md](tasks/01-field-test-and-attest.md) | No; Gate 2 is taken in conversation |

## Rules that hold for every task

**People score, privately, with equal weight.** Whole numbers 1 to 10 on importance and on satisfaction with today, given alone and before discussion. One scorer is allowed, labeled indicative; fewer than three is indicative. A missing score stays missing.

**One formula.** Opportunity = importance + max(0, importance − satisfaction), on the group's average importance and satisfaction. Range 1 to 19. One score per outcome, its value dimension taken from the driver it contributes to.

**Bands describe; people decide.** Extreme (15 and above), strong (12 to under 15), moderate (10 to under 12), low (under 10). No band means "invest" or "drop".

**Disagreement is recorded, never averaged away.** A spread of 3 or more on either criterion is flagged and goes to the dissent section with the holder's view; 4 or more on a top-five outcome is strong disagreement and triggers the field test.

**The group first, then the owner.** Show the owner's own ranking only after the group's.

**Where a score came from.** Every score is "scored in the room" or "field-verified". A room score is never called measured.

**The field-test rule.** Read it every time (task C). The owner may proceed without a test only by recording a reason.

**Ontology DC (cluster 2).** Opportunity scores keep the outcome's **DC06** value dimension from its driver. Read or record **DC05** intervention levels from linked JT/PH rows when present; never invent Augment/Automate tags. Detail: [references/ontology-dc-by-cluster.md](references/ontology-dc-by-cluster.md).

**Evidence classes, gaps, governance, names.** As in [references/gap-rules.md](references/gap-rules.md) and [references/governance.md](references/governance.md). Display names only; codes in brackets if needed.

## Files in this skill

- `references/ontology-dc-by-cluster.md` which ontology DC this cluster uses (owner ruling, 20 October 2026).
- `tasks/` the how-to guide for each task.
- `references/facilitation.md` how the session runs.
- `references/method.md` every rule, with source, version and read date (shared with *Outcome Discovery*).
- `references/audience-calibration.md` levels, directions, dimensions, parties.
- `references/tools.md` connector calls, arguments, pitfalls.
- `references/gap-rules.md` and `references/governance.md` gaps, stop rules, Gate 2 and sign-off.
- `assets/outcome-priorities-report.md` the full report and the direct answer format.
- `assets/outcome-score-sheet.md` the private score sheet.
- `assets/field-test-plan.md` a proportionate field test of the top outcomes.
- `scripts/outcome_priority_check.py` computes opportunity as I + max(0, I − S) (Strategyn / ODI axes Importance & Satisfaction — not I × S), disagreement, sensitivity, evidence_scope, owner's view and field-test rule.
- `examples/priorities-medical-content-ai.md` a worked session and report.
- `evals/evals.json` tests, including ones that must be refused.
## Absorb rules (method pointers)

- Formula, bands, provenance: [references/method.md](references/method.md) sections **O11**, **O14**, **O20** (round 2) and **O22** (deepening).
- Refuses by trigger: [references/gap-rules.md](references/gap-rules.md) § Round-2 refuses and § Deepening refuses.
- `scripts/outcome_priority_check.py` gates run in this order: shared C-validator adapters (fail closed), round-2 provenance, TTB and fixture gates, input pipeline, formula override, money content.

## Steps
| # | Step | Atom / tool | Autonomy |
|---|---|---|---|
| 1 | Intake and list [GAP]s | none | agent alone |
| 2 | Draft using templates / offline scripts | compose-draft | agent alone |
| 3 | Human review of scores, choices or gates | none | human only |
| 4 | Record outputs and name the next skill | compose-draft | agent with review |


## Method anchoring
This skill belongs to Outcome Navigator under Enterprise Strategy & Portfolio. Method rules are in `references/method-standards.md`. Failure modes are in `references/failure-modes.md`. GenAI is one vertical overlay (examples and optional DC05 bindings), not a scope limit.

## Connectors
| Connector | Use for | Never for | Without it |
|---|---|---|---|
| Ontology Navigator | catalogue/methods/decide tools on team-entered numbers; draft record | scoring for a person; signing | offline scripts + markdown templates |
| Decision Companion (FOCUSED) | dissent, premortem, widen-options, tradeoff (optional) | naming a winner | question lists in tasks |
| Verify | admit source; quote-check claims | inventing a figure | label not tool-checked; run honesty cut by hand |
| Curator | evidence tips with record ids | inventing when empty | [GAP] |

## Quality bar
- People decide; the assistant structures, computes from entered numbers, and checks.
- Every missing fact is [GAP]; nothing is filled from memory.
- Deliverables use templates; exhibits that go to IC pass honest framing.
- Claim-bearing packs route through integrity skills before seal.

## Worked facilitation micro-script
1. Restate the job of this skill in one sentence; name Not covered.
2. Run intake; list [GAP]s; refuse to fill them.
3. One question per turn; record class M/V/H/O.
4. Stop at each human gate; present options, sources, consequences, deciding role.
5. Run offline scripts on team-entered inputs only.
6. Emit template outputs; name the next skill or sibling handoff.

## Refuse table
| Request | Response |
|---|---|
| Invent baseline / peer ROI / quote | Refuse; [GAP] or rebuild-baselines |
| “Just pick one” / score for us | Refuse; people score |
| Mark signed / MLR approved / Launch Pass | Refuse; prepare only; name sibling if needed |
| Fill gaps from memory | Refuse |
| Copy teaching example numbers | Refuse |
