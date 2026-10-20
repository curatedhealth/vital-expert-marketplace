# A1 Positioning check set and artifact sample

Framework task: DH-02.01.2.2, Part A, task A1. Replaces the old "Positioning check set" and "Artifact sample" tasks.

## What this task delivers

A check set (each artifact that must carry the line, its segment, its pass rule as the person writes it, and who samples it) and a sample of the in-market copies: the line present, altered or absent in each, the sentence that contradicts or extends the line quoted, and words flagged against the sourced promotion rules. It answers "is our positioning actually what customers see?"

Why it matters: in every market read, promotional material is part of the intended use (PC-US-17, PC-EU-03, PC-UK-01). A line that drifts in an app store page or a leave-behind changes what the product claims to be, whatever the approved messaging says.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Marketing Manager (`digital-marketing-manager`) |
| Skill | DH-02.01.2.2 Part A, Positioning check set and artifact sample |
| Workflow | The steps below |
| Knowledge | `references/positioning-rules.md`; `references/monitoring-signals.md` (signals 1 and 2); `references/promotion-and-claims-sources.md` |
| Tools | `scripts/positioning_check.py sample` (optional, with code execution). No library call: the person's copies stay out of the connector |
| Prompt | This guide |
| Template | `assets/check-and-sample-output.md` |
| Input | The request and its context; the positioning line per segment; the claim list; the in-market copies (text, files or pasted); who samples and how often, as the person sets it |
| Governance | `references/governance.md`; flags are signals; claims stop for the regulatory or legal owner |
| Catalogue job | none. The person's copies stay out of the connector. |

## Read the request

- **The line.** Required, per segment. If missing, ask, or point to the segmentation skill (B2).
- **Artifacts.** The ones the person names. Offer the channels the UK guidance names as promotional (adverts, app store description and category, landing page, social media; PC-UK-01) plus the old method's list (leave-behind, site, partner brief) for the person to accept or drop.
- **In-market copy.** Only what customers see now. A draft is "not scored".

## Workflow

### Step 1. Write the check set with the person

One row per artifact: artifact, segment, the line it must carry, pass rule (the person's words; offer the register's shape "the line is present and no contradicted claim is present"), sampler and how often (the person's). Write it back for confirmation. Missing sampler: "sampler not named"; ask.

### Step 2. Collect the copies

Ask for one current in-market copy of each artifact. Mark artifacts with no copy "not measurable `[GAP]`".

### Step 3. Mark the line

For each copy: present (the line as written), altered (a close variant; quote it), or absent. With code execution, save the copies as text and a check set CSV (columns artifact, file, segment, line, in_market, sampler) and run `scripts/positioning_check.py sample <checkset.csv>`; its similarity cut for "altered" is a tool setting, and the person's rule decides whether an altered line passes. Without code, compare by reading and quote the closest sentence.

### Step 4. Flag the words

For each copy, list sentences that hold a flag word from `positioning-rules.md`: device-indicating words (PC-UK-04), approval wording (CP-US-74, PC-EU-11, PC-UK-08), certainty or no-side-effect wording (PC-DE-04; PC-UK-13 [INDUSTRY]), wellness exit wording (PC-US-63), testimonials (PC-UK-03). Quote the sentence and give the row. Then read for what a word list misses: a use, population or result beyond the stated intended use (Rule 1), a comparison (Rule 5), a disclaimer contradicted elsewhere (PC-UK-02). Each is a flag for the owner, never "non-compliant".

State for each artifact whether a source treats it as promotional: the app store description, category and landing page are promotional material in Great Britain (PC-UK-01). For Germany, mark whether the copy reaches only professional circles (PC-DE-02) or the public (PC-DE-09); if that is unknown, ask and mark `[GAP]`.

### Step 5. Contradicted claims

Where the person supplied a claim list, quote any sentence that states a claim not on it or contradicts one on it. That is the register's "contradicted claim".

## Build the output

Follow `assets/check-and-sample-output.md`. Short mode: per artifact the line status and the most serious flag, then not-measurable artifacts, then the stop. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Only in-market copies scored; drafts marked "not scored".
- Every flag quotes its sentence and cites its row; [INDUSTRY] and [WF] said.
- No verdict without the person's pass rule (that is B1).
- Flagged claims routed to the claims audit (DH-02.01.3.2) and the regulatory or legal owner.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- The model marks and flags; it does not clear copy, rewrite artifacts in market, or judge the people who wrote them.
- Copy, lines and claim lists never go into a library call.
- Drugs, biologics and wellness apps are out of scope.
