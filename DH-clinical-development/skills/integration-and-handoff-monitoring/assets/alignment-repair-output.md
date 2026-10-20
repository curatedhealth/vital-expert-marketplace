# Output format: alignment repair list

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** handoffs not received (count), the first in dependency order, the decisions still blocked, and how many lack an owner or a look-again date.
2. **Repairs in dependency order:** table Step · Work product · Owner owes (named, or "owner not named") · Blocked decision · Waits on · Look again on (person's date, or `[GAP]`).
3. **Routed elsewhere:** items that are not handoff problems, each with pack and skill (or old-pack heading).
4. **Record:** "Alignment repair list draft for OWNER. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft. This is the last line of the answer body.
5. **Calls made** (after the record line): list (script run included).

## Full mode

### Answer
### Repairs in dependency order
| Step | id | Work product | Owner owes | Blocked decision | Gate anchor (rows) | Waits on | Look again on |
|---|---|---|---|---|---|---|---|
### Circular waits (the person decides which goes first)
### Sourced clocks that bear on an item (facts, with instrument)
### Routed elsewhere
### Gaps
### Record
Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
### Calls made (after the record line)
