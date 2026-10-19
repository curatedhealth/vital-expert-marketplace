# A1 Adoption rule

Framework task: DH-02.02.4.2, Part A, task A1. Replaces register task CF-12.02.02.4.2.1 "Adoption after training".

## What this task delivers

A written adoption rule and metric sheet: the task that counts (from the task card), the users or settings in the denominator, the window after training, the share the person sets, the published definition each metric follows (Proctor or RE-AIM, named), the old step to watch, and the data each metric needs. It answers "what counts as adopted, measured how, against which denominator?"

Why it matters: adoption is defined differently in Proctor (an intention, decision or action to try, CS34) and RE-AIM (number, proportion and representativeness of settings and staff willing to start, CS24), and penetration has two denominators (CS39). A rule that does not name its definition and denominator produces numbers no one can compare. NHS buyers expect usage reported against a profile agreed at commissioning (CS61).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Adoption Lead (`digital-adoption-lead`) |
| Skill | DH-02.02.4.2 Part A, Adoption rule |
| Workflow | The steps below |
| Knowledge | `references/adoption-metrics.md`; rows CS22 to CS40, CS44, CS59, CS61, CS62; UX-M-07 to UX-M-10 (optional acceptability) |
| Tools | `verify.qualify_source` then `verify.check_claim` (counted, only if the definition leaves the conversation); `literature.get_record` for a citation |
| Prompt | This guide |
| Template | `assets/adoption-rule-output.md` |
| Input | The request and its context: the task card (sibling skill A1 or the person), who is eligible, what the usage log records, training dates, the old step, the market (NHS or other), whether the rule goes into a contract or commissioning document |
| Governance | `references/governance.md`; the rule is the person's; a rule written into a contract or commissioning profile stops for that document's owner |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. evidence-table grades a set of studies for a product's claims; this task only identifies or checks a source the person names. |

## Read the request

- **Task.** The trained task done in production. If the person offers logins, sessions or minutes as the measure, say once that these are not adoption (register CF-12.02.02.4.2.1; expert stop) and ask which task event the log records.
- **Level.** Staff (clinicians who deliver), patients (who use), or settings (wards, clinics). Each has its own definition (CS24, CS22, CS28).
- **Denominator.** Trained, eligible (expected to deliver), or settings approached. Ask which list the person holds.
- **Window and share.** The person's. Never propose numbers; if asked for a proposal, write "proposed" and give only the structure ("the share of trained users who complete the task within W days").
- **Use of the rule.** Internal, customer report, contract or NHS commissioning profile. The last two stop for the document owner.

## Workflow

### Step 1. Name the task event

Write the task from the card and the log event that shows it was done in production. If the log cannot show the task (only logins), `[GAP]`: name the event the product would need to record.

### Step 2. Choose one definition per metric

Lay out, for the level the person chose, the definitions with rows (`references/adoption-metrics.md` section 2) and ask the person to pick one per metric. State the conflict once: Proctor penetration is similar to RE-AIM reach; adoption differs between the two (research "Changes and conflicts").

### Step 3. Write the rule

Fill: task event; level; denominator; window W (person's); share (person's); as-of date convention; old step to watch; maintenance horizon if wanted (the person's M; RE-AIM uses 6 or more months, CS26, CS30). Blank fields stay blank with "ask".

### Step 4. For NHS buyers

Say that ESF Standard 16 asks for usage against an expected usage profile agreed at commissioning and for anonymized aggregate outcomes (CS61), and that pilot statements may confirm use "in line with expectation (who, how, for how long)" (CS59). The rule should be written so that it can be that profile. The profile itself is agreed by the person's owner and the commissioner.

### Step 5. Optional acceptability reading

If the person wants one, offer SUS with its scoring as restated by Hyzy et al. (UX-M-07) and the benchmarks labeled context only (UX-M-08 to UX-M-10).

### Step 6. Check the definition if it leaves the conversation

Call `verify.qualify_source {doi: "10.1007/s10488-010-0319-7"}`, then `verify.check_claim` with the definition, the quoted passage from CS39 or CS34 with a locator, and `source {source_id, tier, source_type: "literature", code}`. Read `references/tools.md` first: "supported" proves word overlap only, and it returned "supported" with numerator and denominator swapped. Confirm the direction yourself. Build the citation from `literature.get_record`.

## Build the output

Follow `assets/adoption-rule-output.md`. Answer first: the rule in one sentence, with blanks for what the person has not set. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- The rule names one definition per metric, with its row.
- Every denominator is named.
- Window, share and horizon are the person's or blank.
- No login, session or attendance is used as adoption.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Adoption of the trained task. Customer health scores and renewal belong to DH-02.02.2.x and 3.x and are the person's definitions (not sourced). Clinical outcomes the customer agreed to see belong to DH-02.02.3.x; payment tied to outcomes to Market Access (outcomes-contract-monitoring).
- Patient engagement and retention design belong to the patient engagement and digital therapeutic design packs.
