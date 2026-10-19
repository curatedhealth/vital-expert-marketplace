# Gap rules

A gap is information. Each reason for a gap leads to a different next step, so name the reason.

## Public signals (library)

| Situation | How to word it | Next step |
|---|---|---|
| `get_deltas` returns nothing | "No change events available from the library for this scope `[GAP]`; an empty feed is not evidence that nothing changed." | Compare two dated sequence runs |
| Market Access delta feed missing | "Market Access change feed not available (connector states it is not on the server) `[GAP]`." | Same |
| Only one sequence run exists | "Baseline recorded on DATE; changes can be read from the next run." | Save the run; repeat when the person asks |
| `changed_on` without status | "Changed on DATE (source); status after the change not stated `[GAP]`." | Check the authority's page |
| DiGA trial end | "Trial end date not stored in the library `[GAP]`; the rule allows up to twelve months (CP-DE-13)." | Check the BfArM directory entry |
| Peer not returned | "Not found under this name `[GAP]`; absence is not evidence the product is not listed." | Use the exact stored name |
| UK or Swiss records | "The library loads no UK device registrations and no Swiss records `[GAP]`." | Ask the person or the authority |

## The person's records

| Situation | How to word it |
|---|---|
| No threshold for a measure | Report the number; no verdict. Ask for the rule |
| No data for a measure | "Not measured `[GAP]`", and name the record that would hold it (CRM activity log, briefing log, claim-use log) |
| No approved claim list | "Unapproved claim use not measured: no approved list supplied" |
| Records described but not shown | "Described, not seen" |
| No owner for a miss | "Owner not named"; ask. Never suggest a job title |
| No scores for ranking repairs | No ranking; lay out the options and ask for the person's scores |

## Rule facts

| Class | How to word it |
|---|---|
| Sourced | The fact plus the row id |
| Moved rule | The date and the instrument that moved it (`references/launch-clocks.md`) |
| [INDUSTRY] or [WF] row | Say so when you apply it |
| Not in the research | "Not in this skill's sources `[GAP]`" |

## Never

- Never fill a count, threshold, owner, date or cause from memory or estimate.
- Never treat an empty change feed as "no change", or a missing record as "not listed".
- Never treat uptake as clinical evidence.
