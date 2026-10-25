# Rules for Widen options

Pack: vital-decision-companion. Method version: 0.2.0. Content pack: 2026-10-24.1.

- **R1.** Pass options as a list of objects with name. Empty names are refused.
- **R2.** Warnings, not errors: fewer than 3 options; do-nothing missing; do-it-internally missing.
- **R3.** If a warning is present, ask the person for that option. Do not insert one.
- **R4.** The stage is complete when the stored list has at least three options.
- **R5.** Ids may be omitted. The tool assigns opt-1 and onward.
- **R6.** This skill does not rate and does not rank.

Hard rules DC-H1 through DC-H8 in `SKILL.md` still apply.
