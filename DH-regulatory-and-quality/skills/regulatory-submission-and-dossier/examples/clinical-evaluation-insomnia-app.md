# Worked example: A2 clinical evaluation support on live library data

Run on 19 October 2026 against the VITAL Digital Health Library. The product is a hypothetical prescription app delivering cognitive behavioral therapy for insomnia, intended for EU class IIa under Rule 11 (as the person's regulatory owner decided) and a later US 510(k). Trimmed outputs: `examples/live/literature_2026-10-19.json`, `examples/live/verify_2026-10-19.json`, `examples/live/retrieve_guidance_2026-10-19.json`.

## The request

"We're building the CER for our insomnia CBT app, class IIa under Rule 11 per our RA lead. We have our verification and validation reports and a usability study. Our draft CER says app-based CBT-I prevents depression in young people, citing the PLOS Medicine trial. What do we have and what's missing?"

## Calls made (7 counted)

1. `regulatory-dh.retrieve_guidance(query="clinical evaluation", limit=5)`: five EMA vaccine and medicines passages, none device guidance. Not used.
2. `literature.search_literature(query="digital cognitive behavioral therapy for insomnia randomized controlled trial app", limit=5)`: 18 merged records; five returned.
3. `literature.get_record(pmid="39836656")`: the PLOS Medicine RCT; excerpt ends after the methods sentence.
4. `literature.classify_study(record=<conference abstract 10.1093/ijnp/pyae059.428>)`: "meta_analysis", decided by title text.
5. `literature.grade_evidence(records=[RCT, conference abstract], question_type="treatment")`: level 2 and level 1.
6. `verify.qualify_source(doi="10.1371/journal.pmed.1004510")`: gold, current.
7. `verify.check_claim(...)` with the only passage available (aim and design): "supported", 86% overlap. Not accepted (see below).

## The answer (short mode)

**Answer.** Technical performance has evidence (your V&V reports). Valid clinical association and clinical performance have no evidence of your own yet, and the depression claim in your draft is not checked. Next decision for your regulatory owner: whether the depression-prevention statement belongs in your intended purpose at all; if it does, it needs its own clinical data (RP EU-20).

**Evidence by component (MDCG 2020-1)**

| Component | Your evidence | Type | Row |
|---|---|---|---|
| Valid clinical association | None listed `[GAP]` | Literature or guidelines can count | S-60 |
| Technical performance | V&V reports | Verification and validation | S-61 |
| Clinical performance | None listed `[GAP]`; the usability study is not clinical performance on its own | Testing in the target population | S-62 |

**Candidate literature (library, 19 October 2026)**

| Record | Design (basis) | Draft level | Note |
|---|---|---|---|
| 10.1371/journal.pmed.1004510 | RCT (publication type) | CEBM 2 | Youth with insomnia and subclinical depression; excerpt ends before results |
| 10.1093/ijnp/pyae059.428 | Conference abstract; library label "meta-analysis" from title text | Library gave 1; not a systematic review | Pooled analysis of two trials, abstract only |
| 10.3349/ymj.2024.0398 | RCT (publication type) | not graded | Adherence and effectiveness |

These are candidates for your systematic review (S-58), not the review.

**The depression claim.** Verify returned "supported", but the only passage available states what the trial set out to test, not what it found. Not checked: no results passage `[GAP]`. Send the results paragraph or table and the check can be run properly.

**Gaps the notified body will see (CEAR, S-66)**
1. Section C: no clinical evaluation plan elements beyond the class.
2. Section D: no systematic literature review protocol.
3. Section F: no PMCF plan or justification (S-54).

**Record.** Uncleared draft, AI-assisted. Clinical wording is a draft for the regulatory owner.

Full version available: adds the plan skeleton, the amount and quality questions, and the CEAR mapping per section.

## What the run showed about the tools

- The guidance store does not hold device clinical-evaluation guidance (register C6 evidence).
- A design label from title words lifted a conference abstract to level 1 (register N8 evidence).
- `check_claim` said "supported" from a passage stating the aim only (register N3 evidence).
