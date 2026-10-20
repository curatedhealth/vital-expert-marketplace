# Output format: value note and next action

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** which accounts get a value note, which get a next-action note, under your pass rule; the one decision you must take.
2. **Per account, one block:**
   - Value note (draft for the owner): each result with value, numerator and denominator, period and signal row; one sentence on what it cannot show.
   - Or next action: missed signal against target, hypotheses (labeled), actions (proposed), owner you named or "owner not named", forum and date or "not set".
3. **Open questions (at most three):** the pass rule if not given; forum and date for each action marked "not set"; who clears the note.
4. **Stops:** sending, effect or cost wording, payment-linked outcomes, renewal or price.
5. **Record:** "Drafts for the owner. Nothing sent." Name who clears it: "Cleared by NAME; record built with `verify.build_record`." Until a named person clears it: "Uncleared draft." This line also closes every refusal.
6. One line offering the full version.

## Full mode

### Answer

### Pass rule
Your rule for a value note, verbatim; register rule adopted or not.

### Value notes (drafts for the owner)
| Account | Result as drafted | Signal row (measure, period, value) | What it cannot show |
|---|---|---|---|

Claims extracted from each draft and matched to rows (verify.extract_claims): claim · row · matched or removed.

### Next actions
| Account | Missed signal (value vs your target) | Hypotheses (labeled, with what would confirm) | Actions (proposed, with row) | Owner (yours) | Forum and date (yours) |
|---|---|---|---|---|---|

### Ranking (only if you scored)
Reach, Impact, Confidence, Effort as you gave them; order checked by hand.

### Stops for the owner

### Gaps

### Record
Drafts for the accountable owner. No effect, cost or comparison claim. AI-assisted. Cleared by NAME; record built with `verify.build_record` once that named person clears it. Otherwise "Uncleared draft."
