# Worked example: A2 for a stroke CT triage device after clearance

Live library calls on 19 October 2026; trimmed outputs in `live/`. The product ("StrokeSense", 510(k) with an authorized PCCP, product code QAS) and its change log are illustrative inputs supplied by the person in this example; the safety rows are live library data.

**Request:** "Since our clearance we retrained twice on new-site data and switched the DICOM parser to a new vendor library. Our PCCP covers retraining only. Were these covered, and has anything happened to Aidoc or Brainomix devices that we should know about?"

**Person's PCCP facts (illustrative):** Description of Modifications lists "re-training on data from additional sites"; acceptance criterion set by the person: sensitivity of at least 0.90 on the locked test set. Change log: retrain 1 (result 0.92), retrain 2 (result 0.89), parser library swap (no test recorded).

**Calls made**

1. `regulatory-dh.list_jurisdictions` (free): US and UK hold safety events; EU and CH none.
2. `regulatory-dh.search_safety_events` `{manufacturer: "Aidoc", limit: 10}` and `{product: "BriefCase", limit: 5}`: no recalls; MAUDE QAS 0, QFM 0, QIH 10.
3. `regulatory-dh.search_safety_events` `{manufacturer: "Brainomix", limit: 10}`: no recalls; MAUDE POK 1 (2021), QAS 0, QIH 10.
4. `regulatory-dh.search_safety_events` `{manufacturer: "Viz.ai", limit: 10}`: nothing, because the store spells it "Viz.Al, Inc.".
5. `regulatory-dh.search_safety_events` `{product_code: "QAS", jurisdiction: "all", limit: 10}`: ten Siemens fluoroscopy and CT recalls, none a QAS device; MAUDE QAS 0.

## Answer (short mode)

**Answer.** Retrain 1 sorts as in the PCCP as described, with your recorded result (0.92) above your criterion (0.90). Retrain 2 is in the PCCP, but your recorded result (0.89) is below your criterion: a change implemented outside its Modification Protocol would deviate from the authorized plan, which FDA says would generally make the device adulterated and misbranded [AI US-12, US-13]. Whether it was released, and what follows, is the regulatory owner's decision. The parser swap is not in your PCCP, so the 2017 software-change questions apply [Q CH9 to CH16]; it touches the input path, so question 3a (new or modified hazard) is the first to answer. No recall in the library names an Aidoc or Brainomix device.

| # | Change | In the PCCP? | Your criterion · your result | Sort (owner to confirm) | Row |
|---|---|---|---|---|---|
| 1 | Retrain on new-site data | Yes | 0.90 · 0.92 | In the PCCP as described | AI US-12 |
| 2 | Retrain on new-site data | Yes | 0.90 · 0.89 | In the PCCP but the protocol's criterion is not met on your record | AI US-13 |
| 3 | DICOM parser library swap | No | None recorded | Outside the PCCP: 2017 questions apply, owner decides | Q CH11 to CH16 |

**Safety context.** MAUDE: 0 reports for QAS; 10 for QIH (2024 to 2026), across all QIH devices, not attributable to Aidoc or Brainomix. The ten recalls returned for product code QAS were Siemens imaging systems, not QAS devices, and were excluded.

**Open items.**
1. Release status of retrain 2 and who decides on it: owner not named.
2. Verification evidence for the parser swap `[GAP]`.
3. Viz.ai events need a search under the stored name "Viz.Al, Inc." or a check in FDA's databases.

**Record:** Tracking draft. Coverage of changes and reportability are the owner's decisions. Library records retrieved 13 and 14 October 2026. Uncleared.

## What this example shows

- The model compares the person's recorded result to the person's own criterion and states both numbers; it does not set or judge the criterion.
- Off-target recalls from a product-code search are excluded and counted, not presented as comparables' events.
- MAUDE counts stay with their product code.
