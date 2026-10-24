# Rules for Verify handoff

Pack: vital-mlr-review. Method version: 0.3.1.

- **R1. `vital-mlr-review:mlr_handoff_verify` first — it does not call Verify.**
- **R2. One vvfy_ connector; no second claim checker.**
- **R3. Happy path `vital-verify:qualify_source` → `vital-verify:check_claim`.**
- **R4. Never invent statuses without tools.**

Hard rules MLR-H1 through MLR-H8 in `SKILL.md` still apply.
