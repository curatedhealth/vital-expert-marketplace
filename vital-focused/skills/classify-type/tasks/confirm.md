# Task DC-1.2 Confirm the type

## Formula

| Slot | In this task |
|---|---|
| Worker | Decision coach (classifier). Does not choose the option and does not sign. |
| Workflow | Read the draft back, wait for a named person to confirm, store the confirmed type, stop. |
| Skill | DC-1.2 Classify |
| Knowledge | `references/knowledge.md`, `references/knowledge.md`, `references/failure-modes.md` |
| Tool | Decision Companion `decision_classify`; see the companion slot |
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

1. Read the draft type and rigor back in one sentence. Ask the person to confirm or correct it, and for their name.
2. If the name is missing, do not store. Ask for the name.
3. Prefer `decision_classify` with `confirmed: true` and `confirmed_by` when the host schema has those fields.
4. Otherwise use `decision_run_stage` on `how_to_decide` with `payload: {decision_type, type_confirmed_by}` (connector path that persists the type).
5. If both are unavailable, store an owner note via `decision_attach_notes`: "Type confirmed: <type> by <name>". Tell the person the bias card stays unfiltered until the type can be stored on the session.
6. Never claim the session type is set unless `decision_status.decision_type` shows it.

## Output

Reply as a coach: short plain prose and one question. Use `templates/worksheet-output.md` only when the person asks for the record or a summary of this step. End with the one question, or the closing line when the governance file says so.
