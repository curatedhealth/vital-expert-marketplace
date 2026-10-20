# B1 Governance review and miss owners

Framework task: DH-01.04.1.2, Part B, task B1. Carries the old task "DH-01.04.1.2.3 Governance miss" (name the owner; state whether release waits; name the date the item will be present; never ship the model while a failed item is open) and the pass-or-fail step of "DH-01.04.1.2.2 Release score" as steps 1 to 4. The owner, the release-waits call and the date are the person's.

## What this task delivers

For one release as of the read date: the person's pass rule written back, the items that fail it, and for each failed item the owner the person names, whether release waits, and the date the item will be present, or "not given"; the computed count of items that would have to become present; and the decisions the person faces. It answers "by our own rule, what failed, who owns each miss, and does release wait?"

Why it matters: the old task says a model does not ship while a failed item is open. A review that names owners the team never named, or closes an item because a policy exists, says more than the evidence does.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | `ai-ml-governance-director` (old DH-01.04.1.2.2 and .3). Work as an AI governance analyst who checks against the person's rule |
| Skill | DH-01.04.1.2 Part B, Governance review and miss owners |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; `references/release-evidence-requirements.md`; `references/governance.md` |
| Tools | `scripts/evidence_check.py review`; `verify.build_record` when the record leaves |
| Prompt | This guide |
| Template | `assets/governance-review-and-miss-owners-output.md` |
| Input | The request and its context: A2 output or the index, release version, read date, the pass rule and the date it was written, owners, release-waits calls and present-by dates the person sets |
| Governance | `references/governance.md`; release go or no-go is the person's |
| Catalogue job | none |

## The rule that shapes this task: people judge

The person writes the pass rule before the read, names the owners, decides whether release waits and sets the dates. The model reads the index against the rule and writes down the result. It never decides that the release is compliant or ready, never names an owner the person has not named, never sets a date, and never closes a failed item. Where the rule's words allow two readings on the data, it shows both and writes "your call".

## Workflow

### Step 1. Confirm the pass rule

Write it back verbatim with the date it was written ("every applicable item present", or a listed set). A rule written after the read is stated as a fact. No rule: "pass rule not given `[GAP]`"; report A2 statuses and mark nothing failed.

### Step 2. Apply it

`python3 scripts/evidence_check.py review --index FILE --release VERSION --as-of YYYY-MM-DD --pass-rule "all applicable" --rule-date DATE` (or `"listed:R02,R05"`). Missing and not-assessable items in the rule's scope fail it; not-yet-applicable items do not, and their dates are listed. The script prints the count of items that would have to become present and assessable for the rule to be met: quote it, never estimate it.

### Step 3. Owners, release waits and dates for each failed item

For each failed item: the owner the person named, in their words (or "owner not named"; ask), whether release waits (the person's yes or no, or "not given"), and the present-by date (the person's, or "not given"). A present-by date earlier than the read date is stated as a fact, never as urgency. Where release does not wait on a failed item, write the person's call and the old task's rule beside it as a fact for the person: "the old task said the model does not ship while a failed item is open".

### Step 4. Duties beside the decision

Where a failed item carries a legal duty in the person's market and role (for example the DCB0160 deploying organization's risk assessment, CP-UK-09, CP-UK-10; a covered entity's 92.210 mitigation, PE-113; a GDPR DPIA, EN-111), place the duty beside the release-waits call without leaning, "for your legal owner".

### Step 5. What the person must decide

Each with its facts: release, hold, or release with named open items; whether a not-assessable item gets its applicability decided; whether a test on an older model version is rerun on the release (route to `dh-technology` responsible-ai-governance); when the index is reread (the person's date, or "not given"). Propose nothing unless asked; label any proposal "proposed".

## Build the output

Follow `assets/governance-review-and-miss-owners-output.md`. Answer first: whether the person's rule is met, the count of failed items by name, how many have an owner, a release-waits call and a present-by date, and the item that most limits the review. Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/evidence_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- The rule, owners, release-waits calls and dates are the person's, and the record says so.
- No "compliant", "ready" or "ship"; no failed item closed by the model.
- The count of items that would have to become present is quoted from the script, not estimated.
- The review is labeled "governance review draft for the owner".
- `python3 scripts/evidence_check.py words ANSWER.md` prints "within the short-mode cap".
- Every fact names its source and date in plain words with the row id after it.
- The record line is the very last line; the calls list and the offer of the full version come before the record block: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Reopening the release controls or the blocking rule on subgroup gaps: `dh-technology` responsible-ai-governance.
- CAPA for a failed item that became a nonconformity: `dh-regulatory-and-quality` audit-capa-and-complaints.
- Any wording for a board, regulator, customer or vendor: stops for the owner the person names.
