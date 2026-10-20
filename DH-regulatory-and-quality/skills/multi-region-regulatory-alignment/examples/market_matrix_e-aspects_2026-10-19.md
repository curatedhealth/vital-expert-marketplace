# Output of scripts/market_matrix.py on saved live data (19 October 2026)

```
python3 scripts/market_matrix.py --search examples/live/search_devices_brainomix_2026-10-19.json --status examples/live/get_market_status_brainomix_e-aspects_2026-10-19.json --jurisdictions examples/live/list_jurisdictions_2026-10-19.json --product e-ASPECTS --markets US,EU,GB,CH,CA,AU,BR,JP
```

Market matrix for 'e-ASPECTS'

| Market | Library result | Class as recorded | Regime / pathway | Latest decision | Identifiers | Source, retrieved |
|---|---|---|---|---|---|---|
| US | Found (2 records) | 2 | US_FDA / FDA_510K | 2025-02-14 | K243294, K221564 | https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K221564; https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K243294 (2026-10-13) |
| EU | Found (4 records) | Class IIa, Class IIb | EU_MDD, EU_MDR / CE_MARK | [GAP] not stored | ++B720EASPECTSCEGK, B-+B720EASPECTS113CE0, B-+B720EASPECTS111CE0, B-+B720EASPECTS112CE0 | https://ec.europa.eu/tools/eudamed/#/screen/search-device (2026-10-14) |
| GB | Register not loaded | | | | | The library holds no records for this register: MHRA medical safety alerts only; device registration (MHRA PARD) is not loaded [GAP] |
| CH | Register not loaded | | | | | The library holds no records for this register: Swissmedic FSCA not loaded in this release [GAP]; swissdamed is web-only [GAP] |
| CA | Register loaded, not searchable by product | | | | | The library holds 227 Health Canada MDALL rows (last load 2026-10-18), but search_devices cannot reach them (no CA in its jurisdiction list; is_software is null). Check MDALL directly. |
| AU | Register not loaded | | | | | The library holds no records for this register: TGA commercial use is blocked |
| BR | Register not loaded | | | | | The library holds no records for this register: No software or programa class. No rows loaded. |
| JP | Register not loaded | | | | | The library holds no records for this register: PMDA forbids automated download |

Note (EU): More than one class recorded in this jurisdiction: read each record (regime, identifier) before comparing.

get_market_status returned 3 rows that disagree on: US, EU. Merged as 'any record found'; a 'false' means no record in the library's copy, not 'not authorized'.
