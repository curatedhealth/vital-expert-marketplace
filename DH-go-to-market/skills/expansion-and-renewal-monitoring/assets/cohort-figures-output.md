# Output format: cohort renewal and expansion figures

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words and write 'Words: N' as the first line of the Calls made list. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap. State each fact once. Open questions: at most three. One line per item; a rule column holds the row ids and at most fifteen words.

## Short mode (default for a direct question)

Budget: answer 60, figures 120, outside 70, losses 70, questions 40, record 40. The format itself fits under 450 words; do not add sections.

1. **Answer** (at most 60 words): the account renewal rate and, if computed, value retained without and with expansion, each with formula and denominator, for the period in full dates; the count of open and unclassified accounts.
2. **Figures** (one table row per figure): Figure (your name) · Formula · Value · Your rule · Met / missed / no rule set. If open accounts are in the denominator, one extra line per figure: 'if open accounts renew flat, for reading only'.
3. **Outside the figures** (one line each, with contract ids): excluded, open, unclassified, past-date open, missing values.
4. **Losses by recorded reason** (one line each, kept apart): reason, contract id, where it routes.
5. **Open questions** (at most three): your pass rule for each figure if none was given.
6. **Record:** Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
7. One line offering the full version.

**Refusal (any task, same cap):** (1) what is declined and why, one line with the rows; (2) the elements or figures behind it, one line each, at most five; (3) "Draft for the owner", at most 120 words, holding only facts the person stated and figures from the run, never a commitment they did not make; (4) the record line.

## Full mode

### Answer

### Cohort
Period · Accounts in period · Excluded (rule) · Counted · Renewed · Lost · Open · Unclassified

### Figures
| Figure (your name) | Formula used | Value | Your rule | Verdict |
|---|---|---|---|---|

### Value bridge (if value fields exist)
| Starting value | Lost | Contraction | Open (if counted) | Expansion | End value counted |
|---|---|---|---|---|---|

### Lost accounts
| Account | Contract | Renewal date | Recorded reason | Routes to |
|---|---|---|---|---|

### Open, excluded and unclassified accounts
| Account | Contract | Status | Why outside or inside the denominator |
|---|---|---|---|

### Gaps

### Calls and runs
`scripts/renewal_metrics.py cohort` with your definitions file.

### Record
Figures on your data and your definitions; no benchmark is sourced and none is used. Not clinical evidence. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
