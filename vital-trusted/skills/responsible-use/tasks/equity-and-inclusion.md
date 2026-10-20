# Task TR-6.2.4 Equity and inclusion

## Formula

| Slot | For this task |
|---|---|
| Worker | Responsible AI lead who also knows the business |
| Workflow | Read how people are described; repair stigmatizing, blaming or erasing language; name evidence gaps for groups only from the supplied material |
| Skill | TR-6.2.4 |
| Knowledge | `references/rules.md` (U9–U13), `references/patterns.md` (E1–E8) |
| Tool | `scripts/scan_language.py` where code can run. Companion slot: future language companion (none yet) |
| Prompt | This guide |
| Template | `assets/use-note.md` (language part), `assets/check-line.md` |
| Input | The draft, who it describes and who reads it, any community or company language guide the person supplies, the source material for evidence statements |
| Governance | TR-H1, TR-H3, TR-H9, TR-H12, `references/governance.md` |

## What to look at

| Kind | Looks like | Repair |
|---|---|---|
| The condition as the person | "diabetics", "epileptics", "the mentally ill" | "people with diabetes", unless the community prefers identity-first terms (U10) |
| Suffering and victim framing | "suffers from", "sufferers", "victims of", "wheelchair-bound" | "has", "lives with", "people with", "uses a wheelchair" (U13, good practice) |
| Blame | "non-compliant patients", "addicts", "substance abusers" | "people who stopped treatment", "person with a substance use disorder" (U9) |
| Stereotype | One age, sex or ethnicity shown as "the patient"; assumptions about a group's behavior | Describe groups as the evidence does; drop the assumption (U11) |
| Erasure | A group affected by the condition absent from the material | Ask whether it was intended; describe the population as the source does (U11) |
| Silent evidence gap | "Works in adults" when the supplied paper shows few people over 75 or from some groups | One plain sentence naming the gap, from the supplied material only (U12) |

## Guard (while drafting)

1. **Set the depth.** Internal and quick: fix an obvious stigmatizing word quietly; no
   note. Patient materials, campaigns, publications and anything public: continue.
2. **Write people first** by default, and follow any preference the person, the
   community or a supplied guide states (U10). Keep quotations exact (E8).
3. **Describe groups as the source does**, at the right level of detail (U11). Do not
   add groups, ages or ethnicities the source does not give.
4. **Name evidence gaps honestly** when the work says who a result applies to: if the
   supplied material shows a group was few or absent, say so in one plain sentence. If
   the material does not say, do not guess: `[GAP: not supplied — who was in the study
   by age, sex and ethnicity — supply the baseline table]` (TR-H1, E7).
5. **Scan** with `scripts/scan_language.py` where code can run, then read the hits;
   they are phrases to look at, not findings.

## Repair (existing draft or campaign copy)

1. **Make the changes** in the text, keeping the message and brand voice (TR-H9).
2. **List them briefly** in the use note: before, after, and a few plain words of why
   ("defines people by their condition", "suggests blame for stopping treatment").
3. **Ask, do not impose**, where a community's own preference may differ (for example
   identity-first terms) or where a term is in a quotation or a product name.
4. **For a patient campaign**, add one line pointing to the company's promotional or
   patient-material review, and, if the company has one, its patient engagement or
   advocacy function for the community's preferred terms.

## Check line

See `assets/check-line.md`.

## Boundaries

- Reading level and plain language are `fit-for-reader`. This task changes words only
  where they stigmatize, stereotype or erase people.
- Which studies or endpoints a document leaves out is `balanced-evidence`. This task
  names gaps for population groups only.
- Whether an evidence statement matches its source can go to `claim-assessment` when
  VERIFY is connected.
- This is not a style guide (TR-H9). Voice, tone and brand style stay with the person.
