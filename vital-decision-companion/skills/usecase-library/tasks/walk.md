# Task DC-8.1 Walk one gold card

## Formula

| Slot | In this task |
|---|---|
| Worker | Decision coach (examples). Does not choose the option and does not sign. |
| Workflow | Ask, call `decision_usecase_card`, read the result, ask one question, stop. |
| Skill | DC-8.1 Use-case library |
| Knowledge | `references/rules.md`, `references/patterns.md`, `references/gap-rules.md` |
| Tool | Decision Companion `decision_usecase_card`; see the companion slot |
| Prompt | Use only fields the person supplied or the tool returned. |
| Template | `assets/worksheet-output.md` |
| Input | The person's words and, when a session exists, `session_id`. |
| Governance | DC-H1, DC-H3, DC-H4, DC-H5. A missing field stays `[GAP]`. |

## Companion

| State | What to do |
|---|---|
| `vdec_` connected | Call `decision_usecase_card` with the arguments in `references/tools.md`. |
| `vdec_` absent | Follow the same steps by hand. Head the result **not tool-checked**. Do not invent a tool field. |

Navigator tools, when this skill names them, use `vont_` on `vital-ontology-navigator`. Verify tools use `vvfy_` on `vital-verify`. Those calls are not simulated here.

## Steps

1. Call `decision_usecase_card` with that id.
2. Walk the beats. Label the card as teaching material.
3. Do not copy its choice onto the person's session.

## Output

Match `assets/worksheet-output.md`. End with the one question, or the closing line when the governance file says so.
