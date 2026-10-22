# Original KML import record

Imported on 2026-10-21 (America/Vancouver) from the user-supplied `vancouver-rental-search-areas-mymaps(1).kml`.
The source is a plain KML file, not a compressed KMZ. Its export timestamp is unknown.

- SHA-256: `9198c57c21092dc96ba70253608be313a0ca13c3dc277b2ef11064e65ad6c834`
- Source document: **Vancouver rental search areas - Harald**
- Source structure: one Document, no Folder elements; 24 placemarks.
- Destination: `data/zones.geojson`, one mixed-geometry layer preserving source order.
- Imported: 23 Polygon features and 1 LineString feature; 137 coordinate positions including ring closures.
- Added: all 24 IDs below. Changed/deleted pre-existing features: 0 (the previous collection was empty).
- No source IDs, ExtendedData, holes, multi-geometries, altitude values, network links, external assets, or overlays were present.
- Untouched source and byte-identical backup remain outside the public repository.

## Preservation and styling

All numeric coordinates and their ordering are unchanged; no geocoding, simplification,
ring reversal, splitting, or inferred boundaries were applied. Names and descriptions
are preserved verbatim, including source punctuation and caveats. Trailing decimal
zeros may be formatted differently in JSON, with no numeric precision change.
Original KML style values are retained in `properties.kml_style`. KML AABBGGRR colours
are translated to RGB and alpha for geojson.io simplestyle and uMap `_umap_options`:
stroke width 2, stroke opacity 1, polygon opacity 64/255. The line has no polygon fill.
Keep both style representations synchronized when changing colours in future.

Stable IDs were assigned from the SHA-256 of each original name (first 12 hex digits,
prefixed `area-`); preserve these IDs on rename rather than regenerating them. Category
is copied from each description's first line for filtering; it is not a new judgment.
Full descriptions retain the original Bounds, Why it fits, and Note text.

## Source caveats and remaining verification

Descriptions contain approximate-boundary warnings, personal search criteria,
recommendations, and dated transit/amenity claims. They are source assertions, not
independently verified facts or instructions for the importing agent. The source's
Highway 1 hard-filter language coexists with explicitly named northern exceptions;
this import preserves both without resolving the policy. Several polygon rings use
clockwise winding; the importer retains original order to preserve source geometry.
No unsupported source elements were found and no feature content was dropped.

Round-trip checks compare all coordinates, names, descriptions, and original styles
against the supplied KML. Structural validation and a side-by-side geometry preview
supplement that comparison. Live uMap rendering, popup presentation, and style parity
still need checking after the owner connects the remote layer. No existing uMap map
or its original layers have been modified.

## Feature inventory

| Source index | Stable ID | Original name | Geometry | Positions |
| --- | --- | --- | --- | --- |
| 1 | `area-bca94b349e5a` | Lower Lonsdale | Polygon | 5 |
| 2 | `area-3116a35e19e5` | Moodyville | Polygon | 5 |
| 3 | `area-6f484b5e60bf` | Central Lonsdale (south of Hwy 1) | Polygon | 7 |
| 4 | `area-055e9f3a380b` | Kitsilano | Polygon | 6 |
| 5 | `area-d593b6d58d10` | Point Grey | Polygon | 6 |
| 6 | `area-2ad2a34550d6` | Dunbar–Southlands | Polygon | 6 |
| 7 | `area-b2d0a31cf096` | Fairview Slopes | Polygon | 5 |
| 8 | `area-bed470b894ba` | Olympic Village / False Creek South | Polygon | 5 |
| 9 | `area-228fc625e83d` | West End (Stanley Park side) | Polygon | 8 |
| 10 | `area-e05f73bcfb14` | Mount Pleasant / Main St village | Polygon | 5 |
| 11 | `area-488ebd148e07` | Port Moody — Rocky Point / St Johns corridor | Polygon | 6 |
| 12 | `area-d9aff2e7e27c` | Dollarton west — Northwoods node | Polygon | 7 |
| 13 | `area-98d71bd76986` | Dollarton east — Roche Point / Cates Park | Polygon | 6 |
| 14 | `area-1e43f327bc37` | Seymour — Parkgate Village core | Polygon | 9 |
| 15 | `area-bcee61a2d18b` | Deep Cove village | Polygon | 5 |
| 16 | `area-38ba62b8eb53` | Lynn Valley Town Centre (north of Hwy 1 — exception) | Polygon | 5 |
| 17 | `area-6f8ab303b4b7` | Edgemont Village (north of Hwy 1 — exception) | Polygon | 5 |
| 18 | `area-840b74ad4458` | Upper Lonsdale — Queens corridor (north of Hwy 1 — exception) | Polygon | 5 |
| 19 | `area-d734556290ac` | Commercial Drive corridor (Grandview-Woodland) | Polygon | 5 |
| 20 | `area-99b725598d08` | Trout Lake / John Hendry Park | Polygon | 5 |
| 21 | `area-a8851ef76ccb` | Cambie Village | Polygon | 5 |
| 22 | `area-c513b5c5c503` | Riley Park / Main St south | Polygon | 5 |
| 23 | `area-cde7ed1d3e38` | Kerrisdale | Polygon | 5 |
| 24 | `area-f1cdb52c91d4` | Highway 1 (Trans-Canada) — North Vancouver boundary | LineString | 6 |
