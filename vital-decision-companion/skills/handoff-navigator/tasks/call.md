# Task DC-9.1 Call Navigator

## Formula

| Slot | In this task |
|---|---|
| Worker | Decision coach (navigator handoff). Does not choose the option and does not sign. |
| Workflow | Ask, call `decision_handoff_navigator`, read the result, ask one question, stop. |
| Skill | DC-9.1 Handoff to Navigator |
| Knowledge | `references/rules.md`, `references/patterns.md`, `references/gap-rules.md` |
| Tool | Decision Companion `decision_handoff_navigator`; see the companion slot |
| Prompt | Use only fields the person supplied or the tool returned. |
| Template | `assets/worksheet-output.md` |
| Input | The person's words and, when a session exists, `session_id`. |
| Governance | DC-H1, DC-H3, DC-H4, DC-H5. A missing field stays `[GAP]`. |

## Companion

| State | What to do |
|---|---|
| `vdec_` connected | Call `decision_handoff_navigator` with the arguments in `references/tools.md`. |
| `vdec_` absent | Follow the same steps by hand. Head the result **not tool-checked**. Do not invent a tool field. |

Navigator tools, when this skill names them, use `vont_` on `vital-ontology-navigator`. Verify tools use `vvfy_` on `vital-verify`. Those calls are not simulated here.

## Steps

1. Call `decision_handoff_navigator`.
2. Then call the named Navigator tool on `vital-ontology-navigator`.
3. If `vont_` is absent, label the turn not tool-checked.

## Output

Match `assets/worksheet-output.md`. Then the closing line.
