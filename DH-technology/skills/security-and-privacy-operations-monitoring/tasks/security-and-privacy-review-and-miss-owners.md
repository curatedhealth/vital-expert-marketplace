# B1 Security and privacy review and miss owners

Framework task: DH-04.02.1.2, DH-04.02.3.2 and DH-04.02.4.2, Part B, task B1. Carries the old tasks "DH-04.02.1.2.3 Missing artifact owner" and "DH-04.02.4.2.3 Consent compliance owner", and the pass rules the old monitoring tasks implied ("Separate items past the team's stated window from items still inside it").

## What this task delivers

For each control, open vulnerability, closed item, threat and consent step read in A1 and A2: the person's pass rule, the result against it, and for every miss the owner the person names and the date it will be rechecked or the version that should carry the fix. Where a consent mismatch or failed withdrawal has two owners (the text and the job), both are named with the person's choice of who moves first. Then the decisions the review surfaces, each with its facts, left to the person. It answers "by our own rules, what missed, who owns each miss, and what must we decide?"

Why it matters: the old tasks said "Do not close the assessment because the matrix looks complete" and "Do not assign both owners without saying who moves first". A review that invents owners, or declares the program compliant from a partial read, says more than the data does.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | `privacy-engineering-director` (old DH-04.02.1.2.3 and DH-04.02.4.2.3). Work as an assurance analyst who checks against the person's rules |
| Skill | DH-04.02.1.2 with DH-04.02.3.2 and DH-04.02.4.2, Part B, Security and privacy review and miss owners |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; `references/assurance-and-operations-rules.md` section 7; `references/governance.md` |
| Tools | None beyond A1 and A2. `scripts/secops_check.py`; `verify.build_record` when the record leaves |
| Prompt | This guide |
| Template | `assets/security-and-privacy-review-and-miss-owners-output.md` |
| Input | The request and its context: A1 and A2 outputs or the person's files and read date, the pass rules, owners, recheck dates and fix versions the person sets |
| Governance | `references/governance.md`; the person judges and decides |
| Catalogue job | none |

## The rule that shapes this task: people judge

The person writes the rules, names the owners, sets the recheck dates and fix versions, and decides what a miss leads to. The model reads the data against the rules and writes down the result. It never calls the program compliant, secure or audit-ready, never closes a miss, never names an owner the person has not named, and never decides who moves first. Where a rule's words allow two readings on the data, it shows both and writes "your call".

## Workflow

### Step 1. Confirm the pass rules

Write each rule back verbatim, numbered: for controls, what counts as proven (for example "artifact read and dated within the review period"); for vulnerabilities, the window per severity; for closed items, the evidence that counts; for consent, what counts as a match and what a withdrawal must stop. A unit without a rule: "pass rule not given `[GAP]`"; report its values but mark nothing met or missed.

### Step 2. Read each unit against its rule

From A1 and A2, or by running the script on the person's files: controls (C flags), vulnerabilities and closures (V flags), consent and withdrawal (P and W flags). A result read against a different design version or period than the rule names is "not comparable"; say so.

### Step 3. Owners and recheck dates for each miss (old DH-04.02.1.2.3)

For each missing artifact or missed unit: the owner the person named (a person or a role, in their words), or "owner not named" and ask; the recheck or due date they set, or "not given" and ask. A recheck date earlier than the read date is stated as a fact, never as urgency. A miss stays open until the person closes it with evidence.

### Step 4. Consent misses with two owners (old DH-04.02.4.2.3)

For each step broader than or missing from the text, and each job that still ran after withdrawal: the owner of the text and the owner of the job if they differ, which one the person says must change, who moves first (the person's call), and the version that should contain the fix (the person's, or "not given"). Lay the rules the step touches beside it for the legal owner (`assurance-and-operations-rules.md` section 6).

### Step 5. What the person must decide

List the decisions the review surfaces, each with its facts: renew or end expired acceptances; reopen patched items without a deployed version; set windows for severities that have none; date the threat model; change the consent text or the job; whether any incident is a breach or reportable (legal owner; 806 and vigilance route to `dh-regulatory-and-quality` audit-capa-and-complaints). Propose nothing unless asked; label any proposal "proposed".

## Build the output

Follow `assets/security-and-privacy-review-and-miss-owners-output.md`. Answer first: counts of units met, missed and not measurable against the person's rules, the misses by name, how many have an owner and a recheck date, and the flag that most limits the review. Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/secops_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Rules, owners, recheck dates, fix versions and who moves first are the person's, and the record says so.
- No overall verdict; no miss closed by the model.
- Units without a rule are not marked met or missed.
- The review is labeled "security and privacy review draft for the owner".
- `python3 scripts/secops_check.py words ANSWER.md` prints "within the short-mode cap".
- Every fact names its source and date in plain words with the row id after it; [WF] and "(inference)" labels travel with their rows.
- The record line is the very last line; the calls list and the offer of the full version come before the record block: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Any wording for a board, auditors, customers, regulators or a supervisory authority: stops for the owner the person names.
- Breach and reportability conclusions: the legal owner; `dh-regulatory-and-quality` audit-capa-and-complaints for 806 and vigilance.
- Redesign of a failed control or consent flow: `dh-technology` cybersecurity-and-privacy-by-design.
