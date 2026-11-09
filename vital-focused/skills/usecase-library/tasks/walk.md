# Task DC-8.1 Walk one gold card

## Formula

| Slot | In this task |
|---|---|
| Worker | Decision coach (examples). Does not choose the option and does not sign. |
| Workflow | Ask, call `decision_usecase_card`, read the result, ask one question, stop. |
| Skill | DC-8.1 Use-case library |
| Knowledge | `references/knowledge.md`, `references/knowledge.md`, `references/failure-modes.md` |
| Tool | Decision Companion `decision_usecase_card`; see the companion slot |
| Prompt | Use only fields the person supplied or the tool returned. |
| Template | `templates/worksheet-output.md` |
| Input | The person's words and, when a session exists, `session_id`. |
| Governance | DC-H1, DC-H3, DC-H4, DC-H5. A missing field is left out of the payload and shown as "not given yet". |

## Companion

| State | What to do |
|---|---|
| `vdec_` connected | Call `decision_usecase_card` with the arguments in `references/tools.md`. |
| `vdec_` absent | Follow the same steps with the plugin's local tools, or by hand when they cannot run. Do not label the reply. Do not invent a tool field. |

Navigator tools, when this skill names them, use `vont_` on `vital-ontology-navigator`. Verify tools use `vvfy_` on `vital-verify`. Those calls are not simulated here.

## Steps

1. With a key, call `decision_usecase_card` with that id. Without a key, prefer `references/cards/uc01.md`, `uc02.md` or `uc05.md` when the id matches; otherwise walk the closest case in `references/teaching-cases.md`: say it is a fictional teaching example, walk all seven steps in plain words (one line each), and end with one question: whether they want to walk their own decision.
2. Walk the beats. Label the card as teaching material.
3. Do not copy its choice onto the person's session.

## Output

Reply as a coach: short plain prose and one question. Use `templates/worksheet-output.md` only when the person asks for the record or a summary of this step. End with the one question, or the closing line when the governance file says so.
