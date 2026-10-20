# A1 Document check

Framework task: DH-03.02.2.2, Part A, task A1. Replaces the earlier "Document check" and "Document score" sections (the scoring moves to B1, where people score).

## What this task delivers

A findings table for the person's document and record set: each required record (from sourced rules and from the person's own procedures) marked present and current, present but not current, missing, not applicable with the reason, or not assessable `[GAP]`; plus every version and citation problem (two versions marked current, an obsolete copy in the working set, a submission citing a superseded version). It answers "what is missing or wrong in our documentation, against what the rules require?"

Why it matters: since 2 February 2026 FDA inspects against the QMSR, and management review, internal audit and supplier audit reports are inspectable (QS15) and expected to be readily available (QX8). A gap found by the company is a repair; the same gap found by an investigator is an observation.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | QA Manager, Software (`quality-assurance-manager-software`) |
| Skill | DH-03.02.2.2 Part A, Document check |
| Workflow | The steps below |
| Knowledge | `references/required-records.md`; `references/QUALITY_SYSTEMS.md`; `references/supplementary-rows.md` |
| Tools | None. The person's documents never go into a library call |
| Prompt | This guide |
| Template | `assets/document-check-output.md` |
| Input | The request and its context: document list or folder export (id, title, version, status, owner, approver, dates, location), device class, markets, the procedure list, any submission or technical file and the versions it cites |
| Governance | `references/governance.md` |

## Read the request

- **The set.** Which documents are in scope (whole QMS, one product's design and development file, the technical file, the inspection-readiness set). Name the set you check; the check is only as wide as the list.
- **Markets and class.** These decide which lines of `required-records.md` apply (for example US-R2 only for class II, III, or class I with software, QS9).
- **The list's date.** Every finding is "as of" the date of the list the person gave.
- **Mode.** "Are we missing anything for the inspection?" gets short mode. A readiness pack gets full mode.

## Workflow

### Step 1. Build the expected list

Take the lines of `required-records.md` that apply to the markets and class. Add the record types the person's own procedures name; those come from the person, cited to their procedure id. Say once that ISO 13485 records beyond FDA's and the MDR's restatements are checked only through the person's procedures, because the clause text is not sourced.

### Step 2. Match

For each expected line, find the matching documents in the list. Classify:

| Class | When |
|---|---|
| Present, current | One current version, owner and approver recorded |
| Present, problem | Two versions marked current; no approver; obsolete copy in the working set |
| Missing | Expected and not in the list |
| Not applicable | The condition in "applies when" does not hold; give the reason |
| Not assessable `[GAP]` | The list lacks the field needed (no version, no status) |

Do not infer content from a title. A file named "Management review 2026" shows the record exists, not that it covers what the procedure requires; say "content not checked" unless the person shares it.

### Step 3. Version and citation check

For every submission, technical file or design and development file the person shares, list each cited document and version, and compare with the current version in the list. A citation of a superseded version is a finding even if the right file also exists (pack method, `required-records.md`).

### Step 4. Pre-QMSR records

If records created before 2 February 2026 are in scope, note FDA's suggestion of a comparative analysis showing they meet the QMSR (QS26). It is a suggestion, not a requirement; say so.

### Step 5. Context, labeled

If the person asks where inspectors look, add the FY 2025 citation counts from `required-records.md` (QS52 to QS54) with their limits: counts under the retired QS regulation numbering, not a complete list of observations (QS51), not a prediction.

## Build the output

Follow `assets/document-check-output.md`. Answer first: how many expected lines were checked, how many are missing or have problems, and the two or three findings that most need the person's attention by the facts (missing records the rules require, wrong citations in a filed document). Do not score or rank beyond that; scoring is B1. Short mode: 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections; offer the full version in one line.

## Before you hand it over

- Every expected line cites its row or the person's procedure id.
- No finding claims a document's content was checked when only its title was seen.
- No statement that the set "complies" or "passes".
- The list's date is on the output.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Checks presence, currency and citations. It does not review the content of procedures against ISO 13485.
- Setting up document control is the sibling skill's A1.
- Repairs and owners are B1.
