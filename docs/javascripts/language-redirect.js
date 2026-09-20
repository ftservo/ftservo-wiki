(function () {
  "use strict";
  var script = document.currentScript;
  if (!script) return;

  var siteRoot = new URL("../", script.src);
  siteRoot.pathname = siteRoot.pathname.replace(/en\/$/, "");
  var currentPath = window.location.pathname.replace(/\/index\.html$/, "/");
  var rootPath = siteRoot.pathname.replace(/\/index\.html$/, "/");

  // Resolve the same page against the actual serving root, including local
  // preview and project subpaths. Both languages have matching page coverage.
  if (currentPath.indexOf(rootPath) !== 0) return;
  var pagePath = currentPath.slice(rootPath.length).replace(/^en\//, "");
  var preferenceKey = "feetech-language:" + rootPath;
  document.querySelectorAll('.md-select__link[hreflang]').forEach(function (link) {
    var locale = link.getAttribute("hreflang");
    if (locale !== "zh" && locale !== "en") return;
    var target = new URL((locale === "en" ? "en/" : "") + pagePath, siteRoot);
    target.search = window.location.search;
    // Translated headings have different generated anchors, so land at the
    // translated page's title rather than a potentially nonexistent fragment.
    link.href = target.href;
    link.addEventListener("click", function (event) {
      try { sessionStorage.setItem(preferenceKey, locale); } catch (_) { /* Optional. */ }
      if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey || event.button !== 0) return;
      event.preventDefault();
      event.stopPropagation();
      window.location.assign(link.href);
    });
  });

  // Only redirect the neutral home page. Keep direct links and manual language
  // choices stable.
  if (currentPath !== rootPath) return;

  var preferred;
  try { preferred = sessionStorage.getItem(preferenceKey); } catch (_) { /* Optional. */ }
  if (preferred === "zh") return;

  var language = (navigator.language || "").toLowerCase();
  var prefersChinese =
    language === "zh-cn" ||
    language === "zh-sg" ||
    language.indexOf("zh-hans") === 0;

  if (preferred === "en" || !prefersChinese) {
    var home = new URL("en/", siteRoot);
    home.search = window.location.search;
    window.location.replace(home.href);
  }
})();
