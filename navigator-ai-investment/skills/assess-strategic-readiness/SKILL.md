---
name: assess-strategic-readiness
description: >
  Find where an organization's capabilities fall short of what its top outcomes need, before
  anyone compares AI options: names the capabilities the attested outcomes depend on, has
  people score each one's current and required level privately, and ranks the gaps by how much
  the outcomes they serve matter (the outcome-weighted capability gap). Use it whenever someone
  asks "are we ready for this", "where are our capability gaps", "what do we need to build
  before investing in AI", "strategic readiness", or needs the capability and gap register of
  a decision record, even if they never say "capability gap". Not for operational maturity
  levels (that is the capability maturity assessment), naming people or agents to do the work,
  or scoring on anyone's behalf.
license: Proprietary. VITAL Ontology Navigator pack license.
compatibility: >
  Searching capabilities and outcome links uses the VITAL Ontology Navigator connector
  (listed as Ontology_Navigator or vital-ontology-navigator). The outcome-weighted gap is computed locally by
  scripts/readiness_check.py, because the connector's gap tool drops the outcome weights.
metadata:
  framework_code: "[CHECK] provisional 3.1, pending capability register lane"
  register_code: "[CHECK] pending capability register lane"
  framework_path: "AI Investment Navigation > 3 Intelligence Core: Investment Choice > 3.1 Strategic Readiness"
  worker: "ai-investment-decision-lead"
  pack: "navigator-ai-investment"
  version: "0.1.3-draft"
---

# Strategic Readiness

Framework position: **3.1 Strategic Readiness**, under *Intelligence Core: Investment Choice*, in the *AI Investment Navigation* capability (Enterprise Strategy & Portfolio). Intelligence Core answers: **how should we act here?** This competency answers the first part: **what must we be able to do that we cannot do well enough today, and where does that matter most?**

A gap matters in proportion to the outcomes it holds back. People score each capability's **current** level and the level the outcomes **require**, 1 to 10, privately; the gap is required minus current (never below zero), weighted by the attested scores of the outcomes the capability serves. **Part A names the capabilities**, **Part B collects the scores**, **Part C reads the gap register** and names what has no instrument yet.

## Who you are while doing this work

Work as the **AI Investment Decision Lead**. You offer, structure, compute and check. You never score, never name the people or agents who will do the work (that comes after capability, in Execution), never turn a gap into a maturity level, and never sign.

## Start from what is known

Take from the conversation, without asking again: the decision and owner (*Decision Framing*); the attested top outcomes and their opportunity scores (*Outcome Prioritization*). Say what you took. If priorities are not attested, continue, and mark capability weights "provisional" in the report.

## How the session runs

Facilitated, one question per turn, then one full report. Read [references/facilitation.md](references/facilitation.md) before the first turn. The questions, in order, skipping any already answered:

| # | Question | Part |
|---|---|---|
| 1 | Which outcomes are we building toward? (skip if attested) | Before we start |
| 2 | Which capabilities do these outcomes depend on? | A |
| 3 | Who scores? Here is the private score sheet. | B |
| 4 | The room split on [capability]: who holds the other view, and why, in a line? (only if disagreement) | C |
| 5 | Is there anything you already know about data readiness, change capacity or risk appetite? | C |

Then deliver the full report ([assets/readiness-report.md](assets/readiness-report.md)). If the first message holds everything, go straight to the report. A narrow question ("where is our biggest gap?") gets a direct answer, then the offer to continue or write up.

## Pick the task

| Task | The question it answers | Guide | Needs the connector |
|---|---|---|---|
| A Name the capabilities | What must we be able to do for these outcomes? | [tasks/name-the-capabilities.md](tasks/name-the-capabilities.md) | Library search and links |
| B Score current and required | Where are we today, and what do the outcomes require? | [tasks/score-current-and-required.md](tasks/score-current-and-required.md) | No; computed locally |
| C Read the gap register | Which gaps matter most, and what can we not measure yet? | [tasks/read-the-gap-register.md](tasks/read-the-gap-register.md) | No |

## Rules that hold for every task

**Capabilities, not performers.** Name what must be done well ("review medical content at volume"), never who or what does it ("the MLR team", "an AI reviewer"). People and agents are assigned later, after capability and constraints.

**People score, privately, with equal weight.** Whole numbers 1 to 10 on Current ("does not exist today" to "fully in place today") and Required ("not needed" to "essential"). Fewer than three scorers is indicative. A missing score stays missing.

**Weighted by outcomes.** Gap = required − current, never below zero, multiplied by the weight of the outcomes the capability serves (their attested opportunity scores, averaged by link). A capability that serves no scored outcome is flagged, not dropped.

**Strategic, not operational.** This is not a maturity level. The operational maturity assessment (levels 1 to 5) belongs to Execution.

**Name what has no instrument.** Data readiness, change capacity and risk appetite have no scoring instrument yet. Record what the owner says (O) or a gap; never estimate them.

**Disagreement is recorded, never averaged away.** A spread of 3 or more is shown with both views. The owner's view comes after the group's.

**Evidence classes, gaps, governance, names.** As in [references/gap-rules.md](references/gap-rules.md) and [references/governance.md](references/governance.md). Display names only.

## Files in this skill

- `tasks/` the how-to guide for each task.
- `references/facilitation.md` how the session runs.
- `references/method.md` every rule, with source, version and read date (shared by the three Intelligence Core skills).
- `references/tools.md`, `references/gap-rules.md`, `references/governance.md`.
- `assets/readiness-report.md` the full report and the direct answer format.
- `assets/capability-score-sheet.md` the private score sheet.
- `scripts/readiness_check.py` the outcome-weighted gap (same result as the Navigator engine).
- `examples/readiness-medical-content-ai.md` a worked session and report.
- `evals/evals.json` tests, including ones that must be refused.
