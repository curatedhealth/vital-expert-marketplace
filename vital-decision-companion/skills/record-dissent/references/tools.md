# Tool calls

## Companion slot

`decision_attach_notes` is available when Decision Companion is connected with a `vdec_` key. Without it, run the task by hand and label the turn not tool-checked (DC-H4).

## decision_attach_notes

Arguments: session_id, stage make_decision, notes ("Dissent — holder: <name>. <words>" or "No dissent — attested by <name>"), source participant or owner.

Returns: stored_length and draft. The note is stored on the stage and is not a choice.

Pitfall: Writing dissent with source draft marks it as AI-drafted. Use participant for a holder's own words.

A call the skill must refuse returns `gaps` whose text starts with `refused:`. The rejected field is not stored.

In the governed Navigator record, dissent is written with `decide_record_dissent` on `vital-ontology-navigator` with a `vont_` key and a person_name. Decision Companion does not call it.

Schema source: `mcps/decision_companion/tools.py`, content pack `2026-10-24.1`.

## Also named

- `decide_record_dissent`

These tools stay on their own connector. This skill does not reimplement them.
