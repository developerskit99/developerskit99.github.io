(()=>{function ready(fn){document.readyState!=="loading"?fn():document.addEventListener("DOMContentLoaded",fn)}
ready(()=>{var y=document.getElementById("year");if(y)y.textContent=new Date().getFullYear();
var btn=document.querySelector("[data-nav-toggle]"),menu=document.querySelector("[data-nav-menu]");
if(btn&&menu){btn.addEventListener("click",()=>{var o=menu.classList.toggle("open");btn.setAttribute("aria-expanded",o)});}
var inp=document.querySelector("[data-search-input]");
if(inp){inp.addEventListener("input",()=>{var q=inp.value.trim().toLowerCase();
document.querySelectorAll("[data-search]").forEach(el=>{var t=(el.getAttribute("data-search")||el.textContent).toLowerCase();
el.hidden=q&&!t.includes(q);el.style.display=el.hidden?"none":""})})}
document.querySelectorAll(".faq-q").forEach(q=>{q.addEventListener("click",()=>{var ex=q.getAttribute("aria-expanded")==="true";
q.setAttribute("aria-expanded",!ex);var a=document.getElementById(q.getAttribute("aria-controls"));
if(a)a.hidden=ex;var it=q.closest(".faq-item");if(it){if(ex)it.removeAttribute("open");else it.setAttribute("open","")}});q.addEventListener("keydown",e=>{if(e.key==="Enter"||e.key===" ") {e.preventDefault();q.click()}})});
document.querySelectorAll("[data-copy]").forEach(b=>{b.addEventListener("click",()=>{var sel=b.getAttribute("data-copy-target");
var src=sel?document.querySelector(sel):null;var txt=src?src.value||src.textContent:"";
copyText(txt,b)})})});
function copyText(t,btn){if(window.ToolKit&&window.ToolKit.copyText){return window.ToolKit.copyText(t,btn)}if(!t)return;function done(ok){if(!btn)return;var o=btn.textContent;btn.textContent=ok?"Copied!":"Failed";
setTimeout(()=>btn.textContent=o,1600)}
if(navigator.clipboard&&window.isSecureContext){navigator.clipboard.writeText(t).then(()=>done(1),()=>fallback(t,done))}
else fallback(t,done)}
function fallback(t,done){try{var ta=document.createElement("textarea");ta.value=t;ta.setAttribute("readonly","");
ta.style.position="fixed";ta.style.opacity="0";document.body.appendChild(ta);ta.select();
var ok=document.execCommand("copy");document.body.removeChild(ta);done(ok)}catch(e){done(0)}}
window.copyText=copyText;
})();
