# A1 V&V completeness and compliance read

Framework task: DH-04.03.2.2 with DH-04.03.4.2, Part A, task A1. Carries the old tasks "DH-04.03.2.2.1 Trace from hazard to case", "DH-04.03.2.2.2 Build under test", "DH-04.03.4.2.1 Class versus hazard check" and "DH-04.03.4.2.2 Plan completeness" as steps.

## What this task delivers

For one release candidate, as of a read date the person gives: every hazard in the person's risk file traced to its verification and validation cases, the cases run on a build other than the candidate, failed or unrun cases, vague expected outputs, the class statement read against the hazard as the person recorded both, and the plans the person's procedure requires checked for presence and product. It answers "is our V&V evidence complete for this candidate against our own lists, and where are the holes?"

Why it matters: validation status must be re-established after any change (EN-008), and design and development software validation is a minimum element of FDA's inspection model 2 since 2 February 2026 (QS33). A trace that counts unit tests which never exercise the hazard, or carries a pass across a changed build, looks complete and is not.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | `clinical-algorithm-validator` (old DH-04.03.2.2.x and DH-04.03.4.2.x). Work as a V&V analyst who reads the person's records against the person's lists |
| Skill | DH-04.03.2.2 Part A, V&V completeness and compliance read |
| Workflow | The steps below |
| Knowledge | `references/monitoring-rules.md` section 1; the research files |
| Tools | `scripts/delivery_check.py trace` and `plans`; `regulatory-dh.get_authorization` only to quote the person's clearance when they give its number; `verify.build_record` on sign-off |
| Prompt | This guide |
| Template | `assets/vv-completeness-and-compliance-read-output.md` |
| Input | The request and its context: product, release candidate build id, read date, hazard list and case records (CSV columns in `scripts/delivery_check.py`), the plan register, and, only if the person gives it, the class their procedure treats as lowest |
| Governance | `references/governance.md`; rules, thresholds and judgments are the person's |
| Catalogue job | none known (needs a live check) |

## Read the request

- **Candidate and read date.** Both needed. If either is missing, ask; write "not given" and do not use today's date.
- **Rules.** If the person has a pass rule for trace completeness ("every hazard has a passing case on the candidate build"), write it verbatim. Without one, report counts and flags and mark nothing pass or fail.
- **Short or full.** "Is our trace complete?" is short mode. "Full V&V completeness report" is full mode.

## Workflow

### Step 1. Header

Product, candidate build, read date, the person's rule (verbatim or "not given"). If the person gives a clearance number, quote the record (`references/tools.md`); the record holds no software version.

### Step 2. Trace from hazard to case (old 2.2.1)

Run `python3 scripts/delivery_check.py trace --hazards H.csv --cases C.csv --candidate BUILD`. Report T1 (no case: an open gap), T2 (only unit-level cases: old rule "Do not count a unit test that does not exercise the hazard"; whether they do is the person's call), T4 (failed or not run), T5 (expected output "works correctly" or blank, quoted). Cases pointing at hazard ids not in the list are shown as written.

### Step 3. Build under test (old 2.2.2)

From the same run: T3 lists cases run on a build other than the candidate with no waiver. Old rules: compare build ids with the candidate; require each to be repeated or explicitly waived (by the person they name); never carry a pass across a build that changed the hazardous function (EN-008, EN-009). A waiver is shown verbatim; whether the build changed the hazardous function is the person's fact.

### Step 4. Class versus hazard (old 4.2.1)

Read the class and hazard as the person recorded them. T6: class not given, or never tied to a hazard. T7 only if the person names the class their procedure treats as lowest (`--lowest-class`): an item they mark as able to influence a clinical action carrying that class is listed for them. Old rule: never confirm a class from a document title. The model never reclassifies; IEC 62304 class definitions are not in the sources (`[GAP]`).

### Step 5. Plan completeness (old 4.2.2)

Run `python3 scripts/delivery_check.py plans --register P.csv --product NAME` on the plans the person's procedure requires. L1 missing, L2 draft, L3 template not filled (old rule: do not score a template not filled for this product), L4 names another product. The script reads titles and statuses; it does not open documents. Say so.

## Build the output

Follow `assets/vv-completeness-and-compliance-read-output.md`. Answer first: hazards with no case, hazards covered only by unit-level cases, cases on another build, failed or unrun cases, plans missing or naming another product, and the flag that most limits the read. Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/delivery_check.py words ANSWER.md`; without code execution, count the same way by hand. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- No coverage threshold, no "complete" or "incomplete" verdict unless the person's own rule says what complete means.
- No item reclassified; T7 stated as the person's facts.
- Every rule names its source and date in plain words with the row id after it.
- `python3 scripts/delivery_check.py words ANSWER.md` prints "within the short-mode cap".
- The record line is the very last line; the calls list and the offer of the full version come before the record block: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Writing new cases or a V&V plan: `medical-software-lifecycle-and-delivery` (this pack), task A2.
- Risk file and design review health: `dh-regulatory-and-quality` design-control-and-risk-monitoring.
- Release gate and miss owners: task B1 of this skill.
