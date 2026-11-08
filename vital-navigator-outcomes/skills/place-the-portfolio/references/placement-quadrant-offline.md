# Portfolio placement quadrant — offline path

Live connector tools for grid / portfolio_place remain a **tools-lane** item. Until those land, use:

1. Team enters option coordinates (value axis + delivery/feasibility axis) with source_ids.
2. Run `scripts/placement_check.py` on the JSON worksheet.
3. Surface the quadrant diagram in `design-decision-exhibits` type `portfolio_placement` only when series locked.
4. Assistant never moves a dot to make the story prettier.

Sensitivity of placement under weight swings: `run-weight-sensitivity` then re-check placement — do not auto-replot without team numbers.
