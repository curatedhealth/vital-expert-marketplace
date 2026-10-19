# Output format: renewal and retention definitions

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words and write 'Words: N' as the first line of the Calls made list. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap. State each fact once. Open questions: at most three. One line per item; a rule column holds the row ids and at most fifteen words.

## Short mode (default for a direct question)

Budget: answer 40, definitions 120, choices 130, check 60, record 40. The format itself fits under 450 words; do not add sections.

1. **Answer** (at most 40 words): one line that no source defines these measures, so they are your definitions (owner-stated).
2. **Definitions** (one line per measure you asked about): name: formula, denominator.
3. **Choices still open** (one line each): the choice, and the register starter rule beside it where one exists, labeled 'yours to adopt'.
4. **Consistency check** (one line per failure only).
5. **Record:** Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
6. One line offering the full version.

**Refusal (any task, same cap):** (1) what is declined and why, one line with the rows; (2) the elements or figures behind it, one line each, at most five; (3) "Draft for the owner", at most 120 words, holding only facts the person stated and figures from the run, never a commitment they did not make; (4) the record line.

## Full mode

### Answer

### Definitions card (owner-stated)
| Item | Your definition | Register starter rule adopted (SR id) | Changed from last period? |
|---|---|---|---|
| Cohort | | | |
| Unit | | | |
| Renewed | | | |
| Lost | | | |
| Open, and in the denominator? | | | |
| Exclusions (field = value) | | | |
| Value basis and currency | | | |
| Expansion | | | |
| Contraction | | | |
| Offer signed, refused, open | | | |

### Formulas
| Figure (your name) | Formula |
|---|---|

### Consistency check
| Check | Result |
|---|---|

### Definitions file
The JSON the script reads, as confirmed.

### Gaps

### Record
Definitions draft. Owner-stated, not a standard. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
