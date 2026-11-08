# Output format: VERIFY block

Only when a VERIFY tool ran in this conversation (TR-H4). Every value comes from the
tool result; nothing is filled in. Goes at the foot of the source card.

## After qualify_source (and check_currency, if it ran)

```
Checked with VERIFY on <date in full>
<reference line: the citation from citation-and-record if built, otherwise the title, issuer and date the tool returned>
Source score <total>: <axis> <value> · <axis> <value> · ...   (only axes with a number)
Tier: <tier word as returned> (how completely the source identifies itself, not how strong the evidence is)
Retraction and updates: <notice as returned, e.g. "corrected", "none reported">, checked <time> | not checked (<reason, e.g. "link only, no DOI">)

What the score describes: who published it, how recent it is, how well it matches your
question, how completely it identifies itself, and whether a currency check cleared it.
It does not say whether any sentence in your draft is supported.
```

Plain names for the axes, if the person asks:

| Axis as returned | Say |
|---|---|
| authority | who published it |
| recency | how recent it is |
| relevance | how well it matches your question |
| provenance | how completely it identifies itself |
| currency | whether a retraction or update check cleared it |

[CHECK: axis names and meanings as described in the earlier vital-verify method;
confirm against a live qualify_source return.]

## When qualify_source returned inadmissible

```
VERIFY could not qualify this source: <reason as returned; for a failed fetch, "the fetch failed">.
The title, publisher and date are not filled in. To go further: <supply the PDF | supply a DOI or PMID | open the link and paste the page>.
```

No score is printed. No tier other than the one returned is printed. The card's other
fields are filled only from what the person supplied, marked "as supplied by you".

## Rules

- Omit any axis whose value is null. Do not write "relevance: n/a" or "currency: 0" for
  a null.
- Do not round, rescale or recompute the total.
- Do not show a tier or score when no tool ran, not even as "about".
