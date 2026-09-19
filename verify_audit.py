#!/usr/bin/env python3
"""Atom-by-atom verification of repository-audit fixes."""
import re, json, html, sys

fails = []
def check(name, cond, detail=""):
    print(("PASS " if cond else "FAIL ") + name + ((" — " + detail) if detail and not cond else ""))
    if not cond:
        fails.append(name)

# 1. FAQ sync: custom page (json-formatter) + generic page (churn) + bmi
for slug in ["json-formatter", "churn-rate-calculator", "loan-emi-calculator", "bmi-calculator"]:
    p = open(slug + "/index.html", encoding="utf-8").read()
    vis = re.findall(r'<summary class="faq-q">(.*?)</summary>', p)
    m = re.search(r'"@type":"FAQPage","mainEntity":(\[.*?\])\}</script>', p, re.S)
    ld = [q["name"] for q in json.loads(m.group(1))] if m else []
    check("faq-sync:" + slug, [html.unescape(v) for v in vis] == ld and len(vis) == 4,
          "vis=%d ld=%d" % (len(vis), len(ld)))

# 2. og:image points at PNG, not page URL
for slug in ["index", "json-formatter", "age-calculator"]:
    path = "index.html" if slug == "index" else slug + "/index.html"
    p = open(path, encoding="utf-8").read()
    m = re.search(r'og:image"\s+content="([^"]+)"', p)
    check("og-image:" + slug, bool(m) and m.group(1).endswith("/assets/images/og-default.png"),
          m.group(1) if m else "missing")

# 3. Age: ToolKit returns object; page renders years+months+days
tk = open("assets/js/tools.js", encoding="utf-8").read()
check("tk-age-object", "totalDays" in tk and "months" in tk.split("TK.age")[1][:600])
agep = open("age-calculator/index.html", encoding="utf-8").read()
check("age-page-ymd", "months" in agep and "days total" in agep)

# 4. Previously-fallback slugs now wired
wires = {"churn-rate-calculator": "TK3.churn", "growth-rate-calculator": "TK3.growthRate",
         "discount-calculator": "TK3.discount", "tip-calculator": "TK3.tip",
         "character-counter": "wordCount", "roi-calculator": "TK3.roi",
         "gpa-calculator": "TK3.gpa", "markdown-table-generator": "markdownTable",
          "hex-to-rgb": "hexToRgb", "image-compressor": "compressImage",
          "css-gradient-generator": "buildGradient", "unit-conversion-calculator": "convertLength",
          "bmi-calculator": "ToolKit.bmi"}
# TK3 alias must be defined in every page
for _slug in ["churn-rate-calculator", "word-counter", "image-resizer"]:
    _p = open(_slug + "/index.html", encoding="utf-8").read()
    check("tk3-alias:" + _slug, "TK3=window.ToolKit" in _p or "TK3 = window.ToolKit" in _p)
for slug, token in wires.items():
    p = open(slug + "/index.html", encoding="utf-8").read()
    check("wired:" + slug, token in p, "missing " + token)

# 5. Scope notes
check("note:yaml", "Anchors" in open("yaml-formatter/index.html", encoding="utf-8").read())
check("note:js-min", "Basic" in open("javascript-minifier/index.html", encoding="utf-8").read())

# 6. Image UI fields
check("image-ui-whq", 'id="tool-w"' in open("image-resizer/index.html", encoding="utf-8").read())

# 7. common.js delegates to ToolKit
check("copy-dedupe", "ToolKit.copyText" in open("assets/js/common.js", encoding="utf-8").read())

# 8. No "No tracking" anywhere
import subprocess
tracked = []
for f in ["index.html", "about/index.html"]:
    if "No tracking" in open(f, encoding="utf-8").read():
        tracked.append(f)
gen = open("generate.py", encoding="utf-8").read()
check("no-tracking-claim", not tracked and "No tracking" not in gen, ",".join(tracked))

# 9. Precise privacy claim on homepage
check("privacy-claim", "No uploads. No account required." in open("index.html", encoding="utf-8").read())

# 10. Sitemap: hub + about + privacy + 10 cats + tools + guides
sm = open("sitemap.xml", encoding="utf-8").read()
n = sm.count("<url>")
import json as _json
_ng = len(_json.load(open("seo/guides.json", encoding="utf-8"))["guides"])
_nt = len(_json.load(open("tools.json", encoding="utf-8-sig"))["tools"])
check("sitemap-count", n == 3 + 10 + _nt + _ng, "found %d want %d" % (n, 3 + 10 + _nt + _ng))
check("sitemap-cats", all(s in sm for s in ["developer-tools", "finance-calculators", "image-tools"]))
check("sitemap-bmi", "bmi-calculator" in sm)
check("sitemap-guides", "/guides/" in sm)

# 11. Category pages: 10 exist with unique titles
import os
cats = ["developer-tools", "css-html-tools", "text-tools", "math-calculators", "student-tools",
        "date-time", "finance-calculators", "business-calculators", "color-tools", "image-tools"]
titles = set()
ok = True
for c in cats:
    pth = os.path.join(c, "index.html")
    if not os.path.exists(pth):
        ok = False
        break
    titles.add(re.search(r"<title>(.*?)</title>", open(pth, encoding="utf-8").read()).group(1))
check("category-pages", ok and len(titles) == 10, "titles=%d" % len(titles))

# 12. Finance disclaimer + formula render
emip = open("loan-emi-calculator/index.html", encoding="utf-8").read()
check("finance-disclaimer", "does not constitute financial advice" in emip)
check("finance-formula", "EMI = P" in emip)

# 14. Guide pages: canonical + FAQPage + Article schema + target-tool link
import json as _json2
_guides = _json2.load(open("seo/guides.json", encoding="utf-8"))["guides"]
_gok = True
for _g in _guides:
    _p = open(os.path.join("guides", _g["slug"], "index.html"), encoding="utf-8").read()
    if ('/guides/' + _g["slug"] + '/' not in _p or '"@type":"FAQPage"' not in _p
            or '"@type":"Article"' not in _p or _g["target_tool"] not in _p):
        _gok = False
        break
check("guide-pages", _gok and len(_guides) <= 12, "guides=%d" % len(_guides))

# 13. Dump actual handler bodies for the failing slugs (diagnostic)
pages = {"churn-rate-calculator": "churn-rate-calculator",
         "growth-rate-calculator": "growth-rate-calculator",
         "discount-calculator": "discount-calculator",
         "tip-calculator": "tip-calculator",
         "roi-calculator": "roi-calculator",
         "gpa-calculator": "gpa-calculator"}
for slug, page in pages.items():
    p = open(page + "/index.html", encoding="utf-8").read()
    i = p.find('slug==="' + slug + '"')
    print("--- " + slug + ": " + (p[i:i + 320].replace("\n", " ") if i != -1 else "HANDLER NOT FOUND"))

print()
if fails:
    print("FAILURES:", fails)
    sys.exit(1)
print("ALL CHECKS PASSED")
