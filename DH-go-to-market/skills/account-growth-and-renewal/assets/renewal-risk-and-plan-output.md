# Output format: renewal risk note and plan

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words and write 'Words: N' as the first line of the Calls made list. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap. State each fact once. Open questions: at most three. One line per item; a rule column holds the row ids and at most fifteen words.

## Short mode (default for a direct question)

Budget: answer 50, table 140, stops 90, ranking 80, record 40. The format itself fits under 450 words; do not add sections.

1. **Answer** (at most 50 words): which accounts are at risk on your rule, the recorded reason for each, and the first action in the dependency chain.
2. **Risk notes** (one table row per account): Account · Renewal date · Verdict (your rule) · Reason from the record · Action · Owner (as you named them).
3. **Stops** (one line each): actions that need the compliance, pricing, legal or data protection owner, with rows.
4. **Ranking** (only if you scored the actions): values, any tie in plain words, and the weight at which the top action changes, labeled arithmetic on your scores.
5. **Record:** Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
6. One line offering the full version.

**Refusal (any task, same cap):** (1) what is declined and why, one line with the rows; (2) the elements or figures behind it, one line each, at most five; (3) "Draft for the owner", at most 120 words, holding only facts the person stated and figures from the run, never a commitment they did not make; (4) the record line.

## Full mode

### Answer

### Your rule
The risk rule you stated, or the register starter rule you adopted (SR9, SR11).

### Risk notes
| Account | Contract | Renewal date | Verdict (your rule) | Reason from the record | Source in your file |
|---|---|---|---|---|---|

Accounts not caught by your rule: list (never "healthy").

### Hypotheses (labeled)
| Account | Hypothesis | What would confirm it | Row |
|---|---|---|---|

### Actions
| Account | Action (yours, or proposed) | Responds to | Stop it triggers (row) | Owner (as you named them) |
|---|---|---|---|---|

### Ranking of your scored actions (if scored)
| Action | Value | Contributions by criterion |
|---|---|---|
Weights and scores are yours. Ties stated.

### If an account does not renew
PHI return or destroy (CS100); EU delete or return at the controller's choice (CS109); owner as you named them.

### Sequence by dependency

### Gaps

### Calls
`analytics.mcda` (or `analytics.rice`) on your scores; `verify.build_record` at sign-off.

### Record
Risk note and plan draft. Verdicts on your rule; causes are hypotheses; proposals labeled. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
