# Tool calls

## Companion slot

`decision_usecase_card` is available when Decision Companion is connected with a `vdec_` key. Without it, run the task by hand and label the turn not tool-checked (DC-H4).

## decision_usecase_card

Arguments: usecase_id or query, optional session_id.

Returns: card with beats, or card null, gold_set, and a gap. leverage_packages for a found card.

Pitfall: Query matching is a substring of the card title. A vague query can miss. Prefer the id.

A call the skill must refuse returns `gaps` whose text starts with `refused:`. The rejected field is not stored.

Schema source: `mcps/decision_companion/tools.py`, content pack `2026-10-24.1`.

## Also named

- none

These tools stay on their own connector. This skill does not reimplement them.
