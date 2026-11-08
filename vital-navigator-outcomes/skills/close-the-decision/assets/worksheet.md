# Working worksheet: close-the-decision

Use for live facilitation, one prompt per turn. Leave a cell blank rather than invent; write `[GAP]` with who can close it. Evidence class: M measured, V validated, H hypothesis (assistant proposal), O owner statement. People enter every score, choice and attestation.

Check script: `scripts/record_check.py`. Field names in the right-hand column are the JSON keys the script reads.

## Dissent carried in (CLOSE-01)

| Prompt | Answer | Class (M/V/H/O) | Source id / date or [GAP] | JSON field |
|---|---|---|---|---|
| Was dissent recorded earlier in this decision? (yes / no) | | | | `prior_dissent_present` |
| List each earlier dissent: id, holder's name, one-line text | | | | `prior_dissent_ids`; section 8 entries |
| If there is truly none: who attests, by name? | | | | `none_attested_by` (only when no earlier dissent) |

## Reopen conditions (CLOSE-02)

| Prompt | Answer | Class (M/V/H/O) | Source id / date or [GAP] | JSON field |
|---|---|---|---|---|
| Does this decision need explicit reopen conditions? (yes / no) | | | | `requires_reopen_conditions` |
| What observed change, date or trigger reopens it? One per line | | | | `reopen_conditions` |

## Assumptions and lifespan (CLOSE-03)

| Prompt | Answer | Class (M/V/H/O) | Source id / date or [GAP] | JSON field |
|---|---|---|---|---|
| Assumption text and named owner | | | | section 7 `assumptions[].text`, `.owner` |
| Date after which it may no longer hold (ISO) | | | | `expires_on` |
| Date a named person reviews it, no later than expiry | | | | `review_by` |

## Human close (CLOSE-04, CLOSE-05)

| Prompt | Answer | Class (M/V/H/O) | Source id / date or [GAP] | JSON field |
|---|---|---|---|---|
| Result, exactly one of the three; who chose it? | | | | section 6 `result`, `chosen_by` |
| Two named signers, one is the decision owner | | | | `signers` |

## Integrity link (PACK-03 close link)

| Prompt | Answer | Class (M/V/H/O) | Source id / date or [GAP] | JSON field |
|---|---|---|---|---|
| Revision ids from the board pack: ground, cut, verify (or verify_fallback), frame | | | | `integrity_revisions` |

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
