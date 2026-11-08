# Task TR-8.2.2 Evidence strength and currency

Absorbs the currency-check method of the earlier vital-verify plugin.

## Formula

| Slot | For this task |
|---|---|
| Worker | Evidence lead |
| Workflow | Place the evidence (design), count the studies behind the claim, check retraction, correction and supersession, date it, then say what it can carry |
| Skill | TR-8.2.2 |
| Knowledge | `references/rules.md` (R1, R2, R4, R5, R6), `references/source-types.md`, `references/patterns.md` (S5, S6, S9–S12, S16) |
| Tool | VERIFY `check_currency`. `scripts/identify_source_id.py` where code runs |
| Prompt | This guide |
| Template | `assets/source-card.md` (strength and currency rows), `assets/verify-block.md`, `assets/check-line.md` |
| Input | The qualified source from TR-8.2.1, the claim it is meant to support, who will read it |
| Governance | TR-H1, TR-H3, TR-H4, TR-H6, TR-H8; stop rules in `references/governance.md` |

## Steps

### 1. Where the evidence sits

Name the design as the source names it. Do not upgrade it.

| Design, as the source states it | What it can show | Plain caution to give |
|---|---|---|
| Systematic review or meta-analysis of randomized trials | A pooled estimate across several trials | Only as good as the trials it pools; check which ones and when it searched |
| Randomized controlled trial | An effect of the intervention compared with the comparator, in that population | One trial, one population, one comparator |
| Non-randomized or observational study (cohort, registry, case-control, real-world data) | An association in routine practice | Cannot by itself show cause; groups may differ in ways not measured |
| Case series or case report | That something happened in these patients | No comparison group; cannot show how often or why |
| Expert opinion, consensus, editorial, advisory board | What these experts think | It is a view, not a measurement |
| Model (economic, budget impact, simulation, forecast) | What follows if its inputs and assumptions hold | Results depend on inputs; it is not an observation |
| Market research, survey | What these respondents said | Who was asked and how many limits who it speaks for |

This order follows the logic of GRADE and the Oxford CEBM levels (`references/rules.md`
R1, R2): randomized evidence starts higher than observational evidence; case series and
expert opinion sit lowest; and a level can move down for risk of bias, inconsistency,
indirectness, imprecision or publication bias. Do not assign a GRADE certainty rating
or a CEBM level yourself. Report one only when the source itself states it (for
example a guideline that grades its recommendations), and say who assigned it.

### 2. One study or a body of evidence

GRADE rates certainty for each outcome across a body of studies, not one study at a
time (R1). Ask: is the claim resting on one study, or on several that agree?

- One study carrying a general claim ("X reduces admissions") is the most common stretch.
  Write what the one study showed, in its population, and say it is one study.
- If several studies were supplied and they disagree, say so. Do not pick the favorable
  one silently (that is also a balance problem for `balanced-evidence`).
- If the person says "the evidence shows" but supplied one source, write `[GAP: not
  supplied — other studies on this question — supply them or say "one study"]`.

### 3. Retraction, correction, expression of concern

With VERIFY: call `check_currency` with the DOI, PMID or PMCID in its own argument
(`references/tools.md`). Report the notice it returns, in plain words, with the time of
the check. A URL alone returns "not checked"; say exactly that. "Not checked" is not
"clear".

Without VERIFY: ask whether the person has checked the journal page and a retraction
database (`references/rules.md` R6), and write "retraction and correction status not
checked". Never say a paper "has not been retracted" without a check.

What the notices mean for the person:

- **Retracted**: the paper should not carry the claim. It can be cited only for the fact
  that it was retracted (R4, R5).
- **Corrected**: read the correction. The figure being used may be the one that changed.
- **Expression of concern**: the journal has raised a question it has not resolved.
  Treat the paper as in doubt and say so.
- **Superseded or withdrawn** (guidance, labels, documents): the newer version is the
  source to use. Ask for it.

### 4. Superseded guidance and labels

Guidelines, labels, regulator and HTA documents are replaced. For each:

- Note the date and version shown on the document.
- Ask whether a newer version exists, or check the issuing body's page if the person
  supplied the link and it can be opened. Do not name a newer version from memory.
- If the document says it is under review, updated, replaced or withdrawn, say so
  plainly.
- For a label, the approved label in the person's market at the time of use is the
  reference; another market's label or an older version is a different source (flag for
  `claims-and-label`).

### 5. Date and currency

- Give the publication or issue date as the source shows it, in full ("12 March 2024").
  If there is only a year, give the year and say the full date is not shown.
- For "current", "latest", "standard of care" or "now" claims, the source must carry a
  date that supports them. Otherwise `[GAP: out of date or unclear date — …]`.
- Without a tool and without a date, ask for the date and mark currency "not checked".
- Age alone is not a verdict. An older trial can still be the pivotal evidence; an older
  guideline may have been replaced. Say which question the date raises.

### 6. What it can carry

Write the two lines that matter most on the card:

- **Can carry**: the narrowest true statement the source supports, for this reader. For
  example: "That in one randomized trial in adults with condition X, events were lower
  with drug D than placebo at 52 weeks."
- **Cannot carry**: what the person may be tempted to make it say. For example: "That
  drug D reduces events in all patients, or compared with other treatments, or that it
  is standard of care."

## Without VERIFY

Run steps 1, 2 and 4 to 6 by hand. Retraction and correction status is "not checked"
and currency is "not checked" unless the person supplies a dated check. Label the card
"not tool-checked".

## Check line

See `assets/check-line.md`.

## Boundaries

- Do not perform a formal risk-of-bias assessment or assign a GRADE rating. Name the
  design, the count of studies and the questions the reader will ask. A formal
  appraisal belongs to a specialist evidence or HEOR function.
- Do not judge whether a surrogate endpoint or a model is acceptable to a specific payer
  or HTA body. Say what it is; the person's market access or HEOR colleagues decide.
- Do not give clinical advice or say which treatment a guideline makes "right" for a
  patient (TR-H6).
