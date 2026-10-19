# Decide support

## Formula

| Slot | In this task |
|---|---|
| Worker | Claim checker. Does not search and does not sign. |
| Workflow | Admit the source, compare the quoted passage, choose one status, then print the faithfulness line only after every finding. |
| Skill | Support decision. Register code is [GAP]. |
| Knowledge | Status table in [references/statuses.md](../references/statuses.md), from check_claim behavior in mcps/verify as of 19 October 2026. |
| Tool | `check_claim` with the claim, the source id, and the quoted passage. `verify_text` only for a first pass on text the person already supplied with its sources. |
| Prompt | Decide this passage only. Name the unsupported part when the status is partial. |
| Template | [assets/decide-support-output.md](../assets/decide-support-output.md) |
| Input | One claim, one already graded source, one quoted passage. |
| Governance | Inadmissible or an empty passage is unverifiable. Do not replace the sentence with a guess. |

## Steps

1. Confirm the tier from source grading. If it is inadmissible, or the passage is empty, status is unverifiable and the reason is "No admissible source was available."
2. If the tier is bronze, status is partial and the rationale is "source tier bronze." Do not ask the scorer to upgrade it.
3. For gold or silver, call `check_claim` when a key is present. Otherwise apply the table and mark the decision manual.
4. If the scorer says supported on anything other than gold or silver, demote it to partial.
5. Map the result onto a gap class in the gap rules.
6. After the reference list, print one faithfulness line: (supported + 0.5 times partial) divided by (supported + partial + unsupported + contradicted + unverifiable), as a whole percent. Leave out of scope out of the denominator.

## Checks

- The rationale quotes the deciding words.
- Partial names the part the passage does not state.
- The faithfulness line is not labelled as the source score.

## Boundaries

A list that merely contains an item does not show that the item is the newest or the required one, unless the passage says so. Word overlap can still mark the weaker sentence supported. Say that limit on the card.
