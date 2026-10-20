# A1 Economic question and reference case

Framework task: DH-01.07.2.1, Part A, task A1. Replaces the old "Economic question" section (CF-12.01.07.2.1.1), whose rule stays as Step 1: write the decision the model has to answer, in the buyer's words.

## What this task delivers

A one-page frame for an economic model of a digital health technology: the decision in the person's words, who decides it, the technology and comparators specified, the reference case that decision-maker has written (perspective, horizon, discounting, outcome measure, utilities, form of analysis, threshold as written), the open conflicts and recent changes in those rules, and the list of inputs the model will need. Every rule carries its row id.

Why it matters: most model rework starts with a frame that does not match the decision-maker. A NICE HealthTech model discounted at the wrong rate, valued with a retired EQ-5D value set, or argued against the wrong threshold is rebuilt, not repaired. A budget-impact-first reviewer such as ICER-PHTI reads a lifetime cost-utility model as an answer to a question nobody asked.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-01.07.2.1 Part A, Economic question and reference case |
| Workflow | The steps below |
| Knowledge | `references/reference-cases.md`; `references/model-build-rules.md` sections 1 and 2; `references/health-economics-methods-research.md` (HE rows) |
| Tools | None required. `verify.qualify_source` and `verify.check_claim` only if the person supplies a published source for the question; `verify.build_record` when a named person clears the frame |
| Prompt | This guide |
| Template | `assets/economic-question-output.md` |
| Input | The request and its context: the technology, its intended use as the person states it, the market, the decision-maker if known, comparators, any analysis plan |
| Governance | `references/governance.md` |
| Catalogue job | none (`find_job` returned no job for an economic model on 19 October 2026) |

## Read the request

- **Which decision?** "Will NICE recommend", "will the health plan cover", "what will the commissioner pay for", "will IQWiG" each name a different decision-maker. If none is named and the market is named, lay out the bodies `reference-cases.md` holds for that market and ask which one the model is for. Do not choose the route: route choice is dh-access-and-value's (coverage-pathway-and-access-strategy).
- **What is the technology?** A device status or intended use the person has not stated is `[GAP]`, routed to dh-regulatory-and-quality (regulatory-pathway-and-classification). Never infer it.
- **Short or full?** A direct question ("which discount rate does NICE use for our app") gets short mode. "Write the decision problem", "analysis plan", "for the HTA team" gets full mode.
- **Out of scope?** Drugs, biologics and wellness apps: say so in two lines and stop. A request to conclude that the product is cost-effective: decline that part (see Boundaries) and offer the frame.

## Workflow

### Step 1. Write the decision in the person's words

One or two sentences: who decides, about what, for whom, compared with what. Quote the person. Where a part is missing, write it as `[GAP]` in the sentence rather than filling it.

### Step 2. Name the decision-maker and its current text

From `reference-cases.md`, name the body and the version of its text: for NICE, PMG36 (HE-033) for technology appraisals, PMG48 (HE-064, HE-065) for HealthTech including digital and AI, the ESF (HE-078, HE-079) for commissioners; HAS 2020 (HE-102); IQWiG 8.0 (HE-108); ICER VAF (HE-114) or ICER-PHTI for DHTs (HE-115); AMCP 6.0 draft rows for a US formulary dossier (HE-131, HE-133 to HE-139). For NICE topics, state which transitional rule applies by start date (HE-062, HE-063, HE-066). For the EU, say that joint clinical assessment holds no economic evaluation (HE-093, HE-094) and the model is national.

### Step 3. Specify the technology and comparators

Lay the person's description into the PICOTS-ComTeC domains (HE-032, [PAPER] Zrubka et al. 2024, DOI 10.1016/j.jval.2024.01.009, SIG report, abstract only): population, intervention, comparator, outcome, timing, setting, communication, technology, context. Leave unstated domains `[GAP]`. For an ESF question, record the tier the person assigns (HE-082 to HE-084); the tier is theirs, the definitions are the rows'. Comparators are the person's; for NICE cost-comparison, the source names comparators "recommended in published NICE guidance for the same population" (HE-042).

### Step 4. Lay out the reference case

Fill the reference-case table for the named body only: perspective on costs and on outcomes, form of analysis, outcome measure and value set, time horizon, discount rate and any exception, threshold as written, budget impact rule. Copy the row ids. A cell the research file does not hold is `[GAP]` with the text to read.

### Step 5. Choose the form of analysis, with the person

From `model-build-rules.md` section 2, list the forms the body names for this situation, and what each would need. For a likely cost-saving DHT at NICE, cost-comparison (HE-042, HE-076); for early use, a simplified model or threshold analysis (HE-069); for ICER-PHTI, a 1-year budget impact from two perspectives (HE-121 to HE-123); for an ESF higher-financial-risk DHT, cost-utility or cost-consequences (HE-090, HE-091). The person chooses; if asked to recommend, label it "proposed" with the rows behind it.

### Step 6. State conflicts and recent changes

Name every open conflict that touches this frame (`reference-cases.md`, "Open conflicts"): the NICE PMG36 and PMG48 threshold ranges (HE-050, HE-051, HE-074), always with the statement that NICE uses no precise maximum (HE-049) and, for HealthTech, that the severity modifier is not applied initially (HE-075); never cut these when shortening, PMG51 replacing PMG36 section 4.3.16 for new topics (HE-046, HE-058), early value assessment renamed (HE-067), AMCP draft status. Never resolve a conflict; state both texts and whose choice it is.

### Step 7. List the inputs the model will need

A skeleton input register for task A2: each input, its unit, the source kind expected (person's data, published study, real-world evidence, value set), and who supplies it. For a BIA, the HE-019 (DOI 10.1016/j.jval.2013.08.2291) elements and, for NICE ESF, the HE-088 cost lines. Clinical effect and utility inputs that need a review point to dh-clinical-development (`literature-and-real-world-evidence-review`).

### Step 8. Analysis plan

CHEERS 2022 item 4 asks whether a health economic analysis plan was developed and where it is available (HE-006, DOI 10.1177/23814683211061097). Offer the frame as the start of one; say whether the person has one.

## Build the output

Follow `assets/economic-question-output.md`. Short mode answers the question asked with the reference-case rows that bind it. Full mode is the decision problem document.

## Before you hand it over

- The decision sentence is the person's; every gap in it is visible.
- Every rule has a row id and the text version; conflicts are stated both ways.
- No threshold is presented as the answer to "will it be cost-effective".
- Count the words in short mode.
- If the frame leaves the conversation (to an HTA team or a payer), it stops for the owner the person named; call `verify.build_record` with that named clearer, or label it an uncleared draft.

## Boundaries

- Route choice, HTA submission mechanics and payer engagement belong to dh-access-and-value (coverage-pathway-and-access-strategy, payer-engagement-and-hta-submission); device status and intended use to dh-regulatory-and-quality (regulatory-pathway-and-classification); the literature review to dh-clinical-development (literature-and-real-world-evidence-review).
- The skill never states that a product will be, or is, cost-effective.
- Drugs, biologics and wellness apps are out of scope.
