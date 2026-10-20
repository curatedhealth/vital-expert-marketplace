# Output format: source score lines and the confidence line

Plain language, no rule codes (TR-H13). Printed in this order, after the draft.

## Under each reference

The reference line is the one `citation-and-record` built. Under it, the score total and
only the axes that came back as numbers. Leave out an empty axis; never print it as 0.

```
<reference line as built>
  Source score <total>: <axis> <n> · <axis> <n> · <axis> <n>
```

Once per answer, under the first score line:

```
  (A source score is about the page: who published it, how recent, how close to the
  question, how complete its details, whether it was checked for retraction. It is not
  about the statements.)
```

If relevance is low because the title is short, say so in one line; do not change the
number.

## Immediately under the reference list

When VERIFY returned the statuses:

```
Faithfulness <n>%: of the <d> factual statements checked, this share is backed by the
passages supplied (partly backed counts half). <k> statements were not factual and are
not counted.
Arithmetic: (<supported> + 0.5 × <partial>) ÷ <d> = <exact>%.
This is support from the passages you supplied. It is not a measure of whether the
statements are true, the sources good, the evidence balanced or the work ready to send.
```

When nothing factual was checked:

```
No confidence figure: nothing factual was checked (<k> statements were not factual).
```

When VERIFY did not run:

```
No confidence figure: these statements were not checked with VERIFY. A figure is only
given for tool-checked results.
```

## Internal, low stakes

```
Faithfulness <n>% (<d> statements checked against your passages); <m> open items.
```
