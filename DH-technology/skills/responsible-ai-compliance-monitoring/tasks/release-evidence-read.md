# A2 Release evidence read

Framework task: DH-01.04.1.2, Part A, task A2. Carries the old task "DH-01.04.1.2.2 Release score" (check each item and keep the record id; mark pass or fail; note a group that was [GAP] at test time and is still unseen; never pass a release with an unseen group presented as tested). The pass or fail against the person's rule is B1; this task reads each item's status.

## What this task delivers

For one release model version as of the person's read date: each item of the person's evidence index marked present, missing, not yet applicable or not assessable, with its record id, evidence date and flags G1 to G8; the groups unseen at test time; and, where the person names an AI device, the post-release safety events the library holds for it and for comparable devices the person names. It answers "for this release, what do we hold, what is missing, and what has happened since go-live?"

Why it matters: a bias test run on the previous model, or a fairness policy filed where a test belongs, reads as "present" on a checklist that only asks whether a file exists. The old task was explicit: an unseen group is never presented as tested.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | `ai-ml-governance-director` (old DH-01.04.1.2.2). Work as an AI governance analyst who reads evidence against requirements |
| Skill | DH-01.04.1.2 Part A, Release evidence read |
| Workflow | The steps below |
| Knowledge | A1 output or the person's index; `references/release-evidence-requirements.md` section 6; `references/gap-rules.md` |
| Tools | `scripts/evidence_check.py read`; optional `regulatory-dh.search_safety_events` for a device the person names; `verify.build_record` when the record leaves |
| Prompt | This guide |
| Template | `assets/release-evidence-read-output.md` |
| Input | The request and its context: the evidence index, the release model version, the read date, the device name, manufacturer and comparable devices (if any), the release date |
| Governance | `references/governance.md`; completeness only, the person judges quality |
| Catalogue job | none |

## Read the request

- **Release version and read date.** Both required. Not given: "not given"; ask. Never use today's date as the read date.
- **The index.** CSV in the columns of `SKILL.md` Input. If the person gives a list instead, write it into those columns and show it back before reading.
- **Since release.** Safety events only if the person names a device or manufacturer, with `since` the release date the person gives.

## Workflow

### Step 1. Read the index

`python3 scripts/evidence_check.py read --index FILE --release VERSION --as-of YYYY-MM-DD`. Without code execution, apply the same rules by hand: applicability (yes, no, from a date, not given), evidence present of the required type, model version against the release, dates against the read date.

### Step 2. Write each status with its record id

For each item: status, evidence record id, evidence date, flags. A policy in place of a test is "missing" (G2). A test on another model version is "not assessable for this release" (G3). A "from" date after the read date is "not yet applicable" with the date. Evidence dated after the read date is stated as a fact (G4).

### Step 3. Groups still unseen

List every group in `groups_not_seen` with its item (G5): "not seen at test time, still not tested". Never fold it into a present test.

### Step 4. Post-release events (optional)

For a device the person names: `regulatory-dh.search_safety_events` with `manufacturer` (short form) and with `product`, `since` the release date, `limit` 10; for each comparable device the person names, the same by its manufacturer. Keep a row only if its title or summary names the device; count the rest as "returned, not about these devices". MAUDE counts are reports, not confirmed events, never attributed to a company (`references/tools.md`). Describe kept events only by what the record states. Reportability routes to `dh-regulatory-and-quality` audit-capa-and-complaints. A press claim stays "from you (press claim, not checked)".

### Step 5. What the read cannot show

One line each: quality of present evidence (the person's); items whose applicability was not given; items the index does not list that A1 would add.

## Build the output

Follow `assets/release-evidence-read-output.md`. Answer first: counts by status, the items missing or not assessable by name, the groups still unseen, and the flag that most limits the read. Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/evidence_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Release version and read date are the person's, or "not given".
- Every item keeps its record id; no item marked present on a policy in place of a test or on another model version.
- Every unseen group listed as not tested.
- No "compliant", "ready" or score presented as approval.
- Events kept only where the record names the device; excluded rows counted; no empty result read as safety.
- `python3 scripts/evidence_check.py words ANSWER.md` prints "within the short-mode cap".
- Every fact names its source and date in plain words with the row id after it.
- The record line is the very last line; the calls list and the offer of the full version come before the record block: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Rerunning the subgroup test on the release model: `dh-technology` responsible-ai-governance.
- Performance drift since release: `dh-technology` model-performance-and-drift-monitoring.
- Device file readiness: `dh-regulatory-and-quality` ai-ml-readiness-monitoring.
