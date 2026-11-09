# Claim card

One card per claim that can be checked on its own: one proposition, one card. Split a
sentence that holds two facts into two cards.

```text
Claim <N>: <exact wording from the draft>
Result: <one of the manual result words below>
Passage: "<the deciding words, quoted exactly>"
Where: <page, section, link fragment or "text you supplied">
Do: <Keep | Rewrite to match | Remove or rewrite to the passage | Keep with a gap and ask for a passage | Ask you | Leave to the person>
Not tool-checked: I compared this with your passage by hand.
```

## Manual result words

| Say | Do |
|---|---|
| Found in your passage | Keep; show the passage |
| Partly found: <missing part> not in your passage | Rewrite to match |
| Not found in your passage | A supplied passage covers the topic but does not state this: remove it, or rewrite it to what the passage states, and list it |
| Your passage says something different | Ask you |
| No passage to compare with | No supplied passage covers the topic: keep the sentence in the revised text with a visible gap, and ask for a passage. Never remove it or fill it |
| Opinion, recommendation or definition | Leave to the person |

## Rules

1. Quote the passage. Do not paraphrase the deciding words.
2. "Found in your passage" means your passage says the same thing. It does not mean the
   statement is true, the source is good or the work is ready.
3. Without a passage that covers the topic, the result is "No passage to compare with".
   It is never "Not found".
4. Never fill a gap with a plausible figure. Leave the gap and say what is missing.
5. A significance word ("significantly") backed by a p-value under the analysis plan's
   stated threshold, or by a stated confidence interval, is found; add a note saying
   whether the endpoint is primary or secondary.
6. The meanings of the results are defined once, in
   `skills/claim-assessment/references/statuses.md`; if this card and that file ever
   differ, that file wins.
