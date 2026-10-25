# Rules for Widen options

Pack: vital-decision-companion. Method version: 0.3.2. Content pack: 2026-10-26.1

- **R1.** Pass options as a list of objects with name. Empty names are refused.
- **R2.** Warnings, not errors: fewer than 3 options (`too_few_options` reads as "2 of 3 options"); do-nothing missing; do-it-internally missing. Warnings appear on both `decision_widen_options` and `run_stage`.
- **R3.** If a warning is present, ask the person for that option. Do not insert one.
- **R4.** The stage is complete when the stored list has at least three options.
- **R5.** Ids may be omitted. The tool assigns opt-1 and onward.
- **R6.** This skill does not rate and does not rank.
- **R7.** Ask one widening question per turn: and what else, vanishing options, opportunity cost, both-and, outside view.
- **R8.** A yes-or-no list is a whether-or-not frame. Name it and ask for another option.
- **R9.** Store widening answers via `decision_run_stage` on widen_options: `vanishing_options_answer`, `opportunity_cost`, `outside_view`.
- **R10.** After `decision_widen_options`, call `decision_status`. If the widen stage is still incomplete with 3 or more options stored, call `run_stage widen_options {options}` once so the stage completes.

Hard rules DC-H1 through DC-H8 in `SKILL.md` still apply.
