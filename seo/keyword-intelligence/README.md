# Keyword intelligence — refresh workflow + decision system

## Refresh (every 2-4 weeks or after any implementation)
1. GSC Performance -> set 3 months -> EXPORT (Queries + Pages tabs) -> save as `gsc-export-YYYY-MM-DD.csv` in this folder.
2. Append new rows to `gsc-keywords.csv` / `gsc-pages.csv` with the export date_range.
3. Re-run opportunity detection:
   - NEW queries with impressions -> add to `keyword-map.csv` (map to closest existing URL; never create a page first).
   - Position 4-20 + impressions rising -> Category B.
   - Impressions up + CTR < 2% -> Category C (snippet rewrite).
   - Same query hitting 2+ URLs -> check cannibalization section below.
4. Update `seo-opportunities.md` priorities; move MONITOR items up only on new evidence.

## Decision system ("what should I improve next?")
Sort open opportunities by:
1. Has GSC impressions? (yes beats no evidence)
2. Position 4-20? (closest to clicks wins)
3. CTR below expectation for position? (snippet fix is cheapest)
4. Effort (title/desc/FAQ/link < new guide < new tool)
5. Cluster value (does it lift sibling pages?)

Output format: `PRIORITY -> "query" -> /url -> evidence -> problem -> action`.

## Cannibalization check (current status: NONE)
- 690 keywords across 230 tools: zero duplicates (verified 2026-09-18).
- Re-check after each tools.json edit: every keyword must map to exactly one slug.

## Data vintage
- GSC: 2026-06-18 to 2026-09-18 (site lifetime; property created ~Sep 13).
- SERP observations: 2026-09-18, desktop, India locale.
- Next refresh due: after sitemap status flips + indexed count passes 50.
