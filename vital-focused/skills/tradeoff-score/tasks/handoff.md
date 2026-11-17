# Task DC-4.6 Add up the stored weights and ratings

## Formula

| Slot | In this task |
|---|---|
| Worker | Decision coach (matrix). Does not choose the option and does not sign. |
| Workflow | Run the local scorer (or `decision_score` with a key), read back the totals and the robustness line, stop. |
| Skill | DC-4.6 Trade-off |
| Knowledge | `references/knowledge.md`, `references/knowledge.md`, `references/failure-modes.md` |
| Tool | Decision Companion `decision_score`; see the companion slot |
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

1. Do not add up or rank by hand; `decision_score` adds up the person's own weights and ratings.
2. Call `decision_score` for the person's own weights and ratings added up. Say the totals are their inputs added up and do not choose for them.
3. Only if the person asks for a sealed or governed score on Ontology Navigator, point to `handoff-navigator`.

## Output

Reply as a coach: short plain prose and one question. Use `templates/worksheet-output.md` only when the person asks for the record or a summary of this step. End with the one question, or the closing line when the governance file says so.
