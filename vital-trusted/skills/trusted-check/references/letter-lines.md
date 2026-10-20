# Letter lines: what each skill returns to trusted-check

Every Build and Prove skill returns its result to `trusted-check` as lines in one shape,
so the summary can be assembled the same way whichever skills ran. Lines go to
`trusted-check` only. They are never appended to a reply the person reads directly.

This file holds the grammar every line follows. The exact counts for each skill live in
that skill's own `assets/check-line.md`, which is the source of truth: `trusted-check`
reads the line shapes there, so the two can never drift apart. A skill that changes its
counts changes its own `check-line.md`; nothing here needs editing.

## Grammar

```
<Letter word> · <aspect>: <count> <plain noun phrase>, <count> <plain noun phrase>, ... (<not tool-checked | checked with VERIFY>)
  - <note: where and what, in everyday words>        (0 to 3 notes)
```

Rules for every line:

- **Letter word**, never the code letter: Tangible, Rule-compliant, Unbiased, Safe,
  True, Ethical, Defensible.
- **Counts only.** No verdict words (TR-H3). A zero is written as 0.
- **One line per task that ran.** A task that does not apply returns no line. A task
  that could not run returns a not-checkable line:

  ```
  <Letter word> · <aspect>: not checkable — <what is missing> (<n> statements affected)
  ```

- **Notes** are optional and plain. They say where the problem is ("the second
  paragraph", "the subject line") and what it is. No rule ids, no pattern ids.
- **Tool status** at the end: "not tool-checked" for Build skills today, "checked with
  VERIFY" only when a VERIFY tool returned the result.
- **Fallback** when the skill is not available on the host and `trusted-check` applied
  the letter's main question:

  ```
  <Letter word> · checked against the main question only: <n> to look at
  ```

All skills may add up to three notes per line, including `grounded-statements`.

## Build skills

Read each skill's `assets/check-line.md` for its exact lines.

| Letter | Skill | Line shapes |
|---|---|---|
| Tangible | `substance-and-usefulness` | `substance-and-usefulness/assets/check-line.md` |
| Tangible | `fit-for-reader` | `fit-for-reader/assets/check-line.md` |
| Rule-compliant | `claims-and-label` | `claims-and-label/assets/check-line.md` |
| Rule-compliant | `market-rules-and-data` | `market-rules-and-data/assets/check-line.md` |
| Unbiased | `balanced-evidence` | `balanced-evidence/assets/check-line.md` |
| Unbiased | `honest-framing` | `honest-framing/assets/check-line.md` |
| Safe | `patient-safety` | `patient-safety/assets/check-line.md` |
| True | `grounded-statements` | `grounded-statements/assets/check-line.md` |
| True | `sourced-claims` | `sourced-claims/assets/check-line.md` |
| Ethical | `responsible-inputs` | `responsible-inputs/assets/check-line.md` |
| Ethical | `responsible-use` | `responsible-use/assets/check-line.md` |
| Defensible | `work-record` | `work-record/assets/check-line.md` |

## Prove skills (when VERIFY is connected, or by hand marked "not tool-checked")

| Skill | What its lines carry | Line shapes |
|---|---|---|
| `claim-assessment` | Support for each claim against its passage | `claim-assessment/assets/check-line.md` |
| `source-assessment` | What each source can carry, its score and currency | `source-assessment/assets/check-line.md` |
| `confidence-scoring` | The faithfulness line and the VERIFY card | `confidence-scoring/assets/check-line.md` |
| `citation-and-record` | Reference lines and the record, with a named clearer or "uncleared draft" | `citation-and-record/assets/check-line.md` |

## Who prints what under the reference list

- `source-assessment` produces the source score and its numeric axes from VERIFY and
  explains them in plain words. It never computes a score itself.
- `citation-and-record` prints each reference line, with the score beneath it when
  `source-assessment` supplied one.
- `confidence-scoring` prints the faithfulness line and the VERIFY card under the
  reference list, from VERIFY statuses only. No figure from by-hand results.
