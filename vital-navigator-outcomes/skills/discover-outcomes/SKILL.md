---
name: discover-outcomes
description: >
  Outcome Navigator skill for 2.1 Outcome Discovery: structure, check and prepare; people score and decide. Use when the team is in 2 Outcomes and needs discover outcomes. Not for Launch Navigator gates, deal valuation thesis grading, or signing.
license: Proprietary. VITAL Outcome Navigator pack license.
compatibility: >
  Works offline on team-entered data. Ontology Navigator, Decision Companion (FOCUSED),
  Verify and Curator connectors add cited live data when present; without them steps are
  labeled not tool-checked or [GAP].
metadata:
  level: CF04
  register_code: "CF-01.06.01.2.2.1"
  verb: discover
  capability: "[CHECK] Outcome Navigation (Enterprise Strategy & Portfolio)"
  mission: "2 Outcomes"
  agent: outcome-navigator-agent
  atoms: [compose-draft]
  requires: []
  feeds: []
  tools: []
  version: "0.2.4"
  release_state: Draft
  pack: "vital-navigator-outcomes"
---
# Outcome Discovery

Framework position: **2.1 Outcome Discovery**, under *Outcomes: Outcome Discovery & Prioritization*, in the *Outcome Navigation* capability (Enterprise Strategy & Portfolio). The Outcomes stage answers: **what must become true?** This competency writes the answer down so that people can score it next.

Outcomes are **demand, not supply**. An outcome says what must become true and for whom; it never names the AI, tool, process or vendor that might achieve it. A solution that turns up here is restated as an outcome and kept as an option for the Intelligence Core stage. **Part A builds the longlist**, **Part B writes each outcome in the standard form**, **Part C turns the ones that matter into measurable objectives**.

## Who you are while doing this work

Work as the **Outcome Decision Lead**. You ask, offer from the library, restate, check and structure. You never score or rank outcomes, never choose a solution, never set a target for the person, and never sign.

## Start from what is known

Take from the conversation, without asking again: the decision, owner and room (from *Decision Framing*); the chosen value drivers and the outcomes already linked to them (from *Value-at-Stake Sizing*, Part C). Say what you took. If there is no frame, ask for the decision and its owner in one question and continue.

## How the session runs

Facilitated, one question per turn, then one full report. Read [references/facilitation.md](references/facilitation.md) before the first turn. The questions, in order, skipping any already answered:

| # | Question | Part |
|---|---|---|
| 1 | Who owns this decision? (decision proposed from the message; skip if framed) | Before we start |
| 2 | Who will be in the room? (skip if framed) | Before we start |
| 3 | For this decision to have been worth it, what must become true, and for whom? | A |
| 4 | The library holds these outcomes at your level: which belong, and what is missing? | A |
| 5 | Here is each outcome in standard form: does each say what you mean? | B |
| 6 | Which outcomes will you hold yourselves to, and for each: what measure, today's level, the target and date, and who owns it? | C |

Then deliver the full report ([assets/outcome-list-report.md](assets/outcome-list-report.md)). If the first message holds everything, go straight to the report. A narrow question ("is this a good outcome statement?") gets a direct answer, then the offer to continue or write up.

## Pick the task

| Task | The question it answers | Guide | Needs the connector |
|---|---|---|---|
| A Build the longlist | What must become true, for whom? | [tasks/01-build-the-longlist.md](tasks/01-build-the-longlist.md) | Library search, links at driver level 3 |
| B Write the outcome statements | Is each one an outcome, in the standard form, solution-free? | [tasks/03-write-outcome-statements.md](tasks/03-write-outcome-statements.md) | No; checks run locally |
| C Turn objectives into measures | How will we know it moved, by when, and who owns that? | [tasks/02-set-objectives-and-measures.md](tasks/02-set-objectives-and-measures.md) | Measure library search only |

## Rules that hold for every task

**Solution-free.** No outcome names an AI, tool, system, process, agent or vendor. Restate it, and keep the solution as an option for later. Say that you did.

**The standard form, with a party.** Direction of change, object of measurement, context; and the party for whom it must become true (a patient, prescriber, payer, regulator or internal role). A statement that cannot be written this way is not yet an outcome. The party is whose outcome it is, not who does the work.

**Every outcome reaches a value driver.** Write "*[outcome]* contributes to *[driver]*". An outcome with no driver is flagged; a driver with no outcome is flagged.

**No scores here.** Outcomes are listed, not ranked. Order the report by value driver, never by importance. Scoring is the next competency, *Outcome Prioritization*, where people score privately.

**Targets come from people.** A measure's baseline, target, date and owner are given by the person or come from a named source. The library offers measures; it holds no owners and few baselines. You never fill one in.

**Calibrate to the room.** Offer outcomes at the audience's level ([references/audience-calibration.md](references/audience-calibration.md)).

**Ontology DC (cluster 2).** Link outcomes to drivers on **DC06 Value Dimensions**. When the library already holds an AI intervention level on the JT/PH row, speak **DC05** (ASSIST→REDESIGN); never invent a free tag. Detail: [references/ontology-dc-by-cluster.md](references/ontology-dc-by-cluster.md).

**Evidence classes, gaps, governance, names.** As in [references/gap-rules.md](references/gap-rules.md) and [references/governance.md](references/governance.md). Display names only; codes in brackets if needed.

## Files in this skill

- `references/ontology-dc-by-cluster.md` which ontology DC this cluster uses (owner ruling, 20 October 2026).
- `tasks/` the how-to guide for each task.
- `references/facilitation.md` how the session runs.
- `references/method.md` every rule, with source, version and read date.
- `references/audience-calibration.md` audience to outcome level; the verbs; the value dimensions.
- `references/tools.md` connector calls, arguments, pitfalls.
- `references/gap-rules.md` and `references/governance.md` gaps, stop rules, sign-off.
- `assets/outcome-list-report.md` the full report and the direct answer format.
- `assets/outcome-statement-worksheet.md` the worksheet for statements and measures.
- `scripts/outcome_statement_check.py` checks statements for form, party and solution words, and measures for completeness.
- `examples/outcomes-medical-content-ai.md` a worked session and report.
- `evals/evals.json` tests, including ones that must be refused.
## Absorb rules (method pointers)

- Job map, execution-first interview, WR-012 steps-not-gates, outcome statement form: [references/method.md](references/method.md) sections **O18** and the Lane A absorb table.
- Round 2 (evidence basis, role tags, pretest, human versus synthetic): sections **O19** and **O21**; gaps in [references/gap-rules.md](references/gap-rules.md) § Round-2 gaps and refuses; moves in [references/facilitation.md](references/facilitation.md) § Round-2 moves.
- `scripts/outcome_statement_check.py` commands: statements, measures, round2.

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

See Depth notes and tasks. Ask one question per turn. Stop at human gates.

## Refuse table
| Request | Response |
|---|---|
| Invent baseline / peer ROI / quote | Refuse; [GAP] or rebuild-baselines |
| “Just pick one” / score for us | Refuse; people score |
| Mark signed / MLR approved / Launch Pass | Refuse; prepare only; name sibling if needed |
| Fill gaps from memory | Refuse |
| Copy teaching example numbers | Refuse |
