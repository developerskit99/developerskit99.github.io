#!/usr/bin/env python3
"""SEO intelligence report — reads keyword-intelligence CSVs, prints priorities.

Usage: python seo/report.py
Refresh: drop new GSC exports beside the CSVs; this script picks up
gsc-keywords.csv / gsc-pages.csv / keyword-map.csv automatically.
"""
import csv
import json
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "keyword-intelligence")


def load_csv(name):
    p = os.path.join(ROOT, name)
    if not os.path.exists(p):
        return []
    with open(p, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def fnum(v, default=0.0):
    try:
        s = str(v).strip().replace("%", "")
        return float(s) if s not in ("", "UNKNOWN") else default
    except (ValueError, TypeError):
        return default


def main():
    pages = load_csv("gsc-pages.csv")
    kmap = load_csv("keyword-map.csv")
    try:
        with open(os.path.join(ROOT, "clusters.json"), encoding="utf-8") as f:
            clusters = json.load(f).get("clusters", [])
    except OSError:
        clusters = []

    print("SEO REPORT — DevelopersKit\n")
    print("TOP OPPORTUNITIES")
    ranked = sorted(
        kmap,
        key=lambda r: (fnum(r.get("gsc_impressions")), r.get("priority", "") in ("HIGH", "CRITICAL")),
        reverse=True,
    )
    for i, r in enumerate(ranked[:10], 1):
        print(f"{i}. {r.get('primary_query', '?')}")
        print(f"   Page: {r.get('target_url', '?')}")
        print(f"   Impressions: {r.get('gsc_impressions', '?')}  Clicks: {r.get('gsc_clicks', '?')}  [{r.get('priority', '?')}]")
        print(f"   Action: {r.get('recommended_action', '?')}")
    if not ranked:
        print("   (no keyword-map rows yet)")

    print("\nCLUSTER PERFORMANCE (by GSC impressions)")
    slug_imps = {}
    for p in pages:
        slug_imps[p.get("page", "").rstrip("/").rsplit("/", 1)[-1]] = fnum(p.get("impressions"))
    for c in clusters:
        tot = sum(slug_imps.get(s, 0) for s in c.get("tools", []))
        bar = "#" * min(int(tot), 10)
        print(f"{c.get('name', '?'):22s} {bar} ({tot:g} imp)")

    print("\nCONTENT GAPS (pages with impressions but zero clicks)")
    gaps = [p for p in pages if fnum(p.get("impressions")) > 0 and fnum(p.get("clicks")) == 0]
    for p in gaps[:10]:
        print(f"- {p.get('page')}  ({p.get('impressions')} imp, 0 clicks) -> snippet/FAQ pass")
    if not gaps:
        print("(none)")

    print("\nDONE — refresh GSC CSVs and re-run to update.")


if __name__ == "__main__":
    main()
