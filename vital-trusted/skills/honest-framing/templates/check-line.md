# Output format: check line for trusted-check

Returned to `trusted-check` only, never shown at the end of a direct reply. One line per
task that ran, in plain words. Counts only; no verdict words (TR-H3, TR-H13). Shape from
`trusted-check/references/letter-lines.md`.

```
Unbiased · uncertainty: <n> statements more certain than the data allow, <n> statements less certain than the data allow, <n> results missing an interval, sample size, follow-up or limitation the material gives (not tool-checked)
Unbiased · framing: <n> figures or charts framed to look larger or smaller than they are (not tool-checked)
Unbiased · interests: <n> interests in the material, <n> not disclosed where the result is used, <n> sources labeled independent or neutral without support in the material (not tool-checked)
```

The interests line runs only when the material shows an interest or the draft labels a
source independent or neutral.

Each line may carry up to three short plain notes after it, for the summary:

```
  - <where and what, e.g. "slide 3: 'proves superiority' from one trial">
  - <e.g. "chart on slide 4 starts at 80%, so 88% and 84% look far apart">
  - <e.g. "the summary calls the study independent; the paper names the company as funder">
```

If no study material was supplied:

```
Unbiased · uncertainty: not checked, no study material supplied (<n> statements affected)
Unbiased · framing: not checked, chart data or axis not supplied (<n> statements affected)
```
