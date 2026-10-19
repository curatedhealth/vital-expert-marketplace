# A1 Submission content map

Framework task: DH-03.03.4.1, Part A, task A1. Replaces the earlier "Retrieve guidance" tool section and the content half of "Submission Dossier Compilation".

## What this task delivers

A sourced list of what the dossier has to contain for each route the person is taking: FDA 510(k) or De Novo through eSTAR, the software documentation elements at the chosen level, a PCCP section where one is proposed, EU MDR Annex II and III technical documentation, and the UK position. Each section carries the row it comes from. It answers "what exactly does our submission need to contain?"

Why it matters: incomplete submissions are the commonest early failure. In FY 2025, 7.20% of 510(k)s and 10.61% of De Novos were not accepted or failed technical screening on the first cycle (S-38, S-44), and only 14 of 52 EU notified bodies report that more than half of submissions arrive complete (S-73, contractor study).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | SaMD Regulatory Affairs Director (`samd-regulatory-affairs-director`) |
| Skill | DH-03.03.4.1 Part A, Submission content map |
| Workflow | The steps below |
| Knowledge | `references/content-maps.md` and `content-maps.json`; `references/submission-sources-supplement.md`; `references/REG_PATHWAYS_SUBMISSIONS.md`; `references/AI_ML_REGULATION.md` (PCCP rows) |
| Tools | `regulatory-dh.list_jurisdictions` (free), `regulatory-dh.retrieve_guidance` (once); `scripts/dossier_gaps.py` (optional) |
| Prompt | This guide |
| Template | `assets/content-map-output.md` |
| Input | The request and its context: product, intended use, the route and class the regulatory owner has chosen, the software documentation level if chosen, whether a PCCP is proposed |
| Governance | `references/governance.md`; the route, class and level are the owner's decisions |

## Read the request

- **Route and class.** Take them from the person or from an earlier pathway decision in the conversation. If not decided, say the map needs a route, offer the maps for the routes the person is weighing side by side, and point to the pathway competency (DH-03.03.3) for the decision. Never pick the route.
- **Software level (US).** If the regulatory owner has chosen Basic or Enhanced, use it. If not, lay out the test (RP US-26 to RP US-29) with the device facts the person gave and ask the owner to choose. Map both levels if the choice is open.
- **AI.** If the device is AI-enabled and a PCCP is proposed, add the PCCP section.
- **Mode.** A direct question ("what goes in a De Novo eSTAR?") gets short mode. A planning document gets full mode.

## Workflow

### Step 1. Say what the library can add

Call `regulatory-dh.list_jurisdictions` (free) once if the run will touch library data. Call `regulatory-dh.retrieve_guidance` once with a short query in the source's words (for example "eSTAR De Novo" or "Annex II technical documentation"). On 19 October 2026 the store returned no device-submission passage for these questions and returned medicines passages instead (`references/tools.md`). Use a passage only if it is device guidance with a source URL; otherwise say "the library holds no passage for this; the map is from the reference files".

### Step 2. Build the map per route

For each route, list the sections from `content-maps.md` with the source row on every line:

- **FDA 510(k):** the eSTAR sections (S-13), with the predicate section (S-14) and the Special 510(k) section marked "Special 510(k) only".
- **FDA De Novo:** the De Novo eSTAR sections (S-19), including alternatives (S-22), proposed class (S-20) and benefits, risks and mitigations with special controls if class II (S-21, RP US-12).
- **FDA software overlay:** the ten elements at the chosen level (S-01 to S-10), with the SDS difference (S-06) and the IEC 62304 declaration option (S-07). Cite the 14 June 2023 guidance (RP US-25), and note that the eSTAR guidance text still names the older title (S-17).
- **PCCP:** a standalone, titled, versioned section with its three parts (AI US-03, AI US-11); only in a submission type that allows it (AI US-09). AI lifecycle content guidance is draft (AI US-21).
- **EU MDR:** Annex II sections 1 to 6 and Annex III (RP EU-13 to RP EU-16, S-49 to S-54); the conformity route for the class the owner stated (RP EU-08 to RP EU-11). For AI devices, one technical file and the AI Act date with its amending act (AI EU-19, AI EU-29).
- **UK:** CE acceptance dates in force and the open consultation (RP UK-02 to RP UK-05); MHRA registration (RP UK-01); UKCA content `[GAP]`; the GB versus EU software classification difference (RP UK-14).
- **PMA, Switzerland:** content structure `[GAP]` in this skill; say what is sourced (clocks, classification basis).

With code execution, `python3 scripts/dossier_gaps.py --route <route> [--software basic|enhanced] [--pccp]` prints the list with rows; it is the same data as `content-maps.json`.

### Step 3. Flag what changes the content

From the person's facts and the rows only, flag items that change what goes in: a combination product or class III (Enhanced generally recommended, RP US-28); a device first CE marked under the MDD that Rule 11 up-classifies (transition conditions, RP EU-23, RP EU-24); human factors content now inside eSTAR (RP US-39); clinical investigations required for class III and implantables unless an exception applies (A2 handles this).

A De Novo filed directly on "no predicate": the classification summary must list similar regulations, 510(k)s and product codes (S-79), and FDA may decline an already-classified type (S-80). If the person or the conversation names a product code or a cleared device of the same intended use, state that record as a fact for the regulatory owner. Do not change the route.

### Step 4. What it means for the person

Close with the consequence in sourced terms, for example: "If you want a PCCP, it has to be in this De Novo; FDA will not authorize one through a Pre-Sub, though it will give feedback on it (AI US-09, AI US-10)", or "If the owner chooses Enhanced, the SDS and unit and integration test reports join the submission (S-06, S-08)". Keep it conditional and short. Do not estimate effort or time.

## Build the output

Follow `assets/content-map-output.md`. Answer first: the number of sections per route and the two or three that most often need early work for this device type, from the rows. Then the map.

## Before you hand it over

- Every section has a source row; every `[GAP]` says what was not read.
- Draft guidance is labeled draft with its date; superseded versions are flagged.
- The route, class and level are attributed to the person's owner, or marked "not decided".
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- No classification or pathway decision (DH-03.03.3). No PCCP design (DH-03.03.1).
- No ISO or IEC clause text.
- Drugs, biologics and wellness apps are out of scope.
