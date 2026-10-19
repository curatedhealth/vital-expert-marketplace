# Output format: research action log

Short mode: 450 words maximum, counted without the calls list and tables' source column. Every other table cell counts. Before handing over, count the words of the answer above "Calls made" (for example with `wc -w`) and state nothing over 450. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Use only these sections, in this order. One line per item; no context paragraphs and no explanatory bullets. Tables at most five rows; quotes at most ten words; each row id once. The format fits under 450 words when followed.

1. **Answer** (at most 60 words): the stops that need a decision under the person's rule, plus critical-task stops.
2. **Actions:** Stop · Participants · Action or refusal (proposed or yours) · Fix type · Retest · Owner you named · Release you set. "Owner not named" or "not set" where missing.
3. **Ranking:** one line: the RICE order if the person scored; otherwise which scores are needed (reach, impact, confidence as a percent, effort).
4. **For the owner:** one line: critical-task stops and any usability or benefit wording.
5. **Below your rule:** stop ids in one line.
6. **Record:** "Research action draft, AI-assisted. Clearer: [name you give, or not named]. The record is built with verify.build_record once that named person clears it; until then this is an uncleared draft."
7. One line offering the full version and the insight log file.

## Full mode

### Answer

### Your rule for "repeated"
In your words, or "register starter rule, adopted by you", or "no rule: all stops listed".

### Action log
| Stop | Participants by group | Their words | Action or refusal | Proposed or yours | Fix type (UX-US-33) | Retest (UX-US-42) | Owner | Release | Date |
|---|---|---|---|---|---|---|---|---|---|
"Owner not named" or "not set" where missing.

### Ranking (only if you scored)
| Rank | Action | Reach | Impact | Confidence (%) | Effort | RICE score |
|---|---|---|---|---|---|---|

### Insight log (for the monitoring sibling)
CSV columns: insight_id, study_id, stop_id, participants_hit, raised_on, decision, decided_on, decision_ref, owner, release.

### Stops for the accountable owner

### Gaps

### Calls made

### Record
Research action draft. No claim that a fix makes the product usable or safe. AI-assisted. Clearer: NAME, or not named. The record is built with verify.build_record once that named person clears it; until then this is an uncleared draft.
