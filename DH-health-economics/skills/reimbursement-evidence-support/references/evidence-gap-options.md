# Options for closing evidence and economic gaps (B1)

Interpretive reference for B1. Each option is a sourced method with the row it rests on. These are options to lay out, never a plan you choose: which gap to close, how, and in what order is the person's decision. Rows read 19 October 2026; not owner-reviewed. [PAPER] rows cite their DOI; "abstract only" is stated.

## By kind of gap

| Gap found in A2 | Sourced option | What it gives, and its limit | Rows |
|---|---|---|---|
| No full model, early-use route | Reuse an existing model or its outputs; else a simplified model, or intermediate outcomes with threshold analysis | Accepted for NICE early use; the reference case still applies and deviations are discussed with NICE early | `HE-069`, `HE-070` |
| The decision hinges on one uncertain input | Threshold analysis that reports the switching value of that input | Shows what the input would need to be for the decision to change at a given threshold; NICE asks for it for rapidly iterating technologies | `HE-077` |
| Several uncertainties; which research is worth doing | Value of information analysis | Puts a value on reducing decision uncertainty with new evidence; aimed at adoption and research-funding decisions. [PAPER] Fenwick et al. 2020, DOI 10.1016/j.jval.2020.01.001, abstract only | `HE-031` |
| Uncertainties a body wants resolved through use | Evidence generation during NICE early use | Only uncertainties resolvable within 3 years of publication qualify | `HE-071`, `HE-072` |
| Effect or resource-use evidence from routine data | A hypothesis-evaluating (HETE) real-world study: declared in advance, protocol and analysis plan registered before analysis, results published with conformance or deviation, tested on a different data source where feasible, stakeholders including HTA bodies and payers involved | Makes a real-world study credible to a body; it does not turn exploratory data into a test. [PAPER] Berger et al. 2017, DOI 10.1002/pds.4297 | `HE-025` to `HE-030` |
| Utilities not from EQ-5D, or from the wrong value set | Collect EQ-5D-5L and value it with the set the body names (UK 5L for new NICE topics; French 5L for HAS) | Mapping is a NICE departure and needs a described, justified function | `HE-058`, `HE-045`, `HE-106` |
| No BIA, or a BIA without the ESF or IQWiG elements | Build or extend the BIA: eligible population, mix before and after, technology and implementation costs, comparator costs, decision-maker scenarios; a simple cost calculator where it can capture the problem | Validation at least by face validity with decision makers and verification of calculations | `HE-019` to `HE-024`, `HE-088`, `HE-112` |
| Costs not in the body's currency or system | Re-cost with the body's own sources (NICE ESF names NHS reference costs, national tariff, PLICS) | Unit costs and prices are the person's inputs; never filled from memory | `HE-089`, `HE-008` |
| Perspective differs from the body's | Add a reference-case analysis in the body's perspective; keep the other as a separate analysis | NICE: NHS and PSS; HAS: collective; IQWiG: SHI community; ICER-PHTI: user and payer | `HE-035`, `HE-037`, `HE-103`, `HE-110`, `HE-123` |
| Reporting incomplete | Report the missing CHEERS 2022 items | Completeness of reporting, item by item, never a score | `HE-001`, `HE-005` |
| No comparative clinical evidence for the comparator the body uses | A comparative study against that comparator. What a body asked for in comparable published decisions is read with the monitoring skill (`reimbursement-evidence-monitoring`, A1) | Study design belongs to dh-clinical-validation `study-protocol-and-endpoint-design` | `ES-127` (NICE); `HE-115` is ICER-PHTI context only |
| Digital technology still in evidence generation | ESF early deployment subset (16 standards, no BIA or CEA) for evidence-generation programs | Not a substitute for standards 17 and 18 at commissioning | `HE-092` |
| Evidence for an EU JCA | Systematic review to the JCA rules (MEDLINE and CENTRAL at least, 3-month cut-off, RoB 1 and ROBINS-I, PRISMA flow) | Method belongs to dh-clinical-validation `literature-and-real-world-evidence-review`; JCA does not assess economics | `ES-155`, `ES-156`, `ES-163`, `ES-164`, `ES-162`, `HE-094` |

## Ordering by dependency (how to lay it out, not what to choose)

Some gaps block others. Lay out the dependency so the person can sequence:

1. **Scope facts first.** Device class, intended purpose and ESF tier (from the owner the person names for device status, or owner not named). They decide which items apply at all.
2. **Clinical effect before economics.** A model's result is only as good as its effect input; a gap in comparative effectiveness blocks every economic conclusion that rests on it.
3. **Utilities and costs before the model result.** Value set, perspective and unit costs change the ICER and the BIA; fix inputs before re-running.
4. **Model before the economic section.** The dossier section can only describe what the model shows.
5. **Reporting last.** CHEERS items document what exists.

Within a level, the order is the person's. If asked to rank, the person scores each gap on criteria they choose; `analytics.mcda` or `analytics.rice` ranks only those scores (`tools.md`). Report where a weight change would swap two gaps, worked by hand (the connector returns no robustness view).
