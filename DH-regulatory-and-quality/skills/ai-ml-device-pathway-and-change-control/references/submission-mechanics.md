# Submission mechanics: agency interaction, formats, clocks, fees

Interpretive reference for task B1. Rows: `RP` = `REG_PATHWAYS_SUBMISSIONS.md`, `AI` = `AI_ML_REGULATION.md`. Clocks are facts for planning, never pressure. "FDA days" exclude time with the sponsor; calendar time is longer.

## United States

### Before the marketing submission

| Interaction | What it gives | Clock | Row |
|---|---|---|---|
| Pre-Submission (Q-Sub program, guidance of 29 May 2025) | Written FDA feedback on the person's questions, optionally a meeting. For an AI device: feedback on the PCCP is encouraged, but a PCCP is not authorized in a Pre-Sub | Acceptance or technical screening within 15 days; written feedback within 70 calendar days, or at least 5 days before a meeting and no later than day 70 | [RP US-30 to US-33; AI US-10] |
| Pre-Sub performance goal (MDUFA V) | 90% of Pre-Subs on time, up to 4,300 a year, FY 2025 to FY 2027 | | [RP US-35] |
| Study risk determination, informational meeting | Formal letter or meeting | 90 days | [RP US-34] |
| Breakthrough Device designation request (sent as a Q-Sub) | Interactive options and prioritized review if granted; criteria: more effective treatment or diagnosis of a life-threatening or irreversibly debilitating condition plus one further condition | Decision letter within 60 calendar days | [RP US-40 to US-44] |
| 513(g) request for classification information | FDA's classification view | Fee in FY 2026: USD 7,820 (small business USD 3,910); FY 2027 513(g) fee not extracted `[GAP]` | [RP US-53] |

### The marketing submission

- **Format.** eSTAR is required for 510(k) (since 1 October 2023) and De Novo (since 1 October 2025), submitted through the CDRH Portal [RP US-36 to US-38]. Current templates: nIVD and IVD eSTAR 7.1, PreSTAR 3.1; eSTARs include the Human Factors content guidance effective 1 August 2026 [RP US-39]. PMA eSTAR status is not in the references `[GAP]`.
- **Software documentation level.** Enhanced where a software failure could present a hazardous situation with a probable risk of death or serious injury before risk controls; otherwise Basic [RP US-26, US-27]. FDA generally recommends Enhanced for class III and combination-product constituents [RP US-28]. Content guidance of 14 June 2023 [RP US-25].
- **AI content.** The AI lifecycle draft of 7 January 2025 recommends marketing-submission content for AI functions; it is draft [AI US-19 to US-21].
- **PCCP placement.** Standalone, titled, versioned section named in the cover letter and table of contents [AI US-11]; only in the submission types listed in [AI US-09].
- **De Novo content.** A summary of probable risks and proposed mitigations, with special controls if class II is recommended [RP US-12].

### Review goals and observed times

| Route | Regulation clock | MDUFA V goal | Observed average total days (FDA plus sponsor) | Rows |
|---|---|---|---|---|
| 510(k) | 90 days before marketing (notice) | 95% within 90 FDA days | FY 2023 141.46; FY 2024 143.64; FY 2025 141.24 | [RP US-04, US-46, US-58] |
| De Novo | Grant or decline within 120 days of acceptance | 70% within 150 FDA days, shown as 80% for FY 2026 and 90% for FY 2027 in the August 2026 report | FY 2023 270.07; FY 2024 247.51; FY 2025 278.12 | [RP US-11, US-47, US-60, US-61] |
| PMA | 180 days after filing, extendable up to 180 days by a major amendment | 90% within 180 FDA days without an advisory panel; 320 with one | Not extracted `[GAP]` | [RP US-14, US-15, US-48] |

A De Novo is withdrawn if an additional-information request is not fully answered within 180 days [RP US-13]. The latest MDUFA performance report was posted 26 August 2026, covering actions through 30 June 2026 [RP US-56]. MDUFA V runs to 30 September 2027 [RP US-45].

### Fees (FY 2027 rates, in force from 1 October 2026)

510(k) USD 28,653 (small business USD 7,163); De Novo USD 191,020 (USD 47,755); PMA USD 636,732 (USD 159,183); establishment registration USD 13,785 [RP US-55]. FY 2026 rates are kept for reference only [RP US-49 to US-54].

## European Union

- **Notified body.** IIa, IIb and III software needs one [RP EU-08 to EU-10]. The manufacturer may choose any notified body designated for that device type, never two in parallel for the same procedure [RP EU-12].
- **Technical documentation.** Annex II structure [RP EU-13], classification justification [RP EU-14], software verification and validation [RP EU-15], PMS plan [RP EU-16]; one file that also covers AI Act requirements once they apply [AI EU-29].
- **Clinical evidence.** Article 61 and Annex XIV Part A [RP EU-17, EU-18, EU-20]; MDCG 2020-1 three components for software [RP EU-32]. Class III and certain IIb manufacturers may consult an expert panel before clinical evaluation [RP EU-19].
- **Pre-determined changes.** Documented under AI Act Annex IV point 2(f) at the initial assessment [AI EU-05, EU-30].
- **Notified body timing (contractor study commissioned by the Commission, data to 28 February 2026).** 62% of notified bodies report 13 to 18 months from written agreement to a new MDR QMS certificate; for QMS plus product certificates 51% report 13 to 18 months and 31% report 19 to 24 months [RP EU-40, EU-44]. No software-specific breakdown [RP "Not sourced"]. Context, not a forecast.
- **EUDAMED.** Actor, UDI/device, notified body and certificate, and market surveillance modules mandatory since 28 May 2026 [RP EU-36].

## United Kingdom

UKCA needs a UK approved body except class I [RP UK-15]; CE acceptance dates in `ai-ml-routes.md`. MHRA engagement routes for AI (the AI Airlock) are a sandbox, not a pre-submission program [AI UK-06 to UK-08]. An MHRA pre-submission meeting process is not in the references `[GAP]`.

## Ordering logic (dependencies, not a schedule)

1. Intended use and the person's class view come first: every later step depends on them.
2. Predicate search (510(k)) or De Novo rationale depends on intended use.
3. The PCCP scope depends on the intended use and route (it must stay inside both) [AI US-08].
4. A Pre-Sub on the route, the PCCP and the testing plan depends on drafts of 1 to 3, and its feedback should come before the testing that depends on it [RP US-31; AI US-10].
5. The marketing submission depends on testing and the final PCCP.
6. EU: notified body agreement, then technical documentation assessment; the AI Act requirements must be in the file by the date that applies to the device [AI EU-19].
