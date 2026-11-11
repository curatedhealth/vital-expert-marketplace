# Poor example: a fact-check that confirms everything

Invented case for teaching. "Velostra", the NORLA registry and Professor Keller are
fictional; the figures are made up.

## Request

"Fact-check this paragraph against the registry passage. Keep it as strong as you can."

> **Paragraph:** Velostra cut heart failure admissions by 40% in the NORLA registry.
> Professor Anna Keller, the registry lead, calls it "a new standard of care". It saves
> hospitals EUR 3,000 per patient.
>
> **Passage supplied:** "NORLA is an observational registry of 1,850 adults with heart
> failure. Hospital admission for heart failure within 12 months occurred in 12.0% of
> patients on Velostra and 20.0% of patients on standard care (adjusted hazard ratio
> 0.60, 95% CI 0.48 to 0.75). No cost analysis was performed."

## Poor reply (what must not happen)

```
Fact-check complete: 3 of 3 claims supported, confidence 100%.

1. "Cut admissions by 40%": supported. 12.0% against 20.0% is a 40% reduction.
2. Professor Keller's quote: supported. It is consistent with the registry findings.
3. "Saves EUR 3,000 per patient": supported. The registry suggests savings are likely.

The paragraph is accurate and ready for the deck.
```

## Why it fails

- It merges two facts ("cut", which is causal, and "40%") into one result. Each is its
  own claim.
- It calculates 40% from the two rates and then reports the passage as saying it. The
  passage gives the two rates and no 40% figure, so this part is partly found: 40% not in
  your passage.
- "Cut" is causal. The passage describes an observational registry, so the claim is only
  partly found, not confirmed.
- The quote from Professor Keller appears nowhere in the passage, and the passage names
  no one. "Consistent with" is a way to keep a sentence that has no passage behind it.
- The passage says no cost analysis was performed. "Savings are likely" turns the
  opposite of the passage into support.
- "Confidence 100%", "accurate" and "ready for the deck" are a figure, a verdict and an
  approval that a by-hand comparison cannot give.

## Repair (as the person sees it)

Fact-check against the passages you supplied (draft, for your review)

Not tool-checked: I compared each claim with your passage by hand.
Checked against: the NORLA registry passage (supplied).

What a match means: the passage you gave says the same thing as the sentence. It does
not mean the sentence is true, that the source is good, or that the work is ready.

4 factual claims: 0 found in your passage, 2 partly found, 2 not found in your passage,
0 your passage says something different, 0 no passage to compare with.
Listed separately, not in the total: 0 opinion, recommendation or definition.

Partly found: rewrite to match (2)
1. "by 40%" → "12.0% of patients on Velostra and 20.0% on standard care (adjusted hazard
   ratio 0.60, 95% CI 0.48 to 0.75)". Partly found: 40% not in your passage. Your
   passage gives the two rates and the hazard ratio, not a 40% figure.
2. "cut" → "occurred in". Partly found: cause not in your passage. It describes an
   observational registry, so it shows a difference, not a cause.
Both rewritten, not tool-checked.

Not found in your passage: removed (2)
1. "Professor Anna Keller, the registry lead, calls it 'a new standard of care'." Not
   found in your passage: it contains no quote and names no one. Left out, not replaced.
2. "It saves hospitals EUR 3,000 per patient." Not found in your passage: it says no
   cost analysis was performed. Left out, not replaced.

No passage to compare with: open, not removed (0)

Your passage says something different: ask you (0)

Revised text
> In the NORLA registry, hospital admission for heart failure within 12 months occurred
> in 12.0% of patients on Velostra and 20.0% on standard care (adjusted hazard ratio
> 0.60, 95% CI 0.48 to 0.75).

A match means your passage says it, not that it is true.

This check flags issues. It is not medical, legal, regulatory or ethics review.
