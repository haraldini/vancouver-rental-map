# Selected inlet-side residential pockets

Added 2026-10-23 at the owner's request. Three focused additions to the main Zones
layer: Burnaby Heights/Confederation Park edge, Capitol Hill/Cambridge ridge, and
College Park/Easthill. The two named Burnaby pockets are exceptions to the earlier
Burnaby exclusion; this does not approve the whole municipality or waterfront.
The College Park pocket extends the considered part of western Port Moody beyond
the original Rocky Point corridor. The r/askvan overlay is unchanged.

The main layer now contains 39 area polygons and the Highway 1 line. All 37 previous
features, their IDs, geometry, notes, and metadata are unchanged. The three new IDs
are `area-heights-confederation`, `area-capitol-cambridge`, and
`area-college-park-easthill`. Source and status metadata stay outside descriptions,
which contain only brief Good/Bad notes.

## Selection and boundary method

- Heights: a compact residential pocket between Carleton and Willingdon, Hastings
  and Oxford, immediately west of Confederation Park. Prioritizes access to shops
  and the park, rather than treating all north Burnaby as waterfront housing.
- Capitol: selected ridge streets between Hythe North and Grosvenor North,
  Cambridge and Dundas. This is an approximate Cambridge ridge pocket; a north-facing
  home and a useful view must be confirmed from the listing and in person.
- College Park/Easthill: a compact residential hill pocket anchored around
  Oxford/Princeton/College Park and Cecile. This is not the entire College Park or
  Harbour Heights district; waterfront and station access are address-dependent.

Westridge's terminal-side waterfront and isolated Barnet stretches were not added.
Harbour Heights/Shoreline Circle was considered, but the selected Port Moody
addition focuses on College Park/Easthill rather than drawing a broad hillside
band. No rent availability, acceptable building condition, or walking time is
implied by these outlines.

All 12 corners use exact-match BC Address Geocoder INTERSECTION results with score
100 and the intended municipality. Wrong-locality and street-only matches were
rejected; Cambridge ridge corners do not use the nonexistent Hythe/McGill or
Grosvenor/McGill intersections. Straight connecting edges are approximate search
boundaries, not official neighbourhood lines, road curves, or measured catchments.
[Accepted coordinates and provenance](inlet-pocket-anchors.json).

Context: [Confederation Park](https://www.burnaby.ca/explore-outdoors/parks/confederation-park),
[Burnaby trails](https://www.burnaby.ca/explore-outdoors/walking-hiking-and-biking/trans-canada-trail),
[Burnaby community plans](https://www.burnaby.ca/our-city/strategies-and-plans/official-community-plan/community-plans),
[Port Moody neighbourhood context](https://engage.portmoody.ca/portmoody-2050).
Geometry: [BC Address Geocoder](https://geocoder.api.gov.bc.ca/), Province of British
Columbia, [Open Government Licence - BC](https://www2.gov.bc.ca/gov/content/data/open-data/open-government-licence-bc).

The main remote source stays `https://raw.githubusercontent.com/haraldini/vancouver-rental-map/main/data/zones.geojson`.
Merge the addition and reload the connected uMap layer to load all 40 features.

## Separate viewing layer

`data/inlet-pockets.geojson` mirrors these three main-map additions for independent toggling in uMap. Its unique `inlet-` IDs refer to canonical main-zone IDs via `related_zone_id`. Keep mirrored geometry, notes, and styling synchronized when editing these three pockets. Overlap with a connected full Zones layer is intentional; hide one layer if needed.

Remote source: `https://raw.githubusercontent.com/haraldini/vancouver-rental-map/main/data/inlet-pockets.geojson` (GeoJSON, Dynamic off).

The **Inlet-side pockets** layer was saved in uMap on 2026-10-23 and its permanent main URL was verified in the downloaded map export. Three polygons were visually previewed from the proposal branch. The production URL becomes available on merge; until then it may show a remote-data warning. The existing original and r/askvan layers were retained with unchanged feature data and remote source settings. The original static layer could not be opened for source editing, so this change connects only the new inlet layer.
