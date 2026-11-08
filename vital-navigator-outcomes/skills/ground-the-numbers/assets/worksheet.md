# Working worksheet: ground-the-numbers

Use for live facilitation, one prompt per turn. Leave a cell blank rather than invent; write `[GAP]` with who can close it. Evidence class: M measured, V validated, H hypothesis (assistant proposal), O owner statement. People enter every score, choice and attestation.

Check script: `scripts/grounding_check.py`. Field names in the right-hand column are the JSON keys the script reads.

## Claim inventory (one block per claim)

| Prompt | Answer | Class (M/V/H/O) | Source id / date or [GAP] | JSON field |
|---|---|---|---|---|
| Claim id and the sentence as drafted | | | | `claims[].id`, `.text` |
| Numbers in the claim, exactly as written | | | | `claims[].numbers` |
| Supplied source id, or blank if none | | | | `claims[].source_id` |
| Evidence class: M measured, V validated, H hypothesis, O owner estimate | | | | `claims[].evidence_class` |
| Action: keep, gap or remove | | | | `claims[].action` |

## Grounding (GROUND-01), required for keep

| Prompt | Answer | Class (M/V/H/O) | Source id / date or [GAP] | JSON field |
|---|---|---|---|---|
| Methods: how was the figure derived, by whom, when? | | | | `methods` |
| Data assumptions: population, period, scope, version of the data | | | | `data_assumptions` |
| Assumption note: what is taken as given, and what breaks if it is wrong? | | | | `assumption_note` |

## Relative and cash figures

| Prompt | Answer | Class (M/V/H/O) | Source id / date or [GAP] | JSON field |
|---|---|---|---|---|
| Relative change: is the absolute figure present? | | | | `relative`, `absolute_present` |
| Labeled cash: what is the realization action? | | | | `cashable`, `realization_action` |

## Repair

| Prompt | Answer | Class (M/V/H/O) | Source id / date or [GAP] | JSON field |
|---|---|---|---|---|
| If removed or gapped, what repair note will the owner see? | | | | `repair_note` |

## Warrant (by hand, GROUND-02 deferred)

| Prompt | Answer | Class (M/V/H/O) | Source id / date or [GAP] | JSON field |
|---|---|---|---|---|
| What links the evidence to the claim, and what would a skeptic say? | | | | hand check; no script |

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
