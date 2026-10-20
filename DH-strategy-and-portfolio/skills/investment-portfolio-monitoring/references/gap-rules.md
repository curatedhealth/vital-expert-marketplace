# Gap rules

A gap is information. Each reason for a gap leads to a different next step, so name the reason.

## Library facts

| Situation | How to word it | Next step |
|---|---|---|
| Status not read | "Status: `[GAP]`: not read. To open: EDGAR filing list for CIK(s) [as returned] and any listed parent or successor (8-K Items 1.03, 2.01, 3.01, 5.01; Form 25; Form 15), or the register (Companies House status; German insolvency notices)" | The person opens them, or the assistant reads them with a contact the person's organization gives (`references/company-status.md`) |
| Status read | "FORM ITEM, DATE, URL, read on DATE; what it does not mean: ..." (a Form 15 or 25 is not dissolution, DL-144, DL-149) | None |
| Sub-field absent | "FIELD field absent", never 0 or none | Make the specific call if the person needs it |
| Authorization country only | "Authorized in COUNTRY"; incorporation not in the record | Never "US company" |
| Change recorded | Change as returned, event date, source, "retrieved DATE" | Open the source if the person needs the content |
| No change recorded | "No change recorded in the library's log from FIRST ENTRY to the last sweep on DATE" | Never "nothing happened" |
| Window before the log began | "The window starts before the log began on 12 October 2026; events between SINCE and then may be missing; that span is not 'no change'" | Give the dated primary filings and authorization records for that span (saved funding signals first, then EDGAR per CIK, FDA or DiGA records) |
| Holding not read | "Not read in this cycle" | Run the call, or record why not |
| Unresolved name | "Lookup missed: the library found no exact match for NAME" | Ask for the legal name or a register number |
| Field absent or `not_assessable` | "Not a zero; SOURCE is not loaded" or "field absent" | None, or the specific call |
| Not loaded | Companies House, Zefix, funding, the DiGA directory feed, NICE (19 October 2026); HHS portal not listed | The person reads the source directly |
| 8-K item | "8-K reported; item not stated in the library row" | Open the filing URL |
| Score changed between runs | "The library's score changed from A to B; rubric version on both runs: V or not stated" | `evidence-maturity-monitoring` (this pack) |
| Response shape not yet seen | "Needs a live check" | Report as returned |

## Rule facts

| Class | When | How to word it |
|---|---|---|
| Sourced | A DL row states it | The rule plus the row id |
| Inference | The DL row is marked "(inference)" | "the research file's inference (DL-023)" |
| Not in the sources | Benchmarks for filing frequency or portfolio health, Companies House PSC rules, CFIUS fees and timelines, national FDI laws other than the Swiss IPG, state health privacy laws, HHS guidance on rendering PHI unusable | "Not in this skill's sources `[GAP]`" |

## The person's facts

| Situation | How to word it |
|---|---|
| No holdings list | Ask for it (holding, library reference, since, owner, reread date); never build one from the library |
| No watch rules | "Watch rules not stated `[GAP]`"; offer A1 |
| No since date | "since not given"; ask. Never choose one |
| Owner not named | "owner not named"; ask. Never suggest a job title |
| Reread date not given | "reread date not given"; ask |
| Confidential holding data (board packs, KPIs, cap tables) | In its own section, labeled "from the person (confidential)", never in a library call or a public-record statement |

## Never

- Never turn "no change recorded" into "nothing happened", or a missing filing into "no event".
- Never fill revenue, runway, valuation, a mark, an exit view or a company's status from memory or from filing dates.
- Never carry facts from an earlier request; use only the inputs of the current request.
