(() => {
  'use strict';
  const assetRoot = new URL('../products/', document.currentScript.src);
  const keys = ['interface', 'family', 'voltage', 'torque', 'speed', 'positionRange', 'motor', 'gear', 'case', 'shaft', 'dimensions', 'weight', 'continuous', 'pending', 'more', 'detail', 'placeholder'];
  const words = {
    zh: ['控制接口', '产品系列', '输入电压', '堵转扭矩', '空载速度', '位置控制范围', '电机类型', '齿轮材质', '外壳材质', '输出轴型', '外形尺寸', '重量', '连续旋转', '待补充', '更多参数', '查看型号页', '占位图 · HL-3950-C001'],
    en: ['Control interface', 'Family', 'Input voltage', 'Stall torque', 'No-load speed', 'Position control range', 'Motor type', 'Gear material', 'Case material', 'Shaft', 'Dimensions', 'Weight', 'Continuous rotation', 'Not provided', 'More specifications', 'Model page', 'Placeholder · HL-3950-C001']
  };
  const options = {
    motor: [['brushed-iron', '有刷铁心', 'Brushed iron-core'], ['brushed-coreless', '有刷空心杯', 'Brushed coreless'], ['brushless-coreless', '无刷空心杯', 'Brushless coreless']],
    gear: [['copper', '铜齿', 'Copper'], ['steel', '钢齿', 'Steel'], ['titanium', '钛齿', 'Titanium'], ['plastic', '塑胶', 'Plastic']],
    case: [['plastic', '全塑胶', 'All plastic'], ['metal', '全金属', 'All metal'], ['hybrid', '铝中壳+塑胶', 'Aluminum middle + plastic']],
    shaft: [['single', '单轴', 'Single shaft'], ['dual', '双轴', 'Dual shaft']],
    continuous: [['true', '支持', 'Supported'], ['false', '不支持', 'Not supported']]
  };
  const numeric = {
    torque: ['torque', 'min'], torqueMax: ['torque', 'max'],
    speed: ['speed', 'min'], speedMax: ['speed', 'max'],
    positionRange: ['positionRange', 'min'], maxEdge: ['maxEdge', 'max'], weight: ['weight', 'max']
  };
  const basicCategories = ['interface', 'family', 'voltage'];
  const finite = value => typeof value === 'number' && Number.isFinite(value);
  const normalize = value => String(value || '').normalize('NFKC').toLowerCase().replace(/[\s\-_·]/g, '');
  function element(tag, className, text) {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (text != null) node.textContent = text;
    return node;
  }
  function valueOf(item, key, en, copy) {
    const value = item[key];
    if (['voltage', 'torque', 'speed'].includes(key)) return finite(value) ? item[key + 'Label'] || `${value} ${key === 'voltage' ? 'V' : key === 'torque' ? 'kg·cm' : 'rpm'}` : copy.pending;
    if (key === 'dimensions') return Array.isArray(value) ? value.join(' × ') + ' mm' : copy.pending;
    if (key === 'weight') return finite(value) ? `${value}${item.weightTolerance ? ' ± ' + item.weightTolerance : ''} g` : copy.pending;
    if (key === 'positionRange') return finite(value) ? value + '°' : copy.pending;
    if (key === 'continuous') return typeof value === 'boolean' ? (en ? (value ? 'Supported' : 'Not supported') : (value ? '支持' : '不支持')) : copy.pending;
    if (!value && item[key + 'Note']) return en ? item[key + 'NoteEn'] || item[key + 'Note'] : item[key + 'Note'];
    return options[key]?.find(option => option[0] === value)?.[en ? 2 : 1] || copy.pending;
  }
  const desktop = matchMedia('(min-width: 900px) and (hover: hover) and (pointer: fine)');
  let preview, activeCard, closeTimer;
  function closePreview() {
    clearTimeout(closeTimer);
    if (preview) { preview.hidePopover(); preview.remove(); preview = null; }
    activeCard?.querySelector('.ft-card-preview-button')?.setAttribute('aria-expanded', 'false');
    activeCard = null;
  }
  function scheduleClose() { closeTimer = setTimeout(closePreview, 180); }
  function showPreview(article, item, en, copy) {
    if (!desktop.matches) return;
    clearTimeout(closeTimer);
    if (activeCard === article) return;
    closePreview();
    activeCard = article;
    preview = element('aside', 'md-typeset ft-product-preview');
    preview.setAttribute('popover', 'manual');
    preview.setAttribute('aria-label', item.model + ' ' + copy.more);
    const heading = element('div', 'ft-preview-heading');
    const close = element('button', 'ft-preview-close', '×');
    close.type = 'button'; close.setAttribute('aria-label', en ? 'Close preview' : '关闭预览');
    close.addEventListener('click', () => { closePreview(); article.querySelector('.ft-card-preview-button').focus(); });
    heading.append(element('strong', null, item.model), close);
    const media = element('div', 'ft-preview-media');
    for (const drawing of [false, true]) {
      const figure = element('figure');
      const img = element('img');
      const path = drawing ? item.drawing : item.image;
      img.src = new URL(path || 'models/hl-3950-c001/images/' + (drawing ? 'drawing.png' : 'main.webp'), assetRoot);
      const label = drawing ? (en ? 'Mechanical drawing' : '机身尺寸图') : (en ? 'Product' : '产品主图');
      img.alt = path ? item.model + ' · ' + label : copy.placeholder + ' · ' + label;
      const link = element('a'); link.href = img.src; link.target = '_blank'; link.rel = 'noopener';
      link.setAttribute('aria-label', en ? 'Open full-size ' + img.alt : '查看原图：' + img.alt);
      link.append(img);
      figure.append(link, element('figcaption', null, path ? label : copy.placeholder));
      media.append(figure);
    }
    const list = element('dl', 'ft-preview-specs');
    ['voltage', 'torque', 'speed', 'positionRange', 'continuous', 'motor', 'gear', 'case', 'shaft', 'dimensions', 'weight'].forEach(key => {
      const row = element('div');
      row.append(element('dt', null, copy[key]), element('dd', null, valueOf(item, key, en, copy)));
      list.append(row);
    });
    const note = element('p', 'ft-preview-note', item.drawing
      ? (en ? 'Click an image to view full size.' : '点击图片可查看原图。')
      : (en ? 'Drawing placeholder: HL-3950-C001. Not this model’s dimensions.' : '图纸为 HL-3950-C001 占位图，不代表本型号尺寸。'));
    if (item.specificationNote) note.append(document.createTextNode(' ' + (en ? item.specificationNoteEn : item.specificationNote) + (en ? '; see the model page.' : '，详见型号页。')));
    preview.append(heading, media, list, note);
    document.body.append(preview);
    preview.showPopover();
    const rect = article.getBoundingClientRect();
    const width = Math.min(480, innerWidth - 32);
    // Place the preview on the opposite side, outside the hovered card.
    const left = rect.left >= width + 24 ? rect.left - width - 12 : Math.min(rect.right + 12, innerWidth - width - 16);
    preview.style.width = width + 'px';
    preview.style.left = Math.max(16, left) + 'px';
    preview.style.top = Math.max(64, Math.min(rect.top, innerHeight - preview.offsetHeight - 16)) + 'px';
    article.querySelector('.ft-card-preview-button').setAttribute('aria-expanded', 'true');
    preview.addEventListener('mouseenter', () => clearTimeout(closeTimer));
    preview.addEventListener('mouseleave', scheduleClose);
  }
  function details(item, en, copy) {
    const panel = element('div', 'ft-card-details');
    const button = element('button', 'ft-card-preview-button', en ? 'Quick view' : '参数预览');
    button.type = 'button'; button.setAttribute('aria-expanded', 'false');
    panel.append(button);
    return panel;
  }
  function hoverDetails(article, item, en, copy) {
    article.addEventListener('mouseenter', () => showPreview(article, item, en, copy));
    article.addEventListener('mouseleave', scheduleClose);
    article.querySelector('.ft-card-preview-button').addEventListener('click', () => showPreview(article, item, en, copy));
    article.addEventListener('click', event => {
      if (!desktop.matches && !event.target.closest('a, button')) article.querySelector('.ft-selector-detail').click();
    });
  }
  document.addEventListener('keydown', event => { if (event.key === 'Escape') closePreview(); });
  document.addEventListener('pointerdown', event => {
    if (preview && !preview.contains(event.target) && !activeCard.contains(event.target)) closePreview();
  });
  document.addEventListener('scroll', event => {
    if (preview && !preview.contains(event.target)) closePreview();
  }, true);
  window.addEventListener('resize', closePreview);
  desktop.addEventListener('change', closePreview);
  function card(item, en, copy) {
    const article = element('article', 'ft-selector-card');
    const figure = element('figure', 'ft-product-image');
    const img = element('img');
    img.src = new URL(item.image || 'models/hl-3950-c001/images/main.webp', assetRoot);
    img.alt = item.image ? item.model : copy.placeholder;
    img.loading = 'lazy'; img.width = 800; img.height = 800;
    figure.append(img, element('figcaption', null, item.image ? '' : copy.placeholder));
    const heading = element('div', 'ft-selector-card-top');
    const badges = element('div', 'ft-selector-badges');
    [item.family, item.interface].forEach(value => badges.append(element('span', null, value)));
    heading.append(element('h3', null, item.model), badges);
    const metrics = element('dl', 'ft-selector-metrics');
    ['voltage', 'torque', 'speed'].forEach(key => {
      const row = element('div');
      row.append(element('dt', null, copy[key]), element('dd', null, valueOf(item, key, en, copy)));
      metrics.append(row);
    });
    const actions = element('div', 'ft-selector-actions');
    const link = element('a', 'ft-selector-detail', copy.detail);
    link.href = item.detail; actions.append(link);
    article.append(figure, heading, metrics, details(item, en, copy), actions);
    hoverDetails(article, item, en, copy);
    return article;
  }
  function init() {
    const data = window.FEETECH_SERVO_DATA || [];
    const en = document.documentElement.lang.startsWith('en');
    const copy = Object.fromEntries(keys.map((key, index) => [key, words[en ? 'en' : 'zh'][index]]));
    document.querySelectorAll('.servo-catalog-card:not([data-enhanced])').forEach(article => {
      const id = article.querySelector('a')?.getAttribute('href')?.match(/models\/([^/]+)\//)?.[1];
      const item = data.find(model => model.model.toLowerCase() === id);
      if (!item) return;
      article.dataset.enhanced = 'true';
      article.insertBefore(details(item, en, copy), article.querySelector('.ft-selector-actions'));
      hoverDetails(article, item, en, copy);
    });
    const root = document.getElementById('ft-servo-selector');
    if (!root || root.dataset.ready || !data.length) return;
    root.dataset.ready = 'true';
    const controls = [...root.querySelectorAll('[data-filter]')];
    const groups = [...root.querySelectorAll('[data-group]')];
    const categoryOptions = {};
    groups.forEach(group => {
      const key = group.dataset.group;
      const values = options[key] || [...new Set(data.map(item => key === 'voltage' ? String(item.voltage ?? '') : item[key]).filter(Boolean))]
        .sort((a, b) => (key === 'family' ? (a === 'HLS' ? 0 : a === 'STS' ? 1 : 2) - (b === 'HLS' ? 0 : b === 'STS' ? 1 : 2) : 0) || String(a).localeCompare(String(b), undefined, {numeric: true}))
        .map(value => [value, key === 'voltage' ? value + ' V' : value, key === 'voltage' ? value + ' V' : value]);
      categoryOptions[key] = values.map(option => option[0]);
      values.forEach(([value, zh, english]) => {
        const label = element('label');
        const input = element('input'); input.type = 'checkbox'; input.value = value;
        label.append(input, document.createTextNode(en ? english : zh)); group.append(label);
        const select = root.querySelector(`[data-category="${key}"]`);
        if (select) { const option = element('option', null, en ? english : zh); option.value = value; select.append(option); }
      });
    });
    const advanced = root.querySelector('[data-action="advanced"]');
    const sidebar = root.querySelector('.ft-selector-sidebar');
    const results = root.querySelector('.ft-selector-results');
    const scrollRegion = root.querySelector('.ft-results-scroll');
    const status = root.querySelector('.ft-selector-status');
    const more = root.querySelector('[data-action="more"]');
    const state = {query: '', sort: 'recommended'};
    Object.keys(numeric).forEach(key => state[key] = '');
    groups.forEach(group => state[group.dataset.group] = []);
    let professional = false, visible = 24;

    // Both modes edit the same state. Multi-select choices survive mode switches.
    function syncControls() {
      controls.forEach(input => { if (input.value !== state[input.dataset.filter]) input.value = state[input.dataset.filter]; });
      groups.forEach(group => group.querySelectorAll('input').forEach(input => input.checked = state[group.dataset.group].includes(input.value)));
      root.querySelectorAll('[data-category]').forEach(select => {
        const choices = state[select.dataset.category];
        select.querySelector('[data-multiple]')?.remove();
        if (choices.length > 1) {
          const option = element('option', null, en ? `${choices.length} selected` : `已选 ${choices.length} 项`);
          option.dataset.multiple = 'true'; option.value = choices.join(','); select.append(option);
        }
        select.value = choices.join(',');
      });
      root.querySelectorAll('[data-range-for]').forEach(slider => {
        slider.value = state[slider.dataset.rangeFor] || slider.dataset.default;
        slider.setAttribute('aria-valuetext', state[slider.dataset.rangeFor] || (en ? 'Unrestricted' : '不限'));
      });
      root.classList.toggle('is-professional', professional);
      sidebar.hidden = !professional;
      root.querySelector('.ft-selector-basic').hidden = professional;
      advanced.setAttribute('aria-expanded', String(professional));
      advanced.textContent = en ? (professional ? 'Basic selection' : 'Professional selection') : (professional ? '基础选型' : '专业选型');
    }
    function render() {
      closePreview();
      const invalidRange = professional && ['torque', 'speed'].some(key => state[key] !== '' && state[key + 'Max'] !== '' && Number(state[key]) > Number(state[key + 'Max']));
      const rows = invalidRange ? [] : data.filter(item => {
        if (state.query && !normalize(`${item.model} ${item.coverModel} ${item.family} ${item.interface}`).includes(normalize(state.query))) return false;
        for (const group of groups) {
          const key = group.dataset.group;
          if (!professional && !basicCategories.includes(key)) continue;
          if (state[key].length && !state[key].includes(String(item[key]))) return false;
        }
        for (const [key, [field, direction]] of Object.entries(numeric)) {
          if (!professional && !['torque', 'speed'].includes(key)) continue;
          if (state[key] === '') continue;
          const value = field === 'maxEdge' ? (Array.isArray(item.dimensions) ? Math.max(...item.dimensions) : null) : item[field];
          const limit = Number(state[key]);
          if (!finite(value) || (direction === 'min' ? value < limit : value > limit)) return false;
        }
        return true;
      });
      const [field, direction] = state.sort.split('-');
      rows.sort((a, b) => {
        const rank = item => item.family === 'HLS' ? 0 : item.family === 'STS' ? 1 : 2;
        const priority = rank(a) - rank(b);
        if (priority) return priority;
        if (['torque', 'speed', 'weight'].includes(field)) {
          if (!finite(a[field])) return finite(b[field]) ? 1 : 0;
          if (!finite(b[field])) return -1;
          const difference = (a[field] - b[field]) * (direction === 'desc' ? -1 : 1);
          if (difference) return difference;
        }
        return a.model.localeCompare(b.model, undefined, {numeric: true});
      });
      const shown = Math.min(visible, rows.length);
      results.replaceChildren(...rows.slice(0, shown).map(item => card(item, en, copy)));
      if (!rows.length) results.append(element('p', 'ft-selector-empty', invalidRange
        ? (en ? 'The minimum must not exceed the maximum.' : '下限不能大于上限，请调整范围。')
        : (en ? 'No matching models. Broaden filters; unknown parameters cannot match an active filter.' : '没有符合条件的型号。请放宽条件；未提供的参数不能满足该项筛选。')));
      status.textContent = en ? `${rows.length} models found · showing ${shown}` : `找到 ${rows.length} 个型号，当前显示 ${shown} 个`;
      more.hidden = shown === rows.length;
    }
    function write() {
      const url = new URL(location.href);
      Object.entries(state).forEach(([key, value]) => {
        const parameter = key === 'query' ? 'model_query' : key;
        const text = Array.isArray(value) ? value.join(',') : value;
        if (text && !(key === 'sort' && text === 'recommended')) url.searchParams.set(parameter, text);
        else url.searchParams.delete(parameter);
      });
      if (professional) url.searchParams.set('professional', '1'); else url.searchParams.delete('professional');
      history.replaceState(null, '', url);
      document.querySelectorAll('.md-select__link[hreflang]').forEach(link => {
        const target = new URL(link.href); target.search = url.search; link.href = target.href;
      });
    }
    function read() {
      const params = new URLSearchParams(location.search);
      Object.keys(state).forEach(key => {
        const value = params.get(key === 'query' ? 'model_query' : key) || '';
        if (Array.isArray(state[key])) state[key] = value.split(',').filter(v => categoryOptions[key].includes(v));
        else if (key === 'sort') state[key] = ['recommended', 'model', 'torque-desc', 'torque-asc', 'speed-desc', 'weight-asc'].includes(value) ? value : 'recommended';
        else if (key in numeric) state[key] = value !== '' && Number.isFinite(Number(value)) && Number(value) >= 0 ? value : '';
        else state[key] = value;
      });
      professional = params.get('professional') === '1'; visible = 24;
      syncControls(); render();
    }
    function update(event) {
      const input = event.target;
      if (input.matches('[data-filter]')) {
        const key = input.dataset.filter;
        state[key] = key in numeric && input.value !== '' ? String(Math.max(0, Number(input.value))) : input.value;
      } else if (input.matches('[data-range-for]')) state[input.dataset.rangeFor] = input.value;
      else if (input.matches('[data-category]')) state[input.dataset.category] = input.value ? input.value.split(',') : [];
      else if (input.matches('input[type="checkbox"]')) {
        const group = input.closest('[data-group]');
        state[group.dataset.group] = [...group.querySelectorAll('input:checked')].map(checkbox => checkbox.value);
      } else return;
      visible = 24; syncControls(); write(); render(); scrollRegion.scrollTop = 0;
    }
    root.addEventListener('input', event => { if (event.target.tagName !== 'SELECT') update(event); });
    root.addEventListener('change', event => { if (event.target.tagName === 'SELECT') update(event); });
    advanced.addEventListener('click', () => {
      professional = !professional; visible = 24; syncControls(); write(); render();
      if (professional) root.scrollIntoView({block: 'start'});
    });
    root.querySelector('[data-action="reset"]').addEventListener('click', () => {
      Object.keys(state).forEach(key => state[key] = Array.isArray(state[key]) ? [] : key === 'sort' ? 'recommended' : '');
      visible = 24; syncControls(); write(); render(); scrollRegion.scrollTop = 0;
    });
    more.addEventListener('click', () => { visible += 24; render(); });
    window.addEventListener('popstate', () => { if (root.isConnected) read(); });
    read();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
  if (typeof document$ !== 'undefined') document$.subscribe(init);
})();
