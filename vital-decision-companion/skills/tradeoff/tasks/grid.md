# Task DC-4.1 Store the matrix

## Formula

| Slot | In this task |
|---|---|
| Worker | Decision coach (matrix). Does not choose the option and does not sign. |
| Workflow | Set criteria and weights first, collect named ratings, call `decision_tradeoff_matrix`, stop. |
| Skill | DC-4.1 Trade-off |
| Knowledge | `references/rules.md`, `references/patterns.md`, `references/gap-rules.md` |
| Tool | Decision Companion `decision_tradeoff_matrix`; see the companion slot |
| Prompt | Use only fields the person supplied or the tool returned. |
| Template | `assets/worksheet-output.md` |
| Input | The person's words and, when a session exists, `session_id`. |
| Governance | DC-H1, DC-H3, DC-H4, DC-H5. A missing field stays `[GAP]`. |

## Companion

| State | What to do |
|---|---|
| `vdec_` connected | Call `decision_tradeoff_matrix` with the arguments in `references/tools.md`. |
| `vdec_` absent | Follow the same steps by hand. Head the result **not tool-checked**. Do not invent a tool field. |

Navigator tools, when this skill names them, use `vont_` on `vital-ontology-navigator`. Verify tools use `vvfy_` on `vital-verify`. Those calls are not simulated here.

## Steps

1. Ask for the criteria before any rating. If ratings come first, stop and ask for the criteria.
2. Ask for weights in the person's words, before rating. Offer swing weighting: imagine each criterion moving from worst to best; which swing matters most? Give it 100 and the others a share of it.
3. Ask the person to declare the scale (for example 1 to 5, higher is better) and which criteria are costs (lower is better).
4. In a group, ask raters to score privately before any discussion, then share.
5. Call `decision_tradeoff_matrix` with `criteria: [{name, weight, direction}]` and `ratings: [{option, criterion, score, rater, authored_by}]`. Set rater and authored_by to the person's name on every rating, never empty: v0.1 accepts a rating with no author.
6. Read back the stored grid. Speak winner null. Do not average, total, or rank.

## Output

Match `assets/worksheet-output.md`. End with the one question, or the closing line when the governance file says so.
