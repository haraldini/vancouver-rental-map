# Vancouver rental map

A shared map with versioned GeoJSON on GitHub, human editing in **geojson.io**, and display through **uMap remote layers**. Humans and AI agents edit the same files through reviewed pull requests.

**Status: original KML imported.** The layer contains 23 area polygons and one Highway 1 boundary line from the supplied export. Geometry and original source notes are preserved. Current search priorities and display colours follow the [owner-approved priority update](docs/search-priorities.md). See the [import record and feature inventory](docs/import-record.md) for provenance and source caveats. The descriptions are source assertions, not independently verified rental or transit facts.

## Start here

1. Review the [current priorities and colour legend](docs/search-priorities.md), with source provenance in the [import record](docs/import-record.md).
2. [Edit the zones in geojson.io](https://geojson.io/#id=github:haraldini/vancouver-rental-map/blob/main/data/zones.geojson&map=12/49.274314/-123.021465). Follow [the editing guide](CONTRIBUTING.md) to save changes back to GitHub.
3. Configure [uMap remote layers](docs/umap.md) once, then reload uMap after updates reach `main`.

The editor link and production URL show `main`. Changes in a pull request appear there only after merge. To preview a proposed update, download `data/zones.geojson` from its branch and use Open → File in geojson.io.

## Layers and publishing

| Layer | Canonical file | Purpose |
| --- | --- | --- |
| Zones | [data/zones.geojson](data/zones.geojson) | 23 supplied search areas + Highway 1 boundary (one source layer) |

Production remote URL:

```text
https://raw.githubusercontent.com/haraldini/vancouver-rental-map/main/data/zones.geojson
```

GitHub serves the committed file directly. **No Pages site, build, API key, or deployment account is required.** Merging a pull request to `main` publishes the data at the stable URL. Raw-file and browser caching may delay visibility; reload and verify the raw contents before troubleshooting uMap. This is not live collaboration: geojson.io does not synchronize changes back automatically.

Add one `.geojson` file per actual source layer under `data/`, then add its raw URL to uMap and this table. Do not split or merge original layers without recording the mapping. uMap layer order and layer defaults live in uMap; GitHub owns geometry, feature properties, and imported per-feature styles. The import provides simplestyle properties for geojson.io and `_umap_options` for uMap. Keep these style values synchronized when editing colours.

## Checks

Python 3.11+ with no extra dependencies:

```sh
python3 scripts/validate_geojson.py
python3 -m unittest discover -s tests -v
```

GitHub Actions runs these checks on pushes and pull requests. In repository Settings → Rules → Rulesets, optionally require the `validate` check and a pull request for `main`. The workflow alone does not prevent direct pushes or enforce a merge gate.

See [data conventions](docs/data-format.md), [human editing](CONTRIBUTING.md), and [AI editing rules](AGENTS.md).

## Ownership and privacy

This repository is public. Publish only information intended for public viewing; keep private rental notes, contact details, credentials, and uMap secret editing links out of commits. Source data rights and attribution must be established during import. No data license is assumed by this scaffold.
