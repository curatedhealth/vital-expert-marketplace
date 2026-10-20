# B1 Release controls and acceptance

Framework task: DH-01.04.1.1, Part B, task B1. Carries the old task "DH-01.04.1.1.3 Governance control" (name the threshold that blocks release; name who may accept a difference and the reason they must write; name the monitoring that continues after release; never release a blocked difference without that written reason) as steps 1 to 4. The threshold, the acceptor and the monitoring are the person's.

## What this task delivers

A release control record draft for one model version: the person's blocking rule applied to the A2 result, with the computed change that would meet it; who may accept a difference and the written reason the person requires; the oversight, transparency, logging and monitoring controls the sources describe for the person's markets, each marked present, missing or not given in the person's material; and the decisions the person faces. It answers "by our own rule, what blocks this release, who may accept it, and what has to run after release?"

Why it matters: the old task was clear that a blocked difference is never released without a written reason. A control record that the model fills with its own threshold, acceptor or cadence says more than the organization decided.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | `ai-ml-governance-director` (old DH-01.04.1.1.3). Work as an AI governance analyst who applies the person's rules |
| Skill | DH-01.04.1.1 Part B, Release controls and acceptance |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; `references/responsible-ai-rules.md` section 4; rows DA-14 to DA-16, DA-18, DA-29, DA-33, DA-44, DA-46, DA-54 to DA-63, DA-65, DA-66, DA-80 to DA-84, AI US-32, AI US-33, AI US-37, AI US-38, AI UK-10, AI EU-14, AI EU-20, UX-US-55 to UX-US-60, UX-US-65 to UX-US-71, PE-113, CP-UK-05 to CP-UK-11 |
| Tools | `scripts/subgroup_check.py rule`; `verify.build_record` when the record leaves |
| Prompt | This guide |
| Template | `assets/release-controls-and-acceptance-output.md` |
| Input | The request and its context: A2 output or the person's file, the person's blocking rule and the date it was written, the acceptor and the written reason required, the person's oversight, transparency, logging and monitoring material, markets |
| Governance | `references/governance.md`; release go or no-go is the person's |
| Catalogue job | none |

## The rule that shapes this task: people decide

The person writes the blocking rule before reading the result, names who may accept a difference, sets what the written reason must say, chooses the monitoring and decides release. The model applies the rule to the data and writes down the result. It never supplies a threshold, never names an acceptor, never decides that a difference is acceptable, and never decides release. Where the rule's words allow two readings on the data, it shows both and writes "your call".

## Workflow

### Step 1. Confirm the blocking rule

Write the rule back verbatim with the date it was written (for example "sensitivity in any language group at most 0.05 below English, written 1 October 2026"). A rule written after the result is stated as a fact. No rule: "blocking rule not given `[GAP]`"; report the A2 values and mark nothing blocked. If asked for a number: refuse (no source sets one), and list what the person could base theirs on (the error that harms from A1, the intervals from A2).

### Step 2. Apply the rule

`python3 scripts/subgroup_check.py rule --data FILE ... --reference GROUP --rule METRIC:MAX --rule-date DATE`. For each group: met, not met or not measurable, with counts. For each group that does not meet it, the computed change that would (for example "12 more detected of 32"), labeled arithmetic on the person's data, not a target. Groups marked `[GAP]` stay "not tested"; they never pass.

### Step 3. Acceptance of a difference

For each group not meeting the rule: the acceptor the person names (or "owner not named"; ask), the written reason the person requires (or "not given"), and whether release waits (the person's). Where the market and role bring a duty, place it beside the decision without leaning: a covered entity's duty to mitigate the risk of discrimination (45 CFR 92.210, PE-113); AI Act oversight and transparency duties from their dates (DA-59 to DA-62, AI EU-19); DCB0129 and DCB0160 risk management in England (CP-UK-06 to CP-UK-10). "For your legal owner."

### Step 4. Controls that go with the release

For the person's markets, from `references/responsible-ai-rules.md` section 4, mark each present, missing or not given in the person's material, with standing and date:

- **Human oversight:** override, disregard or stop to a safe state (AI Act Art 14(4)(d), (e), DA-61); awareness of automation bias (DA-60; FDA CDS guidance, 29 January 2026, UX-US-72).
- **Transparency to users:** accuracy and group performance in the instructions (DA-56, DA-57, DA-62); for non-device CDS, Criterion 4 elements (UX-US-65, UX-US-67 to UX-US-69); for certified health IT, source attributes and feedback capture (UX-US-55, UX-US-56, UX-US-59; HTI-5 proposes removal, UX-US-60, proposed only); model card as a format (FDA draft, DA-46, draft).
- **Logging:** automatic event logs over the lifetime (DA-54, DA-55; EU).
- **Monitoring after release:** what is measured, by whom, how often, and what triggers a response, all the person's. The sources: NIST MEASURE 3.1 and MANAGE 4 (DA-14, DA-16, voluntary); AI Act post-market monitoring (DA-65; template guidance due 2 September 2027, DA-66); FDA draft performance monitoring plan (DA-44, AI US-37, AI US-38, draft); GMLP principle 10 (AI UK-10); WHO principle 6 (DA-29). Drift statistics route to `dh-technology` model-performance-and-drift-monitoring.
- **Early live evaluation**, if the person runs one: user agreement and reasons for variation, errors and malfunctions, modifications during the study (DECIDE-AI, DOI 10.1136/bmj-2022-070904, DA-81 to DA-83).
- **Generative AI:** governance, content provenance, pre-deployment testing, incident disclosure (NIST AI 600-1, DA-18).
- **Non-AI alternative** weighed (NIST MANAGE 2.1, DA-15).

### Step 5. What the person must decide

List each decision with its facts: release, hold, or release with an accepted difference and its written reason; a rule written after the result rewritten and dated; each missing control given an owner and a date the person sets ("not given" until then). Propose nothing unless asked; label any proposal "proposed". Release is the person's.

## Build the output

Follow `assets/release-controls-and-acceptance-output.md`. Answer first: groups meeting and not meeting the person's rule with counts, the computed change for each miss, how many misses have an acceptor and a written reason, and the missing control that most limits the record. Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/subgroup_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- The rule, the acceptor, the written reason, the monitoring and release are the person's, and the record says so.
- No threshold, acceptor, cadence or date supplied by the model; "not given" where missing.
- The computed change is labeled arithmetic, not a target.
- Drafts (FDA AI-enabled device draft) and proposals (HTI-5) labeled; AI Act dates as amended.
- The record is labeled "release control draft for the owner".
- `python3 scripts/subgroup_check.py words ANSWER.md` prints "within the short-mode cap".
- Every fact names its source and date in plain words with the row id after it; [PAPER] rows carry their DOI.
- The record line is the very last line; the calls list and the offer of the full version come before the record block: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Checking a whole release's evidence and owners of misses over time: `dh-technology` responsible-ai-compliance-monitoring.
- Change control plans for a device: `dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control.
- Usability evidence for Criterion 4: `dh-patient-and-user-experience` usability-monitoring.
- Any wording for a board, regulator, customer or patients: stops for the owner the person names.
