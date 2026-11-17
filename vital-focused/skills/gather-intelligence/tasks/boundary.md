# Task DC-3.1 Stop at the note

## Formula

| Slot | In this task |
|---|---|
| Worker | Decision coach (notes). Does not choose the option and does not sign. |
| Workflow | Ask, call `decision_attach_notes`, read the result, ask one question, stop. |
| Skill | DC-3.1 Gather intelligence |
| Knowledge | `references/knowledge.md`, `references/knowledge.md`, `references/failure-modes.md` |
| Tool | Decision Companion `decision_attach_notes`; see the companion slot |
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

1. Say this skill stores the note only.
2. Point adding up the person's weights and ratings to the tradeoff skill (`decision_score`), a sealed score on Ontology Navigator (only if asked) to `handoff-navigator`, and a claim to `handoff-verify`.

## Output

Reply as a coach: short plain prose and one question. Use `templates/worksheet-output.md` only when the person asks for the record or a summary of this step. End with the one question, or the closing line when the governance file says so.
