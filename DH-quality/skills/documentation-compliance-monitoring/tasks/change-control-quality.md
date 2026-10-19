# A2 Change control quality

Framework task: DH-03.02.2.2, Part A, task A2. New in this version; it covers the change control half of the competency, which the earlier sections did not.

## What this task delivers

A check of the person's change log: changes with no impact assessment, assessments with no rationale, "no submission" or "not significant" decisions with no basis, changes implemented before approval or before assessment, missing approvers, hazard-touching changes with no risk file review, and items changed several times with no aggregate assessment. Each finding carries the change id, the detail and the row it rests on; counts and rates per check; and the person's own thresholds, if they set any, marked met or not met. It answers "is our change control doing what it should?"

Why it matters: FDA's Change Control inspection area exists "to ensure changes are adequately evaluated for risk and impact on products and processes prior to implementation" (QS34). A change released before its assessment is the plainest way to fail that purpose.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | QA Manager, Software (`quality-assurance-manager-software`) |
| Skill | DH-03.02.2.2 Part A, Change control quality |
| Workflow | The steps below |
| Knowledge | `references/change-control-checks.md`; `references/QUALITY_SYSTEMS.md`; `references/supplementary-rows.md` |
| Tools | `scripts/change_log_check.py`; optional `regulatory-dh.search_safety_events` for public recall context |
| Prompt | This guide |
| Template | `assets/change-control-quality-output.md` |
| Input | The change log (CSV or table) with the columns listed in the script; the period it covers; any thresholds and owners the person sets |
| Governance | `references/governance.md` |

## Read the request

- **The log.** Which columns exist. Map the person's names to the script's (`--map`). A missing column makes its check not measurable `[GAP]`; say which.
- **Period and scope.** Which product, which items, which dates. Findings are "as of" the log's export date.
- **Rules.** Ask whether the person has thresholds (for example "no change implemented before approval") and owners. Without them, report counts and rates with no verdict.

## Workflow

### Step 1. Run the checks

With code execution, run `python3 scripts/change_log_check.py log.csv [--rules rules.json] [--map their_column=field]`. Without it, apply the checks in `change-control-checks.md` by hand, change by change. Never put the log into a library call.

### Step 2. Read each finding for what it is

- A change implemented before approval is a fact from two dates. It is not proof that the change was unassessed in substance; the person may hold evidence elsewhere. Report the dates and ask.
- A rationale field that is filled is not checked for quality here. Whether a rationale supports its decision is reviewed with the sibling skill's question sheet (`document-and-change-control`, A2 and B1).
- An aggregate finding means several changes to one item with no aggregate assessment reference; whether the cumulative effect crosses a threshold is the owner's question (QX12, QX13).

### Step 3. Apply the person's rules

If the person gave thresholds, show each as met or not met with the count behind it and the owner they named. If not, show counts and rates only and offer to record rules for the next run. Never propose a threshold as a target; if asked to propose one, mark it "proposed" with the fact behind it and do not apply it until confirmed.

### Step 4. Public context (optional)

If the person asks how release-control failures show up in the field, call `regulatory-dh.search_safety_events` with a comparable manufacturer or product code (public identifiers only). Report rows by what they state: firm, product, version range, event date, class, summary. Flag rows that are not software defects. This is context, not evidence about the person's log.

## Build the output

Follow `assets/change-control-quality-output.md`. Answer first: how many changes, how many findings by check, and which findings concern changes that touch a hazard. Short mode: 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections; offer the full version in one line.

## Before you hand it over

- Each finding has a change id, the dates or fields behind it, and its row.
- Rates state their base (number of changes in the log, the period).
- No threshold appears that the person did not set; no owner the person did not name.
- No finding is worded as misconduct; the facts are dates and fields.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Checks the log's completeness and sequence. It does not redo any change's significance assessment.
- Never edits, fills in or backdates log entries; repairs are recorded as new, dated entries (B1).
- Not a CAPA effectiveness review; that belongs to DH-03.02.4.
