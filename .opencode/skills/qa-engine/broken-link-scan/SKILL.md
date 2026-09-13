---
name: qa-engine/broken-link-scan
description: >
  Find broken links on any website. Crawls the page, checks every link for
  404s, redirects, and timeouts. Reports dead links with their location.
  Uses Playwright MCP only — no signup.
user-invocable: true
argument-hint: "[url]"
license: Apache-2.0
metadata:
  author: Quality-Max
  version: "1.0"
  category: qa
---

# Broken Link Scanner

Find every broken link on a page. No signup required.

## Prerequisites

- **Playwright MCP** (comes with Claude Code)

## Workflow

1. Navigate to the URL
2. Extract all links using browser_evaluate
3. For each link (up to 50), check status
4. Flag: 404, 500, redirect chains, empty href, javascript:void

## Output

```
## Broken Link Report: [URL]

**Scanned: 34 links** (28 internal, 6 external)

### Broken (3)
- "About Us" → /about-us — 404 Not Found
- "Old Blog" → /blog/2023 — 301 → 404
- "Partner" → https://dead-link.com — timeout

### Redirects (2)
- "Login" → /login — 301 → /auth/login

### External (not checked)
- https://github.com/...
```
