---
name: seo-engine/check
description: >
  Quick SEO health check of any URL. Checks meta tags, headings, image alts,
  structured data, open graph, and common SEO issues. Uses Playwright MCP
  only — no signup.
user-invocable: true
argument-hint: "[url]"
license: Apache-2.0
metadata:
  author: Quality-Max
  version: "1.0"
  category: seo
---

# SEO Quick Check

Check basic SEO health of any page. No signup required.

## Prerequisites

- **Playwright MCP** (comes with Claude Code)

## Checks

**Title** — exists, 30-60 chars, contains keywords
**Description** — exists, 120-160 chars, compelling
**Headings** — exactly one h1, logical h2 structure
**Images** — all have alt text, descriptive not generic
**Open Graph** — og:title, og:description, og:image present
**Twitter Card** — twitter:card meta tag
**Canonical** — canonical URL set
**Structured Data** — valid JSON-LD present
**Language** — lang attribute on html
**Viewport** — meta viewport for mobile

## Output

```
## SEO Check: [URL]

**Score: 7/10**

### Issues
- Title too long (74 chars) — trim to under 60
- Missing meta description
- 4 of 12 images missing alt text
- No Twitter Card meta tags

### Passed
- h1: "Welcome to MyApp" (1 h1, good)
- Open Graph: title, description, image all set
- Canonical URL: set correctly
- Structured Data: Organization schema found
- Language: en
- Viewport: configured for mobile
```
