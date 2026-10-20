# Gap rules

A gap is information. Each reason for a gap leads to a different next step, so name the reason.

## Rule facts

| Class | When | How to word it | Next step |
|---|---|---|---|
| Sourced | A DL or CP row states it | The fact plus the row id ("8-K generally within four business days, DL-019") | None |
| Researcher's reading | The row is marked "(inference)" | "Breaches under 500 do not show in the portal (DL-092 (inference))" | Do not present as the regulator's words |
| Published method | The row is [PAPER] | "Evidence DEFINED authors plan updates every 6 to 12 months (DL-113), DOI 10.1038/s41746-023-00836-5" | DOI once in prose, beside the row id in tables |
| Pending or scheduled | HSR appeal, Swiss IPG, EU 2026/1386, UK 2028 accounts | "Applies from 17 January 2028 (DL-075); until then 2019/452 governs" | State instrument and date; never as in force before its date |
| Not in the sources | Market size, valuation multiples, return benchmarks, sector funding totals; revenue, churn or pipeline of the company; national FDI laws; state privacy laws; AI Act dates (research_reg2, not copied) | "Not in this skill's sources `[GAP]`" | The person or the owner they name supplies it, or owner not named |

## Library facts

| Situation | How to word it |
|---|---|
| No change recorded | "No change recorded in the library's log for COMPANY since DATE; the log began 12 October 2026 and was last swept 19 October 2026 (saved run); this is about the log, not the company" |
| `since` before the log began | "The log began after your memo date; changes between DATE and 12 October 2026 cannot be read from it (T5); compared filings and authorizations by date instead" |
| Period asked starts before the log | Say so first, then give the company's dated primary filings and authorization records for that period; never report "no change" for the part before 12 October 2026 |
| Company status | "Company status [GAP]: not read. Open the 8-Ks of DATE (accession, URL) for Items 1.03, 2.01, 3.01 and 5.01, and check for a Form 25 or Form 15 (DL-136 to DL-149)"; once read, quote the item with its date. Form 25 or 15 is not dissolution (DL-144, DL-149) |
| A field the saved record lacks | "not stored"; never 0, none, or a country read from an authorization ("US company") |
| A new filing | "Form TYPE dated DATE (SEC, reference, URL, retrieved DATE)"; never what it means for the company's finances |
| Evidence maturity moved | "Score X to Y on rubric v1; component C moved because input I changed"; if rubric differs, "not comparable (T4)" |
| Source not loaded | "Companies House not loaded in the library `[GAP]`; read the register directly" |
| A tool with no saved output | "Needs a live check" |

## The person's facts

| Situation | How to word it |
|---|---|
| No memo date | "Memo date not given"; A2 cannot set `since`; ask, never pick one |
| No triggers | "Trigger not given `[GAP]`"; B1 reports values, not tripped or held |
| A trigger in words only | Write it verbatim; if its reading is ambiguous on the data, say "your call" and show both readings |
| No owner or reread date | "Owner not named" (T1); "reread date not given" (T2); ask. Never suggest a job title |
| Assumption with no public signal | "Not measurable from the record (T3)"; the person's own data, labeled non-public, or not watched |

## Never

- Never advise selling, holding, buying more or writing down, and never give a valuation or a return.
- Never infer revenue, runway, outcomes, intent, market status or why filings stopped.
- Never infer company status (bankrupt, delisted, deregistered, acquired, dissolved) from press, memory or the last filing date; read the filing or register, or write "[GAP]: not read".
- Never present "no change recorded" as "nothing happened".
- Never call a watch tool.
- Never fill a date, data cut, threshold or status the person did not give; write "not given" and ask.
- Never carry facts from an earlier request; use only the inputs of the current request.
