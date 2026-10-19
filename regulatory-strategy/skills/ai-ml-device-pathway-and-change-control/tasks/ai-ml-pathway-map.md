# A1 AI/ML pathway map

Framework task: DH-03.03.1.1, Part A, task A1. Replaces the earlier "AI/ML Pathway Selection" section.

## What this task delivers

A sourced, dated map of the routes and rules that apply to an AI-enabled device software product in the US, the EU and the UK: the candidate route per jurisdiction with the arguments for each, whether a change control plan mechanism exists and in what form, which AI Act obligations apply and from which date as amended, and what comparable AI devices went through, from their own records. It answers "what applies to us, and what did others do?"

Why it matters: AI rules moved in 2025 and 2026. The FDA PCCP guidance was reissued on 18 August 2025, the AI lifecycle guidance is still a draft, the AI Act high-risk dates for devices moved to 2 August 2028 by Regulation (EU) 2026/1744, and the MHRA has announced, not published, PCCP guidance. A plan built on the old dates or on a draft read as final goes wrong in ways nobody notices until a reviewer does.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | SaMD Regulatory Affairs Director |
| Skill | DH-03.03.1.1 Part A, AI/ML pathway map |
| Workflow | The steps below |
| Knowledge | `references/ai-ml-routes.md`; `references/AI_ML_REGULATION.md`; `references/REG_PATHWAYS_SUBMISSIONS.md`; library device records |
| Tools | `regulatory-dh.list_jurisdictions`, `search_devices`, `get_pathway_precedents`, `find_predicates`, `get_authorization`, `classify_product`; `verify.build_record` on sign-off; `scripts/precedent_table.py` (optional) |
| Prompt | This guide |
| Template | `assets/pathway-map-output.md` |
| Input | The request and its context: product, intended use, target jurisdictions, the person's class view if any, known competitors or product codes |
| Governance | `references/governance.md`; the class and route are the regulatory owner's |

## Read the request

Decide four things. Ask at most one question, and only if the intended use is unknown; otherwise state your assumption and proceed.

- **Intended use and user.** Everything depends on it. If it is missing, ask for one sentence: what the software does, for whom, with what output (notify, quantify, diagnose, recommend treatment).
- **Jurisdictions.** Keep to those named. If none, cover US, EU and UK and say so.
- **Short or full.** A direct question ("does the AI Act apply to us?") gets short mode. "Memo", "board", "full map" gets full mode.
- **Precedent wanted?** "Who else", "what did X do", a product code, a competitor name: run step 4.

## Workflow

### Step 1. Know what the library holds

Call `regulatory-dh.list_jurisdictions` (free). Keep, per jurisdiction, the record count, last load and scope line. It tells you that EU rows carry no decision date, that UK and CH registrations are not loaded, and that Canada rows drop out of software-only searches.

### Step 2. Lay out the US route arguments

From `references/ai-ml-routes.md`, United States:

1. Is it a device? If the person thinks it may be non-device CDS, set out the four criteria with the 29 January 2026 guidance rows [RP US-19 to US-23]. Image or signal analysis fails criterion 1.
2. Route arguments: predicate available (510(k)), novel with no predicate (De Novo), class III (PMA) [RP US-04 to US-14]. Use step 4 to show whether the product code has 510(k) precedents.
3. Change control: section 515C and the PCCP final guidance of 18 August 2025, which applies on all three routes [AI US-01, US-02, US-15 to US-18].
4. AI-specific documentation: the AI lifecycle guidance, draft of 7 January 2025, on CDRH's FY 2027 A-list [AI US-19 to US-22]. Say "draft".

Write each as "argument for" and "argument against" with the row. Do not write "the route is". Write "the regulatory owner decides between".

### Step 3. Lay out the EU and UK position

**EU.** Set out the Rule 11 arguments for the class [RP EU-02 to EU-05]. Then the AI Act: if the device is an AI system and its MDR class needs a notified body, MDCG 2025-6 Table 1 puts it in high-risk [AI EU-27, EU-28]. Give the date table from `ai-ml-routes.md` with the amending act on every line. In short mode, keep two date lines whenever the person asks when the AI Act applies: high-risk requirements from 2 August 2028 [AI EU-19], and Article 4 AI literacy already applying since 2 February 2025, with the wording softened by Regulation (EU) 2026/1744 to "take measures to support" [AI EU-15, EU-20]. Literacy is not a "secondary rule" to cut. If the device is already on the market, add the legacy rule [AI EU-22] and the open question on what counts as a significant design change `[GAP]`. State that EU PCCP guidance is not published and give the Article 43(4) counterpart [AI EU-05, EU-30, EU-31].

**UK.** CE acceptance dates (MDR devices 30 June 2030 [RP UK-03]; MDD 30 June 2028 [RP UK-02]; up-classified [RP UK-04]), the different GB software classification [RP UK-14], and the PCCP position: announced in the 6 October 2026 government response, draft guidance intended by December 2026, none published [AI UK-04]. Nothing about GB PCCPs is in force.

### Step 4. Find comparable AI devices, by record

Run this when the person names a competitor or product code, or asks for precedent.

- **By manufacturer or product name:** `regulatory-dh.search_devices` with `query` and `jurisdiction` "all", `limit` 10. Confirm identity on identifiers (K number, Basic UDI-DI), not names: the same product is spelled differently across jurisdictions. When a manufacturer has several records in the relevant product code, report the most recent decision first, with the count of records in that code. Do not pick one by name match alone.
- **By product code:** `regulatory-dh.get_pathway_precedents` with `product_code` (for example "QAS"). Report decisions by pathway and year, the De Novo grants, and the median calendar days between stored submission and decision dates, labeled as such.
- **Predicate chain** for a 510(k) or De Novo the person cares about: `regulatory-dh.find_predicates` with `reference`. Report the chain back to the De Novo that created the device type, with dates.
- **By input modality:** if the intended use names an input (for example non-contrast CT), run `search_devices` with that term (for example "NCCT") in the product code. Report the records whose own name or predicate chain states that input, and run `find_predicates` on the most recent one. State modality only where the record states it.
- Optional: save the `search_devices` output and run `scripts/precedent_table.py FILE` for a dated table with days to decision.

Describe each device only by its record: name, manufacturer, route, class, product code, decision date, predicates, source. The records carry no AI or PCCP field. Do not say a precedent "uses AI" or "has a PCCP" unless the person shows it on FDA's AI-enabled device list or in its decision summary; offer to check the list. Context line for the list: FDA's hub says over 1,600 AI-enabled devices authorized as of September 2026; the list's CSV has 1,614 rows, current as of 4 September 2026, latest decision 29 June 2026; FDA says it is not comprehensive [AI US-24 to US-26, US-34, US-35].

### Step 5. For a product already on file, read its record

If the person names their own authorized product: `regulatory-dh.get_authorization` with the K, DEN or P number or Basic UDI-DI. Read each jurisdiction from the row that holds it. Do not use `get_market_status` or the report's market-status block for cross-jurisdiction status (`references/tools.md`). For a new product, `classify_product` returns no record; do not spend a call on it unless the person asks.

### Step 6. Classify every gap

Use `references/gap-rules.md`. In short mode, one line per class.

## Build the output

Follow `assets/pathway-map-output.md`. Short mode for a direct question: the answer, one table by jurisdiction, at most three gaps, the record line. Full mode adds the argument tables, the AI Act date table, the precedent table and sources.

## Before you hand it over

- Every rule carries its row id and its draft or final status with date.
- Every AI Act date names the act that set it.
- No route or class is stated as decided. The wording is "the regulatory owner decides between".
- Precedents are described only by their records.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Drugs, biologics, wellness apps and general-purpose AI that is not a medical device are out of scope. Say so in two lines and stop.
- Jurisdictions outside the US, EU and UK: the references hold no AI rules for them `[GAP]`; the library may hold registrations (Canada, Taiwan). Say which.
- No forecast of review outcome or time beyond the published goals and observed averages.
