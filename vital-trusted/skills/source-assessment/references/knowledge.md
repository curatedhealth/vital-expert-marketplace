# Knowledge: source-assessment

This file is the single home for this skill's sourced rules, failure patterns, gap
wording and failure modes. Where the same rule or pattern appeared in more than one
earlier file, one copy is kept.

## Contents

- Part 1: Rules (sourced, with scope and confirmation status)
- Part 2: Failure patterns (before and after)
- Part 3: Gap rules (shared wording, with this skill's cases)
- Part 4: Failure modes (detection questions)

## Part 1: Rules

Each entry names its primary document, its date and how it was confirmed (TR-H8). A
`Confirmed` entry was read in the official copy on the date shown. A `[CHECK]` entry is
described as good practice and is not cited as a requirement.

These are methodology and publication-ethics documents, not laws. None of them is a
regulatory requirement for a company's promotional or medical material. Where a company
SOP sets its own standard for sources, that standard governs (TR-H11).

Last reviewed: 20 October 2026. Jurisdiction: international (none is tied to one
market).

| Id | What the skill takes from it | Primary document | Status |
|---|---|---|---|
| R1 | Certainty of evidence is rated for each outcome across a body of studies, not study by study. Randomized trials without important limitations start as high; observational studies without special strengths start as low. Certainty can be lowered for risk of bias, inconsistency, indirectness, imprecision and publication bias, and raised for a large effect, a dose-response gradient, or when plausible confounding would reduce the effect. Four levels: high, moderate, low, very low. Case series usually warrant very low. "Expert opinion is not a category of quality of evidence." | GRADE Handbook, eds. Schünemann, Brożek, Guyatt, Oxman, updated October 2013 (gdt.gradepro.org/app/handbook/handbook.html), sections 5 and 5.1.1, tables 5.1 to 5.3. The handbook states it is being replaced by the GRADE Book (book.gradepro.org) and that some sections are outdated. | Confirmed from the official online handbook on 20 October 2026. Whether the GRADE Book changes any wording used here: `[CHECK]`. |
| R2 | A hierarchy of likely best evidence by question type (treatment benefit, harm, diagnosis, prognosis), with systematic reviews of randomized trials at level 1, and the levels intended as a heuristic that can be moved up or down. | OCEBM Levels of Evidence Working Group, "The Oxford Levels of Evidence 2" (the 2011 Oxford CEBM Levels of Evidence), Oxford Centre for Evidence-Based Medicine, cebm.ox.ac.uk/resources/levels-of-evidence/ocebm-levels-of-evidence. | Partly confirmed 20 October 2026: the official page, working group and citation were read. The levels table and its grading-up and grading-down note could not be opened from the official site: `[CHECK]`. The skill uses only the ordering, not level numbers. |
| R3 | Preprints are work not peer reviewed; servers should identify them as such and require disclosure of interests and funding. A citation should clearly indicate that the reference is a preprint. Where a preprint was later published in a peer-reviewed journal, cite the published article rather than the preprint. Authors "should be cautious about referencing preprints" never later published. | ICMJE, Recommendations for the Conduct, Reporting, Editing, and Publication of Scholarly Work in Medical Journals, updated January 2026 (icmje.org/icmje-recommendations.pdf), section III.D.3 "Preprints" and the references section. | Confirmed from the official PDF on 20 October 2026. |
| R4 | Honest errors require a published correction. Errors serious enough to invalidate results and conclusions may require retraction; retracted articles remain in the public domain and are clearly labeled as retracted. Editors may publish an expression of concern while misconduct procedures are under way. | ICMJE Recommendations, updated January 2026 (as R3), section on corrections, retractions and expressions of concern. | Confirmed from the official PDF on 20 October 2026. |
| R5 | "The purpose of retraction is to correct the literature and ensure its integrity, not to punish the authors." Where reliability is in doubt but evidence is incomplete or delayed, an expression of concern may be used. | COPE, Retraction guidelines, version 3, published 4 September 2025 (publicationethics.org/guidance/guideline/retraction-guidelines; doi:10.24318/cope.2019.1.4). | Confirmed from the official COPE page on 20 October 2026. |
| R6 | Retraction data can be checked openly: the Retraction Watch database was acquired by Crossref and released through Crossref's Labs API; publishers also record retractions through Crossmark. Coverage depends on available metadata and is not complete. | Crossref, "Crossref acquires Retraction Watch data and opens it for the scientific community", 12 September 2023 (crossref.org/blog/news-crossref-and-retraction-watch). | Confirmed from the official Crossref post on 20 October 2026. |
| R7 | Authors are responsible for disclosing relationships and activities that might bias their work, and sources of support, including sponsor names and their role. | ICMJE Recommendations, updated January 2026 (as R3), sections on disclosure of relationships and activities, and on sponsors. | Confirmed from the official PDF on 20 October 2026. |
| R8 | An abstract or poster displayed at a scientific meeting is a preliminary report; it does not bar a later complete report. | ICMJE Recommendations, updated January 2026 (as R3), section on overlapping publications. | Confirmed from the official PDF on 20 October 2026. The skill uses it only to treat an abstract as preliminary, not as the full study. |
| R9 | In promotional material, claims and comparisons must be capable of substantiation, and "data on file" must be supplied on request to health professionals. | Intended sources: national or regional codes of practice for pharmaceutical promotion (for example the ABPI Code of Practice for the UK; the EFPIA Code for Europe) and US FDA rules for promotional labeling. | `[CHECK]`: not read in this build. Applied only as good practice: data on file is described as unpublished company data that the reader cannot inspect. Which rules apply is for `claims-and-label` and `market-rules-and-data`, and the company's promotional review. |

### How to use these rules in output

- In what the person reads, say the practice plainly: "A preprint has not been peer
  reviewed yet. If a published version exists, cite that." Name the document only if the
  person asks why, or in a note for a reviewer ("ICMJE recommendations, January 2026").
- Never cite R2's level numbers or R9 as a requirement while they are `[CHECK]`.
- Never present GRADE or CEBM as a rule a payer, regulator or company applies unless the
  person's material says so.
- Do not extend any rule beyond what it covers. ICMJE governs journal publication; it is
  a sound reference for how to treat preprints and retractions, not a promotional code.

## Part 2: Failure patterns

Each pattern: what it looks like, why it fails, before and after, and the rule it
breaks. All examples are invented for teaching; "Tavexa", "Orvelin", "Kestrel-2" and
every figure are fictional.

Pattern ids are for this file only. In what the person reads, describe the problem in
plain words (TR-H13).

### Contents

- Kind of source S1–S4
- Strength S5–S6
- Authorship and review S7–S8
- Currency S9–S12
- Fit and chain S13–S14
- Scores and unchecked items S15–S16

### Kind of source

**S1 The press release as evidence.** A company announcement cited as if it were the
study.
Why: a press release is written by an interested party and does not show methods,
denominators or limitations. A payer or doctor will ask for the publication.
Before: "Orvelin cuts relapses by 60% (Orvelin press release, 2 May 2026)."
After: "Orvelin's maker announced on 2 May 2026 that its trial reduced relapses; the
announcement gives a 60% relative reduction and no event rates [GAP: not supplied ; 
the trial publication or results posting; supply it before using the figure]." (TR-H1,
R7)

**S2 The preprint as published.** A preprint cited with no label, as settled evidence.
Why: it has not been peer reviewed, and its numbers may change before publication.
Before: "Tavexa reduced admissions by 35% (Lee et al., 2026)."
After: "A preprint, not yet peer reviewed (Lee et al., posted 3 June 2026), reports …"
and, if a journal version exists, cite that instead. (R3)

**S3 The abstract as the study.** A conference abstract described as if the full
methods and results were known.
Why: abstracts are preliminary; final numbers often differ.
After: "Preliminary results presented at <meeting>, <date> (abstract only)." (R8)

**S4 Data on file as published evidence.** "Data on file" cited as if any reader could
check it.
Why: the reader cannot inspect it, and the company is not independent of it.
After: "Company data on file (unpublished analysis, <date>)", only when the person supplied
it or said it exists (otherwise a gap: no data on file is named), and point external use to
the promotional review process. (R9 `[CHECK]`, TR-H11)

### Strength

**S5 One study as the evidence.** "The evidence shows" resting on a single trial.
Why: certainty is judged across the body of evidence, per outcome (R1).
Before: "The evidence shows Tavexa reduces admissions."
After: "One randomized trial (Kestrel-2, 600 adults) found fewer admissions with Tavexa
than placebo at 52 weeks." (R1, TR-H1)

**S6 The upgraded design.** A registry described as proof of cause; a single-arm study
as controlled; expert consensus as evidence of effect.
Why: design sets what a study can show. Observational data shows association; expert
opinion is a view (R1).
After: name the design as the source does; "was associated with", not "reduced".
(R1; for the wording of the claim, see `grounded-statements`)

### Authorship and review

**S7 Peer review assumed or asserted.** "Peer-reviewed data" written because the source
has a DOI, looks like a journal, or the person asked for it.
Why: a DOI is given to preprints, reports and datasets too. An unverified "peer
reviewed" is an invented fact a reviewer will check first.
After: "Peer review status not confirmed: <what would confirm it>." (TR-H1, R3)

**S8 Interests left out, or "independent" assumed.** A sponsor-funded study described
as independent, or no mention of who paid.
Why: readers weigh evidence by who produced it. "Independent" with no disclosure
statement is invented.
After: "Funded by the manufacturer; two authors are employees (as disclosed in the
paper)" or "funding and interests not stated in the source". (R7, TR-H1)

### Currency

**S9 The superseded guideline.** An older guideline version quoted as current.
Why: recommendations change; the reader will check the current version.
Before: "Guidelines recommend drug D first line (Society guideline 2019)."
After: "The 2019 version of the guideline recommended … [GAP: out of date or unclear
date; whether a newer version exists; check the society's page]." (TR-H1)

**S10 The retracted or corrected paper.** A paper used after a retraction, or a figure
used that a correction changed.
Why: a retracted paper no longer supports its findings; a correction may change the
number you are quoting (R4, R5).
After: retracted: drop it as support, cite it only for the retraction. Corrected: use
the corrected figure and cite the correction.

**S11 The undated "current".** "Current standard of care", "latest data" with no date.
After: date it from the source, or `[GAP: out of date or unclear date; …]`. (TR-H1)

**S12 Another market's document.** A US label or a different country's HTA decision
used for a European payer or a Swiss doctor.
Why: label text and HTA positions differ by market.
After: name the market of the source; ask for the document for the reader's market.
(TR-H7)

### Fit and chain

**S13 The wrong fit.** A source about a different population, comparator, endpoint or
setting used for the claim.
Before: a trial in hospitalized adults used for "reduces admissions in primary care".
After: "The trial enrolled hospitalized adults; it does not cover primary care
patients." (TR-H1)

**S14 The source about the source.** A news story, review slide or press release cited
for a study's result.
Why: the chain adds errors and loses limitations.
After: cite the primary; if it was not supplied, `[GAP: not supplied; the original
study; supply it]`. (TR-H1)

### Reading results

**S15 A score or tier invented.** A source is given "86 out of 100", "gold tier" or "high
quality" when nobody computed it.
Why: no score can be worked out by hand, and a number looks like a measurement. A score
would also say nothing about whether a specific sentence matches the source.
After: describe the source (kind, peer review, funders, fit, date) and say what it can and
cannot carry; send the claim to `claim-assessment`. (TR-H3, TR-H4)

**S16 "Not checked" read as clear.** A source with no retraction check is described as
current or not retracted.
Why: no check ran on its retraction or supersession status.
After: "Currency not checked. Look at the journal's page for the article and a retraction
database, or the issuing body's page for a newer version, and tell me the date you
checked." (TR-H4)

## Part 3: Gap rules

> **Where the marker belongs.** Use the `[GAP: …]` marker only inside a drafted deliverable. In notes, open-item lists and explanations, write the gap as a plain sentence ("Still missing: …, from …"). See `trusted-capability-map/references/knowledge.md` (Part 2).

Same format and classes as every TRUSTED skill:
`[GAP: <class>; <what is missing>; <what would close it>]`

| Class | Typical case in this skill |
|---|---|
| `not supplied` | The source itself, the published version behind a press release or preprint, the funding statement, the other studies behind "the evidence shows" |
| `not checkable here` | A field or status that can only be read from a source the person has not supplied (publisher of a link that cannot be opened), or that only the person can check (retraction status, newer version) |
| `conflicting` | The preprint and the published article give different figures; two versions of a guideline say different things |
| `needs a decision` | Whether data on file or a preprint may be used for this reader, which the company's review process decides |
| `out of date or unclear date` | No date on the source; a guideline or label that may have been replaced; "current" with nothing dated |

### Mapping from by-hand results

Translate what you could not read into the classes above so every skill reads the same way.

| What happened | Class | What the person reads |
|---|---|---|
| A provenance field is missing from the source (no date, no publisher) | `not supplied` | "The source does not show its date." |
| The person gave a link you cannot open | `not checkable here` | "I could not open the link. The details are not filled in." |
| Retraction and update status were not checked | `not checkable here` | "Retraction and update status not checked: checking is yours to do. Look at the journal's page for the article and a retraction database." |
| No source was supplied for the claim | `not supplied` | "There is no source for this yet." |

### Wording rules

- Name the exact item: "the funding statement", "the publication date", "the 2024
  version of the guideline", not "more information".
- Never hint at a value inside a gap ("probably peer reviewed", "likely 2023").
- An empty field is a missing field, not a finding. "No retraction" is a finding only
  when the person reports checking the journal's page and a retraction database, with the
  date.
- "Not peer reviewed" is a finding only when the source is a kind that is never peer
  reviewed or says so. Otherwise it is "peer review status not confirmed".

## Part 4: Failure modes

Skill-specific rows for this skill. FM-08 is shared by every skill and covers Prove honesty.

| Id | Failure mode | Detection question | Documented for | Source | Status |
|---|---|---|---|---|---|
| FM-SA-01 | Press as substantiation | Was company press treated as scientific substantiation? | Sources | IFPMA 4.3 | PARTIAL |
| FM-SA-02 | Currency faked as checked | Was currency described as checked when the person did not check it? | Currency | TR-H4 | VERIFIED practice |
| FM-SA-03 | Score or tier shown | Was a tier, score or grade shown for a source? | Scoring | Owner decision of 9 November 2026 | VERIFIED practice |
| FM-08 | Hand-check result treated as world-truth | Is a hand-check result described as "true in the world"? | Prove honesty | TR-H3 | VERIFIED |
