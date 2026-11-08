# Working worksheet: handoff-evidence-steward

Use for live facilitation, one prompt per turn. Leave a cell blank rather than invent; write `[GAP]` with who can close it. Evidence class: M measured, V validated, H hypothesis (assistant proposal), O owner statement. People enter every score, choice and attestation.

Check script: `scripts/steward_handoff_check.py`. Field names in the right-hand column are the JSON keys the script reads.

## Packet

| Prompt | Answer | Class (M/V/H/O) | Source id / date or [GAP] | JSON field |
|---|---|---|---|---|
| Proposal owner, named | | | | `owner` |
| Is the Curator store reachable? If not, who acknowledges the gap? | | | | `store_available`, `store_gap_acknowledged` |

## Item inventory (one block per item)

| Prompt | Answer | Class (M/V/H/O) | Source id / date or [GAP] | JSON field |
|---|---|---|---|---|
| Title and evidence class (M/V/H/O) | | | | `items[].title`, `.evidence_class` |
| Source as supplied, and its date | | | | `items[].source`, `.source_date` |
| Derived from: what record or step did it come from? | | | | `items[].derived_from` or `.lineage` |
| Responsible party: named person or team | | | | `items[].responsible_party` |
| Exact version or date (no 'latest') | | | | `items[].version` |

## Rights

| Prompt | Answer | Class (M/V/H/O) | Source id / date or [GAP] | JSON field |
|---|---|---|---|---|
| Is reuse cleared? If yes, on what stated basis? Leave unknown if not | | | | `reuse_cleared`, `rights_basis` |

## No source

| Prompt | Answer | Class (M/V/H/O) | Source id / date or [GAP] | JSON field |
|---|---|---|---|---|
| Why is there no source? Who can supply one? | | | | `items[].gap` |

## Hold back

| Prompt | Answer | Class (M/V/H/O) | Source id / date or [GAP] | JSON field |
|---|---|---|---|---|
| Steward ids: leave blank; the steward assigns them | | | | `steward_id` stays null |

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
