# Output format: check lines for trusted-check

Returned to `trusted-check` only, never shown at the end of a direct reply. One line per
aspect that ran, in plain words. Counts only; no verdict words (TR-H3, TR-H13). The
grammar is the one in `trusted-check/references/letter-lines.md`.

```
Tangible · substance: <n> statements too vague to act on, <n> passages of filler or repetition, <n> sections with no "so what" (not tool-checked)
Tangible · next step: decision or recommendation <present | missing | not needed for this work>, owner <named | missing | not needed> (not tool-checked)
Tangible · structure: <n> headings that do not match their content, <n> frameworks or groupings the content does not support, <n> points out of order for the reader (not tool-checked)
```

Which task feeds which line:

| Line | Tasks |
|---|---|
| substance | Specificity (vague statements), No fluff (filler or repetition), So what (sections with no "so what") |
| next step | Actionability |
| structure | Structure integrity |

Each line may carry up to three short plain notes, for the summary:

```
  - <where and what, e.g. "the opening paragraph says the market is 'evolving' and nothing else">
  - <e.g. "the update ends without saying what the board is asked to decide">
  - <e.g. "the 'Impact vs Readiness' matrix has no defined axes and nothing in your notes places the items">
```

Rules:

- A line whose task did not apply returns nothing. A board update with no headings
  returns no structure line.
- "Not needed for this work" is used only when the work genuinely calls for no action
  (an information note, a reply to a question); say so in a note if the reader might
  expect one.
- Counts are of passages the reader would notice, not of list hits from the script.
- Specifics left as gaps are counted in the substance line ("statements too vague to
  act on") until the person supplies them.

Two differences from the shapes proposed in `trusted-check/references/letter-lines.md`:
the structure line adds "frameworks or groupings the content does not support", and the
next step line adds the "not needed" values. Both are proposed amendments to that file,
to be applied there by its owner so the contract stays in one place.
