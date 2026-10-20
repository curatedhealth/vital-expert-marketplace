# Worked example: confidence line and Verify card for a payer value story

Invented case for teaching. "Brelvia" is a fictional product; the registry, figures,
findings and source scores are made up. No VERIFY tool was called for this example: the
findings below show the shape the card is built from, not a real run. Source score axis
names follow `references/rules.md` C7, which is `[CHECK]`.

## Request

"VERIFY has checked our Brelvia value story for the regional payer meeting. Give me the
confidence score and the card. Is 69% good enough to send?"

## Findings passed on from the claim check (9 statements)

| # | Statement (short) | Status |
|---|---|---|
| 1 | Registry of 1,850 patients followed for 12 months | supported |
| 2 | Admissions 12.0% on Brelvia vs 20.0% on standard care | supported |
| 3 | Adjusted hazard ratio 0.60 (95% CI 0.48 to 0.75) | supported |
| 4 | Observational design, so association not cause | supported |
| 5 | Discontinuation 7% at 12 months | supported |
| 6 | Benefit seen across all age groups | partial (passage gives age under 65 and 65 to 74 only) |
| 7 | Brelvia saves the regional budget money | unsupported |
| 8 | Recommended in the national guideline | unverifiable (no guideline supplied) |
| 9 | Payers should prioritize patients at high admission risk | out_of_scope |

## Computation

`python scripts/faithfulness.py --source verify --json-file findings.json`

(5 + 0.5 × 1) ÷ 8 = 68.75%, rounded half up to 69%. Statement 9 is not factual and is
not counted.

## Output to the person

> Brelvia Registry Study Group. "Admissions in a 12-Month Observational Registry." Report, 2026.
>   Source score 86: authority 15 · recency 25 · relevance 30 · provenance 7
>   (A source score is about the page: who published it, how recent, how close to the
>   question, how complete its details, whether it was checked for retraction. It is not
>   about the statements.)
>
> Faithfulness 69%: of the 8 factual statements checked, this share is backed by the
> passages supplied (partly backed counts half). 1 statement was not factual and is not
> counted.
> Arithmetic: (5 + 0.5 × 1) ÷ 8 = 68.75%.
> This is support from the passages you supplied. It is not a measure of whether the
> statements are true, the sources good, the evidence balanced or the work ready to send.
>
> Verify card (draft, for human review)
>
> Checked with VERIFY: 9 statements
>   5 backed by the passage
>   1 partly backed
>   1 not backed by the passages checked
>   0 contradicted by a passage
>   1 could not be checked
>   1 not a factual statement (not counted)
>
> Open for a human (3)
> 1. "Brelvia saves the regional budget money" (not backed). The passages checked do not
>    state this; no cost analysis was supplied.
> 2. "Recommended in the national guideline" (could not be checked). No guideline was
>    supplied.
> 3. "Benefit seen across all age groups" (partly backed). The passage gives results for
>    patients under 65 and 65 to 74; it does not give results for 75 and over.
>
> Recommendation: remove the budget-savings statement, or supply the cost analysis that
> backs it and check again.
>
> The check matches words in each statement with words in its passage; a reworded or
> weaker sentence can still come back backed, so a human read still matters.
> Next step: your market access review before the meeting material is used.
> This card is not a clearance. A named reviewer clears the record.
>
> This check flags issues. It is not medical, legal, regulatory or ethics review.

## Answer to "is 69% good enough to send?"

> There is no pass mark for this number. It says how much of the text is backed by the
> passages you supplied, nothing more. The three open items above are what stands
> between 69% and the rest, and the budget statement is the one a payer will test first.
> Whether the story goes is for your market access review to decide.

## Why this is the right depth

A payer value story leaves the company (TR-H12): full card, every open item named with
the statement it concerns, the next internal process named in plain words, no threshold
and no send decision. The currency axis is absent because no currency check ran; it is
left out, not shown as 0. The total (86) is not the sum of the axes shown (77): the
connector is described as rescaling the remaining weights to 100 when an axis is empty
(`references/rules.md` C7, `[CHECK]`). Print the total as returned; never recompute it.
