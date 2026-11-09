# Output format: check line for trusted-check

Returned to `trusted-check` only, never shown at the end of a direct reply. One line per
task that ran, in plain words. Counts only; no verdict words (TR-H3, TR-H13).

```
True · invented details: <n> not in your material, <n> changed from the source, <n> where sources disagree (not tool-checked)
True · numbers: <n> figures looked at, <n> differ from the source, <n> missing what they describe, <n> given only as a percentage change (not tool-checked)
True · how studies are described: <n> statements looked at, <n> say more than the study did, <n> mix two studies or time points (not tool-checked)
```

Each line may carry up to three short plain notes after it, for the summary:

```
  - <note, e.g. "Q4 figure is a forecast written as an actual">
```

If no material was supplied:

```
True · invented details: not checked, no source material supplied (<n> statements affected)
```
