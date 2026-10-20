# A2 Technology evaluation and readiness

Framework task: Part A, task A2. Replaces the old tasks DH-01.08.1.1.1 Technology Scouting, DH-01.08.1.1.2 Fit-for-Purpose Assessment and DH-01.08.1.1.3 Feasibility Scoring.

## What this task delivers

For each technology the person names (or a scouting list built from A1 signals, labeled proposed): a fact sheet with what kind of intervention it is (WHO classification axis), its record on the registers (authorizations by register, decision dates, product codes, predicates), evidence on record (publication and trial signals, never findings), a proposed readiness level in the EU wording verbatim, the conditions and standards that would apply to its use (WHO 2019 conditions, NICE ESF deployment standards for England, IDEAL-D stage for a device innovation), the early clinical and regulatory routes that exist, and the gaps. Feasibility criteria and scores, if the person gives them, sit beside the facts as theirs. It answers "what is this technology, how far along is it on the record, and what would using it require?"

Why it matters: "fit for purpose" verdicts written from vendor decks are not repeatable. A fact sheet with a quoted readiness level, register records and named gaps lets the person reach their own verdict and defend it.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Chief Compliance Officer (`chief-compliance-officer-digital-health`), as bound to DH-01.08.1.1 in the old skill (a better-fitting expert is proposed in the build notes, not bound) |
| Skill | DH-01.08.1.1 Part A, Technology evaluation and readiness |
| Workflow | The steps below |
| Knowledge | `references/technology-evaluation-rules.md` (SP-028 to SP-057, SP-062, SP-076 to SP-079, SP-109 to SP-129; CS56 to CS68; PL110 to PL121; UK-06 to UK-08); `references/horizon-methods.md` section 3; `references/company-status.md` for a named maker |
| Tools | `regulatory-dh.list_jurisdictions` (free); `regulatory-dh.search_devices`; `regulatory-dh.get_pathway_precedents`; `literature.search_literature`; `literature.find_trial` (needs a live check); `scripts/horizon_helpers.py trl` and `signals` |
| Prompt | This guide |
| Template | `assets/technology-evaluation-output.md` |
| Input | The request and its context: the technologies (name, maker, product, K number or Basic UDI-DI if known), the person's intended use for it, markets, the person's feasibility criteria and scores if any, and A1 output if run |
| Governance | `references/governance.md`; verdicts, levels and scores are the person's |
| Catalogue job | none (no technology evaluation job in `examples/live/list_jobs_2026-10-19.json`) |

## Read the request

- **Technologies.** Named by the person. "Scout options for X" without names: build a candidate list from A1 signals, each labeled "proposed candidate" with its signal id. Never add a vendor from memory.
- **Intended use for the person.** What they would use it for and where. If not given: "intended use not given `[GAP]`"; the WHO conditions and ESF lines depend on it.
- **Markets.** England brings the NICE ESF lines; US brings the FDA routes; EU brings the AI Act and EHDS dates. If not given, ask once.
- **Feasibility criteria and scores.** Theirs. "Score feasibility" without scores: lay out facts per criterion and ask them to score; propose criteria only when asked, labeled "proposed criteria".
- **"Fit for purpose" or "readiness verdict".** The verdict is the person's. Give the facts and a proposed TRL.

## Workflow

### Step 1. Perimeter and record (counted calls only for named technologies)

Call `regulatory-dh.list_jurisdictions {}` (free) for the coverage note. For each technology, call `regulatory-dh.search_devices {query: "<product or maker>", jurisdiction: "all", limit: 25}`. Report rows by register with identifiers, decision dates and status as stored, and the "does not show" line (no AI or PCCP field, no intended use; EU decision date empty). Match across registers on identifiers, never on names (the saved Aidoc rows spell product and maker differently in the US and EU). If the device type matters, call `regulatory-dh.get_pathway_precedents {product_code}` for the count, first decision and De Novo grants (QAS: 88 decisions, first De Novo DEN170073 on 13 February 2018). A name search with no row is "lookup missed", not "not authorized" (`gap-rules.md`).

For a named maker, add the company status line (`company-status.md`): for Akili, Pear Therapeutics, Big Health and Aidoc, the status already read (section 6), cited by filing or register name and date with the row id after it; for any other maker, "Status: [GAP]: not read" with the filings to open. Never infer from press. State the product's current FDA listing holder apart from the company that was authorized (for example Somryst: cleared to Pear Therapeutics, FDA 510(k) K191716, 23 March 2020 (SP-165); listed today by Nox Medical, FDA registration and listing, listing created 18 December 2024 (SP-167)).

### Step 2. What kind of intervention

Name the WHO classification axes that apply (SP-055, SP-056): the health system challenge, the digital health intervention, the service or application type, in words. Codes are "`[GAP]`: look up in the WHO classification (SP-054)". If the person asks whether it counts as an innovation, apply the Oslo Manual definitions (SP-036 to SP-041) to the facts they give, labeled "proposed".

### Step 3. Proposed readiness level

Pick the EU level whose words the record supports and quote it with `python3 scripts/horizon_helpers.py trl N` (SP-028 to SP-031). Write the fact behind it (for example "510(k) clearance K261317, 14 May 2026" is a register fact; whether it supports the level 9 wording "Actual system proven in an operational environment" is the person's reading, because a clearance does not show use in operation; the level is "proposed"). Never use NASA flight terms for 7 to 9 (SP-035). Keep TRL, regulatory status and evidence in separate columns; no crosswalk exists in the sources.

For a device innovation still in development, name the proposed IDEAL stage (PL111, PL112) and the proportionality rule (PL113) with [PAPER] DOI 10.1097/SLA.0000000000004907.

### Step 4. Evidence on record

Call `literature.search_literature {query: "<technology and use>", limit: 20}`. List records as publication signals (DOI, year, type as stored, library design label marked as a draft). Do not summarize findings; review method routes to `dh-clinical-development` literature-and-real-world-evidence-review. For a key RCT, `literature.find_trial` (needs a live check). Never write that evidence "proves" anything.

### Step 5. Conditions, standards and routes that would apply

From `technology-evaluation-rules.md`:
- WHO 2019 conditions for the intervention type (SP-049 to SP-053), as conditions, never as a judgment that they are met.
- England: the ESF standards that bear on deployment (CS59 to CS66, CS67, CS68), as questions the person's evidence must answer; tiers are `[GAP]` here and route to `dh-access-and-value` reimbursement-evidence-support.
- Early clinical and regulatory routes that exist (EFS, TAP, RAPID, IDAP, AI Airlock, Innovation Office, EHDS secondary use; SP-109 to SP-126, UK-06 to UK-08, SP-071, SP-072), with status as read. Eligibility is for the owner the person names for regulatory matters; the pathway routes to `dh-regulatory-and-quality` regulatory-pathway-and-classification or ai-ml-device-pathway-and-change-control. Whether it is a device is the developer's call (SP-129).
- Dated regime changes that touch it (AI Act dates EU-19; EHDS SP-068 to SP-073).
- For a UK or England use, always one line in the short answer: MHRA AI Airlock is a regulatory sandbox for AI-enabled medical devices (UK-06), phase 3 announced 6 October 2026 (UK-07); innovator case-study reports are not MHRA guidance (UK-08); eligibility is the regulatory owner's.

### Step 6. Feasibility facts and the person's scores

Lay out one row per criterion the person named (any example criterion the model offers is labeled "proposed"): the facts from Steps 1 to 5 that bear on it, with ids, and the person's score if given. Check the criteria against SP-076 to SP-079 ([PAPER] Marsh 2016, DOI 10.1016/j.jval.2015.12.016, [WF]) and raise overlaps as questions. Ranking several technologies runs in B1 on these scores. Without scores, no ranking and no verdict.

## Build the output

Follow `assets/technology-evaluation-output.md`. Short mode answers first: per technology, its record in one line, the proposed TRL in the EU wording, the two facts that most limit a verdict, and what the person must decide. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words with `python3 scripts/horizon_helpers.py words ANSWER.md` (counts the whole answer except the calls list, and leaves out the Source, Rows and Retrieved columns); without code execution, count the same way by hand. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop, the company status line or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- TRL quoted verbatim in the EU wording with its row, labeled "proposed"; no NASA flight terms.
- Register facts have identifiers, dates and retrieval dates; "lookup missed" is not "not authorized".
- No verdict, score, probability, price or market size from the model; no "validated", "proven", "safe", "effective" or "compliant".
- Every named maker carries the company status line; the current FDA listing holder is stated apart from the company authorized.
- Example criteria labeled "proposed"; for UK or England use, the AI Airlock line is present.
- Every fact names its source in plain words with its date, then the row id; never a row id alone.
- [PAPER] rows carry their DOI; [WF] rows say so; abstract-only rows say so.
- The record line is the very last line of the answer; the calls list and the one-line offer of the full version come before the record block: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Ranking technologies or choosing one: B1, on the person's scores.
- Device status and pathway: `dh-regulatory-and-quality` regulatory-pathway-and-classification; AI change control: `dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control.
- Evidence review method: `dh-clinical-development` literature-and-real-world-evidence-review.
- Prototypes and experiments to test an option: `strategic-vision-and-options` (this pack).
- Partnering with the technology's maker: `dh-go-to-market` channel-and-partner-design; investing in it: `company-and-evidence-assessment` (this pack).
