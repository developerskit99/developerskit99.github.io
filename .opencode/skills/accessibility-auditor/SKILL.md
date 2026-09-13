---
name: accessibility-auditor
description: >
  Quick WCAG accessibility scan of any URL. Checks color contrast, missing
  alt text, keyboard navigation, ARIA labels, heading hierarchy, and focus
  indicators. Produces a graded report. Uses Playwright MCP only — no signup.
user-invocable: true
argument-hint: "[url]"
license: Apache-2.0
metadata:
  author: Quality-Max
  version: "1.0"
  category: qa
---

# Accessibility Check

Scan any web page for WCAG accessibility violations. No signup required.

## Prerequisites

- **Playwright MCP** (comes with Claude Code)

## Checks

### Images & Media
- Every `img` must have `alt` attribute
- Decorative images should have `alt=""`
- `video` and `audio` should have captions/transcripts

### Headings
- Page should have exactly one `h1`
- Headings should not skip levels (h1 → h3 without h2)
- Headings should be descriptive, not empty

### Forms
- Every input must have a visible `label` or `aria-label`
- Required fields should be marked
- Error messages should be associated with fields

### Keyboard
- All interactive elements should be focusable
- Tab order should be logical
- No keyboard traps (can tab in and out of everything)
- Focus indicator must be visible

### Color & Contrast
- Text should have 4.5:1 contrast ratio (AA)
- Large text (18px+) needs 3:1 minimum
- Information should not rely on color alone

### ARIA
- Interactive elements should have accessible names
- `role` attributes should be valid
- `aria-hidden="true"` should not hide focusable elements

### Structure
- Page should have landmark regions (main, nav, header, footer)
- Links should have descriptive text (not "click here")
- Language attribute on `<html>`

## Grading

- A: 0-1 issues
- B: 2-4 issues
- C: 5-8 issues
- D: 9-12 issues
- F: 13+ issues

## Output

```
## Accessibility Report: [URL]

**Grade: B** (3 issues found)

### Issues
1. [CRITICAL] 2 images missing alt text
2. [WARNING] Heading hierarchy skips h2
3. [WARNING] 1 form input without label

### Passed
- Color contrast: OK
- Keyboard navigation: OK
- ARIA landmarks: OK
- Language attribute: OK
```
