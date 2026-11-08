# Working worksheet: handoff-verify

Use for live facilitation, one prompt per turn. Leave a cell blank rather than invent; write `[GAP]` with who can close it. Evidence class: M measured, V validated, H hypothesis (assistant proposal), O owner statement. People enter every score, choice and attestation.

Check script: `scripts/verify_handoff_check.py`. Field names in the right-hand column are the JSON keys the script reads.

## Packet

| Prompt | Answer | Class (M/V/H/O) | Source id / date or [GAP] | JSON field |
|---|---|---|---|---|
| Pack owner, named | | | | `owner` |
| Verify status: verified, not tool-checked, or claims_removed | | | | `verify_status` |
| Circulation: internal_only, external_blocked, external_ok | | | | `circulation` |

## Roles (VERIFY-04)

| Prompt | Answer | Class (M/V/H/O) | Source id / date or [GAP] | JSON field |
|---|---|---|---|---|
| Who wrote the claims? (name or role) | | | | `author_role` or `preparer` |
| Who assures them, and are they a different person? | | | | `assurance_role` or `assurer` |

## Claim list and binding (VERIFY-06), one block per claim

| Prompt | Answer | Class (M/V/H/O) | Source id / date or [GAP] | JSON field |
|---|---|---|---|---|
| Claim id and text | | | | `claims[].id`, `.text` |
| Was it tool-checked? (yes / no) | | | | `claims[].tool_checked` |
| Source and its version or date | | | | `claims[].source_revision` |
| The passage checked against, quoted from the supplied source | | | | `claims[].passage` |

## Renewal (VERIFY-05)

| Prompt | Answer | Class (M/V/H/O) | Source id / date or [GAP] | JSON field |
|---|---|---|---|---|
| Revision assured, and the current revision | | | | `assured_revision`, `current_revision` |

## Limits (by hand)

| Prompt | Answer | Class (M/V/H/O) | Source id / date or [GAP] | JSON field |
|---|---|---|---|---|
| What did this assurance not cover? State it for the cover note | | | | hand check |

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
