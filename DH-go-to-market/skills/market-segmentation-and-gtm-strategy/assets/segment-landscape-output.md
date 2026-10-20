# Output format: segment landscape (fact table)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** one or two sentences: how many candidate segments, which have a payer route on record, and the one gap that most changes the picture.
2. **Segments:** Segment (proposed or yours) · Buyer · User · Payer and route (row) · Binding channel rule (row) · Peers on record (as of date).
3. **Coverage:** one line: what the library does not load (from `list_commercial_dh_sources`).
4. **Gaps that matter:** at most three, classed per `gap-rules.md`.
5. **Calls made:** tool and arguments, one line each.
6. **Record:** "Fact draft. Segments proposed unless yours." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
7. One line offering the full version.

## Full mode

### Summary

### Perimeter
| Feed | Loaded | Not loaded and why | Last load |
|---|---|---|---|

### Segments
| Segment | Buyer | User | Payer | Setting and job | Market | Status (yours or proposed) |
|---|---|---|---|---|---|---|

### Payer route and channel rules per segment
| Segment | Route | Entry conditions (rows) | Channel rules that bind a motion (rows) |
|---|---|---|---|

### Peers on record
| Peer | Product | Record (authorization or listing) | Date | Source URL | Retrieved | Lookup status |
|---|---|---|---|---|---|---|

### Peer evidence position (only if asked)
| Company (products covered) | Authorizations by register | Studies by link tier | Safety events | Evidence maturity (points of assessable, rubric v1) | Not assessable | Retrieved |
|---|---|---|---|---|---|---|
Context about each peer's published evidence; not a judgment of your product and not a prediction.

### Company or product view (only if asked)
Identity, products and authorizations, studies, recalls, filings, as tables with URLs. No raw tool JSON.

### Gaps
| Fact | Class | Next step |
|---|---|---|

### Record
Fact draft. No peer outcome, revenue or intent inferred. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
