/*! Shared demo chrome injector */
(function () {
 var root = document.documentElement;
 var title = root.getAttribute("data-demo-title") || document.title || "Demo";
 var one = root.getAttribute("data-demo-one-liner") || root.getAttribute("data-demo-one") || "";
 var tier = (root.getAttribute("data-demo-tier") || "L0").toUpperCase();
 var howto = root.getAttribute("data-demo-howto") || "";
 var back = root.getAttribute("data-demo-back") || "./index.html";
 var claim = root.getAttribute("data-demo-claim") || "";

 function el(tag, cls, text) {
 var n = document.createElement(tag);
 if (cls) n.className = cls;
 if (text != null) n.textContent = text;
 return n;
 }

 function mount() {
 if (document.querySelector(".demo-chrome")) return;
 var bar = el("div", "demo-chrome");
 bar.setAttribute("role", "navigation");
 bar.setAttribute("aria-label", "作品集导航");

 var a = el("a", "demo-chrome-back", "← 作品集");
 a.href = back;

 var meta = el("div", "demo-chrome-meta");
 meta.appendChild(el("div", "demo-chrome-title", title));
 if (one) meta.appendChild(el("div", "demo-chrome-one", one));

 var badge = el("span", "demo-chrome-badge" + (tier === "L1" ? " l1" : ""), tier);
 badge.title = tier === "L0" ? "旗舰深打磨" : "壳层统一";

 bar.appendChild(a);
 bar.appendChild(meta);
 bar.appendChild(badge);
 if (claim) {
 var claimEl = el("span", "demo-chrome-claim", claim);
 bar.appendChild(claimEl);
 }

 var first = document.body.firstChild;
 document.body.insertBefore(bar, first);

 if (howto) {
 var tip = el("p", "demo-chrome-howto");
 tip.innerHTML = "<strong>60 秒怎么玩：</strong> " + howto;
 bar.insertAdjacentElement("afterend", tip);
 }
 }

 if (document.readyState === "loading") {
 document.addEventListener("DOMContentLoaded", mount);
 } else {
 mount();
 }
})();
