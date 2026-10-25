# Task DC-2.1 Ask about a missing option

## Formula

| Slot | In this task |
|---|---|
| Worker | Decision coach (option list). Does not choose the option and does not sign. |
| Workflow | Ask, call `decision_widen_options`, read the result, ask one question, stop. |
| Skill | DC-2.1 Widen options |
| Knowledge | `references/rules.md`, `references/patterns.md`, `references/gap-rules.md` |
| Tool | Decision Companion `decision_widen_options`; see the companion slot |
| Prompt | Use only fields the person supplied or the tool returned. |
| Template | `assets/worksheet-output.md` |
| Input | The person's words and, when a session exists, `session_id`. |
| Governance | DC-H1, DC-H3, DC-H4, DC-H5. A missing field stays `[GAP]`. |

## Companion

| State | What to do |
|---|---|
| `vdec_` connected | Call `decision_widen_options` with the arguments in `references/tools.md`. |
| `vdec_` absent | Follow the same steps by hand. Head the result **not tool-checked**. Do not invent a tool field. |

Navigator tools, when this skill names them, use `vont_` on `vital-ontology-navigator`. Verify tools use `vvfy_` on `vital-verify`. Those calls are not simulated here.

## Steps

1. Read the warning aloud.
2. Ask the person to name the missing option.
3. Do not invent one to clear the warning.

## Output

Match `assets/worksheet-output.md`. Then the closing line.
