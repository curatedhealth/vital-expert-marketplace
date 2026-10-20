# A1 Fidelity rules

Framework task: DH-01.01.4.2, Part A, task A1. Replaces the earlier "Fidelity check" section (DH-01.01.4.2.1).

## What this task delivers

A fidelity rule set draft for one product: the framework it uses (named, because frameworks disagree), the core components where fidelity is expected and the variation that is permitted or prohibited, the fail conditions for claims and decision rules, and the delivery measures to track (content, frequency, duration, coverage) with the regimen they are measured against. Every threshold is left for the person; every proposal is labeled.

Why it matters: an app can change weekly. Without written fidelity rules, each release reopens what "faithful to the evidence" means. The old rule stands: a citation being present does not pass fidelity (DH-01.01.4.2.1).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Clinical Validation Director (`clinical-validation-director`) |
| Skill | DH-01.01.4.2 Part A, Fidelity rules |
| Workflow | The steps below |
| Knowledge | `references/fidelity-frameworks.md`; `references/claim-and-rule-fidelity.md`; rows TM11 to TM13, TM19, TM32, TM61, TM70, TM88, TM89, TM91 to TM106, TM114 to TM118, CS4, CS9, CS25, CS29, CS37, CS48, PC-US-23, PC-US-24, TM148 |
| Tools | None required |
| Prompt | This guide |
| Template | `assets/fidelity-rules-output.md` |
| Input | The request and its context: the claim map and specification from DH-01.01.4.1 (or the person's equivalent), the regimen, the release practice, the owners the person names |
| Governance | `references/governance.md`; the person sets every threshold and decides which components are core |
| Catalogue job | none |

## Read the request

- **What is being held faithful.** Claims and product text, decision rules, content, dose, or all of them.
- **Source of truth.** The claim map and specification from DH-01.01.4.1, a treatment manual, a label or indication. If none exists, say so: fidelity needs something to be faithful to (TM100).
- **Release practice.** How versions are named and how often they ship; the sample in A2 is per version.
- **Owners.** Who owns claims, rules, content and release, in the person's words.

## Workflow

### Step 1. Name the framework

Offer the choices and their parts, and ask the person to pick one (research file "Changes and conflicts" item 3): Carroll (fidelity measured as adherence: content, frequency, duration, coverage; moderators: complexity, facilitation, quality of delivery, participant responsiveness; TM100 to TM104, DOI 10.1186/1748-5908-2-40), Moore's process evaluation (fidelity, dose, reach, with no consensus on subdividing, TM91 to TM94, DOI 10.1136/bmj.h1258), Bellg's five areas (design, training, delivery, receipt, enactment; abstract only, TM99), or Proctor's fidelity as an implementation outcome (CS37, DOI 10.1007/s10488-010-0319-7). If the person has no preference, propose Carroll for software delivery because its adherence subcategories map onto logged data, labeled "proposed".

### Step 2. List core components and permitted variation

From the specification, list each component and mark, as "proposed", core or adaptable, with the permitted and prohibited variation (TM11, TM117; CFIR core components versus adaptable periphery, CS4, DOI 10.1186/1748-5908-4-50; ERIC "promote adaptability", CS48). Note the option to standardize function rather than form (TM12) and that adaptations are acceptable when key functions are kept (TM19). Essential components may be all that fidelity requires, if they are identified (TM105). The person decides.

### Step 3. Write the claim fail conditions

Start from the old method's three fail types and lay them out with the rows behind each, as "proposed" until the person confirms (`references/claim-and-rule-fidelity.md` section 1):
- **Wider population** than the source (TM144 shows a source population; PC-US-27 for labeled products).
- **Stronger verb** than the source (a hedge dropped, "may" to "does", "might be used to improve" to "clinically proven").
- **Missing caveat** the source had (a limitation, an adjunct-only statement, a subgroup without benefit; TM122, TM138, TM144).
Add, if the person wants them: a different outcome or measure than the source, a different dose or regimen (PC-US-23 lists regimen as a factor), and a claim with no source (old DH-01.01.4.2.2 rule: fail).

### Step 4. Write the decision rule fail conditions

For each rule in the specification: the rule fires as specified (decision point, tailoring variable, option); behavior on missing tailoring data is the specified one (TM89); the tailoring variable is measured as specified (TM88). Name the evidence each check needs: test records, logs, event data. A live precedent: FDA recalls of reSET and reSET-O on 7 June 2021 describe reward access "regardless of the UDS results" where a positive screen should not have given access (`references/tools.md`); the specified rule was reward on negative screens (TM135).

### Step 5. Choose the delivery measures

For the framework chosen, list the measures and the data source for each: content delivered (modules, lessons), frequency and duration against the regimen (TM29, TM102), coverage or reach (TM94; RE-AIM implementation at individual level is clients' use, CS25), and engagement and fatigue as proximal outcomes where adaptive (TM87). Each measure's threshold is the person's; leave the column empty. Define what one "session" is before measuring: the STARS-ADHD abstract counts "100 expected sessions" for a 4-week, 5-days-per-week regimen without stating the unit (`examples/live/pubmed_abstracts_2026-10-20.txt`).

### Step 6. Write the rules back

Return the rule set in the template, every threshold and owner blank or in the person's words, every proposal labeled. Ask the person to confirm before A2 applies any of it.

## Build the output

Follow `assets/fidelity-rules-output.md`. Short mode for a direct question: the framework named, the core components, the fail conditions, the delivery measures, and the decisions waiting for the person. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- The framework is named, and the conflict between frameworks is stated once.
- No threshold is set by the model; proposals are labeled.
- "Citation present" is not a pass condition anywhere in the rules.
- Each [PAPER] paper cited has its DOI once in prose, and every table cell that cites a [PAPER] row carries that row's own DOI; abstract-only and [WF] rows carry their label each time.
- No date, data cut, version, threshold or status appears that the person did not give ("not given" and ask); no fact comes from an earlier, separate request.
- The record line is the last line of the answer body (the calls list, if any, follows it): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Writing or changing the claim map and specification: evidence-to-intervention translation (DH-01.01.4.1).
- Recording the rules in the quality system: `dh-regulatory-and-quality` document-and-change-control.
- Implementation fidelity at customer sites (training, workflow fit): `dh-go-to-market` implementation-quality-monitoring.
