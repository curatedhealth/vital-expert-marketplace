# Working worksheet: compile-board-pack

Use for live facilitation, one prompt per turn. Leave a cell blank rather than invent; write `[GAP]` with who can close it. Evidence class: M measured, V validated, H hypothesis (assistant proposal), O owner statement. People enter every score, choice and attestation.

Check script: `scripts/board_pack_check.py`. Field names in the right-hand column are the JSON keys the script reads.

## Pack

| Prompt | Answer | Class (M/V/H/O) | Source id / date or [GAP] | JSON field |
|---|---|---|---|---|
| Pack owner, named | | | | `owner` |
| Are the eight client sections (or mapped 10 parts) complete? (yes / list gaps) | | | | `record_parts_complete` |
| Close vocabulary the owner chose, if any | | | | `close_vocabulary` |

## Integrity revisions (PACK-03)

| Prompt | Answer | Class (M/V/H/O) | Source id / date or [GAP] | JSON field |
|---|---|---|---|---|
| Revision id of the grounding pass | | | | `integrity_revisions.ground` |
| Revision id of the cut-the-slop pass | | | | `integrity_revisions.cut` |
| Revision id of Verify, or of the not-tool-checked fallback | | | | `integrity_revisions.verify` or `.verify_fallback` |
| Revision id of the exhibit framing pass | | | | `integrity_revisions.frame` |
| Latest material edit: revision id | | | | `last_material_edit_rev` |

## Exhibits

| Prompt | Answer | Class (M/V/H/O) | Source id / date or [GAP] | JSON field |
|---|---|---|---|---|
| Exhibit id, type and whether the owner locked it | | | | `exhibits[].id`, `.type`, `.locked` |

## Prior challenge (PACK-01)

| Prompt | Answer | Class (M/V/H/O) | Source id / date or [GAP] | JSON field |
|---|---|---|---|---|
| Challenge ids raised earlier | | | | `prior_challenges` |
| Which of them are visible in this pack? | | | | `pack_challenges` |

## Approval (PACK-04)

| Prompt | Answer | Class (M/V/H/O) | Source id / date or [GAP] | JSON field |
|---|---|---|---|---|
| Is a seal requested? Who, by name, approves? | | | | `seal_requested`, `approved_by` |

## Evidence behind each gate (PACK-02, by hand)

| Prompt | Answer | Class (M/V/H/O) | Source id / date or [GAP] | JSON field |
|---|---|---|---|---|
| For each gate marked complete: where is the evidence? | | | | hand check; no script |

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
