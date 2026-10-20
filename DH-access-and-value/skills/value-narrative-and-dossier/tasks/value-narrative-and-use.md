# B1 Value narrative and use

Framework task: DH-01.07.4.1, Part B, task B1. Replaces the old "Value narrative" and "Narrative use" tasks.

## What this task delivers

The value narrative per audience, drafted for the owner: what the product does for that audience, the checked claims it rests on with the certainty a person assigned, what the narrative does not say, and, for each place the person says it will be used (dossier, payer meeting, slide, publication, sales material, HTA submission), the rules that bind that use, with the stop.

Why it matters: the same sentence is HCEI in a payor dossier (PC-US-06), a labeling question in a clinician leave-behind (PC-US-23), and an advertising question for a German patient (PC-DE-10). The narrative is only as strong as its weakest claim and its use decides the rules.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-01.07.4.1 Part B, Value narrative and use |
| Workflow | The steps below |
| Knowledge | `references/certainty-and-wording.md`; `references/audience-frameworks.md`; A1 claim register; A2 dossier if built |
| Tool | `verify.qualify_source` and `verify.check_claim` for any claim not yet checked; `verify.extract_claims` to split a draft the person supplies; `verify.build_record` |
| Prompt | This guide |
| Template | `assets/narrative-output.md` |
| Input | The request and its context; intended use per market; the audiences; the uses the person names; the claim register or the evidence |
| Governance | `references/governance.md`; every narrative stops for the owner the person names for regulatory or legal review, or owner not named |
| Catalogue job | None. (`value-dossier` is design-partner only.) |

## Read the request

- **Audiences and uses.** Write down each audience and each use exactly as the person names them (old rule: "State where the buyer said the narrative will be used"). A US payer deck that will also sit on a public website is two uses (PC-US-35).
- **Cleared yet?** Before clearance or for an uncleared use, the payor narrative follows 502(gg) only; nothing is drafted for clinicians or consumers about that use.
- **Existing draft?** If the person supplies narrative text, split it with `verify.extract_claims` and split joined claims yourself (the tool returns one claim per sentence).
- **Short or full?** "A paragraph for our payer slide" is short; "value narrative for the launch" is full.

## Workflow

### Step 1. Take the claims

Use only claims A1 marked "may enter". Any new claim runs A1 Step 3 first. A claim with no passage is `[GAP]` and is left out of the narrative, named in "not said".

### Step 2. Write the narrative per audience

One short paragraph per audience, in plain words, built from: the problem the audience owns (in the person's words), what the product does within its intended use, the checked results with population, comparator, outcome and time point, and the certainty level named as the person assigned it (ES-89, ES-96), worded with the Table 15.6.b verb for that level: direct for high, "likely" or "probably" for moderate, "may" for low, "the evidence is very uncertain" for very low (ES-203 to ES-206). Where certainty is `[GAP]`, say "certainty not yet rated" and quote the effect as the source reports it, attributed. Use "proposed" for any framing the person did not give. Never write "proves", "cost-effective" or "saves money" as fact (`references/certainty-and-wording.md`).

### Step 3. State what the narrative does not say

List the claims held (no passage, opposite passage, wider population), outcomes that did not move and limitations: for payor uses cite PC-US-40 (balanced and complete presentation in HCEI); cite PC-US-31 only for clinician (CFL) material.

### Step 4. Bind each use

For each use the person named, write the rows that bind it and the stop:

- US payor dossier or meeting, cleared use: HCEI conditions and context (PC-US-04, PC-US-06, PC-US-40), not for prescribers or a public website (PC-US-35), guidance status (PC-US-47).
- US payor, before clearance or uncleared use: PC-US-08 to PC-US-10, PC-US-44 to PC-US-46.
- US clinician material: consistent with labeling, rows for the product's route (PC-US-22, or PC-US-23 and PC-US-24, plus PC-US-25 to PC-US-31); review before release (PC-US-33).
- EU and Germany: MDR Article 7 (PC-EU-01, PC-EU-02); HWG for advertising, stricter outside professional circles (PC-DE-01 to PC-DE-05, PC-DE-09, PC-DE-10).
- UK: medical purpose follows promotion (PC-UK-01); testimonials count as manufacturer claims (PC-UK-03).
- Publication: the rows hold no rule on scientific publication; write "publication rules not sourced `[GAP]`" and keep the narrative's claims to the passage.
- Sales or marketing material, patient or consumer messages: belong to dh-go-to-market (pricing-and-value-proposition); point there.
- HTA submission or payer negotiation: belongs to dh-access-and-value (payer-engagement-and-hta-submission); point there.

### Step 5. Route for review

List what the owner decides: each narrative, each use, each `[GAP]`, each AMCP draft row relied on. Name the owner the person gave, or "owner not named".

## Build the output

Follow `assets/narrative-output.md`. Answer first: the narrative in one or two sentences per audience.

## Before you hand it over

- Every sentence of result traces to a "may enter" claim; held claims are listed under "not said".
- Certainty is a person's rating or `[GAP]`.
- Each use has its rows and the stop.
- Count the words in short mode; record line.

## Boundaries

- The skill never clears a narrative or says it complies with any law or code.
- No narrative for an uncleared use to clinicians or consumers.
- No price or budget figure unless the person supplies it and it is labeled as theirs; a price position belongs to dh-go-to-market.
