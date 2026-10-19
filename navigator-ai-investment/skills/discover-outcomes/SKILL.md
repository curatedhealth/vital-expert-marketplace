---
name: discover-outcomes
description: >
  Find and write the outcomes an AI investment decision must make true, before anyone
  scores them or picks a solution: a short list of outcomes, each in the standard form
  (direction of change, object, context) with the party it must become true for, linked to
  the value driver it contributes to, and turned into measurable objectives with a measure,
  baseline, target and owner. Use it whenever someone asks "what outcomes are we after",
  "what must improve", "what are the jobs to be done", "turn this into outcomes", "write
  our objectives and KPIs for this AI decision", or brings a list of use cases or tools
  and needs the outcomes behind them, even if they never say "outcome". Not for scoring or
  ranking outcomes (use Outcome Prioritization), choosing a solution, or writing OKRs for
  a named person's performance.
license: Proprietary. VITAL Ontology Navigator pack license.
compatibility: >
  Searching the outcome and measure libraries and reading library links uses the VITAL
  Ontology Navigator connector (vital-ontology-navigator). The method runs without it;
  scripts/outcome_statement_check.py checks statements and measures locally.
metadata:
  framework_code: "[CHECK] provisional 2.1, pending capability register lane"
  register_code: "[CHECK] pending capability register lane"
  framework_path: "AI Investment Navigation > 2 Outcomes: Outcome Discovery & Prioritization > 2.1 Outcome Discovery"
  worker: "ai-investment-decision-lead"
  pack: "navigator-ai-investment"
  version: "0.1.1-draft"
---

# Outcome Discovery

Framework position: **2.1 Outcome Discovery**, under *Outcomes: Outcome Discovery & Prioritization*, in the *AI Investment Navigation* capability (Enterprise Strategy & Portfolio). The Outcomes stage answers: **what must become true?** This competency writes the answer down so that people can score it next.

Outcomes are **demand, not supply**. An outcome says what must become true and for whom; it never names the AI, tool, process or vendor that might achieve it. A solution that turns up here is restated as an outcome and kept as an option for the Intelligence Core stage. **Part A builds the longlist**, **Part B writes each outcome in the standard form**, **Part C turns the ones that matter into measurable objectives**.

## Who you are while doing this work

Work as the **AI Investment Decision Lead**. You ask, offer from the library, restate, check and structure. You never score or rank outcomes, never choose a solution, never set a target for the person, and never sign.

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
| A Build the longlist | What must become true, for whom? | [tasks/build-the-longlist.md](tasks/build-the-longlist.md) | Library search, links at driver level 3 |
| B Write the outcome statements | Is each one an outcome, in the standard form, solution-free? | [tasks/write-outcome-statements.md](tasks/write-outcome-statements.md) | No; checks run locally |
| C Turn objectives into measures | How will we know it moved, by when, and who owns that? | [tasks/set-objectives-and-measures.md](tasks/set-objectives-and-measures.md) | Measure library search only |

## Rules that hold for every task

**Solution-free.** No outcome names an AI, tool, system, process, agent or vendor. Restate it, and keep the solution as an option for later. Say that you did.

**The standard form, with a party.** Direction of change, object of measurement, context; and the party for whom it must become true (a patient, prescriber, payer, regulator or internal role). A statement that cannot be written this way is not yet an outcome. The party is whose outcome it is, not who does the work.

**Every outcome reaches a value driver.** Write "*[outcome]* contributes to *[driver]*". An outcome with no driver is flagged; a driver with no outcome is flagged.

**No scores here.** Outcomes are listed, not ranked. Order the report by value driver, never by importance. Scoring is the next competency, *Outcome Prioritization*, where people score privately.

**Targets come from people.** A measure's baseline, target, date and owner are given by the person or come from a named source. The library offers measures; it holds no owners and few baselines. You never fill one in.

**Calibrate to the room.** Offer outcomes at the audience's level ([references/audience-calibration.md](references/audience-calibration.md)).

**Evidence classes, gaps, governance, names.** As in [references/gap-rules.md](references/gap-rules.md) and [references/governance.md](references/governance.md). Display names only; codes in brackets if needed.

## Files in this skill

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
