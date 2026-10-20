# A2 Complaint handling and vigilance

Framework task: DH-03.02.4.1, Part A, task A2. Replaces the earlier "Complaint record" section.

## What this task delivers

A complaint record and a reportability assessment for each jurisdiction where the product is on the market: whether it meets the complaint definition, which reporting criteria the facts touch in the EU, Great Britain and the US, the latest permitted date for each possible report, what is still unknown, and what happened to comparable products in public records. It answers "is this reportable, where, and by when?" and leaves the decision with the reporting owner.

Why it matters: the clocks start at awareness, not at the decision. In the EU the awareness date is day 0 and the count starts the next day (VG12); in the US a 5-day report counts work days (VG18, R9). A late decision does not move the clock, and the record has to show the deliberation (VG21).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | QA Manager, Software (V&V) |
| Skill | DH-03.02.4.1 Part A, Complaint handling and vigilance |
| Workflow | The steps below |
| Knowledge | `references/vigilance-clocks.md`; rows QS8, QS11, QS12, VG1 to VG29, R9 to R13 |
| Tools | `regulatory-dh.list_jurisdictions` (free), `regulatory-dh.search_safety_events` (two or three calls at most); `scripts/reporting_clock.py` |
| Prompt | This guide |
| Template | `assets/complaint-and-vigilance-output.md` |
| Input | The request and its context: product, version, markets, what was reported, by whom, when the first employee or representative received it, any harm, any action already taken |
| Governance | `references/governance.md`; reportability is the reporting owner's decision |

## Read the request

- **Product, version, markets.** Which of EU, GB, US the product is on. Only those jurisdictions get a clock.
- **Awareness date.** EU, GB and US 30-day: the date the first employee or representative (including an outsourced complaint handler) received the information (VG11, VG19). If the person gives a later date (for example when quality logged it), use the first receipt and say why. US 5-day: the date a manager or supervisor over regulatory, scientific or technical staff learned that remedial action is needed (VG19); ask for it, and if unknown show both dates and do not call the 5-day limit passed. Without an awareness date, no clock: write `[GAP]`.
- **The facts of the event.** What happened, any harm, the outcome, whether a decision was made on the device's output, whether the issue could recur.
- **Mode.** "Is this reportable?" gets short mode. A full complaint file entry gets full mode.

## Workflow

### Step 1. Record the complaint

Check the definition (VG16). Fill the record with the seven US items where the US applies (QS11): device name, date received, UDI or UPC, complainant contact (held by the person, never sent to the library), nature and details, correction or corrective action, reply. Mark missing items `[GAP]`. If a similar complaint was already investigated, say a new investigation may be skipped only with a recorded justification (QS12).

### Step 2. Lay the facts against the criteria, per jurisdiction

Use the tables in `vigilance-clocks.md`. For each jurisdiction, list each criterion and whether the facts given meet it, do not meet it, or are not known:

- **EU:** incident (VG1); serious incident, including "might have led" and indirect harm from a decision based on wrong device output (VG2, VG14, VG15); death or unanticipated serious deterioration; serious public health threat; whether an FSCA is planned (VG3, VG8).
- **GB:** the same three limits (VG28); GB definitions and day counting are `[GAP]`.
- **US:** serious injury (R10), malfunction (R11), caused or contributed (R12), likely to cause or contribute if it recurred (VG17); remedial action needed to prevent unreasonable risk of substantial harm (5-day, VG18); a correction or removal to reduce a risk to health (VG22, R13) or an exempt action (VG23).

Do not conclude. Write "criteria met on the facts given", "not met on the facts given", or "unknown: needs X". Where the EU facts are uncertain, state the MDR rule: if unsure, report within the deadline (VG7).

### Step 3. Compute the clocks

Run `scripts/reporting_clock.py --date <awareness date> --event <the event types still open> --as-of <today>`. Run `us-806-correction` separately with the initiation date of any correction, and `us-mdr-5` separately with the management awareness date (VG19). If reportability became clear later than awareness, add `--reportability-date` and show both EU and GB dates, with the VG13 note. Without code execution, count by hand from `vigilance-clocks.md` section 3 and show the count. Federal holidays are excluded from work-day counts by definition (R9); the helper reads the OPM list for 2026 and 2027 (R14) by default and names any holiday it excluded. If the window runs outside those years, the helper warns: pass `--holidays` with the person's list, or state that the date may be later.

### Step 4. What happened to comparable products (optional, public records)

Call `regulatory-dh.list_jurisdictions` once to show which jurisdictions hold safety events (the EU holds none). Then call `regulatory-dh.search_safety_events` with a single product word or a comparable manufacturer, for example `{product: "insulin", since: "2025-01-01", limit: 5}` or `{manufacturer: "Dexcom", limit: 10}`, and `{product: "<word>", jurisdiction: "UK"}` for MHRA alerts. Describe each event only by what its record states: product and version, date as stored, class, the defect in the summary's words, source URL. Never infer another firm's cause, CAPA or reporting. Read the pitfalls in `tools.md` first (phrase matching, loose software filter, wrong MHRA manufacturer field).

### Step 5. Investigation and what not to touch

State the MDR rule that the device or samples are not altered in ways that affect cause analysis before the authority is informed (VG10), and that the risk file is reviewed when the event brings new information (QS22, EU15). The investigation and any CAPA go to B1.

### Step 6. Who decides, and what is drafted

Name the reporting owner the person gave; if none, "owner not named". If the owner asks for it, draft the deliberation note for the event file (VG21): facts, criteria, conclusion left blank for the owner. Any MIR, MDR report, 806 report or field notice is a draft for the owner.

## Build the output

Follow `assets/complaint-and-vigilance-output.md`. Answer first: the earliest open date and what it is for, then the criteria per jurisdiction, the unknowns, the clock table, comparables, and the decision owner.

## Before you hand it over

- Every clock shows its rule, its anchor date and the count.
- No event is called "not reportable"; criteria are "met", "not met" or "unknown" on the facts given.
- Complainant and patient details never went into a library call.
- Comparables are described from their records only.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- The model does not decide reportability and does not submit anything.
- No legal opinion on a regulator's position.
- Drugs, biologics and wellness apps are out of scope; for combination products, say the drug side is outside this skill.
