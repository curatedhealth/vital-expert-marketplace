# Output format: expansion result review

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words and write 'Words: N' as the first line of the Calls made list. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap. State each fact once. Open questions: at most three. One line per item; a rule column holds the row ids and at most fifteen words.

## Short mode (default for a direct question)

Budget: answer 50, not signatures 30, repairs 160, ranking 60, record 40. The format itself fits under 450 words; do not add sections.

1. **Answer** (at most 50 words): offers signed out of offers made, acceptance with its formula, refusals by recorded reason, and your rules missed.
2. **Not signatures** (one line): outcomes outside your lists (for example a meeting held).
3. **Repairs** (one line each): Reason · Repair (yours, or proposed) · Stop it triggers (rows) · Owner (as you named them).
4. **Ranking** (only if you scored the repairs): values; ties stated.
5. **Record:** Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
6. One line offering the full version.

**Refusal (any task, same cap):** (1) what is declined and why, one line with the rows; (2) the elements or figures behind it, one line each, at most five; (3) "Draft for the owner", at most 120 words, holding only facts the person stated and figures from the run, never a commitment they did not make; (4) the record line.

## Full mode

### Answer

### Offers and outcomes
| Account | Contract | Offer date | Outcome (your value) | Counted as | Recorded reason |
|---|---|---|---|---|---|

### Figures
| Figure | Formula used | Value | Your rule | Verdict |
|---|---|---|---|---|

### Reasons and where they route
| Reason (as recorded) | Accounts | Routes to | Hypotheses (labeled, if asked) | What would confirm |
|---|---|---|---|---|

### Repairs
| Repair (yours, or proposed) | Responds to | Offer element? Rows and stop | Owner (as you named them) |
|---|---|---|---|

### Ranking of your scored repairs (if scored)
| Repair | Value | Contributions |
|---|---|---|

### Gaps

### Calls and runs
`scripts/renewal_metrics.py expansion`; `analytics.mcda` or `analytics.rice` on your scores; `verify.build_record` at sign-off.

### Record
Expansion review draft. Verdicts on your rules; causes are hypotheses; proposals labeled. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
