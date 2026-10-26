# Task DC-7.1 Compile the draft

## Formula

| Slot | In this task |
|---|---|
| Worker | Decision coach (drafter). Does not choose the option and does not sign. |
| Workflow | Ask, call `decision_build_brief`, read the result, ask one question, stop. |
| Skill | DC-7.1 Brief |
| Knowledge | `references/rules.md`, `references/patterns.md`, `references/gap-rules.md` |
| Tool | Decision Companion `decision_build_brief`; see the companion slot |
| Prompt | Use only fields the person supplied or the tool returned. |
| Template | `assets/worksheet-output.md` |
| Input | The person's words and, when a session exists, `session_id`. |
| Governance | DC-H1, DC-H3, DC-H4, DC-H5. A missing field is left out of the payload and shown as "not given yet". |

## Companion

| State | What to do |
|---|---|
| `vdec_` connected | Call `decision_build_brief` with the arguments in `references/tools.md`. |
| `vdec_` absent | Follow the same steps by hand. Head the result **not tool-checked**. Do not invent a tool field. |

Navigator tools, when this skill names them, use `vont_` on `vital-ontology-navigator`. Verify tools use `vvfy_` on `vital-verify`. Those calls are not simulated here.

## Steps

1. Call `decision_build_brief`.
2. When reading the record back to the person, use `person_summary_markdown` if present (no watermark, no tool names); otherwise use `brief_markdown` and drop the watermark line and any tool or stage names. Copy only stored fields. Leave gaps visible as "not given yet". Do not sign.

## Output

Match `assets/worksheet-output.md`. Then the closing line.
