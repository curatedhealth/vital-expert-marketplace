# C Prepare Gate 3

Framework task: 6.2 Decision Record (route for named sign-off).

## What this task delivers

The record prepared for two named signers, one of them the decision owner, with its status ("prepared for signature" or "blocked" and why), and the instruction that signing happens in the Navigator app.

Why it matters: Gate 3 is critical. A record signed by one person, or by a role, or by an assistant, does not carry responsibility (method.md D5, D6).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | AI Investment Decision Lead |
| Skill | 6.2 |
| Knowledge | `references/method.md` (D5, D6) |
| Tools | `scripts/record_check.py`; `decide_prepare_signoff` |
| Template | `assets/signoff-sheet.md` |
| Input | The checked record |

## Workflow

1. **Ask who signs with the owner** (question 7): a named person whose role qualifies them (for example the head of the function that carries the risk). A role alone is a gap.
2. **Check** both signers with the script: two different named people, one the owner, neither an assistant.
3. **Prepare** with `decide_prepare_signoff` once per signer, if a brief is open; status "prepared for signature" or "blocked" with the reasons.
4. **Say where signing happens**: in the Navigator app, by each signer; this conversation never records a signature.
5. **Clearing a copy**: if the record will leave the organization, a named person clears it; with VITAL Verify, `build_record` with that person in `cleared_by`.

## Boundaries

- Never write "signed", "approved" or "final".
- A blocked record goes back to the section that blocks it, not around it.

## When you are unsure

If the owner wants to sign alone, say in one line that Gate 3 needs two named people, and ask who the second is.
