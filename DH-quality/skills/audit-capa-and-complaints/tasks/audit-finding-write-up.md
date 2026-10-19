# A1 Audit finding write-up

Framework task: DH-03.02.4.1, Part A, task A1. Replaces the earlier "Audit finding" section.

## What this task delivers

One or more audit findings written so they hold up when a regulator reads them: the requirement, the evidence, the gap, a proposed grade with the criteria behind it, and the owner the person names. It answers "how do I write this finding, and how serious is it under the rule we use?"

Why it matters: under the QMSR, FDA can read internal audit reports (QS15). A finding that mixes opinion with evidence, cites no requirement, or carries a grade nobody can trace will not survive that reading.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | QA Manager, Software (V&V) |
| Skill | DH-03.02.4.1 Part A, Audit finding write-up |
| Workflow | The steps below |
| Knowledge | `references/audit-and-grading.md`; rows QS15, QS16, QS28 to QS35, QS44 to QS49, EU25, R1 to R8 |
| Tools | None required. No library call |
| Prompt | This guide |
| Template | `assets/audit-finding-output.md` |
| Input | The request and its context: the audit type (internal, supplier, MDSAP, notified body, FDA prep), the observation, the records seen, the person's procedure and grading rule |
| Governance | `references/governance.md`; the grade is the person's or the auditor's |

## Read the request

- **Audit type.** Internal, supplier, MDSAP, notified body, or preparation for an FDA inspection. It decides which grading rule applies. Ask if unclear.
- **Grading rule.** The person's procedure (number and rule), or the MDSAP scale if their procedure adopts it. If neither is given, show the MDSAP criteria as reference and say no grade can be proposed under their own rule until they give it.
- **The observation.** What was seen, which records, which dates. Opinions are separated from facts.
- **Mode.** One finding as a direct question gets short mode. A full audit write-up gets full mode.

## Workflow

### Step 1. Separate evidence from opinion

From the person's notes, list what was seen: record ids, dates, versions, sample sizes, interviews. Move any judgment ("poor", "inadequate", "lack of culture") out of the evidence column. If a fact is missing, write `[GAP]` and ask; never fill it.

### Step 2. Name the requirement

Cite the requirement by its source: a CFR section or MDR article from the rows, an ISO 13485 clause number as a regulator names it (QS8, QS9, QS17, QS19, QS33, QS34, R8), or the person's own procedure with number and revision. Do not quote ISO clause text. Where the person's procedure is stricter than the regulation, cite the procedure; the gap is against what the organization committed to.

### Step 3. State the gap

One or two sentences: the difference between the requirement and the evidence. No cause, no remedy. Causes belong to B1.

### Step 4. Propose a grade, if a rule applies

- **MDSAP scale (if adopted).** Ask the four questions in `audit-and-grading.md` section 2 and record each answer with its basis: QMS impact (direct 3 or indirect 1, by clause per QS46), repeat in the two previous audits of the same sub-clause within three years (QS47, R3), missing procedure combined with failure to implement (only when both, R4), release of nonconforming devices (not if released under justified concession, R5). Sum, cap at 5 (R1). Label the result "proposed grade" with the arithmetic shown.
- **The person's own rule.** Apply it as written and show which condition decided it.
- **No rule.** Give the facts per criterion and no grade.

The old "major or minor" split is only used if the person's procedure uses it. MDSAP grading goes beyond it (QS44).

### Step 5. Check notice rules

For an MDSAP audit, count grade 5 and grade 4 findings in the set: one or more grade 5, or more than two grade 4, means the auditing organization informs the regulators within 5 working days, and the full package is due before day 45 instead of day 90 (QS48, QS49). These obligations are the auditing organization's, not the manufacturer's. For an internal audit, say these rules do not apply.

### Step 6. Map it to the FDA inspection areas (for inspection prep)

If the audit prepares for an FDA inspection, place each finding in one of the six QMS areas or four other requirements of CP 7382.850 (R6), and note that complaint handling, internal audits and corrective action are minimum elements in model 2 (QS33). Say which inspection model the person's situation points to only from R7, and that the figure should be checked.

### Step 7. Owner and next step

Record the owner the person names; if none, "owner not named". The next step is a CAPA plan (B1) or a recorded decision that no action is needed, which is the person's call. Grades are not changed by later fixes (R2).

## Build the output

Follow `assets/audit-finding-output.md`. Answer first: the finding in one sentence and the proposed grade (or "no grade: rule not given"). Then the requirement, evidence and gap table, the grading arithmetic, notice rules, and owner.

## Before you hand it over

- Evidence holds only facts, each with its record id or date.
- Every requirement has a source; no ISO clause text is quoted.
- The grade is labeled "proposed" and the arithmetic is shown, or no grade is given.
- No cause and no fix appear in the finding.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- The model does not grade; it computes a proposal from the person's answers.
- No legal reading of a 483, a warning letter or a notified body decision; point to the person's regulatory owner.
- Complaints go to A2, not into an audit finding.
