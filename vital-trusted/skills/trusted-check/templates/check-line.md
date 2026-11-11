# Line contract: what trusted-check accepts

`trusted-check` is the only skill that receives check lines. It does not return a check
line of its own; its output is the TRUSTED summary (`templates/check-output-*.md`).

Every Build and Prove skill returns lines in this shape. The full contract, with the
expected line for every skill, including those not yet written, is in
`references/letter-lines.md`.

```
<Letter word> · <aspect>: <count> <plain noun phrase>, ... (not tool-checked)
  - <note: where and what, in everyday words>        (0 to 3 notes)
```

Also accepted:

```
<Letter word> · <aspect>: not checked, <what is missing> (<n> statements affected)
<Letter word> · checked against the main question only: <n> to look at
<Letter word>: off by choice
```

The not-run line ("not checked, ...") gives the count of statements affected when it is
known and carries no "(not tool-checked)" label, because nothing was read. Every line for
a check that ran ends "(not tool-checked)".

On receipt, `trusted-check`:

1. Rejects a line with a verdict word and re-reads that check.
2. Rejects any line that claims a tool checked it, and any line that carries a percentage,
   ratio, score, tier or grade.
3. Translates each line into the plain row of the summary.
