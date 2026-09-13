---
name: release-engineer
description: >
  Pages deploy, build checks, broken-link + Lighthouse gates.
  Validates before push: generate.py, sitemap, robots.txt, no broken links.
user-invocable: true
argument-hint: ""
license: MIT
metadata:
  author: DevelopersKit
  version: "1.0"
  category: release
---

# Release Engineer — Deploy Validation

Pre-deploy quality gate for the 230-tool platform.

## Pre-Deploy Checklist

1. **Build**: `python generate.py` completes without errors
2. **Tool count**: all 230 tools generated
3. **Sitemap**: `sitemap.xml` includes all 231 URLs (230 tools + homepage)
4. **Robots.txt**: sitemap URL is correct (`https://developerskit99.github.io/sitemap.xml`)
5. **Verification meta tag**: Google Search Console verification present in all pages
6. **No console errors**: test 3-5 random tool pages for JS errors
7. **Broken links**: all internal links resolve (no 404s)
8. **SEO metadata**: title, description, canonical, JSON-LD present on every page
9. **Internal links**: each tool links to 6-8 related tools
10. **Git status**: only intended files staged, no secrets/keys

## Post-Deploy Verification

1. **Live site**: `https://developerskit99.github.io/` loads correctly
2. **Tool pages**: spot-check 3-5 tools on live site
3. **Sitemap**: fetch `https://developerskit99.github.io/sitemap.xml` — valid XML
4. **Search Console**: verify meta tag present in page source

## Deploy Commands

```bash
python generate.py
git add -A
git status
git commit -m "feat: [description]"
git push
```

## Rollback

If issues found post-deploy:
```bash
git revert HEAD
git push
```
