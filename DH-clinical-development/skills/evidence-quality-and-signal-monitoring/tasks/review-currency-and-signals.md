# A1 Review currency and change signals

Framework task: DH-01.02.4.2, Part A, task A1. Replaces the monitoring half of the old *Digital Signal Detection Monitoring*.

## What this task delivers

For a review or evidence base the person relies on: the last search date set against the rule of the body it serves (Cochrane 12 months, EU JCA 3-month cut-off, IQWiG up-to-dateness), the retraction, correction and expression-of-concern status of the review and its key studies, candidate new studies and newer reviews published after the last search, and methods or guidance that have been superseded since. It answers "is the evidence still current for our purpose, and what has changed?"

Why it matters: in one sample of 100 reviews, 23% were out of date within two years (ES-102), and out-of-date reviews mislead decision makers (ES-101). An EU JCA dossier needs its own information retrieval cut at most 3 months before submission, whatever a published review's date (ES-152, ES-156, ES-168).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | AI/ML Governance Director (`ai-ml-governance-director`) |
| Skill | DH-01.02.4.2 Part A, Review currency and change signals |
| Workflow | The steps below |
| Knowledge | `references/currency-rules.md`; ES-52, ES-101 to ES-104, ES-119 to ES-125, ES-133, ES-137, ES-152, ES-156, ES-168 |
| Tool | `literature.get_record`; `verify.check_currency` and `literature.check_retraction`; `literature.find_related(direction="cited_by")`; `literature.search_literature` with `filters.date_from`; `scripts/review_check.py currency` |
| Prompt | This guide |
| Template | `assets/currency-output.md` |
| Input | The review (DOI or the person's own protocol and log), its last search date, the body and decision it serves, the planned publication or submission date, its included studies if it is the person's own |
| Governance | `references/governance.md`; "out of date" and "update" are the person's decisions |
| Catalogue job | none |

## Read the request

- **Whose review.** A published review the person wants to cite, or the person's own review being kept up to date. For their own, the included-study list allows a retraction sweep of every study (ES-119).
- **Which body and date.** The rule depends on it: Cochrane publication (ES-52), EU JCA submission (ES-152, ES-156), NICE HealthTech reuse (ES-133), IQWiG (up-to-dateness check, detail `[GAP]`). Ask if not named. The date is the person's; state the rule, never pressure.
- **Last search date.** From the review's methods (PRISMA item 6, ES-06). If the person gives only a publication date, the search date is not that date: read the methods or mark `[GAP]`.

## Workflow

### Step 1. Get the record and the search date

1. `literature.get_record(doi=...)` for identifiers and the open-access link.
2. Read the last search date from the methods (Europe PMC full text or the publisher). Example measured: the 2025 review of fully automated dCBT-I states "studies published up to March 31, 2024" (Methods, Search strategy) and was first published 12 March 2025.

### Step 2. Check the date against the rule

Run `python3 scripts/review_check.py currency --last-search YYYY-MM-DD --target YYYY-MM-DD --rule cochrane|jca|all`. Report its lines as printed. Example: last search 31 March 2024 against publication 12 March 2025 is within 12 months, outside six (ES-52); against a JCA submission on 15 January 2027 the cut-off would need a search on or after 15 October 2026 (ES-156).

### Step 3. Publication-status signals

For the review and each key or included study: `literature.check_retraction(doi=...)` (gives notice and date) or `verify.check_currency(doi=...)`. Report "retracted (notice, date)", "corrected: read the erratum" (ES-121), "expression of concern" (ES-125, [WF]), or "no retraction found in Crossref on DATE". Never report `check_currency` "current" as currency of the evidence (`tools.md`).

### Step 4. New-study signals

1. `literature.find_related(record=<review>, direction="cited_by", limit=20)`: keep items dated after the last search; drop the plainly off-topic with a note.
2. `literature.search_literature(query="<review PICO in plain words>", filters={"date_from": "<day after last search>"}, limit=20)`: candidate trials and newer reviews.
3. Put both lists in a CSV (id, date_or_year, design) and run `python3 scripts/review_check.py currency ... --new-studies FILE.csv` to place them against the last search date.
4. Label every item "candidate, not screened"; design labels from the library are drafts (register N8). Note the library lacks CENTRAL and Embase, so this is a signal check, not an update search.

### Step 5. Method and guidance signals

From `currency-rules.md` section 5, list any method or guidance the review relied on that has since been superseded or is still draft (for example PRISMA 2009, ROBINS-I V2 draft, FDA device RWE guidance of 2017 superseded on 18 December 2025). Only items the review actually used.

### Step 6. What it means for the person

State consequences in sourced terms only: "For a Cochrane publication the search must be rerun within 12 months before publication (ES-52)"; "For a JCA, the dossier's own retrieval needs a cut-off at most 3 months before submission; the review's March 2024 search cannot serve as that (ES-168)". The decision is B1's and the person's.

## Build the output

Follow `assets/currency-output.md`. Answer first: the date check result for the named body, the publication-status signals, the number of candidate new studies with the strongest few named by their record, and the one decision the person must make next.

## Before you hand it over

- The search date comes from the methods, with its locator, or is `[GAP]`.
- Dates are checked by the script, not by mental arithmetic.
- "Current" from Verify is reported as publication status only.
- New studies are "candidate, not screened"; no claim that findings would change.
- Record line present in every answer, refusals included: "Clears it: [the person named, in their words, or owner not named]. The record is built with verify.build_record once that named person clears it; until then, uncleared draft."

## Boundaries

- Not an update search: the person's searcher runs that in the required databases (sibling skill A1).
- Not a judgment that the review is wrong or outdated: a signal list for B1.
- Device adverse-event signals belong to dh-regulatory-and-quality.
