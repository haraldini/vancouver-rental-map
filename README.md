# Vancouver rental map

A shared map with versioned GeoJSON on GitHub, human editing in **geojson.io**, and display through **uMap remote layers**. Humans and AI agents edit the same files through reviewed pull requests.

**Status: 39 search pockets plus a Highway 1 reference line.** The original map has been refined into smaller pockets, with additional pockets in Vancouver, Coquitlam, north Burnaby, and western Port Moody. See the [inlet-side additions](docs/inlet-pockets.md). See the [priority legend](docs/search-priorities.md) and [redraw references](docs/redraw-2026-10-21.md). Boundaries are approximate search guides; assess each actual address. Descriptions contain practical pros and cons, with a short caveat only where useful.

## Start here

1. Review the [current priorities and colour legend](docs/search-priorities.md), with source provenance in the [import record](docs/import-record.md).
2. [Edit the zones in geojson.io](https://geojson.io/#id=github:haraldini/vancouver-rental-map/blob/main/data/zones.geojson&map=12/49.274314/-123.021465). Follow [the editing guide](CONTRIBUTING.md) to save changes back to GitHub.
3. Configure [uMap remote layers](docs/umap.md) once, then reload uMap after updates reach `main`.

The editor link and production URL show `main`. Changes in a pull request appear there only after merge. To preview a proposed update, download `data/zones.geojson` from its branch and use Open → File in geojson.io.

## Layers and publishing

| Layer | Canonical file | Purpose |
| --- | --- | --- |
| Zones | [data/zones.geojson](data/zones.geojson) | 39 search pockets + Highway 1 reference |
| r/askvan recommendations | [data/askvan-recommendations.geojson](data/askvan-recommendations.geojson) | 12 independently toggleable recommendations; [sources and setup](docs/askvan-recommendations.md) |
| Inlet-side pockets | [data/inlet-pockets.geojson](data/inlet-pockets.geojson) | Three selected inlet-side pockets, separately toggleable; [details](docs/inlet-pockets.md) |

Production remote URLs (configure one uMap layer for each):

```text
https://raw.githubusercontent.com/haraldini/vancouver-rental-map/main/data/zones.geojson
https://raw.githubusercontent.com/haraldini/vancouver-rental-map/main/data/askvan-recommendations.geojson
https://raw.githubusercontent.com/haraldini/vancouver-rental-map/main/data/inlet-pockets.geojson
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
