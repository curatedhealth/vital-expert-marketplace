# A1 Traceability and design control check

Framework task: DH-03.02.1.2, Part A, task A1. Replaces the earlier "Design control check" and "Trace score" tasks (CF-12.03.02.1.2.1 and CF-12.03.02.1.2.2).

## What this task delivers

A findings list for a release, a product or a design and development file: what the person's files show against each design-control and risk-management expectation, what they do not show, and the source of each expectation. Every hazard checked, every broken link quoted. Findings, not a score: the earlier "trace score" becomes a count of findings by kind, and any grade is the person's (task B1).

Why it matters: a procedure that exists on paper proves nothing about a release. The earlier task wording said it plainly: "Do not pass because the procedure document exists." FDA investigators follow the risk file into the design records (QS31); under the MDR the risk file must take in post-market information and sits in the documentation a notified body assesses (EU15, EU23). This task does the same walk first. Cite QS31 only for a US product.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Product Development Lead (`product-development-lead`) |
| Skill | DH-03.02.1.2 Part A, Traceability and design control check |
| Workflow | The steps below |
| Knowledge | `references/check-criteria.md` (K1 to K12); `references/trace-structure.md`; `references/quality-systems-sources.md` |
| Tools | `scripts/trace_check.py` on the person's trace export. No library call is needed |
| Prompt | This guide |
| Template | `assets/design-control-check-output.md` |
| Input | The request and its context: the release or scope, the person's trace export, risk file, design and development file index, change records, the markets |
| Governance | `references/governance.md`; findings, not verdicts |

## Read the request

- **Scope.** A named release, a product, or a change. Keep to it. Ask once if the release is not named; the earlier task wording made naming the release the first step.
- **Files.** List what the person gave. Each criterion that needs a file the person did not give becomes "not checked: file not provided", never a finding against them. If the files describe a different device or intended purpose from the one in the request, say so before any finding, and route the classification question to the regulatory owner without stating a class (governance: classification statements stop for the owner).
- **Markets.** US, EU, or both; K11 is US, K9, K10 and K12 are EU.
- **Short or full.** A direct question ("does release 4.1 trace?") gets short mode. "Audit prep", "full", "for the notified body" gets full mode.

## Workflow

### Step 1. Run the trace checks

Map the person's columns to `id, type, links, text, result` and say how. Run `python3 scripts/trace_check.py trace.csv` (or `--json`). Without code execution, apply checks G1 to G7, O1 to O3, R1 and R2 by hand. G7 (design input with no design output) is a working-convention check; say so. For each finding, quote the broken link: the item id, what it links to, and what is absent.

### Step 2. Walk every hazard

For every hazard in the risk file, follow hazard to control to verification of implementation to, where the file records it, verification of effectiveness. Mark each link traced, broken (quote it), or not in the files provided. Do not sample only the hazards that trace (earlier task wording). If the person asks for a sample, say how it was drawn and include hazards that do not trace.

### Step 3. Check the controls' order and disclosure

For each hazard controlled only by information for safety, look for the recorded reason a design control was not feasible (K7, EU16). For residual risks, look for disclosure to users (EU16).

### Step 4. Check the criteria that need other files

Go through K1 to K12 in `references/check-criteria.md` for the markets in scope. For each: the expectation with its row, what the person's file shows, and the finding. Typical findings: software validation record not referenced in the design and development file (K2, K4); software change implemented before its risk assessment (K5); a US software change with no recorded 510(k) assessment against the risk file (K11); risk file not updated after a complaint described a new failure (K6, QS22).

### Step 5. Count, do not score

Report counts by finding code and by criterion. Do not turn them into a percentage or a pass mark. If the person has written their own pass rule (for example "every hazard traces to a verified control"), state whether the files meet that rule, with the number behind it, and say the rule is theirs. The earlier fail conditions, "a hazard with no control, or a control with no verification", are G4 and G5; report them first.

## Build the output

Follow `assets/design-control-check-output.md`. Short mode: the scope, counts by kind, the hazard-trace findings first, then the rest. Full mode: every finding with its criterion, row and quoted link.

Short mode: 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections; offer the full version in one line.

## Before you hand it over

- Short mode: count the words, excluding tables' source column and any 'Calls made' log; if over 450, cut in the stated order before sending.
- Every finding names the item or document from the person's files, and the row behind the expectation.
- "Not in the files provided" is used for anything not given, never "missing".
- No score, no grade, no compliance verdict. Grades are the person's (B1).
- Anything that will be filed as an audit record stops for the owner. If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft. AI-assisted draft.

## Boundaries

- The model checks files; it does not audit people or teams.
- No clause text from ISO 13485 or ISO 14971 beyond what the rows restate.
- Device class and pathway are the regulatory owner's.
