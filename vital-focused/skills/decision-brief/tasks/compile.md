# Task DC-7.1 Compile the draft

## Formula

| Slot | In this task |
|---|---|
| Worker | Decision coach (drafter). Does not choose the option and does not sign. |
| Workflow | Ask, call `decision_build_brief`, read the result, ask one question, stop. |
| Skill | DC-7.1 Brief |
| Knowledge | `references/knowledge.md`, `references/knowledge.md`, `references/failure-modes.md` |
| Tool | Decision Companion `decision_build_brief`; see the companion slot |
| Prompt | Use only fields the person supplied or the tool returned. |
| Template | `templates/worksheet-output.md` |
| Input | The person's words and, when a session exists, `session_id`. |
| Governance | DC-H1, DC-H3, DC-H4, DC-H5. A missing field is left out of the payload and shown as "not given yet". |

## Companion

| State | What to do |
|---|---|
| Offline (this tip) | Follow the method by hand using schemas and cards; label **not tool-checked**. Do not invent tool fields. |

This tip has no live Navigator or Verify connector; do not simulate tool results.

## Steps

1. Call `decision_build_brief`.
2. When reading the record back to the person, use `person_summary_markdown` if present (no watermark, no tool names); otherwise use `brief_markdown` and drop the watermark line and any tool or stage names. Copy only stored fields. Leave gaps visible as "not given yet". Do not sign.

## Output

Use `templates/worksheet-output.md` for this record, then the closing line.
