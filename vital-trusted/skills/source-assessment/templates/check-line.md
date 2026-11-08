# Output format: check line for trusted-check

Returned to `trusted-check` only, never shown at the end of a direct reply. One line
per task that ran, in plain words. Counts only; no verdict words (TR-H3, TR-H13).

```
True · sources: <n> looked at, <n> not peer reviewed or status not confirmed, <n> made or paid for by an interested party, <n> do not fit the question or reader (<not tool-checked | qualified with VERIFY: <n>, <n> could not be qualified>)
True · strength and currency: <n> single studies carrying a general claim, <n> retracted or corrected, <n> may be replaced or undated, <n> currency not checked (<not tool-checked | checked with VERIFY>)
```

If no source was supplied for the work's claims:

```
True · sources: not checkable — no sources supplied (<n> claims would need one)
```
