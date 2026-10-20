# Monitoring signals: what to count, and the clocks and duties the rules set

Interpretive reference for A1, A2 and B1. Rules cite rows in `channels-partners-launch-research.md` (CP prefix, read 19 October 2026). Measures and thresholds are the person's; the rows set no partner performance target.

## Part 1. The counts (the person's measures)

The register method for DH-02.01.4.2 names three counts as a starting list. They are offered, not imposed: the person keeps, renames, drops or adds, and sets every threshold and period.

| Count | Definition to agree with the person | Counted from |
|---|---|---|
| Qualified buyers handed off | Buyers that reached the handoff event the person defined in the channel design (A1 of the design skill) in the period | The person's handoff record, not the partner's own report, when both exist |
| Implementations started | Buyers handed off by this partner whose implementation started in the period (the person defines "started") | The person's implementation record |
| Claim breaches | Uses by the partner of a claim not on the approved claim list, or of wording the rows forbid (for example implying FDA approval from registration, CP-US-74) | The person's evidence (material, link, recording), quoted |

Rules from the register method:

- A partner is not scored on leads it did not hand off.
- A partner report that cannot be tied to a buyer in the handoff record is not counted. It is listed as "partner-reported, not tied".
- The person says which count forces a hold.

No national or industry benchmark for partner performance is sourced `[GAP]`. Never offer one as a target.

## Part 2. Clocks and duties that bear on a live partner

These are facts from the rows. They are not performance measures; they are things a monitoring view should check are in place and being met, with the person's evidence.

| Signal | Rule | Row |
|---|---|---|
| Partner breach notice (US, business associate) | No later than 60 calendar days after discovery | CP-US-49 |
| Security incidents (US, ePHI) | The BAA requires reporting any security incident | CP-US-48 |
| Partner breach notice (EU, processor) | Without undue delay; no hour limit for the processor | CP-EU-08 |
| Consumer breach (US, outside HIPAA) | Notice within 60 calendar days; FTC notice at the same time at 500 or more people; unauthorized disclosure counts | CP-US-55, CP-US-56 |
| New sub-processor (EU) | Prior written authorization; under general authorization, notice of changes with a chance to object | CP-EU-02 |
| Partner reusing data for its own purposes (EU) | It becomes a controller for that processing | CP-EU-07 |
| Outcomes-based partner payments (US) | Regular monitoring of performance and its effect on quality of care; benchmarks and pay reassessed; policies to correct material failures | CP-US-14 |
| Care coordination arrangements (US) | Measures monitored, assessed and revised; records kept 6 years | CP-US-22 |
| Patient engagement tools (US) | Annual retail value cap per patient: $623 for calendar year 2026 (regulation states $500, adjusted by CPI-U); records 6 years | CP-US-27, CP-US-28 |
| Loaner devices to patients | AO 19-02 safeguards OIG relied on (requestor only): not advertised, need-based, cap of two 12-week periods | CP-US-41, CP-US-43 |
| Public partner's material agreements | Form 8-K within four business days for a material definitive agreement or material amendment | CP-US-79 to CP-US-81 |
| Germany | No arrangement about allocating or transmitting DiGA prescriptions; no agreement with drug or aid makers restricting choice | CP-DE-06, CP-DE-07 |
| England | DTAC form refreshed, full transition by 6 April 2026; DCB0160 duties sit with the deploying organization | CP-UK-04, CP-UK-09 |
| EU registration | Manufacturers, authorized representatives and importers registered; data changes updated within one week | CP-EU-10, CP-EU-11 |

A clock is a signal to check with the person's evidence, never a finding that a partner breached a duty.

## Part 3. Public signals on a partner (library)

What the library can show about a partner that is a regulated digital health company or an SEC filer: new authorizations, studies, safety events, filings and awards since a date (`diligence-dh.get_deltas`), filings by type (`diligence-dh.get_funding_signals`). These are public events to note, never a judgment of the partner's health. "No change recorded" is a statement about the library's log, not about the company (`tools.md`).

## Not sourced

Partner performance benchmarks, channel conversion norms, churn or attrition norms for resellers, termination-for-performance norms: all `[GAP]`; the person's rules decide.
