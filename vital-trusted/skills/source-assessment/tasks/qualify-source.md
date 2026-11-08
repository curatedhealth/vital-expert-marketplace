# Task TR-8.2.1 Qualify the source

Absorbs the source-grading method of the earlier vital-verify plugin.

## Formula

| Slot | For this task |
|---|---|
| Worker | Evidence lead |
| Workflow | Identify the source, name its kind, establish peer review, authors and funders, judge fit for the question and the reader, then hand over |
| Skill | TR-8.2.1 |
| Knowledge | `references/source-types.md`, `references/rules.md` (R3, R4, R7, R8), `references/patterns.md` (S1–S8, S13–S15) |
| Tool | VERIFY `qualify_source`; `ingest_document` for a supplied PDF or internal document. `scripts/identify_source_id.py`, `scripts/print_source_score.py` where code runs |
| Prompt | This guide |
| Template | `assets/source-card.md`, `assets/verify-block.md`, `assets/check-line.md` |
| Input | The source (identifier, link, file or pasted text), the question it should answer, who will read the work, the claim it supports if known |
| Governance | TR-H1, TR-H3, TR-H4, TR-H7, TR-H11; stop rules in `references/governance.md` |

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
says whether it is a DOI, PMID, PMCID or URL and which VERIFY argument it goes in.
Otherwise read it by eye: a DOI starts `10.`; a PMID is digits only; a PMCID starts
`PMC`.

Never build an identifier from a title, and never complete a partial DOI from memory.

### 2. Qualify with VERIFY (when connected)

- Call `qualify_source` with the identifier in its own argument and the person's
  question in `question` (`references/tools.md`). Passing the question is what lets the
  tool score relevance; without it, relevance has no value.
- If the source is a PDF, pasted text or internal document with no public identifier,
  it can only be qualified after `ingest_document`, and only if the person says they
  may process it there. Ask: "Are you allowed to upload this document to VERIFY under
  your company's rules?" Never set the attestation for them. If the document is
  confidential or unpublished, point to the company's AI use policy before uploading.
  Then call `qualify_source` with the returned document id.
- If the tool returns inadmissible, say so with the reason it gives. Where the reason
  is a failed fetch, say the fetch failed. Do not fill the missing title, publisher or
  date yourself, and do not grade the source by hand as if the tool had passed it.
- Print the tool block (`assets/verify-block.md`): the reference, the source score
  total and only the axes that have numbers. Where code runs, `scripts/print_source_score.py`
  does this from the tool's JSON.

### 3. Name the kind of source

Use the list in `references/source-types.md`, from what the source shows: peer-reviewed
article, preprint, conference abstract or poster, approved label, regulator or HTA
document, clinical guideline, company data on file, market research, press release,
news, blog or social post, internal document. Two checks that catch most mistakes:

- **Is this the original, or a report about it?** A news story, press release or slide
  that reports a study is not the study. Name it as what it is and ask for the primary
  (`patterns.md` S1, S14).
- **Is this the version that was published?** A preprint, an abstract, a poster and the
  later journal article are different sources with different reach. If a published
  version exists and the person has it, the published version is the one to cite
  (`rules.md` R3).

### 4. Establish peer review

State one of three, and only from evidence:

| Status | Evidence needed |
|---|---|
| Peer reviewed | Published in a journal as a research article, with the journal and date visible, or the source says it was peer reviewed |
| Not peer reviewed | It is a preprint, press release, news item, blog, data on file, market research, internal document, or the source says so |
| Peer review status not confirmed | Anything else, including conference abstracts unless the meeting's process is supplied |

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

Fill `assets/source-card.md` from steps 3 to 6. Then:

- If the person wants to know how strong or current the evidence is, run
  `tasks/evidence-strength-and-currency.md`.
- If the person wants to know whether a specific sentence is supported by the source,
  hand the qualified source and a quoted passage to `claim-assessment`. This task does
  not decide support.

## Without VERIFY

Run steps 1 and 3 to 7 by hand from the source as supplied. Label the card "not
tool-checked". Where a field could only come from the tool (for example the publisher
of a link you cannot open), write `[GAP: not checkable here — <field> — connect VERIFY
or supply the document]`. Never print a tier or a score.

## Check line

See `assets/check-line.md`.

## Boundaries

- Do not decide whether a claim is supported by the source; that is `claim-assessment`.
- Do not choose which type of source a draft should use while it is being written; that
  is `sourced-claims`. This task assesses a source someone has named.
- Do not judge whether the source is permitted in promotional material in a given
  market; flag it for the promotional or medical review process.
- Do not search for a better source and present it as found unless a tool or the person
  supplied it. Suggest where one might be looked for, plainly, as a suggestion.
