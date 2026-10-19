# Release review: rule shapes and the facts that bear on them

Used by B1. The rules themselves are the person's; this file gives the shapes and the sourced facts. `UX-` rows are in `ux-usability-research.md`; `CS` rows in `implementation-research.md`.

## 1. Rule shapes to offer (filled with the person's words and numbers)

| Rule type | Example shape | Checked against | Facts that bear on it |
|---|---|---|---|
| Critical-task use error | "No unresolved use error on a critical task" | A1 log by task and severity | Validation is qualitative; FDA sets no numeric error-rate acceptance (UX-US-43) |
| Control in build | "Every control listed in the use-error analysis is in the shipped build" | A2 control check | Order of preference (UX-US-33) |
| Training-only control | "No critical-task control that rests only on training without data" | A2 control types | UX-US-42, CS79 |
| Return to old step | "No participant returns to the old step on a critical task" (old register rule) | A1 log | None; the person's rule |
| Sample | "At least N per user group" | A1 participant counts | 15 per distinct population for validation (UX-US-35); formative sizes vary (UX-M-04) |
| Test conditions | "No employees, no think-aloud in validation" | A1 flags | UX-US-38, UX-US-40 |
| Satisfaction | "SUS mean at or above the person's figure" | A1 SUS | Benchmarks are context (UX-M-08 to UX-M-10) |

A task without rules gets a factual summary and no verdict.

## 2. Facts the review must not contradict

| Fact | Row |
|---|---|
| Changing labeling or training after critical-task errors needs new data showing it works. | UX-US-42 |
| If flaws appear in a validation test without prior formative work, the test becomes formative. | UX-M-06 |
| A claim of IEC 62366 compliance is not evidence. | UX-UK-16 |
| FDA recommends keeping human factors information whether or not it is submitted. | UX-US-53 |

## 3. Handoff to the regulatory owner (not decided here)

A design change found necessary in review is a change to the user interface, which is one of the Decision Point B triggers in FDA's HF content guidance (final 29 May 2026): user interface, intended users, intended uses, use environments, training or labeling (UX-US-47, UX-US-49). Whether the change needs new validation data or a submission, and which HF Submission Category applies, is the regulatory owner's decision (UX-US-48, UX-US-50, UX-US-51). B1 lists the facts and hands them over.

## 4. Ranking repairs

- `analytics.mcda` ranks repairs the person scored 0 to 4 on criteria they choose, phrased higher is better. Suggest a severity criterion ("harm severity addressed") since FDA weighs severity over probability (UX-US-32).
- `analytics.rice` only if the person asks for RICE. It has no severity term; in the live run a training update tied for first with a contrast fix and ranked above a dose-unit redesign (`examples/live/rice_repairs.json`). Confidence must be in percent (`references/tools.md`).

## 5. Not in the sources

- Any pass threshold for task success, error counts or SUS.
- Whether a release may ship: the person's release owner decides.
