# Output format: decision evidence tracking

## Short mode (default; 250 to 450 words)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, the "what it means" paragraph, repeated row ids in prose, secondary rules, rows not tied to the person's question; then shorten each doubt line to section number and price only. Never cut a doubt line, a gap, a stop, the route line or the record line. Refusals follow the same 450-word cap.

1. **Answer:** per decision, one sentence: category and what it said about the evidence, in the body's words.
2. **Log table:** Reference · Title · Category (verbatim, section) · Published · Read on · Flags (merged, stored status at odds). Where the migration or update page gives a month without a day, write it and mark the day `[GAP]` (HTG562: "December 2025").
3. **Economic statement and every doubt:** per decision, the economic conclusion and the model result it rests on (verbatim, section, with the price, using the section 3 figures), with the data source in the body's words (HTG624 1.1 rationale: "before and after Sleepio was introduced in 9 GP practices") and the committee's accepted conclusion at the accepted price with its conditions (HTG562 4.11: cardiology "slightly cost saving", "symptoms more than 24 hours apart"; stroke or TIA downstream "likely to be cost neutral or cost saving"), then one line per doubt section the guidance names, never a sample (for HTG624: 3.4, 4.5, 4.6, 4.13, 4.14, 4.15, 4.16), each with the price, model or scenario it applied to, or "all prices". Format per line: section · price or scenario · short verbatim phrase. A doubt raised on an earlier price is labeled with that price, not presented as a doubt on the accepted case. Where a scenario has two arms, give both (HTG562 3.14: cost incurring if all monitoring repeated; cost saving if only the comparators repeated). Label clinical doubts "clinical, no price" rather than "all prices".
4. **Windows:** per early-use decision only (omit for routine use): period and its source, dates, as of DATE.
5. **Not read or not published:** one line per `[GAP]`.
6. **Calls and record:** calls made; "Library rows retrieved DATE; decision pages read DATE." Clears it: [the person named, in their words, or owner not named: ask "Who clears this record?"]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
7. **Route:** one line: building or fixing the person's own case goes to `reimbursement-evidence-support`; prices, status and clocks go to dh-market-access.

End with one offer: the full log, or A2 (obligations and methods).

## Full mode

### Answer

### Decisions in scope
| Reference (aliases) | Body, scheme | Title | Stored status | Category as read | Published | Last updated | Read on | Source |
|---|---|---|---|---|---|---|---|---|

### What each decision said about the evidence
| Reference | Topic (economic, clinical, uncertainty, evidence asked) | Price, model or scenario it applies to | Verbatim | Section | URL |
|---|---|---|---|---|---|

### Evidence windows
| Reference | Period | Source of the period | From | To | As of DATE |
|---|---|---|---|---|---|

### Other bodies
DiGA directory, HAS opinions, JCA reports, ICER-PHTI and IQWiG: what was read, what is `[GAP]`, with rows.

### What it means
Facts only: accepted evidence, doubted assumptions, asked outcomes, and which touch the person's case. No forecast.

### Sources and record
Rows, URLs, read and retrieval dates. AI-assisted draft. Clears it: [the person named, in their words, or owner not named: ask "Who clears this record?"]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
