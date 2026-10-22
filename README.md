# Vancouver rental map

A shared map with versioned GeoJSON on GitHub, human editing in **geojson.io**, and display through **uMap remote layers**. Humans and AI agents edit the same files through reviewed pull requests.

**Status: awaiting the original KMZ or uMap export.** The zones file is intentionally empty. No boundaries, neighbourhood rankings, or rental listings have been invented. An empty map is expected until real data is imported.

## Start here

1. Supply the original export and follow [Importing existing data](docs/importing.md).
2. [Edit the zones in geojson.io](https://geojson.io/#id=github:haraldini/vancouver-rental-map/blob/main/data/zones.geojson&map=12/49.274314/-123.021465). Follow [the editing guide](CONTRIBUTING.md) to save changes back to GitHub.
3. Configure [uMap remote layers](docs/umap.md) once, then reload uMap after updates reach `main`.

The editor link and production URL require this scaffold to be merged into `main` first. Before merge, open the file from the pull request's branch or download it and use Open → File in geojson.io.

## Layers and publishing

| Layer | Canonical file | Purpose |
| --- | --- | --- |
| Zones | [data/zones.geojson](data/zones.geojson) | Empty container for the user's supplied search areas |

Production remote URL:

```text
https://raw.githubusercontent.com/haraldini/vancouver-rental-map/main/data/zones.geojson
```

GitHub serves the committed file directly. **No Pages site, build, API key, or deployment account is required.** Merging a pull request to `main` publishes the data at the stable URL. Raw-file and browser caching may delay visibility; reload and verify the raw contents before troubleshooting uMap. This is not live collaboration: geojson.io does not synchronize changes back automatically.

Add one `.geojson` file per actual source layer under `data/`, then add its raw URL to uMap and this table. Do not split or merge original layers without recording the mapping. uMap appearance and layer order live in uMap; GitHub owns geometry and feature properties.

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
