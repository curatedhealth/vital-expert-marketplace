# Task DC-9.2 Build the packet

## Formula

| Slot | In this task |
|---|---|
| Worker | Decision coach (verify handoff). Does not choose the option and does not sign. |
| Workflow | Ask, call `decision_handoff_verify`, read the result, ask one question, stop. |
| Skill | DC-9.2 Handoff to Verify |
| Knowledge | `references/rules.md`, `references/patterns.md`, `references/gap-rules.md` |
| Tool | Decision Companion `decision_handoff_verify`; see the companion slot |
| Prompt | Use only fields the person supplied or the tool returned. |
| Template | `assets/worksheet-output.md` |
| Input | The person's words and, when a session exists, `session_id`. |
| Governance | DC-H1, DC-H3, DC-H4, DC-H5. A missing field is left out of the payload and shown as "not given yet". |

## Companion

| State | What to do |
|---|---|
| `vdec_` connected | Call `decision_handoff_verify` with the arguments in `references/tools.md`. |
| `vdec_` absent | Follow the same steps by hand. Head the result **not tool-checked**. Do not invent a tool field. |

Navigator tools, when this skill names them, use `vont_` on `vital-ontology-navigator`. Verify tools use `vvfy_` on `vital-verify`. Those calls are not simulated here.

## Steps

1. List the claim and the passage, or say the passage is missing.
2. Do not mark the claim supported.

## Output

Match `assets/worksheet-output.md`. Then the closing line.

On `source_missing`, ask for the source. Never say supported.
