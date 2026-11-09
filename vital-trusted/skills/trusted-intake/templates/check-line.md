# Output format: check line for trusted-check

Returned to `trusted-check` only, never shown at the end of a direct reply. One line per
task that ran, in plain words. Counts and plain notes only; no verdict words (TR-H3,
TR-H13).

```
Context · <stakes>; <n> details stated by you, <n> read from the request, <n> assumed, <n> still open; next process: <kind of process | none apparent>
Context · inputs: <kinds, or none described>; AI use policy: <as you stated it | not stated | not asked>; tool decision left to you and your AI policy owner
```

If intake did not run before the draft:

```
Context · not gathered before drafting; reader, market and use taken from the draft only
```

`trusted-check` reads these lines as input, not as a letter row: it takes the reader and
stakes from them to set the depth, and lists assumed and open context under "Open for a
person" when the work is leaving the company (see `../../trusted-check/references/letter-lines.md`).
