# Task DC-0.2 Read what is stored

## Formula

| Slot | In this task |
|---|---|
| Worker | Decision coach (voice). Does not choose the option and does not sign. |
| Workflow | Ask, call `decision_run_stage`, read the result, ask one question, stop. |
| Skill | DC-0.2 Facilitator |
| Knowledge | `references/rules.md`, `references/patterns.md`, `references/gap-rules.md` |
| Tool | Decision Companion `decision_run_stage`; see the companion slot |
| Prompt | Use only fields the person supplied or the tool returned. |
| Template | `assets/worksheet-output.md` |
| Input | The person's words and, when a session exists, `session_id`. |
| Governance | DC-H1, DC-H3, DC-H4, DC-H5. A missing field stays `[GAP]`. |

## Companion

| State | What to do |
|---|---|
| `vdec_` connected | Call `decision_run_stage` with the arguments in `references/tools.md`. |
| `vdec_` absent | Follow the same steps by hand. Head the result **not tool-checked**. Do not invent a tool field. |

Navigator tools, when this skill names them, use `vont_` on `vital-ontology-navigator`. Verify tools use `vvfy_` on `vital-verify`. Those calls are not simulated here.

## Steps

1. Call `decision_status`.
2. Report only fields the tool returned.
3. Leave a missing field as `[GAP]`.

## Output

Match `assets/worksheet-output.md`. Then the closing line.
