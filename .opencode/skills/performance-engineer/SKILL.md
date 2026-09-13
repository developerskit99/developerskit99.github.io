---
name: performance-engineer
description: >
  Measure Core Web Vitals on any URL — LCP, CLS, INP, TTFB, FCP — using the
  browser's own performance APIs. Grades each metric against Google's
  thresholds and produces an A-F report. Playwright MCP only, no signup.
user-invocable: true
argument-hint: "[url]"
license: Apache-2.0
metadata:
  author: Quality-Max
  version: "1.0"
  category: performance
---

# Core Web Vitals

Measure the Core Web Vitals of any page using real browser performance APIs. No signup required.

## Prerequisites

- **Playwright MCP** (comes with Claude Code)

## Workflow

1. Navigate to the URL
2. Let the page settle (~3s)
3. Collect metrics with browser_evaluate:

```javascript
() => new Promise((resolve) => {
  const out = {};
  const nav = performance.getEntriesByType('navigation')[0];
  if (nav) out.ttfb = Math.round(nav.responseStart);
  const fcp = performance.getEntriesByName('first-contentful-paint')[0];
  if (fcp) out.fcp = Math.round(fcp.startTime);
  try {
    new PerformanceObserver((list) => {
      const e = list.getEntries();
      out.lcp = Math.round(e[e.length - 1].startTime);
    }).observe({ type: 'largest-contentful-paint', buffered: true });
  } catch (e) {}
  let cls = 0;
  try {
    new PerformanceObserver((list) => {
      for (const entry of list.getEntries()) {
        if (!entry.hadRecentInput) cls += entry.value;
      }
      out.cls = Math.round(cls * 1000) / 1000;
    }).observe({ type: 'layout-shift', buffered: true });
  } catch (e) {}
  setTimeout(() => resolve(out), 1500);
})
```

## Grading Thresholds

| Metric | Good      | Needs work        | Poor      |
|--------|-----------|-------------------|-----------|
| LCP    | <= 2500ms | 2500–4000ms       | > 4000ms  |
| CLS    | <= 0.1    | 0.1–0.25          | > 0.25    |
| INP    | <= 200ms  | 200–500ms         | > 500ms   |
| TTFB   | <= 800ms  | 800–1800ms        | > 1800ms  |
| FCP    | <= 1800ms | 1800–3000ms       | > 3000ms  |

## Overall Grade

- A: all Good
- B: one "Needs work"
- C: two/three "Needs work"
- D: any Poor
- F: multiple Poor

## Output

```
## Core Web Vitals Report: [URL]

**Grade: B** — one metric needs work

| Metric | Value   | Rating       |
|--------|---------|--------------|
| LCP    | 2.9s    | Needs work   |
| CLS    | 0.04    | Good         |
| INP    | (not measured — needs interaction) |
| TTFB   | 410ms   | Good         |
| FCP    | 1.6s    | Good         |
```
