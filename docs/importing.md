# Import the original map without losing information

**First import completed:** see [the import record](import-record.md) for the supplied KML, checksum, counts, and preserved metadata. Use the checklist below for future imports. Do not reconstruct zones from memory, a screenshot, or guessed neighbourhood boundaries.

1. Keep an untouched source backup outside the public repository. Record its filename, checksum, export date if known, and origin. Review it for private notes and secret edit links before publishing any part of it.
2. Inventory every source layer/folder, feature count, geometry type, name, description, ID, and style. Record that inventory and the source-to-file mapping in the import pull request.
3. For a uMap export, extract each layer's FeatureCollection and retain feature properties and geometry. Keep map-level settings in the private backup; record any public-safe styling needed for reconstruction. Remote layers may reference external data rather than include it: inventory them separately and obtain the actual source.
4. A KMZ is an archive: inspect its KML, linked files, and assets before conversion. Convert each actual layer using a suitable GIS tool, then compare the result. KML folders, ExtendedData, styles, icons, altitude, overlays, and network links may need separate handling. Stop and report unsupported items rather than dropping them.
5. Assign stable `properties.id` values and public-safe `properties.source` provenance. Preserve original IDs and metadata. Use source names; ask the owner about missing names. Reuse `data/zones.geojson` only if it matches the source layer; otherwise add files matching the real layers and update the README.
6. Run validation, compare counts by layer, and visually inspect every zone including holes and multi-part polygons. Record conversion losses and unresolved differences explicitly. Do not simplify boundaries unless requested.
7. Open an import pull request. After owner review and merge, connect new uMap remote layers alongside the originals and compare them. The original map remains the reference until verified.

The original KML has been converted. Importing new exports must reconcile existing feature IDs and edits rather than replacing the layer blindly.
