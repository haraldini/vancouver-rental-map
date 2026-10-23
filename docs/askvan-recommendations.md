# r/askvan recommendation layer

Reviewed 2026-10-23 against the owner's rental preferences. This is an editorial
shortlist from selected public discussions, not a representative survey, a vote
ranking, or a statement that qualifying rentals are currently available.

`data/askvan-recommendations.geojson` contains 12 areas in a separate pink layer:
eight existing mapped pockets and four additional south-Vancouver pockets
(Champlain Heights, Fraserview riverfront, River District, and Marpole). Existing
outlines are reused under new globally unique IDs, with `related_zone_id` pointing
to the original. The original search geometry and approval/status fields are unchanged.
Turning both layers on intentionally shows overlapping geometry.

Descriptions contain only short Good/Bad notes. Thread URLs, fit rationale, review
date, and geometry provenance are separate metadata fields. The assessment combines
resident comments with the owner's preferences; it is not a quotation or consensus.

## Selection

Nature, water access, everyday amenities, useful transport, and house-form housing
were emphasized. School quality, family demographics, purchase prices, and mortgage
budgets were not treated as evidence of rental fit. No ethnicity or demographic
preferences were used. Claims about future SkyTrain openings, exact commute times,
crime/safety, and rental availability were not carried into the map.

Burnaby, West Vancouver, Richmond, New Westminster, and Port Coquitlam recommendations
were left out because they fall outside the current geographic scope. Coquitlam's
Burquitlam pocket is included; no new municipality-wide approval was inferred.
Burke Mountain was considered but not selected because its driving dependence is a
weaker fit. Fairview received mixed comments; it remains in the main map rather
than being presented here as a strong Reddit endorsement.

## Selected pockets and evidence

- **Lower Lonsdale**: Comments recommend the Quay/SeaBus lifestyle. Strong fit for water access and walkability; housing form still needs screening. [discussion](https://www.reddit.com/r/askvan/comments/1ufd274/which_vancouver_neighbourhood_fits_my_lifestyle/), [discussion](https://www.reddit.com/r/askvan/comments/1xc17df/opinions_on_these_neighborhoods/)
- **Kits beach-side / Kits Point**: Repeated beach/walkability recommendations; no inference that a qualifying large rental is available. [discussion](https://www.reddit.com/r/askvan/comments/1ufd274/which_vancouver_neighbourhood_fits_my_lifestyle/), [discussion](https://www.reddit.com/r/askvan/comments/1fqhf2c/opinions_on_mount_pleasant_fairview_west_end/)
- **Mount Pleasant / Main village**: Resident recommendations around Main and nearby parks fit everyday walkability; no water-view advantage assumed. [discussion](https://www.reddit.com/r/askvan/comments/1fqhf2c/opinions_on_mount_pleasant_fairview_west_end/), [discussion](https://www.reddit.com/r/askvan/comments/1xc17df/opinions_on_these_neighborhoods/)
- **Commercial Drive village**: Commercial/Grandview receives direct recommendations; suits village amenities and house-form preference. [discussion](https://www.reddit.com/r/askvan/comments/1fqhf2c/opinions_on_mount_pleasant_fairview_west_end/), [discussion](https://www.reddit.com/r/askvan/comments/1vfojhq/neighbourhood_recommendation_for_young_couple/)
- **Hastings-Sunrise village**: Resident posts praise amenities and community while describing transit and grocery trade-offs. Park access is address-specific. [discussion](https://www.reddit.com/r/askvan/comments/1qf138t/need_help_convincing_my_partner_of_housing/), [discussion](https://www.reddit.com/r/askvan/comments/1vfojhq/neighbourhood_recommendation_for_young_couple/)
- **Olympic Village**: Recommended for centrality and walkability. Included as a weaker housing-form fit, not as proof of qualifying supply. [discussion](https://www.reddit.com/r/askvan/comments/1xc17df/opinions_on_these_neighborhoods/)
- **Moody Centre / Rocky Point**: Port Moody is recommended for nature and community; this existing park/station pocket is the editorial geographic selection. [discussion](https://www.reddit.com/r/askvan/comments/1q5qxo5/priced_out_of_city_of_vancouver_best_place_to/)
- **Burquitlam station pocket**: Burquitlam is directly recommended for transit and access to green space; source anecdotes do not establish commute times or rental prices. [discussion](https://www.reddit.com/r/askvan/comments/1q5qxo5/priced_out_of_city_of_vancouver_best_place_to/), [discussion](https://www.reddit.com/r/askvan/comments/1nqawrp/buying_a_townhouse_in_lower_mainland/)
- **Champlain Heights / Everett Crowley**: A resident recommends its parks and townhouse/low-rise form; other comments describe spacious older homes. Purchasing/leasehold claims were not translated into rental savings. [discussion](https://www.reddit.com/r/askvan/comments/1vfojhq/neighbourhood_recommendation_for_young_couple/), [discussion](https://www.reddit.com/r/askvan/comments/1nqawrp/buying_a_townhouse_in_lower_mainland/)
- **Fraserview riverfront west of Kerr**: Residents mention river walks and larger older townhomes west of Kerr; recent discussion adds social/commute inconvenience. Exact unit condition and rent remain unverified. [discussion](https://www.reddit.com/r/askvan/comments/1nqawrp/buying_a_townhouse_in_lower_mainland/), [discussion](https://www.reddit.com/r/askvan/comments/1q5qxo5/priced_out_of_city_of_vancouver_best_place_to/), [discussion](https://www.reddit.com/r/askvan/comments/1xc17df/opinions_on_these_neighborhoods/)
- **River District / East Fraser Lands**: Residents recommend river walks and townhomes but distinguish newer smaller units from the older stock west of Kerr. Official city context confirms Kerr-to-Boundary location. [discussion](https://www.reddit.com/r/askvan/comments/1nqawrp/buying_a_townhouse_in_lower_mainland/), [discussion](https://www.reddit.com/r/askvan/comments/1q5qxo5/priced_out_of_city_of_vancouver_best_place_to/)
- **Marpole village residential pocket**: Suggested for duplexes/townhouses and usable space. This is a weaker, single-thread lead; no purchase-price claims or generic affordability promise carried into rental notes. [discussion](https://www.reddit.com/r/askvan/comments/1nqawrp/buying_a_townhouse_in_lower_mainland/)

## Geometry

The eight existing outlines are byte-equivalent to their current main-layer
geometries. Four new outlines use 14 exact-match BC Address Geocoder intersections.
Only score-100 INTERSECTION results in Vancouver were accepted. Street-only or
wrong-locality matches were rejected. Where a road intersection was unavailable,
the method explicitly records a projected coordinate from accepted longitude and
latitude anchors. These are approximate search envelopes, not measured walks,
shoreline traces, official neighbourhood boundaries, or individual rental parcels.

- Champlain: Kerr to Boundary, roughly E 54th latitude to SE Marine Drive; includes
  Everett Crowley Park and surrounding residential pockets as context.
- Fraserview riverfront: Victoria to Kerr, SE Marine to East Kent Avenue South.
- River District: Kerr to Boundary, SE Marine to East Kent Avenue South.
- Marpole: Granville to Oak, roughly W 63rd latitude to W 70th.

Accepted anchors, thread links, and pocket-level assessments are recorded in
[askvan-research.json](askvan-research.json).

Official context: [East Fraser Lands](https://vancouver.ca/home-property-development/east-fraser-lands-river-district.aspx),
[Champlain Heights Community Centre](https://vancouver.ca/parks-recreation-culture/champlain-heights-community-centre.aspx).
Geometry anchors: [BC Address Geocoder](https://geocoder.api.gov.bc.ca/), Province
of British Columbia, [Open Government Licence - BC](https://www2.gov.bc.ca/gov/content/data/open-data/open-government-licence-bc).

## Connect the separate uMap layer

After merge, create a layer named **r/askvan recommendations** and set Remote data:

- URL: `https://raw.githubusercontent.com/haraldini/vancouver-rental-map/main/data/askvan-recommendations.geojson`
- Format: GeoJSON
- Dynamic: off
- Popup template: `{name}` followed by `{description}`

Keep it independently toggleable from Zones. No need to reimport a snapshot after
future edits. For review before merge, temporarily substitute the proposal branch
for `main`; production must follow `main`.
