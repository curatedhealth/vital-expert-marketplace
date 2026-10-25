# Tool calls

## Companion slot

`decision_handoff_verify` is available when Decision Companion is connected with a `vdec_` key. Without it, run the task by hand and label the turn not tool-checked (DC-H4).

## decision_handoff_verify

Arguments: session_id, claims list. Verify tools keep their own arguments.

Returns: handoff.product verify, key_prefix vvfy_, next_tools qualify_source and check_claim, called_verify false.

Pitfall: Writing "supported" because the note sounds right bypasses check_claim.

A call the skill must refuse returns `gaps` whose text starts with `refused:`. The rejected field is not stored.

Schema source: `mcps/decision_companion/tools.py`, content pack `2026-10-24.1`.

## Also named

- `qualify_source`
- `check_claim`

These tools stay on their own connector. This skill does not reimplement them.
