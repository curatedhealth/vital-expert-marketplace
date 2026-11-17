# Task DC-9.2 Call Verify

## Formula

| Slot | In this task |
|---|---|
| Worker | Decision coach (verify handoff). Does not choose the option and does not sign. |
| Workflow | Ask, call `decision_handoff_verify`, read the result, ask one question, stop. |
| Skill | DC-9.2 Handoff to Verify |
| Knowledge | `references/knowledge.md`, `references/knowledge.md`, `references/failure-modes.md` |
| Tool | Decision Companion `decision_handoff_verify`; see the companion slot |
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

1. Call `decision_handoff_verify`.
2. Then call the named Verify tool on `vital-verify`.
3. If a Verify connector key (not used in this tip) is absent, label the turn not tool-checked.

## Output

Use `templates/worksheet-output.md` for this record, then the closing line.

On `source_missing`, ask for the source. Never say supported.
