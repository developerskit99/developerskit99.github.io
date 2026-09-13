---
name: qa-engine/console-error-scan
description: >
  Detect JavaScript errors, warnings, and failed network requests on any
  page. Navigates the URL, collects console output and network failures.
  Uses Playwright MCP only — no signup.
user-invocable: true
argument-hint: "[url]"
license: Apache-2.0
metadata:
  author: Quality-Max
  version: "1.0"
  category: qa
---

# Console Error Scanner

Find JS errors and failed requests hiding in the browser console. No signup required.

## Prerequisites

- **Playwright MCP** (comes with Claude Code)

## Categories

- **JS Errors** — uncaught exceptions, type errors, reference errors
- **Failed Requests** — 4xx/5xx responses, CORS errors, timeouts
- **Deprecation Warnings** — deprecated API usage
- **Mixed Content** — HTTP resources on HTTPS page
- **CSP Violations** — blocked by Content Security Policy

## Output

```
## Console Health: [URL]

**Pages checked: 4** | **Errors: 5** | **Warnings: 3**

### Errors
1. [JS] TypeError: Cannot read property 'map' of undefined
   - Page: /dashboard
   - Source: app.bundle.js:234

2. [NETWORK] GET /api/user/preferences — 500 Internal Server Error

### Warnings
1. [DEPRECATION] document.domain setter is deprecated
2. [MIXED CONTENT] Loading HTTP image on HTTPS page

### Clean Pages
- /about — no errors
- /pricing — no errors
```
