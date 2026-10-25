# Task DC-4.6 Point a weighted rank elsewhere

## Formula

| Slot | In this task |
|---|---|
| Worker | Decision coach (matrix). Does not choose the option and does not sign. |
| Workflow | Do not compute; name the Navigator rank and the scale it needs, stop. |
| Skill | DC-4.6 Trade-off |
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

1. Do not compute a weighted total or a rank here.
2. Say the shared weighted rank is `methods_mcda_rank` on Ontology Navigator (vont_), which takes 0 to 4 scores. If the person's scale is different, they choose the mapping; handoff-navigator explains it.
3. Point to `handoff-navigator`.

## Output

Match `assets/worksheet-output.md`. End with the one question, or the closing line when the governance file says so.
