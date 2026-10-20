# Implementation blueprint: what a deployment plan holds

Interpretive reference for task A1. Every rule cites its row in `customer-success-research.md` (CS rows). Rows marked [PAPER] are published methods; cite the DOI given in the row. Frameworks here give structure and definitions, never thresholds or predictions.

## 1. The blueprint skeleton

ERIC's "develop a formal implementation blueprint" names four parts (CS42, Powell et al. 2015, DOI 10.1186/s13012-015-0209-1):

| Part | What goes in it for a customer deployment | Source |
|---|---|---|
| Aim and purpose | What the site wants the product to change, in the site's words | CS42 |
| Scope | Which organizational units are affected: sites, departments, user groups, modules, integrations in the first release and later | CS42 |
| Timeframe and milestones | The person's and the site's dates; "unset" where none is agreed | CS42 |
| Performance and progress measures | Named measures with one definition each (section 4) | CS42 |

ERIC adds that the plan is used and updated over the implementation (CS42). CFIR 2022 "Planning" asks for roles, steps, milestones and success measures defined in advance (CS20).

The register's own scope method (old task CF-12.02.02.1.1.1) adds three items the skeleton must show: the site, modules and users in the first release; the integrations in the first release and those that come later; the clinical workflow that must work on day one. Its rule: do not include a module the site has not agreed to.

## 2. Core components and what may be adapted

- Name the core components (essential, keep) and the adaptable periphery (may change locally) (CS4, CFIR 2009).
- ERIC "promote adaptability": say how the product can be tailored and which elements must stay fixed to preserve fidelity (CS48).
- Why it matters for the sibling skill: fidelity is later measured against what was planned (CS9, CS37), so the plan must say what "as planned" means.

## 3. Context assessment

Use one framework per question and say which version.

**CFIR 2022** (Damschroder et al. 2022, DOI 10.1186/s13012-022-01245-0): 48 constructs and 19 subconstructs across 5 domains (CS10). Before use, define each domain for the project and rewrite constructs in project language (CS11). For a customer deployment, the inner setting is where the product is used (for example a hospital) and the outer setting is the system around it (for example a hospital system or state) (CS12). Constructs that map to a deployment plan:

| Question | CFIR 2022 construct | Row |
|---|---|---|
| Does it fit the site's workflows and systems? | Compatibility | CS14 |
| Is it a priority against other initiatives? | Relative priority | CS14 |
| Are funding, space, equipment there? | Available resources | CS15 |
| Is guidance and training reachable? | Access to knowledge and information | CS15 |
| Is there external financing (for example reimbursement) or a policy or law that supports it? | Financing; Policies and laws | CS16 |
| Can it be piloted small and undone? | Innovation trialability | CS13 |
| Who leads, delivers and receives it? | High-level leaders, implementation leads, deliverers, recipients | CS18 |
| Can each role do it? | Capability, opportunity, motivation | CS19 |

CFIR does not state relationships between constructs and is not a causal model (CS3). Never present a construct as the cause of a delay; at most "a construct to check". Implementation Climate and Readiness for Implementation were removed in 2022 (CS17); if the person uses the 2009 readiness construct (leadership engagement, available resources, access to information, CS7), say it is the 2009 version.

**Readiness assessment** (ERIC): readiness, barriers and strengths (CS43). Report what the person states under each; do not grade readiness without the person's scale.

**NASSS** (Greenhalgh et al. 2017, DOI 10.2196/jmir.8775): seven domains (CS50), each rated simple, complicated or complex (CS51). Programs with complexity in several domains rarely became mainstream (CS51); this is a qualitative heuristic, not a threshold. Useful questions: whether funding depends on savings across several unlinked organizations (CS53); what the product asks of patients (CS54); supply-side and demand-side value (CS52). NASSS has published uses in planning rollout and explaining failure (CS55). The rating is the person's; the model lays out the domain questions and what the person said.

## 4. Measures: one definition per measure

The measures in the blueprint should be implementation outcomes, kept separate from clinical outcomes: implementation outcomes are preconditions for clinical or service outcomes (CS32, Proctor et al. 2011, DOI 10.1007/s10488-010-0319-7). Usage or activation is not efficacy (worker stop rule, `examples/live/agent_pack.json`).

| Measure | Definition to name in the plan | Row |
|---|---|---|
| Acceptability | Perception that the product is agreeable or satisfactory | CS33 |
| Adoption | Intention, decision or action to try it (Proctor); or percent of settings approached, and of staff invited, that take part (RE-AIM) | CS34, CS28 |
| Appropriateness | Perceived fit for the setting or problem | CS35 |
| Feasibility | Extent it can be carried out in the setting | CS36 |
| Fidelity | Degree it was implemented as planned | CS37 |
| Implementation cost | Cost impact of the implementation effort | CS38 |
| Penetration | Eligible users who use it / all eligible; or providers delivering / providers trained or expected to deliver | CS39 |
| Reach | Number, proportion and representativeness of eligible people who take part, on a valid denominator, not volunteers | CS22, CS27 |
| Sustainability or maintenance | Kept in routine operations; RE-AIM checks a program still running 6 or more months after support ends | CS40, CS26, CS30 |

Terms overlap: penetration is similar to reach, sustainability maps to maintenance, adoption has two definitions. Pick one definition per measure and name it (research file, "Changes and conflicts"). Targets for any measure are the person's.

## 5. What the site needs from the company (NICE ESF deployment standards)

The NICE Evidence Standards Framework (ECD7, last updated 9 August 2022, CS56) has three deployment standards that apply to all tiers (CS57). Where the customer is an NHS organization or uses NICE's framework, they are a checklist for the blueprint; elsewhere, label them "NICE ESF, used as a checklist".

| Item | Row |
|---|---|
| Training and education needs, and barriers or enablers to implementation, in the pathway description | CS58 |
| Data dictionary, tolerance for incomplete data, deployment data flow map, data formats, minimum infrastructure | CS64 |
| Communication to users on outputs, features, benefits and limitations; the company's end-user training approach | CS65 |
| Load testing at the scale of expected uptake | CS66 |
| Expected usage profile agreed at commissioning, with ongoing usage and anonymized aggregate outcome reporting | CS61 |
| For products that change over time: how and when performance changes are reported, and to whom | CS62 |
| Implementation costs (staffing, training, IT infrastructure) in the budget impact | CS63 |
| Silent-mode evaluation on local data before use in care, for products affected by local factors such as AI (option) | CS60 |

## 6. Published programs (optional)

Where the person wants published implementation experience for a comparable product, search the literature and accept a statement only after `verify.qualify_source` then `verify.check_claim` with a passage read that states the finding in the same direction (`references/tools.md`). A published program is context, never a target or a forecast for this site.
