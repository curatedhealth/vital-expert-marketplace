# Task DC-9.1 Build the packet

## Formula

| Slot | In this task |
|---|---|
| Worker | Decision coach (navigator handoff). Does not choose the option and does not sign. |
| Workflow | Ask, call `decision_handoff_navigator`, read the result, ask one question, stop. |
| Skill | DC-9.1 Handoff to Navigator |
| Knowledge | `references/knowledge.md`, `references/knowledge.md`, `references/failure-modes.md` |
| Tool | Decision Companion `decision_handoff_navigator`; see the companion slot |
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

1. Read the stored matrix.
2. Build the packet. Speak Approach.
3. Do not compute a rank.

## Output

Use `templates/worksheet-output.md` for this record, then the closing line.
