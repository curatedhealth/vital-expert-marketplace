# Worked example: open-items summary for a payer value story

Invented case for teaching. "Brelvia" is a fictional product; the registry, figures and
results are made up. No tool was called. Every result below was read by hand by
`claim-assessment` and carries the label "not tool-checked".

## Request

"We've fact-checked our Brelvia value story for the regional payer meeting. Give me the
confidence score and the open items. Is it good enough to send?"

## Results passed on from the claim check (9 claims, one per sentence)

| # | Sentence (short) | Result |
|---|---|---|
| 1 | Registry of 1,850 patients followed for 12 months | Found in your passage |
| 2 | Admissions 12.0% on Brelvia vs 20.0% on standard care | Found in your passage |
| 3 | Adjusted hazard ratio 0.60 (95% CI 0.48 to 0.75) | Found in your passage |
| 4 | Observational design, so association not cause | Found in your passage |
| 5 | Discontinuation 7% at 12 months | Found in your passage |
| 6 | Benefit seen across all age groups | Partly found: results for 75 and over not in your passage |
| 7 | Brelvia saves the regional budget money | Not found in your passage |
| 8 | Recommended in the national guideline | No passage to compare with |
| 9 | Payers should prioritize patients at high admission risk | Opinion, recommendation or definition |

## Counting

`python scripts/faithfulness.py --found 5 --partly 1 --not-found 1 --no-passage 1 --not-factual 1`

Eight factual claims, three of them open items counting the partly found one; one
opinion line listed separately, outside the total and left to the person. No ratio is worked out. The results were passed on, so the opening line says the
comparison was done in the claim check, not by this skill.

## Output to the person

> There is no confidence figure. These results were read by hand, and a percentage would
> suggest a tool measured it. Here are the counts and what is still open.
>
> Open items (draft, for human review)
>
> Not tool-checked: these results come from the earlier claim check, done by hand. I have
> not compared the claims myself.
>
> 8 factual claims
>   5 found in your passage
>   1 partly found
>   1 not found in your passage
>   0 your passage says something different
>   1 no passage to compare with
> Listed separately, not in the total: 1 opinion, recommendation or definition (left to
> you, not counted as open)
>
> Open items, in order of risk (3)
> 1. "Brelvia saves the regional budget money" (not found in your passage). The passage
>    covers the topic and does not state this; remove it or rewrite it to what the passage
>    states.
> 2. "Recommended in the national guideline" (no passage to compare with). No guideline was
>    supplied.
> 3. "Benefit seen across all age groups" (partly found). Results for 75 and over are not
>    in the passage.
>
> Recommendation: remove the budget-savings sentence, or supply the cost analysis that
> backs it, and compare again.
>
> No confidence figure: these results were not tool-checked.
>
> Found in your passage means the passage says it. It does not mean the sentence is true,
> the source good, the evidence balanced or the work ready.
> Next step: your market access or promotional review and your medical review, as your
> process names it, before the meeting material is used.
> This summary is not a clearance. A named reviewer clears the record.
>
> This check flags issues. It is not medical, legal, regulatory or ethics review.

## Answer to "is it good enough to send?"

This answer opens the same reply, before the counts, so the closing statement stays the
last line:

> There is no pass mark and no figure. The three open items below are what stands in the
> way, starting with the budget statement. Whether the story goes is for your market
> access or promotional review and your medical review, as your process names it, to
> decide.

## Why this is the right depth

A payer value story leaves the company (TR-H12): every open item named with the sentence it
concerns, the next internal process named in plain words, no threshold and no send
decision. The source note for the registry report stays in its own card from
`source-assessment` and is not added to these counts.
