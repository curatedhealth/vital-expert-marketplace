# Output format: privacy and compliance map

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/secdesign_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Budget in words: answer 70, regimes 110, classes 120, gaps 60, decisions 40, record 50.

1. **Answer** (two or three sentences): the regimes the person's facts point to, the deciding facts still missing, how many data classes have a basis, a control and an artifact, and the documents most missing. No compliance verdict.
2. **Regimes your facts point to:** Regime · Your fact that points there · What it asks (one line) · Source. Regimes whose deciding fact is missing: one line each, "not given; ask".
3. **Data classes:** Class · Region · Basis (yours, or "basis not given [GAP]") · Control (mechanism) · In force (artifact, or "not in force") · Rows.
4. **Gaps:** missing documents and facts, each with the row that asks for it.
5. **For you and your owners to decide:** regime conclusions, legal bases, device status (route named with pack and skill).
6. **Calls made**, then one line offering the full version.
7. **Record (the very last line, nothing after it):** "Privacy and compliance map, draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Regimes and the facts that point to them
| Regime | Your fact | What it asks | Status or version (dated) | Source | Rows |
|---|---|---|---|---|---|
### Device facts (if any), beside the 524B test, without a conclusion
### Data classes, legal basis and controls
| Class | Region | Basis (yours) | Access control | Retention | Leaves region | Artifact | In force | Rows |
|---|---|---|---|---|---|---|---|---|
### Script flags (datamap D1 to D6)
### Consent purposes and capture
| Purpose (product's words) | Data class | Screen or form | What is stored | Withdrawal stops | Rows |
|---|---|---|---|---|---|
### Fields collected but not used (proposed changes, with the version that carries them)
### Reviewer document set
| Document | Asked for by | Have it (version named) | Rows |
|---|---|---|---|
### Proposals (labeled "proposed")
### Gaps
### For you and your owners to decide
### Calls made
### One line offering anything not shown
### Record (the very last line)
Privacy and compliance map, draft for the owner. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
