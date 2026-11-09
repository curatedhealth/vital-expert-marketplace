# Tools

No connector, no key and no live tool. Claims are compared with passages by hand, and every
result is labeled "not tool-checked". The steps are in `by-hand.md`; the six results are
defined once in `statuses.md`.

## What no tool does here

| Job | Who does it |
|---|---|
| Split the text into claims | You, by hand, or the manual script below |
| Decide whether a passage says what the sentence says | You, by hand |
| Judge whether the source is good | `source-assessment`, by hand |
| Give a percentage or score | Nobody. There is none |

## Script (manual split)

`scripts/split_claims.py` splits a text into sentences with start and end offsets that
slice back to the exact input, and flags priority signals (numbers, proportions in words,
documents said to exist or be attached, comparisons, quotes,
efficacy or safety words, causal words, named titles, recommendation words). It is a
manual aid, labeled "manual split, not tool-checked". It never gives a result.

```
python scripts/split_claims.py text.txt
python scripts/split_claims.py text.txt --json
```

Pitfalls: abbreviations such as "e.g." and "vs." are not sentence ends; decimals are not
split; flags are signals for ranking, not a judgment. Two facts in one sentence come back
as one sentence, so note both parts yourself.
