# Rental search priorities

Updated 2026-10-21 at the owner's request following the area-fit discussion.
These are search priorities and conditional eligibility, not property endorsements
or claims about current rental availability. No geometry was changed.

| Priority | Map colour | Areas |
| --- | --- | --- |
| Lead the search | `#18794e` | Lower Lonsdale, Moodyville, Kitsilano, Fairview Slopes |
| Search consistently | `#2478b4` | Central Lonsdale (south of Hwy 1), Mount Pleasant / Main St village, Commercial Drive corridor (Grandview-Woodland), Trout Lake / John Hendry Park |
| Exceptional-home opportunities | `#a66b16` | Point Grey, Dunbar–Southlands, Port Moody — Rocky Point / St Johns corridor |
| Selective property search | `#7e57a5` | Olympic Village / False Creek South, West End (Stanley Park side) |
| Nature-focused alternative | `#bc641b` | Dollarton west — Northwoods node, Dollarton east — Roche Point / Cates Park, Seymour — Parkgate Village core, Deep Cove village |
| Northern exception: case-by-case | `#aa4276` | Lynn Valley Town Centre (north of Hwy 1 — exception), Edgemont Village (north of Hwy 1 — exception), Upper Lonsdale — Queens corridor (north of Hwy 1 — exception) |
| Trial search area | `#008b8b` | Cambie Village, Riley Park / Main St south |
| Proposed: not activated | `#757575` | Kerrisdale |
| Reference boundary | `#c62828` | Highway 1 (Trans-Canada) — North Vancouver boundary |

## How to apply these priorities

- Lead with Lower Lonsdale/Moodyville, Kitsilano, and Fairview Slopes.
- Keep searching Central Lonsdale, Mount Pleasant/Main, and the named East Vancouver pockets. East Vancouver is still case-by-case, even when searched consistently.
- Consider Point Grey/Dunbar and Rocky Point when the home is particularly strong. Port Moody remains the named municipality exception.
- Be property-selective in Olympic Village and the West End.
- Treat Deep Cove, Dollarton, and Parkgate as nature-focused alternatives requiring a workable everyday walking and transport experience.
- Retain the three existing northern village pockets as case-by-case exceptions; do not expand their boundaries or approve all areas north of Highway 1.
- Activate Cambie Village and Riley Park as trial search areas. Kerrisdale remains an unactivated proposal.

Check each real civic address for actual walks to groceries, a cafe, park/waterfront
access, and useful transit, including hills. The owner's regular destinations and
travel mode are unresolved, so these are provisional fit judgments rather than a
commute-based ranking. A good location never overrides the property requirements.

## Data and styling

`search_priority` controls the displayed search grouping; `search_status` distinguishes
core, approved exception, case-by-case, trial, proposed, and reference features.
`search_guidance` explains the practical trade-off. `category` now reflects the current
priority. The normal `description` popup starts with current guidance, followed by
clearly labelled historical KML notes. Original descriptions and categories are
preserved in `source_description` and `source_category`; original KML style values
remain in `kml_style`. Preserve these historical fields on future edits.

Both geojson.io simplestyle and uMap `_umap_options` colours were updated together.
Opacity, line width, all 24 stable IDs, all 137 coordinate positions, and source
provenance remain unchanged. No features were added or removed; properties were
updated on all 24 features. The Highway 1 reference note now explicitly acknowledges
the named northern exceptions rather than presenting the line as an absolute rule.

After merge, reload the uMap remote layer and verify its colours and popups. If the
popup uses a custom template, include `{name}` and `{description}`. The existing
remote URL stays the same. These edits do not create separate toggleable layers;
they preserve the original single-layer structure.
