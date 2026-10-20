# Horizon scanning: method, signals and dated changes

Interpretive reference for task A1 (and the scenarios in B1). Every rule cites its row in `strategy-and-portfolio-sources.md` (SP), `ai-ml-regulation-research.md` (US, EU, UK, IM) or `diligence-research.md` (DL). Rows marked [PAPER] carry their DOI; rows marked [WF] were read through a summarizer: say so whenever a rule rests on one.

## 1. What a horizon scan is, in the sources

| Rule | Rows |
|---|---|
| Horizon scanning systematically searches for and analyzes signs of important developments in order to plan ahead; in healthcare the developments include medicines, devices, diagnostics and digital health tools | SP-001, SP-002 |
| The NIHR Innovation Observatory method uses a defined scope and prespecified methods, and catches change at emerging, transitional or imminent-to-launch stages (the IO's own summary of its paper; the paper itself was not read) | SP-004 |
| Records are extracted from trial registries, industry and medical databases, triangulated, and monitored to trigger notifications | SP-005 |
| Early awareness and alert methods run in four phases: identification; filtration and prioritization; assessment; dissemination ([PAPER] Packer 2015, DOI 10.1017/S0266462315000100) | SP-009 |
| Identification can be active, passive or both ([PAPER] Packer 2015, DOI 10.1017/S0266462315000100) | SP-011 |
| Device scanning systems use a reactive, pro-active or hybrid identification model; prioritization is usually by committee, by scoring or debate ([PAPER] Ormstad 2023, DOI 10.1017/S0266462323002684) | SP-013 |
| Device systems most often look from about 3 years to a few months before market entry ([PAPER] Ormstad 2023, DOI 10.1017/S0266462323002684) | SP-014 |
| Reactive systems tend to catch devices only at or near approval and are less systematic ([PAPER] Ormstad 2023, DOI 10.1017/S0266462323002684) | SP-015 |
| Device scanning is resource intensive and needs a dedicated, skilled team ([PAPER] Ormstad 2023, DOI 10.1017/S0266462323002684) | SP-016 |
| EMA scans trials, patents, publications, technology reports, research funding calls and stakeholder interactions; experts review and prioritize; reports assess the landscape, regulatory challenges and preparedness | SP-017 to SP-019, SP-022 |

How the skill uses it: A1 follows the four phases. Identification is the library calls plus the person's own sources; filtration applies the person's scope and filters; prioritization is the person's (scores or debate, SP-013), ranked by `analytics.mcda` or `analytics.rice` only on their scores (B1); assessment is A2 and B1; dissemination stops for the owner (`governance.md`). The time horizon is the person's. Ormstad's 3 years to a few months (SP-014) describes device systems studied in that paper; it is context, never the person's horizon.

## 2. Signal and trend: the rule this skill enforces

- **Signal:** one sourced, dated record. It has a source (register entry, filing, publication record, registry entry, regulator page or legal act), an event date (decision, filing, publication or application date), a retrieval or read date, and a line saying what the record does not show. A signal without a source or a date is not a signal; it is a lead to check.
- **Trend:** the person's interpretation of several signals ("AI triage clearances are accelerating"). The model may offer a reading only when asked, labeled "proposed reading", with the signal ids it rests on and the signals that cut against it. Counts by year (for example `get_pathway_precedents` by_year) are signals; whether they make a trend is the person's call.
- **Press and vendor claims:** a press release, news item, conference talk or vendor deck is not a source in this skill (the research rules exclude news, vendor and blog pages). It becomes a lead: name the record that would confirm it (a 510(k) or De Novo number, an EUDAMED Basic UDI-DI, a trial registration, an 8-K item, an Official Journal act) and look that record up. Until the record is read, the item is "lead, not a signal: record not read [GAP]".
- **Forecasts:** the model gives no probability that a technology will be cleared, adopted or reimbursed, and no date by which it will happen. A development success rate is quoted only as context with its counting method (`scenario-and-decision-rules.md` section 3).

## 3. Signal sources and what each does not show

| Signal type | Library call or source | What it shows | What it does not show | Rows or tools.md |
|---|---|---|---|---|
| Authorization decision (US) | `regulatory-dh.search_devices` | Product, maker, pathway, decision and submission date, product code, predicates, FDA URL | Whether the device uses AI or carries a PCCP; intended use text; clinical effect; uptake | `tools.md`; US-24, US-25 |
| Authorization (EU) | `regulatory-dh.search_devices` with `jurisdiction: "EU"` | Product, maker, class, "On the EU market" or "No longer placed", Basic UDI-DI | Decision date (empty on all 3,142 EU rows on 19 October 2026); a device page URL | `tools.md` |
| Decisions per device type | `regulatory-dh.get_pathway_precedents` | Decisions by pathway and year, first and last decision, stored-date days | An AI count, uptake, market size; MDUFA "FDA days" | `tools.md` |
| Register change log | `regulatory-dh.get_deltas`, `get_register_deltas` | Rows only once a watch exists | Anything before a watch: on 19 October 2026 every call returned "no watch is registered for this scope; the change log has not started" | `tools.md`; register C11, N2 |
| Company record change | `diligence-dh.get_deltas` | Event-dated changes since a date | Anything before 12 October 2026 (log start); status of the company | `tools.md`; DL-135 to DL-168 |
| Publication | `literature.search_literature` | Candidate records with DOI, year, type | Findings; reliable design labels or trial ids (register N8) | `tools.md` |
| Trial registration | `literature.find_trial` | Registry entry linked to a paper | Unregistered or unlinked trials | `tools.md` (needs a live check here) |
| AI-enabled device list (US) | FDA list page, not a library call | Devices FDA identified as AI-enabled; 1,614 rows in the CSV read on 19 October 2026, latest decision 29 June 2026 | Completeness: the list is not comprehensive and is updated periodically; it lags authorizations | US-24 to US-27, US-34, US-35 |
| Safety records | `regulatory-dh.search_safety_events` | Recalls and alerts as filed | Cause; on 19 October 2026 the `product_code` filter applied to MAUDE counts, not to recalls | `tools.md` |
| Rule or program change | The rows in section 4 | Instrument, date, status (draft, final, pilot, in force) | Whether it applies to the person's product: that is the owner's call | Section 4 |

## 4. Dated rule and program changes a scan can carry (as read on the row's date)

| Change | Date and status | Rows |
|---|---|---|
| EU AI Act high-risk obligations deferred by Regulation (EU) 2026/1744 | Adopted 8 July 2026, in force 27 July 2026; Chapter III Sections 1 to 3 apply from 2 December 2027 (Annex III) and 2 August 2028 (Article 6(1) and Annex I, including MDR and IVDR devices) | EU-17 to EU-19 |
| EU AI Act new prohibited points | Apply from 2 December 2026 | EU-21 |
| FDA AI-enabled device software lifecycle guidance | Still draft on 19 October 2026; on CDRH's FY 2027 A-list as a final guidance topic | US-21, US-22 |
| FDA PCCP guidance (AI) | Final; reissued 18 August 2025 | US-01 |
| MHRA PCCP draft guidance | MHRA stated (6 October 2026) it will issue draft guidance for comment; no published guidance found | UK-04 |
| MHRA AI Airlock regulatory sandbox | Phase 3 announced 6 October 2026; innovator case studies are not MHRA guidance | UK-06 to UK-08 |
| FDA TAP pilot | Expanded on 1 July 2026 to all OHTs for Breakthrough and STeP devices; 159 devices enrolled as of 7 October 2026 (do not reuse the count without its date) | SP-121, SP-122 |
| CMS and FDA RAPID coverage pathway for Breakthrough devices | Announced 23 April 2026 | SP-123 |
| MHRA IDAP pilot | Closed to new applications; future IDAP not defined on the page read | SP-124 |
| European Health Data Space, Regulation (EU) 2025/327 | Applies from 26 March 2027; EHR duties phase in 26 March 2029 and 26 March 2031; secondary use from 26 March 2029; many implementing acts due by 26 March 2027 | SP-068 to SP-073 |
| WHO Global Strategy on Digital Health | Extended to 2027 by WHA78 (27 May 2025); a 2028 to 2033 strategy goes to the 80th World Health Assembly in 2027, not yet adopted | SP-066 |
| EU technology transfer block exemption | Regulation 316/2014 expired 30 April 2026; Regulation (EU) 2026/877 in force 1 May 2026 to 30 April 2038; transition to 30 April 2027; new Guidelines published 21 April 2026 | SP-134, SP-135, SP-137, SP-141 |
| ISO innovation management standards [WF] | ISO 56000:2020 withdrawn 23 January 2025 (replaced by ISO 56000:2025, not read); ISO 56002:2019 under revision; ISO 56001:2024 is the certifiable standard | SP-044 to SP-047 |

Every change carries its instrument and status as read. Whether it touches the person's product, partner or deal is for the owner the person names (`governance.md`).

## 5. Triage filters

Filters are the person's (scope, technology classes, markets, time horizon, sources in or out). Where the person gives none, the skill proposes filters, labeled "proposed", from: the person's own product and markets; the WHO classification axes (SP-055, SP-056) to name the intervention type; the time horizon the person states. Duplicates are merged on identifiers (K number, Basic UDI-DI, DOI, PMID), never on names: the same product appears under different spellings across registers (`tools.md`).

## 6. Not sourced here

- A general horizon scanning method document from WHO or OECD: none found (SP research, "Not sourced").
- The EuroScan toolkit itself and the NIHR IO full methods paper: not read; methods come from the survey paper and the IO summary (SP-004, SP-008).
- Signal "strength" scores, disruption indices, hype cycles, adoption curves or market sizes: no primary source sets them. Any strength, impact or likelihood score is the person's.
