# Output format: check line for trusted-check

Returned to `trusted-check` only, never shown at the end of a direct reply. One line per
task that ran, in plain words. Counts only; no verdict words (TR-H3, TR-H13). Shape from
`trusted-check/references/letter-lines.md`.

```
Unbiased · uncertainty: <n> statements more certain than the data allow, <n> statements less certain than the data allow, <n> results missing an interval, sample size, follow-up or limitation the material gives (not tool-checked)
Unbiased · framing: <n> figures or charts framed to look larger or smaller than they are (not tool-checked)
Unbiased · interests: <n> interests in the material, <n> not disclosed where the result is used, <n> sources labeled independent or neutral without support in the material (not tool-checked)
```

The first count of each line is the one proposed in `letter-lines.md`. The added
counts on the uncertainty and interests lines are this skill's proposal: over-hedging
and missing intervals are half of the uncertainty task, and an unsupported
"independent" label is the commonest interest failure. `letter-lines.md` needs the same
change before `trusted-check` relies on the extra counts.

The interests line runs only when the material shows an interest or the draft labels a
source independent or neutral.

Each line may carry up to three short plain notes after it, for the summary:

```
  - <where and what, e.g. "slide 3: 'proves superiority' from one trial">
  - <e.g. "chart on slide 4 starts at 80%, so a 4-point gap looks like a doubling">
  - <e.g. "the summary calls the study independent; the paper names the company as funder">
```

If no study material was supplied:

```
Unbiased · uncertainty: not checkable — no study material supplied (<n> result statements in the draft)
Unbiased · framing: not checkable — chart data or axis not supplied (<n> charts affected)
```
