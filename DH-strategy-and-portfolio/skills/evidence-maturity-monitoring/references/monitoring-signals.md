# Monitoring signals: what moves an evidence read, and what only looks like it

Interpretive reference for all three tasks. Rows come from `diligence-research.md` (DL, read 20 October 2026), `clinical-study-and-rwe-research.md` (CV), `hta-submissions-research.md` (DE and UK), `health-economics-methods-research.md` (HE-) and `customer-success-implementation-research.md` (CS), read 19 October 2026. Connector behavior comes from saved outputs of 19 October 2026 (`tools.md`).

The rule behind the file: a later score that differs from an earlier one is a fact about two library responses. It becomes a statement about the company's evidence only when the record behind the changed input is read. No source sets a benchmark for how fast evidence should mature; the person's rules judge the movement.

## 1. Three kinds of change (the classes `scripts/maturity_diff.py` prints)

| Class | What changed | What it means | What it does not mean |
|---|---|---|---|
| INPUT | A component input: authorizations, registered studies naming the brand, completed interventional studies, randomized studies, results posted, active studies, cleared product names | The library now holds a different record set for the company | That the company's evidence improved or weakened: read the record first |
| METHOD | Rubric version, assessable maximum, a component moving between assessable and excluded, a component added or dropped | The convention changed | Anything about the company |
| COVERAGE | Loaded record counts, a source moving into or out of "not loaded" | The library's perimeter changed | Anything about the company |
| RESOLUTION | The same reference resolved to a different company, or two references matched by company name | The two runs may cover different filers or products | A trend; the runs are not comparable as they stand |

The script also prints POINTS lines (which component's points moved; the INPUT or METHOD line beside it says why) and NONE when nothing differs.

The library states its formula as "score = round(100 x points earned / assessable maximum); a component whose source is not loaded is excluded from the maximum, not counted as zero" (rubric v1, 7 October 2026). So a source being loaded can raise or lower a score with no new evidence: a METHOD or COVERAGE change.

## 2. Record events that can sit behind an INPUT change

| Event | What the record shows | Clock or rule that applies | Rows |
|---|---|---|---|
| A new FDA authorization | Record with decision date; a 510(k) is a clearance, not an approval | Public registration data lag uploads, generally weekly (DL-129) | DL-128, DL-129, US-65, US-66 |
| A new registered trial | Registration date; ICMJE requires registration at or before first enrollment | US applicable trials: within 21 days of first enrollment | CV132, CV141 |
| Results posted | Summary results in the registry | US: no later than 1 year after primary completion (CV145), later for certified unapproved products (CV146); WHO norm 12 months, journal publication indicative 24 months (CV140). Primary completion defined in CV144 | CV140, CV144 to CV146 |
| A trial terminated, withdrawn or suspended | The library raises a risk flag ("2 registered studies terminated, withdrawn or suspended", GAIA AG, 19 October 2026) | None; the reason is not in the flag | `tools.md` |
| DiGA listing, change or delisting (Germany) | Announced in the Federal Gazette, quarterly as a rule; refusals are not announced | DiGA studies registered and published within 12 months of completion (DE14); refusals not disclosed (DE32) | DE14, DE30 to DE32 |
| DiGA usage data | The 2026 DiGAV amendment (in force 1 February 2026) covers usage-based outcome reporting; studies collect duration and frequency of use | Stated with the instrument | DE1, DE15 |
| DiGA trial-listing extension | An extension of a trial listing exists (DE25 sets its fee); trial listing lasts up to 12 months (DE19) | Stated with the instrument | DE19, DE25 |
| Company status change | 8-K Item 1.03 (bankruptcy or receivership), 2.01 (completed acquisition), 3.01 (listing notice or withdrawal), 5.01 (change in control); Form 25 (delisting); Form 15 (SEC reporting stopped); Companies House `company_status`; German insolvency notices. Not in the library: read directly (`company-status.md`) | 8-K within four business days (DL-135); Form 25 effective after 10 days (DL-143); Form 15 and Form 25 are not dissolution (DL-144; DL-149 (inference)); German notices deleted after six months (DL-166 (inference)) | DL-135 to DL-168 |

A record's silence is not an event: "no change recorded" in a change log is a statement about the log, not the company (section 4).

## 3. Framework changes that can move a proposed level

| Framework | What to check at each reread | Rows |
|---|---|---|
| NICE ESF | Version and last update (last updated 9 August 2022 when read); a changed intended purpose can change the tier | CS56, UK12, HE-082 to HE-084 |
| Evidence DEFINED | The authors plan updates every 6 to 12 months (DL-113); a new graded review the person brings can change the level | DL-107 to DL-113 (DOI 10.1038/s41746-023-00836-5) |
| V3 | A new verification, analytical or clinical validation study for a sensor-based measure | CV155 to CV159 (DOI 10.1038/s41746-020-0260-4) |

A level the person confirmed stays theirs. A new proposed level is labeled "proposed" and is not applied until the person confirms it.

## 4. Change log limits (pipeline-and-market-monitoring's tool, read here for dating)

`diligence-dh.get_deltas` returned, on 19 October 2026: log first entry 12 October 2026, last sweep 19 October 2026, and limits: "the since filter uses event dates (filing signal_date, authorization decision_date, study start_date, safety event_date), not observed_at (load time)"; "the change log began on the first_entry_at date; older clearances loaded before the log existed may have no entries"; "no change recorded is a statement about in-window event-dated log rows up to last_sweep_at". Report "no change recorded in the library's log since DATE (log started 12 October 2026)", never "nothing happened". When the period asked for starts before 12 October 2026, say the log does not cover the earlier part and offer the company's dated primary filings (EDGAR filing list) and authorization records (FDA decision dates) for that part instead of reporting "no change".

## 5. What does not count as evidence movement

- A score change classed METHOD, COVERAGE or RESOLUTION.
- A new framework level the person has not confirmed.
- Funding: funding has not tracked evidence in the samples studied (DL-117, DOI 10.2196/37677; DL-124, DOI 10.1371/journal.pone.0323390). A new Form D is a filing, not evidence.
- A vendor funding database entry: such databases may lack full funding details (DL-125 (inference)). A press release or deck not backed by a record does not count by this skill's rule (no row).
- A company status (bankruptcy, delisting, acquisition) taken from press or memory: status counts only when read from the company's filing or register (`company-status.md`).
- A days-since-last-change figure compared with a norm: no benchmark is sourced.
