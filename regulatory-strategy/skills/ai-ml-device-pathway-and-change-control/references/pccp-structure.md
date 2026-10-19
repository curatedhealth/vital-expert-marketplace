# PCCP structure: what it holds, what fits, what the person supplies

Interpretive reference for task A2 and B1. Rows: `AI` = `AI_ML_REGULATION.md`, `RP` = `REG_PATHWAYS_SUBMISSIONS.md`. The source document is FDA's final PCCP guidance of 18 August 2025 [AI US-01] unless a line says otherwise. Section numbers below are the guidance's own (VI, VII, VIII) as quoted in the rows.

## The three components (FDA)

| Component | What it is, in the guidance's words | Row | What the model may draft | What only the person supplies |
|---|---|---|---|---|
| Description of Modifications (Section VI) | "The specifications for the characteristics and performance of the planned modifications to the device" | [AI US-04] | The list of planned change types, each tied to the device's current intended use; the headings for each change | The specifications, the performance targets, the input types, the populations |
| Modification Protocol (Section VII) | "The associated verification and validation testing activities that will support the planned modifications and acceptance criteria to assure the device remains safe and effective across the intended use populations" | [AI US-05] | The protocol skeleton: data, retraining, testing, update and labeling steps as headings; a list of every acceptance criterion that must be set | Every acceptance criterion value, every test method, every dataset, every statistical plan |
| Impact Assessment (Section VIII) | "The assessment of the benefits and risks of implementing a PCCP, as well as the plan for risk mitigation" | [AI US-06] | A table that links each planned change to the risks the person names and the mitigation they propose | The benefit-risk judgment and the mitigations |

The plan must have all three: "A PCCP should consist of a detailed Description of Modifications, a Modification Protocol, and an Impact Assessment" [AI US-03].

**What the statute lets FDA require in the plan** (section 515C): labeling for safe use as the device changes, notification requirements if the device does not function as intended, and performance requirements for changes under the plan [AI US-17]. The draft includes a placeholder for each.

**Post-market side.** FDA anticipates that manufacturers will monitor safety and performance as changes are implemented; the Modification Protocol should describe post-market surveillance plans [AI US-36]. PCCP guiding principle 1 includes mechanisms to detect and revert or stop a change that fails its performance criteria [AI US-31]. The draft includes both as headings for the person to fill.

## Which changes fit

FDA names three types that may fit [AI US-07]:

1. Changes to quantitative measures of the AI device software function's performance specifications (for example re-training on new data).
2. Changes to device inputs and compatibility with the AI function.
3. Certain changes to the device's use and performance, for example a specific subpopulation *within the originally indicated population* [AI US-07]. A population outside the cleared indication (for example a new age band) is not this example; it is an indications-for-use question for the owner, and FDA encourages raising it in a Q-Sub [AI US-08].

**Boundaries.** Changes must keep the device within its intended use and, for a 510(k), substantially equivalent to the predicate [AI US-08, US-16]. FDA expects most indications-for-use changes to be hard to assess in advance [AI US-08]. Changes should keep or improve safety or effectiveness and be verifiable and validatable [AI US-07]. In a later 510(k), comparison is to the predicate as cleared before PCCP changes [AI US-14].

**Sorting a person's planned change.** For each change the person lists, the model writes one of: "fits type 1, 2 or 3 as described (person to confirm)", "may cross intended use: for the regulatory owner", or "not enough detail to sort `[GAP]`". The model never declares a change in or out of scope.

## Where the plan sits and how it is used

- Established only in a submission where FDA makes an affirmative decision: original, modular, 180-day, panel-track or real-time PMA supplement; Traditional or Abbreviated 510(k); original De Novo [AI US-09].
- Authorized with the marketing authorization; Q-Sub feedback is encouraged but FDA does not authorize a PCCP in a Pre-Submission [AI US-10].
- A standalone section with title and version number, flagged in the cover letter and table of contents [AI US-11].
- A change consistent with the authorized plan needs no new submission; it is implemented per the Modification Protocol and documented in the quality system [AI US-12].
- Deviating from the authorized plan would generally make the device adulterated and misbranded [AI US-13].

## EU and UK counterparts

- **EU.** AI Act Article 43(4): changes pre-determined at initial conformity assessment and documented under Annex IV point 2(f) are not a substantial modification [AI EU-05]. MDCG 2025-6: such changes are not a change to the certified device under MDR Annex IX 4.10 or IVDR Annex IX 4.11 [AI EU-30]. Dedicated EU PCCP guidance is not published; MDCG expects it to build on IMDRF work [AI EU-31]. The content an EU notified body expects in Annex IV point 2(f) is not in the references `[GAP]`.
- **UK.** No MHRA PCCP guidance is published; draft guidance for comment is stated as intended by December 2026 [AI UK-04]. A GB plan cannot yet be relied on `[GAP]`.
- **Joint principles.** Focused and bounded; risk-based; evidence-based; transparent; total product lifecycle [AI US-31]. Useful as a review lens, not a legal test.

## What the connector holds

`retrieve_guidance` with query "PCCP" returns passages that read as Health Canada guidance (they speak of a "medical device licence amendment application") with no source URL or date (`references/tools.md`). They cannot support a rule. Do not quote them.

## Never

- Write an acceptance criterion value, a performance threshold, a sample size, or a statistical margin. Write "acceptance criterion: set by the person `[GAP]`".
- Present a PCCP as authorized, or a change as covered, before the marketing authorization says so.
- Quote the guidance beyond the rows above. Further detail of Sections VI to VIII was not extracted in the research pass `[GAP]`; the person or their regulatory owner reads the guidance itself.
