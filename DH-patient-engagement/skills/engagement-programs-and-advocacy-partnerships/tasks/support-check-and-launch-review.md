# B1 Support check and launch review

Framework task: DH-02.03.2.1, Part B, task B1. Holds the judgment the old competency left implicit: the launch rule ("pass rule") and the owner of a miss, as steps inside this task.

## What this task delivers

Two things, in this order. First, for any support the program would give patients, caregivers or patient groups: the support described in the person's words, each sourced element the compliance owner will weigh laid out against the person's facts (met as the person states it, not stated, or in tension), and the stop. Second, the launch review: the person's own launch rules applied to the A1 and A2 outputs, each rule met or missed, the owner of each miss as the person names them, and, if the person scored support options, the ranking of their scores with its swap points. It answers "is any of this something our compliance owner must decide, and are we ready by our own rules?"

Why it matters: OIG treated even a limited loaner phone as remuneration to the patient (CP-US-40); safe harbor protection needs every condition met (CP-US-07); the 2026 cap for patient engagement tools is $623 per patient (CP-US-27). These facts decide what the owner sees before a program launches.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Marketing Manager (`digital-marketing-manager`) |
| Skill | DH-02.03.2.1 Part B, Support check and launch review |
| Workflow | The steps below |
| Knowledge | `references/patient-support-rules.md`; A1 and A2 outputs |
| Tools | `analytics.mcda` (counted, only on the person's scores); `scripts/mcda_swap.py` (optional) |
| Prompt | This guide |
| Template | `assets/support-check-and-launch-review-output.md` |
| Input | The request and its context: each support item (what, to whom, value per patient per year as the person states it, cash or in kind, who recommends it, eligibility, advertised or not, duration), whether the company bills Medicare or Medicaid or makes devices, markets, the person's launch rules, owners, scores and weights if options are compared |
| Governance | `references/governance.md`; all support stops for the compliance owner |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. partner-prioritization runs the same ranking calculators but is scoped to partners and indications; call the calculator directly. |

## The rule that shapes this task: lay out, never conclude

The model never says that support is protected, permitted, within a safe harbor, low risk or compliant, and never says the reverse as a verdict either. It states each element and whether the person's facts meet it as stated, and stops. A value under the cap is one element, never protection on its own. AO 19-02 binds only its requestor (CP-US-43).

## Read the request

- **Support items.** One line each, in the person's words. Missing value, recipients or eligibility: `[GAP]`; ask once.
- **Company facts.** Device maker, drug maker, a company that bills Medicare or Medicaid, Open Payments reporter: these change which rows apply (CP-US-25, CP-US-42). Unknown: lay out each case as conditional.
- **Launch rules.** The person's. Without rules there is no launch verdict; list what A1 and A2 left open instead.
- **Options and scores.** Only if the person compares support options. Scores 0 to 4, weights summing to 1, all theirs.
- **Owners.** Compliance owner, launch owner, as named.

## Workflow

### Step 1. List the support

Table: item, recipient, value per patient per calendar year as stated, cash or cash equivalent (yes or no), recommended by a licensed professional (yes, no, not stated), eligibility rule, advertised (yes, no), duration. Never estimate a value.

### Step 2. Lay out the US elements (if US patients or Federal program business are in scope)

For each item: the AKS facts (CP-US-01 to CP-US-08), the beneficiary CMP and its exceptions (CP-US-34 to CP-US-38), and the patient engagement safe harbor elements hh-1 to hh-8 from section 3 of `references/patient-support-rules.md`. Mark each element "as you state it, met", "not stated `[GAP]`" or "in tension" (for example: a gift card is a cash equivalent against hh-3, CP-US-26; a stated 2026 value above the $623 figure is in tension with hh-5, CP-US-27). Where the item resembles a loaned device, add the AO 19-02 safeguards as the pattern OIG weighed (CP-US-39 to CP-US-41), with its reliance limit.

### Step 3. Lay out other markets

From section 7 of the reference: Germany (PC-DE-06, CP-DE-05, CP-DE-07), European patient organizations (PE-71, PE-80 [INDUSTRY]). Other markets `[GAP]`.

### Step 4. The stop

Write: "Support to patients or patient groups stops for [compliance owner as named, or owner not named]. The elements above are laid out for that decision; this draft does not say the arrangement is protected." Where the person asks for wording to patients about the support, draft only what the facts support, labeled "draft for the owner".

### Step 5. Rank options the person scored (optional)

If the person compares support options and has scored them, call `analytics.mcda` with `alternatives` (id and scores) and `criteria_weights`. Criteria must be phrased so that higher is better ("inducement exposure avoided"). Save the call and response as JSON and run `scripts/mcda_swap.py FILE` to check values and get swap weights. Report the ranking as the result of their scores, never as a recommendation, and say that the ranking does not change the stop.

### Step 6. Launch review against the person's rules

For each launch rule the person set (for example "every activity has an approved claims list", "signed agreement before any support"), write: rule, evidence from A1 and A2, met or missed. For each miss, the owner the person names, or "owner not named". No dates unless the person sets them. If the person set no rules, list the open items from A1 and A2 and ask for rules; do not invent any.

## Build the output

Follow `assets/support-check-and-launch-review-output.md`. Answer first: which support items stop for the compliance owner and the elements in tension, then the launch rules missed. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- No sentence says or implies that support is protected, permitted or safe.
- Every element carries its row; the cap is stated as the 2026 OIG figure with its basis.
- Values, rules, scores, weights and owners are the person's.
- The ranking, if any, is described as the result of their scores.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Support and launch readiness of the program only. Payer coverage of the product is Market Access; claims clearance is the review owner's.
- No legal opinion and no prediction of an enforcement outcome.
- Results after launch are DH-02.03.2.2.
