# Data conventions

Each `data/*.geojson` is an RFC 7946 FeatureCollection, with `features: []` permitted. Coordinates use WGS84 longitude, latitude (optional elevation), in that order. Do not include a legacy `crs` member or use projected metre coordinates.

Each feature must have:

| Property | Meaning |
| --- | --- |
| `properties.id` | Nonempty string, unique across all layer files and stable over time |
| `properties.name` | Human-readable name from the source or supplied by the owner |
| `properties.source` | Public-safe provenance, for example the original filename and placemark ID |

A top-level GeoJSON `id` may also exist; preserve it. The repository's stable editing key is `properties.id`. During import, preserve any original ID; if it cannot serve as the stable key, retain it in another explicitly documented property. Do not silently overwrite conflicting fields.

Point, MultiPoint, LineString, MultiLineString, Polygon, MultiPolygon, and GeometryCollection are supported by the validator. Polygon rings need at least four positions, the first and last identical, and three distinct vertices. Holes are subsequent rings. Preserve geometry precision; use RFC 7946 winding on new polygons (outer counterclockwise, holes clockwise).

Preserve all additional properties, including source styling. geojson.io simplestyle properties and uMap styling are not guaranteed to translate one-to-one. Test the imported styles in uMap and document any mapping; layer-level styles can be set in uMap independently.

Validation checks required properties, unique IDs, numeric coordinate bounds, geometry nesting, and ring closure. It does not check self-intersections, winding, overlapping zones, polygon containment, real-world correctness, or whether a source claim is true. Visual comparison against the original export is required.

Reference: [RFC 7946](https://www.rfc-editor.org/rfc/rfc7946).
