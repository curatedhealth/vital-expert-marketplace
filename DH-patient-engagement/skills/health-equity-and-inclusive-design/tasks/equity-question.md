# A1 Equity question

Framework task: DH-02.03.4.1, Part A, task A1. Replaces the earlier "Equity question" section (CF-12.02.03.4.1.1).

## What this task delivers

A written equity question for one product or program: the subgroups the person chose to look at, the product step where exclusion would show for each, what the person's own counts say at that step (if they have counts), the sourced duties or frames that touch that step, and the groups the data cannot see, marked `[GAP]`. It answers "who may this product leave out, where, and what do we not know?"

Why it matters: exclusion shows at a step (enrollment, onboarding, first use, follow-up), not in a product description. A step that works only in English, only on a smartphone, or only for people who can read a dense consent text leaves people out whether or not anyone intended it. A group the data does not record cannot be shown to be reached.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Health Equity & Digital Access Lead (`health-equity-access-lead`) |
| Skill | DH-02.03.4.1 Part A, Equity question |
| Workflow | The steps below |
| Knowledge | `references/equity-frames.md`; `references/patient-engagement-equity-research.md` (PE rows); `references/accessibility-pointer-rows.md` (UX rows, pointers only) |
| Tools | None required. Optional `literature.search_literature`, then `verify.qualify_source` and `verify.check_claim` for a published finding. `scripts/equity_compare.py` on the person's counts. `verify.build_record` only for sign-off |
| Prompt | This guide |
| Template | `assets/equity-question-output.md` |
| Input | The request and its context: the product or program, its steps, market(s), the people it is meant for, the subgroups the person wants examined, any aggregate counts by subgroup |
| Governance | `references/governance.md`; the subgroups and priorities are the person's |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. evidence-table grades a set of studies for a product's claims; this task only identifies or checks a source the person names. |

## The rule that shapes this task: the person chooses the groups; unseen groups stay unseen

The model offers the frames (NIH-designated populations, SVI themes, Section 1557 language access, Core20PLUS5, the DAP disaggregation) as options and never picks the equity priorities. A group the person's data does not record is written as `[GAP]` with the record that would show it; no rate, share or estimate is invented for it.

## Read the request

- **Product and steps.** Ask for the steps from first contact to the outcome (for example referral, enrollment, onboarding, first use, ongoing use, follow-up measurement). Without steps, exclusion cannot be placed.
- **Market.** US, England, EU or other. The frames differ (equity-frames.md); the US frames are sourced in most depth.
- **Subgroups.** Which dimensions the person wants examined. If they have none, offer the frames as a short menu and ask; the old register examples (language, disability, connectivity, site type) are one option.
- **Counts.** Whether they have aggregate counts by subgroup at any step, and their small-cell rule. Never patient-level data.
- **Decision support.** Whether the product scores, triages or recommends for clinical decisions, and which inputs it uses (for 92.210, PE-113, PE-114).
- **Mode.** Short for a direct question; full for an assessment document.

## Workflow

### Step 1. Fix the frame

Write back: product, steps, market, the subgroups chosen (or the menu offered), and whether the person's organization or customer is treated as a Section 1557 covered entity by their legal owner (`[GAP]` if not known; the definition is not in this skill's sources). Confirm before going on.

### Step 2. Place each subgroup at a step

For each subgroup, name the step where exclusion would show and the barrier type, in the person's words where they gave them. Typical barrier types with a sourced anchor:

- Language: help not offered, offered only in English, machine translation of critical text not reviewed by a human (PE-107, PE-108, PE-109).
- Disability and access: content or app not accessible (PE-110, PE-111); point to the dh-user-experience accessibility skills for conformance.
- Decision support inputs: a scoring or triage tool with race, color, national origin, sex, age or disability inputs (PE-113).
- Area deprivation: subgroups by SVI band (PE-120 to PE-123) or, in England, Core20 by IMD [WF] (PE-127).
- Device, connectivity, site type: no row sets a rule `[GAP]`; the person's own evidence is the basis.

### Step 3. Duties and frames that touch each step

For each step and barrier, list the rows that apply with their dates as the rows give them, for example "92.210(b) and (c): within 300 days of 5 July 2024 (PE-115)". Say "applies if your legal owner treats you as a covered entity" where it depends on that. For a clinical study, lay out the DAP status from PE-36, PE-40 and PE-41 with the research file's reading labeled as a reading, and route the study question to the regulatory owner.

### Step 4. What the person's counts show (if any)

If the person has aggregate counts by subgroup at a step, ask for their small-cell threshold and reference group, then run:

```
python scripts/equity_compare.py counts.csv --min-cell <their rule> --reference "<dimension>=<their reference subgroup>"
```

Report reach per subgroup with its interval and the difference from the reference, the share not recorded, and any suppressed cells. No verdict: whether a difference matters is the person's rule (sibling skill `health-equity-monitoring` B1). Without counts, write "no counts for this step".

### Step 5. Groups the data cannot see

List every subgroup that the person chose but that their records do not capture (for example disability status not recorded, preferred language captured only at one site), each `[GAP]`, with the record that would show it. Where a dimension has "not recorded" values, report that share with its count; never redistribute it across groups. These go to A2.

### Step 6. Published evidence (optional)

Only if the person asks what is known about who similar interventions leave out: call `literature.search_literature` with the intervention type and population, read titles and drop off-topic records, and for any finding you will state, call `verify.qualify_source {doi}` then `verify.check_claim` with a passage you have read that states the finding in the same direction. Label it "published context about another population, not evidence about your product". Count the calls.

## Build the output

Follow `assets/equity-question-output.md`. Answer first: the one or two steps where the chosen groups are most likely left out on the evidence given, and the groups no data can see. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every subgroup is the person's choice or explicitly offered as an option.
- Every duty cites its row and date; applicability left to the legal owner where the rows do not decide it.
- Every rate comes from the person's counts through the script, with the small-cell rule stated.
- Every unseen group is `[GAP]` with the record that would show it; no invented numbers.
- No equity or compliance claim. If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Not an accessibility conformance review (dh-user-experience accessibility skills) and not a legal opinion on Section 1557 coverage.
- Who could see an unseen group is A2; what to change is B1; whether a shipped change reached the group is `health-equity-monitoring`.
- No decision about any individual's eligibility.
