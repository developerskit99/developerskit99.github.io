# DevelopersKit — Project Rules (Enforced on Every Task)

You are working on a production-grade static SEO tools platform hosted at https://developerskit.github.io.

## PROJECT GOAL
Build a fast, professional, accessible, SEO-focused collection of 230 browser-based online tools hosted entirely on GitHub Pages. Priorities: Search usefulness > Technical correctness > UX > Performance > Accessibility > Maintainability > Security > Scalable architecture.

## GENERAL ENGINEERING RULES
1. Inspect existing repo before modifying anything.
2. Reuse existing components/utilities. Do not duplicate functionality.
3. Do not create unnecessary dependencies. Prefer vanilla JS (no framework) for GitHub Pages.
4. Keep project compatible with static GitHub Pages hosting. No backend, no VPS, no database.
5. Prefer client-side processing (file processing in browser via Canvas/FileReader). Never upload user files.
6. Preserve SEO metadata, accessibility, mobile responsiveness.
7. Keep tools client-side whenever technically possible.

## ARCHITECTURE — Tools are data + reusable components
Every tool must have: dedicated route (/<slug>/), config in tools.json, reusable ToolLayout/Input/Output/Copy/Download/Reset/Error/FAQ/RelatedTools/Breadcrumbs, input validation, Processing, Result, error handling, empty state, mobile layout, keyboard a11y.
Shared: assets/css/style.css, assets/js/common.js, assets/js/tools.js

## SEO — Every indexable page
- unique URL, title (50-60ch), meta description (150-160ch), canonical https://developerskit.github.io/<slug>/, correct H1, heading hierarchy, useful content (formula + 2 worked examples + 3-4 FAQ), internal links (6-8 related), breadcrumbs, JSON-LD (SoftwareApplication + FAQPage + BreadcrumbList), sitemap.xml inclusion
- No thin pages, no keyword stuffing, no fake stats/testimonials, no "best" claims.

## INTERNAL LINKING — Topic clusters
JSON Formatter → Validator → Minifier → JSON→CSV → CSV→JSON. Every tool links to 6-8 related. Build logical clusters.

## PERFORMANCE
Minimal JS, minimal deps, lazy-load where useful, optimized assets, semantic HTML, Core Web Vitals. No large libs globally if only one tool needs it.

## ACCESSIBILITY
Keyboard nav, visible focus, semantic HTML, labels, ARIA only when necessary, contrast WCAG AA, screen-reader usable, errors not color-only.

## FILE TOOLS (Image)
Validate type/size, handle corrupt/unsupported, useful errors, revokeObjectURL, prevent memory leaks.

## SECURITY
Check XSS, unsafe innerHTML, malicious input, file handling, deps. Never put secrets in frontend.

## BEFORE COMPLETE
1. Run generate.py + verify build
2. Check console errors, broken links, a11y, responsive, SEO metadata/canonical/structured data/sitemap/performance
3. Tests pass (if present)

## WHEN ADDING NEW TOOL
Research intent → check duplicate → design URL → SEO metadata → identify related → reuse components → implement logic → UI → explanatory content → internal links → tests → quality gates → build → review diff.

Do NOT blindly generate duplicates, thin SEO pages, copy competitor content, stuff keywords, sacrifice UX/a11y/perf.
