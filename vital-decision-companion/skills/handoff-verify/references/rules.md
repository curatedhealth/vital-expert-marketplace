# Rules for Handoff to Verify

Pack: vital-decision-companion. Method version: 0.3.6. Content pack: 2026-10-26.1

- **R1.** Call decision_handoff_verify with session_id and the claims the person listed. called_verify is false.
- **R2.** next_tools are qualify_source and check_claim. Call them on vital-verify, in that order.
- **R3.** check_claim needs the admitted source object and a quoted passage. A passage the coach wrote does not count.
- **R4.** Without a vvfy_ key, say Verify is not connected. Do not invent a status.
- **R5.** Do not restate source grading, claim decomposition, currency, honesty, or the Verify record. Those skills live in vital-verify.
- **R6.** An unverifiable sentence stays out of the brief. It is not replaced with a guess.

Hard rules DC-H1 through DC-H8 in `SKILL.md` still apply.
