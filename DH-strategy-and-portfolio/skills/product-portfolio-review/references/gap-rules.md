# Gap rules

A gap is information. Each reason for a gap leads to a different next step, so name the reason.

## The person's records

| Situation | How to word it | Next step |
|---|---|---|
| Forum or sitting not named | "Forum not given" | Ask; a review needs one named forum (old method) |
| No decision log or minutes supplied | "Not measurable `[GAP]`: no decision record supplied" | Ask for the record the forum keeps |
| Decision only in a slide or deck | "Fail: lives only in a slide" under the default pass rule | The person decides whether to keep that part of the rule |
| No pass rule confirmed | Report the four fields per decision; no pass or fail | Offer the default rule (`review-signals.md` section 1) labeled "proposed" |
| Rule not supplied, or dated after the forum | "Rule not given" or "rule dated after the forum: cannot score this sitting" | Ask for the rule confirmed before the forum |
| Scores or weights missing | "Not recomputed: scores not in the record" | Ask; never reconstruct scores |
| Decision rule not machine-readable | "Read by hand"; both readings if the words allow two, "your call" | The person settles the reading |
| Capacity not given | "Capacity not given"; no capacity check | Ask for amount, unit and period |
| Benefits plan missing a field | "owner not given", "baseline not given", "target not given", "measure not given", "review date not given" | Ask; the field is the person's |
| Actual not measured | "Not measurable" | Ask the owner the person named for the measure |
| No benefits threshold | Share of planned change only; "no rule given", no verdict | The person sets the rule |
| Owner, next forum or date not named | "owner not named", "forum not named", "date not set"; ask | Never suggest a job title, a forum or a date |

## Rule facts

| Class | When | How to word it |
|---|---|---|
| Sourced | An SP or DL row states it | The fact, its source in plain words with its date ("Akili 8-K, 2 July 2024"), then the row id; never a row id alone |
| Inference | The research file marks the row "(inference)" (for example DL-137, DL-142, DL-147, DL-149, DL-159, DL-163, DL-166, DL-168, DL-101's second sentence) | The row id followed by "(inference)", every time |
| Old method | The pass rule, forum score and repair steps | "Old method, CF-12.01.03.3.2.x" |
| [PAPER] | A published method | Row id plus the DOI of that row's own paper, every time; in a table, in the Rows cell |
| [WF] | Read through a summarizer (ISPOR MCDA rows SP-074 to SP-081; SP-106) | "Read through a summarizer; re-check before external use" |
| UK public-sector guidance used for a company | SP-088 to SP-106; optimism bias table SP-170 to SP-176 | "UK public-sector guidance, applied by analogy"; optimism bias values also "built on 2002 data, context, not your adjustment" |
| Not in the sources | Decision-quality scores, benefits realization rates, portfolio size or hit-rate targets, optimism bias values for operating costs or benefits shortfall (SP-176), OKRs | "Not in this skill's sources `[GAP]`" |

## Library facts

| Situation | How to word it |
|---|---|
| No change recorded | "No change in the library's log from DATE (log began 12 October 2026) to LAST SWEEP; not a statement about the company" |
| Period starts before 12 October 2026 | "The library change log began 12 October 2026, after the start of your period; it cannot show changes before then. Here are the company's dated filings and authorization records for the period instead"; never "no change" |
| Company status, company covered by a row | Quote each filing by name and date, then the row: "Akili 8-K, 2 July 2024: tender offer completed; Akili became a wholly owned subsidiary of Virtual Therapeutics Corporation (SP-151, [WF])"; add what the form does not mean: "Form 25 is not dissolution (DL-144)"; "Form 15 is not dissolution (DL-149, inference)" (`licensing-and-deal-flags.md` section 3) |
| Company status, no row | "Company status [GAP]: not read. Open, most recent first and not only from the start of your period, the company's 8-Ks for Items 1.03, 2.01, 3.01 and 5.01, and any Form 25 or Form 15 (DL-136 to DL-149)" |
| A holding or license in a company whose status changed | "Your holding is unconfirmed until status is read and your own records confirm it" |
| A product's current holder | "Cleared or granted to COMPANY (FDA record); listed today by COMPANY (FDA registration and listing, read 20 October 2026)"; who holds the rights `[GAP]` |
| A tool with no saved output | "Needs a live check" |
| A field the saved record lacks | "not stored"; never 0, none, or a country read from an authorization |

## Never

- Never average decisions into one forum score; report each.
- Never rescore the rule to match what was decided, or reconstruct a missing score.
- Never call a drift wrong or a match right; both are readings against the rule as written.
- Never judge the people in the forum.
- Never fill a date, threshold, capacity, owner or status the person did not give.
- Never carry facts from an earlier request; use only the inputs of the current request.
