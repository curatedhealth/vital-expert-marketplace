# Worked example: fact-checking a value story against a registry summary

Invented case for teaching. "Velostra", the NORLA registry and Professor Anna Keller are
fictional; the figures are made up.

This run is manual, because no VERIFY result can be shown in a teaching file without
simulating one (TR-H4). With VERIFY connected, the same steps run with `extract_claims`
and `check_claim`, and the result reports the status VERIFY returned.

## Request

"Fact-check this paragraph for our payer deck against the registry summary. Keep it as
strong as you can."

## Text submitted

> Velostra cuts heart failure admissions by 40%, as shown in the NORLA trial of nearly
> 2,000 patients. Patients stay on treatment, with 95% persistence at one year. Professor
> Anna Keller, the registry lead, calls it "a new standard of care". Velostra saves
> hospitals EUR 3,000 per patient. Payers should prioritize Velostra for patients over 65.

## Passage supplied (registry summary)

> (1) NORLA is an observational registry of 1,850 adults with heart failure treated in 14
> hospitals in Germany between 2022 and 2024. (2) Hospital admission for heart failure
> within 12 months occurred in 12.0% of patients on Velostra and 20.0% of patients on
> standard care (adjusted hazard ratio 0.60, 95% CI 0.48 to 0.75). (3) Discontinuation of
> Velostra for any reason was 14% at 12 months. (4) No cost analysis was performed.

## Part A: claims, ranked and paired

| # | Claim as written | Priority | Passage |
|---|---|---|---|
| 1 | "Velostra cuts heart failure admissions by 40%" | 1 (number, efficacy, cause) | (2) |
| 2 | "as shown in the NORLA trial" | 2 (study description) | (1) |
| 3 | "of nearly 2,000 patients" | 1 (number) | (1) |
| 4 | "with 95% persistence at one year" | 1 (number) | (3) |
| 5 | Professor Anna Keller "calls it 'a new standard of care'" | 1 (quote, named person) | no passage found |
| 6 | "saves hospitals EUR 3,000 per patient" | 1 (number, performance claim) | (4) |
| 7 | "Payers should prioritize Velostra for patients over 65" | recommendation | none; "over 65" appears nowhere |

Claims 1 to 3 sit in one sentence; VERIFY would return that sentence as one claim. They
are paired separately so the result can say which part holds.

## Result as the person sees it

Fact-check against the passages you supplied (draft, for your review)

Not tool-checked: I compared each sentence with your passages by hand.
Checked against: NORLA registry summary (supplied).

What a match means: the passage you gave says the same thing as the sentence. It does
not mean the sentence is true, that the source is good, or that the work is ready.

Rewrite to match (3)
1. "Velostra cuts heart failure admissions by 40%" → "Hospital admission for heart
   failure within 12 months occurred in 12.0% of patients on Velostra and 20.0% on
   standard care (adjusted hazard ratio 0.60, 95% CI 0.48 to 0.75)". Your summary gives
   the two rates and the hazard ratio; it does not give a 40% figure, and as an
   observational registry it shows an association, not that Velostra caused the
   difference.
2. "the NORLA trial" → "the NORLA observational registry". Your summary calls it a
   registry, not a trial.
3. "nearly 2,000 patients" → "1,850 adults". Your summary gives the exact number.
All three rewritten, not tool-checked.

Removed (2)
1. "Professor Anna Keller, the registry lead, calls it 'a new standard of care'." Your
   summary contains no quote and names no one. Left out, not replaced.
2. "Velostra saves hospitals EUR 3,000 per patient." Your summary says no cost analysis
   was performed. Left out, not replaced.

Ask you (1)
1. "Patients stay on treatment, with 95% persistence at one year." Your summary says:
   "Discontinuation of Velostra for any reason was 14% at 12 months." That is not 95%.
   Should the sentence report discontinuation as the summary does?

For your judgment (1)
1. "Payers should prioritize Velostra for patients over 65." This is a recommendation,
   not something a passage can settle, and nothing supplied reports results for patients
   over 65. Whether it can appear in payer material is a question for your review
   process.

Revised text

> In the NORLA observational registry of 1,850 adults with heart failure, hospital
> admission for heart failure within 12 months occurred in 12.0% of patients on Velostra
> and 20.0% on standard care (adjusted hazard ratio 0.60, 95% CI 0.48 to 0.75).
> [GAP: conflicting — persistence at one year — confirm whether to report 14%
> discontinuation as in the summary]

VERIFY would test each sentence against its passage; connect it if this needs to be
shown. Next: because this goes to payers, source quality, the confidence figure and the
record can be added, and it goes through your promotional review process before use.

This check flags issues. It is not medical, legal, regulatory or ethics review.

## Why this is the right depth

Payer material leaves the company (TR-H12): every factual sentence checked, the full
result, the next Prove steps offered, the review process named. "As strong as you can"
was met by leading with the supported rates, not by keeping the 40%, the quote or the
saving.

## Behind the result (reference only, not shown to the person)

Patterns: C2 (sentence 1 bundles effect, design and size), C7 (figure kept on partial
support), C5 avoided (no replacement saving or quote), C6 avoided (claim 4 is a
different figure, so the person is asked, not told the passage contradicts it outright),
C11, C8. Rules R1 and R2 (substantiation; absolute claims qualified), R5 (numbers, named
people, quotes stay only from a quoted passage). The persistence figure is not derived
as 86% from the 14% discontinuation: the summary does not say persistence, and a derived
figure would need the person's decision.
