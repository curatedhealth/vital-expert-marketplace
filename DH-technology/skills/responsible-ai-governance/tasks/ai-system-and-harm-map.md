# A1 AI system and harm map

Framework task: DH-01.04.1.1, Part A, task A1. Carries the old task "DH-01.04.1.1.1 Bias question" (name the harm and the group this model could disadvantage; name the error that harms; name a group you cannot see in the data and mark it [GAP]; never claim fairness from overall accuracy).

## What this task delivers

For each AI system the person names: the decision it influences and its role (informs, augments, replaces), the users, the error that harms (false alert, missed deterioration, denied access) and who bears it, the groups the person will compare, the groups the data cannot show (`[GAP]`), the bias sources to look for, and the rules that may apply in the person's markets with their standing and date. It answers "what could this system do to whom, and which rules should we read before we test it?"

Why it matters: a model with good overall accuracy can hide poor performance in a subgroup (FDA draft of 7 January 2025, DA-43, draft), and a group nobody wrote down is a group nobody tests. NIST asks that risks which cannot be measured are documented rather than dropped (NIST AI RMF 1.0, January 2023, MEASURE 1.1, DA-12, voluntary).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | `ai-ml-governance-director` (old DH-01.04.1.1.1). Work as an AI governance analyst who maps and cites |
| Skill | DH-01.04.1.1 Part A, AI system and harm map |
| Workflow | The steps below |
| Knowledge | `references/responsible-ai-rules.md` sections 1, 2 and 5; rows DA-05, DA-08, DA-10 to DA-12, DA-19 to DA-21, DA-25, DA-28, DA-34, DA-115, DA-116, DA-120, PE-113 to PE-115, UX-US-57, UX-US-58, UX-US-66, UX-US-72, UX-US-73, CV125, AI EU-19, AI EU-27, DA-67, EN-111, CP-UK-05 to CP-UK-10 |
| Tools | Optional: `regulatory-dh.search_safety_events` for comparable AI devices the person names; `verify.qualify_source` and `verify.check_claim` for a paper or vendor document the person brings; `verify.build_record` when the record leaves |
| Prompt | This guide |
| Template | `assets/ai-system-and-harm-map-output.md` |
| Input | The request and its context: system name, intended use, decision, users, setting, markets, data available (which group attributes exist), who builds and who deploys it |
| Governance | `references/governance.md`; legal readings and device questions stop or route |
| Catalogue job | none |

## Read the request

- **One system or an inventory.** One system: one map. Several: one row per system, then a map for the one the person picks.
- **Markets.** US, EU, England, other. They decide which rows are cited. Not given: ask; meanwhile cite none of the market-specific rows.
- **Who the person is.** Developer, deployer (hospital, health system), pharma sponsor using AI in a trial, or a vendor of certified health IT. Not given: write "not given" and lay out the rules by role.
- **The data.** Which group attributes exist in the data (age, sex, language, race and ethnicity, insurance, site). This decides which groups are visible.
- **Generative AI.** If the system generates text or images (a discharge summary drafter, a chatbot), add the NIST AI 600-1 risks (DA-19 to DA-21) and the WHO LMM rows (DA-30 to DA-34).

## Workflow

### Step 1. Write the system back

Name, intended purpose, decision influenced, users, setting, the person's markets, in the person's words (NIST MAP 1.1, DA-10). For decision support, the decision-making role as the person states it: informs, augments or replaces (45 CFR 170.315(b)(11), UX-US-57). Missing: "not given".

### Step 2. The error that harms, and who bears it

For each output, name both errors in the person's setting (a missed deterioration and a false alert; a denied referral and an unnecessary one) and who bears each (patient, clinician, payer). Where the output allocates something scarce (a care-management slot, a referral), say that fairness concerns apply to such polar decisions (Paulus and Kent 2020, DOI 10.1038/s41746-020-0304-9, DA-116). Which error matters more is the person's call.

### Step 3. Groups: visible, compared, unseen

- Groups the person will compare, from attributes present in the data.
- Groups the person cares about that the data cannot show: "[GAP]: not visible in this data", each one, kept in the record (DA-12).
- Where the decision support tool uses race, color, national origin, sex, age or disability as an input and the organization may be a Section 1557 covered entity: the duty to identify such tools and mitigate the risk of discrimination (45 CFR 92.210, PE-113, PE-114; paragraphs (b) and (c) within 300 days of 5 July 2024, PE-115). Whether the organization is covered: "for your legal owner".
- Known health inequalities between sociodemographic groups in the condition, if the person has them (TRIPOD+AI item 3c, CV125, DOI 10.1136/bmj-2023-078378).

### Step 4. Bias sources to look for

One line each, tied to the person's system: systemic, computational and statistical, human-cognitive (NIST AI RMF, DA-08); label bias where the outcome is recorded differently across groups, for example a diagnosis that depends on access to testing (Rajkomar 2018, DOI 10.7326/M18-1990, DA-115; Paulus and Kent 2020, DA-120); feedback loops where outputs feed future inputs (AI Act Art 10(2)(f), DA-48; Art 15(4), DA-63, EU only); automation bias in the users (FDA CDS guidance, 29 January 2026, UX-US-72; WHO LMM guidance, DA-34). Generative systems: confabulation, harmful bias or homogenization, human-AI configuration (NIST AI 600-1, July 2024, DA-19 to DA-21).

### Step 5. Events on comparable devices (optional)

Only if the person names comparable AI devices or their manufacturer: `regulatory-dh.search_safety_events` with `manufacturer` (short form) and `since` the person gives, `limit` 10. Keep a row only if its title or summary names the product or the comparable device; count the rest as "returned, not about these devices". MAUDE counts are reports, not confirmed events, never attributed to a company (`references/tools.md`). Describe each kept event only by what its record states; never judge its relevance to the person's model. An empty result says nothing about fairness.

### Step 6. Rules that may apply, by market and role

From `references/responsible-ai-rules.md` sections 1, 2 and 5, for the person's markets only, each with its standing and date:

- **All markets:** NIST AI RMF (voluntary, DA-01 to DA-16); WHO principles (DA-24 to DA-29); for generative AI NIST AI 600-1 (DA-17 to DA-21).
- **US:** 45 CFR 92.210 for covered entities (PE-113 to PE-115); 45 CFR 170.315(b)(11) source attributes for certified health IT developers (UX-US-54 to UX-US-59), with HTI-5 proposing removal (UX-US-60, proposed only); FDA CDS guidance of 29 January 2026 (UX-US-64 to UX-US-73): patient-facing recommendations meet the device definition (UX-US-73) and time-critical decisions do not meet Criterion 4 (UX-US-66), so device status routes out; the FDA AI-enabled device draft (DA-35 to DA-46, draft).
- **EU:** AI Act high-risk duties from 2 August 2028 for MDR and IVDR devices that need notified-body assessment and from 2 December 2027 for Annex III systems (AI EU-19, DA-67); MDCG 2025-6 maps MDR class IIa and above as high-risk (AI EU-27, not legally binding); AI literacy measures already apply (AI EU-14, AI EU-20); GDPR DPIA before high-risk processing (EN-111, EN-112).
- **England:** DCB0129 for the developer and DCB0160 for the deploying organization (CP-UK-05 to CP-UK-10); DTAC as best practice in procurement (CP-UK-01 to CP-UK-04).
- **AI in a medicinal product trial:** EMA reflection paper (DA-68 to DA-75).

Whether the system is a device, its class and whether it is high-risk under the AI Act are not decided here: `dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control.

## Build the output

Follow `assets/ai-system-and-harm-map-output.md`. Answer first: the decision and the error that harms, the groups compared and the groups unseen, and the rule with the earliest date that applies in the person's market. Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/subgroup_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every unseen group is listed as `[GAP]`, none dropped; no claim of fairness from overall accuracy.
- Only rows for the person's markets; each with standing and date; drafts and proposals labeled.
- No statement that the system is or is not a device, high-risk, or covered by a law; legal readings "for your legal owner".
- Events kept only where the record names the product or comparable device; excluded rows counted.
- `python3 scripts/subgroup_check.py words ANSWER.md` prints "within the short-mode cap".
- Every fact names its source and date in plain words with the row id after it; [PAPER] rows carry their DOI.
- The record line is the very last line; the calls list and the offer of the full version come before the record block: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Device status, class, AI Act high-risk status of a device: `dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control.
- Who is reached by the product and inclusive design: `dh-patient-and-user-experience` health-equity-and-inclusive-design.
- Security threats to the model and data: `dh-technology` cybersecurity-and-privacy-by-design.
- Running the test: A2 in this skill.
