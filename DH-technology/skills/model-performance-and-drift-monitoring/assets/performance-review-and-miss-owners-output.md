# Output format: performance review and miss owners

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/drift_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Build line 3 from A1 and A2 script output; do not recount by hand. Budget in words: answer 60, rules 60, misses 180, routes 40, decisions 50, record 45.

1. **Answer** (two sentences): the misses by name, how many have an owner, an action and a recheck date, and the open item that most limits the review.
2. **Your rules:** record rule and each personalization rule, verbatim with dates; units without a rule listed, not marked failed.
3. **Misses:** Miss · Fact · Your threshold or rule · Owner (yours or "owner not named") · Action (yours or "not given") · Version or stop · Recheck date (yours or "not given").
4. **Routes:** change control (`dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control); reportability (`dh-regulatory-and-quality` audit-capa-and-complaints).
5. **Decisions for you:** each with its facts; none taken by the model.
6. **Calls made**, then one line offering the full version.
7. **Record (the very last line, nothing after it):** "Performance review draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Your rules (verbatim, with dates)
### Misses and responses
| Miss | Fact (script) | Your threshold or rule | Owner | Action | Version or stop | May influence the decision meanwhile | Recheck date |
|---|---|---|---|---|---|---|---|
### Personalization misses
| Rule | Failed element | Owner | Recheck date or stopped |
|---|---|---|---|
### Facts that inform the choice (DA-90, DA-92; US-12, US-13; EU-05)
### Routes
### Decisions for you
### Gaps
### Calls made
### One line offering anything not shown
### Record (the very last line)
Performance review draft for the owner. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
