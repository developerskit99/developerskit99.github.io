---
name: tool-engineer
description: >
  Implements tool page logic: Input → Validation → Processing → Result → Copy → Download → Reset → Error.
  Reuses ToolKit from assets/js/tools.js (130+ helpers). No data leaves browser.
user-invocable: true
argument-hint: "[slug]"
license: MIT
metadata:
  author: DevelopersKit
  version: "1.0"
  category: engineering
---

# Tool Engineer — Tool Page Implementation

Implements tool page HTML/JS following the Tool contract and reusing ToolKit.

## Tool Contract

Every tool must follow this flow:

```
Input → Validation → Processing → Result → Copy/Download → Reset
```

## Implementation Template

```html
<section class="tool-section">
  <h2>Input</h2>
  <label for="input">Input Label</label>
  <textarea id="input" rows="6" placeholder="Enter data..."></textarea>
  <div class="tool-actions">
    <button onclick="processTool()" class="btn-primary">Process</button>
    <button onclick="resetTool()" class="btn-secondary">Reset</button>
  </div>
</section>

<section class="tool-section result-section" id="result" style="display:none">
  <h2>Result</h2>
  <pre id="output"></pre>
  <div class="tool-actions">
    <button onclick="copyResult()" class="btn-secondary">Copy</button>
    <button onclick="downloadResult()" class="btn-secondary">Download</button>
  </div>
</section>

<section class="tool-section" id="error" style="display:none">
  <div class="error-msg" role="alert"></div>
</section>
```

## ToolKit Helpers (from assets/js/tools.js)

| Helper | Purpose |
|--------|---------|
| `ToolKit.copy(text)` | Copy to clipboard |
| `ToolKit.download(text, filename)` | Download as file |
| `ToolKit.error(msg)` | Show error message |
| `ToolKit.result(html)` | Show result |
| `ToolKit.reset()` | Reset all fields |
| `ToolKit.validate(input)` | Basic input validation |
| `ToolKit.sanitize(html)` | XSS prevention |
| `ToolKit.formatNumber(n)` | Number formatting |
| `ToolKit.formatBytes(b)` | File size formatting |
| `ToolKit.debounce(fn, ms)` | Debounce function |

## Rules

1. **No data uploads** — all processing client-side
2. **XSS prevention** — use ToolKit.sanitize() for any user content display
3. **Input validation** — always validate before processing
4. **Error handling** — show user-friendly error messages
5. **Empty state** — show placeholder/instructions when no input
6. **Mobile first** — test at 320px width
7. **Keyboard accessible** — all actions reachable via keyboard
8. **Reuse ToolKit** — never duplicate existing helpers

## After Implementation

1. Test all edge cases (empty, huge, special chars)
2. Verify copy/download works
3. Verify reset clears everything
4. Check console for errors
5. Test keyboard navigation
6. Run `python generate.py` to rebuild
