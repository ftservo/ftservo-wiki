(() => {
  "use strict";
  const script = document.currentScript;
  if (!script) return;
  const siteRoot = new URL("../", script.src);
  // i18n can serve the shared script from either the neutral or translated root.
  siteRoot.pathname = siteRoot.pathname.replace(/en\/$/, "");
  const en = document.documentElement.lang.startsWith("en");
  const languageRoot = new URL(en ? "en/" : "./", siteRoot);
  const storageKey = `feetech-reference-model:${siteRoot.pathname}`;
  const items = window.FEETECH_SERVO_DATA || [];
  const find = (id) => items.find((item) => item.model.toLowerCase() === String(id).toLowerCase());
  let selected;
  const pathModel = window.location.pathname.match(/\/products\/models\/([^/]+)\//)?.[1];
  const params = new URLSearchParams(window.location.search);
  let saved = null;
  try { saved = sessionStorage.getItem(storageKey); } catch (_) { /* Storage can be disabled. */ }
  selected = find(pathModel || (params.has("model") ? params.get("model") : saved));
  try {
    if (selected) sessionStorage.setItem(storageKey, selected.model.toLowerCase());
    else sessionStorage.removeItem(storageKey);
  } catch (_) { /* Direct links still work without storage. */ }

  function init() {
    const article = document.querySelector(".md-content__inner");
    if (!article || !selected) return;
    const relative = window.location.pathname.slice(languageRoot.pathname.length);
    if (!/^(sdk\/|getting-started\/|mechanical\/|reference\/|tools\/|troubleshooting\/|downloads\/)/.test(relative)) return;
    if (article.querySelector(".ft-model-context")) return;
    const root = document.createElement("aside");
    root.className = "ft-model-context";
    root.setAttribute("aria-label", en ? "Reference model" : "当前参考型号");
    const heading = document.createElement("strong");
    heading.textContent = `${en ? "Reference model" : "当前参考型号"}：${selected.model} · ${selected.interface}`;
    const note = document.createElement("p");
    note.textContent = en
      ? "This is a shared guide. Confirm the model, firmware and supplied resources before applying settings."
      : "本页是共享指南，应用具体参数前仍需核对该型号、固件及已提供的资料。";
    const actions = document.createElement("div");
    actions.className = "ft-model-context-actions";
    const link = (label, path) => {
      const element = document.createElement("a");
      element.textContent = label;
      element.href = new URL(path, languageRoot).href;
      actions.append(element);
    };
    const id = selected.model.toLowerCase();
    link(en ? "Model and files" : "型号与资料", `products/models/${id}/main/#resources`);
    link(en ? "Control guide" : "型号控制说明", `products/models/${id}/software/`);
    link(en ? "Mechanical guide" : "型号安装说明", `products/models/${id}/mechanical/`);
    link(en ? "Change model" : "更换型号", `products/?model_query=${encodeURIComponent(selected.model)}`);
    if (selected.interface === "PWM" && !relative.startsWith("getting-started/pwm/")) {
      link(en ? "PWM getting started" : "PWM 入门路线", "getting-started/pwm/");
      note.textContent = en
        ? "This reference model uses PWM. Serial-bus IDs, register tables and SDK examples do not apply to its PWM interface."
        : "当前参考型号为 PWM；串行总线 ID、寄存器表及总线 SDK 示例不适用于它的 PWM 接口。";
    }
    const clear = document.createElement("button");
    clear.type = "button";
    clear.textContent = en ? "Clear reference" : "清除参考型号";
    clear.addEventListener("click", () => {
      selected = null;
      try { sessionStorage.removeItem(storageKey); } catch (_) { /* Optional storage. */ }
      const url = new URL(window.location.href);
      url.searchParams.delete("model");
      window.history.replaceState(null, "", url);
      root.remove();
      const heading = article.querySelector("h1");
      if (heading) { heading.tabIndex = -1; heading.focus(); }
    });
    actions.append(clear);
    root.append(heading, note, actions);
    const title = article.querySelector("h1");
    if (title) title.after(root);
    else article.prepend(root);
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
