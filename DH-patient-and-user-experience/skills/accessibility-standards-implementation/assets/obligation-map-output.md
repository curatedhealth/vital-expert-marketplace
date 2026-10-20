# Output format: obligation map

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question; 250 to 450 words)

1. **Answer:** on the facts you gave, the instruments that may apply, the WCAG version and level (or EN 301 549 edition) each cites, and the nearest date in force with the instrument that set or moved it. One to three sentences.
2. **Your facts:** role, size, markets, surfaces, as you stated them; open ones marked `[GAP]`.
3. **Map (compact):** Instrument · Applies if · Cites · Date (instrument) · Rows.
4. **Where versions differ:** one line with the criteria count (for example "2.1 AA to 2.2 AA adds six criteria, drops 4.1.1").
5. **Exceptions on your surfaces:** one line naming only the exceptions that touch the product the person described (for a patient portal or record letters: individualized, password-protected documents, UX-US-12, UX-US-20), written "applies if".
6. **Open questions (at most three):** the role question first.
7. **Stops:** coverage is your legal owner's call; nothing here says you conform.
8. **Record:** "Obligation map draft on facts you supplied. Not a legal opinion. AI-assisted. To be cleared by NAME; the record is built with verify.build_record once NAME clears it." Until a named person clears it: "Uncleared draft." Who clears it: the owner the person named, in their words, or "owner not named". The record is built with `verify.build_record` once that named person clears it; until then the line reads "uncleared draft".
9. One line offering the full version.

## Full mode

### Answer

### Your facts
| Fact | Your answer | Decides |
|---|---|---|

### Obligation map
| Instrument | Applies if | Cites (version, level, edition) | Dates (instrument that set or moved them) | Exceptions or burden route | Rows |
|---|---|---|---|---|---|

### Instruments left out, and why

### Version differences
Counts and criteria from `scripts/criteria_lookup.py diff`.

### Inferences and caveats
EAA and health apps (inference, UX-EU-04); interim final rules; proposals (HTI-5); not checked (V4.1.1 in the OJ, national transposition).

### Open questions

### Calls made
Library calls, if any, with arguments and what came back.

### Record
Draft. No statement of coverage or conformance. AI-assisted. Names who clears it (the owner the person named, or "owner not named"); the record is built with `verify.build_record` once that named person clears it. Until then: "Uncleared draft."
