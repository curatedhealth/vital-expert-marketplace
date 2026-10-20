# A2 Evidence maturity read

Framework task: DH-DIL.2.1, Part A, task A2. Replaces the old dh-diligence skills "Evidence maturity" and "Read evidence maturity" (catalogue job `evidence-maturity`).

## What this task delivers

Two things kept apart. First, the library's evidence maturity score for the company, with its formula, every component and input, the excluded components and the tool's own limits, recomputed by script. Second, a proposed level under a named framework that fits the product (NICE ESF tier, Evidence DEFINED level, or V3 components), with the framework's own limits beside it, labeled "proposed" for the person to confirm.

Why it matters: a single number reads like a grade. The library's score counts registrations and registered studies (close in shape to the clinical robustness score, DL-116, DOI 10.2196/37677), which its critics call too narrow (DL-119, DOI 10.2196/41715), and funding has not tracked evidence in the samples studied (DL-117, DL-124, DOI 10.1371/journal.pone.0323390). A named framework says what kind of evidence is expected and for whom; none was built for investors (`diligence-research.md`, "Changes and conflicts" item 8).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Not bound (old skill "Worker: not bound"); see `references/governance.md` |
| Skill | DH-DIL.2.1 Part A, Evidence maturity read |
| Workflow | The steps below |
| Knowledge | `references/evidence-frameworks.md`; rows DL-107 to DL-125 (DOIs in that file), CV155 to CV159 (DOI 10.1038/s41746-020-0260-4), UK12, UK13, HE-079 to HE-084, CS56, CS57, CS67, DE14 |
| Tools | `diligence-dh.get_evidence_maturity`; `scripts/profile_table.py`; `verify.qualify_source` then `verify.check_claim` for a paper the person cites |
| Prompt | This guide |
| Template | `assets/evidence-maturity-output.md` |
| Input | The request and its context: one company or product reference, the product's intended purpose as the record or the person states it, any evidence review or GRADE rating the person brings, the framework the person wants (if any) |
| Governance | `references/governance.md`; the level is proposed, the person confirms |
| Catalogue job | `evidence-maturity` (named by the old skill; job card needs a live check) |

## Read the request

- **Company or product.** The tool scores a company. If the person asks about one product, say the score covers every product of the maker.
- **Intended purpose.** Needed to pick the framework and the NICE tier. Take it from the record (for example FDA classification name) or the person; if neither, `[GAP]` and ask.
- **Evidence the person brings.** A review, a GRADE table, a list of trials. Use it as theirs; this task does not grade studies.
- **Which framework.** If the person names one, use it and say whether it fits (`evidence-frameworks.md` section 1). If not, propose the fitting one.

## Workflow

### Step 1. Get the library's score

Call `diligence-dh.get_evidence_maturity {company: "<exact reference>"}`. Save the output and run `python3 scripts/profile_table.py FILE.json`. Report the score, the formula check, each component with its inputs, the excluded components ("excluded, not zero"), the tool's limits and any risk flags, all as printed. Where recalls or safety bear on the question, add the saved `compare_portfolio` safety events and recall flags for the company with their retrieval date (`references/tools.md`); `none_found` is "none found in the loaded enforcement source; not proof of none". The score says nothing about whether the company still exists: if the person's question turns on that, add one line from the status step (`references/company-status.md`): status as read, or "Status: [GAP]: not read" with the filings to open. If the script flags "US sources only" beside non-US authorizations, name the register behind each authorization.

### Step 2. Say what the score is

One line: "The library's evidence maturity score is a stated convention for comparing documented evidence, not a framework level, a rating or a valuation (rubric v1, 7 October 2026)." Add that it counts registered studies in the loaded registry only, and published trials outside it do not count.

### Step 3. Pick the framework

From `evidence-frameworks.md` section 1: NICE ESF for a digital health technology in UK health and care; Evidence DEFINED for a patient-facing behavior-change intervention whose value rests on health outcomes; V3 for a sensor-based measure. More than one may apply; none may. Name the one you use, why, and its own limits.

### Step 4. Propose the level

Follow `evidence-frameworks.md` section 3:
- NICE ESF: tier from the intended purpose (UK12, HE-084); "proposed; the tier classifies purpose, not evidence".
- Evidence DEFINED: only with a graded evidence base the person brings. Without one, "level not assessable until the evidence is graded `[GAP]`" and route to `dh-clinical-development` literature-and-real-world-evidence-review. Level 4 only with two or more high-quality RCTs identified (DL-112).
- V3: each component present, missing or `[GAP]`, with the reference behind it.

Write "proposed level X under FRAMEWORK, for you to confirm".

### Step 5. Check any paper claim

If the person or the record cites a paper for an effect, run `verify.qualify_source {doi}` and `verify.check_claim` with the passage `{text, locator}` and the full qualify_source object. Accept only a passage that says the same thing in the same direction (N3). Otherwise the claim stays "not checked".

## Build the output

Follow `assets/evidence-maturity-output.md`. Answer first: the library score with its parts and what it excludes, then the proposed framework level with its limits, then the one gap that most limits the read. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- The library score and the framework level are in separate sections; the score is never called a level.
- The level is labeled "proposed" and carries the framework's own limits.
- No "clinically validated", "proven" or "evidence-based" verdict.
- "No registered study linked in the loaded sources", never "no evidence".
- No missing field printed as 0 or "none"; recall flags quoted as saved.
- Word count: run `python3 scripts/profile_table.py --count ANSWER.md` on the short answer; at or under 450 words, counted without the calls list and source columns.
- Each [PAPER] paper cited has its DOI once in prose, and beside its row id in every table.
- The record line is the very last line of the answer (the offer of a full version and any calls list come before it, never between "Record" and "Clears it"): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Grading studies, building an evidence table: `dh-clinical-development` literature-and-real-world-evidence-review.
- Whether evidence meets a payer or HTA bar: `dh-access-and-value` coverage-pathway-and-access-strategy.
- Economic evidence: `dh-access-and-value` economic-model-development.
- The score over time: `evidence-maturity-monitoring` (this pack).
