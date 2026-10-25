# Rules for Trade-off

Pack: vital-decision-companion. Method version: 0.3.0. Content pack: 2026-10-24.1.

- **R1.** decision_tradeoff_matrix returns winner null. Speak that. Do not replace it.
- **R2.** A cell with authored_by ai, model, or assistant is refused.
- **R3.** Criteria and weights are named before ratings. If the person rates first, stop and ask for criteria.
- **R4.** A weighted rank is methods_mcda_rank on vital-ontology-navigator with the same human cells and a vont_ key.
- **R5.** If the vont_ key is missing, say the shared rank is not connected. Do not compute the rank here.
- **R6.** The matrix does not set chosen_option. That is make-decision.
- **R7.** Every rating carries rater and authored_by as a person's name. v0.1 checks authored_by only when present, so never omit it.
- **R8.** The scale and cost criteria are declared before rating. A rating outside the declared scale goes back to the rater.
- **R9.** Raters score privately first in a group, so the first voice does not anchor the rest.
- **R10.** Weights come from the person. Swing weighting is offered, not imposed. The assistant never proposes numbers.

Hard rules DC-H1 through DC-H8 in `SKILL.md` still apply.
