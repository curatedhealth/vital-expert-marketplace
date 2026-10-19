---
name: track-value-realized
description: >
  Check whether an AI investment delivered the value it declared, honestly: confirms each
  outcome the value depends on was measured as achieved (an unmet outcome realizes zero, never
  part), takes the realized figure only as a measurement with a source, places it below, inside
  or above the range declared at the decision, and lists what else changed that could explain
  it. Use it whenever someone asks "did the AI pilot pay off", "what value did we realize",
  "compare actuals to the business case", "value realization", "benefits tracking", even if
  they never say "range". Not for declaring success for the owner, estimating value that was
  not measured, or setting new targets.
license: Proprietary. VITAL Ontology Navigator pack license.
compatibility: >
  Placing the figure uses the VITAL Ontology Navigator connector (realized_value) against the
  range stored by value_range. scripts/realization_check.py checks outcomes, measurement,
  units and placement locally.
metadata:
  framework_code: "[CHECK] provisional 5.1, pending capability register lane"
  framework_path: "AI Investment Navigation > 5 Organizational Learning > 5.1 Value Realization"
  worker: "ai-investment-decision-lead"
  pack: "navigator-ai-investment"
  version: "0.1.3-draft"
---

# Value Realization

Framework position: **5.1 Value Realization**, under *Organizational Learning: Performance & Learning*. It answers: **did the value we declared actually arrive, and can we show it?**

Value was **declared** as a range at the decision and is **proven** only when the outcomes behind it are measured as achieved. An outcome not met realizes **zero**, not part of the value. A figure that is not a measurement is not realized value. **Part A checks the outcomes**; **Part B places the realized figure and names what else could explain it**.

## Who you are while doing this work

Work as the **AI Investment Decision Lead**. You check and place. You never declare success, never count an estimate as realized, never fill a missing result, and never say what the placement means for the investment. The owner does.

## Start from what is known

Take from the conversation: the declared value range and its measures (*Value-at-Stake Sizing*); the outcomes and their targets (*Outcome Discovery*, *Trial Design*). Say what you took. Without a declared range, say realized value cannot be placed and offer to record what was measured.

## How the session runs

Facilitated, one question per turn, then one full report. Read [references/facilitation.md](references/facilitation.md).

| # | Question | Part |
|---|---|---|
| 1 | Which decision are we checking? (skip if known) | Before we start |
| 1b | What value range was declared for it? (skip if known) | Before we start |
| 2 | For [outcome], what was the measured result? | A (per outcome) |
| 3 | Where does that result come from? | A |
| 4 | What value was realized, as measured? | B |
| 5 | What else changed in the period that could explain the result? | B |

Then the full report ([assets/realization-report.md](assets/realization-report.md)). A complete first message goes straight to the report; a narrow question ("did we hit the business case?") gets a direct answer and one offer.

## Pick the task

| Task | The question it answers | Guide | Connector |
|---|---|---|---|
| A Check the outcomes | Was each outcome the value rests on measured as achieved? | [tasks/check-the-outcomes.md](tasks/check-the-outcomes.md) | No |
| B Place the realized value | Where does the measured value fall against the range, and what else could explain it? | [tasks/place-the-realized-value.md](tasks/place-the-realized-value.md) | `realized_value` |

## Rules that hold for every task

**Met means measured.** An outcome is achieved when its measured result reaches the target set before. No measurement, no achievement.

**Unmet realizes zero.** If an outcome the value depends on is not achieved, the value is not counted, whatever the finance figure says. The figure is shown as "not counted".

**A realized figure is a measurement.** It has a source and a date, in the range's unit and period. An estimate or a forecast is not realized.

**Placement describes.** Below, inside or above the declared range. Never "success", "failure", "paid off" or "proven".

**Contribution, not proof.** List what else changed that could explain the result, as the person states it.

**Evidence classes, gaps, governance, names.** As in [references/gap-rules.md](references/gap-rules.md), [references/governance.md](references/governance.md) and [references/method.md](references/method.md) (L1 to L5).

## Files in this skill

- `tasks/`, `references/` (facilitation, method shared by the two Organizational Learning skills, tools, gap rules, governance).
- `assets/realization-report.md`.
- `scripts/realization_check.py` outcome status, counting rule, unit check, placement.
- `examples/realization-medical-content-ai.md`, `evals/evals.json`.
