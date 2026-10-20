# Output format: open dependency log (draft for the person)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** open items (count), how many lack an owner, a receiver or a late path, the first item in dependency order, and the decisions waiting.
2. **Open items in dependency order:** table Step · Work product · Owed by (named, or "owner not named") · Receiver · Asked on · Due on (the person's date, or `[GAP]`) · Days open · Waits on · Blocked decision · Late path.
3. **Sourced clocks that apply:** one line each with row and instrument (for example PL82, PL41), stated as facts.
4. **Missing:** owners, receivers, dates and late paths to fill, listed once.
5. **Record:** "Open dependency log draft. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft. This is the last line of the answer body.
6. **Calls made** (after the record line): list (script runs included).

## Full mode

### Answer
### Log as checked (script output or the same table by hand)
| id | Work product | Category (person's) | CTQ (person's mark) | Sender to receiver | Owed by | Asked on | Due on | Days open | Waits on | Blocked decision | Late path |
|---|---|---|---|---|---|---|---|---|---|---|---|
### Dependency order and circular waits
### Sourced clocks (rows, instrument, applies or not)
### Late paths: given, missing, proposed (labeled; not applied)
### Gaps
### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
### Calls made (after the record line)
