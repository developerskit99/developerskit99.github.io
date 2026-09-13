---
name: qa-engineer
description: >
  Edge cases, mobile, keyboard, copy/download checks for tool pages.
  Validates Tool contract: Input → Validation → Processing → Result → Copy → Download → Reset → Error.
user-invocable: true
argument-hint: "[slug]"
license: MIT
metadata:
  author: DevelopersKit
  version: "1.0"
  category: qa
---

# QA Engineer — Tool Page Validation

Validates every tool page against the Tool contract and catches edge cases.

## Tool Contract Checklist

For each tool page, verify:

1. **Input**: accepts user data (text, file, options) with proper labels
2. **Validation**: shows meaningful errors for invalid/empty input
3. **Processing**: performs computation client-side with no data uploads
4. **Result**: displays output clearly with formatting
5. **Copy**: copy-to-clipboard works (text output)
6. **Download**: download button works (file output)
7. **Reset**: clears all fields and returns to empty state
8. **Error**: handles edge cases gracefully (empty, huge input, special chars)

## Edge Cases to Test

### Input Edge Cases
- Empty submission
- Very long input (>10,000 chars)
- Special characters: `<script>alert(1)</script>`, `'"; DROP TABLE--`
- Unicode: emoji, RTL text, CJK characters
- Whitespace-only input
- Paste vs type behavior

### Processing Edge Cases
- Zero values in calculators
- Negative numbers where inappropriate
- Division by zero
- Infinity/NaN results
- Maximum safe integer overflow

### Output Edge Cases
- Very long output (scroll behavior)
- Copy button with long text
- Download with empty output
- Multiple rapid clicks on process/copy/download

## Mobile Checks

- All inputs accessible on 320px viewport
- No horizontal scroll
- Touch targets >= 48x48px
- Keyboard doesn't overlap inputs
- Results visible without excessive scrolling

## Keyboard Checks

- Tab order: input → process → result → copy/download → reset
- Enter submits form
- Escape clears/errors
- Focus visible on all interactive elements
- No keyboard traps

## Output

### QA Report: [Tool Name]

| Check | Status | Notes |
|-------|--------|-------|
| Input validation | pass/fail | ... |
| Processing | pass/fail | ... |
| Result display | pass/fail | ... |
| Copy functionality | pass/fail | ... |
| Download functionality | pass/fail | ... |
| Reset functionality | pass/fail | ... |
| Error handling | pass/fail | ... |
| Mobile layout | pass/fail | ... |
| Keyboard navigation | pass/fail | ... |
| XSS prevention | pass/fail | ... |

### Issues Found
### Recommendations
