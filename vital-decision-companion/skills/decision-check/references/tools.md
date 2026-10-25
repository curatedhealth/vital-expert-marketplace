# Tool calls

## Companion slot

`decision_status` is available when Decision Companion is connected with a `vdec_` key. Without it, run the task by hand and label the turn not tool-checked (DC-H4).

## decision_status

Arguments: session_id.

Returns: stages with complete and gaps, open_stage, rigor, decision_type, daii_filled, leverage, persistence.

Pitfall: daii_filled true does not prove the decider is a person in v0.1. Check the stored name yourself.

A call the skill must refuse returns `gaps` whose text starts with `refused:`. The rejected field is not stored.

Schema source: `mcps/decision_companion/tools.py`, content pack `2026-10-24.1`.

## Also named

- `decision_build_brief`
- `decision_rigor_guide`

These tools stay on their own connector. This skill does not reimplement them.
