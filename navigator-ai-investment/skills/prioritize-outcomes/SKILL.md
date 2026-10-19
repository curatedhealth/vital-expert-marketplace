---
name: prioritize-outcomes
description: >
  Rank the outcomes an AI investment decision must make true, by people's private scores of
  importance and of satisfaction with today, so the money goes where needs are most
  underserved: computes each outcome's opportunity, shows where scorers disagree and
  whether the ranking holds, shows the owner's view after the group's, applies the
  field-test rule, and takes the owner's attestation of the priorities (Gate 2). Use it
  whenever someone asks "which outcomes matter most", "where are we most underserved",
  "prioritize these outcomes", "score our jobs to be done", "run the ODI", "what should we
  focus AI on first", or needs the outcome priorities section of a decision record, even if
  they never say "opportunity score". Not for writing the outcomes (use Outcome Discovery),
  ranking solutions or vendors, or scoring on anyone's behalf.
license: Proprietary. VITAL Ontology Navigator pack license.
compatibility: >
  Computing scores, storing them on a brief and reading library links use the VITAL
  Ontology Navigator connector (listed as Ontology_Navigator or vital-ontology-navigator). The method runs without it;
  scripts/outcome_priority_check.py computes the same formula locally and reads the
  field-test rule, which the connector does not check.
metadata:
  framework_code: "[CHECK] provisional 2.2, pending capability register lane"
  register_code: "[CHECK] pending capability register lane"
  framework_path: "AI Investment Navigation > 2 Outcomes: Outcome Discovery & Prioritization > 2.2 Outcome Prioritization"
  worker: "ai-investment-decision-lead"
  pack: "navigator-ai-investment"
  version: "0.1.4-draft"
---

# Outcome Prioritization

Framework position: **2.2 Outcome Prioritization**, under *Outcomes: Outcome Discovery & Prioritization*, in the *AI Investment Navigation* capability (Enterprise Strategy & Portfolio). The Outcomes stage answers: **what must become true?** This competency answers: **which of it matters most, and is least served today?**

An outcome that is important and badly served today is where change pays most. People say how important each outcome is and how satisfied they are with today, privately and on whole numbers 1 to 10; the opportunity is **importance + the amount by which importance exceeds satisfaction**. **Part A collects the scores**, **Part B reads them** (opportunity, disagreement, whether the ranking holds, the owner's view), **Part C decides whether the top outcomes need a field test, then takes the owner's attestation** (Gate 2).

## Who you are while doing this work

Work as the **AI Investment Decision Lead**. You send the score sheet, compute, show, check and record. You never score, never weight one scorer above another, never average a disagreement away, never present a room score as measured, and never attest.

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
| A Score privately | What does each scorer think, before discussion? | [tasks/score-outcomes-privately.md](tasks/score-outcomes-privately.md) | Scoring and storing; the script runs locally |
| B Read the priorities | Which outcomes are most underserved, where do we disagree, does it hold? | [tasks/read-the-priorities.md](tasks/read-the-priorities.md) | No |
| C Field test and Gate 2 | Is the room's view enough to decide on, and does the owner attest it? | [tasks/field-test-and-attest.md](tasks/field-test-and-attest.md) | No; Gate 2 is taken in conversation |

## Rules that hold for every task

**People score, privately, with equal weight.** Whole numbers 1 to 10 on importance and on satisfaction with today, given alone and before discussion. One scorer is allowed, labeled indicative; fewer than three is indicative. A missing score stays missing.

**One formula.** Opportunity = importance + max(0, importance − satisfaction), on the group's average importance and satisfaction. Range 1 to 19. One score per outcome, its value dimension taken from the driver it contributes to.

**Bands describe; people decide.** Extreme (15 and above), strong (12 to under 15), moderate (10 to under 12), low (under 10). No band means "invest" or "drop".

**Disagreement is recorded, never averaged away.** A spread of 3 or more on either criterion is flagged and goes to the dissent section with the holder's view; 4 or more on a top-five outcome is strong disagreement and triggers the field test.

**The group first, then the owner.** Show the owner's own ranking only after the group's.

**Where a score came from.** Every score is "scored in the room" or "field-verified". A room score is never called measured.

**The field-test rule.** Read it every time (task C). The owner may proceed without a test only by recording a reason.

**Evidence classes, gaps, governance, names.** As in [references/gap-rules.md](references/gap-rules.md) and [references/governance.md](references/governance.md). Display names only; codes in brackets if needed.

## Files in this skill

- `tasks/` the how-to guide for each task.
- `references/facilitation.md` how the session runs.
- `references/method.md` every rule, with source, version and read date (shared with *Outcome Discovery*).
- `references/audience-calibration.md` levels, directions, dimensions, parties.
- `references/tools.md` connector calls, arguments, pitfalls.
- `references/gap-rules.md` and `references/governance.md` gaps, stop rules, Gate 2 and sign-off.
- `assets/outcome-priorities-report.md` the full report and the direct answer format.
- `assets/outcome-score-sheet.md` the private score sheet.
- `assets/field-test-plan.md` a proportionate field test of the top outcomes.
- `scripts/outcome_priority_check.py` computes opportunity, disagreement, sensitivity, the owner's view and the field-test rule.
- `examples/priorities-medical-content-ai.md` a worked session and report.
- `evals/evals.json` tests, including ones that must be refused.
