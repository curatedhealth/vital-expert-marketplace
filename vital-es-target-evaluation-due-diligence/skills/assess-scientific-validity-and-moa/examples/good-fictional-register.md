# Mechanism register: FICTIONAL FX-701 (bd, asset, markets US and EU)

Reviewer: UNSIGNED    Scientific go/no-go: HUMAN ONLY (scientist: to be named)    Status: Draft
(Every name, study and result here is FICTIONAL.)

## Answer first
- Evidence chain as supplied: human_genetic, resting on one biobank cohort (loss-of-function variants in the kinase KX1 associated with lower fibrosis risk). It is the only human evidence.
- Weakest points: (1) the preclinical finding in the mouse model was only partly reproduced by an independent laboratory; the rat finding was repeated by the originating laboratory alone; (2) target engagement is shown with a blood biomarker in animals but not in humans; (3) a previous KX1 compound failed on efficacy and another KX-family compound carries a class safety warning, and no sourced differentiation addresses either.
- Gaps that change what can be said: differentiation (no basis supplied); human pharmacodynamic data (none). Disabled rule SEOK-MOUSE-HUMAN-R2 is not applied.

## 3. Preclinical evidence and translatability
| Id | Model (species) | Originator | ARRIVE reported / 10 | Not reported | Not assessable | What the model does not represent | Source |
|---|---|---|---|---|---|---|---|
| P1 | bleomycin lung injury (mouse) | FICTIONAL Lab Alpha | 8 | blinding | inclusion and exclusion criteria | chronic, progressive disease in older animals | F-2 |
| P2 | unilateral injury (rat) | FICTIONAL Lab Alpha | 10 | none | none | second species, same laboratory and injury concept | F-3 |

## 4. Independent reproduction
| Finding | Performed by | Independent of originator | Result | Source |
|---|---|---|---|---|
| P1 | FICTIONAL Lab Beta | yes | partial | F-4 |
| P2 | FICTIONAL Lab Alpha | no | reproduced (originator only) | F-3 |

## 6. Class precedent
| Agent | Target / mechanism | Outcome | Source |
|---|---|---|---|
| FICTIONAL compound C1 | KX1 | failed_efficacy | F-5 |
| FICTIONAL compound C2 | KX family | class_safety_warning | F-6 |

## Failure-mode screen
| Mode | State | Register ref or reason | Gap |
|---|---|---|---|
| FM-01 | triggered | independent_reproduction[1] | |
| FM-02 | triggered | preclinical_evidence[0] | |
| FM-03 | triggered | class_precedent[1] | |
| FM-04 | not triggered | human genetic evidence is supplied (one cohort); its strength is a question for the scientist | |
| FM-05 | triggered | preclinical_evidence[0] | |

## Questions for the named scientist
1. Is one biobank cohort enough human support, and has the association been replicated elsewhere?
2. Does the class safety warning for compound C2 apply to FX-701's selectivity profile?
3. What did the previous KX1 compound's failure show, and does FX-701 differ in the way that matters?

## Open items
[GAP]: differentiation basis; human pharmacodynamic data.  Decisions needed (owner): whether to ask the seller for the independent laboratory's full report (deal lead).  Hand-off: review-clinical-data-quality.

## Fact patterns and the real precedents they follow
Every fact below is fictional. The pattern behind it is documented in a registered passage of this skill's `references/verbatim-passages.json`; the real names behind the passages are in the local appendix `docs/due_diligence/EXAMPLES_REAL_PRECEDENTS.md` (not shipped).

| Fact in the example | Pattern documented in | Passage ids |
|---|---|---|
| the human evidence is one biobank association (context, not a probability) | population-level analysis of genetic support | VP-F-001 to VP-F-003 |
| an independent laboratory reproduced the mouse finding only partly | replication effect sizes much smaller than the originals | VP-F-040 to VP-F-043 |
| the rat finding was repeated by the originating laboratory alone | reproduction by the originator is not independent (house rule); selected landmark findings often not confirmed | VP-F-030 to VP-F-032 |
| ARRIVE: blinding not reported, exclusion criteria not assessable | the ARRIVE Essential 10 items | VP-F-016, VP-F-014, VP-F-022 |
| the model does not represent chronic disease in older animals | animal models benefit where trials show none | VP-F-070 to VP-F-072 |
| a prior compound failed; another in the class carries a class warning | class-wide warning triggered by one member's safety trial | VP-F-050, VP-F-051 |
| target engagement shown with a blood biomarker in animals, not in humans | pharmacodynamic biomarker definition | VP-F-075 |
