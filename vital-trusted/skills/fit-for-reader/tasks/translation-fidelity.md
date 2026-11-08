# Task TR-1.2.3 Translation fidelity

## Formula

| Slot | For this task |
|---|---|
| Worker | Medical writer who has written for every audience, working with qualified translators |
| Workflow | List what must survive unchanged, translate or read the translation against it, compare numbers and units, flag terms that need a qualified translator or approved wording |
| Skill | TR-1.2.3 |
| Knowledge | `references/rules.md` (R3, R6, R7), `references/patterns.md` (T1–T9) |
| Tool | `scripts/compare_numbers.py` where code can run. Companion slot: none (no companion planned) |
| Prompt | This guide |
| Template | `assets/translation-note.md`, `assets/check-line.md` |
| Input | The original, the target language and country, the reader, any approved local wording or glossary the person supplies, any existing translation |
| Governance | TR-H1, TR-H3, TR-H6, TR-H7, TR-H11 |

## Before translating

1. **Language and country.** From the person or the context card. Ask if missing:
   German for Germany, Austria and Switzerland can differ in terms and conventions.
2. **Reader.** A translation keeps the reader of the original. If the person also wants
   it adapted for a different reader, do that as a separate step (task TR-1.2.1) and say
   so; never adapt silently while translating.
3. **Approved wording.** Ask whether the person has approved local wording for this
   product or message: the approved product information in that language, an approved
   local key message, a company glossary. Use it as supplied, with its source and date.
   If none is supplied, do not substitute remembered wording for it (TR-H1).

## The fixed list

Before translating, list what must survive unchanged:

```
Numbers and units:   every figure, with its unit, timepoint and denominator
Names:               product, study, comparator, company and people, as written
Regulated terms:     indication, dosing, contraindications, warnings, side-effect terms, frequency terms
Medical terms:       disease names, endpoints, outcome measures, test names
Claims and limits:   every qualifier ("in adults", "post hoc", "compared with placebo", "may")
Required lines:      any statement the original carries for a market or process
```

## Guard (while translating)

1. **Meaning exactly.** Translate what the original says. No strengthening ("may
   reduce" stays "may reduce"), no softening, no added explanation, no dropped
   qualifier, no "improvement" of the message. A key message stays as strong as it was.
2. **Natural, not literal.** Word order and idiom follow the target language; meaning
   does not move. Where a literal rendering would be unnatural and a natural one would
   shift the meaning, keep the meaning and note the choice.
3. **Medical terms are not paraphrased loosely.** Use the approved local term when
   supplied. Otherwise use the standard term you would expect a qualified medical
   translator to use and flag it in the note as unconfirmed, or leave it in the original
   with a flag. Never invent a local brand name, indication wording or frequency term.
4. **Numbers and units unchanged.** Same values, same units, same precision. Local
   notation (decimal comma, thousands separator, space before %) is a convention, not a
   change; apply it consistently and never round. Do not convert units unless the person
   asks, and then show both.
5. **Names unchanged.** Product, study and comparator names stay as written in the
   original unless approved local names are supplied.
6. **Flag what needs a qualified translator.** Patient material, regulated product
   information, safety wording, consent or legal text, and anything leaving the company
   in the target market is flagged for a qualified medical translator and the company's
   review in that market, whatever the quality of the draft.

## Repair (checking an existing translation)

1. **Make the fixed list** from the original.
2. **Compare numbers and units.** Where code can run:
   `python scripts/compare_numbers.py original.txt translation.txt --source-locale en --target-locale de`.
   Otherwise list every figure in both by hand. Read every difference; numbers written
   as words and word units (weeks, Wochen) are not compared by the script.
3. **Compare meaning sentence by sentence.** Mark each: same meaning; stronger; weaker;
   qualifier dropped; something added; term loosely paraphrased; not translated.
4. **Fix** to the original's meaning, or flag where only a qualified translator or the
   approved wording can settle it.
5. **Note** what changed and what is open in `assets/translation-note.md`.

## Check line

See `assets/check-line.md`. The translation line is returned only when a translation
was made or checked.

## Boundaries

- Whether a translation meets a market's legal language or labeling requirement is a
  regulatory or legal determination (TR-H6). Flag it for that function.
- A translation by the assistant is a draft for a qualified translator and the company's
  review in the target market. Never call it final, certified, validated or accurate
  (TR-H3, TR-H11).
- Translating a patient-reported outcome questionnaire or other validated instrument
  needs the instrument owner's process. Stop and say so; do not translate it here.
- The facts of the original are not checked here. If the original has an invented or
  inconsistent figure, the translation keeps it and the note points to
  `grounded-statements`.
