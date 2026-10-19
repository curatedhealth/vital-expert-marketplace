# B Assemble and check the record

Framework task: 6.2 Decision Record (build and verify).

## What this task delivers

The eight-section record, each section taken from the report that produced it, with its evidence classes; missing sections named as gaps; the result as the owner chose it; the check's findings.

Why it matters: a record is only as honest as its weakest section. Filling a gap to make the record look complete is the failure this skill exists to prevent (method.md D1, D4, D7).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | AI Investment Decision Lead |
| Skill | 6.2 |
| Knowledge | `references/method.md` (D1, D4, D7) |
| Tools | `scripts/record_check.py`; `decide_build_record`, `decide_verify_record` |
| Template | `assets/decision-record.md` |
| Input | All earlier reports |

## Workflow

1. **Map** each report to its section: Decision Contract to 1; value at stake to 2; outcome priorities (with provenance and Gate 2) to 3; gap register to 4; options with both baselines to 5; result, route (from the delivery plan and trial design) and portfolio placement to 6; assumptions and risks from every report to 7; dissent to 8.
2. **Name gaps**: a section with no report behind it is "[GAP] not worked through"; never drafted from general knowledge.
3. **Result** (question 6): if not recorded, ask which result the owner chose. Never preselect.
4. **Check** with `scripts/record_check.py`: range, provenance, Gate 2, baselines, result wording and owner, dissent, release, named people. Gaps block preparing the signature; annex gaps are listed in the annex. The record line reports the check as it is, never "in order" for an item the annex lists.
5. **Build and verify** on the connector if a brief is open; read only the eight sections; never show key names.

## Boundaries

- Never shorten a section into a recommendation. The record states what was decided and why, not what you think.
- Keep each fact's evidence class.

## When you are unsure

If two reports disagree (for example, a different value range in two places), record both with their dates and flag the conflict for the owner.
