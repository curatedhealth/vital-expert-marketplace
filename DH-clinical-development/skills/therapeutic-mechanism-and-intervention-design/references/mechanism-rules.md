# Mechanism rules

Interpretive reference for A1 (and the starting point for A2 and B1). Every rule cites its row in `therapeutic-mechanism-research.md` (TM). [PAPER] rows carry their DOI the first time a paper is used here. Nothing in this file sets a threshold, an effect size or a milestone: the sources do not, so those stay the person's.

## 1. What a mechanism statement is

| Rule | Rows |
|---|---|
| A mechanism is a causal link between intervention components and outcomes; context shapes whether and how outcomes occur. Write it as links, not as a feature list. | TM8 (MRC/NIHR framework, DOI 10.1136/bmj.n2061) |
| Program theory states the key components and how they interact, the mechanisms, the contextual features that influence those mechanisms, and how mechanisms may influence context. | TM6 (MRC/NIHR, DOI 10.1136/bmj.n2061) |
| Write the program theory at the start, with stakeholders, from evidence and theory, and refine it in later phases. | TM7 (MRC/NIHR, DOI 10.1136/bmj.n2061) |
| Context is any feature of the circumstances in which the intervention is conceived, developed, evaluated and implemented. | TM9 (MRC/NIHR, DOI 10.1136/bmj.n2061) |
| The six core elements (context, program theory, stakeholders, key uncertainties, refinement, economic considerations) are revisited at every phase and before moving between phases; the paper's own questions can be asked of a draft. | TM4, TM5 (MRC/NIHR, DOI 10.1136/bmj.n2061) |
| An intervention is complex because of component count, range of behaviors targeted, skills needed, levels targeted, or permitted flexibility. Name which apply; each adds links. | TM10 (MRC/NIHR, DOI 10.1136/bmj.n2061) |
| TIDieR item 2 ("Why") is where a description states the rationale, theory or goal of the essential elements. A mechanism statement fills it. | TM23 (TIDieR, DOI 10.1136/bmj.g1687) |

## 2. The chain the old task asked for, mapped to the sources

The old task asked for "the user action, the body or behavior change, and the outcome", the population it is for, and one it is not for. The sources give each link a name:

| Link | What to write | Source term | Rows |
|---|---|---|---|
| Component | What the product delivers (lesson, prompt, reward, sensor feedback, clinician step) | Intervention component; intervention option | TM6 (MRC/NIHR, DOI 10.1136/bmj.n2061), TM79 (JITAI, DOI 10.1007/s12160-016-9830-8) |
| User action | What the person does with it (completes a lesson, logs a craving, practices a skill) | Proximal outcome on engagement; enactment | TM84, TM87 (JITAI, DOI 10.1007/s12160-016-9830-8) |
| Change | The capability, opportunity or motivation change, or the physiological change, the action is meant to produce | Mediator on the causal pathway; COM-B component | TM84 (JITAI, DOI 10.1007/s12160-016-9830-8), TM40 to TM44 (BCW, DOI 10.1186/1748-5908-6-42) |
| Outcome | The clinical outcome the product exists for | Distal outcome | TM83 (JITAI, DOI 10.1007/s12160-016-9830-8) |
| For whom | The population the chain is expected to hold in | Context; tailoring variable | TM9 (MRC/NIHR, DOI 10.1136/bmj.n2061), TM80 (JITAI, DOI 10.1007/s12160-016-9830-8) |
| Not for whom | A population where a link is not expected to hold, with the reason | Context; contraindication or labeled limitation in precedents | TM9 (MRC/NIHR, DOI 10.1136/bmj.n2061), TM138 |

Rules for the chain:
- Each link is a hypothesis; write "expected to", never "does" (pack rule 2).
- Proximal outcomes are often mediators on the causal pathway to the distal outcome (TM84, JITAI, DOI 10.1007/s12160-016-9830-8). Name at least one per link where a measure exists; where none exists, mark `[GAP]` for B1.
- Include an engagement or fatigue proximal outcome where the product depends on repeated use (TM87). Engagement is a link, not the outcome.
- Name the "not for whom" from the person's facts or a precedent's labeled limitation; never from memory.

## 3. Describing the "change" link with COM-B

| Rule | Rows |
|---|---|
| Behavior arises from capability, opportunity and motivation (COM-B). | TM40 (BCW, DOI 10.1186/1748-5908-6-42) |
| Capability: psychological and physical capacity, including knowledge and skills. | TM41 (BCW, DOI 10.1186/1748-5908-6-42) |
| Opportunity: factors outside the individual that make the behavior possible or prompt it. | TM43 (BCW, DOI 10.1186/1748-5908-6-42) |
| Motivation: includes habitual and emotional processes, not only conscious decisions. | TM42 (BCW, DOI 10.1186/1748-5908-6-42) |
| Six subcomponents: physical and psychological capability, physical and social opportunity, reflective and automatic motivation. Say which one each "change" link targets. | TM44 (BCW, DOI 10.1186/1748-5908-6-42) |
| Use COM-B only where the target outcome runs through a behavior. Where the mechanism is physiological or perceptual (for example dichoptic presentation, TM130), describe the change in the terms of the therapy model the person names; COM-B does not apply. | TM40 (BCW, DOI 10.1186/1748-5908-6-42), TM130 |

## 4. Mechanism-level texts in US regulations and the DiGAV (context for design)

These are facts about named classifications. Whether any applies to the person's product is `dh-regulatory-and-quality` regulatory-pathway-and-classification's question (pack rule 4).

| What the text requires | Rows |
|---|---|
| 21 CFR 882.5801 (computerized behavioral therapy, psychiatric disorders): clinical data must describe a validated model of behavioral therapy and validate the model as implemented by the device; software documentation must show the device effectively implements the model. | TM119 to TM121 |
| Similar "model of therapy as implemented by the device" wording appears in 876.5960 (GI), 880.5735 (diabetes, codified 24 July 2026) and 890.5800 (VR pain). | TM127, TM128, TM129 |
| 882.5803 (ADHD), 882.5705 (sleep disturbance) and 886.5500 (amblyopia) instead require clinical performance with validated measures and full software description, without a "model of therapy" requirement. | TM123 to TM125, TM130; research file "Changes and conflicts" 7 |
| Labeling texts tie the mechanism to dose: 882.5804 (fibromyalgia, codified 26 June 2026) requires recommended treatment regimes including frequency and duration of use; 886.5500 requires the length of treatment supported by clinical testing. | TM126, TM130 |
| DiGAV § 2: the application gives aim, mode of action, content and use in plain language, the sources of medical content, and the minimum duration of use the manufacturer considers necessary. | TM149, TM150 |
| DiGAV § 9(2): the claimed positive care effect must be consistent with the intended purpose, functions, content and published statements. A mechanism that does not reach the claimed effect breaks this consistency. | TM148 |
| DiGAV § 8: a positive care effect is a medical benefit or a patient-relevant structure and process improvement (nine named areas, including adherence and health literacy). Name which kind the distal outcome is. | TM145 to TM147 |

## 5. What the mechanism statement must not do

- Describe the mechanism as the feature list (old task rule; TM8 defines mechanisms as causal links).
- Call any link proven, validated or evidence-based unless a passage read in the same direction says so for this population (N3; pack rule 2).
- Borrow a precedent's evidence for the person's product. A precedent shows what a regulator described for that product only (`references/precedents.md`).
