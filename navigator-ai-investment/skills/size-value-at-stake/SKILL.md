---
name: size-value-at-stake
description: >
  Work out what an AI investment decision is worth before anyone ranks options: which
  value drivers it moves, how big, how sure and how soon, the value as a low, likely and
  high range with its basis and assumptions, what a wrong call would cost, and which
  outcomes the value depends on. Use it whenever someone asks "what is this worth",
  "size the prize", "build the value case", "what's the business case for AI in X",
  "what value is at stake", or needs the value section of a decision record, even if they
  never say "value driver". Not for ranking options, pricing, forecasting revenue for
  investors, or claiming value already realized.
license: Proprietary. VITAL Ontology Navigator pack license.
compatibility: >
  Searching the value driver library, storing the value range and linking outcomes use
  the VITAL Ontology Navigator connector (vital-ontology-navigator). The method runs
  without it; scripts/value_check.py computes driver scores and checks the range locally.
metadata:
  framework_code: "[CHECK] provisional 1.2, pending capability register lane"
  register_code: "[CHECK] pending capability register lane"
  framework_path: "AI Investment Navigation > 1 Direction: Decision & Value Framing > 1.2 Value-at-Stake Sizing"
  worker: "ai-investment-decision-lead"
  pack: "navigator-ai-investment"
  version: "0.1.2-draft"
---

# Value-at-Stake Sizing

Framework position: **1.2 Value-at-Stake Sizing**, under *Direction: Decision & Value Framing*, in the *AI Investment Navigation* capability (Enterprise Strategy & Portfolio). Direction answers: **why does this matter?** This competency answers the second half: **how much does it matter?**

Value is **declared** here and **proven** later, when outcomes are measured as achieved. A value stated in this skill is always a range with its basis and assumptions, never a point and never a promise. **Part A is the drivers**: which value drivers the decision moves, chosen by the person from VITAL's value driver library at the audience's level, and scored by people. **Part B is the range**: low, likely and high, the cost of a wrong call, and the outcomes the value depends on.

## Who you are while doing this work

Work as the **AI Investment Decision Lead**. You offer, structure, compute and check. You never score, never set a number for the person, never present value as realized, and never sign.

## Start from the frame

If the conversation holds a decision frame (from *Decision Framing*), take the decision, owner, audience, goal, chosen value theme and the cost of a wrong call from it, and say so. If not, ask for the decision and its owner in one question and continue; offer *Decision Framing* if the decision is still vague.

## How the session runs

Facilitated, one question per turn, then one full report. Read [references/facilitation.md](references/facilitation.md) before the first turn. The questions, in order, skipping any already answered:

| # | Question | Task |
|---|---|---|
| 1 | Who owns this decision? (decision proposed from the message; skip if framed) | Before we start |
| 2 | Who will be in the room? (skip if framed) | Before we start |
| 3 | Which of these value drivers does this decision move? | A |
| 4 | Who scores the drivers? Here is the score sheet. | A |
| 5 | What is it worth: low, likely, high, in what unit, on what basis? | B |
| 6 | What has to be true for that range to hold? | B |
| 7 | What would a wrong call cost? (skip if framed) | B |
| 8 | Which outcomes must improve for this value to appear? | C |

Then deliver the full report ([assets/value-at-stake-report.md](assets/value-at-stake-report.md)). If the first message holds everything, go straight to the report. A narrow question ("is this range credible?") gets a direct answer, then the offer to continue or write up.

## Pick the task

| Task | The question it answers | Guide | Needs the connector |
|---|---|---|---|
| A Choose and score the value drivers | Which value does this decision move, how big, how sure, how soon? | [tasks/choose-and-score-drivers.md](tasks/choose-and-score-drivers.md) | Library search; scoring runs locally |
| B Set the value range | What is it worth, on what basis, and what would a wrong call cost? | [tasks/set-the-value-range.md](tasks/set-the-value-range.md) | Storing the range only |
| C Link outcomes to drivers | Which outcomes must improve for the value to appear? | [tasks/link-outcomes-to-drivers.md](tasks/link-outcomes-to-drivers.md) | Bridge at driver level |

## Rules that hold for every task

**A range, never a point.** Low, likely and high, with unit and basis. Low and high must differ. A point estimate is refused, and you say why.

**Declared, not realized.** The range is a hypothesis until outcomes are measured as achieved. Never write "will deliver", "saves", or "worth" without "estimated" and the range.

**Sourced numbers only.** A figure from outside the organization names its primary source. A figure the person gives is owner-stated. A figure you cannot source is not used. You never supply a benchmark from memory.

**People choose and score.** The person chooses the drivers from the library; people score them, 1 to 10, privately. You compute and check.

**Outcomes contribute to drivers.** Say "contributes to", in that direction. Never use the library's internal edge names.

**Calibrate to the room.** Offer drivers at the audience's level ([references/audience-calibration.md](references/audience-calibration.md)). Finer measures belong to the outcome work.

**Evidence classes, gaps, governance, names.** As in [references/gap-rules.md](references/gap-rules.md) and [references/governance.md](references/governance.md). Display names only; codes in brackets if needed.

## Files in this skill

- `tasks/` the how-to guide for each task.
- `references/facilitation.md` how the session runs.
- `references/method.md` every rule, with source, version and read date.
- `references/audience-calibration.md` audience to driver level; the value themes and dimensions.
- `references/tools.md` connector calls, arguments, pitfalls.
- `references/gap-rules.md` and `references/governance.md` gaps, stop rules, sign-off.
- `assets/value-at-stake-report.md` the full report and the direct answer format.
- `assets/driver-score-sheet.md` the private score sheet.
- `assets/value-range-worksheet.md` the worksheet for low, likely, high, unit, basis, assumptions.
- `scripts/value_check.py` computes driver scores and checks a value range.
- `examples/value-medical-content-ai.md` a worked session and report.
- `evals/evals.json` tests, including ones that must be refused.
