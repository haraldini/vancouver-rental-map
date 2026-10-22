# Rental search priorities

Updated 2026-10-21 at the owner's request following the area-fit discussion.
These are search priorities and conditional eligibility, not property endorsements
or claims about current rental availability. Current outlines follow the [authorized redraw](redraw-2026-10-21.md).

| Priority | Map colour | Areas |
| --- | --- | --- |
| Lead the search | `#18794e` | Lower Lonsdale, Moodyville, Kits beach-side / Kits Point, Fairview Slopes, Kits southern residential streets |
| Search consistently | `#2478b4` | Central Lonsdale shopping corridor, Mount Pleasant / Main St village, Commercial Drive corridor (Grandview-Woodland), Trout Lake / John Hendry Park |
| Exceptional-home opportunities | `#a66b16` | Point Grey, Dunbar village corridor, Moody Centre / Rocky Point, Southern Dunbar, Grand Boulevard residential pocket |
| Selective property search | `#7e57a5` | Olympic Village, West End (Stanley Park side), Suter Brook / Newport / Inlet Centre |
| Nature-focused alternative | `#bc641b` | Dollarton west — Northwoods node, Dollarton east — Roche Point / Cates Park, Parkgate village core, Deep Cove village, Southlands rural pocket, Seymour southern residential lobe |
| Northern exception: case-by-case | `#aa4276` | Lynn Valley Town Centre (north of Hwy 1 — exception), Edgemont Village (north of Hwy 1 — exception), Upper Lonsdale — Queens corridor (north of Hwy 1 — exception) |
| Trial search area | `#008b8b` | Cambie Village east, Riley Park / Main St south, Douglas Park / Heather streets, False Creek South / Charleson Park, Fraser village / E 24th–33rd, Hastings-Sunrise village pocket, Burquitlam station pocket, Lafarge Lake / Town Centre edges, Austin Heights village pocket |
| Proposed: not activated | `#757575` | Kerrisdale |
| Reference boundary | `#c62828` | Highway 1 (Trans-Canada) — North Vancouver boundary |

## How to apply these priorities

- Lead with Lower Lonsdale/Moodyville, Kitsilano, and Fairview Slopes.
- Keep searching Central Lonsdale, Mount Pleasant/Main, and the named East Vancouver pockets. East Vancouver is still case-by-case, even when searched consistently.
- Consider Point Grey/Dunbar and Rocky Point when the home is particularly strong. Port Moody remains the named municipality exception.
- Be property-selective in Olympic Village and the West End.
- Treat Deep Cove, Dollarton, and Parkgate as nature-focused alternatives requiring a workable everyday walking and transport experience.
- Retain the three existing northern village pockets as case-by-case exceptions; do not expand their boundaries or approve all areas north of Highway 1.
- Trial areas include Cambie Village, Douglas Park, Riley Park, False Creek South, Fraser village, Hastings-Sunrise, and the three named Coquitlam pockets. Kerrisdale remains an unactivated proposal.

Check each real civic address for actual walks to groceries, a cafe, park/waterfront
access, and useful transit, including hills. The owner's regular destinations and
travel mode are unresolved, so these are provisional fit judgments rather than a
commute-based ranking. A good location never overrides the property requirements.

## Data and styling

`search_priority` controls the displayed search grouping; `search_status` distinguishes
core, approved exception, case-by-case, trial, proposed, and reference features.
`search_guidance` explains the practical trade-off. `category` now reflects the current
priority. The normal `description` popup contains only three short lines: Good, Bad, and
Important. Keep history, changelogs, provenance, and editing instructions out of
area descriptions. Original descriptions and categories are
preserved in `source_description` and `source_category`; original KML style values
remain in `kml_style`. Preserve these historical fields on future edits.

Both geojson.io simplestyle and uMap `_umap_options` colours were updated together.
Opacity and line width remain consistent. The map now contains 36 area polygons
and one reference line; original IDs are retained, with 13 additional IDs. See the
redraw record for changed coordinates and split-feature provenance. The Highway 1 reference note now explicitly acknowledges
the named northern exceptions rather than presenting the line as an absolute rule.

After merge, reload the uMap remote layer and verify its colours and popups. If the
popup uses a custom template, include `{name}` and `{description}`. The existing
remote URL stays the same. These edits do not create separate toggleable layers;
they preserve the original single-layer structure.
