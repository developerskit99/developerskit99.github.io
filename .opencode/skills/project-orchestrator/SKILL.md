---
name: project-orchestrator
description: Master orchestrator — coordinates all skills via 14-step quality gate for 230-tool platform
license: MIT
---

# project-orchestrator

> Master skill that coordinates all other skills.

## Checklist (run on every feature/tool)

1. Read project architecture (`AGENTS.md`, `tools.json`, `assets/`)
2. Understand existing components — reuse, don't duplicate
3. Identify reusable functionality
4. Implement feature with Tool contract: Input → Validation → Processing → Result → Copy → Download → Reset → Error
5. Run tests (if present)
6. Run accessibility checks (keyboard, focus, labels, contrast)
7. Run SEO checks (title/meta/canonical/H1/JSON-LD/sitemap/internal links)
8. Run performance checks (minimal JS, no global large libs, CWV)
9. Check mobile layout (320px → 1440px)
10. Update sitemap.xml
11. Update internal links (6-8 related per tool, topic clusters)
12. Review generated content (formula, 2 examples, 3-4 FAQ — no filler)
13. Run build: `python generate.py` → verify no console errors / broken links
14. Report problems

## Skill invocation order
product-architect → seo-engine → frontend-architect + ui-design-engineer → tool-engineer → content-engineer → internal-linking-engineer → qa/security/a11y/perf → release-engineer
