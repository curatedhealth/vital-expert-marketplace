# Output format: renewal horizon

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words and write 'Words: N' as the first line of the Calls made list. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap. State each fact once. Open questions: at most three. One line per item; a rule column holds the row ids and at most fifteen words.

## Short mode (default for a direct question)

Budget: answer 50, table 150, points 100, check 30, record 40. The format itself fits under 450 words; do not add sections.

1. **Answer** (at most 50 words): how many renewals fall inside your window (as-of date and end date in full), which are ready on your rule, and the nearest renewal date.
2. **Renewals** (one table row per account in the window): Account · Contract · Renewal date · Days · Readiness (your rule) · Fact behind it. If you stated no rule, drop the readiness column and ask for the rule once.
3. **Points the renewals must cover** (one line each, only points tied to an account in the window and its market, with row ids): others go in one line offering the full version.
4. **Check the record** (one line): open accounts whose renewal date has passed.
5. **Record:** Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
6. One line offering the full version.

**Refusal (any task, same cap):** (1) what is declined and why, one line with the rows; (2) the elements or figures behind it, one line each, at most five; (3) "Draft for the owner", at most 120 words, holding only facts the person stated and figures from the run, never a commitment they did not make; (4) the record line.

## Full mode

### Answer

### Window
As-of date · Horizon (days, yours) · Window end · Readiness rule (yours, or the register starter rule you adopted, by SR id)

### Renewals inside the window
| Account | Contract | Renewal date | Days to renewal | Value before renewal | Readiness (your rule) | Rule hit |
|---|---|---|---|---|---|---|

### Readiness facts per account
| Account | Go-live | Open implementation items | Outcomes agreed | Result seen by the account | Usage profile agreed (CS61) |
|---|---|---|---|---|---|

### Contract and data points for these renewals
| Account | Point | What the row says | Row | Owner (as you named them) |
|---|---|---|---|---|

### Check the record
Open accounts past their renewal date; status values your lists do not cover.

### Gaps

### Calls and runs
`scripts/renewal_metrics.py horizon` with your definitions file.

### Record
Renewal list draft. Readiness on your rule; no account is called healthy. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
