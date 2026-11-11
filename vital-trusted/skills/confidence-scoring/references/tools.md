# Tools

No connector, no key and no live tool. This skill reads the results `claim-assessment`
already gave, by hand, and counts them. The steps are in `by-hand.md`.

## What no tool does here

| Job | Who does it |
|---|---|
| Decide a result for a sentence | `claim-assessment`, by hand |
| Give a percentage, score or grade | Nobody. There is none |
| Describe a source | `source-assessment`, by hand |

## Script

`scripts/faithfulness.py` prints counts by result in plain words, the number of open items,
one default recommendation and the line "No confidence figure: these results were not tool-checked.". It takes counts or a JSON list of
result words. It prints no percentage and decides nothing.

```
python scripts/faithfulness.py --found 4 --partly 1 --not-found 1 --not-factual 2
python scripts/faithfulness.py --words-file results.json
```

Pitfalls: an unknown result word stops the script rather than being guessed; the default
recommendation is chosen by the first open item in risk order and may be sharpened with
the specific sentence, but keep it to one recommendation. The script cannot see whether a
sentence with no passage carries a figure; when one does, it goes first and the
recommendation aims at it. The total printed is factual claims only; opinion lines are
printed separately.
