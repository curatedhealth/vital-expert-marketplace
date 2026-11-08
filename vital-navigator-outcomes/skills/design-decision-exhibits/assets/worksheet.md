# Working worksheet: design-decision-exhibits

Use for live facilitation, one prompt per turn. Leave a cell blank rather than invent; write `[GAP]` with who can close it. Evidence class: M measured, V validated, H hypothesis (assistant proposal), O owner statement. People enter every score, choice and attestation.

Check script: `scripts/exhibit_check.py`. Field names in the right-hand column are the JSON keys the script reads.

## Question (EXH-01)

| Prompt | Answer | Class (M/V/H/O) | Source id / date or [GAP] | JSON field |
|---|---|---|---|---|
| Which decision does this exhibit inform, and who decides it? | | | | `title`, `owner` |
| State the one question the exhibit lets a reader answer | | | | `question` |
| Could the reader answer it without the chart? If yes, say so and stop | | | | withhold or keep text |

## Series and sources (EXH-02)

| Prompt | Answer | Class (M/V/H/O) | Source id / date or [GAP] | JSON field |
|---|---|---|---|---|
| For each series: name | | | | `series[].name` |
| Supplied source id or record (team score sheet, log, study) | | | | `series[].source_id` |
| Value as supplied; leave blank if none | | | | `series[].value` |

## Type and baseline

| Prompt | Answer | Class (M/V/H/O) | Source id / date or [GAP] | JSON field |
|---|---|---|---|---|
| Which of the five exhibit types fits the question? | | | | `exhibit_type` |
| Waterfall only: is a baseline required, and is it present? | | | | `baseline_required`, `baseline_present` |

## Lock

| Prompt | Answer | Class (M/V/H/O) | Source id / date or [GAP] | JSON field |
|---|---|---|---|---|
| Owner reviewed and locks? (yes / no) | | | | `locked` |

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
