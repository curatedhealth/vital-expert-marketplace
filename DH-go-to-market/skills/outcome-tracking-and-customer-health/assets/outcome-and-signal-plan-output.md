# Output format: outcome and signal plan

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** for each outcome the customer agreed to see, the signal(s) that will show it; then the gaps (fields not stored, targets not set, instruments without sourced cut points).
2. **Signals (compact):** Signal (your words) · Kind · Definition (row) · Denominator basis · Field or report · Your target. Include a maintenance signal (setting: still running 6 or more months after support ends, CS26, CS30) and one line that the expected usage profile is agreed with the customer at commissioning (NICE ESF Std 16, CS61).
3. **Label, once:** "Uptake, use and customer-reported outcomes are not clinical evidence (CS32)."
4. **Open questions (at most three):** targets and the health rule first, then the eligible population, then any payment link (routed to Market Access outcomes-contract-monitoring).
5. **Record:** "Measurement plan draft. Signals and targets are yours." Name who clears it: "Cleared by NAME; record built with `verify.build_record`." Until a named person clears it: "Uncleared draft." This line also closes every refusal.
6. One line offering the full version.

## Full mode

### Answer

### Frame
| Item | Value |
|---|---|
| Customer and setting (inner, outer: CS12) | |
| Eligible population (reach denominator, CS27) | |
| Outcomes agreed with the customer | |
| Period | |
| Payment-linked outcomes | none, or "routed to outcomes-contract-monitoring" |

### Signals
| Signal (your words) | Kind | Definition used | Row | Numerator | Denominator and basis | Field or report | Source type | Period | Your target and direction |
|---|---|---|---|---|---|---|---|---|---|

### Instruments
| Instrument | Sourced | Not sourced | Row |
|---|---|---|---|

### Health rule and adopted register rules
Your rule (all, at least N, none) and any register starter rule you adopted, verbatim.

### Agreement and review
How the plan is agreed (written commitment, CS49) and reviewed (audit and feedback, CS44); forum, cadence and owner as you set them.

### Target file
The plan in the shape `scripts/account_health.py` reads (version and date included).

### Gaps

### Record
Measurement plan draft for the accountable owner. Not clinical evidence. AI-assisted. Cleared by NAME; record built with `verify.build_record` once that named person clears it. Otherwise "Uncleared draft."
