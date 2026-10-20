# Gap rules

A gap is information. Each reason for a gap leads to a different next step, so name the reason.

## The person's facts

| Situation | How to word it | Next step |
|---|---|---|
| Forum or period not given | "Forum not given" or "period not given" | Ask; the choice list cannot be scoped without them |
| An item has no stage gate record | "Not ready for the forum: no stage gate record" (old method, CF-12.01.03.3.1.1) | Route to `dh-clinical-development` clinical-product-lifecycle-and-stage-gates; the item is listed as left off, with the reason |
| Stage, status or readout not given | "Not given"; ask | Never fill from memory or from a public record of another product |
| No rule, criteria or weights | "Rule not given"; no ranking | Offer criteria labeled "proposed" (B1 step 2); rank nothing until confirmed |
| A score missing for one item | "Not ranked: score not given on CRITERION" | Ask; never send the call with a gap filled in |
| Capacity not given | "Capacity not given"; no capacity check | Ask for amount, unit and period |
| Decision, decider or date not given | "Not given"; ask | Never fill; the decider is never the model |
| Owner not named | "owner not named", and ask | Never suggest a job title |
| Probability of success not given | "Your probability not given"; benchmarks shown as context only | The person supplies it, labeled theirs |
| Confidential program names | Kept out of every library call | Use only the person's own material for them |

## Rule facts

| Class | When | How to word it |
|---|---|---|
| Sourced | An SP or DL row states it | The fact, its source in plain words with its date ("Pear 8-K, 7 April 2023"), then the row id; never a row id alone |
| Inference | The research file marks the row "(inference)" (for example DL-137, DL-142, DL-147, DL-149, DL-159, DL-163, DL-166, DL-168, DL-101's second sentence) | The row id followed by "(inference)", every time |
| [PAPER] | A published method or figure | Row id plus the DOI of that row's own paper, every time; in a table, in the Rows cell |
| [WF] | Read through a summarizer (ISPOR MCDA rows SP-074 to SP-081; ISO rows) | "Read through a summarizer; re-check before external use" |
| UK public-sector guidance used for a company | Green Book and benefits rows (SP-088 to SP-106), optimism bias table (SP-170 to SP-176) | "UK public-sector guidance, applied by analogy"; optimism bias values also "built on 2002 data, context, not your adjustment" |
| Benchmark | SP-082 to SP-087 | Figure with counting method and dataset; "context, not your probability" |
| Moved rule | TTBER 316/2014 expired 30 April 2026; 2026/877 in force 1 May 2026; transition to 30 April 2027 (SP-134 to SP-137) | State the instrument and the date |
| Not in the sources | Market sizes, valuations, returns, portfolio size or hit-rate targets, software or medtech success rates, optimism bias values for operating costs or benefits shortfall (SP-176), ISPOR MCDA Report 1, OKRs | "Not in this skill's sources `[GAP]`"; the person supplies it, labeled theirs, or it stays out |

## Library facts

| Situation | How to word it |
|---|---|
| A record holds an authorization | "FDA record K233577: 510(k), cleared, decision 5 August 2024 (library, retrieved 19 October 2026)" |
| No row found | "No row in the loaded sources `[GAP]`; a missing record is a coverage limit, not evidence that none exists" |
| Name search missed | "Lookup missed for NAME (exact matching); give the submission number" |
| A calculator returned 503 or 400 | "The calculator did not answer (nothing counted); computed by hand from the same formula" or "not ranked: score missing" |
| A tool with no saved output | "Needs a live check" |
| Company status, company covered by a row | Quote the filing by name and date, then the row: "Pear 8-K, 7 April 2023: chapter 11 filed in Delaware, case 23-10429 (SP-156, [WF])"; add what the form does not mean: "Form 25 is not dissolution (DL-144)"; "Form 15 is not dissolution (DL-149, inference)" (`licensing-and-deal-flags.md` section 3) |
| Company status, no row | "Company status [GAP]: not read. Open, most recent first, the company's 8-Ks for Items 1.03, 2.01, 3.01 and 5.01, and any Form 25 or Form 15 (DL-136 to DL-149)" |
| A product's current holder | "Cleared to COMPANY (FDA 510(k) record); listed today by COMPANY (FDA registration and listing, read 20 October 2026)"; who holds the rights `[GAP]` |
| A field the saved record lacks | "not stored"; never 0, none, or a country read from an authorization |

## Never

- Never fill a weight, score, probability, capacity, threshold, date or status the person did not give.
- Never present a benchmark as the person's probability or as a target.
- Never rank proposed scores.
- Never infer a company's status, intent or the availability of rights from press, memory or a filing pattern.
- Never carry facts from an earlier request; use only the inputs of the current request.
