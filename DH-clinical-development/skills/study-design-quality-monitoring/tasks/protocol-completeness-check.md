# A1 Protocol completeness check

Framework task: DH-01.02.1.2, Part A, task A1. Replaces the first half of the earlier "Protocol Robustness Monitoring" section (checking the protocol text the buyer supplied).

## What this task delivers

An item-by-item reading of the person's protocol against the 34 SPIRIT 2025 items and the additional duties the digital, decentralized, AI and estimand rows trigger: each item addressed (with its locator), partly addressed (naming the missing part), stated not relevant, missing, or not checkable. Plus the standards the protocol cites that have been superseded. The person sees exactly what is open before ethics submission.

Why it matters: SPIRIT 2025 asks for every item to be addressed before ethics submission, with non-applicable items stated explicitly (CV117). Silence is the most common gap, and reviewers read silence as an omission.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Clinical Informatics Lead (`clinical-informatics-lead`) |
| Skill | DH-01.02.1.2 Part A, Protocol completeness check |
| Workflow | The steps below |
| Knowledge | `references/spirit-2025-checklist.md`; `references/completeness-rules.md`; `references/protocol-rules.md`; `references/estimand-and-sap-rules.md` |
| Tools | None. The check runs on the protocol text |
| Prompt | This guide |
| Template | `assets/completeness-check-output.md` |
| Input | The request and its context: the protocol text and version (SP-2), the SAP if separate, which features apply (DHT endpoints, remote visits, AI, RWD, US or EU sites) |
| Governance | `references/governance.md`; the protocol owner decides what to change |
| Catalogue job | none |

## Read the request

- **The text.** Work only on the protocol the person supplies. If they supply part, check that part and mark the rest "not checkable".
- **Version.** Note the version and date (SP-2); later comparisons depend on it.
- **Triggers.** Which rows apply depends on the trial: ask only if the text does not say (DHT endpoints, remote visits, eConsent, AI, RWD, US or EU sites, device or not).
- **Focus.** "Before ethics" means all items; "check our data section" means items 25 to 27 and their triggered duties.

## Workflow

### Step 1. Item by item

For each SP- row, find the protocol passage that addresses it and record the locator. Mark per `references/completeness-rules.md` section 1. Read multi-part items closely (section 2): an outcome without its time point is partly addressed.

### Step 2. Triggered duties

From the person's facts and the text, decide which triggers in `references/completeness-rules.md` section 3 apply. For each, mark addressed, partly, missing or not checkable, with the row.

### Step 3. Estimand and statistics presence

Check that a primary estimand is defined and the main estimator and a sensitivity analysis are prespecified (CV40), and that missing data handling refers to the estimand (CV41). Check presence only; whether the choices are right is for the owner the person names for statistics, or owner not named.

### Step 4. Superseded citations

Check the protocol's references against section 4 (SPIRIT 2013, E6(R2), the 2017 device RWE guidance, the December 2022 EU DCT paper, the 2023 FDA DCT draft). Report the current version with its row.

### Step 5. Count and order

Count addressed, partly addressed, stated not relevant, missing and not checkable. List missing and partly addressed items in dependency order (for example the estimand before missing data handling; the endpoint definition before sample size). Do not turn counts into a score or a verdict; a verdict needs the person's rule (B1).

## Build the output

Follow `assets/completeness-check-output.md`. Answer first: the counts, and the missing items that block the most. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every "addressed" has a locator; every "missing" names the item and its row.
- Silence is never marked "not relevant".
- No score, no "complete", no "compliant". The output is "completeness check of protocol VERSION, draft for OWNER".
- Each [PAPER] paper cited has its DOI once in prose, and beside its row id in every table.
- The record line ends the answer: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Writing the missing sections: the design skill (DH-01.02.1.1, A2 and B1).
- Whether the design choices are sound: B1 against the person's rules, and the owner the person names for statistics, or owner not named.
- Ethics or regulatory acceptability: the accountable owner.
