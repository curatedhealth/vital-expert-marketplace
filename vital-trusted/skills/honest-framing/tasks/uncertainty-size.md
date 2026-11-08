# Task TR-3.2.1 Uncertainty at its real size

## Formula

| Slot | For this task |
|---|---|
| Worker | Medical reviewer with a statistics background |
| Workflow | Fill the result card from the material, set the certainty the result can carry, then hold every result sentence to it, in both directions |
| Skill | TR-3.2.1 |
| Knowledge | `references/rules.md` (R4, R5, R7, R10), `references/patterns.md` (UC1–UC9, OH1–OH5) |
| Tool | `scripts/find_framing_cues.py` where code can run. No companion yet (`references/tools.md`) |
| Prompt | This guide |
| Template | `assets/check-line.md`, `assets/framing-note.md` |
| Input | The draft, the supplied study material, the context card (reader, use, stakes) |
| Governance | TR-H1, TR-H3, TR-H6, TR-H12, TR-H13 |

## The result card

Before writing about a result, fill this from the supplied material only. A field the
material does not give stays `[GAP: not supplied]`. Design, endpoint and population are
taken as `grounded-statements` describes them; do not re-describe them here.

```
Result:            <the finding, in the source's words>
Primary or not:    <primary | secondary | exploratory or post hoc | not stated>
Estimate:          <effect size as reported, with both arms where given>
Interval:          <95% CI or other range as reported | not supplied>
Significance:      <as the source states it, e.g. p = 0.03; met / not met for the primary>
Size of study:     <n analyzed, per arm where given>
Follow-up:         <duration>
Number of studies: <one | several, as supplied>
Limitations named: <as the authors state them | not supplied>
Authors' wording:  <the conclusion as written, quoted>
```

## The certainty the result can carry

Use the card to choose the plain verb. This is a reading aid, not a grading scale, and
it never becomes a label in the draft.

| The card shows | Plain wording that fits | Words to keep out |
|---|---|---|
| Primary endpoint met, interval excludes no effect, more than one study or a large one | "reduced", "improved", "in two trials" | "proves", "definitive", "settles" |
| Primary endpoint met in one study | "in one trial, reduced"; name the study | "proves", "established", "clearly superior" |
| Primary endpoint met, wide interval or small study | "reduced, with a wide range of possible effects (95% CI …)"; give n | "dramatic", "strong", "robust" |
| Secondary, exploratory or post hoc result | "an exploratory analysis suggested"; label it as such | "showed", "demonstrated" |
| Primary endpoint not met | Say so first, with the estimate and interval | "trend", "promising", "numerically better", unless the source uses them |
| Observational or single-arm | "was associated with", "in patients treated with" | "caused", "proves", "superior to" |
| Short follow-up or surrogate only | Name the follow-up; name the endpoint | "long-term", "durable", "life-changing" |

## Guard (while drafting)

1. **Fill the result card first.** Write the result only as strongly as the card
   carries.
2. **Keep certainty words out unless the material earns them.** "Proves", "proven",
   "definitive", "dramatic", "breakthrough", "remarkable", "clearly", "undeniably",
   "game-changing", "unprecedented", and "significant" used to mean "large". If a
   strong word is wanted, use the number instead.
3. **Say the uncertainty in plain words, next to the result it belongs to.** Give the
   interval where supplied ("between 0.45 and 0.97, so the true effect could be small or
   large"). Name a small sample ("in 48 patients") and short follow-up ("over 12
   weeks"). State the limitations the authors name, in the same section, not in a
   footnote.
4. **Do not bury a clear result.** When the primary endpoint was met with an interval
   that excludes no effect, say it once, plainly, then give its limits. One hedge per
   result, placed where the real uncertainty is. Stacked hedges ("may potentially
   suggest a possible benefit") misstate the result as surely as "proves" does.
5. **Keep significance and size apart.** A p-value says how surprising the result would
   be with no effect; it does not say how large or how important the effect is. Do not
   judge clinical importance yourself (TR-H6); say what the estimate and interval are.
6. **Keep the authors' conclusion attributed.** Quote it as theirs. If it goes beyond
   the primary result, say so in one plain sentence; do not restate it in the draft's
   own voice.

## Repair (existing draft)

1. **Fill the result card** from the supplied material. If no material was supplied,
   do not judge the certainty: list the result sentences as "not checkable without the
   source" and ask for it.
2. **List every result sentence.** Where code can run,
   `python scripts/find_framing_cues.py draft.txt` lists certainty and hedging words to
   look at; it finds words, not meaning, so read each one.
3. **Classify each sentence against the card:** at the right size; stronger than the
   card (overclaim); weaker than the card (over-hedged); missing an interval, sample size,
   follow-up or limitation the material gives.
4. **Fix:** replace certainty words with the estimate and the plain verb from the table;
   remove stacked hedges and say the met result once; add the interval, n, follow-up and
   named limitations; attribute the authors' conclusion.
5. **Never delete a limitation to tidy the text.** Every change appears in the framing
   note.

## Check line

See `assets/check-line.md` (uncertainty line).

## Boundaries

- Whether the design, endpoint or population is described correctly (single-arm called
  controlled, secondary called primary, non-significant called a "trend") is
  `grounded-statements`. This task takes those facts as given and sets the certainty
  around them. If a sentence fails both, count it in each for its own reason.
- Whether risks and limitations are present at all, in proportion to benefits, is
  `balanced-evidence`. This task covers the size of the uncertainty around each result.
- Whether "superior" may be claimed against a competitor is `claims-and-label`. This
  task only keeps "proves superiority" from saying more than one trial can.
- No judgment of whether a difference is clinically meaningful, and no clinical advice
  (TR-H6).
