# Connect uMap to GitHub

Do this after the relevant map-update pull request is merged to `main`. No uMap settings have been changed by this repository setup.

1. Open your map with your own edit access. Download a complete uMap backup before changing its layers. Keep any secret editing URL private.
2. Create a **new layer** named `Zones (GitHub)` rather than replacing an existing layer. Open its properties and expand **Remote data**.
3. Enter the URL below, select **geojson** as the format, and use **Verify URL** if available:

   ```text
   https://raw.githubusercontent.com/haraldini/vancouver-rental-map/main/data/zones.geojson
   ```

4. Leave **Dynamic** off for this static file. It fetches the full layer when loading the map. Dynamic mode refetches on map movement; it is not a timer or a GitHub synchronization mechanism. Leave proxy off initially; if the host blocks cross-origin access, try the proxy and account for its cache.
5. Set layer styling and popup content (for example `{name}` and `{description}` where present), then save the map. Check it in a fresh viewer tab.
6. Expect 36 area polygons and one Highway 1 line after the redraw reaches `main`. Compare names, counts, boundaries, and styling against the original map. Per-feature `_umap_options` carry the current priority colours; confirm these render as intended on your uMap instance. Keep original layers until that comparison is complete; hide duplicates only when satisfied.

Repeat for each actual layer file, using `https://raw.githubusercontent.com/haraldini/vancouver-rental-map/main/data/<filename>.geojson`.

Remote features are maintained in GitHub, not by editing their shapes inside uMap. Configure the remote URL instead of importing a snapshot through uMap's general Import menu, which would create a separate stored copy.

## Verify publishing

Open the raw URL: it must return a FeatureCollection, not GitHub's HTML file page or a sign-in screen. After a reviewed change reaches `main`, verify that file's contents, then reload uMap. Allow for caching. If data fails to load, check the URL, format, validation result, and proxy setting before changing geometry.

For a temporary preview, substitute the pull request's branch name for `main` in a separate test layer. Restore `main` before treating it as production. For an immutable snapshot, substitute a commit SHA.

Reference: [uMap remote-data tutorial](https://discover.umap-project.org/fr/tutorials/10-embed-remote-data/) (the English translation is currently incomplete).
