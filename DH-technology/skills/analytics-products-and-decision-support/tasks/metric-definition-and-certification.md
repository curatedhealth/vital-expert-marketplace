# A2 Metric definition and certification

Framework task: DH-05.02.1.1, DH-05.02.1.2 and DH-05.03.3 (certification, platform governance and center of excellence), Part A, task A2. Carries the old tasks "Metric on the semantic layer", "Entity the metric hangs on", "Layer change" (DH-05.02.1.1.1 to .3), "Template purpose", "Template contents", "Template retirement" (DH-05.02.1.2.1 to .3), "Metric certification rule" and "Certification record" (DH-05.03.3.1.1 and .2), "Platform access rule" and "Publish record" (DH-05.03.3.2.1 and .2), "CoE charter", "CoE decision log" and "CoE dispute" (DH-05.03.3.3.1 to .3). Decertification (DH-05.03.3.1.3) and the access review (DH-05.03.3.2.3) are monitoring tasks in `analytics-adoption-and-impact-monitoring` (this pack).

## What this task delivers

Each metric card checked against the elements the sourced rows name (CMS measure specification structure as a checklist, DA-132 to DA-137) and the old task method (owner, grain, certified source, filters, version), with flags K1 to K13; the dashboard figure recomputed from the person's rows with the card's rules; duplicates recomputed beside a certified metric; a certification record drafted for the certifier under the person's rule; template specifications; publish rights with the HIPAA facts where PHI is involved; and the CoE charter, decision log or dispute record in the person's words. It answers "is this metric defined well enough to certify, does the dashboard match it, and who may publish it?"

Why it matters: the old tasks named the failure modes: "Do not leave the formula only in a dashboard", "Do not correct a formula silently", "Do not certify a metric with no owner". Two cards with the same numerator and denominator on two dashboards produce two truths in the same meeting.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | `data-analytics-lead` (old DH-05.02.1.1); `clinical-content-product-manager` (old DH-05.02.1.2); `ai-ml-governance-director` (old DH-05.03.3). Work as a metric analyst who checks the person's cards and data |
| Skill | Analytics products and decision support, Part A, Metric definition and certification |
| Workflow | The steps below |
| Knowledge | `references/metric-governance-rules.md`; rows DA-94 to DA-112, DA-132 to DA-140, CS103 to CS105, EN-097 to EN-107; `references/governance.md` |
| Tools | None from the library. `scripts/metric_check.py cards`, `recompute`, `words`; `verify.build_record` when the record leaves |
| Prompt | This guide |
| Template | `assets/metric-definition-and-certification-output.md` |
| Input | The request and its context: metric cards (CSV columns in SKILL.md), the person's certification rule, row-level data and the dashboard figure with its data timestamp, templates, the publisher list and roles, whether PHI is involved, the CoE charter |
| Governance | `references/governance.md`; the certifier decides |
| Catalogue job | none |

## Read the request

- Defining a new metric, checking cards, a mismatch between dashboard and definition, certifying, publish rights, or the CoE? Run the matching steps only.
- Is the person's certification rule given? Without it, the cards are checked against the sourced elements but nothing is called certifiable: "certification rule not given".
- Is PHI involved, and in which market? HIPAA rows apply to US covered entities and business associates only.
- Is the metric a CMS quality measure itself? Then the CMS rows are the measure's own specification source, not a checklist; say which.

## Workflow

### Step 1. Write or check the card (old DH-05.02.1.1)

For a new metric, write the card in the person's words: name, decision, owner, entity and key, grain, period, initial population, denominator in words, numerator with its time window, exclusions, scoring direction, strata, certified source tables, allowed filters and the attribute kept off the filters (leaky or unstable), version and status. Each missing element is "not given". For existing cards, run:

```
python3 scripts/metric_check.py cards --file METRICS.csv
```

Report flags K1 to K13 with their rows: K3 numerator or denominator (DA-134, DA-135), K4 initial population (DA-133), K5 denominator in codes only (DA-134, "words, not codes"), K6 scoring direction (DA-137), K7 strata (DA-136), K11 a card with the same numerator and denominator as another (recomputed beside it). Label every CMS row "CMS quality-measure guidance, used as a checklist". Descriptive statistics do not show reliability or validity (DA-139): a card that cites only counts as its evidence says so.

### Step 2. Source data terms

Name, for the certified source, the data quality checks the person requires in Kahn's terms (conformance, completeness, plausibility; verification and validation; Kahn 2016, DA-94 to DA-98, DOI 10.13063/2327-9214.1244) and its provenance and usage license (FAIR R1.1, R1.2, DA-100, DOI 10.1038/sdata.2016.18). Running the checks is `data-quality-monitoring` (this pack). On OMOP, state the observation period rule for denominators (DA-105 [SPEC]). For USCDI elements, keep "published" (v7, 23 July 2026, DA-108) apart from "required for certification" (v1 expired 1 January 2026 and v3, DA-111).

### Step 3. Recompute the dashboard figure (old DH-05.02.1.2.2)

With the person's row-level file, the card's rules and the figure the dashboard shows (with its data timestamp), run:

```
python3 scripts/metric_check.py recompute --data ROWS.csv --denominator "<card rule>" --numerator "<card rule>" --reported <figure> --by <stratum>
```

Report the recomputed rate, the figure shown and the difference, by stratum where the card names one. A difference is a fact: formula, filters or refresh differ until shown otherwise. No tolerance comes from the model. If the data timestamp is not given, the comparison is not made.

### Step 4. Changes and corrections (old DH-05.02.1.1.3)

For a change: name it, the dashboards that use the metric, whether it is a new version or a correction, and who is told before a correction ships (the person's names, or owner not named). A silent correction is flagged.

### Step 5. Certification record (old DH-05.03.3.1.1 and .2)

Write the person's certification rule back verbatim. Check the card against each element of the rule. Draft the record for the certifier: metric, version, rule elements met or not met, the recomputation result, pass or refuse as the certifier decides ("for the certifier"), date and certifier as given, and the pointer to the layer definition. A metric stays "draft" until the certifier passes it. The model never certifies; adding a metric to a dashboard is not certification.

### Step 6. Templates (old DH-05.02.1.2)

For a template: audience and decision, certified metrics only, filters allowed, empty state, the owner who fixes a broken metric, and for retirement the last date used (if known), the replacement or "none", and who tells the audience. Two templates for one decision are flagged.

### Step 7. Publish rights and access (old DH-05.03.3.2.1 and .2)

Write back the roles that may publish, the roles that may explore, and the data they may not export, as the person sets them. Where PHI is involved (US), lay the facts beside them: minimum necessary (45 CFR 164.502, CS103), workforce classes and role-based access (45 CFR 164.514, CS104), routine disclosure protocols (CS105), required activity review and unique user identification (HIPAA Security Rule, EN-101, EN-103); the January 2025 NPRM is a proposal, not in force (EN-106, EN-107). Whether a role's access is the minimum necessary is the owner the person names for privacy matters. Record each publish as given; a publish that recomputes a certified metric locally is flagged.

### Step 8. Center of excellence (old DH-05.03.3.3)

Write the charter, decision log entry or dispute in the person's words: decisions owned and not owned, seats, the charter line that applies, who resolves what the charter does not cover. A decision outside the charter is flagged as such. Proposed charter headings only if asked, labeled "proposed".

## Build the output

Follow `assets/metric-definition-and-certification-output.md`. Answer first: how many cards carry which flags, the duplicate pairs, the recomputed figure beside the shown figure, and what the certifier must decide. Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/metric_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Card wording, the certification rule, each certification, publish rights and charter decisions are the person's, and the record says so.
- CMS rows are labeled as a checklist for internal metrics; no tolerance or target came from the model.
- Draft and proposed rules (NPRM) are not presented as requirements; USCDI versions are dated.
- Every fact names its source and date in plain words with the row id after it; [PAPER] and [SPEC] rows are labeled.
- `python3 scripts/metric_check.py words ANSWER.md` prints "within the short-mode cap".
- The record line is the very last line; the calls list and the offer of the full version come before the record block: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Running data quality checks: `data-quality-monitoring` (this pack).
- Decertification after a formula change and the periodic access review: `analytics-adoption-and-impact-monitoring` (this pack).
- Platform security controls: `cybersecurity-and-privacy-by-design` (this pack).
- Patient engagement KPI cards: `dh-patient-and-user-experience` engagement-kpi-dashboards.
