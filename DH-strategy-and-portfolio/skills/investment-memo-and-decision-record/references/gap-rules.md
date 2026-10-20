# Gap rules

A gap is information. Each reason for a gap leads to a different next step, so name the reason.

## Rule facts

| Class | When | How to word it | Next step |
|---|---|---|---|
| Sourced | A DL or CP row states it | The fact plus the row id ("Form D does not show investor names, DL-016") | None |
| Researcher's reading | The row is marked "(inference)" | "Smaller tuck-ins may never appear in an 8-K (DL-023 (inference))" | Do not present as the regulator's words |
| Published method | The row is [PAPER] | "Funding did not correlate with the robustness score (DL-117), DOI 10.2196/37677" | DOI once in prose, beside the row id in tables; state the paper's own limits |
| Moved or pending | HSR form vacated, appeal pending; EU 2026/1386 not yet applicable; Swiss IPG not in force | "Updated HSR form vacated 12 February 2026; appeal pending on the pages read (DL-051, DL-053)" | State the instrument and date; never present a pending rule as settled |
| Yearly figure | HSR thresholds and fees | "2026 figure, effective 17 February 2026 (DL-044, DL-045)" | Earlier years are `[GAP]` |
| Not in the sources | Market size, valuation multiples, return benchmarks, funding totals by sector; intermediate HSR fee tiers; CFIUS fees and timelines; national FDI laws; state health privacy laws; Companies House PSC rules; Evidence DEFINED checklist items; AI Act dates (in research_reg2, not copied) | "Not in this skill's sources `[GAP]`" | The person or the owner they name supplies it, or owner not named; never fill it |

## Library facts

| Situation | How to word it |
|---|---|
| A record holds an authorization | "FDA record K191716: 510(k), decision 23 March 2020, product code QVO (library, retrieved 19 October 2026)" |
| `status` is "DENG" | "De Novo granted (FDA code DENG; register C3)" |
| No row found | "No row in the loaded sources `[GAP]`; a missing record is a coverage limit, not evidence that none exists" |
| Source not loaded | "Companies House is not loaded in the library (API key not yet provisioned) `[GAP]`" |
| Company did not resolve | "Lookup missed for NAME (exact matching); give the legal name, FDA number or SEC number" |
| Two filing names combined | Repeat the library's flag: "the combination is a proposal until a person validates it" |
| `funding` `[GAP]` beside Form D rows | "Form D amounts as the filings state them; private rounds `[GAP]`" |
| Sum of stated amounts | Never quoted as money raised; amounts by filing type and date |
| Evidence maturity | Score with rubric version, components, excluded components and limits; "a stated convention, not a valuation" |
| A tool with no saved output | "Needs a live check"; describe from the old skill text only |
| Company status | "Company status [GAP]: not read. Open the 8-Ks of DATE (accession, URL) for Items 1.03, 2.01, 3.01 and 5.01, and check for a Form 25 or Form 15 (DL-136 to DL-149)"; once read, quote the item with its date. Form 25 or 15 is not dissolution (DL-144, DL-149) |
| A period that starts before the change log (12 October 2026) | "The library change log began 12 October 2026, after the start of your period; it cannot show changes before then. Here are the company's dated filings and authorization records for the period instead"; never "no change" |
| A field the saved record lacks | "not stored"; never 0, none, or a country read from an authorization ("US company") |

## The person's facts

| Situation | How to word it |
|---|---|
| No headings | Offer the headings in `memo-sources.md` section 7, labeled "proposed" |
| No thesis, criteria or scores | "Thesis not given" or "criteria not given"; B1 records nothing as met or missed without them |
| A deal fact missing | "Not given"; ask. Never assume a value, a date, a nationality or a data count |
| Decision, decider or date missing | "Not given"; ask. Never fill |
| Non-public material | Label "from you (non-public)" and keep it apart |
| Vendor or press figures the person brings | "From you (vendor figure, not checked against a primary record, DL-125)" |

## Never

- Never recommend investing or passing, and never give a valuation, price, multiple or return.
- Never infer revenue, runway, outcomes, intent or why filings stopped from a filing pattern.
- Never infer a valuation or investor names from a Form D.
- Never infer company status from press, memory or the last filing date.
- Never say a deal is clear, not reportable or compliant.
- Never write "approved" for a 510(k) or a De Novo, or "FDA registered" as an authorization (DL-126 to DL-128).
- Never fill a date, data cut, threshold or status the person did not give; write "not given" and ask.
- Never carry facts from an earlier request; use only the inputs of the current request.
