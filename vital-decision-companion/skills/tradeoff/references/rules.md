# Rules for Trade-off

Pack: vital-decision-companion. Method version: 0.2.0. Content pack: 2026-10-24.1.

- **R1.** decision_tradeoff_matrix returns winner null. Speak that. Do not replace it.
- **R2.** A cell with authored_by ai, model, or assistant is refused.
- **R3.** Criteria are named before ratings. If the person rates first, stop and ask for criteria.
- **R4.** A weighted rank is methods_mcda_rank on vital-ontology-navigator with the same human cells and a vont_ key.
- **R5.** If the vont_ key is missing, say the shared rank is not connected. Do not compute the rank here.
- **R6.** The matrix does not set chosen_option. That is make-decision.

Hard rules DC-H1 through DC-H8 in `SKILL.md` still apply.
