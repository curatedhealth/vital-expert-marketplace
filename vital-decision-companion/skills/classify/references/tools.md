# Tool calls

## Companion slot

`decision_classify` is available when Decision Companion is connected with a `vdec_` key. Without it, run the task by hand and label the turn not tool-checked (DC-H4).

## decision_classify

Arguments: statement (required), optional session_id.

Returns: decision_type, recommended_rigor, rationale, draft true, gaps, next_stage how_to_decide.

Pitfall: Storing rigor before the person confirms writes a draft over their process.

A call the skill must refuse returns `gaps` whose text starts with `refused:`. The rejected field is not stored.

Schema source: `mcps/decision_companion/tools.py`, content pack `2026-10-24.1`.

## Also named

- `decision_run_stage`

These tools stay on their own connector. This skill does not reimplement them.
