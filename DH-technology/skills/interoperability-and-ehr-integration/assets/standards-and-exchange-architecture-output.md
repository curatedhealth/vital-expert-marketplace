# Output format: standards and exchange architecture

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/fhir_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Budget in words: answer 70, versions 120, pattern 100, rules 80, record 50.

1. **Answer** (two or three sentences): the versions that apply for certification and the current publications, kept apart; the guide option and pattern per exchange; the rule that most changes the design. No compliance verdict.
2. **Versions:** Standard · Required for certification (regulation, date read) · Current publication (date) · Rows.
3. **Pattern:** Profile · Pattern · Interaction · Scope · Why others set aside (only exchanges asked about).
4. **Rules that attach:** one line each, source name and date in plain words with the row id after it; proposals say "proposed".
5. **For you to decide:** guide and version, patterns, open elements, rules for the owner the person names for legal or regulatory matters.
6. **Calls made**, then one line offering the full version.
7. **Record (the very last line, nothing after it):** "Architecture draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Exchanges (sender, receiver, purpose, as you gave them)
### Version baseline
| Standard | Required for certification | Current publication | Rows |
|---|---|---|---|
### Guide options and profiles in use
| Exchange | Guide options (yours to choose) | Profiles in use | Elements left open (local profile or out of scope, your call) | Rows |
|---|---|---|---|---|
### Exchange patterns
| Profile | Pattern | FHIR interaction | Scope | Why the other patterns were set aside | Rows |
|---|---|---|---|---|---|
### Rules that attach to each exchange (payer APIs, TEFCA, information blocking, HIPAA and BAA, Part 2, consumer health data, EHDS, DiGA ePA, DTAC and DCB, DSI, terminology licensing)
### Proposals, not rules (with dates)
### Gaps
### For you to decide
### Calls made
### One line offering anything not shown
### Record (the very last line)
Architecture draft for the owner. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
