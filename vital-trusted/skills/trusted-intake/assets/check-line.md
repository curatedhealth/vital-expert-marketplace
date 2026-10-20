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

Suggested for `trusted-check` (not yet built): list assumed and open context under "Open for a human" when the stakes
are leaving the company.
