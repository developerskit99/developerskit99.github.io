#!/usr/bin/env python3
"""Production crawl of all sitemap URLs: status, SEO tags, dupes, broken links."""
import re, sys, html as htmllib
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from collections import Counter

BASE = "https://developerskit99.github.io"
UA = {"User-Agent": "DevelopersKit-audit-crawl/1.0"}

def fetch(url, timeout=25):
    req = Request(url, headers=UA)
    try:
        with urlopen(req, timeout=timeout) as r:
            return r.status, r.read().decode("utf-8", "replace"), str(r.url)
    except HTTPError as e:
        try:
            body = e.read().decode("utf-8", "replace")
        except Exception:
            body = ""
        return e.code, body, url
    except Exception as e:
        return -1, "", url + " :: " + str(e)

def tag(pat, page):
    m = re.search(pat, page, re.S | re.I)
    return htmllib.unescape(m.group(1).strip()) if m else ""

sm = fetch(BASE + "/sitemap.xml")[1]
urls = re.findall(r"<loc>(.*?)</loc>", sm)
print("sitemap urls:", len(urls))

rows = []
for u in urls:
    st, page, final = fetch(u)
    rows.append((u, st, final, page))

bad_status = [(u, s) for u, s, f, p in rows if s != 200]
print("non-200:", bad_status if bad_status else "none")

titles, descs, h1s, canons = {}, {}, {}, {}
issues = []
for u, st, final, p in rows:
    if st != 200 or not p:
        continue
    t = tag(r"<title>(.*?)</title>", p)
    d = tag(r'<meta name="description" content="([^"]*)"', p)
    h1 = tag(r"<h1>(.*?)</h1>", p)
    c = tag(r'<link rel="canonical" href="([^"]*)"', p)
    og = tag(r'og:image"\s+content="([^"]*)"', p)
    has_faq = '"@type":"FAQPage"' in p or '"@type": "FAQPage"' in p
    has_app = "SoftwareApplication" in p
    has_crumb = "BreadcrumbList" in p
    titles.setdefault(t, []).append(u)
    descs.setdefault(d, []).append(u)
    h1s.setdefault(h1, []).append(u)
    if not t:
        issues.append((u, "missing title"))
    if not d:
        issues.append((u, "missing meta description"))
    if len(d) < 50 or len(d) > 200:
        issues.append((u, "meta description length %d" % len(d)))
    if len(t) > 70:
        issues.append((u, "title too long (%d)" % len(t)))
    if not h1:
        issues.append((u, "missing h1"))
    if not c:
        issues.append((u, "missing canonical"))
    elif c.rstrip("/") != u.rstrip("/"):
        issues.append((u, "canonical mismatch: " + c))
    if og.endswith(".github.io/") or ("/" in og and "." not in og.rsplit("/", 1)[-1]):
        issues.append((u, "og:image is page URL: " + og))
    if "/about/" not in u and u != BASE + "/" and not u.rstrip("/").split("/")[-1].startswith(("developer", "css", "text", "math", "student", "date", "finance", "business", "color", "image")):
        pass
    if u not in (BASE + "/",) and "/about/" not in u and not any(
            k in u for k in ["developer-tools", "css-html", "text-tools", "math-", "student-",
                             "date-time", "finance-", "business-", "color-", "image-"]):
        if not (has_faq and has_app and has_crumb):
            issues.append((u, "tool page missing schema (faq=%s app=%s crumb=%s)" % (has_faq, has_app, has_crumb)))

print("duplicate titles:", {k: len(v) for k, v in titles.items() if len(v) > 1} or "none")
print("duplicate descriptions:", len([k for k, v in descs.items() if len(v) > 1]),
      {k[:60]: len(v) for k, v in descs.items() if len(v) > 1} or "")
print("duplicate h1s:", {k: len(v) for k, v in h1s.items() if len(v) > 1} or "none")
print("empty h1 pages:", len(h1s.get("", [])))

# internal link check: collect all site-internal hrefs from a sample + homepage hub links
print("--- internal link integrity ---")
link_re = re.compile(r'href="(/[^"]*?/)"')
known = set(u.replace(BASE, "") or "/" for u in urls)
known.add("/")
broken = Counter()
checked_pages = 0
for u, st, final, p in rows:
    if st != 200 or not p:
        continue
    checked_pages += 1
    for href in set(link_re.findall(p)):
        href = href.split("#")[0].split("?")[0] or "/"
        if href.startswith("/assets/"):
            continue
        if href not in known:
            broken[href] += 1
print("pages checked:", checked_pages)
print("broken internal links:", dict(broken) if broken else "none")

print("--- other issues (%d) ---" % len(issues))
for u, msg in issues[:60]:
    print(" ", msg, "::", u)
if len(issues) > 60:
    print(" ... and %d more" % (len(issues) - 60))
