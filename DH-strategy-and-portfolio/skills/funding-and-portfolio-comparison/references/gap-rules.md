# Gap rules

A gap is information. Each reason for a gap leads to a different next step, so name the reason.

## Library facts

| Situation | How to word it | Next step |
|---|---|---|
| Status not read | "Status: `[GAP]`: not read. To open: EDGAR filing list for CIK(s) [as returned] and any listed parent or successor (8-K Items 1.03, 2.01, 3.01, 5.01; Form 25; Form 15), or the register (Companies House status; German insolvency notices)" | The person opens them, or the assistant reads them with a contact the person's organization gives (`references/company-status.md`) |
| Status read | "FORM ITEM, DATE, URL, read on DATE; what it does not mean: ..." (a Form 15 or 25 is not dissolution, DL-144, DL-149) | None |
| Window before the change log | "The library change log began on 12 October 2026; it does not cover [start] to 11 October 2026" | Give the dated primary filings and authorization records for that span; never "no change" |
| Sub-field absent | "FIELD field absent", never 0 or none | Make the specific call if the person needs it |
| Authorization country only | "Authorized in COUNTRY"; incorporation not in the record | Never "US company" |
| Found | Fact, date, source URL or reference, "as of" retrieval date ("Form D, 9 June 2021, amount as stored USD 110,000,007, Item 13 field not stated; library, retrieved 19 October 2026") | None |
| Unresolved company | "Lookup missed: the library found no exact match for NAME" | Ask for the legal name or a register number (FDA, EUDAMED, SEC, LEI) |
| `none_found` | "The loaded sources were searched and hold no row for COMPANY" | Never "none exists" |
| `not_assessable` | "Not assessable: SOURCE is not loaded" | Never zero |
| Field absent | "The response has no FIELD for COMPANY; not a zero" | Make the specific call if the person needs it |
| Not loaded | "The library does not load SOURCE (REASON as returned)": Companies House, the BfArM DiGA directory feed, NICE, funding, Zefix on 19 October 2026 | The person reads the register directly |
| Private rounds | "Private rounds: `[GAP]`; no funding source is licensed" | Use the person's own figures, labeled as theirs |
| 8-K item | "8-K, item not stated in the library row" | Open the filing URL |
| Form D amount | "Amount as stored; Form D Item 13 field not stated by the tool; may be stale (DL-006)" | Open the filing |
| Combined filing names | "Combined by the library; a proposal until a person validates it" | Ask the person |
| Verify gives no verdict | "Verify returned no verdict; the fact rests on the record read (reference, date)" | None |

## Rule facts

| Class | When | How to word it |
|---|---|---|
| Sourced | A DL row states it | The rule plus the row id |
| Inference | The DL row is marked "(inference)" | "the research file's inference (DL-018)" |
| Published method | The row is [PAPER] | Row id plus its DOI (once in prose, beside the row id in every table) |
| Not in the sources | Market size, valuation multiples, return benchmarks, funding totals by sector, Rule 501(a) accredited investor text, Companies House PSC rules, CFIUS fees and timelines, national FDI laws other than the Swiss IPG, state health privacy laws | "Not in this skill's sources `[GAP]`" |

## The person's facts

| Situation | How to word it |
|---|---|
| No companies named | Ask for 2 to 12 names; never pick companies |
| No criteria, weights or scores for B1 | No ranking. Show the A2 table and ask the person to score |
| A score missing for one option | "OPTION not ranked: score for CRITERION not given"; the others are ranked |
| Weights do not sum to 1 | Show the sum and ask the person to confirm |
| Owner not named | "owner not named"; ask. Never suggest a job title |
| Date, threshold or pass rule not given | "not given"; ask |
| Confidential or data-room material | Kept in its own column or section, labeled "from the person (confidential)", never merged into a public-record statement |
| A vendor funding total | "The person's figure, from SOURCE AS NAMED"; never checked against or added to filings |

## Never

- Never turn a gap into "not funded", "no investors", "no evidence", "not authorized", "not reimbursed" or "no safety events".
- Never fill a valuation, investor name, round size, revenue, runway, market size or return from memory.
- Never carry facts from an earlier request; use only the inputs of the current request.
