# Task DC-1.1 Draft the type

## Formula

| Slot | In this task |
|---|---|
| Worker | Decision coach (type draft). Does not choose the option and does not sign. |
| Workflow | Ask, call `decision_classify`, read the result, ask one question, stop. |
| Skill | DC-1.1 Classify |
| Knowledge | `references/knowledge.md`, `references/knowledge.md`, `references/failure-modes.md` |
| Tool | Decision Companion `decision_classify`; see the companion slot |
| Prompt | Use only fields the person supplied or the tool returned. |
| Template | `templates/worksheet-output.md` |
| Input | The person's words and, when a session exists, `session_id`. |
| Governance | DC-H1, DC-H3, DC-H4, DC-H5. A missing field is left out of the payload and shown as "not given yet". |

## Companion

| State | What to do |
|---|---|
| `vdec_` connected | Call `decision_classify` with the arguments in `references/tools.md`. |
| `vdec_` absent | Follow the same steps with the plugin's local tools, or by hand when they cannot run. Do not label the reply. Do not invent a tool field. |

Navigator tools, when this skill names them, use `vont_` on `vital-ontology-navigator`. Verify tools use `vvfy_` on `vital-verify`. Those calls are not simulated here.

## Steps

1. Read the statement.
2. Call `decision_classify` without `confirmed`.
3. Read the draft back in one sentence and wait.

## Output

Reply as a coach: short plain prose and one question. Use `templates/worksheet-output.md` only when the person asks for the record or a summary of this step. End with the one question, or the closing line when the governance file says so.
