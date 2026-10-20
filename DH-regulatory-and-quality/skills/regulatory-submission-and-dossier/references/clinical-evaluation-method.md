# Clinical evaluation for medical device software: the sourced method

Row prefixes as in `content-maps.md` (`RP`, `AI`, `S`). Read 19 October 2026. ISO and IEC texts are not quoted anywhere in this skill.

## What the MDR requires

- Conformity with the relevant GSPRs, and the benefit-risk judgment, rest on clinical data giving sufficient clinical evidence; the manufacturer specifies and justifies the level of evidence (RP EU-17). The evaluation is planned, conducted and documented under Article 61 and Annex XIV Part A (RP EU-18).
- Article 61(3): a defined, methodologically sound procedure based on a critical evaluation of the literature (data about another device count only where equivalence is shown under Annex XIV Section 3), a critical evaluation of all clinical investigations, and a consideration of available alternative treatments (S-55).
- Annex XIV Part A Section 1: a clinical evaluation plan with at least the GSPRs needing clinical data, intended purpose, target groups with indications and contra-indications, intended clinical benefits with specified outcome parameters (RP EU-20), and a clinical development plan including PMCF; then identify data and gaps through a systematic literature review, appraise all relevant data for suitability (S-58), generate new data where needed, and analyze all of it.
- Favourable and unfavourable data are both considered and both go in the technical documentation (S-59).
- Equivalence: technical (including software algorithms), biological and clinical characteristics, similar enough for no clinically significant difference, with sufficient access to the other device's data (S-75, S-76).
- The CER is part of the Annex II technical documentation (S-57) and is updated through the life cycle with PMCF and PMS data (S-56).
- Class III and certain class IIb manufacturers may consult an expert panel on their clinical development strategy before the evaluation (RP EU-19).

## How MDCG 2020-1 frames software (March 2020, not revised per the MDCG index read; RP EU-32, RP EU-35)

Three components, which are a principle, not a sequence (S-65):

| Component | What it shows | Where evidence comes from |
|---|---|---|
| Valid clinical association | The output is associated with the targeted clinical condition or physiological state (RP EU-33) | Literature, professional guidelines, proof of concept studies, or the manufacturer's own investigations (S-60) |
| Technical performance | The software accurately, reliably and precisely generates the intended output from the input data (S-61; definition taken from IMDRF N41, RP IM-03) | Verification and validation, curated databases, registries, reference databases, previously collected patient data |
| Clinical performance | The software yields clinically relevant output in line with its intended purpose (S-62) | Testing the device or an equivalent device in the target population: pre-clinical testing, a clinical investigation or a clinical performance study |

- The level of evidence is justified by both amount and quality, with guiding questions for each (S-63). Use those questions as headings for the person's justification; do not answer them for the person.
- Clinical performance validation should be considered at each new release, or the decision justified (S-64).

## How the notified body will read it: MDCG 2020-13 (July 2020)

The CEAR template the notified body fills runs Section A (administrative), B (reviewers), C (device description, classification, CEP, information materials, standards, equivalence and state of the art), D (clinical literature review), E (clinical investigations), F (PMS, PMCF, update plan), G (IFU, SSCP, labelling), then overall conclusions (S-66, S-67). It applies to Annex IX section 4 and Annex X section 3 assessments and to sampled class IIa and IIb files (S-68). It is not legally binding (S-70). The notified body specifically assesses claimed equivalence (S-69).

Practical use: map each part of the person's CER to the CEAR section that will assess it, so gaps show up from the reviewer's side before submission.

## How the library tools fit

| Step | Tool | What it can and cannot do (measured 19 October 2026, `tools.md`) |
|---|---|---|
| Find candidate literature | `literature.search_literature` | Federated search; returns design labels and often an empty excerpt. It is a search aid, not the systematic review Annex XIV asks for: the protocol, databases, strings and screening are the person's. |
| Resolve one paper | `literature.get_record` | Returns identifiers and, for some records, an abstract excerpt that may stop before the results. |
| Design label | `literature.classify_study` | Decides from title words: a conference abstract titled "pooled analysis" came back "meta_analysis". Check the publication type yourself. |
| Level | `literature.grade_evidence` | CEBM 2011 level from the design label only (register N8). It graded that conference abstract level 1. Treat the level as a draft; appraisal for the CER is the person's. |
| Support check | `verify.qualify_source` then `verify.check_claim` | Accept "supported" only if you have read a results passage that states the finding in the same direction. On 19 October 2026 `check_claim` returned "supported" for an efficacy claim from a passage that stated only the trial's aim (register N3). |

## Boundaries of this method

- The model does not write clinical conclusions, does not judge whether evidence is sufficient, and does not declare equivalence. It lays out the structure, places the person's evidence in it, and marks gaps.
- The FDA adoption of IMDRF N41 as a clinical evaluation guidance is `[GAP]` (the FDA link returned 404; RP "Not sourced"). For US submissions, clinical data go in Performance Testing (S-13, S-19); no FDA clinical-evaluation structure is sourced here.
