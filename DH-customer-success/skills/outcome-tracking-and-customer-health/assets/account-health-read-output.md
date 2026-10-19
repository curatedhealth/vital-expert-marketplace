# Output format: account health read

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** accounts that meet your rule, accounts that miss and on which signal, accounts that cannot be decided and why (not measured, not comparable).
2. **Frame:** period, targets version and date, your health rule, adopted register rules.
3. **Accounts (compact):** Account · Signals met / missed / not measured or not comparable · Health under your rule. Missed signals named with value against target.
4. **Label, once:** "Uptake, use and customer-reported outcomes are not clinical evidence; no comparator, so not evidence of effect (CS32)."
5. **Open questions (at most three):** missing targets or rule, missing data, denominator bases.
6. **Record:** "Health read on data you supplied." Name who clears it: "Cleared by NAME; record built with `verify.build_record`." Until a named person clears it: "Uncleared draft." This line also closes every refusal.
7. One line offering the full version.

## Full mode

### Answer

### Frame
| Item | Value |
|---|---|
| Period | |
| Targets (version, set by, set on) | |
| Health rule | |
| Adopted register rules | |

### Attainment by account and signal
| Account | Signal | Kind | Value | Numerator / denominator (basis) | Your target | Status | Gap to target |
|---|---|---|---|---|---|---|---|

### Health view
| Account | Met | Missed | Not measured or not comparable | Health under your rule | Day-one item open | Months since support ended |
|---|---|---|---|---|---|---|

### Outcome figures read honestly
Denominator, completeness beside each outcome share, PHQ-9 bands only with CS92.

### What it means for you
Two or three conditional consequences under your rule. No cause, no renewal forecast.

### Gaps

### Calls and runs
Script commands run; no library call carried account data.

### Record
Health read draft. Not clinical evidence. AI-assisted. Cleared by NAME; record built with `verify.build_record` once that named person clears it. Otherwise "Uncleared draft."
