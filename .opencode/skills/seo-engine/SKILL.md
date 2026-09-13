---
name: seo-engine
description: >
  Technical SEO audit: crawlability, indexability, security, URL structure,
  mobile, Core Web Vitals, structured data, JavaScript rendering, and
  IndexNow protocol. Use when user says "technical SEO", "crawl issues",
  "robots.txt", "Core Web Vitals", "site speed", or "security headers".
user-invocable: true
argument-hint: "[url]"
license: MIT
metadata:
  author: AgriciDaniel
  version: "2.3.1"
  category: seo
---

# Technical SEO Audit

## Categories

### 1. Crawlability
- robots.txt: exists, valid, not blocking important resources
- XML sitemap: valid, referenced in robots.txt
- Noindex tags: intentional vs accidental
- Crawl depth: important pages within 3 clicks of homepage
- JavaScript rendering: check if critical content requires JS execution
- Googlebot fetch limits: first 2MB of HTML (keep key content + structured data within this)
- Crawl rate auto-adjusts (no manual crawl-rate control since Jan 2024)
- AI crawler management (GPTBot, ClaudeBot, PerplexityBot, etc.) via robots.txt

### 2. Indexability
- Canonical tags: self-referencing, no conflicts with noindex
- Duplicate content: near-duplicates, parameter URLs, www vs non-www
- Thin content: pages below minimum word counts per type
- Hreflang: correct for multi-language/multi-region sites
- Index bloat: unnecessary pages consuming crawl budget

### 3. Security
- HTTPS: enforced, valid SSL certificate, no mixed content
- Security headers: CSP, HSTS, X-Frame-Options, X-Content-Type-Options, Referrer-Policy
- Back-button hijacking: flag pages that defeat the Back button (spam-policy violation since 2026-04-13)

### 4. URL Structure
- Clean URLs: descriptive, hyphenated, no query parameters for content
- Redirects: no chains (max 1 hop), 301 for permanent moves
- URL length: flag >100 characters
- Trailing slashes: consistent usage

### 5. Mobile Optimization & Page Experience
- Responsive design: viewport meta tag, responsive CSS
- Touch targets: minimum 48x48px with 8px spacing
- Font size: minimum 16px base
- No horizontal scroll
- Mobile-first indexing: Googlebot Smartphone is the primary crawler
- Mobile/desktop content parity: equivalent primary content, matching robots meta tags

### 6. Core Web Vitals
- LCP (Largest Contentful Paint): target <=2.5s
- INP (Interaction to Next Paint): target <=200ms (replaced FID March 2024)
- CLS (Cumulative Layout Shift): target <=0.1
- Evaluation uses 75th percentile of real user data

### 7. Structured Data
- Detection: JSON-LD (preferred), Microdata, RDFa
- Validation against Google's supported types
- JSON-LD preferred format (Google's stated preference)
- Include in initial server-rendered HTML for time-sensitive data

### 8. JavaScript Rendering
- Check if content visible in initial HTML vs requires JS
- SSR/SSG for public SEO content, CSR only for authenticated content
- Serve critical SEO elements (canonical, meta robots, structured data) in initial HTML

### 9. IndexNow Protocol
- Check if site supports IndexNow for Bing, Yandex, Naver
- Recommend implementation for faster indexing on non-Google engines

## Output

### Technical Score: XX/100

### Category Breakdown
| Category | Status | Score |
|----------|--------|-------|
| Crawlability | pass/warn/fail | XX/100 |
| Indexability | pass/warn/fail | XX/100 |
| Security | pass/warn/fail | XX/100 |
| URL Structure | pass/warn/fail | XX/100 |
| Mobile | pass/warn/fail | XX/100 |
| Core Web Vitals | pass/warn/fail | XX/100 |
| Structured Data | pass/warn/fail | XX/100 |
| JS Rendering | pass/warn/fail | XX/100 |
| IndexNow | pass/warn/fail | XX/100 |

### Critical Issues (fix immediately)
### High Priority (fix within 1 week)
### Medium Priority (fix within 1 month)
### Low Priority (backlog)
