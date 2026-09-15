#!/usr/bin/env python3
import json, os, html, datetime

ROOT=os.path.dirname(os.path.abspath(__file__))
TOOLS_JSON=os.path.join(ROOT,"tools.json")
def _get_site_url():
    try:
        with open(TOOLS_JSON, encoding="utf-8-sig") as f:
            return json.load(f).get("site",{}).get("url","https://developerskit99.github.io")
    except Exception:
        return "https://developerskit99.github.io"
SITE_URL=_get_site_url()
# derive base path for subpath deploys (e.g. /developerskit99.github.io/)
from urllib.parse import urlparse as _urlparse
_BP=_urlparse(SITE_URL).path.rstrip("/")
BASE="" if not _BP else _BP
DATE="2026-09-13"
YEAR=datetime.datetime.now().year

SUBCATEGORIES = {
    "Developer Tools": [
        ("JSON Tools", ["json-formatter","json-validator","json-minifier","json-to-csv","csv-to-json","json-to-yaml","yaml-to-json","yaml-formatter"]),
        ("Encoding Tools", ["base64-encoder","base64-decoder","url-encoder","url-decoder","html-entity-encoder","html-entity-decoder"]),
        ("Dev Utilities", ["uuid-generator","random-string-generator","hash-generator","jwt-decoder","unix-timestamp-converter","cron-expression-generator","regex-tester","regex-generator","lorem-ipsum-generator"]),
    ],
    "CSS/HTML Tools": [
        ("Minify & Beautify", ["css-minifier","css-beautifier","html-minifier","html-beautifier","javascript-minifier","javascript-beautifier"]),
        ("CSS Generators", ["css-gradient-generator","css-box-shadow-generator","css-border-radius-generator","css-text-shadow-generator","css-button-generator","css-glassmorphism-generator","css-neumorphism-generator","css-transform-generator","css-animation-generator"]),
        ("Layout & Utilities", ["css-flexbox-generator","css-grid-generator","css-clamp-generator","css-filter-generator","css-color-converter"]),
    ],
    "Text Tools": [
        ("Word & Character Counts", ["word-counter","character-counter","sentence-counter","paragraph-counter","reading-time-calculator"]),
        ("Case & Format", ["case-converter","uppercase-converter","lowercase-converter","title-case-converter","text-to-slug-converter","slug-generator"]),
        ("Text Processing", ["remove-duplicate-lines","sort-lines-alphabetically","reverse-text","remove-extra-spaces","find-and-replace-tool","text-cleaner","text-diff-checker","text-line-break-remover"]),
        ("Markdown & Conversion", ["markdown-previewer","markdown-table-generator","markdown-to-html-converter","html-to-markdown-converter","text-to-ascii-generator","ascii-art-generator"]),
    ],
    "Math Calculators": [
        ("Percentage & Ratio", ["percentage-calculator","percentage-increase-calculator","percentage-decrease-calculator","ratio-calculator","proportion-calculator"]),
        ("Statistics", ["average-calculator","median-calculator","mode-calculator","standard-deviation-calculator","mean-calculator"]),
        ("Fractions & Numbers", ["fraction-calculator","decimal-to-fraction","fraction-to-decimal","mixed-number-calculator","gcd-calculator","lcm-calculator","prime-number-checker","prime-number-generator","factor-calculator"]),
        ("Number Systems", ["binary-calculator","binary-to-decimal","decimal-to-binary","hex-to-decimal","decimal-to-hex","octal-converter","roman-numeral-converter","scientific-notation-converter"]),
        ("Advanced Math", ["exponent-calculator","square-root-calculator","random-number-generator"]),
    ],
    "Student Tools": [
        ("Grade Calculators", ["grade-calculator","gpa-calculator","cgpa-calculator","percentage-to-gpa-calculator","exam-percentage-calculator","marks-percentage-calculator","final-grade-calculator","weighted-grade-calculator"]),
        ("Study Planning", ["study-time-calculator","pomodoro-timer","exam-countdown","assignment-countdown","semester-countdown","study-schedule-generator","revision-schedule-generator"]),
        ("Practice & Quizzes", ["flashcard-generator","random-quiz-generator","multiplication-table-generator","times-table-quiz","random-math-quiz"]),
        ("Advanced Math", ["equation-solver","quadratic-equation-solver","factorial-calculator","scientific-calculator","unit-conversion-calculator"]),
    ],
    "Date & Time": [
        ("Age & Date Diff", ["age-calculator","date-difference-calculator","days-between-dates","weeks-between-dates","months-between-dates"]),
        ("Business Days", ["business-days-calculator","working-days-calculator"]),
        ("Date Operations", ["days-until-date","date-addition-calculator","date-subtraction-calculator"]),
        ("Time & Conversion", ["time-difference-calculator","time-duration-calculator","hours-to-minutes-converter","minutes-to-seconds-converter","seconds-to-hours-converter"]),
        ("Date Utilities", ["unix-timestamp-generator","leap-year-checker","day-of-week-calculator","week-number-calculator","date-format-converter"]),
    ],
    "Finance Calculators": [
        ("Interest & Loans", ["simple-interest-calculator","compound-interest-calculator","loan-emi-calculator","mortgage-calculator","loan-payment-calculator","loan-interest-calculator"]),
        ("Investments", ["investment-return-calculator","cagr-calculator","sip-calculator","inflation-calculator","savings-goal-calculator","retirement-calculator"]),
        ("Shopping & Bills", ["discount-calculator","sale-price-calculator","markup-calculator","tip-calculator","split-bill-calculator"]),
        ("Income & Tax", ["salary-calculator","hourly-to-yearly-salary","yearly-to-hourly-salary","tax-percentage-calculator","budget-calculator","net-worth-calculator"]),
        ("Profit & Margin", ["profit-margin-calculator","break-even-calculator"]),
    ],
    "Business Calculators": [
        ("Revenue & Profit", ["profit-calculator","revenue-calculator","roi-calculator","roas-calculator","gross-margin-calculator","net-margin-calculator","markup-vs-margin-calculator"]),
        ("Marketing Metrics", ["conversion-rate-calculator","ctr-calculator","cpm-calculator","cpc-calculator","customer-acquisition-cost-calculator","customer-lifetime-value-calculator","churn-rate-calculator","growth-rate-calculator"]),
        ("Operations", ["inventory-turnover-calculator","sales-commission-calculator","break-even-units-calculator","saas-pricing-calculator","freelance-hourly-rate-calculator"]),
    ],
    "Color Tools": [
        ("Color Conversion", ["hex-to-rgb","rgb-to-hex","rgb-to-hsl","hsl-to-rgb","hex-to-hsl","css-color-converter","tailwind-color-converter","material-color-converter","css-color-generator"]),
        ("Color Picking & Palettes", ["color-picker","color-palette-generator","random-color-generator","gradient-generator","complementary-color-generator","analogous-color-generator","triadic-color-generator","rgb-color-mixer","color-name-finder"]),
        ("Accessibility", ["contrast-checker","wcag-contrast-checker","color-blindness-simulator"]),
    ],
    "Image Tools": [
        ("Resize & Crop", ["image-resizer","image-cropper","social-media-image-resizer","youtube-thumbnail-resizer","instagram-image-resizer"]),
        ("Convert & Compress", ["image-compressor","jpg-to-png","png-to-jpg","webp-to-jpg","jpg-to-webp","png-to-webp"]),
        ("Metadata & Info", ["image-metadata-viewer","image-dimension-checker","image-aspect-ratio-calculator","image-pixel-color-picker"]),
        ("Generate & Encode", ["favicon-generator","app-icon-generator","gif-frame-extractor","image-to-base64","base64-to-image"]),
    ],
}

CATEGORY_SLUGS = {
    "Developer Tools": "developer-tools",
    "CSS/HTML Tools": "css-html-tools",
    "Text Tools": "text-tools",
    "Math Calculators": "math-calculators",
    "Student Tools": "student-tools",
    "Date & Time": "date-time",
    "Finance Calculators": "finance-calculators",
    "Business Calculators": "business-calculators",
    "Color Tools": "color-tools",
    "Image Tools": "image-tools",
}

def esc(s): return html.escape(str(s or ""),quote=True)
def esc_txt(s): return html.escape(str(s or ""))

def seo_title(t):
    base=f"{t} \u2014 Free Online Tool | DevelopersKit"
    if len(base)<=60: return base
    # truncate title part to fit 60
    max_t=60-len(" \u2014 Free Online Tool | DevelopersKit")
    tt=t[:max_t].rstrip()
    return f"{tt} \u2014 Free Online Tool | DevelopersKit"

def read_data():
    with open(TOOLS_JSON,encoding="utf-8-sig") as f: d=json.load(f)
    site=d.get("site",{})
    tools=d.get("tools",[])
    return site, tools

def head_html(title,desc,canonical):
    og=esc(canonical)
    return f"""<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="google-site-verification" content="_LFM9G4uH81w3sp_bIwp7BGQTwWR5vq_BrqW4hGFofc" />
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{og}">
<meta name="theme-color" content="#2563eb">
<link rel="icon" type="image/svg+xml" href="{BASE}/assets/images/favicon.svg">
<link rel="icon" type="image/png" sizes="192x192" href="{BASE}/assets/images/favicon-192x192.png">
<link rel="icon" type="image/png" sizes="48x48" href="{BASE}/assets/images/favicon-48x48.png">
<link rel="icon" type="image/png" sizes="32x32" href="{BASE}/assets/images/favicon-32x32.png">
<link rel="apple-touch-icon" sizes="180x180" href="{BASE}/assets/images/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{og}">
<meta property="og:image" content="{SITE_URL}/assets/images/og-default.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:type" content="image/png">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<link rel="stylesheet" href="{BASE}/assets/css/style.css">"""

def header_html(search=False):
    s_input='<div class="search-wrap"><label for="q" class="sr-only">Search tools</label><input id="q" data-search-input type="search" class="search-input" placeholder="Search tools (e.g. JSON Formatter)" autocomplete="off"></div>' if search else ''
    return f"""<a href="#main" class="skip">Skip to content</a>
<header class="header">
<div class="container header-inner">
<a href="{BASE}/" class="logo" aria-label="DevelopersKit home"><img src="{BASE}/assets/images/logo.svg" alt="DevelopersKit" height="32" width="160"></a>
<nav class="nav" aria-label="Primary">
<button class="nav-toggle" data-nav-toggle aria-expanded="false" aria-controls="nav-links" aria-label="Toggle menu">Menu</button>
<ul id="nav-links" class="nav-links" data-nav-menu>
<li><a href="{BASE}/">Home</a></li>
<li><a href="{BASE}/#tools">Tools</a></li>
<li><a href="{BASE}/#categories">Categories</a></li>
<li><a href="{BASE}/about/">About</a></li>
</ul>
</nav>
</div>
</header>
{s_input}"""

def footer_html():
    return f"""<footer class="footer">
<div class="container footer-grid">
<div><img src="{BASE}/assets/images/logo.svg" alt="DevelopersKit" height="28" width="140" style="margin-bottom:8px"><p style="margin-top:8px">Free browser-based tools for developers, students, and professionals. Your data stays in your browser \u2014 no uploads, no sign-up.</p></div>
<div><p><a href="{BASE}/">Home</a> \u00b7 <a href="{BASE}/about/">About</a> \u00b7 <a href="{BASE}/sitemap.xml">Sitemap</a> \u00b7 <a href="{BASE}/privacy/">Privacy</a> \u00b7 <a href="https://github.com/developerskit99/developerskit99.github.io">GitHub</a></p><p style="margin-top:8px">\u00a9 <span id="year">{YEAR}</span> DevelopersKit. All tools run client-side.</p></div>
</div>
</footer>
<script src="{BASE}/assets/js/common.js" defer></script>
<script src="{BASE}/assets/js/tools.js" defer></script>"""

def tool_ui(tool):
    slug=tool["slug"]; cat=tool["category"]; title=tool["title"]
    # generic UI: provide flexible inputs, hidden extra fields toggled by js
    # For Image Tools: file input + canvas preview
    if cat=="Image Tools":
        return f"""
<div class="tool-layout">
<div class="tool-main">
<label for="tool-input">Upload image</label>
<input id="tool-input" type="file" accept="image/*">
<div class="form-row" style="margin-top:12px">
<div><label for="tool-w">Width (px, optional)</label><input id="tool-w" type="number" min="1" max="8000" placeholder="e.g. 800"></div>
<div><label for="tool-h">Height (px, optional)</label><input id="tool-h" type="number" min="1" max="8000" placeholder="e.g. 600"></div>
<div><label for="tool-q">Quality (0.1-1, optional)</label><input id="tool-q" type="number" min="0.1" max="1" step="0.05" placeholder="0.85"></div>
</div>
<div id="tool-error" class="error" hidden aria-live="polite"></div>
<div style="margin:12px 0"><button id="tool-btn" class="btn btn-primary" type="button">Process</button></div>
<div id="tool-preview" style="margin:12px 0"></div>
<label for="tool-output">Result</label>
<textarea id="tool-output" readonly placeholder="Result will appear here..." rows="4"></textarea>
<canvas id="tool-canvas" style="display:none"></canvas>
<div class="btn-group" style="margin-top:12px">
<button data-copy data-copy-target="#tool-output" class="btn btn-secondary btn-sm" type="button">Copy</button>
<button id="tool-download" class="btn btn-secondary btn-sm" type="button">Download</button>
<button id="tool-reset" class="btn btn-ghost btn-sm" type="button">Reset</button>
</div>
</div>
</div>"""
    if cat=="Color Tools":
        return f"""
<div class="tool-layout">
<div class="tool-main">
<label for="tool-color">Pick color</label>
<input id="tool-color" type="color" value="#2563eb" style="height:48px;width:100%;padding:2px">
<label for="tool-input" style="margin-top:12px">Or enter HEX / RGB</label>
<input id="tool-input" type="text" placeholder="#2563eb or rgb(37,99,235)">
<div id="tool-error" class="error" hidden aria-live="polite"></div>
<div style="margin:12px 0"><button id="tool-btn" class="btn btn-primary" type="button">Process</button></div>
<label for="tool-output">Result</label>
<textarea id="tool-output" readonly placeholder="Result will appear here..." rows="6"></textarea>
<div id="tool-preview" style="margin-top:12px;height:48px;border-radius:8px;border:1px solid #e2e8f0;background:#2563eb"></div>
<div class="btn-group" style="margin-top:12px">
<button data-copy data-copy-target="#tool-output" class="btn btn-secondary btn-sm" type="button">Copy</button>
<button id="tool-download" class="btn btn-secondary btn-sm" type="button">Download</button>
<button id="tool-reset" class="btn btn-ghost btn-sm" type="button">Reset</button>
</div>
</div>
</div>"""
    if cat in ("Math Calculators","Finance Calculators","Business Calculators","Student Tools"):
        return f"""
<div class="tool-layout">
<div class="tool-main">
<div class="form-row">
<div><label for="tool-a">Value A</label><input id="tool-a" type="number" placeholder="e.g. 120"></div>
<div><label for="tool-b">Value B</label><input id="tool-b" type="number" placeholder="e.g. 30"></div>
</div>
<div class="form-row">
<div><label for="tool-c">Value C (optional)</label><input id="tool-c" type="number" placeholder="optional"></div>
<div><label for="tool-input">Extra / Expression</label><input id="tool-input" type="text" placeholder="e.g. 2+2 or text"></div>
</div>
<div id="tool-error" class="error" hidden aria-live="polite"></div>
<div style="margin:12px 0"><button id="tool-btn" class="btn btn-primary" type="button">Calculate</button></div>
<label for="tool-output">Result</label>
<textarea id="tool-output" readonly placeholder="Result will appear here..." rows="5"></textarea>
<div class="btn-group" style="margin-top:12px">
<button data-copy data-copy-target="#tool-output" class="btn btn-secondary btn-sm" type="button">Copy</button>
<button id="tool-download" class="btn btn-secondary btn-sm" type="button">Download</button>
<button id="tool-reset" class="btn btn-ghost btn-sm" type="button">Reset</button>
</div>
</div>
</div>"""
    if cat=="Date & Time":
        return f"""
<div class="tool-layout">
<div class="tool-main">
<div class="form-row">
<div><label for="tool-date-a">Start date</label><input id="tool-date-a" type="date"></div>
<div><label for="tool-date-b">End date</label><input id="tool-date-b" type="date"></div>
</div>
<label for="tool-input" style="margin-top:12px">Or enter date / timestamp</label>
<input id="tool-input" type="text" placeholder="e.g. 2026-01-01 or 1715700000">
<div id="tool-error" class="error" hidden aria-live="polite"></div>
<div style="margin:12px 0"><button id="tool-btn" class="btn btn-primary" type="button">Calculate</button></div>
<label for="tool-output">Result</label>
<textarea id="tool-output" readonly placeholder="Result will appear here..." rows="5"></textarea>
<div class="btn-group" style="margin-top:12px">
<button data-copy data-copy-target="#tool-output" class="btn btn-secondary btn-sm" type="button">Copy</button>
<button id="tool-download" class="btn btn-secondary btn-sm" type="button">Download</button>
<button id="tool-reset" class="btn btn-ghost btn-sm" type="button">Reset</button>
</div>
</div>
</div>"""
    # Developer / Text / CSS/HTML generic: textarea + optional second
    extra=""
    if slug in ("text-diff-checker","find-and-replace-tool"):
        extra='<label for="tool-input2" style="margin-top:12px">Second input</label><textarea id="tool-input2" placeholder="Second text for comparison..." rows="6"></textarea>'
    elif slug in ("regex-tester",):
        extra='<div class="form-row" style="margin-top:12px"><div><label for="tool-pattern">Pattern</label><input id="tool-pattern" type="text" placeholder="e.g. \\d+"></div><div><label for="tool-flags">Flags</label><input id="tool-flags" type="text" placeholder="gimsuy"></div></div>'
    elif slug in ("hash-generator",):
        extra='<label for="tool-algo" style="margin-top:12px">Algorithm</label><select id="tool-algo"><option value="SHA-256">SHA-256</option><option value="SHA-1">SHA-1</option><option value="SHA-384">SHA-384</option><option value="SHA-512">SHA-512</option></select>'
    elif slug in ("lorem-ipsum-generator",):
        extra='<div class="form-row" style="margin-top:12px"><div><label for="tool-lorem-type">Type</label><select id="tool-lorem-type"><option value="paragraphs">Paragraphs</option><option value="sentences">Sentences</option><option value="words">Words</option></select></div><div><label for="tool-lorem-count">Count</label><input id="tool-lorem-count" type="number" value="3" min="1" max="50"></div></div>'
    return f"""
<div class="tool-layout">
<div class="tool-main">
<label for="tool-input">{esc_txt(title)} Input</label>
<textarea id="tool-input" placeholder="Paste your content here..." rows="8"></textarea>
{extra}
<div id="tool-error" class="error" hidden aria-live="polite"></div>
<div style="margin:12px 0"><button id="tool-btn" class="btn btn-primary" type="button">Process</button></div>
<label for="tool-output">Result</label>
<textarea id="tool-output" readonly placeholder="Result will appear here..." rows="8"></textarea>
<div class="btn-group" style="margin-top:12px">
<button data-copy data-copy-target="#tool-output" class="btn btn-secondary btn-sm" type="button">Copy</button>
<button id="tool-download" class="btn btn-secondary btn-sm" type="button">Download</button>
<button id="tool-reset" class="btn btn-ghost btn-sm" type="button">Reset</button>
</div>
</div>
</div>"""

def inline_script(tool):
    slug=tool["slug"]; cat=tool["category"]
    # JS wires UI to ToolKit helpers; uses textContent safe
    return f"""
<script>
(function(){{
var slug={json.dumps(slug)}, cat={json.dumps(cat)};
var $=function(s){{return document.querySelector(s)}};
var input=$("#tool-input"), input2=$("#tool-input2"), output=$("#tool-output"), err=$("#tool-error"), btn=$("#tool-btn");
var aEl=$("#tool-a"), bEl=$("#tool-b"), cEl=$("#tool-c");
var dateA=$("#tool-date-a"), dateB=$("#tool-date-b");
var colorEl=$("#tool-color"), preview=$("#tool-preview"), canvas=$("#tool-canvas");
var wEl=$("#tool-w"), hEl=$("#tool-h"), qEl=$("#tool-q");
var patternEl=$("#tool-pattern"), flagsEl=$("#tool-flags"), algoEl=$("#tool-algo"), loremType=$("#tool-lorem-type"), loremCount=$("#tool-lorem-count");
var fileInput=input && input.type==="file" ? input : null;
function showErr(m){{if(!err) return; err.textContent=m; err.hidden=false; err.setAttribute("role","alert")}}
function clearErr(){{if(!err) return; err.textContent=""; err.hidden=true; err.removeAttribute("role")}}
function setOut(t){{if(output){{ output.value=t; output.textContent=t }} }}
function getVal(el){{return el?el.value:""}}
async function process(){{
 clearErr();
 try{{
   // Image tools
   if(cat==="Image Tools"){{
    var TK=window.ToolKit;
    var f=fileInput && fileInput.files[0];
    if(!f){{ showErr("Please select an image file (max 10MB)."); return; }}
    var v=TK.validateImageFile(f);
    if(!v.ok){{ showErr(v.error); return; }}
    var wv=parseInt(getVal(wEl),10), hv=parseInt(getVal(hEl),10), qv=parseFloat(getVal(qEl));
    if(getVal(qEl) && !(qv>=0.1 && qv<=1)){{ showErr("Quality must be between 0.1 and 1."); return; }}
    function showPrev(url){{ if(preview){{ preview.textContent=""; var im=document.createElement("img"); im.style.maxWidth="100%"; im.style.borderRadius="8px"; im.alt="Processed image preview"; im.src=url; preview.appendChild(im); }} window._lastImageDataURL=url; }}
    var meta=TK.imageMetadata(f);
    var info="Name: "+meta.name+"\\nType: "+meta.type+"\\nSize: "+meta.sizeKB+" KB";
    async function loadEl(){{
     var u=URL.createObjectURL(f);
     try{{ var im2=await TK.loadImage(u); return {{img:im2,url:u}}; }}catch(e){{ URL.revokeObjectURL(u); throw e; }}
    }}
    try{{
    if(slug==="image-resizer"){{ if(!wv&&!hv){{ showErr("Enter Width and/or Height in px."); return; }} var r=await TK.resizeImage(f,wv||undefined,hv||undefined,qv||0.85); showPrev(r); var im0=await TK.loadImage(r); setOut(info+"\\nWidth: "+im0.naturalWidth+" px\\nHeight: "+im0.naturalHeight+" px\\nResized successfully."); return; }}
    if(slug==="image-compressor"){{ var c=await TK.compressImage(f,qv||0.7); showPrev(c); setOut(info+"\\nCompressed (q="+(qv||0.7)+"). Use Download to save."); return; }}
    if(slug==="image-cropper"){{ if(!wv||!hv){{ showErr("Enter Width and Height for centered crop."); return; }} var L=await loadEl(); var iw=L.img.naturalWidth, ih=L.img.naturalHeight, cw=Math.min(wv,iw), ch=Math.min(hv,ih), sx=Math.max(0,Math.floor((iw-cw)/2)), sy=Math.max(0,Math.floor((ih-ch)/2)); URL.revokeObjectURL(L.url); var cr=await TK.cropImage(f,sx,sy,cw,ch); showPrev(cr); setOut(info+"\\nCropped: "+cw+"x"+ch+" (centered)."); return; }}
    if(slug==="jpg-to-png"||slug==="png-to-jpg"||slug==="webp-to-jpg"||slug==="jpg-to-webp"||slug==="png-to-webp"){{ var mime=slug.indexOf("to-png")>-1?"image/png":slug.indexOf("to-webp")>-1?"image/webp":"image/jpeg"; var Ld=await loadEl(); var cv2=document.createElement("canvas"); cv2.width=Ld.img.naturalWidth; cv2.height=Ld.img.naturalHeight; cv2.getContext("2d").drawImage(Ld.img,0,0); URL.revokeObjectURL(Ld.url); var out=cv2.toDataURL(mime,qv||0.92); showPrev(out); setOut(info+"\\nConverted to "+mime+". Use Download to save."); return; }}
    if(slug==="image-to-base64"){{ var b64=await TK.fileToBase64(f); window._lastImageDataURL=""; setOut(b64); return; }}
    if(slug==="base64-to-image"){{ var t0=getVal(input).trim(); if(!t0){{ showErr("Paste a Base64 data URL or raw Base64."); return; }} var src=t0.indexOf("data:")===0?t0:"data:image/png;base64,"+t0.replace(/\\s+/g,""); try{{ await TK.loadImage(src); }}catch(e){{ showErr("Invalid or corrupt Base64 image."); return; }} showPrev(src); setOut("Preview loaded. Use Download to save as PNG."); return; }}
    if(slug==="favicon-generator"){{ var fv=await TK.resizeImage(f,32,32,1); showPrev(fv); var fi=await TK.loadImage(fv); setOut(info+"\\nFavicon: "+fi.naturalWidth+"x"+fi.naturalHeight+" (32x32)."); return; }}
    if(slug==="app-icon-generator"){{ var ai=await TK.resizeImage(f,180,180,1); showPrev(ai); setOut(info+"\\nApp icon: 180x180."); return; }}
    if(slug==="social-media-image-resizer"||slug==="instagram-image-resizer"){{ var sm=await TK.resizeImage(f,1080,1080,qv||0.9); showPrev(sm); setOut(info+"\\nResized to 1080x1080."); return; }}
    if(slug==="youtube-thumbnail-resizer"){{ var yt=await TK.resizeImage(f,1280,720,qv||0.9); showPrev(yt); setOut(info+"\\nResized to 1280x720."); return; }}
    if(slug==="image-metadata-viewer"){{ var Md=await TK.loadImage(URL.createObjectURL(f)).catch(function(){{return null}}); var dims=""; if(Md&&Md.naturalWidth){{ dims="\\nWidth: "+Md.naturalWidth+" px\\nHeight: "+Md.naturalHeight+" px"; }} setOut(info+"\\nLast modified: "+(meta.lastModified||"n/a")+dims); window._lastImageDataURL=""; if(preview) preview.textContent=""; return; }}
    if(slug==="image-dimension-checker"){{ var u2=URL.createObjectURL(f); try{{ var dm=await TK.loadImage(u2); setOut("Width: "+dm.naturalWidth+" px\\nHeight: "+dm.naturalHeight+" px\\nAspect: "+(dm.naturalWidth/dm.naturalHeight).toFixed(3)); }}finally{{ URL.revokeObjectURL(u2); }} window._lastImageDataURL=""; if(preview) preview.textContent=""; return; }}
    if(slug==="image-aspect-ratio-calculator"){{ var u3=URL.createObjectURL(f); try{{ var ar2=await TK.loadImage(u3); var g=window.ToolKit.gcd(ar2.naturalWidth,ar2.naturalHeight); setOut(ar2.naturalWidth+"x"+ar2.naturalHeight+" → "+(ar2.naturalWidth/g)+":"+(ar2.naturalHeight/g)+" ("+(ar2.naturalWidth/ar2.naturalHeight).toFixed(3)+")"); }}finally{{ URL.revokeObjectURL(u3); }} window._lastImageDataURL=""; if(preview) preview.textContent=""; return; }}
    if(slug==="gif-frame-extractor"){{ var b6=await TK.fileToBase64(f); showPrev(b6); setOut(info+"\\nNote: browsers decode GIFs to a single frame — showing first-frame preview only. For full frame extraction use desktop software."); return; }}
    if(slug==="image-pixel-color-picker"){{ var u4=URL.createObjectURL(f); try{{ var pk=await TK.loadImage(u4); var cvp=document.createElement("canvas"); var sc=Math.min(1,800/pk.naturalWidth); cvp.width=Math.round(pk.naturalWidth*sc); cvp.height=Math.round(pk.naturalHeight*sc); var cx=cvp.getContext("2d"); cx.drawImage(pk,0,0,cvp.width,cvp.height); if(preview){{ preview.textContent=""; cvp.style.maxWidth="100%"; cvp.style.cursor="crosshair"; preview.appendChild(cvp); }} setOut("Click on the image to read the pixel color."); cvp.addEventListener("click",function(e){{ var r=cvp.getBoundingClientRect(), px=Math.floor((e.clientX-r.left)*cvp.width/r.width), py=Math.floor((e.clientY-r.top)*cvp.height/r.height); var d=cx.getImageData(px,py,1,1).data; var hx=TK.rgbToHex(d[0],d[1],d[2]); setOut("Pixel ("+px+","+py+"): "+hx+" rgb("+d[0]+","+d[1]+","+d[2]+")"); }}); }}finally{{ URL.revokeObjectURL(u4); }} return; }}
    }}catch(e){{ showErr(e.message||"Image processing failed (file may be corrupt or unsupported)."); return; }}
    var b64d=await TK.fileToBase64(f);
    showPrev(b64d);
    setOut(info+"\\n\\nLoaded successfully. Use Download to save processed image (if applicable).");
    return;
   }}
   // Color tools
   if(cat==="Color Tools"){{
    var TK2=window.ToolKit;
    function parseCol(s){{ s=String(s||"").trim(); var r=TK2.hexToRgb(s); if(r) return {{hex:TK2.rgbToHex(r.r,r.g,r.b),rgb:r}}; var m=s.match(/rgba?\\s*\\(\\s*(\\d+)\\s*,\\s*(\\d+)\\s*,\\s*(\\d+)/i); if(m){{ r={{r:+m[1],g:+m[2],b:+m[3]}}; return {{hex:TK2.rgbToHex(r.r,r.g,r.b),rgb:r}}; }} var mh=s.match(/hsl\\s*\\(\\s*(\\d+)\\s*,\\s*(\\d+)%?\\s*,\\s*(\\d+)%?/i); if(mh){{ r=TK2.hslToRgb(+mh[1],+mh[2],+mh[3]); return {{hex:TK2.rgbToHex(r.r,r.g,r.b),rgb:r}}; }} return null; }}
    function fmtCol(p){{ var h=TK2.rgbToHsl(p.rgb.r,p.rgb.g,p.rgb.b); return "HEX: "+p.hex+"\\nRGB: "+p.rgb.r+", "+p.rgb.g+", "+p.rgb.b+"\\nHSL: "+h.h+", "+h.s+"%, "+h.l+"%\\nName: "+TK2.colorName(p.hex); }}
    var raw=getVal(input).trim() || getVal(colorEl);
    if(slug==="color-palette-generator"){{ var b=parseCol(raw); if(!b){{ showErr("Enter a valid base color."); return; }} var ty=["complementary","analogous","triadic","complementary"]; setOut(ty.map(function(t){{return t+": "+TK2.palette(b.hex,t).join(", ")}}).join("\\n")); if(preview) preview.style.background=b.hex; return; }}
    if(slug==="random-color-generator"){{ var n=Math.floor(Math.random()*16777215).toString(16).padStart(6,"0"); var p2=parseCol("#"+n); setOut(fmtCol(p2)+"\\nContrast vs white: "+TK2.contrastRatio(p2.hex,"#ffffff")+":1"); if(preview) preview.style.background=p2.hex; return; }}
    if(slug==="gradient-generator"){{ var parts=raw.split(",").map(function(s){{return s.trim()}}).filter(Boolean); if(parts.length<2){{ showErr("Enter 2+ colors comma-separated."); return; }} setOut(TK2.buildGradient("linear",parts,90)); if(preview) preview.style.background=""; return; }}
    if(slug==="complementary-color-generator"||slug==="analogous-color-generator"||slug==="triadic-color-generator"){{ var bc=parseCol(raw); if(!bc){{ showErr("Enter a valid color."); return; }} var pt=slug.indexOf("complement")>-1?"complementary":slug.indexOf("analog")>-1?"analogous":"triadic"; setOut(pt+": "+TK2.palette(bc.hex,pt).join(", ")); if(preview) preview.style.background=bc.hex; return; }}
    if(slug==="contrast-checker"||slug==="wcag-contrast-checker"){{ var pp=raw.split(",").map(function(s){{return s.trim()}}); if(pp.length<2){{ showErr('Format: fg,bg — e.g. #000000,#ffffff'); return; }} var A=parseCol(pp[0]), B=parseCol(pp[1]); if(!A||!B){{ showErr("Enter two valid colors as fg,bg."); return; }} var ra=TK2.contrastRatio(A.hex,B.hex); setOut("Ratio: "+ra+":1\\nAA normal (4.5): "+(ra>=4.5?"PASS":"FAIL")+"\\nAA large (3): "+(ra>=3?"PASS":"FAIL")+"\\nAAA normal (7): "+(ra>=7?"PASS":"FAIL")+"\\nAAA large (4.5): "+(ra>=4.5?"PASS":"FAIL")); return; }}
    if(slug==="color-blindness-simulator"){{ var sb=parseCol(raw); if(!sb){{ showErr("Enter a valid HEX color."); return; }} setOut("Original: "+sb.hex+"\\nProtanopia: "+TK2.simulateColorBlind(sb.hex,"protanopia")+"\\nDeuteranopia: "+TK2.simulateColorBlind(sb.hex,"deuteranopia")+"\\nTritanopia: "+TK2.simulateColorBlind(sb.hex,"tritanopia")); if(preview) preview.style.background=sb.hex; return; }}
    if(slug==="rgb-color-mixer"){{ var np=raw.split(",").map(Number); if(np.length<6||np.some(function(x){{return !isFinite(x)}})){{ showErr('Format: r1,g1,b1,r2,g2,b2 — e.g. 255,0,0,0,0,255'); return; }} var mx=[Math.round((np[0]+np[3])/2),Math.round((np[1]+np[4])/2),Math.round((np[2]+np[5])/2)]; setOut("Mixed: "+TK2.rgbToHex(mx[0],mx[1],mx[2])+" rgb("+mx.join(",")+")"); if(preview) preview.style.background=TK2.rgbToHex(mx[0],mx[1],mx[2]); return; }}
    if(slug==="tailwind-color-converter"||slug==="material-color-converter"||slug==="color-name-finder"||slug==="css-color-generator"){{ var cb=parseCol(raw); if(!cb){{ showErr("Enter a valid HEX / RGB / HSL color."); return; }} setOut(fmtCol(cb)+" (nearest family: "+TK2.colorName(cb.hex)+")"); if(preview) preview.style.background=cb.hex; return; }}
    if(slug==="hex-to-rgb"||slug==="rgb-to-hex"||slug==="rgb-to-hsl"||slug==="hsl-to-rgb"||slug==="hex-to-hsl"||slug==="css-color-converter"){{ var cc2=parseCol(raw||getVal(colorEl)); if(!cc2){{ showErr("Enter HEX e.g. #2563eb or rgb(37,99,235)"); return; }} var hh=TK2.rgbToHsl(cc2.rgb.r,cc2.rgb.g,cc2.rgb.b); setOut("HEX: "+cc2.hex+"\\nRGB: "+cc2.rgb.r+", "+cc2.rgb.g+", "+cc2.rgb.b+"\\nHSL: "+hh.h+", "+hh.s+"%, "+hh.l+"%\\nName: "+TK2.colorName(cc2.hex)); if(preview) preview.style.background=cc2.hex; return; }}
    var hex=raw;
    var rgb=TK2.hexToRgb(hex);
    if(!rgb){{ // try rgb input like rgb(...)
      var m=hex.match(/rgb\\s*\\(\\s*(\\d+)\\s*,\\s*(\\d+)\\s*,\\s*(\\d+)\\s*\\)/i);
      if(m){{ rgb={{r:+m[1],g:+m[2],b:+m[3]}}; hex=TK2.rgbToHex(rgb.r,rgb.g,rgb.b); }}
    }}
    if(!rgb){{ showErr("Enter valid HEX e.g. #2563eb or rgb(37,99,235)"); return; }}
    var hsl=TK2.rgbToHsl(rgb.r,rgb.g,rgb.b);
    var out="HEX: "+TK2.rgbToHex(rgb.r,rgb.g,rgb.b)+"\\nRGB: "+rgb.r+", "+rgb.g+", "+rgb.b+"\\nHSL: "+hsl.h+", "+hsl.s+"%, "+hsl.l+"%\\nName: "+TK2.colorName(hex)+"\\nContrast vs white: "+TK2.contrastRatio(hex,"#ffffff")+":1";
    if(preview) preview.style.background=hex;
    setOut(out);
    return;
   }}
  // Date & Time
  if(cat==="Date & Time"){{
   var d1=getVal(dateA)||getVal(input), d2=getVal(dateB);
   if(!d1){{ showErr("Please enter a date."); return; }}
   if(slug==="age-calculator"){{
     var ag=window.ToolKit.age(d1);
     if(ag&&typeof ag==="object"){{ setOut(ag.years+" years, "+ag.months+" months, "+ag.days+" days ("+ag.totalDays+" days total)"); return; }}
     if(typeof ag!=="number"||isNaN(ag)){{ showErr("Invalid date."); return; }}
     var _b=new Date(d1), _n=new Date(), _td=Math.floor(Math.abs(_n-_b)/86400000);
     var _y=ag, _m=_n.getMonth()-_b.getMonth()+(_n.getDate()<_b.getDate()?-1:0); if(_m<0)_m+=12;
     var _dm=new Date(_n.getFullYear(),_n.getMonth(),0).getDate()||30, _d=(_n.getDate()-_b.getDate()+_dm)%_dm;
     setOut(_y+" years, "+_m+" months, "+_d+" days ("+_td+" days total)"); return;
    }}
   if(slug==="leap-year-checker"){{ var y=new Date(d1).getFullYear()||Number(d1); var is=window.ToolKit.isLeap(y); setOut(y+" is "+(is?"a leap year":"not a leap year")); return; }}
   if(slug==="day-of-week-calculator"){{ setOut(window.ToolKit.dayOfWeek(d1)||"Invalid date"); return; }}
   if(slug==="week-number-calculator"){{ setOut("Week: "+window.ToolKit.weekNumber(d1)); return; }}
   if(slug.includes("business")||slug.includes("working")){{ if(!d2){{ showErr("Enter both dates"); return;}} setOut("Business days: "+window.ToolKit.businessDays(d1,d2)); return; }}
   if(d1 && d2){{ var diff=window.ToolKit.dateDiff(d1,d2,"days"); if(isNaN(diff)){{ showErr("Invalid dates"); return;}} setOut("Days: "+diff.toFixed(2)+"\\nHours: "+(diff*24).toFixed(1)+"\\n"+window.ToolKit.duration(Math.abs(new Date(d2)-new Date(d1)))); return; }}
   if(slug==="unix-timestamp-generator"){{ var ts=window.ToolKit.toTimestamp(d1,false); setOut("Timestamp: "+ts+"\\nISO: "+window.ToolKit.fromTimestamp(ts,false)); return; }}
    if(slug==="weeks-between-dates"){{ var dw=window.ToolKit.dateDiff(d1,d2||d1,"days"); if(isNaN(dw)){{ showErr("Invalid dates"); return;}} setOut((dw/7).toFixed(2)+" weeks ("+dw.toFixed(1)+" days)"); return; }}
    if(slug==="months-between-dates"){{ var dm2=window.ToolKit.dateDiff(d1,d2||d1,"days"); if(isNaN(dm2)){{ showErr("Invalid dates"); return;}} setOut((dm2/30.44).toFixed(2)+" months ("+dm2.toFixed(1)+" days)"); return; }}
    if(slug==="days-until-date"){{ var tvd=getVal(input)||d1; var today=new Date().toISOString().slice(0,10); var du=window.ToolKit.dateDiff(today,tvd,"days"); if(isNaN(du)){{ showErr("Enter date as YYYY-MM-DD."); return;}} setOut(Math.round(du)+" days"); return; }}
    if(slug==="date-addition-calculator"){{ if(!d1){{ showErr("Enter a start date."); return; }} var addN=Number(getVal(input).trim()); if(!isFinite(addN)){{ showErr("Enter days to add in the text field (number)."); return; }} setOut(window.ToolKit.addDays(d1,addN)); return; }}
    if(slug==="date-subtraction-calculator"){{ if(!d1){{ showErr("Enter a start date."); return; }} var subN=Number(getVal(input).trim()); if(!isFinite(subN)){{ showErr("Enter days to subtract in the text field (number)."); return; }} setOut(window.ToolKit.addDays(d1,-subN)); return; }}
    if(slug==="time-difference-calculator"||slug==="time-duration-calculator"){{ var tp=(getVal(input)||"").split(",").map(function(s){{return s.trim()}}); if(tp.length<2||!/^\\d{1,2}:\\d{2}$/.test(tp[0])||!/^\\d{1,2}:\\d{2}$/.test(tp[1])){{ showErr('Format: HH:MM,HH:MM — e.g. 09:00,17:30'); return; }} var p1=tp[0].split(":"), p2=tp[1].split(":"); var ms=Math.abs((+p2[0]*60+ +p2[1])-(+p1[0]*60+ +p1[1]))*60000; setOut(window.ToolKit.duration(ms)+" ("+(ms/3600000).toFixed(2)+" hours)"); return; }}
    if(slug==="hours-to-minutes-converter"){{ var hv2=Number((getVal(input)||"").trim()); if(!isFinite(hv2)||getVal(input).trim()===""){{ showErr("Enter hours in the text field."); return; }} setOut(hv2+"h = "+(hv2*60)+" min"); return; }}
    if(slug==="minutes-to-seconds-converter"){{ var mv=Number((getVal(input)||"").trim()); if(!isFinite(mv)||getVal(input).trim()===""){{ showErr("Enter minutes in the text field."); return; }} setOut(mv+" min = "+(mv*60)+" sec"); return; }}
    if(slug==="seconds-to-hours-converter"){{ var sv=Number((getVal(input)||"").trim()); if(!isFinite(sv)||getVal(input).trim()===""){{ showErr("Enter seconds in the text field."); return; }} setOut(sv+" sec = "+(sv/3600).toFixed(4)+" h"); return; }}
    if(slug==="date-format-converter"){{ var tvf=getVal(input).trim()||d1; var df=new Date(tvf); if(isNaN(df)){{ showErr("Enter a valid date."); return; }} var iso=df.toISOString().slice(0,10); setOut("ISO: "+iso+"\\nUS: "+(df.getMonth()+1)+"/"+df.getDate()+"/"+df.getFullYear()+"\\nUK: "+String(df.getDate()).padStart(2,"0")+"/"+String(df.getMonth()+1).padStart(2,"0")+"/"+df.getFullYear()); return; }}
   // generic date
   var diff2=window.ToolKit.dateDiff(d1,d2||new Date().toISOString(),"days"); setOut(isNaN(diff2)? new Date(d1).toString() : "Difference: "+diff2.toFixed(2)+" days");
   return;
  }}
  // Math / Finance / Business / Student numeric
  if(["Math Calculators","Finance Calculators","Business Calculators","Student Tools"].includes(cat)){{
   var av=getVal(aEl), bv=getVal(bEl), cv=getVal(cEl), tv=getVal(input);
   var an=Number(av), bn=Number(bv);
   // specific slugs
   if(slug==="percentage-calculator"){{ if(!av||!bv){{ showErr("Enter value and percentage."); return;}} setOut(window.ToolKit.pct(an,bn)+" ("+bn+"% of "+an+")"); return; }}
   if(slug==="percentage-increase-calculator"){{ setOut(window.ToolKit.pctChange(an,bn).toFixed(2)+"%"); return; }}
   if(slug==="percentage-decrease-calculator"){{ setOut(window.ToolKit.pctChange(an,bn).toFixed(2)+"%"); return; }}
   if(slug==="ratio-calculator"){{ setOut(window.ToolKit.ratio(an,bn)); return; }}
   if(slug==="gcd-calculator"){{ setOut(String(window.ToolKit.gcd(an,bn))); return; }}
   if(slug==="lcm-calculator"){{ setOut(String(window.ToolKit.lcm(an,bn))); return; }}
   if(slug==="prime-number-checker"){{ setOut(window.ToolKit.isPrime(an)? an+" is prime":"not prime"); return; }}
   if(slug==="factor-calculator"){{ setOut(window.ToolKit.factors(an).join(", ")); return; }}
   if(slug==="binary-to-decimal"){{ var n=parseInt(tv||av,2); setOut(isNaN(n)?"Invalid binary":String(n)); return; }}
   if(slug==="decimal-to-binary"){{ setOut(window.ToolKit.toBinary(tv||av)); return; }}
   if(slug==="hex-to-decimal"){{ setOut(String(parseInt(tv||av,16))); return; }}
   if(slug==="decimal-to-hex"){{ setOut(window.ToolKit.toHex(tv||av)); return; }}
   if(slug==="octal-converter"){{ setOut(window.ToolKit.toOctal(tv||av)); return; }}
   if(slug==="roman-numeral-converter"){{ setOut(window.ToolKit.toRoman(tv||av)||"Enter 1-3999"); return; }}
   if(slug==="exponent-calculator"){{ setOut(String(window.ToolKit.pow(an,bn))); return; }}
   if(slug==="square-root-calculator"){{ setOut(String(window.ToolKit.sqrt(an||tv))); return; }}
   if(slug==="average-calculator"||slug==="mean-calculator"){{ var arr=(tv||av+","+bv).split(/[ ,]+/).map(Number); setOut(String(window.ToolKit.mean(arr))); return; }}
   if(slug==="median-calculator"){{ var ar=(tv||av+","+bv).split(/[ ,]+/).map(Number); setOut(String(window.ToolKit.median(ar))); return; }}
   if(slug==="standard-deviation-calculator"){{ var arr2=(tv||av+","+bv).split(/[ ,]+/).map(Number); setOut(String(window.ToolKit.stddev(arr2,false).toFixed(4))); return; }}
   if(slug==="factorial-calculator"){{ setOut(String(window.ToolKit.factorial(tv||av))); return; }}
   if(slug==="simple-interest-calculator"){{ setOut("Interest: "+window.ToolKit.simpleInterest(av,bv,cv)); return; }}
   if(slug==="compound-interest-calculator"){{ setOut("Interest: "+window.ToolKit.compoundInterest(av,bv,12,cv).toFixed(2)); return; }}
   if(slug==="loan-emi-calculator"||slug==="mortgage-calculator"){{ setOut("EMI: "+window.ToolKit.emi(av,bv,cv).toFixed(2)); return; }}
   if(slug==="cagr-calculator"){{ setOut(window.ToolKit.cagr(av,bv,cv).toFixed(2)+"%"); return; }}
   if(slug==="sip-calculator"){{ setOut(window.ToolKit.sip(av,bv,cv).toFixed(2)); return; }}
   if(slug==="grade-calculator"){{ var g=window.ToolKit.grade(an,bn||100); setOut(g.pct+"% Grade "+g.letter); return; }}
   if(slug==="scientific-calculator"||slug==="equation-solver"){{ var r=window.ToolKit.safeEval(tv||av); if(!r.ok){{ showErr(r.error); return;}} setOut(String(r.result)); return; }}
    var TK3=window.ToolKit;
    if(slug==="profit-calculator"){{ if(!isFinite(an)||!isFinite(bn)){{ showErr("Enter revenue (A) and cost (B)."); return; }} var pf=an-bn; setOut("Profit: "+pf.toFixed(2)+"\\nMargin: "+(an?((pf/an*100).toFixed(2)+"%"):"n/a")); return; }}
    if(slug==="revenue-calculator"){{ if(!isFinite(an)||!isFinite(bn)){{ showErr("Enter units (A) and price (B)."); return; }} setOut("Revenue: "+(an*bn).toFixed(2)); return; }}
    if(slug==="roi-calculator"){{ if(!isFinite(an)||!isFinite(bn)){{ showErr("Enter gain (A) and cost (B)."); return; }} var ri=TK3.roi(an,bn); if(!isFinite(ri)){{ showErr("Cost must not be zero."); return; }} setOut(ri.toFixed(2)+"%"); return; }}
    if(slug==="roas-calculator"){{ if(!isFinite(an)||!isFinite(bn)){{ showErr("Enter revenue (A) and spend (B)."); return; }} var ra2=TK3.roas(an,bn); if(!isFinite(ra2)){{ showErr("Spend must not be zero."); return; }} setOut(ra2.toFixed(2)+"x"); return; }}
    if(slug==="conversion-rate-calculator"){{ if(!isFinite(an)||!isFinite(bn)){{ showErr("Enter conversions (A) and visitors (B)."); return; }} var cr2=TK3.conversionRate(an,bn); if(!isFinite(cr2)){{ showErr("Visitors must not be zero."); return; }} setOut(cr2.toFixed(2)+"%"); return; }}
    if(slug==="ctr-calculator"){{ if(!isFinite(an)||!isFinite(bn)){{ showErr("Enter clicks (A) and impressions (B)."); return; }} var ct=TK3.ctr(an,bn); if(!isFinite(ct)){{ showErr("Impressions must not be zero."); return; }} setOut(ct.toFixed(2)+"%"); return; }}
    if(slug==="cpm-calculator"){{ if(!isFinite(an)||!isFinite(bn)){{ showErr("Enter spend (A) and impressions (B)."); return; }} var cp=TK3.cpm(an,bn); if(!isFinite(cp)){{ showErr("Impressions must not be zero."); return; }} setOut(cp.toFixed(2)); return; }}
    if(slug==="cpc-calculator"){{ if(!isFinite(an)||!isFinite(bn)){{ showErr("Enter spend (A) and clicks (B)."); return; }} var cc3=TK3.cpc(an,bn); if(!isFinite(cc3)){{ showErr("Clicks must not be zero."); return; }} setOut(cc3.toFixed(2)); return; }}
    if(slug==="customer-acquisition-cost-calculator"){{ if(!isFinite(an)||!isFinite(bn)){{ showErr("Enter spend (A) and customers (B)."); return; }} var ca=TK3.cac(an,bn); if(!isFinite(ca)){{ showErr("Customers must not be zero."); return; }} setOut(ca.toFixed(2)); return; }}
    if(slug==="customer-lifetime-value-calculator"){{ var cn3=Number(cv); if(!isFinite(an)||!isFinite(bn)||!isFinite(cn3)){{ showErr("Enter avg value (A), frequency (B), lifespan (C)."); return; }} setOut(TK3.clv(an,bn,cn3).toFixed(2)); return; }}
    if(slug==="churn-rate-calculator"){{ if(!isFinite(an)||!isFinite(bn)){{ showErr("Enter lost (A) and start (B)."); return; }} var ch=TK3.churn(an,bn); if(!isFinite(ch)){{ showErr("Start must not be zero."); return; }} setOut(ch.toFixed(2)+"%"); return; }}
    if(slug==="growth-rate-calculator"){{ if(!isFinite(an)||!isFinite(bn)){{ showErr("Enter old value (A) and new value (B)."); return; }} var gr=TK3.growthRate(an,bn); if(!isFinite(gr)){{ showErr("Old value must not be zero."); return; }} setOut(gr.toFixed(2)+"%"); return; }}
    if(slug==="gross-margin-calculator"){{ if(!isFinite(an)||!isFinite(bn)){{ showErr("Enter revenue (A) and COGS (B)."); return; }} var gm=(an-bn)/an*100; if(!isFinite(gm)){{ showErr("Revenue must not be zero."); return; }} setOut("Gross profit: "+(an-bn).toFixed(2)+"\\nMargin: "+gm.toFixed(2)+"%"); return; }}
    if(slug==="net-margin-calculator"){{ if(!isFinite(an)||!isFinite(bn)){{ showErr("Enter revenue (A) and costs (B)."); return; }} var nm=(an-bn)/an*100; if(!isFinite(nm)){{ showErr("Revenue must not be zero."); return; }} setOut("Net: "+(an-bn).toFixed(2)+"\\nMargin: "+nm.toFixed(2)+"%"); return; }}
    if(slug==="markup-vs-margin-calculator"){{ if(!isFinite(an)||!isFinite(bn)){{ showErr("Enter cost (A) and price (B)."); return; }} var mm=TK3.markupVsMargin(an,bn); setOut("Markup: "+mm.markup.toFixed(2)+"%\\nMargin: "+mm.margin.toFixed(2)+"%"); return; }}
    if(slug==="inventory-turnover-calculator"){{ if(!isFinite(an)||!isFinite(bn)){{ showErr("Enter COGS (A) and avg inventory (B)."); return; }} var to=TK3.turnover(an,bn); if(!isFinite(to)){{ showErr("Inventory must not be zero."); return; }} setOut(to.toFixed(2)+"x"); return; }}
    if(slug==="sales-commission-calculator"){{ if(!isFinite(an)||!isFinite(bn)){{ showErr("Enter sales (A) and rate % (B)."); return; }} setOut(TK3.commission(an,bn).toFixed(2)); return; }}
    if(slug==="break-even-units-calculator"){{ var vc=Number(cv); if(!isFinite(an)||!isFinite(bn)||!isFinite(vc)){{ showErr("Enter fixed (A), price (B), variable (C)."); return; }} var be=TK3.breakEven(an,bn,vc); if(!isFinite(be)){{ showErr("Price must exceed variable cost."); return; }} setOut(Math.ceil(be)+" units"); return; }}
    if(slug==="saas-pricing-calculator"){{ var mc=Number(cv)||20; if(!isFinite(an)||!isFinite(bn)||!bn){{ showErr("Enter costs (A) and customers (B)."); return; }} setOut(((an/bn)*(1+mc/100)).toFixed(2)+" / customer"); return; }}
    if(slug==="freelance-hourly-rate-calculator"){{ if(!isFinite(an)||!isFinite(bn)||!bn){{ showErr("Enter annual income (A) and hours (B)."); return; }} setOut(TK3.freelanceRate(an,bn).toFixed(2)+" / hour"); return; }}
    if(slug==="discount-calculator"){{ if(!isFinite(an)||!isFinite(bn)){{ showErr("Enter price (A) and % off (B)."); return; }} var sa=TK3.discount(an,bn); setOut("Sale: "+sa.toFixed(2)+"\\nSavings: "+(an-sa).toFixed(2)); return; }}
    if(slug==="sale-price-calculator"){{ if(!isFinite(an)||!isFinite(bn)){{ showErr("Enter original (A) and amount off (B)."); return; }} setOut("Sale: "+(an-bn).toFixed(2)); return; }}
    if(slug==="markup-calculator"){{ if(!isFinite(an)||!isFinite(bn)){{ showErr("Enter cost (A) and markup % (B)."); return; }} setOut(TK3.markup(an,bn).toFixed(2)); return; }}
    if(slug==="profit-margin-calculator"){{ if(!isFinite(an)||!isFinite(bn)){{ showErr("Enter revenue (A) and cost (B)."); return; }} var pm=TK3.profitMargin(an,bn); if(!isFinite(pm)){{ showErr("Revenue must not be zero."); return; }} setOut(pm.toFixed(2)+"%"); return; }}
    if(slug==="break-even-calculator"){{ var vc2=Number(cv); if(!isFinite(an)||!isFinite(bn)||!isFinite(vc2)){{ showErr("Enter fixed (A), price (B), variable (C)."); return; }} var be2=TK3.breakEven(an,bn,vc2); if(!isFinite(be2)){{ showErr("Price must exceed variable cost."); return; }} setOut(be2.toFixed(2)+" units"); return; }}
    if(slug==="tip-calculator"){{ var tp3=Number(bv)||15, pp=Math.max(1,Number(cv)||1); if(!isFinite(an)){{ showErr("Enter bill amount (A)."); return; }} var t4=TK3.tip(an,tp3,pp); setOut("Tip: "+t4.tip.toFixed(2)+"\\nTotal: "+t4.total.toFixed(2)+"\\nEach ("+pp+"): "+t4.perPerson.toFixed(2)); return; }}
    if(slug==="split-bill-calculator"){{ var sp=Math.max(2,Number(bv)||2); if(!isFinite(an)){{ showErr("Enter total (A)."); return; }} setOut((an/sp).toFixed(2)+" each ("+sp+" people)"); return; }}
    if(slug==="salary-calculator"){{ if(!isFinite(an)){{ showErr("Enter annual salary (A)."); return; }} setOut("Monthly: "+(an/12).toFixed(2)+"\\nWeekly: "+(an/52).toFixed(2)+"\\nHourly: "+(an/2080).toFixed(2)); return; }}
    if(slug==="hourly-to-yearly-salary"){{ var hb=Number(bv)||40; if(!isFinite(an)){{ showErr("Enter hourly rate (A)."); return; }} setOut("Yearly: "+(an*hb*52).toFixed(2)); return; }}
    if(slug==="yearly-to-hourly-salary"){{ var yb=Number(bv)||40; if(!isFinite(an)){{ showErr("Enter annual salary (A)."); return; }} setOut("Hourly: "+(an/(yb*52)).toFixed(2)); return; }}
    if(slug==="tax-percentage-calculator"){{ if(!isFinite(an)||!isFinite(bn)){{ showErr("Enter income (A) and tax paid (B)."); return; }} setOut((bn/an*100).toFixed(2)+"%"); return; }}
    if(slug==="budget-calculator"){{ if(!isFinite(an)||!isFinite(bn)){{ showErr("Enter income (A) and expenses (B)."); return; }} var rem=an-bn; setOut("Remaining: "+rem.toFixed(2)+"\\nSavings: "+(an?(rem/an*100).toFixed(2)+"%":"n/a")); return; }}
    if(slug==="net-worth-calculator"){{ if(!isFinite(an)||!isFinite(bn)){{ showErr("Enter assets (A) and liabilities (B)."); return; }} setOut(TK3.netWorth(an,bn).toFixed(2)); return; }}
    if(slug==="loan-payment-calculator"){{ var nc=Number(cv); if(!isFinite(an)||!isFinite(bn)||!isFinite(nc)){{ showErr("Enter principal (A), rate % (B), months (C)."); return; }} setOut("Payment: "+TK3.emi(an,bn,nc).toFixed(2)); return; }}
    if(slug==="loan-interest-calculator"){{ var nc2=Number(cv); if(!isFinite(an)||!isFinite(bn)||!isFinite(nc2)){{ showErr("Enter principal (A), rate % (B), months (C)."); return; }} var em=TK3.emi(an,bn,nc2); setOut("EMI: "+em.toFixed(2)+"\\nTotal interest: "+(em*nc2-an).toFixed(2)); return; }}
    if(slug==="investment-return-calculator"){{ if(!isFinite(an)||!isFinite(bn)){{ showErr("Enter initial (A) and final (B)."); return; }} setOut(((bn-an)/Math.abs(an)*100).toFixed(2)+"% (gain "+(bn-an).toFixed(2)+")"); return; }}
    if(slug==="inflation-calculator"){{ var yc=Number(cv); if(!isFinite(an)||!isFinite(bn)||!isFinite(yc)){{ showErr("Enter amount (A), rate % (B), years (C)."); return; }} setOut(TK3.inflation(an,bn,yc).toFixed(2)); return; }}
    if(slug==="savings-goal-calculator"){{ if(!isFinite(an)||!isFinite(bn)||!bn){{ showErr("Enter goal (A) and months (B)."); return; }} setOut((an/bn).toFixed(2)+" / month"); return; }}
    if(slug==="retirement-calculator"){{ if(!isFinite(an)){{ showErr("Enter annual expenses (A)."); return; }} setOut("Need: "+(an*25).toFixed(2)+" (4% rule: 25x annual expenses)"); return; }}
    if(slug==="proportion-calculator"){{ var pts=(tv||av+","+bv+","+cv).split(/[,\\s]+/).filter(function(s){{return s!==""}}); if(pts.length<3||!isFinite(Number(pts[0]))||!isFinite(Number(pts[1]))||!isFinite(Number(pts[2]))){{ showErr("Enter three values a,b,c (a/b = c/x)."); return; }} var pv=TK3.solveProportion(pts[0],pts[1],pts[2]); if(!isFinite(pv)){{ showErr("First value (a) must not be zero."); return; }} setOut("x = "+pv); return; }}
    if(slug==="mode-calculator"){{ var ml=(tv||av+","+bv+","+cv).split(/[,\\s]+/).filter(function(s){{return s!==""}}).map(Number).filter(isFinite); if(!ml.length){{ showErr("Enter numbers comma-separated."); return; }} setOut(TK3.mode(ml).join(", ")); return; }}
    if(slug==="decimal-to-fraction"){{ var dv=tv||av; if(dv===""||!isFinite(Number(dv))){{ showErr("Enter a decimal number."); return; }} setOut(TK3.toFraction(dv)); return; }}
    if(slug==="fraction-to-decimal"){{ var fv=String(tv||av||"").trim(); if(!fv){{ showErr("Format: a/b — e.g. 3/4"); return; }} var fd=TK3.fractionToDecimal(fv); if(!isFinite(fd)){{ showErr("Format: a/b — e.g. 3/4"); return; }} setOut(String(fd)); return; }}
    if(slug==="mixed-number-calculator"){{ var mv2=String(tv||av||"").trim(); if(!mv2){{ showErr("Enter a fraction (a/b) or decimal."); return; }} if(mv2.indexOf("/")>-1){{ var dec=TK3.fractionToDecimal(mv2); if(!isFinite(dec)){{ showErr("Invalid fraction."); return; }} setOut(TK3.toMixed(dec)+" ("+dec+")"); return; }} if(!isFinite(Number(mv2))){{ showErr("Enter a fraction (a/b) or decimal."); return; }} setOut(TK3.toFraction(mv2)); return; }}
    if(slug==="prime-number-generator"){{ var pn=Math.floor(Number(av)||100); if(pn<2){{ showErr("Enter n ≥ 2."); return; }} setOut(TK3.primesUpTo(pn).join(", ")); return; }}
    if(slug==="random-number-generator"){{ var rmn=isFinite(Number(av))?Number(av):1, rmx=isFinite(Number(bv))?Number(bv):100; var ri2=TK3.randomInt(rmn,rmx); if(!isFinite(ri2)){{ showErr("Min must be ≤ max."); return; }} setOut(String(ri2)); return; }}
    if(slug==="scientific-notation-converter"){{ var snv=String(tv||av||"").trim(); if(!snv){{ showErr("Enter a number."); return; }} if(/[eE]/.test(snv)){{ var ex=TK3.fromScientific(snv); if(!isFinite(ex)){{ showErr("Invalid scientific notation."); return; }} setOut(String(ex)); return; }} if(!isFinite(Number(snv))){{ showErr("Enter a number."); return; }} setOut(TK3.toScientific(snv)); return; }}
    if(slug==="gpa-calculator"){{ var sc=Number(cv)||4; if(!tv.trim()){{ showErr("Enter grades comma-separated (e.g. A,B,C)."); return; }} var gp=TK3.gpa(tv,sc); if(!isFinite(gp)){{ showErr("No valid grades found."); return; }} setOut(String(gp)); return; }}
    if(slug==="cgpa-calculator"){{ if(!tv.trim()){{ showErr("Enter semesters comma-separated."); return; }} var cg=TK3.cgpa(tv.split(",").map(Number)); if(!isFinite(cg)){{ showErr("No valid numbers found."); return; }} setOut(cg.toFixed(2)); return; }}
    if(slug==="percentage-to-gpa-calculator"){{ if(!isFinite(an)){{ showErr("Enter percentage (A)."); return; }} setOut((an/100*4).toFixed(2)); return; }}
    if(slug==="exam-percentage-calculator"||slug==="marks-percentage-calculator"){{ if(!isFinite(an)||!isFinite(bn)||!bn){{ showErr("Enter obtained (A) and total (B)."); return; }} setOut((an/bn*100).toFixed(2)+"%"); return; }}
    if(slug==="final-grade-calculator"){{ if(!isFinite(an)||!isFinite(Number(bv))||!isFinite(Number(cv))){{ showErr("Enter current (A), final weight % (B), target (C)."); return; }} var fg=TK3.finalGradeNeeded(an,Number(bv),Number(cv)); if(!isFinite(fg)){{ showErr("Weight must be between 0 and 100."); return; }} setOut(fg.toFixed(2)+" needed on final"); return; }}
    if(slug==="weighted-grade-calculator"){{ var ss=tv.split(",").map(Number), ws=String(cv||"").split(",").map(Number); if(!tv.trim()||!String(cv||"").trim()){{ showErr("Enter scores in text (a,b,..) and weights in C (w1,w2,..)."); return; }} var wg=TK3.weightedGrade(ss,ws); if(!isFinite(wg)){{ showErr("Scores/weights must match in count and be numeric."); return; }} setOut(wg.toFixed(2)); return; }}
    if(slug==="study-time-calculator"){{ if(!isFinite(an)||!isFinite(bn)){{ showErr("Enter topics (A) and hours each (B)."); return; }} setOut((an*bn).toFixed(1)+" hours total"); return; }}
    if(slug==="pomodoro-timer"){{ var ses=Math.max(1,Math.floor(Number(av)||4)); setOut(ses+" sessions: 25m focus + 5m break each, long break 15m every 4 ("+(ses*25)+"m focus total)"); return; }}
    if(slug==="exam-countdown"||slug==="assignment-countdown"||slug==="semester-countdown"){{ var dtv=tv.trim(); if(!/^\\d{4}-\\d{2}-\\d{2}$/.test(dtv)){{ showErr("Enter date as YYYY-MM-DD in the text field."); return; }} var today2=new Date().toISOString().slice(0,10); var dd=TK3.dateDiff(today2,dtv,"days"); if(isNaN(dd)){{ showErr("Invalid date."); return; }} setOut(Math.round(dd)+" days"); return; }}
    if(slug==="study-schedule-generator"||slug==="revision-schedule-generator"){{ var subs=tv.split(",").map(function(s){{return s.trim()}}).filter(Boolean); if(!subs.length||!isFinite(an)||!an){{ showErr("Enter subjects comma-separated and hours (A)."); return; }} var per=an/subs.length; setOut(subs.map(function(s){{return s+": "+per.toFixed(1)+"h"}}).join("\\n")); return; }}
    if(slug==="flashcard-generator"){{ var lines=tv.split("\\n").map(function(s){{return s.trim()}}).filter(Boolean); if(!lines.length||lines.every(function(l){{return l.indexOf("|")<0}})){{ showErr("One card per line as Question|Answer"); return; }} setOut(lines.length+" cards:\\n"+lines.map(function(l,i){{ var p=l.split("|"); return (i+1)+". Q: "+(p[0]||"").trim()+" → A: "+(p[1]||"").trim()}}).join("\\n")); return; }}
    if(slug==="multiplication-table-generator"){{ var nn=Math.floor(Number(av)||5), up=Math.floor(Number(bv)||10); if(nn<1||up<1){{ showErr("Enter n (A) and up-to (B)."); return; }} var o=[]; for(var k=1;k<=up;k++) o.push(nn+" × "+k+" = "+(nn*k)); setOut(o.join("\\n")); return; }}
    if(slug==="times-table-quiz"||slug==="random-math-quiz"){{ var qn=Math.floor(Number(av)||5); var x1=TK3.randomInt(2,12), x2=TK3.randomInt(2,12); setOut("Q: "+qn+" × "+x1+" = ?\\nA: "+(qn*x1)+" (also try "+x2+" + "+qn+" = "+(x2+qn)+")"); return; }}
    if(slug==="unit-conversion-calculator"){{ var up3=tv.split(",").map(function(s){{return s.trim()}}); if(up3.length<3){{ showErr("Format: value,from,to — e.g. 10,km,mi"); return; }} var val=Number(up3[0]), fr2=up3[1].toLowerCase(), to2=up3[2].toLowerCase(); var rr=TK3.convertLength(val,fr2,to2); if(!isFinite(rr)) rr=TK3.convertWeight(val,fr2,to2); if(!isFinite(rr)) rr=TK3.convertTemp(val,fr2[0],to2[0]); if(!isFinite(rr)){{ showErr("Unsupported units. Length (mm,cm,m,km,inch,ft,yd,mile), weight (mg,g,kg,lb,oz), temp (c,f,k)."); return; }} setOut(val+" "+fr2+" = "+rr+" "+to2); return; }}
   // generic fallback numeric
   if(tv){{ var ev=window.ToolKit.safeEval(tv); if(ev.ok){{ setOut(String(ev.result)); return;}} }}
   if(isFinite(an) && isFinite(bn)){{ setOut("Result A: "+an+" B: "+bn+"\\nSum: "+(an+bn)+"\\nAvg: "+window.ToolKit.mean([an,bn])); return; }}
   showErr("Enter numbers to calculate."); return;
  }}
  // Dev / Text
  var txt=getVal(input);
  if(slug==="json-formatter"){{ if(!txt.trim()){{ showErr("Paste JSON to format."); return;}} var p=window.ToolKit.safeJSONParse(txt); if(!p.ok){{ showErr(p.error); return;}} setOut(JSON.stringify(p.data,null,2)); return; }}
  if(slug==="json-validator"){{ var pr=window.ToolKit.safeJSONParse(txt); setOut(pr.ok?"Valid JSON\\n"+JSON.stringify(pr.data,null,2): "Invalid: "+pr.error); if(!pr.ok) showErr(pr.error); return; }}
  if(slug==="json-minifier"){{ var pj=window.ToolKit.safeJSONParse(txt); if(!pj.ok){{ showErr(pj.error); return;}} setOut(JSON.stringify(pj.data)); return; }}
  if(slug==="json-to-csv"){{ var pj2=window.ToolKit.safeJSONParse(txt); if(!pj2.ok){{ showErr(pj2.error); return;}} var arr=Array.isArray(pj2.data)?pj2.data:[pj2.data]; var rows=[Object.keys(arr[0]||{{}})]; arr.forEach(function(o){{rows.push(rows[0].map(function(k){{return o[k]}}))}}); setOut(window.ToolKit.csvStringify(rows)); return; }}
  if(slug==="csv-to-json"){{ var cp=window.ToolKit.csvParse(txt); if(!cp.ok){{ showErr(cp.error); return;}} var hd=cp.data[0]||[], out=cp.data.slice(1).map(function(r){{var o={{}}; hd.forEach(function(h,i){{o[h]=r[i]}}); return o}}); setOut(JSON.stringify(out,null,2)); return; }}
  if(slug==="xml-formatter"||slug==="xml-validator"){{ var xv=window.ToolKit.xmlValidate(txt); setOut(xv.ok?"Valid XML":"Invalid: "+xv.error); if(!xv.ok) showErr(xv.error); return; }}
  if(slug==="yaml-formatter"||slug==="yaml-to-json"){{ var yp=window.ToolKit.yamlParse(txt); if(!yp.ok){{ showErr(yp.error); return;}} setOut(JSON.stringify(yp.data,null,2)); return; }}
  if(slug==="json-to-yaml"){{ var pj3=window.ToolKit.safeJSONParse(txt); if(!pj3.ok){{ showErr(pj3.error); return;}} setOut(window.ToolKit.yamlStringify(pj3.data)); return; }}
  if(slug==="base64-encoder"){{ if(!txt){{ showErr("Enter text to encode."); return;}} setOut(window.ToolKit.base64Encode(txt)); return; }}
  if(slug==="base64-decoder"){{ setOut(window.ToolKit.base64Decode(txt)||"Invalid Base64"); if(!window.ToolKit.base64Decode(txt)) showErr("Invalid Base64"); return; }}
  if(slug==="url-encoder"){{ setOut(window.ToolKit.urlEncode(txt)); return; }}
  if(slug==="url-decoder"){{ setOut(window.ToolKit.urlDecode(txt)); return; }}
  if(slug==="html-entity-encoder"){{ setOut(window.ToolKit.htmlEncode(txt)); return; }}
  if(slug==="html-entity-decoder"){{ setOut(window.ToolKit.htmlDecode(txt)); return; }}
  if(slug==="uuid-generator"){{ setOut(window.ToolKit.uuid()); return; }}
  if(slug==="hash-generator"){{ var a=getVal(algoEl)||"SHA-256"; window.ToolKit.hash(txt,a).then(function(h){{ setOut(h||"Error") }}); return; }}
  if(slug==="jwt-decoder"){{ var jd=window.ToolKit.jwtDecode(txt); if(!jd.ok){{ showErr(jd.error); return;}} setOut("Header: "+JSON.stringify(jd.header,null,2)+"\\nPayload: "+JSON.stringify(jd.payload,null,2)); return; }}
  if(slug==="unix-timestamp-converter"){{ var n=Number(txt.trim()); if(isFinite(n)){{ setOut(window.ToolKit.fromTimestamp(n,false)) }} else {{ setOut(String(window.ToolKit.toTimestamp(txt,false)))}} return; }}
  if(slug==="cron-expression-generator"||slug==="cron-expression-generator"){{ var cr=window.ToolKit.validateCron(txt); setOut(cr.ok?"Valid cron":"Invalid: "+cr.error); if(!cr.ok) showErr(cr.error); return; }}
  if(slug==="regex-tester"){{ var pat=getVal(patternEl)||txt, fl=getVal(flagsEl), t2=getVal(input2)||""; var rt=window.ToolKit.regexTest(pat,fl,t2||txt); if(!rt.ok){{ showErr(rt.error); return;}} setOut(rt.matches.length? rt.matches.map(function(m){{return m.match+" @"+m.index}}).join("\\n"):"No matches"); return; }}
  if(slug==="lorem-ipsum-generator"){{ var tp=getVal(loremType)||"paragraphs", cn=getVal(loremCount)||3; setOut(window.ToolKit.lorem(tp,cn)); return; }}
  if(slug.includes("word")||slug==="word-counter"){{ var wc=window.ToolKit.wordCount(txt); setOut("Words: "+wc.words+"\\nChars: "+wc.chars+"\\nNo spaces: "+wc.charsNoSpaces+"\\nSentences: "+wc.sentences+"\\nReading: "+wc.readingTime+" min"); return; }}
  if(slug==="character-counter"){{ var w2=window.ToolKit.wordCount(txt); setOut("Chars: "+w2.chars+" with spaces\\n"+w2.charsNoSpaces+" without"); return; }}
  if(slug==="case-converter"){{ setOut(txt.toUpperCase()+"\\n--- lower ---\\n"+txt.toLowerCase()); return; }}
  if(slug==="uppercase-converter"){{ setOut(window.ToolKit.toUpper(txt)); return; }}
  if(slug==="lowercase-converter"){{ setOut(window.ToolKit.toLower(txt)); return; }}
  if(slug==="title-case-converter"){{ setOut(window.ToolKit.toTitleCase(txt)); return; }}
  if(slug==="text-to-slug-converter"||slug==="slug-generator"){{ setOut(window.ToolKit.toSlug(txt)); return; }}
  if(slug==="reverse-text"){{ setOut(txt.split("").reverse().join("")); return; }}
  if(slug==="remove-duplicate-lines"){{ setOut(window.ToolKit.removeDuplicates(txt)); return; }}
  if(slug==="sort-lines-alphabetically"){{ setOut(window.ToolKit.sortLines(txt,false)); return; }}
  if(slug==="remove-extra-spaces"){{ setOut(txt.replace(/\\s+/g," ").trim()); return; }}
  if(slug==="text-diff-checker"){{ var d=window.ToolKit.textDiff(txt,getVal(input2)); setOut(d.map(function(x){{return x.type+": "+x.text}}).join("\\n")); return; }}
  if(slug==="markdown-previewer"||slug==="markdown-to-html-converter"){{ setOut(window.ToolKit.markdownBasic(txt)); return; }}
  // CSS/HTML min/beautify
  if(slug==="css-minifier"){{ setOut(window.ToolKit.cssMinify(txt)); return; }}
  if(slug==="css-beautifier"){{ setOut(window.ToolKit.cssBeautify(txt)); return; }}
  if(slug==="html-minifier"){{ setOut(window.ToolKit.htmlMinify(txt)); return; }}
  if(slug==="html-beautifier"){{ setOut(window.ToolKit.htmlBeautify(txt)); return; }}
  if(slug==="javascript-minifier"){{ setOut(window.ToolKit.jsMinify(txt)); return; }}
  if(slug==="javascript-beautifier"){{ setOut(window.ToolKit.jsBeautify(txt)); return; }}
  if(slug==="sentence-counter"){{ var sc2=window.ToolKit.wordCount(txt); setOut("Sentences: "+sc2.sentences+"\\nWords: "+sc2.words); return; }}
  if(slug==="paragraph-counter"){{ var pc=window.ToolKit.wordCount(txt); setOut("Paragraphs: "+pc.paragraphs+"\\nWords: "+pc.words); return; }}
  if(slug==="reading-time-calculator"){{ var rc=window.ToolKit.wordCount(txt); setOut("Reading time: "+rc.readingTime+" min ("+rc.words+" words @200wpm)"); return; }}
  if(slug==="markdown-table-generator"){{ var mr2=parseInt((document.querySelector("#tool-a")||{{}}).value,10), mc3=parseInt((document.querySelector("#tool-b")||{{}}).value,10); var mt=txt.trim().split(","); if(mt.length>=2&&isFinite(+mt[0])&&isFinite(+mt[1])){{ mr2=+mt[0]; mc3=+mt[1]; }} if(!isFinite(mr2)) mr2=3; if(!isFinite(mc3)) mc3=3; setOut(window.ToolKit.markdownTable(mr2,mc3)); return; }}
  if(slug==="text-to-ascii-generator"){{ if(!txt){{ showErr("Enter text."); return; }} setOut(window.ToolKit.toAscii(txt)); return; }}
  if(slug==="ascii-art-generator"){{ if(!txt.trim()){{ showErr("Enter text."); return; }} setOut(window.ToolKit.asciiArt(txt)); return; }}
  if(slug==="text-line-break-remover"){{ if(!txt){{ showErr("Enter text."); return; }} setOut(txt.replace(/([^\\n])\\n(?!\\n)/g,"$1 ").replace(/\\n{3,}/g,"\\n\\n").trim()); return; }}
  if(slug==="css-gradient-generator"){{ var gp=txt.split(",").map(function(s){{return s.trim()}}).filter(Boolean); if(gp.length<2){{ showErr("Format: color1, color2[, angle] — e.g. #ff0000, #0000ff, 90"); return; }} var ga=90; if(/deg$|^\\d+$/.test(gp[gp.length-1])){{ ga=parseFloat(gp.pop()); }} var gg=window.ToolKit.buildGradient("linear",gp,ga); if(!gg){{ showErr("Enter 2+ valid colors."); return; }} setOut("background: "+gg+";"); return; }}
  if(slug==="css-box-shadow-generator"){{ var bp=txt.trim().split(/\\s+/); if(bp.length<5){{ showErr("Format: x y blur spread color — e.g. 0 4 10 0 rgba(0,0,0,0.15)"); return; }} var bs=window.ToolKit.buildBoxShadow({{x:+bp[0],y:+bp[1],blur:+bp[2],spread:+bp[3],color:bp.slice(4).join(" ")}}); if(!bs){{ showErr("Invalid shadow values."); return; }} setOut("box-shadow: "+bs+";"); return; }}
  if(slug==="css-border-radius-generator"){{ var rp=txt.trim().split(/\\s+/).filter(Boolean); if(!rp.length||rp.length>4){{ showErr("Format: up to 4 values — e.g. 8px 8px 8px 8px"); return; }} setOut("border-radius: "+rp.join(" ")+";"); return; }}
  if(slug==="css-text-shadow-generator"){{ var sp2=txt.trim().split(/\\s+/); if(sp2.length<4){{ showErr("Format: x y blur color — e.g. 1 1 2 rgba(0,0,0,0.4)"); return; }} var tsh=window.ToolKit.buildTextShadow({{x:+sp2[0],y:+sp2[1],blur:+sp2[2],color:sp2.slice(3).join(" ")}}); setOut("text-shadow: "+tsh+";"); return; }}
  if(slug==="css-button-generator"){{ var btp=txt.split(",").map(function(s){{return s.trim()}}); if(btp.length<3){{ showErr("Format: background,foreground,radius — e.g. #2563eb, #ffffff, 8px"); return; }} setOut(".btn{{\\n  background: "+btp[0]+";\\n  color: "+btp[1]+";\\n  border-radius: "+btp[2]+";\\n  padding: 10px 20px;\\n  border: none;\\n  cursor: pointer;\\n}}\\n.btn:hover{{\\n  filter: brightness(1.1);\\n}}"); return; }}
  if(slug==="css-glassmorphism-generator"){{ var glp=txt.split(",").map(function(s){{return s.trim()}}); if(glp.length<2){{ showErr("Format: blur,alpha — e.g. 10px, 0.2"); return; }} setOut(".glass{{\\n  background: rgba(255, 255, 255, "+glp[1]+");\\n  backdrop-filter: blur("+glp[0]+");\\n  -webkit-backdrop-filter: blur("+glp[0]+");\\n  border: 1px solid rgba(255, 255, 255, 0.3);\\n  border-radius: 12px;\\n}}"); return; }}
  if(slug==="css-neumorphism-generator"){{ var nmp=txt.split(",").map(function(s){{return s.trim()}}); if(nmp.length<2){{ showErr("Format: base,dist — e.g. #e0e5ec, 9px"); return; }} setOut(".neu{{\\n  background: "+nmp[0]+";\\n  box-shadow: "+nmp[1]+" "+nmp[1]+" "+(+parseFloat(nmp[1])*2)+"px #babecc, -"+nmp[1]+" -"+nmp[1]+" "+(+parseFloat(nmp[1])*2)+"px #ffffff;\\n  border-radius: 12px;\\n}}"); return; }}
  if(slug==="css-transform-generator"){{ var tfp=txt.split(",").map(function(s){{return s.trim()}}); if(tfp.length<4){{ showErr("Format: rotate,scale,tx,ty — e.g. 15deg, 1.1, 10px, 5px"); return; }} setOut("transform: rotate("+tfp[0]+") scale("+tfp[1]+") translate("+tfp[2]+", "+tfp[3]+");"); return; }}
  if(slug==="css-animation-generator"){{ var anp=txt.split(",").map(function(s){{return s.trim()}}); if(anp.length<2||["fade","slide","bounce"].indexOf(anp[0])<0){{ showErr("Format: preset(fade|slide|bounce),duration — e.g. fade, 1s"); return; }} var kf=anp[0]==="fade"?"@keyframes fade{{from{{opacity:0}}to{{opacity:1}}}}":anp[0]==="slide"?"@keyframes slide{{from{{transform:translateY(20px);opacity:0}}to{{transform:none;opacity:1}}}}":"@keyframes bounce{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-12px)}}}}"; setOut(kf+"\\n.anim{{\\n  animation: "+anp[0]+" "+anp[1]+" ease both;\\n}}"); return; }}
  if(slug==="css-flexbox-generator"){{ var flp=txt.split(",").map(function(s){{return s.trim()}}); if(flp.length<4){{ showErr("Format: direction,justify,align,gap — e.g. row, center, center, 12px"); return; }} setOut(".flex{{\\n  display: flex;\\n  flex-direction: "+flp[0]+";\\n  justify-content: "+flp[1]+";\\n  align-items: "+flp[2]+";\\n  gap: "+flp[3]+";\\n}}"); return; }}
  if(slug==="css-grid-generator"){{ var grp=txt.split(",").map(function(s){{return s.trim()}}); if(grp.length<2){{ showErr("Format: cols,gap — e.g. 3, 16px"); return; }} setOut(".grid{{\\n  display: grid;\\n  grid-template-columns: repeat("+grp[0]+", 1fr);\\n  gap: "+grp[1]+";\\n}}"); return; }}
  if(slug==="css-clamp-generator"){{ var clp=txt.split(",").map(function(s){{return s.trim()}}); if(clp.length<3){{ showErr("Format: min,pref,max — e.g. 1rem, 2.5vw, 2rem"); return; }} setOut("font-size: clamp("+clp[0]+", "+clp[1]+", "+clp[2]+");"); return; }}
  if(slug==="css-filter-generator"){{ if(!txt.trim()){{ showErr("Enter a filter value — e.g. blur(4px) brightness(1.1)"); return; }} setOut("filter: "+txt.trim()+";"); return; }}
  if(slug==="css-color-converter"){{ if(!txt.trim()){{ showErr("Enter a color (HEX, RGB or HSL)."); return; }} var cp3=window.ToolKit.hexToRgb(txt.trim()); if(cp3){{ var h3=window.ToolKit.rgbToHsl(cp3.r,cp3.g,cp3.b); setOut("HEX: "+txt.trim()+"\\nRGB: "+cp3.r+", "+cp3.g+", "+cp3.b+"\\nHSL: "+h3.h+", "+h3.s+"%, "+h3.l+"%"); return; }} var cm=txt.match(/rgba?\\s*\\(\\s*(\\d+)\\s*,\\s*(\\d+)\\s*,\\s*(\\d+)/i); if(cm){{ var hx2=window.ToolKit.rgbToHex(+cm[1],+cm[2],+cm[3]); var h4=window.ToolKit.rgbToHsl(+cm[1],+cm[2],+cm[3]); setOut("HEX: "+hx2+"\\nRGB: "+cm[1]+", "+cm[2]+", "+cm[3]+"\\nHSL: "+h4.h+", "+h4.s+"%, "+h4.l+"%"); return; }} var hm=txt.match(/hsl\\s*\\(\\s*(\\d+)\\s*,\\s*(\\d+)%?\\s*,\\s*(\\d+)%?/i); if(hm){{ var rr2=window.ToolKit.hslToRgb(+hm[1],+hm[2],+hm[3]); setOut("HEX: "+window.ToolKit.rgbToHex(rr2.r,rr2.g,rr2.b)+"\\nRGB: "+rr2.r+", "+rr2.g+", "+rr2.b+"\\nHSL: "+hm[1]+", "+hm[2]+"%, "+hm[3]+"%"); return; }} showErr("Enter a valid HEX, RGB or HSL color."); return; }}
  // fallback generic
  if(!txt.trim()){{ showErr("Please enter input."); return; }}
  setOut(txt);
 }}catch(e){{ showErr(e.message||"Error") }}
}}
if(btn) btn.addEventListener("click",process);
var dl=$("#tool-download"), rs=$("#tool-reset");
if(dl) dl.addEventListener("click",function(){{ if(window._lastImageDataURL){{ var a=document.createElement("a"); a.href=window._lastImageDataURL; a.download=slug+".png"; document.body.appendChild(a); a.click(); a.remove(); return; }} var t=getVal(output)||output.textContent; if(!t){{ showErr("Nothing to download"); return;}} window.ToolKit.downloadText(t,slug+".txt","text/plain") }});
if(rs) rs.addEventListener("click",function(){{ window._lastImageDataURL=""; if(input){{ if(input.type==="file") input.value=""; else input.value="";}} if(input2) input2.value=""; if(aEl) aEl.value=""; if(bEl) bEl.value=""; if(cEl) cEl.value=""; if(dateA) dateA.value=""; if(dateB) dateB.value=""; var wE=$("#tool-w"),hE=$("#tool-h"),qE=$("#tool-q"); if(wE) wE.value=""; if(hE) hE.value=""; if(qE) qE.value=""; if(output){{ output.value=""; output.textContent=""}} clearErr(); if(preview){{ preview.textContent=""; if(preview.style) preview.style.background=""}} }});
}})();
</script>"""

def tool_page(tool, slug_map):
    title=tool["title"]; desc=tool["description"]; cat=tool["category"]; slug=tool["slug"]
    seo=seo_title(title)
    canonical=f"{SITE_URL}/{slug}/"
    related=tool.get("related",[])[:8]
    # generic FAQ (single source; custom pages override final_faq below)
    generic_faq_qas=[
        (f"What does {title} do?", f"{title} {desc.split('.')[0].lower()}. All processing happens in your browser with no data uploaded."),
        (f"Is {title} really free?", "Yes. It is completely free with no sign-up, no premium tier, and no hidden costs."),
        (f"Is my data safe with {title}?", "Yes. Your data never leaves your browser. All processing happens locally on your device using JavaScript."),
        (f"Can I use {title} on my phone?", "Yes. The tool is fully responsive and works on phones, tablets, and desktops."),
    ]
    # resolved related tools for display
    rel_cards=""
    for rslug in related:
        rt=slug_map.get(rslug)
        if rt:
            rel_cards+=f'<a href="{BASE}/{esc(rslug)}/" data-search="{esc(rt["title"]+" "+rt["description"])}"><h3>{esc_txt(rt["title"])}</h3><p>{esc_txt(rt["description"][:90])}</p></a>'
        else:
            rel_cards+=f'<a href="{BASE}/{esc(rslug)}/">{esc_txt(rslug.replace("-"," ").title())}</a>'
    if not rel_cards:
        rel_cards='<p>No related tools.</p>'
    # Custom hand-written content for top money pages
    custom_content={
        "json-formatter":{
            "howto":'<h2>How to use the JSON Formatter</h2><ol style="margin-left:20px;line-height:1.8"><li>Paste your raw, minified, or malformed JSON into the input box above.</li><li>Click <strong>Process</strong> to instantly pretty-print and validate it.</li><li>The formatted JSON appears in the output area with proper indentation (2 spaces).</li><li>Click <strong>Copy</strong> to grab the result, or <strong>Download</strong> to save it as a <code>.json</code> file.</li></ol>',
            "formula":'<h2>How JSON formatting works</h2><p>The formatter parses your input using the browser\u2019s native <code>JSON.parse()</code> API, then re-serializes it with <code>JSON.stringify(data, null, 2)</code> to produce clean, indented output. If your JSON is invalid, the tool shows exactly where the syntax error is so you can fix it.</p>',
            "examples":"""<h2>Worked examples</h2>
<div class="tool-grid">
<div class="tool-card"><h3>Example 1 \u2014 Minified to formatted</h3><p><strong>Input:</strong> <code>{"name":"Alice","age":30,"hobbies":["reading","gaming"]}</code></p><p><strong>Output:</strong></p><pre style="background:#f1f5f9;padding:8px;border-radius:6px;overflow-x:auto;font-size:13px">{
  "name": "Alice",
  "age": 30,
  "hobbies": [
    "reading",
    "gaming"
  ]
}</pre></div>
<div class="tool-card"><h3>Example 2 \u2014 Catching errors</h3><p><strong>Input:</strong> <code>{"name": "Bob", age: 25}</code> (missing quotes around key)</p><p><strong>Output:</strong> Error: Unexpected token a in JSON at position 14. This tells you exactly where to fix the syntax.</p></div>
</div>""",
            "faq":[
                ("What is a JSON Formatter?", "A JSON Formatter is a free online tool that takes raw, minified, or messy JSON data and pretty-prints it with proper indentation and line breaks. It also validates your JSON and shows syntax errors if any exist."),
                ("Why is my JSON not formatting?", "If the formatter shows an error, your JSON has a syntax mistake \u2014 like a missing comma, unquoted key, or trailing comma. Fix the error shown and try again."),
                ("Is my JSON data uploaded to a server?", "No. All formatting happens in your browser using JavaScript. Your JSON data never leaves your device, making it completely private."),
                ("Can I format JSON from an API response?", "Yes. Copy the JSON response from any API (Postman, browser DevTools, curl output) and paste it into the formatter. It works with any valid JSON."),
            ]
        },
        "percentage-calculator":{
            "howto":'<h2>How to use the Percentage Calculator</h2><ol style="margin-left:20px;line-height:1.8"><li>Enter the <strong>base value</strong> in the first field (e.g. 200).</li><li>Enter the <strong>percentage</strong> in the second field (e.g. 15).</li><li>Click <strong>Calculate</strong> to see the result: 15% of 200 = 30.</li></ol>',
            "formula":'<h2>Formula</h2><p>The percentage formula is: <strong>Result = (Value \u00d7 Percent) \u00f7 100</strong></p><p>For example, to find 15% of 200: (200 \u00d7 15) \u00f7 100 = 30.</p>',
            "examples":"""<h2>Worked examples</h2>
<div class="tool-grid">
<div class="tool-card"><h3>Example 1 \u2014 Discount calculation</h3><p>A $80 shirt is 25% off. What\u2019s the discount?</p><p>Enter 80 as Value A and 25 as Value B.</p><p><strong>Result:</strong> 25% of 80 = 20. So you save $20 and pay $60.</p></div>
<div class="tool-card"><h3>Example 2 \u2014 Test score</h3><p>You scored 42 out of 50 on a test. What percentage is that?</p><p>Enter 42 as Value A and 50 as Value B, then the tool calculates 42/50 \u00d7 100 = 84%.</p></div>
</div>""",
            "faq":[
                ("How do I calculate a percentage?", "Enter the base value and the percentage number, then click Calculate. The formula is: Result = (Value \u00d7 Percent) \u00f7 100."),
                ("How do I find what percent A is of B?", "Divide A by B and multiply by 100. For example, 30 out of 50: (30 \u00f7 50) \u00d7 100 = 60%."),
                ("Can I calculate percentage increase or decrease?", "Yes. Use the separate Percentage Increase and Percentage Decrease calculators linked below, or enter the old and new values."),
                ("Is this percentage calculator accurate?", "Yes. It uses precise JavaScript math. For most real-world purposes (taxes, discounts, grades), the results are exact."),
            ]
        },
        "word-counter":{
            "howto":'<h2>How to use the Word Counter</h2><ol style="margin-left:20px;line-height:1.8"><li>Paste or type your text into the input box above.</li><li>Click <strong>Process</strong> to instantly count.</li><li>See the word count, character count (with and without spaces), sentence count, and estimated reading time.</li></ol>',
            "formula":'<h2>How word counting works</h2><p>The tool splits your text by whitespace to count words, counts each character for character totals, splits by sentence-ending punctuation (.!?) for sentences, and estimates reading time at <strong>200 words per minute</strong> (average adult reading speed).</p>',
            "examples":"""<h2>Worked examples</h2>
<div class="tool-grid">
<div class="tool-card"><h3>Example 1 \u2014 Short paragraph</h3><p><strong>Input:</strong> "The quick brown fox jumps over the lazy dog. This sentence contains every letter of the English alphabet."</p><p><strong>Result:</strong> Words: 16 | Characters: 86 | Characters (no spaces): 71 | Sentences: 2 | Reading time: 0 min</p></div>
<div class="tool-card"><h3>Example 2 \u2014 Essay check</h3><p><strong>Input:</strong> Paste a 500-word essay draft.</p><p><strong>Result:</strong> Words: 500 | Characters: 3,200 | Reading time: 2 min. Great for checking if you\u2019re within a word limit.</p></div>
</div>""",
            "faq":[
                ("How accurate is the word counter?", "Very accurate. It counts words by splitting on whitespace and characters by iterating each character. The reading time estimate uses 200 words per minute, the average adult reading speed."),
                ("Does it count characters with or without spaces?", "Both. You\u2019ll see character count with spaces and without spaces, plus word count, sentence count, and estimated reading time."),
                ("Can I use it to check essay word limits?", "Absolutely. Paste your essay or assignment text and instantly see if you\u2019re within the word limit."),
                ("Does it work with multiple languages?", "It works with any text that uses spaces between words. For languages without spaces (Chinese, Japanese), the character count is more useful than word count."),
            ]
        },
        "age-calculator":{
            "howto":'<h2>How to use the Age Calculator</h2><ol style="margin-left:20px;line-height:1.8"><li>Enter your <strong>date of birth</strong> using the date picker, or type it in YYYY-MM-DD format.</li><li>Click <strong>Calculate</strong>.</li><li>See your exact age in years, and today\u2019s date for reference.</li></ol>',
            "formula":'<h2>How age is calculated</h2><p>The calculator subtracts your birth date from today\u2019s date. It accounts for whether your birthday has occurred this year yet, giving you your <strong>exact age</strong> (not rounded). For example, if you were born on March 15, 2000 and today is September 14, 2026, you are 26 years old (not 26.5 or 27).</p>',
            "examples":"""<h2>Worked examples</h2>
<div class="tool-grid">
<div class="tool-card"><h3>Example 1 \u2014 Exact age</h3><p><strong>DOB:</strong> January 1, 2000</p><p><strong>Today:</strong> September 14, 2026</p><p><strong>Result:</strong> Age: 26 years. You turned 26 on January 1, 2026 and will turn 27 on January 1, 2027.</p></div>
<div class="tool-card"><h3>Example 2 \u2014 Birthday not yet this year</h3><p><strong>DOB:</strong> December 25, 1995</p><p><strong>Today:</strong> September 14, 2026</p><p><strong>Result:</strong> Age: 30 years. Your 31st birthday is coming on December 25, 2026.</p></div>
</div>""",
            "faq":[
                ("How accurate is the age calculator?", "It calculates your exact age based on the difference between your birth date and today\u2019s date, accounting for whether your birthday has passed this year."),
                ("Does it show months and days too?", "Currently it shows age in complete years. For a more detailed breakdown, you can use the date difference calculator linked below."),
                ("Can I calculate someone else\u2019s age?", "Yes. Enter any birth date \u2014 it doesn\u2019t have to be yours. Great for calculating a family member\u2019s or friend\u2019s age."),
                ("Is my birth date stored anywhere?", "No. All calculations happen in your browser. Your date of birth is never sent to any server."),
            ]
        },
        "loan-emi-calculator":{
            "howto":'<h2>How to use the Loan EMI Calculator</h2><ol style="margin-left:20px;line-height:1.8"><li>Enter the <strong>loan amount</strong> (principal) in Value A \u2014 e.g. 500000.</li><li>Enter the <strong>annual interest rate</strong> (%) in Value B \u2014 e.g. 8.5.</li><li>Enter the <strong>loan tenure</strong> in months in Value C \u2014 e.g. 60.</li><li>Click <strong>Calculate</strong> to see your monthly EMI amount.</li></ol>',
            "formula":'<h2>EMI Formula</h2><p>EMI = P \u00d7 r \u00d7 (1+r)<sup>n</sup> / ((1+r)<sup>n</sup> \u2212 1)</p><p>Where:</p><ul style="margin-left:20px;line-height:1.8"><li><strong>P</strong> = Principal loan amount</li><li><strong>r</strong> = Monthly interest rate (annual rate \u00f7 12 \u00f7 100)</li><li><strong>n</strong> = Loan tenure in months</li></ul>',
            "examples":"""<h2>Worked examples</h2>
<div class="tool-grid">
<div class="tool-card"><h3>Example 1 \u2014 Home loan</h3><p><strong>Loan:</strong> \u20b950,00,000 | <strong>Rate:</strong> 8.5% p.a. | <strong>Tenure:</strong> 240 months (20 years)</p><p><strong>Monthly EMI:</strong> \u20b943,391</p><p><strong>Total payment:</strong> \u20b91,04,13,840 | <strong>Total interest:</strong> \u20b954,13,840</p></div>
<div class="tool-card"><h3>Example 2 \u2014 Car loan</h3><p><strong>Loan:</strong> \u20b98,00,000 | <strong>Rate:</strong> 9% p.a. | <strong>Tenure:</strong> 60 months (5 years)</p><p><strong>Monthly EMI:</strong> \u20b916,607</p><p><strong>Total payment:</strong> \u20b99,96,420 | <strong>Total interest:</strong> \u20b91,96,420</p></div>
</div>""",
            "faq":[
                ("What is EMI?", "EMI stands for Equated Monthly Installment. It is the fixed amount you pay every month to repay a loan over a set tenure. It includes both principal and interest."),
                ("How is EMI calculated?", "EMI = P \u00d7 r \u00d7 (1+r)^n / ((1+r)^n \u2212 1), where P is the loan amount, r is the monthly interest rate, and n is the tenure in months."),
                ("Is this EMI calculator accurate?", "Yes. It uses the standard reducing balance formula used by all banks. The result matches what banks show in their EMI calculators."),
                ("Can I compare different loan offers?", "Yes. Calculate the EMI for each offer with different interest rates and tenures, then compare the total interest paid to find the cheapest option."),
            ]
        }
    }
    # Tool scope/format notes (blue info box above tool UI)
    NOTES={
        "yaml-formatter": "Handles common flat YAML (key: value, lists). Anchors, aliases and complex multiline scalars may not parse.",
        "yaml-to-json": "Handles common flat YAML (key: value, lists). Anchors, aliases and complex multiline scalars may not parse.",
        "json-to-yaml": "Handles common flat YAML (key: value, lists). Anchors, aliases and complex multiline scalars may not parse.",
        "javascript-minifier": "Basic regex-based minifier — always test output; may not suit code with tricky strings/templates.",
        "css-minifier": "Basic regex-based minifier — always test output; may not suit code with tricky strings/templates.",
        "html-minifier": "Basic regex-based minifier — always test output; may not suit code with tricky strings/templates.",
        "css-gradient-generator": "Format: color1, color2[, angle] — e.g. #ff0000, #0000ff, 90",
        "css-box-shadow-generator": 'Format: x y blur spread color — e.g. 0 4 10 0 rgba(0,0,0,0.15)',
        "css-border-radius-generator": "Format: up to 4 values — e.g. 8px 8px 8px 8px",
        "css-text-shadow-generator": "Format: x y blur color — e.g. 1 1 2 rgba(0,0,0,0.4)",
        "css-button-generator": "Format: background,foreground,radius — e.g. #2563eb, #ffffff, 8px",
        "css-glassmorphism-generator": "Format: blur,alpha — e.g. 10px, 0.2",
        "css-neumorphism-generator": "Format: base,dist — e.g. #e0e5ec, 9px",
        "css-transform-generator": "Format: rotate,scale,tx,ty — e.g. 15deg, 1.1, 10px, 5px",
        "css-animation-generator": "Format: preset(fade|slide|bounce),duration — e.g. fade, 1s",
        "css-flexbox-generator": "Format: direction,justify,align,gap — e.g. row, center, center, 12px",
        "css-grid-generator": "Format: cols,gap — e.g. 3, 16px",
        "css-clamp-generator": "Format: min,pref,max — e.g. 1rem, 2.5vw, 2rem",
        "css-filter-generator": "Enter a full filter value — e.g. blur(4px) brightness(1.1)",
        "css-color-converter": "Enter any HEX, RGB or HSL color in the text field.",
        "unit-conversion-calculator": "Format: value,from,to — e.g. 10,km,mi",
        "flashcard-generator": "One card per line as Question|Answer",
        "markdown-table-generator": "Use Value A for rows and Value B for columns (or type rows,cols).",
        "exam-countdown": "Enter date as YYYY-MM-DD in the text field.",
        "assignment-countdown": "Enter date as YYYY-MM-DD in the text field.",
        "semester-countdown": "Enter date as YYYY-MM-DD in the text field.",
    }
    note_html=""
    if slug in NOTES:
        note_html=f'<div role="note" style="margin:12px 0;padding:12px 16px;background:#eff6ff;border:1px solid #3b82f6;border-radius:8px;font-size:14px;color:#1e40af"><strong>Note:</strong> {esc_txt(NOTES[slug])}</div>'
    # Formula / examples logic — single-source FAQ: build ONE final_faq per branch,
    # then render BOTH visible faq_html AND faq_json from it (no divergence).
    formula_html=""
    if slug in custom_content:
        cc=custom_content[slug]
        howto_html=cc.get("howto","")
        formula_html=cc.get("formula","")
        examples=cc.get("examples","")
        final_faq=list(cc.get("faq",generic_faq_qas))
    elif cat in ("Math Calculators","Finance Calculators","Business Calculators","Date & Time","Student Tools"):
        formula_html='<h2>How it works</h2><p>This calculator processes your input entirely in your browser using JavaScript. The result is computed instantly and never sent to any server.</p>'
        howto_html='<h2>How to use this calculator</h2><ol style="margin-left:20px;line-height:1.8"><li>Enter your values in the fields above.</li><li>Click <strong>Calculate</strong> to see the result instantly.</li><li>Click <strong>Copy</strong> to grab the result, or <strong>Download</strong> to save it as a text file.</li></ol>'
        examples=f"""
<h2>Try it yourself</h2>
<div class="tool-grid">
<div class="tool-card"><h3>Quick test</h3><p>Enter sample values in the fields above and click Calculate. The result appears instantly in the output area.</p></div>
<div class="tool-card"><h3>Tip</h3><p>You can copy the result with one click, or download it as a text file for your records.</p></div>
</div>"""
        final_faq=list(generic_faq_qas)
    else:
        formula_html='<h2>How it works</h2><p>All processing happens locally in your browser. Your input is never uploaded to any server. The tool uses the ToolKit JavaScript library for fast, private results.</p>'
        howto_html='<h2>How to use this tool</h2><ol style="margin-left:20px;line-height:1.8"><li>Paste or type your input in the text area above.</li><li>Click <strong>Process</strong> to transform it instantly.</li><li>Click <strong>Copy</strong> to grab the result, or <strong>Download</strong> to save it as a file.</li></ol>'
        examples=f"""
<h2>Try it yourself</h2>
<div class="tool-grid">
<div class="tool-card"><h3>Quick test</h3><p>Paste some sample text or data above and click Process. The result appears instantly in the output area.</p></div>
<div class="tool-card"><h3>Tip</h3><p>You can copy the result with one click, or download it as a text file for your records.</p></div>
</div>"""
        final_faq=list(generic_faq_qas)
    faq_html=""
    for q,a in final_faq:
        faq_html+=f'<details class="faq-item"><summary class="faq-q">{esc_txt(q)}</summary><div class="faq-a"><p>{esc_txt(a)}</p></div></details>'
    faq_json=json.dumps([{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in final_faq])

    ui=tool_ui(tool)
    script=inline_script(tool)
    breadcrumbs=f'<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="{BASE}/">Home</a><span>\u203a</span><a href="{BASE}/#categories">{esc_txt(cat)}</a><span>\u203a</span><span aria-current="page">{esc_txt(title)}</span></nav>'

    # Finance disclaimer and formula from tools.json
    disclaimer_html=""
    if tool.get("disclaimer"):
        disclaimer_html=f'<div style="margin-top:16px;padding:12px 16px;background:#fef3c7;border:1px solid #f59e0b;border-radius:8px;font-size:14px;color:#92400e"><strong>Disclaimer:</strong> {esc_txt(tool["disclaimer"])}</div>'
    formula_from_json=""
    if tool.get("formula_text"):
        formula_from_json=f'<div style="margin-top:12px;padding:12px 16px;background:#f0f9ff;border:1px solid #3b82f6;border-radius:8px;font-size:14px;color:#1e40af"><strong>Formula:</strong> {esc_txt(tool["formula_text"])}</div>'

    jsonld=f"""
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"SoftwareApplication","name":"{esc(title)}","description":"{esc(desc)}","url":"{esc(canonical)}","applicationCategory":"UtilitiesApplication","operatingSystem":"Web","offers":{{"@type":"Offer","price":"0","priceCurrency":"USD"}}}}</script>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":{faq_json}}}</script>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"Home","item":"{SITE_URL}/"}},{{"@type":"ListItem","position":2,"name":"{esc(cat)}","item":"{SITE_URL}/#categories"}},{{"@type":"ListItem","position":3,"name":"{esc(title)}","item":"{esc(canonical)}"}}]}}</script>"""

    body=f"""{header_html(False)}
<main id="main" class="container">
{breadcrumbs}
<h1>{esc_txt(title)}</h1>
<p>{esc_txt(desc)}</p>
{note_html}
{ui}
<section style="margin-top:24px">
{howto_html}
{formula_html}
{formula_from_json}
{examples}
{disclaimer_html}
<div class="faq" style="margin-top:24px"><h2>FAQ</h2>{faq_html}</div>
<div style="margin-top:24px"><h2>Related tools</h2><div class="related" style="display:grid;gap:12px;grid-template-columns:repeat(auto-fill,minmax(240px,1fr))">{rel_cards}</div></div>
</section>
</main>
{footer_html()}
{jsonld}
{script}"""

    html_doc=f"""<!doctype html>
<html lang="en">
<head>
{head_html(seo,desc,canonical)}
</head>
<body>
{body}
</body>
</html>"""
    return html_doc

def about_page():
    canonical=f"{SITE_URL}/about/"
    title="About DevelopersKit — Free Online Browser Tools"
    desc="Learn about DevelopersKit, a free collection of 230 browser-based tools for developers, students, and professionals. No uploads, no sign-up, fully private."
    faq_qas=[
        ("What is DevelopersKit?", "DevelopersKit is a free collection of 230 browser-based tools for developers, students, and professionals. Every tool runs entirely in your browser \u2014 no data is uploaded to any server."),
        ("Is DevelopersKit really free?", "Yes, all 230 tools are completely free to use with no sign-up required. There are no hidden fees or premium tiers."),
        ("How does DevelopersKit protect my privacy?", "All processing happens locally in your browser using JavaScript. Your data never leaves your device \u2014 there are no server uploads, databases, or tracking of your input."),
        ("Who built DevelopersKit?", "DevelopersKit was created by a web developer passionate about building fast, accessible, and privacy-respecting tools that help people get things done without complicated software."),
    ]
    faq_json=json.dumps([{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq_qas])
    faq_html=""
    for q,a in faq_qas:
        faq_html+=f'<details class="faq-item"><summary class="faq-q">{esc_txt(q)}</summary><div class="faq-a"><p>{esc_txt(a)}</p></div></details>'
    faq_schema={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq_qas]}
    breadcrumb_schema={"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":f"{SITE_URL}/"},{"@type":"ListItem","position":2,"name":"About","item":f"{SITE_URL}/about/"}]}
    jsonld=f"""
<script type="application/ld+json">{json.dumps(faq_schema)}</script>
<script type="application/ld+json">{json.dumps(breadcrumb_schema)}</script>"""
    body=f"""{header_html(False)}
<main id="main" class="container">
<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="{BASE}/">Home</a><span>\u203a</span><span aria-current="page">About</span></nav>
<h1>About DevelopersKit</h1>
<p>We built DevelopersKit because finding reliable, fast, and private online tools shouldn't be hard. Most tool websites are cluttered with ads, require sign-ups, or upload your data to unknown servers. We wanted something different.</p>

<section style="margin-top:24px">
<h2>What We Offer</h2>
<p>DevelopersKit is a collection of <strong>230 free browser-based tools</strong> spanning 10 categories: Developer Tools, CSS/HTML Tools, Text Tools, Math Calculators, Student Tools, Date & Time, Finance Calculators, Business Calculators, Color Tools, and Image Tools.</p>
<p>Whether you need to format JSON, calculate your EMI, count words, resize an image, or pick a color palette \u2014 we have a tool for it. Every tool is designed to be fast, accurate, and easy to use.</p>

<h2>How It Works</h2>
<p>All tools run entirely in your browser using modern web APIs and JavaScript. When you paste text into the JSON Formatter or upload an image to the Resizer, the processing happens on your device. <strong>Your data never leaves your browser.</strong> There are no server uploads, no databases storing your input, and no analytics tracking what you do with the tools.</p>

<h2>Our Principles</h2>
<div class="tool-grid" style="margin-top:12px">
<div class="tool-card"><h3>Privacy First</h3><p>Your data stays on your device. We cannot see what you enter or process. No uploads. No account required. Processing happens locally in your browser.</p></div>
<div class="tool-card"><h3>Always Free</h3><p>No sign-ups, no premium tiers, no hidden costs. Every tool is free to use, today and tomorrow.</p></div>
<div class="tool-card"><h3>Fast &amp; Lightweight</h3><p>No heavy frameworks or bloated libraries. Pages load fast and tools respond instantly.</p></div>
<div class="tool-card"><h3>Works Offline</h3><p>Once loaded, most tools work without an internet connection. Use them anywhere, anytime.</p></div>
<div class="tool-card"><h3>Accessible</h3><p>Built with keyboard navigation, screen reader support, and WCAG-compliant contrast ratios.</p></div>
<div class="tool-card"><h3>No Account Required</h3><p>Jump in and use any tool immediately. No email, no password, no registration form.</p></div>
</div>

<h2>Built With</h2>
<p>DevelopersKit is built with vanilla HTML, CSS, and JavaScript \u2014 no frameworks, no build tools, no dependencies. It is hosted on GitHub Pages and the source code is open for anyone to inspect.</p>

<h2>FAQ</h2>
<div class="faq" style="margin-top:12px">{faq_html}</div>

<h2 style="margin-top:24px">Get Started</h2>
<p>Ready to use our tools? <a href="{BASE}/" style="color:#2563eb;font-weight:600">Browse all 230 tools \u2192</a></p>
</section>
</main>
{footer_html()}
{jsonld}"""
    doc=f"""<!doctype html>
<html lang="en">
<head>
{head_html(title,desc,canonical)}
</head>
<body>
{body}
</body>
</html>"""
    return doc

def privacy_page():
    canonical=f"{SITE_URL}/privacy/"
    title="Privacy Policy — DevelopersKit"
    desc="DevelopersKit privacy policy: all tools run locally in your browser. No uploads, no accounts, no analytics, no tracking of your input."
    faq_qas=[
        ("Does DevelopersKit collect my data?", "No. All tool processing happens locally in your browser using JavaScript. We do not collect, store, or transmit anything you type, paste, or upload into the tools."),
        ("Does DevelopersKit use cookies or analytics?", "No. We do not set cookies and we do not run analytics, advertising, or tracking scripts on this site."),
        ("What about hosting logs?", "This site is hosted on GitHub Pages. GitHub may collect standard server logs (such as IP addresses) as described in the GitHub Privacy Statement. We do not have access to those logs."),
        ("How can I contact you about privacy?", "Open an issue on our GitHub repository: https://github.com/developerskit99/developerskit99.github.io."),
    ]
    faq_schema={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq_qas]}
    breadcrumb_schema={"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":f"{SITE_URL}/"},{"@type":"ListItem","position":2,"name":"Privacy","item":f"{SITE_URL}/privacy/"}]}
    app_schema={"@context":"https://schema.org","@type":"SoftwareApplication","name":"DevelopersKit","url":SITE_URL,"applicationCategory":"DeveloperApplication","operatingSystem":"Web Browser","offers":{"@type":"Offer","price":"0","priceCurrency":"USD"},"description":"230 free browser-based tools for developers, students, and professionals. Your data stays in your browser."}
    jsonld=f"""
<script type="application/ld+json">{json.dumps(app_schema)}</script>
<script type="application/ld+json">{json.dumps(faq_schema)}</script>
<script type="application/ld+json">{json.dumps(breadcrumb_schema)}</script>"""
    faq_html=""
    for q,a in faq_qas:
        faq_html+=f'<details class="faq-item"><summary class="faq-q">{esc_txt(q)}</summary><div class="faq-a"><p>{esc_txt(a)}</p></div></details>'
    body=f"""{header_html(False)}
<main id="main" class="container">
<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="{BASE}/">Home</a><span>\u203a</span><span aria-current="page">Privacy</span></nav>
<h1>Privacy Policy</h1>
<p><strong>Short version:</strong> everything you do with our tools stays in your browser. No uploads, no accounts, no analytics, no tracking of your input.</p>
<section style="margin-top:24px">
<h2>What we collect</h2>
<p>Nothing. We do not collect, store, or transmit anything you type, paste, or upload into the tools. All processing happens locally on your device using JavaScript.</p>
<h2>Cookies and tracking</h2>
<p>We do not set cookies and we do not run analytics, advertising, or tracking scripts.</p>
<h2>Hosting</h2>
<p>This site is hosted on GitHub Pages. GitHub may collect standard server logs (such as IP addresses) as described in the GitHub Privacy Statement. We do not have access to those logs.</p>
<h2>Third parties</h2>
<p>We do not share data with third parties because we do not collect any data in the first place.</p>
<h2>Contact</h2>
<p>Questions about this policy? Open an issue at <a href="https://github.com/developerskit99/developerskit99.github.io" style="color:#2563eb;font-weight:600">our GitHub repository</a>.</p>
<h2>FAQ</h2>
<div class="faq" style="margin-top:12px">{faq_html}</div>
</section>
</main>
{footer_html()}
{jsonld}"""
    doc=f"""<!doctype html>
<html lang="en">
<head>
{head_html(title,desc,canonical)}
</head>
<body>
{body}
</body>
</html>"""
    return doc

def hub_page(tools):
    # group by category
    from collections import defaultdict, OrderedDict
    cats=defaultdict(list)
    for t in tools: cats[t["category"]].append(t)
    order=["Developer Tools","CSS/HTML Tools","Text Tools","Math Calculators","Student Tools","Date & Time","Finance Calculators","Business Calculators","Color Tools","Image Tools"]
    # ensure all present
    for k in list(cats.keys()):
        if k not in order: order.append(k)
    sections=""
    for cat in order:
        lst=cats.get(cat,[])
        if not lst: continue
        total=len(lst)
        slug_map_local={t["slug"]:t for t in lst}
        cat_slug=CATEGORY_SLUGS.get(cat, cat.lower().replace(" ","-").replace("&","").replace("/","-"))
        sub_sections_html=""
        subcats=SUBCATEGORIES.get(cat,[])
        if subcats:
            for sub_name, sub_slugs in subcats:
                sub_tools=[slug_map_local[s] for s in sub_slugs if s in slug_map_local]
                if not sub_tools: continue
                sub_cards=""
                for t in sorted(sub_tools, key=lambda x:x["title"]):
                    sub_cards+=f'<div class="tool-card" data-search="{esc(t["title"]+" "+t["description"]+" "+t["category"])}"><h3><a href="{BASE}/{esc(t["slug"])}/">{esc_txt(t["title"])}</a></h3><p>{esc_txt(t["description"][:110])}</p></div>\n'
                sub_sections_html+=f'<h3 class="sub-cat-heading">{esc_txt(sub_name)}</h3><div class="tool-grid">{sub_cards}</div>\n'
        else:
            sub_cards=""
            for t in sorted(lst, key=lambda x:x["title"]):
                sub_cards+=f'<div class="tool-card" data-search="{esc(t["title"]+" "+t["description"]+" "+t["category"])}"><h3><a href="{BASE}/{esc(t["slug"])}/">{esc_txt(t["title"])}</a></h3><p>{esc_txt(t["description"][:110])}</p></div>\n'
            sub_sections_html=f'<div class="tool-grid">{sub_cards}</div>\n'
        anchor="cat-"+esc(cat.lower().replace(" ","-").replace("&","").replace("/","-"))
        sections+=f'<section class="cat-card" id="{anchor}"><h2><a href="{BASE}/{cat_slug}/">{esc_txt(cat)}</a> <span class="cat-count">{total} tools</span></h2>{sub_sections_html}</section>\n'

    seo_title_hub="Free Developer & Utility Tools — 230 Online Tools | DevelopersKit"
    desc_hub="230 free browser-based tools for developers, students, and professionals. Your data stays in your browser — no uploads, no sign-up."
    head=head_html(seo_title_hub,desc_hub,SITE_URL+"/")
    # category quick-links for hero
    quick_cats=""
    for cat in order:
        lst=cats.get(cat,[])
        if not lst: continue
        anchor="cat-"+esc(cat.lower().replace(" ","-").replace("&","").replace("/","-"))
        quick_cats+=f'<a href="#{anchor}" class="popular-pill">{esc_txt(cat)}</a>\n'
    hero=f"""
<main id="main" class="container">
<section class="hero">
<h1>Free Online Developer &amp; Utility Tools</h1>
<p class="hero-sub">230 browser-based tools — your data stays in your browser, no uploads.</p>
<p class="stats-bar">No uploads. No account required. Processing happens locally in your browser.</p>
<div class="hero-search"><div class="search-wrap"><label for="q" class="sr-only">Search tools</label><input id="q" data-search-input type="search" class="search-input" placeholder="Search 230 tools (e.g. JSON Formatter, Word Counter)" autocomplete="off"></div></div>
<div class="popular">{quick_cats}</div>
</section>
<div class="category-grid" id="categories">
{sections}
</div>
<section id="tools" style="padding-bottom:32px"><p style="text-align:center;color:#64748b">All tools run locally \u2014 your data never leaves your device.</p></section>
</main>"""

    doc=f"""<!doctype html>
<html lang="en">
<head>
{head}
</head>
<body>
{header_html(False)}
{hero}
{footer_html()}
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"WebSite","name":"DevelopersKit","url":"{SITE_URL}","description":"230 free browser-based tools for developers, students, and professionals.","potentialAction":{{"@type":"SearchAction","target":"{SITE_URL}/?q={{search_term_string}}","query-input":"required name=search_term_string"}}}}</script>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Organization","name":"DevelopersKit","url":"{SITE_URL}","logo":"{SITE_URL}/assets/images/logo.svg","description":"Free browser-based tools for developers, students, and professionals."}}</script>
</body>
</html>"""
    return doc

def category_page(cat_name, tools, slug_map):
    cat_slug=CATEGORY_SLUGS.get(cat_name, cat_name.lower().replace(" ","-").replace("&","").replace("/","-"))
    canonical=f"{SITE_URL}/{cat_slug}/"
    title=f"{cat_name} \u2014 Free Online Tools | DevelopersKit"
    desc=f"Free {cat_name.lower()} for developers, students, and professionals. All tools run in your browser \u2014 no uploads, no sign-up."
    if len(desc)>160: desc=desc[:157]+"..."
    breadcrumbs=f'<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="{BASE}/">Home</a><span>\u203a</span><span aria-current="page">{esc_txt(cat_name)}</span></nav>'
    # sub-category sections
    subcats=SUBCATEGORIES.get(cat_name,[])
    sub_sections=""
    if subcats:
        for sub_name, sub_slugs in subcats:
            sub_tools=[slug_map[s] for s in sub_slugs if s in slug_map]
            if not sub_tools: continue
            sub_cards=""
            for t in sorted(sub_tools, key=lambda x:x["title"]):
                sub_cards+=f'<div class="tool-card" data-search="{esc(t["title"]+" "+t["description"])}"><h3><a href="{BASE}/{esc(t["slug"])}/">{esc_txt(t["title"])}</a></h3><p>{esc_txt(t["description"][:110])}</p></div>\n'
            sub_sections+=f'<h2>{esc_txt(sub_name)}</h2><div class="tool-grid">{sub_cards}</div>\n'
    else:
        all_cards=""
        for t in sorted(tools, key=lambda x:x["title"]):
            all_cards+=f'<div class="tool-card" data-search="{esc(t["title"]+" "+t["description"])}"><h3><a href="{BASE}/{esc(t["slug"])}/">{esc_txt(t["title"])}</a></h3><p>{esc_txt(t["description"][:110])}</p></div>\n'
        sub_sections=f'<div class="tool-grid">{all_cards}</div>\n'
    # related categories
    related_cats=[c for c in CATEGORY_SLUGS if c!=cat_name][:6]
    rel_html=""
    for rc in related_cats:
        rc_slug=CATEGORY_SLUGS[rc]
        rel_html+=f'<a href="{BASE}/{rc_slug}/" class="popular-pill">{esc_txt(rc)}</a>\n'
    # FAQ
    faq_qas=[
        (f"What {cat_name.lower()} are available?", f"DevelopersKit offers {len(tools)} free {cat_name.lower()} including {', '.join(t['title'] for t in tools[:5])} and more."),
        (f"Are {cat_name.lower()} really free?", "Yes. All tools are completely free with no sign-up, no premium tier, and no hidden costs."),
        (f"Is my data safe with {cat_name.lower()}?", "Yes. Your data never leaves your browser. All processing happens locally on your device using JavaScript."),
        (f"Can I use {cat_name.lower()} on my phone?", "Yes. All tools are fully responsive and work on phones, tablets, and desktops."),
    ]
    faq_html=""
    for q,a in faq_qas:
        faq_html+=f'<details class="faq-item"><summary class="faq-q">{esc_txt(q)}</summary><div class="faq-a"><p>{esc_txt(a)}</p></div></details>'
    faq_json=json.dumps([{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq_qas])
    jsonld=f"""
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"Home","item":"{SITE_URL}/"}},{{"@type":"ListItem","position":2,"name":"{esc(cat_name)}","item":"{esc(canonical)}"}}]}}</script>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":{faq_json}}}</script>"""
    body=f"""{header_html(True)}
<main id="main" class="container">
{breadcrumbs}
<h1>{esc_txt(cat_name)} Tools</h1>
<p>Free browser-based {cat_name.lower()} for developers, students, and professionals. Your data stays in your browser.</p>
<section style="margin-top:24px">
{sub_sections}
<div class="faq" style="margin-top:24px"><h2>FAQ</h2>{faq_html}</div>
<div style="margin-top:24px"><h2>Related categories</h2><div style="display:flex;flex-wrap:wrap;gap:8px">{rel_html}</div></div>
</section>
</main>
{footer_html()}
{jsonld}"""
    doc=f"""<!doctype html>
<html lang="en">
<head>
{head_html(title,desc,canonical)}
</head>
<body>
{body}
</body>
</html>"""
    return doc

def main():
    site, tools=read_data()
    slug_map={t["slug"]:t for t in tools}
    # hub
    hub=hub_page(tools)
    with open(os.path.join(ROOT,"index.html"),"w",encoding="utf-8") as f: f.write(hub)
    # about page
    about=about_page()
    about_dir=os.path.join(ROOT,"about")
    os.makedirs(about_dir, exist_ok=True)
    with open(os.path.join(about_dir,"index.html"),"w",encoding="utf-8") as f: f.write(about)
    # privacy page
    priv=privacy_page()
    priv_dir=os.path.join(ROOT,"privacy")
    os.makedirs(priv_dir, exist_ok=True)
    with open(os.path.join(priv_dir,"index.html"),"w",encoding="utf-8") as f: f.write(priv)
    # tool pages
    for t in tools:
        slug=t["slug"]
        d=os.path.join(ROOT, slug)
        os.makedirs(d, exist_ok=True)
        html_doc=tool_page(t, slug_map)
        with open(os.path.join(d,"index.html"),"w",encoding="utf-8") as f: f.write(html_doc)
    # sitemap
    urls=[f'  <url><loc>{SITE_URL}/</loc><lastmod>{DATE}</lastmod><changefreq>weekly</changefreq><priority>1.0</priority></url>']
    urls.append(f'  <url><loc>{SITE_URL}/about/</loc><lastmod>{DATE}</lastmod><changefreq>monthly</changefreq><priority>0.6</priority></url>')
    urls.append(f'  <url><loc>{SITE_URL}/privacy/</loc><lastmod>{DATE}</lastmod><changefreq>monthly</changefreq><priority>0.4</priority></url>')
    # category pages
    order=["Developer Tools","CSS/HTML Tools","Text Tools","Math Calculators","Student Tools","Date & Time","Finance Calculators","Business Calculators","Color Tools","Image Tools"]
    for cat in order:
        cat_tools=[t for t in tools if t["category"]==cat]
        if not cat_tools: continue
        cat_slug=CATEGORY_SLUGS.get(cat, cat.lower().replace(" ","-").replace("&","").replace("/","-"))
        cat_dir=os.path.join(ROOT, cat_slug)
        os.makedirs(cat_dir, exist_ok=True)
        cat_html=category_page(cat, cat_tools, slug_map)
        with open(os.path.join(cat_dir,"index.html"),"w",encoding="utf-8") as f: f.write(cat_html)
        urls.append(f'  <url><loc>{SITE_URL}/{cat_slug}/</loc><lastmod>{DATE}</lastmod><changefreq>monthly</changefreq><priority>0.7</priority></url>')
    for t in sorted(tools, key=lambda x:x["slug"]):
        urls.append(f'  <url><loc>{SITE_URL}/{t["slug"]}/</loc><lastmod>{DATE}</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>')
    sitemap='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+ "\n".join(urls) + '\n</urlset>'
    with open(os.path.join(ROOT,"sitemap.xml"),"w",encoding="utf-8",newline="\n") as f: f.write(sitemap)
    # robots
    with open(os.path.join(ROOT,"robots.txt"),"w",encoding="utf-8",newline="\n") as f: f.write(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")
    print(f"Generated {len(tools)} tools + hub + about + sitemap")

if __name__=="__main__":
    main()
