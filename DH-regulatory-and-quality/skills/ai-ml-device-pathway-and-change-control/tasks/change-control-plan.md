# A2 Change control plan

Framework task: DH-03.03.1.1, Part A, task A2. Replaces the earlier "Predetermined Change Control Plan Authoring" section.

## What this task delivers

The structure of a predetermined change control plan for the person's AI-enabled device software function: the three FDA components with their headings, each planned change sorted against the three modification types FDA names, a list of everything the person must supply, and the EU and UK counterparts. The model drafts structure and lists gaps. It never writes acceptance criteria values, thresholds, test methods or sample sizes.

Why it matters: a PCCP is authorized as part of the marketing authorization, and deviating from it would generally make the device adulterated and misbranded [AI US-10, US-13]. Every number in it becomes a binding commitment. The value of this task is a complete, sourced skeleton and an honest list of what is missing, so the regulatory and data science owners spend their time on the decisions only they can make.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | SaMD Regulatory Affairs Director |
| Skill | DH-03.03.1.1 Part A, Change control plan |
| Workflow | The steps below |
| Knowledge | `references/pccp-structure.md`; `references/ai-ml-routes.md`; `references/AI_ML_REGULATION.md` |
| Tools | None required. `verify.build_record` on sign-off |
| Prompt | This guide |
| Template | `assets/change-control-plan-output.md` |
| Input | The request and its context: intended use, route if decided, the planned changes, the data and retraining approach, current performance facts, owners |
| Governance | `references/governance.md`; scope and criteria are the owner's |

## Read the request

- **Intended use and route.** Needed: every change must stay inside the intended use, and for a 510(k) inside substantial equivalence [AI US-08, US-16]. If the route is undecided, draft for the routes the person is weighing and say so.
- **Planned changes.** Ask for a plain list ("retrain quarterly on new sites' data", "add a new scanner vendor", "extend to patients aged 16 to 17"). If none is given, ask once.
- **Short or full.** "Do we need a PCCP?" or "does retraining fit?" is short mode. "Draft our PCCP" is full mode.
- **Jurisdictions.** FDA by default. Add the EU and UK sections only when named.

## Workflow

### Step 1. Confirm the plan can exist on this route

From `references/pccp-structure.md`: a PCCP is established in an original PMA or listed PMA supplements, a Traditional or Abbreviated 510(k), or an original De Novo [AI US-09]. A Special 510(k) is not on that list; if the person plans one, say the guidance's list does not include it and route it to the owner. FDA gives feedback on a PCCP in a Pre-Sub but does not authorize it there [AI US-10].

### Step 2. Sort each planned change

For each change the person lists, write one line:

| Planned change (person's words) | Closest FDA type [AI US-07] | Intended-use check [AI US-08] | Sort |
|---|---|---|---|

Sort values: "fits type N as described (owner to confirm)"; "may change indications or intended use: for the regulatory owner"; "not enough detail `[GAP]`". Changes that look like new indications get the second value, because FDA expects most indications-for-use changes to be hard to assess in advance [AI US-08].

### Step 3. Draft the three components as headings

Use the component table in `references/pccp-structure.md`:

- **Description of Modifications.** One subsection per change kept in step 2, each with: what changes, the specification that will be met (`[GAP]` for the person), the populations and inputs in scope (from the person).
- **Modification Protocol.** For each change: data management, retraining, verification and validation testing, acceptance criteria, update procedure, labeling update, post-market monitoring, and the detect-and-revert mechanism [AI US-05, US-31, US-36]. Every acceptance criterion line reads "acceptance criterion: set by the person `[GAP]`".
- **Impact Assessment.** A table linking each change to the risks the person names and their mitigations [AI US-06]; benefit-risk conclusion left for the owner.
- **Section 515C placeholders.** Labeling, notification if the device does not function as intended, performance requirements [AI US-17].

### Step 4. List what the person must supply

A numbered list, one line per missing item, each tied to the heading it fills. Group by owner if the person named owners; otherwise "owner not named".

### Step 5. Add the EU and UK counterparts if asked

EU: Article 43(4) and Annex IV point 2(f) [AI EU-05]; MDCG 2025-6 on Annex IX 4.10 [AI EU-30]; no EU PCCP guidance yet [AI EU-31]; the AI Act requirements apply to MDR devices from 2 August 2028 under Regulation (EU) 2026/1744 [AI EU-19]. UK: no MHRA PCCP guidance yet; draft intended by December 2026 [AI UK-04].

### Step 6. Placement and use

Say where it goes (a standalone, titled, versioned section named in the cover letter and table of contents [AI US-11]) and how it is used after authorization (changes made per the protocol, documented in the quality system [AI US-12]). Route tracking of changes after authorization to the readiness monitoring skill, task A2.

## Build the output

Follow `assets/change-control-plan-output.md`. Short mode: the answer (does a PCCP fit, which changes sort where), the sorting table, the top three items to supply, the record line. Full mode: the full skeleton with every heading and gap.

## Before you hand it over

- No acceptance criterion, threshold, sample size, test method or statistical margin appears with a value the model chose.
- Every heading cites its row.
- No change is declared "in scope" or "covered"; sorting is "as described, owner to confirm".
- The plan is labeled "draft for the owner"; it is not a submission.
- If it leaves the conversation, ask who clears it and call `verify.build_record`.

## Boundaries

- If asked to fill in acceptance criteria: decline that part, and draft what the facts support instead: the list of criteria that must be set, the populations they must cover [AI US-05], and the questions for the data science and regulatory owners.
- The connector's guidance passages on PCCPs carry no source URL; do not quote them (`references/tools.md`).
- Quality-system procedures for implementing changes belong to the quality pack; cybersecurity content to the cybersecurity pack.
