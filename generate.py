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
<link rel="icon" type="image/png" sizes="32x32" href="{BASE}/assets/images/favicon-32x32.png">
<link rel="apple-touch-icon" sizes="180x180" href="{BASE}/assets/images/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{og}">
<meta property="og:image" content="{og}">
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
<div><img src="{BASE}/assets/images/logo.svg" alt="DevelopersKit" height="28" width="140" style="margin-bottom:8px"><p style="margin-top:8px">Fast, free, browser-based tools for developers and everyday tasks. No uploads \u2014 everything runs locally.</p></div>
<div><p><a href="{BASE}/">Homepage</a> \u00b7 <a href="{BASE}/about/">About</a> \u00b7 <a href="{BASE}/sitemap.xml">Sitemap</a> \u00b7 <a href="{BASE}/privacy/">Privacy</a></p><p style="margin-top:8px">\u00a9 <span id="year">{YEAR}</span> DevelopersKit. All tools run client-side.</p></div>
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
   var f=fileInput && fileInput.files[0];
   if(!f){{ showErr("Please select an image file (max 10MB)."); return; }}
   var v=window.ToolKit.validateImageFile(f);
   if(!v.ok){{ showErr(v.error); return; }}
   var meta=window.ToolKit.imageMetadata(f);
   var info="Name: "+meta.name+"\\nType: "+meta.type+"\\nSize: "+meta.sizeKB+" KB";
   if(preview){{ preview.textContent=""; var img=document.createElement("img"); img.style.maxWidth="100%"; img.style.borderRadius="8px"; preview.appendChild(img); var b64=await window.ToolKit.fileToBase64(f); img.src=b64; }}
   setOut(info+"\\n\\nLoaded successfully. Use Download to save processed image (if applicable).");
   return;
  }}
  // Color tools
  if(cat==="Color Tools"){{
   var hex=getVal(input).trim() || getVal(colorEl);
   var rgb=window.ToolKit.hexToRgb(hex);
   if(!rgb){{ // try rgb input like rgb(...)
     var m=hex.match(/rgb\\s*\\(\\s*(\\d+)\\s*,\\s*(\\d+)\\s*,\\s*(\\d+)\\s*\\)/i);
     if(m){{ rgb={{r:+m[1],g:+m[2],b:+m[3]}}; hex=window.ToolKit.rgbToHex(rgb.r,rgb.g,rgb.b); }}
   }}
   if(!rgb){{ showErr("Enter valid HEX e.g. #2563eb or rgb(37,99,235)"); return; }}
   var hsl=window.ToolKit.rgbToHsl(rgb.r,rgb.g,rgb.b);
   var out="HEX: "+window.ToolKit.rgbToHex(rgb.r,rgb.g,rgb.b)+"\\nRGB: "+rgb.r+", "+rgb.g+", "+rgb.b+"\\nHSL: "+hsl.h+", "+hsl.s+"%, "+hsl.l+"%\\nName: "+window.ToolKit.colorName(hex)+"\\nContrast vs white: "+window.ToolKit.contrastRatio(hex,"#ffffff")+":1";
   if(preview) preview.style.background=hex;
   setOut(out);
   return;
  }}
  // Date & Time
  if(cat==="Date & Time"){{
   var d1=getVal(dateA)||getVal(input), d2=getVal(dateB);
   if(!d1){{ showErr("Please enter a date."); return; }}
   if(slug==="age-calculator"){{
    var age=window.ToolKit.age(d1); if(isNaN(age)){{ showErr("Invalid date."); return;}} setOut("Age: "+age+" years\\nDOB: "+d1+"\\nToday: "+new Date().toISOString().slice(0,10)); return;
   }}
   if(slug==="leap-year-checker"){{ var y=new Date(d1).getFullYear()||Number(d1); var is=window.ToolKit.isLeap(y); setOut(y+" is "+(is?"a leap year":"not a leap year")); return; }}
   if(slug==="day-of-week-calculator"){{ setOut(window.ToolKit.dayOfWeek(d1)||"Invalid date"); return; }}
   if(slug==="week-number-calculator"){{ setOut("Week: "+window.ToolKit.weekNumber(d1)); return; }}
   if(slug.includes("business")||slug.includes("working")){{ if(!d2){{ showErr("Enter both dates"); return;}} setOut("Business days: "+window.ToolKit.businessDays(d1,d2)); return; }}
   if(d1 && d2){{ var diff=window.ToolKit.dateDiff(d1,d2,"days"); if(isNaN(diff)){{ showErr("Invalid dates"); return;}} setOut("Days: "+diff.toFixed(2)+"\\nHours: "+(diff*24).toFixed(1)+"\\n"+window.ToolKit.duration(Math.abs(new Date(d2)-new Date(d1)))); return; }}
   if(slug==="unix-timestamp-generator"){{ var ts=window.ToolKit.toTimestamp(d1,false); setOut("Timestamp: "+ts+"\\nISO: "+window.ToolKit.fromTimestamp(ts,false)); return; }}
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
  // fallback generic
  if(!txt.trim()){{ showErr("Please enter input."); return; }}
  setOut(txt);
 }}catch(e){{ showErr(e.message||"Error") }}
}}
if(btn) btn.addEventListener("click",process);
var dl=$("#tool-download"), rs=$("#tool-reset");
if(dl) dl.addEventListener("click",function(){{ var t=getVal(output)||output.textContent; if(!t){{ showErr("Nothing to download"); return;}} window.ToolKit.downloadText(t,slug+".txt","text/plain") }});
if(rs) rs.addEventListener("click",function(){{ if(input){{ if(input.type==="file") input.value=""; else input.value="";}} if(input2) input2.value=""; if(aEl) aEl.value=""; if(bEl) bEl.value=""; if(cEl) cEl.value=""; if(dateA) dateA.value=""; if(dateB) dateB.value=""; if(output){{ output.value=""; output.textContent=""}} clearErr(); if(preview){{ preview.textContent=""; if(preview.style) preview.style.background=""}} }});
}})();
</script>"""

def tool_page(tool, slug_map):
    title=tool["title"]; desc=tool["description"]; cat=tool["category"]; slug=tool["slug"]
    seo=seo_title(title)
    canonical=f"{SITE_URL}/{slug}/"
    related=tool.get("related",[])[:8]
    # json-ld
    faq_qas=[
        (f"How do I use {title}?", f"Paste your input into the {title} tool, click Process/Calculate, and copy the result. All processing happens in your browser."),
        (f"Is {title} free and private?", "Yes, it is free and runs 100% in your browser. No data is uploaded to any server."),
        (f"Can I use {title} on mobile?", "Yes, the tool is fully responsive and works on phones, tablets and desktops."),
        (f"What makes {title} accurate?", "We use well-tested browser APIs and ToolKit helpers with validation and edge-case handling."),
    ]
    faq_json=json.dumps([{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq_qas])
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
    # Formula / examples logic
    formula_html=""
    if slug in custom_content:
        cc=custom_content[slug]
        howto_html=cc.get("howto","")
        formula_html=cc.get("formula","")
        examples=cc.get("examples","")
        faq_html=""
        for q,a in cc.get("faq",faq_qas):
            faq_html+=f'<details class="faq-item"><summary class="faq-q">{esc_txt(q)}</summary><div class="faq-a"><p>{esc_txt(a)}</p></div></details>'
    elif cat in ("Math Calculators","Finance Calculators","Business Calculators","Date & Time","Student Tools"):
        formula_html='<h2>Formula</h2><p>Used formula depends on the calculation; e.g. Simple Interest = P\u00d7R\u00d7T/100, Percentage = value\u00d7percent/100, CAGR = (FV/PV)<sup>1/n</sup>-1.</p>'
        howto_html='<h2>How to use</h2><ol style="margin-left:20px;line-height:1.8"><li>Paste or enter your input in the field above.</li><li>Click Process / Calculate to transform it locally in your browser.</li><li>Copy or Download the result; use Reset to clear.</li></ol>'
        examples=f"""
<h2>Worked examples</h2>
<div class="tool-grid">
<div class="tool-card"><h3>Example 1</h3><p>Input: Example data for {esc_txt(title)} \u2192 Output: processed result instantly with copy-ready formatting.</p></div>
<div class="tool-card"><h3>Example 2</h3><p>For {esc_txt(title)}, try entering realistic sample values (e.g. numbers 42 and 8 or a JSON snippet) and click Calculate/Process to see the output.</p></div>
</div>"""
        faq_html=""
        for q,a in faq_qas:
            faq_html+=f'<details class="faq-item"><summary class="faq-q">{esc_txt(q)}</summary><div class="faq-a"><p>{esc_txt(a)}</p></div></details>'
    else:
        formula_html='<h2>How it works</h2><p>All transformations run locally using the ToolKit library (client-side, no uploads). Input is validated before processing.</p>'
        howto_html='<h2>How to use</h2><ol style="margin-left:20px;line-height:1.8"><li>Paste or enter your input in the field above.</li><li>Click Process / Calculate to transform it locally in your browser.</li><li>Copy or Download the result; use Reset to clear.</li></ol>'
        examples=f"""
<h2>Worked examples</h2>
<div class="tool-grid">
<div class="tool-card"><h3>Example 1</h3><p>Input: Example data for {esc_txt(title)} \u2192 Output: processed result instantly with copy-ready formatting.</p></div>
<div class="tool-card"><h3>Example 2</h3><p>For {esc_txt(title)}, try entering realistic sample values (e.g. numbers 42 and 8 or a JSON snippet) and click Calculate/Process to see the output.</p></div>
</div>"""
        faq_html=""
        for q,a in faq_qas:
            faq_html+=f'<details class="faq-item"><summary class="faq-q">{esc_txt(q)}</summary><div class="faq-a"><p>{esc_txt(a)}</p></div></details>'

    ui=tool_ui(tool)
    script=inline_script(tool)
    breadcrumbs=f'<nav class="breadcrumbs" aria-label="Breadcrumb"><a href="{BASE}/">Home</a><span>\u203a</span><a href="{BASE}/#categories">{esc_txt(cat)}</a><span>\u203a</span><span aria-current="page">{esc_txt(title)}</span></nav>'

    jsonld=f"""
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"SoftwareApplication","name":"{esc(title)}","description":"{esc(desc)}","url":"{esc(canonical)}","applicationCategory":"UtilitiesApplication","operatingSystem":"Web","offers":{{"@type":"Offer","price":"0","priceCurrency":"USD"}}}}</script>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":{faq_json}}}</script>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"Home","item":"{SITE_URL}/"}},{{"@type":"ListItem","position":2,"name":"{esc(cat)}","item":"{SITE_URL}/#categories"}},{{"@type":"ListItem","position":3,"name":"{esc(title)}","item":"{esc(canonical)}"}}]}}</script>"""

    body=f"""{header_html(False)}
<main id="main" class="container">
{breadcrumbs}
<h1>{esc_txt(title)}</h1>
<p>{esc_txt(desc)}</p>
{ui}
<section style="margin-top:24px">
{howto_html}
{formula_html}
{examples}
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
<div class="tool-card"><h3>Privacy First</h3><p>Your data stays on your device. We cannot see what you enter or process. No cookies, no tracking, no uploads.</p></div>
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
        sorted_lst=sorted(lst, key=lambda x:x["title"])
        display_lst=sorted_lst[:8]
        total=len(sorted_lst)
        cards=""
        for t in display_lst:
            cards+=f'<div class="tool-card" data-search="{esc(t["title"]+" "+t["description"]+" "+t["category"])}"><h3><a href="{BASE}/{esc(t["slug"])}/">{esc_txt(t["title"])}</a></h3><p>{esc_txt(t["description"][:110])}</p></div>\n'
        anchor="cat-"+esc(cat.lower().replace(" ","-").replace("&","").replace("/","-"))
        view_all=f' <a href="#{anchor}" class="view-all">View all \u2192</a>' if total>8 else ""
        sections+=f'<section class="cat-card" id="{anchor}"><h2>{esc_txt(cat)} <span class="cat-count">{total} tools</span></h2><p>Browse {total} tools in {esc_txt(cat)}.{view_all}</p><div class="tool-grid">{cards}</div></section>\n'

    seo_title_hub="Developer & Calculator Tools — 230 Free Online Tools | DevelopersKit"
    desc_hub="Discover 230 free browser-based tools for developers, text, math, finance, dates, colors and images. Private, fast and works offline — no uploads."
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
<h1>Free Developer &amp; Calculator Tools</h1>
<p class="hero-sub">230 browser-based tools \u2014 private, fast, works offline.</p>
<p class="stats-bar">Everything runs in your browser. No sign-up. No uploads.</p>
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
    for t in sorted(tools, key=lambda x:x["slug"]):
        urls.append(f'  <url><loc>{SITE_URL}/{t["slug"]}/</loc><lastmod>{DATE}</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>')
    sitemap='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+ "\n".join(urls) + '\n</urlset>'
    with open(os.path.join(ROOT,"sitemap.xml"),"w",encoding="utf-8",newline="\n") as f: f.write(sitemap)
    # robots
    with open(os.path.join(ROOT,"robots.txt"),"w",encoding="utf-8",newline="\n") as f: f.write(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")
    print(f"Generated {len(tools)} tools + hub + about + sitemap")

if __name__=="__main__":
    main()
