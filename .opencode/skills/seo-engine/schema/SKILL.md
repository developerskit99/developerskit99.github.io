---
name: seo-schema
description: >
  Detect, validate, and generate Schema.org structured data. JSON-LD format
  preferred. Use when user says "schema", "structured data", "rich results",
  "JSON-LD", or "markup".
user-invocable: true
argument-hint: "[url]"
license: MIT
metadata:
  author: AgriciDaniel
  version: "2.3.1"
  category: seo
---

# Schema Markup Analysis & Generation

## Detection

1. Scan page source for JSON-LD `<script type="application/ld+json">`
2. Check for Microdata (`itemscope`, `itemprop`)
3. Check for RDFa (`typeof`, `property`)
4. Always recommend JSON-LD as primary format (Google's stated preference)

## Validation

- Check required properties per schema type
- Validate against Google's supported rich result types
- Test for common errors: missing @context, invalid @type, wrong data types, placeholder text, relative URLs, invalid date formats
- Flag deprecated types (HowTo, SpecialAnnouncement, CourseInfo, etc.)

## Schema Type Status (June 2026)

### ACTIVE (recommend freely):
Organization, LocalBusiness, SoftwareApplication, WebApplication, Product, ProductGroup, Offer, Service, Article, BlogPosting, NewsArticle, Review, AggregateRating, BreadcrumbList, WebSite, WebPage, Person, ProfilePage, ContactPage, VideoObject, ImageObject, Event, JobPosting, Course, DiscussionForumPosting

### DEPRECATED (never recommend):
- **HowTo**: Rich results removed September 2023
- **FAQPage**: Google retired FAQ rich results for ALL sites on May 7, 2026 (use QAPage for genuine Q&A)
- **SpecialAnnouncement**: Deprecated July 31, 2025
- **CourseInfo, EstimatedSalary, LearningVideo**: Retired June 2025

### Still supported (do not flag):
QAPage, DiscussionForumPosting, Education Q&A

## Generation

When generating schema for a page:
1. Identify page type from content analysis
2. Select appropriate schema type(s)
3. Generate valid JSON-LD with all required + recommended properties
4. Include only truthful, verifiable data
5. Validate output before presenting

## Common Schema Templates

### SoftwareApplication (for tools)
```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "[Tool Name]",
  "url": "[Tool URL]",
  "applicationCategory": "DeveloperApplication",
  "operatingSystem": "Web Browser",
  "description": "[Description]",
  "offers": {
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "USD"
  }
}
```

### BreadcrumbList
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "[URL]"},
    {"@type": "ListItem", "position": 2, "name": "[Category]", "item": "[URL]"},
    {"@type": "ListItem", "position": 3, "name": "[Tool]"}
  ]
}
```

### FAQPage
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "[Question]",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[Answer]"
      }
    }
  ]
}
```

## Output

### Validation Results
| Schema | Type | Status | Issues |
|--------|------|--------|--------|
| ... | ... | pass/warn/fail | ... |

### Recommendations
- Missing schema opportunities
- Validation fixes needed
- Generated code for implementation
