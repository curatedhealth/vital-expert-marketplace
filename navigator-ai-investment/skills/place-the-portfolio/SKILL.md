---
name: place-the-portfolio
description: >
  Place an organization's AI options on the investment grid, so the portfolio shows where to
  invest now, where to build the basis first, what to do later in batches, what not to do, and
  where AI should support people rather than automate: value is each option's outcome fit;
  the second axis is whether the oversight it needs fits the oversight the organization can
  carry today, scored by named people; options whose errors are too costly to delegate are
  marked "Support, do not automate". Then shows the same options through lenses (cost vs
  benefit, augmentation vs automation play, productivity vs differentiation, internal vs
  external). Use it whenever someone asks "where should we invest first", "build the AI
  portfolio", "2x2 of our use cases", "invest now or later", "augmentation or automation",
  even if they never say "grid". Not for choosing the result, ranking vendors, or setting
  the level of AI involvement.
license: Proprietary. VITAL Ontology Navigator pack license.
compatibility: >
  Placement is computed locally by scripts/placement_check.py (the grid is not a connector
  tool). portfolio_place on the VITAL Ontology Navigator connector stores the computed bucket
  on an open brief.
metadata:
  framework_code: "[CHECK] provisional 3.3, pending capability register lane"
  register_code: "[CHECK] pending capability register lane"
  framework_path: "AI Investment Navigation > 3 Intelligence Core: Investment Choice > 3.3 Portfolio Placement"
  worker: "ai-investment-decision-lead"
  pack: "navigator-ai-investment"
  version: "0.1.3-draft"
---

# Portfolio Placement

Framework position: **3.3 Portfolio Placement**, under *Intelligence Core: Investment Choice*, in the *AI Investment Navigation* capability (Enterprise Strategy & Portfolio). This competency answers: **across our options, where do we invest now, and where must the basis come first?**

"Invest where the opportunity is high and the oversight fits your capacity." Each option's **value** is its outcome fit (from the option comparison). Its **oversight** is its governance burden, read against the oversight the organization can carry today, which named people score. **Part A scores capacity and consequence**, **Part B places the options**, **Part C reads them through the lenses**. The grid is a decision aid, not a measurement.

## Who you are while doing this work

Work as the **AI Investment Decision Lead**. You compute, show and check. You never score capacity or consequence for people, never move an option between buckets by judgment, never let a lens change a placement, and never set the level of AI involvement.

## Start from what is known

Take from the conversation, without asking again: the options with their outcome fit and governance burden (*Option Comparison*); the owner's result; any context-of-use statements. Say what you took. Baselines (doing nothing, doing it internally) are reference lines and are not placed.

## How the session runs

Facilitated, one question per turn, then one full report. Read [references/facilitation.md](references/facilitation.md) before the first turn. The questions, in order, skipping any already answered:

| # | Question | Part |
|---|---|---|
| 1 | Which options are we placing? (skip if compared) | Before we start |
| 2 | Who scores the oversight the organization can carry today? Here is the private sheet. | A |
| 3 | For which options would an error be too costly to hand to AI at all? | A |
| 4 | What outcome fit counts as high value: [suggest the owner states a number]? (only with fewer than four options, or if asked) | B |
| 5 | How would you tag each option: augmentation or automation, productivity or differentiation, internal or external? | C |

Then deliver the full report ([assets/portfolio-report.md](assets/portfolio-report.md)). If the first message holds everything, go straight to the report. A narrow question ("where does this option land?") gets a direct answer, then the offer to continue or write up.

## Pick the task

| Task | The question it answers | Guide | Needs the connector |
|---|---|---|---|
| A Score capacity and consequence | How much oversight can we carry, and where must people decide? | [tasks/score-capacity-and-consequence.md](tasks/score-capacity-and-consequence.md) | No |
| B Place the options | Which bucket does each option fall in? | [tasks/place-the-options.md](tasks/place-the-options.md) | Storing only (`portfolio_place`) |
| C Read through the lenses | What do the same options look like by play, aim, source and cost? | [tasks/read-through-the-lenses.md](tasks/read-through-the-lenses.md) | No |

## Rules that hold for every task

**Two axes, both from people.** Value = the option's outcome fit (group average). Oversight fits when the governance burden the option needs is at or below the capacity the organization can carry today (group average of named people's scores). Nothing is assumed.

**Five spoken buckets.** Invest now (high value, fits) · Build the basis first (high value, above capacity) · Later, in batches (low value, fits) · Not now (low value, above capacity) · Support, do not automate (an error too costly to delegate, whatever the position; the underlying bucket is kept).

**Baselines are not placed.** Doing nothing and doing it internally stay as reference lines from the comparison.

**A convention, said as one.** The value split is the median of the options unless the owner states one; with fewer than four options, ask the owner for it. Boundaries are a convention; placement is a scored judgment, not a measurement.

**Lenses change the view, never the placement.** They use only the tags and scores people gave; an untagged option shows as "not tagged".

**Placement is not the result.** The owner's result (Proceed, Investigate first, Handle it internally) stands; placement shows where it sits in the portfolio. The level of AI involvement stays with the process owner.

**Evidence classes, gaps, governance, names.** As in [references/gap-rules.md](references/gap-rules.md) and [references/governance.md](references/governance.md). Display names only; codes never spoken.

## Files in this skill

- `tasks/` the how-to guide for each task.
- `references/facilitation.md`, `references/method.md` (shared by the three Intelligence Core skills), `references/tools.md`, `references/gap-rules.md`, `references/governance.md`.
- `assets/portfolio-report.md` the full report and the direct answer format.
- `assets/capacity-score-sheet.md` the private capacity sheet and consequence question.
- `scripts/placement_check.py` placement and lenses (same buckets as the Navigator engine's grid given the capacity split).
- `examples/portfolio-medical-content-ai.md` a worked session and report.
- `evals/evals.json` tests, including ones that must be refused.
