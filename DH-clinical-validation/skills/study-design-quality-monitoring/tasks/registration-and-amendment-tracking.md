# A2 Registration and amendment tracking

Framework task: DH-01.02.1.2, Part A, task A2. Replaces the second half of the earlier "Protocol Robustness Monitoring" section (watching the protocol hold up over time).

## What this task delivers

For one trial, the public record set beside the protocol and the paper: the registry entry linked through the library, the registered primary outcome against the protocol's and the publication's wording, masking and enrollment, the registration and results clocks with whether each applies, and a log of what changed between protocol versions the person supplies. Every difference is reported as a difference with the row that makes it worth reading.

Why it matters: a registry that disagrees with the protocol or the paper is the first thing a journal, an HTA body or a regulator checks. Changes after a trial starts must be reported with reasons (CV114), and ICMJE counts only registration at or before first consent (CV132).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Clinical Informatics Lead (`clinical-informatics-lead`) |
| Skill | DH-01.02.1.2 Part A, Registration and amendment tracking |
| Workflow | The steps below |
| Knowledge | `references/registration-and-reporting-clocks.md`; `references/robustness-signals.md` (registration and consistency signals); SP-2, SP-4, SP-16, SP-31, CV113, CV114 |
| Tools | `literature.find_trial`; ClinicalTrials.gov record read; `scripts/registry_check.py`; `verify.qualify_source` then `verify.check_claim` for the paper's outcome sentence |
| Prompt | This guide |
| Template | `assets/registration-tracking-output.md` |
| Input | The request and its context: NCT id or paper (DOI, PMID), the protocol's primary outcome text and version, first consent date if known, whether the trial is an applicable clinical trial (or unknown), protocol versions to compare |
| Governance | `references/governance.md`; registry updates and results postings stop for the owner |
| Catalogue job | none |

## Read the request

- **Which trial.** An NCT id, or a paper. If only a product name, ask for the registry id or the paper; do not search the person's unpublished trial by name without their say.
- **Their facts.** The protocol's primary outcome text and version, the first consent date, applicability (ACT yes, no or unknown), target enrollment, masking.
- **Versions.** If they want amendments tracked, ask for the versions with dates (SP-2) or their amendment list.

## Workflow

### Step 1. Link paper and registration

If the person gave a paper, call `literature.find_trial {record: {doi, pmid, pmcid, title}}`. If they gave an NCT id, call `literature.find_trial {nct_id}` to get the linked publications. Library records carry no `trial_ids`, so this is the only library route (N8). "No linked registration found" is `[GAP]`, never "unregistered": other registries are not reached (CV134).

### Step 2. Read the registry record

Read `https://clinicaltrials.gov/api/v2/studies/<NCT id>` (or the record page) on the read date. With code execution, save it and write the person's facts as JSON (fields in the script's help), then run `python3 scripts/registry_check.py --registry FILE.json --facts FACTS.json --as-of YYYY-MM-DD`. It reports registration timing, the 21-day, one-year and 12-month clocks with their applicability, and the primary outcome comparison.

### Step 3. Read the paper's outcome sentence

If a publication exists, take its sentence stating the primary outcome (full text or the person). Check it with `verify.qualify_source {doi, question}` then `verify.check_claim` (claim, passage `{text, locator}`, full source object). Report it only after reading the passage yourself (N3).

### Step 4. Compare

Set registry, protocol and paper side by side for the primary outcome (variable, metric, aggregation, time point, SP-16), secondary outcomes, masking and enrollment. Mark each pair "same", "worded differently" or "not stated". Use `references/robustness-signals.md` for the row behind each difference. Never call a difference a change until the registry history or the amendment log shows one; read the History of Changes on the registry page.

### Step 5. Clocks

From `references/registration-and-reporting-clocks.md`, list each clock with its facts, the days counted by the script, and whether it applies (person's answer or `[GAP]`). State them as facts with the instrument; no urgency.

### Step 6. Amendment log

If the person supplied versions or an amendment list: for each change, record the version, date, items affected (by SPIRIT item), whether it touches the primary outcome, estimand, sample size or analysis, whether it came after first enrollment, and whether a reason is documented (CV114, SP-31). The person decides what each change means.

## Build the output

Follow `assets/registration-tracking-output.md`. Answer first: registered before the reference date or not, which clocks apply and where they stand, and the most important difference between documents. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every registry fact carries its read date; every paper fact its locator.
- Applicability of each clock is the person's or `[GAP]`, never assumed.
- Differences are differences; no "switching", no intent.
- Registry updates, results postings, extension requests stop for the owner.
- Each [PAPER] paper cited has its DOI once in prose, and beside its row id in every table.
- The record line ends the answer: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Fixing the registry or protocol: the owner, with the design skill for wording.
- Grading the paper or assessing bias in its results (review method): `dh-clinical-validation` literature-and-real-world-evidence-review (DH-01.02.4.1).
- Regulatory reporting duties beyond the rows here: `dh-regulatory-strategy` regulatory-submission-and-dossier.
