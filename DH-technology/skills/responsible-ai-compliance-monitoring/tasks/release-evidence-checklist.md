# A1 Release evidence checklist

Framework task: DH-01.04.1.2, Part A, task A1. Carries the old task "DH-01.04.1.2.1 Governance evidence" (define the evidence a responsible-AI release must have: the bias test, the intended use and the human who can override the model; a missing item is a fail; name the release you will score; do not accept a policy statement in place of the test).

## What this task delivers

For one system and release: the evidence items the sources describe for the person's markets and role, each with its required type (test, document, control), its standing (law, final guidance, certification criterion, information standard, voluntary, reporting guideline, draft, proposed) and the date it applies, plus the three core items the old task named and any item the person adds. It answers "what should this release hold before we read it, and which of those items bind us from when?"

Why it matters: an evidence list that mixes drafts with law, or cites the AI Act's 2024 dates, sends a team to build the wrong file at the wrong time. AI Act high-risk duties for MDR devices now apply from 2 August 2028 (Regulation (EU) 2026/1744, 8 July 2026, AI EU-19), and the FDA AI-enabled device guidance is still a draft (FDA guidance list, content current 9 April 2026, AI US-21).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | `ai-ml-governance-director` (old DH-01.04.1.2.1). Work as an AI governance analyst who builds the checklist from sourced requirements |
| Skill | DH-01.04.1.2 Part A, Release evidence checklist |
| Workflow | The steps below |
| Knowledge | `references/release-evidence-requirements.md` sections 1 to 6; the rows each item cites |
| Tools | None. `scripts/evidence_check.py` reads the index the checklist becomes (A2) |
| Prompt | This guide |
| Template | `assets/release-evidence-checklist-output.md` |
| Input | The request and its context: system, intended use, release model version, the person's role, markets, whether it is a device (the person's statement), whether generative, whether used in a medicinal product trial, items the person adds |
| Governance | `references/governance.md`; legal readings stop for the owner the person names |
| Catalogue job | none |

## Read the request

- **Release.** The model version the checklist is for (old task: "name the release you will score"). Not given: "not given"; ask.
- **Markets and role.** They decide the sections: US (section 2), EU (section 3), England (section 4), medicinal product development (section 5). Role not given: list the items by role and ask.
- **Device or not.** Take the person's statement; never decide it. A device question routes to `dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control.
- **The person's own items.** Add them as given, marked "yours".

## Workflow

### Step 1. The three core items the old task names

Always first: the subgroup test on the release model (type test; C5), the intended use (type document; C1), and the human who can override the model, named in the person's words (type control; C8). Each with its rows from `release-evidence-requirements.md` section 1.

### Step 2. Add items by market and role

From sections 1 to 5, only the person's markets and role, each with type, standing, the date it applies and rows. EU high-risk items carry "applies from 2 August 2028 (Annex I) or 2 December 2027 (Annex III) under Regulation (EU) 2026/1744 (AI EU-19)"; whether the system is high-risk is not decided here (MDCG 2025-6 maps class IIa and above as high-risk, not legally binding, AI EU-27, AI EU-25). US items for covered entities (PE-113 to PE-115) and certified health IT developers (UX-US-55 to UX-US-60, with HTI-5 proposed only) are marked "applies if you are ...: for your legal owner". The FDA AI-enabled device draft items (US7) are listed as "draft, not a requirement" or left out if the person asks for requirements only.

### Step 3. Mark what is not enough on its own

For each test item, write beside it: a policy statement does not count; evidence on another model version does not count for this release; groups unseen at test time stay "not tested" (section 6).

### Step 4. Turn the list into the person's index

Offer the checklist as an evidence index in the CSV columns `scripts/evidence_check.py` reads (item_id, requirement, rows, applies, required_type, then the evidence columns blank for the person to fill). The `applies` column takes "yes", "no", "from YYYY-MM-DD" (the sourced date) or blank; the model fills "from" dates only from the rows, never a guess. Which items the person keeps is theirs.

## Build the output

Follow `assets/release-evidence-checklist-output.md`. Answer first: how many items apply now, how many from a later date (with the dates), and the three core items. Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/evidence_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- The release is named, or "not given".
- Only the person's markets; every item has type, standing, date and rows; drafts and proposals labeled; AI Act dates as amended.
- No statement that the system is a device, high-risk or covered by a law; legal readings "for your legal owner".
- No pass rule, owner or date supplied.
- `python3 scripts/evidence_check.py words ANSWER.md` prints "within the short-mode cap".
- Every fact names its source and date in plain words with the row id after it; [PAPER] rows carry their DOI.
- The record line is the very last line; the calls list and the offer of the full version come before the record block: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- The device technical file and submission: `dh-regulatory-and-quality` ai-ml-readiness-monitoring.
- Running the subgroup test the checklist asks for: `dh-technology` responsible-ai-governance.
- Security and privacy evidence items in depth: `dh-technology` security-and-privacy-operations-monitoring.
