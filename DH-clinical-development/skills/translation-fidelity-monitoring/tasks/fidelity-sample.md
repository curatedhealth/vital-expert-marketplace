# A2 Fidelity sample

Framework task: DH-01.01.4.2, Part A, task A2. Replaces the earlier "Fidelity sample" section (DH-01.01.4.2.2).

## What this task delivers

For one named version: every shipped claim (or a sample the person defines, with coverage stated) set beside its source passage with the differing words quoted; every decision rule checked against its specification on the evidence the person holds; any safety event for the product that bears on a rule; and delivered dose against the regimen, per user, from usage logs. Nothing is marked pass or fail here unless the person's confirmed A1 rules say so; differences are quoted for the person to mark.

Why it matters: the old method was to mark each claim match or fail with the differing words quoted, never to sample only the claims that match, and to mark a claim with no source as a fail (DH-01.01.4.2.2). Overlap scoring does not catch a dropped hedge or a negation (register N3), so the words have to be set side by side.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Clinical Validation Director (`clinical-validation-director`) |
| Skill | DH-01.01.4.2 Part A, Fidelity sample |
| Workflow | The steps below |
| Knowledge | A1 rules; `references/claim-and-rule-fidelity.md`; `references/fidelity-frameworks.md`; rows TM29, TM32, TM33, TM87 to TM89, TM92 to TM94, TM97, TM102, TM105, TM116, TM135, CS25, CS29 |
| Tools | `verify.extract_claims`; `verify.qualify_source` then `verify.check_claim`; `regulatory-dh.search_safety_events` for a named authorized product; `scripts/fidelity_sample.py` (`claims` and `adherence`) |
| Prompt | This guide |
| Template | `assets/fidelity-sample-output.md` |
| Input | The request and its context: version name, shipped product text, decision rules and test or log evidence, source passages or the claim map, usage log and regimen, the number of claims shipped |
| Governance | `references/governance.md`; the person marks each difference against their rule |
| Catalogue job | none; `claim-labels` (available) labels claims against a stored intended purpose for promotional review and does not compare with the evidence source |

## Read the request

- **Version.** Name and date. The sample is for one version.
- **Population of claims.** How many shipped. If the person gives a sample, ask how it was drawn; a sample of only matching claims is not accepted (old rule).
- **Sources.** The passage for each claim, from the claim map or the person. A claim without one is listed as having no source.
- **Rules and evidence.** The rule specification and what shows how it behaved: test records, event logs.
- **Usage data.** User, week, sessions, minutes, and the regimen in the person's words. Personal data stays with the person; the script runs where the data is.

## Workflow

### Step 1. Extract the shipped claims

If the claims are not already listed, call `verify.extract_claims {text}` on the shipped copy. It marks every sentence checkable, including instructions and caveats: keep caveats in the sample, because a dropped caveat is a fail type (A1 step 3).

### Step 2. Set each claim beside its source

Build a CSV with `claim_id, version, product_text, source_passage, source_ref` (and population columns if held) and run `python3 scripts/fidelity_sample.py claims SAMPLE.csv --shipped N`. The script lists, per claim, words in the source missing from the product text (possible dropped hedge, caveat or population limit), words in the product text missing from the source (possible stronger verb or wider population), and numbers that differ, plus sample coverage and the count with no source. Read each pair yourself and mark the difference against the person's A1 fail conditions.

### Step 3. Use Verify only as a second reader

For claims with a literature source, call `verify.qualify_source {doi, question}` then `verify.check_claim` with the claim, the passage and the full qualify_source object (C18). Record the status and overlap. In the build, a hedge removed ("improves" for "might be used to improve") and a negation both returned "supported" (89 and 90 percent), while a claim with new words (hyperactivity, teenagers) returned "unsupported" (33 percent) (`references/tools.md`). A "supported" status never passes a claim; an "unsupported" status is a prompt to read. FDA decision summaries are rated inadmissible (C1): compare those passages by hand.

### Step 4. Check the decision rules

For each rule, compare the specification (decision point, tailoring variable, option, missing-data behavior, TM77 to TM89) with the evidence the person holds of how it behaved. For a named authorized product, call `regulatory-dh.search_safety_events {product_code, jurisdiction}` and read recall summaries for rule behavior; MAUDE figures are report counts, not confirmed events. Describe any event only by its record.

### Step 5. Measure delivered dose

With the usage log and the person's regimen, run `python3 scripts/fidelity_sample.py adherence LOG.csv --sessions-per-week S --weeks W [--min-minutes M] [--enrolled N]`. It reports per user sessions delivered of expected, weeks with use, mean minutes per session, and coverage (users with any session over enrolled). This is adherence in Carroll's sense: frequency, duration and coverage against the plan (TM102); content delivered needs module-level logs, `[GAP]` if absent. Moore recommends descriptive quantitative information on fidelity, dose and reach (TM97). The person's threshold decides what passes.

### Step 6. Note what the sample cannot show

Say what was not sampled (claims not in the sample, rules without evidence, content without logs), and that delivery data show what was used, not why: responsiveness and quality of delivery are moderators in Carroll (TM103), and Moore separates adaptation from infidelity by reference to the intervention theory (TM93).

## Build the output

Follow `assets/fidelity-sample-output.md`. Answer first: version, coverage, claims with differences by type, claims with no source, rules with differences, dose summary, and what was not sampled. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Sample coverage is stated; no sample of only matching claims.
- Every difference is quoted in both texts' words.
- No claim passes because a citation is present or Verify returned "supported".
- Dose figures state the regimen and the session definition they were measured against.
- Each [PAPER] paper cited has its DOI once in prose, and every table cell that cites a [PAPER] row carries that row's own DOI; abstract-only and [WF] rows carry their label each time.
- No date, data cut, version, threshold or status appears that the person did not give ("not given" and ask); no fact comes from an earlier, separate request.
- The record line is the last line of the answer body (the calls list, if any, follows it): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Promotional claims review: `dh-go-to-market` pricing-and-value-message-monitoring.
- Software verification records and anomaly logs: `dh-regulatory-and-quality` design-controls-and-risk-management.
- Complaint and vigilance reporting of a rule failure: `dh-regulatory-and-quality` audit-capa-and-complaints and `dh-regulatory-and-quality` regulatory-submission-and-dossier.
