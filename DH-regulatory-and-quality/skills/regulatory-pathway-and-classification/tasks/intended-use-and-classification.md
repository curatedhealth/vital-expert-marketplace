# A1 Intended use and classification

Framework task: DH-03.03.3.1, Part A, task A1. Replaces the earlier "Intended-Use Definition", "SaMD Risk Classification" and "Classify a product" sections.

## What this task delivers

An intended use statement, then a classification argument per jurisdiction the person targets (US, EU, GB, Switzerland, with IMDRF N12 as the common reasoning frame): which rule applies, which way the facts point, what would move the product up or down a class, and what the person's regulatory owner has to decide. It answers "is this a medical device, and what class would each regulator likely put it in?"

Why it matters: the class sets the route, the evidence bar, the notified body question, the fee and the clock. A product described one way in the pitch deck and another in the technical file gets classified on the file, and a single word ("diagnose" against "inform") can move it a class.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | SaMD Regulatory Affairs Director |
| Skill | DH-03.03.3.1 Part A, Intended use and classification |
| Workflow | The steps below |
| Knowledge | `references/classification-rules.md`; rows in `references/reg-pathways-sources.md`, `references/multi-region-sources.md`, `references/ai-ml-regulation-sources.md` |
| Tools | `regulatory-dh.classify_product` (record check only); `regulatory-dh.search_devices` for a named comparable; `regulatory-dh.list_jurisdictions` (free) |
| Prompt | This guide |
| Template | `assets/intended-use-and-classification-output.md` |
| Input | The request and its context: product description, claims, users, setting, target jurisdictions, any existing intended use or authorization |
| Governance | `references/governance.md`; the class is the regulatory owner's decision |

## Read the request

- **Product facts.** What the software does with what input, what output it gives, to whom (patient or health care professional), in which condition and setting. Ask for what is missing; each item is a classification input.
- **Jurisdictions.** Which of US, EU, GB, Switzerland. Default to the ones named; ask if none.
- **Existing record.** Is the product, or an earlier version, already cleared or CE marked? If so, get the reference (K, DEN or P number, or Basic UDI-DI).
- **AI.** Does any function learn from data? If yes, the AI Act and PCCP points apply.
- **Mode.** A direct question ("what class is this under Rule 11?") gets short mode. A classification memo for a file gets full mode.

## Workflow

### Step 1. Write the intended use statement

Draft it in five parts, each a classification input (`classification-rules.md`, "Start with the intended use"):

1. Medical purpose: treat, diagnose, prevent, monitor, drive management, or inform management.
2. Condition and its seriousness (critical, serious, non-serious, in the person's clinical words).
3. Intended user: patient, caregiver, or health care professional.
4. Setting and conditions of use.
5. Output: a single directive, or options and their basis that the user reviews.

Use the person's words. Where the person's material says two different things (a "diagnostic" claim on the website, "supports decisions" in the draft label), show both and say which class each points to. The statement is a draft for the owner: it becomes the filed wording only when the owner clears it.

### Step 2. Is it a device

Apply the device tests per jurisdiction: EU MDSW definition and the wellness exclusion (RP EU-01, RP EU-29); FDA's software policy and enforcement discretion (RP US-16 to US-18); for decision support aimed at health care professionals, the four CDS criteria in the guidance dated 29 January 2026, all of which must be met (RP US-19 to US-24). Criterion 2 is not quoted in the research rows: say so and point to the guidance rather than paraphrase. If the product fails one criterion, say which and why; the 2026 single-recommendation policy (RP US-23) is a separate question to raise, not a conclusion.

### Step 3. Check the record (only if a reference exists)

If the product or a named comparable is already authorized, call `regulatory-dh.classify_product` with `reference` (for example `{"reference": "K191716"}`). The result is the stored product code, label and regulation number, labeled "from record". Say plainly that this is an input to the argument, not a decision for the new product. Do not call it with only a description to "get a class": it returns no classification by design, and the taxonomy matches it returns are VITAL's own segments, never a regulatory class (`references/tools.md`).

### Step 4. Argue the class per jurisdiction

For each target jurisdiction, write the argument in three lines: the rule that applies (with its row), how the product's facts meet it, and what would change the answer. Use `classification-rules.md`:

- **US:** which existing product code and regulation number fits the intended use, if one does (from A2's precedents or a named comparable's record); the class that code carries (RP US-01 to US-03). If no code fits, say the De Novo question arises (RP US-09) and that a 513(g) request asks FDA (RP US-53).
- **EU:** Rule 11 sub-rule and class (RP EU-02 to EU-05), with the strictest-rule and driving-software checks (RP EU-06, RP EU-07) and MDCG 2019-11 rev.1 (RP EU-27, RP EU-30, RP EU-31).
- **GB:** the UK MDR 2002 MDD-derived rules (RP UK-14); state where GB and EU differ, and that CE marked MDR devices are accepted to 30 June 2030 (RP UK-03).
- **Switzerland:** follows MDR Annex VIII through Art. 15 MedDO (RP CH-01, CH-04); same class argument as the EU unless hardware is involved (RP CH-06).
- **IMDRF N12:** significance by situation (JX-01 to JX-03; RP IM-02), mapped through MDCG's illustrative table (RP EU-31). Note IMDRF N81 (2025) was not read (RP IM-04).
- **AI-enabled:** if class IIa or higher in the EU, high-risk under the AI Act, applying from 2 August 2028 under Regulation (EU) 2026/1744 (AI EU-19, AI EU-27, AI EU-28).

Lay out the class each reading points to. Where two readings are possible, show both with the fact that decides between them. The model never writes "the class is". It writes "the facts point to class IIa under Rule 11(a); class IIb if the owner judges that a wrong output could lead to serious deterioration".

### Step 5. Name what moves the class

List the two or three facts that would move the product up or down, in the person's terms (for example: "if the output becomes a single treatment directive, CDS criterion 3 fails, RP US-23"; "if the condition is critical, N12 category IV and Rule 11(a) class III, RP EU-03, JX-02"). These are the decisions and claims the owner controls.

## Build the output

Follow `assets/intended-use-and-classification-output.md`. Answer first: the classes the facts point to, per jurisdiction, in one table. A direct question gets short mode: 450 words maximum, counted without tables' source column and the calls list. Before handing over, count the words of the answer (excluding the calls list and table source columns). If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question, full-mode sections. Never cut a gap, a stop or the record line. Offer the full version in one line.

## Before you hand it over

- Every rule has its row id; every guidance is cited with its version date and draft or final status.
- No sentence declares the final class; the owner decides, and the output says who (or "owner not named").
- A `classify_product` result is described as a record check, labeled "from record", and as an input.
- No clause text of ISO or IEC standards and no IMDRF table cell beyond the rows.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Classification arguments only. Which route to take is B1; comparable devices are A2; dossier assembly belongs to the Submission Excellence competency (DH-03.03.4); PCCP drafting to the AI/ML Regulatory competency (DH-03.03.1).
- No legal opinion; point to the owner and counsel where the rule text is ambiguous.
- Drugs, biologics and wellness apps are out of scope.
