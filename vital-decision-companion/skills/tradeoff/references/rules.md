# Rules for Trade-off

Pack: vital-decision-companion. Method version: 0.3.14. Content pack: 2026-10-26.1

- **R1.** decision_tradeoff_matrix returns winner null. Speak that. Do not replace it.
- **R2.** A cell with rater ai, model, assistant, or a product name is refused.
- **R3.** Criteria and weights are named before ratings. If the person rates first, stop and ask for criteria.
- **R4.** A weighted rank is methods_mcda_rank on vital-ontology-navigator with the same human cells and a vont_ key.
- **R5.** If the vont_ key is missing, say the shared rank is not connected. Do not compute the rank here.
- **R6.** The matrix does not set chosen_option. That is make-decision.
- **R7.** Every rating carries `value` and `rater` as a person's name. Never send `score` or cell-level `authored_by`.
- **R8.** Criteria include `direction: higher_better | lower_better`. The scale is declared before rating. Send `scale` only when it is not 1–5; on hosts without `scale`, keep ratings on 1–5.
- **R9.** Raters score privately first in a group, so the first voice does not anchor the rest.
- **R10.** Weights come from the person. Swing weighting is offered, not imposed. The assistant never proposes numbers.
- **R11.** Speak `invalid_cell`, `rater_missing`, `role_only_name`, and `cell_replaced` in plain words, per index.

Hard rules DC-H1 through DC-H8 in `SKILL.md` still apply.
