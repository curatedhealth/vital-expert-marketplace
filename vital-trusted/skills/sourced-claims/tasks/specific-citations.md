# Task TR-5.2.3 Specific citations

## Formula

| Slot | For this task |
|---|---|
| Worker | Experienced colleague with an evidence background |
| Workflow | Build each citation from the supplied source only; mark missing fields; never fill from memory |
| Skill | TR-5.2.3 |
| Knowledge | `references/rules.md` (R3, R4, R7, R10), `references/patterns.md` (C1–C7) |
| Tool | `scripts/find_source_cues.py` flags vague citations. Companion slot: VERIFY `build_citation` through `citation-and-record` |
| Prompt | This guide |
| Template | `assets/reference-list.md`, `assets/check-line.md` |
| Input | The draft, the supplied sources (documents, links, exports) |
| Governance | TR-H1, TR-H3, TR-H4, TR-H11 |

## What a findable citation contains

Enough for a reviewer to find the exact passage without asking. Fill each field from the
supplied source only. A field the source does not show stays a gap.

| Source type | Fields |
|---|---|
| Journal article | Authors (first author et al. is fine), title, journal, year, volume and pages or article number, DOI or PubMed ID, and the table, figure or section used |
| Preprint | As above, plus the server name and "preprint", posting date, version |
| Conference abstract or poster | Authors, title, meeting name, year, abstract or poster number |
| Label or product information | Product, document type (for example SmPC, prescribing information), market, version or revision date, section number |
| Regulator or HTA document | Issuing body, full title, document type (draft or final guidance, assessment report, decision), date, identifier if any, section |
| Clinical guideline | Society, title, edition or year, recommendation number and grade as stated |
| Data on file | Company, a specific name or reference for the data set, date; never "data on file" alone |
| Market research or sales data | Provider or agency, study or data set name, sample or market definition, period, date of the report |
| Press release, news, blog | Publisher or company, title, date, URL as supplied |
| Internal document | Title, owner team, date, version |
| Personal communication | Name, role, date, and that permission was given |

## "Add references to these claims"

This request is common and is where invented references are most likely.

1. **Use only what was supplied.** If the person supplied sources, match each claim to
   one and build the citation from it.
2. **If no sources were supplied, do not produce references.** Say plainly that you will
   not write references from memory, because a reference that looks real but is wrong is
   worse than none: a reviewer cannot tell it from a real one until they look it up.
3. **Offer what helps instead:** a list of the claims that need a source, the kind of
   source each would need for this reader (`tasks/source-type-fit.md`), and where the
   person might get it (their medical information or literature team, the label, the
   publication the claim came from). Each claim gets a gap in the text.
4. **If the person names a reference from their own knowledge** ("it's the Smith paper
   in 2023"), write it as a gap to confirm until they supply the document or its
   identifier: `[GAP: not supplied — full citation for the paper you named — send the
   PDF or its DOI]`.

## Guard (while drafting)

1. **Cite the specific passage** where the work will leave the company: table, figure,
   section or page.
2. **Name guidance by title and date**, never "FDA guidance" or "EMA guidelines" alone.
3. **Date every "current"**: "current" becomes "as of <date of the source>".
4. **Label source types that change weight**: preprint, abstract, press release, data on
   file.
5. **Keep quotations exact and attributed** to the precise source (R4).

## Repair (existing draft)

1. **List every citation** in the draft. Where code can run,
   `scripts/find_source_cues.py <draft.txt>` lists vague and incomplete ones.
2. **For each, record:** complete from the supplied source; fields missing; not
   supplied; vague (no title, no date, no identifier).
3. **Fix:** complete fields from the supplied source; mark missing fields as gaps; never
   complete a field from memory, even a DOI or a year you are sure of.

## Check line

See `assets/check-line.md`.

## Boundaries

- Citation style (Vancouver, APA, house style) is the person's choice (TR-H9). This task
  cares that the fields are there, not how they are punctuated.
- A complete citation is not a verified one. Whether the source exists as cited, and
  whether it says what the claim says, is `citation-and-record` and `claim-assessment`
  with VERIFY. Without VERIFY, say "citation not built or checked with a tool".
