# Map editing instructions

- Canonical geographic data lives in `data/*.geojson`. GitHub `main` is the published version; uMap is a remote viewer.
- Never invent zones, coordinates, rental facts, scores, or source attribution. The original KML is now imported; see `docs/import-record.md`. Preserve source caveats and distinguish source recommendations from owner-approved changes.
- Inspect current files and git status first. Preserve uncommitted user work and unrelated features, all existing properties, IDs, geometry precision, polygon holes, and layer boundaries.
- Make changes on a branch and propose a pull request. Do not merge without the owner's instruction.
- Follow `docs/data-format.md`. Record geometry provenance in `properties.source`; preserve original metadata under its original keys.
- Never publish secret uMap edit links or private notes. Source exports stay outside the public repository until reviewed for publication.
- Do not treat geojson.io or a downloaded file as synchronized with GitHub. Reconcile concurrent edits before replacing any layer.
- Run `python3 scripts/validate_geojson.py` and `python3 -m unittest discover -s tests -v`. These are structural checks, not proof of geographic accuracy or valid polygon topology. Inspect geometry visually too.
- Report feature counts and IDs added, changed, or removed. Flag unsupported conversion types and metadata loss; never silently drop data.
- Document new layers and their production raw URLs in README.md. Keep one file per source layer unless the owner approves a different mapping.

- Keep area `description` popups brief: Good and Bad, plus Important only when it adds a concrete caveat. No trial labels, priorities, approval/exception status, search-workflow instructions, history, changelog, provenance, or editing instructions in popup text. Keep search status in its dedicated fields, not the description. Preserve original source notes in their separate metadata fields.

- Current search includes only the three named Coquitlam trial pockets; no blanket Coquitlam approval. Redraws are approximate search outlines. Consult `docs/redraw-2026-10-21.md` and preserve `derived_from` relationships when editing split areas.

- The owner authorized two north Burnaby pockets (Heights/Confederation Park edge and Capitol Hill/Cambridge ridge) plus College Park/Easthill in western Port Moody. See `docs/inlet-pockets.md`. These override the earlier blanket Burnaby exclusion only within those named pockets.
