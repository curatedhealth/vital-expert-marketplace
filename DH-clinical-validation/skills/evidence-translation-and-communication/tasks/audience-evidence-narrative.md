# B1 Audience evidence narrative

Framework task: DH-01.02.2.1, Part B, task B1. Replaces the old "Payer Value Narrative" section and extends it to clinicians, patients and the public.

## What this task delivers

For each audience the person names (payer or technology assessment committee, clinician, patient or public, journal or congress): the evidence narrative built only from A1 statements, the certainty as rated, the limitations and unfavorable findings that must travel with it, the rules that bind that audience in that market with row ids, the wording those rules require, and the wording they exclude. Every narrative is a draft for the owner the person names for regulatory or legal review, or owner not named. Economic arguments, prices and coverage are not in it.

Why it matters: the same trial is told three ways, and each telling carries its own rules. A payer narrative is a regulated communication in the US (PC-US-02, PC-US-04); a clinician summary must stay consistent with labeling (PC-US-23); a lay summary under the EU CTR is a duty (CV152), and in Germany any public device advertising may not suggest that health improves by use (PC-DE-10). A narrative that drops the comparator or the limitation for a friendlier audience misleads by omission (PC-US-03).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`) |
| Skill | DH-01.02.2.1 Part B, Audience evidence narrative |
| Workflow | The steps below |
| Knowledge | `references/audience-rules.md`; `references/certainty-wording.md`; `references/promotion-and-claims-research.md`; A1 statements |
| Tools | `verify.qualify_source` and `verify.check_claim` for any statement not already checked in A1; `verify.extract_claims` on a draft the person supplies; `verify.build_record`; `scripts/statement_check.py` (optional) |
| Prompt | This guide |
| Template | `assets/audience-narrative-output.md` |
| Input | The request and its context; A1 statements (or the studies and passages to build them); the cleared or certified intended use per market in the person's words or from the labeling; the audiences and markets; any draft text the person wants reworked |
| Governance | `references/governance.md`; every narrative stops for the owner the person names for regulatory or legal review, or owner not named |
| Catalogue job | none startable. `value-dossier` (payer value dossier outline) is design-partner only (`examples/live/jobs_and_experts.json`). |

## Read the request

- **Audience and market.** Each pair is a separate narrative. A US payer narrative that will also sit on a public website is two audiences (PC-US-35).
- **Intended use per market.** The anchor. If the person cannot state it, mark `[GAP]` and label every narrative provisional.
- **Cleared yet?** For a US product or use not cleared, a payer narrative follows the pre-clearance rules (PC-US-08 to PC-US-10, PC-US-43 to PC-US-46) and no clinician or consumer narrative of that use is drafted.
- **Is it really marketing?** A tagline, an ad, an app store text or a value proposition goes to dh-commercial (pricing-and-value-proposition). A payer submission or HTA dossier goes to dh-market-access (payer-engagement-and-hta-submission). Answer the evidence part and point there.
- **Short or full?** "A paragraph for our payer deck" or "lay summary" is short; "evidence narratives for launch" is full.

## Workflow

### Step 1. Start from A1

Use the A1 statement for each outcome. If A1 has not run, run it in short mode first; a narrative without checked passages is not drafted. Outcomes with `[GAP]` stay out of every narrative, said as such.

### Step 2. Pick what each audience needs, without changing what the evidence says

The population, comparator, time point, effect as reported and certainty with its rater are the same in every version. What changes is the order, the words and the required context:
- Payer: design, generalizability, limitations, sensitivity analyses and balanced information (PC-US-40); for an economic analysis, the HCEI conditions (PC-US-04). Whenever any of PC-US-34 to PC-US-40 is cited, add the guidance status line: the 2018 final text applies until the June 2026 revised draft is final (PC-US-47). Where the paper states funding or conflicts, include them as a limitation (CONSORT 2025 item 5, CV111 [PAPER], DOI 10.1136/bmj-2024-081123); where only the abstract was read, say funding and conflicts were not checked `[GAP]`.
- Clinician: material design and limitations disclosed clearly and prominently, unfavorable findings included (PC-US-31, PC-US-32); the cleared population only (PC-US-23, PC-US-27). Where the paper states funding or conflicts, include them as a limitation (CONSORT 2025 item 5, CV111 [PAPER], DOI 10.1136/bmj-2024-081123); where only the abstract was read, say funding and conflicts were not checked `[GAP]`.
- Patient or public: plain words for the outcome and comparator; the certainty level and its handbook meaning in plain words with the rater named (`references/certainty-wording.md`, rule 5); no cure, guarantee or no-side-effect wording (PC-EU-10, PC-DE-04, PC-UK-07). For an EU CTR trial the lay summary is due with the results summary (CV152); its Annex V content is `[GAP]`. For any device in the EU, MDR Article 7 (PC-EU-01, PC-EU-02). In Germany, ask whether the page is public advertising; if the owner says yes, no suggestion that health improves by use (PC-DE-10).
- Journal or congress: the A2 checklist and ICMJE rules.

### Step 3. Apply the market rules

Open `references/audience-rules.md` and list, per audience and market, the rows that bind the narrative and what each requires. Cite only the market's rows. Label [INDUSTRY] and [WF] rows. In Germany, a cited study states whether it concerns the advertised product, with author, date and source, and figures are reproduced faithfully (PC-DE-05).

### Step 4. Draft, and do not draft what crosses a rule

Write the narrative for each audience with its required statements beside it. Where the person wants wording that crosses a rule or goes beyond the passage (an uncleared population, a different comparator, "proven", "cost-effective", a certainty above the rating), do not draft it: name the row or the A1 gap it crosses and offer a safer wording the facts support, labeled "draft for the owner". With code execution, run `scripts/statement_check.py` on the draft with the A1 passages and ratings; judge every hit yourself.

### Step 5. Check what is new

If the draft introduces any statement not checked in A1 (for example from a second paper), split it with `verify.extract_claims`, then run `verify.qualify_source` and `verify.check_claim` with the passage and accept only on a same-direction reading (register N3).

### Step 6. Route for review

List what the owner decides: each narrative, each required statement, each [INDUSTRY] or [WF] row relied on, each `[GAP]`. PC-US-33 recommends review by qualified medical or scientific, legal and regulatory personnel before release; name the owner the person gave, or "owner not named".

## Build the output

Follow `assets/audience-narrative-output.md`. Answer first: one sentence per audience saying what the evidence supports for them.

## Before you hand it over

- Same population, comparator, time point, effect and certainty in every version.
- Every narrative has its binding rows and required statements; [INDUSTRY] and [WF] labeled.
- No uncleared use to clinicians or consumers; no economic or coverage claim.
- Count the words in short mode.
- Label the whole output "draft for the owner"; if it leaves the conversation, call `verify.build_record` with the named clearer, or label it an uncleared draft.

## Boundaries

- The skill never clears a narrative or says it complies with any law or code.
- Marketing claims, ads and value propositions: dh-commercial (pricing-and-value-proposition). Payer submissions, HTA dossiers, prices and coverage: dh-market-access (payer-engagement-and-hta-submission). Economic models and value dossiers: dh-health-economics (value-narrative-and-dossier). Device status: dh-regulatory-strategy (regulatory-pathway-and-classification). Review method: dh-clinical-validation (literature-and-real-world-evidence-review).
- Drugs and biologics are out of scope.
