# Editing the map

## Human workflow

1. Start from the latest GitHub version of the layer. Use the README's geojson.io link, or download the raw `.geojson` and choose **Open → File** in geojson.io.
2. Edit the intended shapes and their properties. Preserve existing names, IDs, metadata, holes, and unrelated features. Use the JSON panel to check properties that are not visible in the table.
3. Choose **Save → GeoJSON** to download the full layer. Saving locally does not publish anything to GitHub.
4. In GitHub, create a branch from the latest `main`. Upload the edited file into `data/` using the **same filename**. Ensure it replaces that layer, not adds a second file such as `map.geojson`.
5. Open a pull request describing changed feature IDs, the reason, and the source of boundary changes. Compare the diff and feature count. If someone changed the layer while you were editing, reopen their latest version and reapply your edits; do not overwrite their work with your stale download.
6. Wait for `validate`, review the shapes visually, then have the owner merge. Reload uMap and verify the published raw file. Changes in an open editor tab are not proof that GitHub was updated.

Do not depend on direct GitHub saving from geojson.io: downloading and uploading works without granting the editor GitHub write access.

## AI / local workflow

Create a branch, edit the minimum required features, run both commands in the README, and open a pull request. Report added/changed/deleted feature IDs and any conversion loss. Preserve unknown properties. Geometry changes need a supplied source or explicit drawing instructions, not guesses from a neighbourhood name.

## New features and layers

Follow [data-format.md](docs/data-format.md). For a new feature, set a unique `properties.id`, a nonempty `properties.name`, and a nonempty `properties.source`. Keep its ID stable across edits. Add a new layer only when it represents actual requested or imported data, and document its uMap remote URL.

## Undo

Use a new pull request reverting the bad commit (or restoring only the affected features). Do not rewrite published history. Review and merge the correction, then reload uMap after the raw file updates.
