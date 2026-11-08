# Knowledge - tradeoff

Step context: **Criteria/Score**.

## Migrated working rules

# Rules for Trade-off

Pack: vital-decision-companion. Method version: 0.4.0. Content pack: 2026-10-29.1

- **R1.** decision_tradeoff_matrix returns winner null. Speak that. Do not replace it.
- **R2.** A cell with rater ai, model, assistant, or a product name is refused.
- **R3.** Criteria and weights are named before ratings. If the person rates first, stop and ask for criteria.
- **R4.** Adding up the person's own weights and ratings is `decision_score` on this connector. Navigator is only for a sealed or governed score the person asks for.
- **R5.** If there is no `vdec_` key, do not add anything up by hand; the person weighs the grid.
- **R6.** The matrix does not set chosen_option. That is make-decision.
- **R7.** Every rating carries `value` and `rater` as a person's name. Never send `score` or cell-level `authored_by`.
- **R8.** Criteria include `direction: higher_better | lower_better`. The scale is declared before rating. Send `scale` only when it is not 1–5; on hosts without `scale`, keep ratings on 1–5.
- **R9.** Raters score privately first in a group, so the first voice does not anchor the rest.
- **R10.** Weights come from the person. Swing weighting is offered, not imposed. The assistant never proposes numbers.
- **R11.** Speak `invalid_cell`, `rater_missing`, `role_only_name`, and `cell_replaced` in plain words, per index.

Hard rules DC-H1 through DC-H8 in `SKILL.md` still apply.

## Patterns

> **Teaching material, never input.** The situations below are invented for shape (DC-H2). Do not copy a name, a date, or a figure into a live answer.

# Patterns for Trade-off

Sources for the method: the Playbook Make the Decision stage (Part 9: weighted decision matrix); von Winterfeldt & Edwards (1986) and Edwards & Barron (1994) on swing weights; Kahneman, Sibony & Sunstein, Noise (2021) on independent judgments.

## Pattern 1

Person rates cost 5 for the cheapest vendor. Ask whether higher means better; declare cost as lower-is-better or keep 5 as best, and store the direction.

## Pattern 2

Person asks which option wins. Say the grid has no winner; offer the added-up totals (`decision_score`) or make-decision.

## Pattern 3

Two raters. Store each rating with its rater's name; do not average them.

## FOCUSED constants

- Person decides; skills never name a winner.
- Local session is default durability.
- MCP is special-service only.
