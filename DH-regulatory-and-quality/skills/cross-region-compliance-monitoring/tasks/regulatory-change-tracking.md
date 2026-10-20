# A2 Regulatory change tracking

Framework task: DH-03.03.2.2, Part A, task A2. Replaces the earlier "Cross-Region Compliance Monitoring" section (drift part).

## What this task delivers

A dated list of what has changed, or is in draft, at the regulators of the person's markets: each item with its status (in force, adopted with a later date, final guidance, draft, proposal, exploratory, superseded), what it changes for this product, where the regulator publishes the next change, and the dated obligations that follow for the person's markets. It answers "what moved at our regulators, is it law yet, and what does it mean for our dates?"

Why it matters: regional drift often starts outside the company. A consultation outcome, a superseded guidance or a new module going live changes what each region requires, and a draft read as law causes as much trouble as a law that was missed.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | SaMD Regulatory Affairs Director |
| Skill | DH-03.03.2.2 Part A, Regulatory change tracking |
| Workflow | The steps below |
| Knowledge | `references/change-sources.md`; `references/obligations.md`; the copied research files |
| Tools | `regulatory-dh.get_deltas`, `retrieve_guidance`; `scripts/obligations_table.py` |
| Prompt | This guide |
| Template | `assets/change-tracking-output.md` |
| Input | The request and its context: markets, product type (including whether it uses AI), the date of the last review |
| Governance | `references/governance.md` |

## Read the request

- **Markets and product.** Which regulators matter. Whether the product is AI-enabled (AI Act dates, FDA AI guidance) or an EU legacy device (transition dates).
- **Since when.** The last review date. Items older than that are context only.
- **A specific item?** If the person names one ("is the UK reliance route live?"), answer it first.

## Workflow

### Step 1. Register events from the library

Call `get_deltas` with the manufacturer, FDA product code or EMDN code and `since` the last review date. If the log has not started, say "no change recorded; the log has not started for this scope" and that this covers register events only (authorizations, safety events), not guidance or law.

### Step 2. Guidance and law from the change register

Walk `references/change-sources.md` section 2 and keep the items that touch the person's markets and product type. For each: status word, instrument and date, what it changes, rows. Examples of the wording: "EU AI Act obligations for MDR devices now apply from 2 August 2028 (Regulation (EU) 2026/1744, adopted, in force 27 July 2026; AI EU-19)." "UK indefinite CE recognition: proposal; consultation closed 10 April 2026; no outcome published (UK-05)." "FDA AI lifecycle guidance: draft; listed for finalization in FY 2027 (AI US-21, CHG-06)."

### Step 3. Check the library's guidance store, carefully

Call `retrieve_guidance` with one keyword at a time (for example "EUDAMED", "MDSAP"); multi-word questions return nothing. Use a passage only to find a document's name; check its status and date against `change-sources.md`. Do not cite a passage that has no source URL. If a returned document is older than a change in the register (MDCG 2019-15 rev1 on EUDAMED registration predates Regulation (EU) 2024/1860), say so.

### Step 4. Where the next change will appear

For each market, name the source to follow from `change-sources.md` section 1 (FDA guidance alerts and the CDRH agenda each October; the MDCG page; MHRA alerts and the reform tracker; Swissmedic RSS and the FOPH legislation page; TGA consultation hub and legislation compilations). Where no source was read (Health Canada, ANVISA, PMDA), `[GAP]`.

### Step 5. Turn the person's markets into a dated obligations table

Write the person's markets and the dates they gave to a JSON file and run `scripts/obligations_table.py FILE --as-of DATE` (or `--markets US,EU,GB,CA,CH`). The script applies only in-force rules; proposals appear as separate lines with their status. Present the table with each line's row.

### Step 6. What changes for the person

For each item that touches them, state the consequence conditionally and which planning task it reopens: a classification change reopens the requirement map (DH-03.03.2.1 A1); a new or lost reliance route reopens the sequence (DH-03.03.2.1 B1); a new evidence expectation reopens the evidence plan (DH-03.03.2.1 A2).

## Build the output

Follow `assets/change-tracking-output.md`. Answer first: the items that change something for this product, with their status. Then the full list, the sources to follow, and the obligations table. Short mode for direct questions.

## Before you hand it over

- Every item carries its status word, date and row.
- No draft, proposal or agenda item is presented as law.
- Superseded documents are named with their replacement.
- No guidance passage without a source URL is cited.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- No legal opinion on how a change applies; the consequence is stated conditionally for the regulatory owner.
- No consultation response on the person's behalf.
- Drugs, biologics and wellness apps are out of scope.
