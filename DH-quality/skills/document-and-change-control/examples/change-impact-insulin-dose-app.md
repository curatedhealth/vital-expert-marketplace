# Worked example: "Does release 4.0 of our insulin dose app need a new 510(k) or notified body approval?"

Task A2. The device and its change are illustrative (no real manufacturer); the library calls are real, made on 19 October 2026, and their trimmed outputs are in `examples/live/`. Shown so the model sees the shape of a good answer, not to be reused as current fact.

## The request

"Our insulin dose calculator app is 510(k) cleared and holds an MDR technical documentation certificate (class IIb). Release 4.0 supports a new major iOS version, which changes how dose alerts are processed in the background, and rounds dose recommendations to 0.5 unit instead of 1 unit. No PCCP. Do we need a new 510(k) or notified body approval?"

## Calls made

| Call | Arguments | What came back |
|---|---|---|
| `regulatory-dh.list_jurisdictions` | none | US 1,226 authorizations, 892 safety events, loaded 19 October 2026; EU 3,142 EUDAMED software devices, decision date empty on all; UK alerts only; CH nothing |
| `regulatory-dh.search_devices` | query "Dexcom", jurisdiction US | Comparable QRX device: Dexcom Smart Basal, K252818 |
| `regulatory-dh.get_authorization` | K252818; K222888 | K252818: 510(k), class 2, decided 18 November 2025, product code QRX, regulation 862.1358, predicate K222888. K222888: BlueStar CGM insulin dose calculator, Welldoc, decided 11 August 2023. Neither record states whether a PCCP was authorized |
| `regulatory-dh.search_safety_events` | jurisdiction US, product_code QRX | 10 recall rows (Dexcom CGM apps, Omnipod 5 iOS app); rows carry no product code; one row (sensor theft) is not a software defect |
| `regulatory-dh.retrieve_guidance` | the 2017 software-change guidance; QMSR records; MDCG 2020-3 | Nothing stored; rules taken from `references/` |

The person's own K number was not given, so their baseline record was not fetched: PRE3 stays "no".

## Question sheet

Built with `scripts/change_questions.py` from `change-impact-answers-example.json`; full output in `change-impact-sheet-example.md`. Answers are the person's.

## The answer the skill should give (short mode)

**Frameworks.** FDA's 2017 software-change questions apply (510(k) device; final guidance of 25 October 2017, which predates the QMSR, CH10). MDR Annex IX 4.10 applies (technical documentation certificate, QX30). No PCCP, so the PCCP route does not apply (AI US-10). MDCG 2020-3 does not apply: it covers legacy devices only (CH3).

**Answers that point toward a submission or approval.**
- Q4, yes: dose output resolution is a performance specification tied to intended use (SRS-112). The guidance says a new 510(k) is "likely required" on that answer (CH16).
- Q3a: two of three criteria answered yes (hazard H-07 cause modified; serious pre-mitigation). The third, whether existing control C-07 already mitigates it, is open; Q3a cannot be read until it is answered (CH14, QX18).
- X2, yes: the change affects the conditions of use of the dose recommendation. Annex IX 4.10 says such changes need approval of the notified body that issued the certificate, and the notified body decides between a new conformity assessment and a supplement (QX30, QX31).

**Answers that point toward documenting only.** F2, no: a feature change not made to reduce a risk to health is exempt from part 806 reporting, but a record with a justification reviewed by a designated person is kept (VG23, VG24).

**Open.** PRE0 (is the rounding change meant to significantly affect safety or effectiveness? If so, the guidance says a new 510(k) is likely required regardless of the questions, QX35), PRE2 (background-processing side effects not assessed), PRE3 (baseline K number), Q3a3, Q3b, POST1 (V&V results). Two other baseline gaps: releases 3.2 and 3.3 were not assessed together with 4.0 (QX12, QX13).

**Context, not evidence.** Released CGM app versions have been recalled for background-processing defects: a Class II recall dated 14 April 2026 describes a file I/O check that "blocks the higher-priority thread responsible for processing estimated glucose values" when the app runs in the background (library, openFDA enforcement, retrieved 13 October 2026). That bears on PRE2 for part (a) of the change.

**Decision.** For the owner (owner not named: who decides?). Not decided here. AI-assisted draft, uncleared. Want the full sheet for the change board?

## Why this is a good answer

It names the frameworks and says why one does not apply. It quotes the guidance's own hedge instead of concluding. It refuses to read Q3a with a criterion open. It turns a public recall into a question for the person's own risk assessment, not a claim about their app. It leaves the decision and the owner to the person.
