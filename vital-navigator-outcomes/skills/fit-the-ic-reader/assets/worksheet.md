# Working worksheet: fit-the-ic-reader

Use for live facilitation, one prompt per turn. Leave a cell blank rather than invent; write `[GAP]` with who can close it. Evidence class: M measured, V validated, H hypothesis (assistant proposal), O owner statement. People enter every score, choice and attestation.

Check script: `scripts/reader_fit_check.py`. Field names in the right-hand column are the JSON keys the script reads.

## Reader and decision

| Prompt | Answer | Class (M/V/H/O) | Source id / date or [GAP] | JSON field |
|---|---|---|---|---|
| Who reads this: IC, board, ELT, other? | | | | `reader` |
| State the decision in one sentence, with the owner's name | | | | `one_pager.decision`, `owner` |

## What the reader must do (READER-01)

| Prompt | Answer | Class (M/V/H/O) | Source id / date or [GAP] | JSON field |
|---|---|---|---|---|
| In one sentence: what must this reader do after reading? | | | | `one_pager.must_do` |
| Which ask type: Endorse, Mandate, Supply or Hold? Request and who | | | | `asks[].type`, `.request`, `.who` |

## Options and value

| Prompt | Answer | Class (M/V/H/O) | Source id / date or [GAP] | JSON field |
|---|---|---|---|---|
| Options on the page, including do nothing or internal | | | | `options` |
| Value at stake in words, and its evidence class (M/V/H/O or GAP) | | | | `value_at_stake.text`, `.evidence_class` |
| What does the decision turn on? | | | | `turns_on` |

## Integrity posture and limits (READER-02, by hand)

| Prompt | Answer | Class (M/V/H/O) | Source id / date or [GAP] | JSON field |
|---|---|---|---|---|
| verified or not tool-checked? | | | | `integrity_posture` |
| List each material limit or dissent in the working file; is it on the page? | | | | hand check; no script |

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
