# A2 Claim currency check

Framework task: DH-01.07.4.2, Part A, task A2. New evidence task; it carries the "every value claim goes through Verify" rule into monitoring.

## What this task delivers

For each claim in the live narrative or dossier: is its source still unretracted and uncorrected, does the passage still state the claim in the same direction, are there candidate new studies to read, and has any guidance or method the line leans on moved since the narrative was built. Each line ends "holds", "re-read needed" or "held", with the signal and the date.

Why it matters: a dossier is a living document (HE-132), retractions are not always shown consistently (ES-123), and the FDA payor guidance, AMCP Format and NICE methods all moved in 2025 and 2026 (`references/currency-signals.md`). A line that was right when written can mislead now.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-01.07.4.2 Part A, Claim currency check |
| Workflow | The steps below |
| Knowledge | `references/currency-signals.md`; `references/certainty-and-wording.md`; the sibling's claim register |
| Tool | `literature.check_retraction`, `verify.check_currency`, `literature.get_record`, `verify.qualify_source`, `verify.check_claim`, `literature.search_literature` (with `date_from`), `verify.extract_claims` for a narrative without a register; `verify.build_record` when cleared |
| Prompt | This guide |
| Template | `assets/currency-check-output.md` |
| Input | The live narrative or dossier text, or the claim register; the DOIs and passages; the date the narrative was last checked; the guidance it cites |
| Governance | `references/governance.md` |
| Catalogue job | `evidence-table` (available) for re-running evidence rows; the same-direction reading remains the method |

## Read the request

- **Which claims.** The register if the person has one; otherwise split the narrative with `verify.extract_claims`, then split joined claims yourself.
- **Since when.** The date the narrative was last checked; if not given, ask, or use the date of the newest source and say so.
- **Which guidance.** The documents the narrative or dossier cites (FDA payor guidance version, AMCP version, NICE manual).
- **Short or full?** "Are our claims still OK" is short; "currency review of the dossier" is full.

## Workflow

### Step 1. Source status per DOI

Call `literature.check_retraction` and `verify.check_currency`. Name the source that answered (Crossref only on 19 October 2026; ES-123). Retracted or expression of concern: hold every claim on it (ES-119). Corrected: re-read the corrected passage (ES-121).

### Step 2. Re-read and re-check

Record the intervention the study tested, quoted from its Interventions or Methods section, and ask the person to confirm it is the product in the dossier. Record any author conflict the paper discloses, quoted. Do not name a product from memory.

For each claim, get the passage (the `get_record` excerpt may stop before the Results; when a source is open access, read the full text before marking any field `[GAP]` from the abstract or the library excerpt), then `verify.qualify_source` and `verify.check_claim` with the full source. Read it yourself: same direction, population, comparator, outcome, time point. A "supported" that fails the reading is held (register N3).

### Step 3. Candidate new evidence

Call `literature.search_literature` once per topic with `filters.date_from` set to the last check date. List up to five records as candidates to read, with the design checked against the paper where you can (N8: labels are unreliable). Do not judge whether they change a finding; that is the person's or a review's (dh-clinical-development, literature-and-real-world-evidence-review).

### Step 4. Guidance and methods

Compare the guidance the narrative cites with `references/currency-signals.md`. Flag each line that cites a superseded or draft version without naming the other (for example PC-US-47 for FDA payor guidance; HE-131 for AMCP; HE-057 to HE-063 for NICE utilities; HE-074 for the NICE HealthTech threshold conflict).

### Step 5. Classify each line

"Holds" (source current, passage re-read in the same direction, no guidance signal), "re-read needed" (correction, new candidates, guidance moved), or "held" (retracted, passage no longer matches, no passage). Every "held" or "re-read needed" goes to B1.

## Build the output

Follow `assets/currency-check-output.md`. Answer first: how many lines hold, which do not, and why.

## Before you hand it over

- Source checked named for every retraction result.
- No search hit reported as a change in the evidence.
- AMCP rows labeled "AMCP 6.0 draft".
- Count the words in short mode; record line.

## Boundaries

- No new review here (dh-clinical-development, literature-and-real-world-evidence-review). No change to the product's labeling (dh-regulatory-and-quality).
- The skill never says a claim is now true or false; it says what the source and the passage show today.
