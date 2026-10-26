# Rules for Brief

Pack: vital-decision-companion. Method version: 0.3.16. Content pack: 2026-10-26.1

- **R1.** Call decision_build_brief with session_id.
- **R2.** A complete stage is rendered from its stored payload. An incomplete stage is shown as "not given yet".
- **R3.** Do not invent a plausible paragraph for a missing field.
- **R4.** watermark SIMULATED means practice. Say so at the top of every page.
- **R5.** The brief is a draft. It is not a signature and it is not clearance.
- **R6.** Compile when the person asks, or when every stage required by the confirmed rigor is complete or explicitly skipped.
- **R7.** If the brief prints `None`, `null`, or `{}`, or omits a stored field, show "not given yet" or pull the field from `decision_status`, and say you did so.

Hard rules DC-H1 through DC-H8 in `SKILL.md` still apply.
