# Task TR-8.2.1 Qualify the source

Contents: Formula; Before you start; Steps; Not tool-checked; Check line; Boundaries.

Absorbs the source-description method of the earlier Prove work, now done by hand.

## Formula

| Slot | For this task |
|---|---|
| Worker | Evidence lead |
| Workflow | Identify the source, name its kind, establish peer review, authors and funders, judge fit for the question and the reader, then hand over |
| Skill | TR-8.2.1 |
| Knowledge | `references/source-types.md`, `references/rules.md` (R3, R4, R7, R8), `references/patterns.md` (S1–S8, S13–S15) |
| Tool | None. `scripts/identify_source_id.py` where code runs |
| Prompt | This guide |
| Template | `templates/source-card.md`, `templates/check-line.md` |
| Input | The source (identifier, link, file or pasted text), the question it should answer, who will read the work, the claim it supports if known |
| Governance | TR-H1, TR-H3, TR-H4, TR-H7, TR-H11; stop rules in `governance.md` |

## Before you start

You need three things. Ask for any that is missing and changes the answer (TR-H7):

1. **The source itself**, or a stable identifier: DOI, PMID, PMCID, a regulator or HTA
   document number, or a link. A title alone is not enough to qualify a source; ask for
   the link or the file.
2. **The question it is meant to answer**, in the person's words ("does Tavexa reduce
   admissions compared with standard care in adults?").
3. **Who will read it**: payer, board, doctors, patients, agency, public, internal team.

If the person names several sources, take them one at a time.

## Steps

### 1. Identify

Find the identifier. Where code runs, `python scripts/identify_source_id.py "<text>"`
says whether it is a DOI, PMID, PMCID or link. Otherwise read it by eye: a DOI starts `10.`; a PMID is digits only; a PMCID starts
`PMC`.

Never build an identifier from a title, and never complete a partial DOI from memory.

### 2. Read what was supplied

Read the document or page the person gave you. Take kind, authors, issuer, funder, date
and identifier from it, and write "not stated" for what it does not show. If the person
gave only a link you cannot open, say so and ask them to paste the text or attach the
file. Do not fill the title, publisher or date yourself. If the person only describes
the source, build the card from what they describe, attributed "as you describe it",
write "not seen" for each field you could not read in the document itself, and ask for
the document in one line at the end ("Can you paste or attach it, so I can read it
rather than your description?"). If the document is confidential
or unpublished, point to the company's AI use policy before it is pasted anywhere. Never
write a tier, a score or "admissible".

### 3. Name the kind of source

Use the list in `references/source-types.md`, from what the source shows: peer-reviewed
article, journal article with abstract only seen, preprint, conference abstract or
poster, approved label, regulator or HTA document, clinical guideline, company data on
file, company fact sheet or brochure, market research, press release, earnings call transcript or investor presentation, news, blog or
social post, internal document. Two checks that catch most mistakes:

- **Is this the original, or a report about it?** A news story, press release or slide
  that reports a study is not the study. Name it as what it is and ask for the primary
  (`references/patterns.md` S1, S14).
- **Is this the version that was published?** A preprint, an abstract, a poster and the
  later journal article are different sources with different reach. If a published
  version exists and the person has it, the published version is the one to cite
  (`references/rules.md` R3).

### 4. Establish peer review

State one of three, and only from evidence:

| Status | Evidence needed |
|---|---|
| Peer reviewed | Published in a journal as a research article, with the journal and date visible, or the source says it was peer reviewed |
| Not peer reviewed | It is a preprint, press release, earnings call transcript or investor presentation, company fact sheet or brochure, news item, blog, data on file, market research, internal document, or the source says so |
| Peer review status not confirmed | Anything else, including conference abstracts unless the meeting's process is supplied, and a journal article where only the abstract was seen and the article type does not show |

Do not infer peer review from a DOI, a journal-like layout, a university logo or a
reputable author. A label, regulator or HTA document is not "peer reviewed"; it carries
the authority of the body that issued it. Say that instead.

### 5. Authors, funders and interests

From the source, record who wrote it, who funded it, and any disclosed interests:

- the company that makes the product, or a competitor
- an agency or consultancy paid by either
- an academic group, a patient group, a payer, a regulator

Write what is disclosed. If the source carries no funding or interest statement, write
"funding and interests not stated in the source", not "independent". A source written
or paid for by an interested party can still carry facts; say so, and say the reader
will weigh it accordingly.

### 6. Fit for the question and the reader

Compare the source with the person's question on four points. Say which match and which
do not:

- **Population**: the patients, customers or market the source covers.
- **Intervention and comparator**: what was tested against what.
- **Outcome**: what was measured, and whether it is what the claim talks about.
- **Setting and market**: country, care setting, health system, time period.

Then the reader. Use `references/source-types.md` for what each kind can carry for a
payer, the board, doctors and the public. Write it as "can carry" and "cannot carry",
never as "good enough" or "not acceptable". The company's own review process decides
acceptability (TR-H11).

### 7. Build the card and hand over

Fill `templates/source-card.md` from steps 3 to 6. Date it in full ("12 March 2026") and
give the currency line as "checked by you on <date>" or "not checked", with the check the
person can do. Then:

- If the person wants to know how strong or current the evidence is, run
  `tasks/evidence-strength-and-currency.md`.
- If the person wants to know whether a specific sentence matches the source,
  hand the source and a quoted passage to `claim-assessment`. This task does not compare
  sentences.

## Not tool-checked

Every card is labeled "not tool-checked". Where a field cannot be read from what was
supplied (for example the publisher of a link you cannot open), write "not stated" in the
card, or in a drafted deliverable `[GAP: not supplied; <field>; supply the document]`.
Never print a tier or a score.

## Check line

See `templates/check-line.md`.

## Boundaries

- Do not decide whether a claim is supported by the source; that is `claim-assessment`.
- Do not choose which type of source a draft should use while it is being written; that
  is `sourced-claims`. This task assesses a source someone has named.
- Do not judge whether the source is permitted in promotional material in a given
  market; flag it for the promotional or medical review process.
- Do not search for a better source and present it as found unless the person
  supplied it. Suggest where one might be looked for, plainly, as a suggestion.
