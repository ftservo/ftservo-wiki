(function () {
  "use strict";
  var script = document.currentScript;
  if (!script) return;

  var siteRoot = new URL("../", script.src);
  var currentPath = window.location.pathname.replace(/\/index\.html$/, "/");
  var rootPath = siteRoot.pathname.replace(/\/index\.html$/, "/");

  // Only redirect the neutral home page. Keep direct links and manual language
  // choices stable.
  if (currentPath !== rootPath) return;

  var language = (navigator.language || "").toLowerCase();
  var prefersChinese =
    language === "zh-cn" ||
    language === "zh-sg" ||
    language.indexOf("zh-hans") === 0;

  if (!prefersChinese) window.location.replace(new URL("en/", siteRoot).href);
})();

