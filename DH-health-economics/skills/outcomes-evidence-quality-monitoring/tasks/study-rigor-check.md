# A1 Study rigor check

Framework task: DH-01.07.3.2, Part A, task A1. Replaces the earlier "Study rigour check" section (CF-12.01.07.3.2.1).

## What this task delivers

A fact sheet for one study result, ready for the person's reviewers to judge: the design read from the paper, the tool that applies (ROBINS-I, RoB 2, or RoB 1 for an EU JCA), the facts per bias domain with their locators, data fitness under one named framework, whether the plan was fixed before outcomes were seen, registration, retraction and currency, funding and conflicts as stated. It answers "what are the facts that decide how much weight this result can bear?"

Why it matters: a rigor judgment is only as good as the facts under it. Reviewers who see the facts per domain, with the page they came from, judge faster and disagree less. Laying out facts, not verdicts, keeps the judgment where it belongs (ES-73).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Clinical Trials Director |
| Skill | DH-01.07.3.2 Part A, Study rigor check |
| Workflow | The steps below |
| Knowledge | `references/rigor-checks.md`; ES, CV and HE rows |
| Tool | `literature.get_record`, `literature.classify_study` (cross-check), `literature.find_trial`, `literature.check_retraction`, `verify.check_currency`, `literature.grade_evidence` (draft context only); `verify.qualify_source` and `verify.check_claim` when a fact is restated outside the conversation |
| Catalogue job | `evidence-table` (available) for a tabular view of several papers; it does not assess bias |
| Prompt | This guide |
| Template | `assets/study-rigor-check-output.md` |
| Input | The request; the paper (DOI, PMID or file) or study report; which result; the audience (internal, NICE, EU JCA, payer) |
| Governance | `references/governance.md`; reviewers judge, the model lays out facts |

## Read the request

- **Which result.** Name the outcome, timepoint and population. One study can need several checks.
- **Which audience.** It decides the tool (RoB 1 for EU JCA randomized results, ES-163) and the data framework.
- **Full text.** Needed. If the source is open access, read the full text before marking any field `[GAP]`. Only when no full text is available, say the domain facts are not checkable and stop at Step 2.
- **Own study.** If it is the person's own study, ask for the protocol and the A2 execution log from `real-world-outcomes-research`.

## Workflow

### Step 1. Resolve the paper

`literature.get_record {doi | pmid | pmcid}`. Note PMCID and `oa_url`; open the full text. Record title, venue, year, DOI.

### Step 2. Read the design from the paper

From the methods section, state design, comparator (concurrent or historical; ES-78 covers uncontrolled before-after studies only. For a historical comparison group, state the comparison period as a confounding fact without citing ES-78), data source, period, adjustment method and analysis population, each with a locator. Then call `literature.classify_study {record}` and show its label beside yours; if they differ, say so (register N8).

### Step 3. Pick the tool and lay out facts per domain

Use `references/rigor-checks.md` section 1 to pick the tool, and say why. For each domain (section 2, 3, or 3a for RoB 1 in an EU JCA), fill the facts listed in section 4 with quotes and locators. Where the paper is silent, write "Not reported `[GAP]`". Add the questions the sources raise for this design: uncontrolled before-after designs (ES-78; not a historical comparison group), confounding (ES-79), immortal time when "users" are defined by later use (ES-82, V2 draft question). For RoB 1, list all seven domains (ES-171) and show beside each the Low, High and Unclear criteria with their rows (ES-180 to ES-187); state "no information" explicitly where the paper is silent (ES-174). RoB 2 remains Cochrane's current tool (ES-69). Do not judge; leave the level column for the reviewers.

### Step 4. Data fitness and prespecification

Apply one framework (section 5) and say which. Then prespecification (section 6): protocol and plan available and dated, registration (`literature.find_trial {record}`; "no linked registration found" is not "unregistered"), stated changes after outcome access, subgroup status (ES-87).

### Step 5. Currency and trustworthiness

`literature.check_retraction {doi}` and `verify.check_currency {doi}`; name the source checked (Crossref). Note comments or corrections if the person has them (ES-122). Funding and conflicts as the paper states them (HE-014 for economic evaluations; ES-42).

### Step 6. Context the reviewers will want

Reporting completeness against STROBE item numbers or CHEERS items, as gaps, never as a score (CV123, HE-005). The GRADE starting point for the design (ES-90, ES-100), and the library's draft level labeled as a draft (`literature.grade_evidence {record, standard: "grade"}`).

## Build the output

Follow `assets/study-rigor-check-output.md`. Short mode: the answer (design as read, tool, the two or three domains where the facts raise the most questions, prespecification status), one domain table with facts and an empty reviewer column, at most three open items, the record line. Full mode adds data fitness, currency, funding, reporting gaps, GRADE context and the calls list.

## Before you hand it over

- Every fact carries a locator in the paper; nothing comes from the library label alone.
- The level column is empty or filled only with the reviewers' judgments, labeled as theirs.
- No "high quality", "robust" or "weak" verdict from the model.
- Every [PAPER] row carries its DOI beside the row id (ES-75: 10.1136/bmj.i4919).
- Every conflict line the paper states is quoted with its locator (employees, shareholders, paid consultants).
- The record line ends the answer: "Clears it: [the person named, in their words, or owner not named]. The record is built with verify.build_record once that named person clears it; until then, uncleared draft."

## Boundaries

- No domain judgment, no certainty rating, no dossier decision.
- Running a full systematic review is dh-clinical-validation `literature-and-real-world-evidence-review`.
- Economic model validity is dh-health-economics 2.2.
