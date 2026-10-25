# Tool calls

## Companion slot

`decision_premortem` is available when Decision Companion is connected with a `vdec_` key. Without it, run the task by hand and label the turn not tool-checked (DC-H4).

## decision_premortem

Arguments: session_id, hypotheses as a list of objects the person described.

Returns: hypotheses as stored. No recommendation field.

Pitfall: Rewriting a blunt failure into a softer risk changes the person's words.

A call the skill must refuse returns `gaps` whose text starts with `refused:`. The rejected field is not stored.

Schema source: `mcps/decision_companion/tools.py`, content pack `2026-10-24.1`.

## Also named

- none

These tools stay on their own connector. This skill does not reimplement them.
