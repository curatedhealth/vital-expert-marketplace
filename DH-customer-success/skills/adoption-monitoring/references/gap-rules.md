# Gap rules

A gap is information. Each reason for a gap leads to a different next step, so name the reason.

## Definition and method facts

| Class | When | How to word it | Next step |
|---|---|---|---|
| Sourced | A research row states it. | The definition plus the row id (for example "penetration: providers who deliver divided by providers trained in or expected to deliver, CS39"). | None. |
| Two definitions | Proctor and RE-AIM both define the metric (adoption; penetration and reach; sustainability and maintenance). | Name the one used and the row; mention the other once. | Ask the person which they want if it matters for a contract. |
| Abstract only | RE-AIM 1999 (CS21) was read from its abstract; definitions come from re-aim.org. | "From re-aim.org (CS22 to CS30); the 1999 full text was not read." | None. |
| No threshold | Any target share, window, penetration or frequency. | "No source in this skill sets a target `[GAP]`; the rule is yours." | Ask the person. |
| Not sourced | Customer health score, renewal, churn, expansion, NPS. | "Not sourced; your definition and formula, labeled owner-stated." | Ask the person. |

## The person's data

| Situation | How to word it |
|---|---|
| No task card | Ask for the task in one line, or run the sibling skill's A1. Without it "adopted" has no meaning. |
| No eligible roster | Penetration among eligible cannot be computed: "eligible list not supplied `[GAP]`". Adoption among trained may still be computed if training dates exist. |
| No training dates | Adoption among trained and window adoption cannot be computed `[GAP]`; penetration may be. |
| Usage events before the training date | Reported by the script as a data check; not counted toward adoption. Ask the person. |
| Usage for users not on the roster | Excluded and listed; ask the person. |
| Window not elapsed | Counted separately, never as a miss. |
| No rule set | Report the numbers; "no rule set"; no verdict. Ask for the rule. |
| No owner named | Use the owner or role the person names, in their words. Only if they named none, write "owner not named" and ask. Never suggest a job title. |
| No scores for B1 | No ranking. Lay out the facts per option and ask the person to score. |
| Old step not logged | "Old step not measured `[GAP]`"; name the record that would hold it (for example the paper log count, the old system's access log). |

## Library facts

| Situation | How to word it |
|---|---|
| `check_claim` "supported" | Accept only after reading the passage and confirming the same direction, numerator and denominator (register N3). |
| `check_claim` "unverifiable" with `source {doi}` | Re-run with `source {source_id, tier, source_type, code}` (`tools.md`). |
| Library 503 | "The library could not answer; nothing was counted." Retry once, then cite the row. |

## Never

- Never fill a threshold, a window, a share, an owner or a score from memory.
- Never treat a missing usage record as non-use without saying the log may be incomplete.
- Never treat high adoption as evidence that the product works clinically.
