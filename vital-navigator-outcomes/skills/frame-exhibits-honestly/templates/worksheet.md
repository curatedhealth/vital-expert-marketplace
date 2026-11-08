# Working worksheet: frame-exhibits-honestly

Use for live facilitation, one prompt per turn. Leave a cell blank rather than invent; write `[GAP]` with who can close it. Evidence class: M measured, V validated, H hypothesis (assistant proposal), O owner statement. People enter every score, choice and attestation.

Check script: `scripts/chart_scale.py`. Field names in the right-hand column are the JSON keys the script reads.

## Chart and axis (CHART-01)

| Prompt | Answer | Class (M/V/H/O) | Source id / date or [GAP] | JSON field |
|---|---|---|---|---|
| What chart kind: bar, line, waterfall, tornado, other? | | | | `chart_kind` |
| Axis minimum and maximum as drawn; why not zero if bar/waterfall/area? | | | | `axis_min`, `axis_max`, `axis_min_justified` |
| Largest value in the series; does the axis maximum cover it? | | | | `series[].value` vs `axis_max` |

## Panels (CHART-02)

| Prompt | Answer | Class (M/V/H/O) | Source id / date or [GAP] | JSON field |
|---|---|---|---|---|
| Will a reader compare panels? If yes, list each panel's axis_min and axis_max | | | | `panels`, `panels_comparable` |
| If scales differ, why? | | | | `scale_justification` |

## Uncertainty (CHART-03)

| Prompt | Answer | Class (M/V/H/O) | Source id / date or [GAP] | JSON field |
|---|---|---|---|---|
| Did the team supply an interval? Low, high and how it was computed | | | | `ci_low`, `ci_high`, `interval_basis` |
| Are any bounds scenarios rather than a statistical interval? | | | | `interval_kind`, `interval_label` |

## Absolute and comparison context (CHART-04, CHART-05)

| Prompt | Answer | Class (M/V/H/O) | Source id / date or [GAP] | JSON field |
|---|---|---|---|---|
| Is a relative change shown? Give the absolute change beside it | | | | `relative_effect`, `absolute_effect` |
| Is one thing compared with another? Denominator and period | | | | `comparison`, `denominator`, `period` |

## Title and withhold

| Prompt | Answer | Class (M/V/H/O) | Source id / date or [GAP] | JSON field |
|---|---|---|---|---|
| Does the title claim a cause the data do not show? | | | | `causal_title` |
| If the exhibit cannot be drawn fairly, why withhold it? | | | | `withhold`, `withhold_reason` |

## Human gates this turn

| Gate | Options presented | Deciding role (named person) | Decision |
|---|---|---|---|
| | | | |

## Open [GAP]s and next step

| Open [GAP] | Who can close it | By when |
|---|---|---|
| | | |

Next skill or sibling handoff:  

Prepared by:  
Reviewed by:  
Version:  
Release state: Draft

Integrity path before seal: ground-the-numbers, cut-the-slop, handoff-verify (or explicit not-tool-checked), frame-exhibits-honestly, then compile-board-pack / close-the-decision. Human close only.
