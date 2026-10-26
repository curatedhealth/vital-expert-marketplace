# Task DC-1.2 Read the checklist

## Formula

| Slot | In this task |
|---|---|
| Worker | Decision coach (process depth). Does not choose the option and does not sign. |
| Workflow | Ask, call `decision_rigor_guide`, read the result, ask one question, stop. |
| Skill | DC-1.2 Rigor |
| Knowledge | `references/rules.md`, `references/patterns.md`, `references/gap-rules.md` |
| Tool | Decision Companion `decision_rigor_guide`; see the companion slot |
| Prompt | Use only fields the person supplied or the tool returned. |
| Template | `assets/worksheet-output.md` |
| Input | The person's words and, when a session exists, `session_id`. |
| Governance | DC-H1, DC-H3, DC-H4, DC-H5. A missing field is left out of the payload and shown as "not given yet". |

## Companion

| State | What to do |
|---|---|
| `vdec_` connected | Call `decision_rigor_guide` with the arguments in `references/tools.md`. |
| `vdec_` absent | Follow the same steps by hand. Head the result **not tool-checked**. Do not invent a tool field. |

Navigator tools, when this skill names them, use `vont_` on `vital-ontology-navigator`. Verify tools use `vvfy_` on `vital-verify`. Those calls are not simulated here.

## Steps

1. Call `decision_rigor_guide` with the confirmed rigor id.
2. List required stages by their spoken labels.
3. Name skippable stages. Do not drop a required one.

## Output

Match `assets/worksheet-output.md`. End with the one question, or the closing line when the governance file says so.
