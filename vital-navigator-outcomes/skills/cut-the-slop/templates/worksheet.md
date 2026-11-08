# Working worksheet: cut-the-slop

Use for live facilitation, one prompt per turn. Leave a cell blank rather than invent; write `[GAP]` with who can close it. Evidence class: M measured, V validated, H hypothesis (assistant proposal), O owner statement. People enter every score, choice and attestation.

Check script: `scripts/substance_check.py`. Field names in the right-hand column are the JSON keys the script reads.

## Reader and need (SUB-01, by hand)

| Prompt | Answer | Class (M/V/H/O) | Source id / date or [GAP] | JSON field |
|---|---|---|---|---|
| Who reads this, and what do they need to decide or do? | | | | hand check |
| Which sentences serve that need, and which do not? | | | | edit log |

## Before and after

| Prompt | Answer | Class (M/V/H/O) | Source id / date or [GAP] | JSON field |
|---|---|---|---|---|
| Paste the original text | | | | `before` |
| Paste the tightened text | | | | `after` |
| Word counts before and after | | | | script output |

## Who acts (SUB-02)

| Prompt | Answer | Class (M/V/H/O) | Source id / date or [GAP] | JSON field |
|---|---|---|---|---|
| Which sentences now name an actor? Where did each name come from? | | | | `attributed_names` |
| Any actor named in the rewrite but not in the original? | | | | must be empty or attributed |

## What must survive (SUB-03)

| Prompt | Answer | Class (M/V/H/O) | Source id / date or [GAP] | JSON field |
|---|---|---|---|---|
| List every qualifier, limit or dissent in the original | | | | check against `after` |
| Any number in the rewrite that was not in the original? Its source | | | | `new_numbers_allowed` |
| Remaining numbers: so what, and what action for whom? | | | | `so_what[].line`, `.owner_action` |

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
