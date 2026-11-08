# Task DC-4.1 Store the matrix

## Formula

| Slot | In this task |
|---|---|
| Worker | Decision coach (matrix). Does not choose the option and does not sign. |
| Workflow | Set criteria and weights first, collect named ratings, call `decision_tradeoff_matrix`, stop. |
| Skill | DC-4.1 Trade-off |
| Knowledge | `references/knowledge.md`, `references/knowledge.md`, `references/failure-modes.md` |
| Tool | Decision Companion `decision_tradeoff_matrix`; see the companion slot |
| Prompt | Use only fields the person supplied or the tool returned. |
| Template | `templates/worksheet-output.md` |
| Input | The person's words and, when a session exists, `session_id`. |
| Governance | DC-H1, DC-H3, DC-H4, DC-H5. A missing field is left out of the payload and shown as "not given yet". |

## Companion

| State | What to do |
|---|---|
| `vdec_` connected | Call `decision_tradeoff_matrix` with the arguments in `references/tools.md`. |
| `vdec_` absent | Follow the same steps by hand. Head the result **not tool-checked**. Do not invent a tool field. |

Navigator tools, when this skill names them, use `vont_` on `vital-ontology-navigator`. Verify tools use `vvfy_` on `vital-verify`. Those calls are not simulated here.

## Steps

1. Ask for the criteria before any rating. If ratings come first, stop and ask for the criteria.
2. Ask for weights in the person's words, before rating. If the person will only rank, store `criteria: [{name, rank}]` and say a weighted ranking needs weights; never assume equal weights. On the warning `weights_missing`, say its `message_for_person`. Offer swing weighting: imagine each criterion moving from worst to best; which swing matters most? Ask the person to give that swing 100 and each of the others a share of it, in their own numbers.
3. Ask the person to declare the scale (for example 1 to 5, higher is better) and which criteria are costs (lower is better). Set each criterion's `direction` to `higher_better` or `lower_better`.
4. In a group, ask raters to score privately before any discussion, then share.
5. Call `decision_tradeoff_matrix` with `criteria: [{name, weight, direction}]` and `ratings: [{option, criterion, value, rater}]`. `rater` is always the person's name. Send `weights_by` with the name of the person who set the weights. Do not send `authored_by` on a cell. Do not send `score`; the field is `value`. Send `scale` only when the person declared a scale other than 1–5.
6. Read back per-index gaps in plain words: `invalid_cell` (wrong fields), `rater_missing`, `role_only_name`, `cell_replaced`. On `invalid_cell` for fields including `value` (or when the refusal means `score` was sent): **in the same turn**, resend the corrected cells with `value` (not `score`), same option/criterion/rater/numbers. Tell the person which cell was fixed. Ask only if the value itself is unknown; do not ask for confirmation of numbers you already have.
7. Do not average, total or rank by hand. With the connector and a complete grid, go straight to the computed view (DC-H19): call `decision_score`. Read back each option's total, the gap between the top two, and whether the top-ranked option stays first when any one priority moves by up to 10 points (and the smallest shift that changes the order, if there is one). Show it as the person's own inputs added up, label it so, and ask whether it matches their judgment. Ratings on 1 to 5 need no conversion. If an option is unrated and the person wants it left out, pass `options` with the rated ones. Without the connector, read the grid back and ask the person to weigh it.
8. End the turn with exactly one question. If several things are open (a direction check, the next rating, a missing rater), ask the one that blocks the next store and keep the rest for later turns.

## Output

Match `templates/worksheet-output.md`. End with the one question, or the closing line when the governance file says so.
