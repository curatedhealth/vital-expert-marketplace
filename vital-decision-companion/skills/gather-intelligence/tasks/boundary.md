# Task DC-3.1 Stop at the note

## Formula

| Slot | In this task |
|---|---|
| Worker | Decision coach (notes). Does not choose the option and does not sign. |
| Workflow | Ask, call `decision_attach_notes`, read the result, ask one question, stop. |
| Skill | DC-3.1 Gather intelligence |
| Knowledge | `references/rules.md`, `references/patterns.md`, `references/gap-rules.md` |
| Tool | Decision Companion `decision_attach_notes`; see the companion slot |
| Prompt | Use only fields the person supplied or the tool returned. |
| Template | `assets/worksheet-output.md` |
| Input | The person's words and, when a session exists, `session_id`. |
| Governance | DC-H1, DC-H3, DC-H4, DC-H5. A missing field is left out of the payload and shown as "not given yet". |

## Companion

| State | What to do |
|---|---|
| `vdec_` connected | Call `decision_attach_notes` with the arguments in `references/tools.md`. |
| `vdec_` absent | Follow the same steps by hand. Head the result **not tool-checked**. Do not invent a tool field. |

Navigator tools, when this skill names them, use `vont_` on `vital-ontology-navigator`. Verify tools use `vvfy_` on `vital-verify`. Those calls are not simulated here.

## Steps

1. Say this skill stores the note only.
2. Point a score to `handoff-navigator` and a claim to `handoff-verify`.

## Output

Match `assets/worksheet-output.md`. End with the one question, or the closing line when the governance file says so.
