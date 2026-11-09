# Output format: check line for trusted-check

Returned to `trusted-check` only, never shown at the end of a direct reply. One line
per task that ran, in plain words. Counts only; no verdict words, no tier, no score
(TR-H3, TR-H13). The shape follows the shared stamp: letter word, aspect, counts, then
"(not tool-checked)" at the end.

```
True · sources: <n> looked at, <n> not peer reviewed or status not confirmed, <n> made or paid for by an interested party, <n> do not fit the question or reader (not tool-checked)
True · strength and currency: <n> single studies carrying a general claim, <n> retracted or corrected, <n> may be replaced or undated, <n> currency not checked (not tool-checked)
```

If no source was supplied for the work's claims:

```
True · sources: not checked, no sources supplied (<n> claims affected)
```
