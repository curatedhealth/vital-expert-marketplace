# Worked example: A1 for a permanently listed depression DiGA

Live library calls on 19 October 2026. The product and its own measures are illustrative inputs from a test request; every official fact cites its row and every library fact its call.

**Request:** "We are a permanently listed DiGA for depression (F32, F33). The GKV-Spitzenverband wants to talk about the outcome-linked part of our price. We collect PHQ-9 at start and week 12 in the app, and minutes of use. What could we put on the table as outcome measures? Also check that the PHQ-9 is validated for tracking change."

**Calls made**

1. `market-access-dh.retrieve_guidance {query: "erfolgsabhängige Preisbestandteile DiGA outcome-based price component", limit: 5}`: no passage, `[GAP]`. The library holds no guidance on DiGA outcome components.
2. `market-access-dh.find_scheme_precedents {scheme: "DE_DIGA", indication: "F32", limit: 10}`: 7 depression DiGA, 1 provisional and 6 permanent; trimmed copy in `de_diga_F32_precedents_2026-10-19.json`.
3. `literature.search_literature {query: "PHQ-9 minimal clinically important difference validation", limit: 5}`: Löwe et al. 2004 (Medical Care, PMID 15550799) ranked first; the other four records were off topic and were dropped.
4. `literature.get_record {pmid: "15550799"}`: abstract opening returned.
5. `verify.qualify_source {doi: "10.1097/00005650-200412000-00006"}`: tier gold.
6. `verify.check_claim` with the quoted abstract passage and the qualified source object: supported. (The same call with `source: {doi}` alone returned unverifiable; see `references/tools.md`.)

## Answer (short mode)

**Answer.** On the facts, your PHQ-9 change score is proposed as the lead candidate (you choose): you already collect it at start and week 12, it is an indication-specific instrument, and you own the data. Minutes of use are easy to collect and will be in the official AbEM data, but they measure use, not health. The decision for you: whether to offer an interim measure now (your PHQ-9) and a switch to the official AbEM PROMs once they exist, because the 20 percent outcome-linked share has applied since 1 January 2026 while AbEM PROMs start only in 2027 and 2028 (OC Germany rows; DE-18).

**Candidates**

| Measure | Origin (row) | Data source and owner | Burden | Attribution risk | Baseline needed |
|---|---|---|---|---|---|
| PHQ-9 change, start to week 12 | Yours | In-app questionnaire; owner not named `[GAP]` | Two questionnaires per patient, already collected | No comparator; patients who stop using the app never give a week-12 score | Yes, at start |
| Weekly minutes and frequency of use | Yours and AbEM Stage I, from 1 July 2026 (DE-18) | App logs; reported to BfArM twice a year | Already logged | Use is not health; reminders can raise minutes without change | No |
| Single-item PROM | AbEM Stage II, 2027 (DE-18) | Manufacturer, reported to BfArM | Voluntary, one reminder allowed (DiGAV § 23a) | Instrument not named in sourced rows `[GAP]` | Depends on method `[GAP]` |
| Indication-specific PROM | AbEM Stage III, 2028 (DE-18) | Manufacturer | Voluntary, one reminder allowed (DiGAV § 23a) | Instrument and method not set `[GAP]` | Depends on method `[GAP]` |

**Limits of the official set.** AbEM covers permanently listed DiGA only; patient answers on satisfaction and PROMs are voluntary with one reminder allowed (DiGAV § 23a); how AbEM feeds the price component is still to be set by the framework partners (DE-19).

**Instrument check.** Löwe et al. 2004 studied responsiveness, reproducibility and the minimal clinically important difference of the PHQ-9 in 434 IMPACT trial patients: supported by the abstract (Verify, gold source). The MCID value itself is not in the abstract passage, so it is not quoted here: not verified from the abstract.

**Open inputs.** Owner of the PHQ-9 data; your week-12 completion rate (decides how much payment missing data would cost under a patient-level rule).

**Full version.** Ask for full mode to add the comparables the library holds (seven depression DiGA, with what it cannot say about their prices) and the measure definitions.

**Record.** Draft for the owner. Measures are not chosen until the accountable owner decides; owner not named: who decides? Uncleared. AI-assisted draft.

## What this example shows

- The library had nothing on outcome components, so the official facts came from `references/` with their rows.
- The two-step Verify sequence works only with the qualified source object.
- Short mode stays under 450 words: the comparables (and what the library cannot say about them) move to the full version.
