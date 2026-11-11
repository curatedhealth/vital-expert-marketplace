# Letter lines: what each skill returns to trusted-check

Every Build and Prove skill returns its result to `trusted-check` as lines in one shape,
so the summary can be assembled the same way whichever skills ran. Lines go to
`trusted-check` only. They are never appended to a reply the person reads directly.

This file holds the grammar every line follows. The exact counts for each skill live in
that skill's own `templates/check-line.md`, which is the source of truth: `trusted-check`
reads the line shapes there, so the two can never drift apart. A skill that changes its
counts changes its own `templates/check-line.md`; nothing here needs editing.

## Context lines from trusted-intake

A line that starts "Context ·" comes from `trusted-intake`. It is not a letter row. Read it
to set the depth and the next process. When the work is leaving the company, list each
assumed or still-open detail under "Open for a person". Never show the line itself.

## Grammar

```
<Letter word> · <aspect>: <count> <plain noun phrase>, <count> <plain noun phrase>, ... (not tool-checked)
  - <note: where and what, in everyday words>        (0 to 3 notes)
```

Rules for every line:

- **Letter word**, never the code letter: Tangible, Rule-compliant, Unbiased, Safe,
  True, Ethical, Defensible.
- **Counts only.** No verdict words (TR-H3). A zero is written as 0.
- **One line per task that ran.** A task that does not apply returns no line. A task
  that could not run returns a not-run line, with the count of statements affected
  when it is known:

  ```
  <Letter word> · <aspect>: not checked, <what is missing> (<n> statements affected)
  ```

- **Notes** are optional and plain. They say where the problem is ("the second
  paragraph", "the subject line") and what it is. No rule ids, no pattern ids.
- **Label** at the end: "(not tool-checked)", on every line for a check that ran. A
  not-run line carries no label, because nothing was read. No line claims a tool checked
  it. The same rule is in `../../../templates/check-line-stamp.md`.
- **Fallback** when the skill is not available on the host and `trusted-check` applied
  the letter's main question:

  ```
  <Letter word> · checked against the main question only: <n> to look at
  ```

All skills may add up to three notes per line, including `grounded-statements`.

## Build skills

Read each skill's `templates/check-line.md` for its exact lines.

| Letter | Skill | Line shapes |
|---|---|---|
| Tangible | `substance-and-usefulness` | `substance-and-usefulness/templates/check-line.md` |
| Tangible | `fit-for-reader` | `fit-for-reader/templates/check-line.md` |
| Rule-compliant | `claims-and-label` | `claims-and-label/templates/check-line.md` |
| Rule-compliant | `market-rules-and-data` | `market-rules-and-data/templates/check-line.md` |
| Unbiased | `balanced-evidence` | `balanced-evidence/templates/check-line.md` |
| Unbiased | `honest-framing` | `honest-framing/templates/check-line.md` |
| Safe | `patient-safety` | `patient-safety/templates/check-line.md` |
| True | `grounded-statements` | `grounded-statements/templates/check-line.md` |
| True | `sourced-claims` | `sourced-claims/templates/check-line.md` |
| Ethical | `responsible-inputs` | `responsible-inputs/templates/check-line.md` |
| Ethical | `responsible-use` | `responsible-use/templates/check-line.md` |
| Defensible | `work-record` | `work-record/templates/check-line.md` |

## Prove skills (by hand, marked "not tool-checked")

| Skill | What its lines carry | Line shapes |
|---|---|---|
| `claim-assessment` | How each claim compares with its passage, in the six hand-check words | `claim-assessment/templates/check-line.md` |
| `source-assessment` | What each source can carry and its currency, with no tier or score | `source-assessment/templates/check-line.md` |
| `confidence-scoring` | Counts by result, open items in order of risk, and the fixed line "No confidence figure: these results were not tool-checked." | `confidence-scoring/templates/check-line.md` |
| `citation-and-record` | Reference lines and the record, with a named person who reviewed it or "Uncleared draft" | `citation-and-record/templates/check-line.md` |

## Who prints what under the reference list

- `source-assessment` writes a source card for each source. It gives no tier or score.
- `citation-and-record` prints each reference line, from the supplied details only.
- `confidence-scoring` prints the open-items summary under the reference list, with the
  fixed line "No confidence figure: these results were not tool-checked." There is no figure.
