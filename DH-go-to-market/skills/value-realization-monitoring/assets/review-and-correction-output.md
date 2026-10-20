# Output format: review and correction plan

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** which of your review rules miss, the corrections (chosen by you or to choose), owners, and the one decision needed.
2. **Rules (compact):** Rule (your words) · Result (count or note ids) · Met / missed / not measurable. Apply each rule to every note in the conversation, not only the notes the person names; list any further note that misses (for example a note with no signal row under a 'figure differs from our data' rule).
3. **Corrections:** Finding · Correction (yours, or proposed) · Owner (yours, or "owner not named") · Forum and date (yours, or "not set"). For an unsupported result, include "add a tracked signal from stored data for the next period" among the options.
4. **Open questions (at most three):** the one choice needed, then forum and date where "not set", then owners not named.
5. **Stops:** customer corrections, effect or saving wording, payment-linked outcomes.
6. **Record:** "Review draft. Rules, choices and owners are yours." Name who clears it: "Cleared by NAME; record built with `verify.build_record`." Until a named person clears it: "Uncleared draft." This line also closes every refusal.
7. One line offering the full version.

## Full mode

### Answer

### Review rules
| Area | Rule (your words) | Checked against | Result | Status |
|---|---|---|---|---|

### Findings and corrections
| Finding | Hypotheses (labeled) | Correction options (proposed, with basis) | Your choice | Owner | Forum and date |
|---|---|---|---|---|---|

### Ranking (only if you scored)
Scores as you gave them; order checked by hand.

### Drafts for the owner
Replacement sentences with only traceable figures, if asked.

### Stops for the owner

### Gaps

### Record
Review and correction draft for the accountable owner. No data edited, no target eased. AI-assisted. Cleared by NAME; record built with `verify.build_record` once that named person clears it. Otherwise "Uncleared draft."
