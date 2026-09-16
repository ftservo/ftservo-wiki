(function () {
  const PAGE_SIZE = 24;

  const messages = {
    zh: {
      matched: (shown, total) => `找到 ${total} 个型号，当前显示 ${shown} 个`,
      empty: "没有符合当前条件的型号，请放宽筛选条件。",
      detail: "查看型号页",
      voltage: "输入电压",
      torque: "堵转扭矩",
      pending: "请咨询",
      revision: "资料版本",
      series: "系列",
      control: "控制",
    },
    en: {
      matched: (shown, total) => `${total} models found · showing ${shown}`,
      empty: "No model matches these filters. Try broader criteria.",
      detail: "Model page",
      voltage: "Input voltage",
      torque: "Stall torque",
      pending: "Contact us",
      revision: "Document revision",
      series: "series",
      control: "control",
    },
  };

  function addOptions(select, values) {
    const counts = new Map();
    values.filter(Boolean).forEach((value) => counts.set(value, (counts.get(value) || 0) + 1));
    [...counts.keys()].sort((a, b) => String(a).localeCompare(String(b), undefined, { numeric: true })).forEach((value) => {
      const option = document.createElement("option");
      option.value = value;
      option.textContent = `${value} (${counts.get(value)})`;
      select.appendChild(option);
    });
  }


  function addVoltageOptions(select, items) {
    const groups = new Map();
    items.filter((item) => item.voltage != null).forEach((item) => {
      const key = String(item.voltage);
      const current = groups.get(key) || { count: 0, label: item.voltageLabel || `${item.voltage} V` };
      current.count += 1;
      groups.set(key, current);
    });
    [...groups.entries()].sort((a, b) => Number(a[0]) - Number(b[0])).forEach(([value, entry]) => {
      const option = document.createElement("option");
      option.value = value;
      option.textContent = `${entry.label} (${entry.count})`;
      select.appendChild(option);
    });
  }

  function buildCard(item, copy) {
    const article = document.createElement("article");
    article.className = "ft-selector-card";

    const top = document.createElement("div");
    top.className = "ft-selector-card-top";
    const title = document.createElement("h3");
    title.textContent = item.model;
    const badges = document.createElement("div");
    badges.className = "ft-selector-badges";
    [item.family, item.interface].filter(Boolean).forEach((value) => {
      const badge = document.createElement("span");
      badge.textContent = value;
      badges.appendChild(badge);
    });
    top.append(title, badges);

    const identity = document.createElement("p");
    identity.className = "ft-selector-identity";
    identity.textContent = item.coverModel && item.coverModel !== item.model
      ? `${item.coverModel}${item.revision ? ` · ${copy.revision} ${item.revision}` : ""}`
      : (item.revision ? `${copy.revision} ${item.revision}` : item.sourceGroup);

    const metrics = document.createElement("dl");
    metrics.className = "ft-selector-metrics";
    const metricRows = [
      [copy.voltage, item.voltage == null ? copy.pending : item.voltageLabel || `${item.voltage} V`],
      [copy.torque, item.torque == null ? copy.pending : item.torqueLabel || item.torqueLabel || item.torqueLabel || item.torqueLabel || `${item.torque} kg·cm`],
    ];
    metricRows.forEach(([label, value]) => {
      const wrapper = document.createElement("div");
      const dt = document.createElement("dt");
      const dd = document.createElement("dd");
      dt.textContent = label;
      dd.textContent = value;
      wrapper.append(dt, dd);
      metrics.appendChild(wrapper);
    });

    const description = document.createElement("p");
    description.className = "ft-selector-description";
    description.textContent = `${item.family} ${copy.series} · ${item.interface} ${copy.control}`;

    const actions = document.createElement("div");
    actions.className = "ft-selector-actions";
    const detail = document.createElement("a");
    detail.href = item.detail;
    detail.textContent = copy.detail;
    detail.className = "ft-selector-detail";
    actions.appendChild(detail);

    article.append(top, identity, metrics, description, actions);
    return article;
  }

  function initSelector() {
    const root = document.getElementById("ft-servo-selector");
    if (!root || root.dataset.ready === "true") return;
    const data = Array.isArray(window.FEETECH_SERVO_DATA) ? window.FEETECH_SERVO_DATA : [];
    if (!data.length) return;
    root.dataset.ready = "true";

    const locale = root.dataset.locale === "en" ? "en" : "zh";
    const copy = messages[locale];
    const controls = Object.fromEntries([...root.querySelectorAll("[data-filter]")].map((el) => [el.dataset.filter, el]));
    const results = root.querySelector(".ft-selector-results");
    const status = root.querySelector(".ft-selector-status");
    const more = root.querySelector('[data-action="more"]');
    const reset = root.querySelector('[data-action="reset"]');
    let visible = PAGE_SIZE;

    addOptions(controls.interface, data.map((item) => item.interface));
    addOptions(controls.family, data.map((item) => item.family));
    addVoltageOptions(controls.voltage, data);

    function filteredData() {
      const query = controls.query.value.trim().toLowerCase();
      const minTorque = controls.torque.value === "" ? null : Number(controls.torque.value);
      const filtered = data.filter((item) => {
        const haystack = `${item.model} ${item.coverModel} ${item.family} ${item.interface} ${item.description}`.toLowerCase();
        if (query && !haystack.includes(query)) return false;
        if (controls.interface.value && item.interface !== controls.interface.value) return false;
        if (controls.family.value && item.family !== controls.family.value) return false;
        if (controls.voltage.value && String(item.voltage) !== controls.voltage.value) return false;
        if (minTorque != null && (!Number.isFinite(item.torque) || item.torque < minTorque)) return false;
        return true;
      });

      const sort = controls.sort.value;
      filtered.sort((a, b) => {
        if (sort === "torque-desc") return (b.torque ?? -Infinity) - (a.torque ?? -Infinity);
        if (sort === "torque-asc") return (a.torque ?? Infinity) - (b.torque ?? Infinity);
        if (sort === "voltage") return (a.voltage ?? Infinity) - (b.voltage ?? Infinity);
        return a.model.localeCompare(b.model, undefined, { numeric: true });
      });
      return filtered;
    }

    function render() {
      const filtered = filteredData();
      const shown = Math.min(visible, filtered.length);
      results.replaceChildren(...filtered.slice(0, shown).map((item) => buildCard(item, copy)));
      if (!filtered.length) {
        const empty = document.createElement("p");
        empty.className = "ft-selector-empty";
        empty.textContent = copy.empty;
        results.appendChild(empty);
      }
      status.textContent = copy.matched(shown, filtered.length);
      more.hidden = shown >= filtered.length;
    }

    Object.values(controls).forEach((control) => {
      control.addEventListener(control.tagName === "INPUT" ? "input" : "change", () => {
        visible = PAGE_SIZE;
        render();
      });
    });
    more.addEventListener("click", () => { visible += PAGE_SIZE; render(); });
    reset.addEventListener("click", () => {
      Object.entries(controls).forEach(([key, control]) => { control.value = key === "sort" ? "model" : ""; });
      visible = PAGE_SIZE;
      render();
      controls.query.focus();
    });
    render();
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", initSelector);
  else initSelector();
  if (typeof document$ !== "undefined") document$.subscribe(initSelector);
})();
