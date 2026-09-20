(() => {
  "use strict";

  const SVG_NS = "http://www.w3.org/2000/svg";
  const isEnglish = document.documentElement.lang.startsWith("en");
  const copy = isEnglish ? {
    speed: "Speed", current: "Current", efficiency: "Efficiency", power: "Power",
    torque: "Torque", dataSource: "Torque-test fixture", noPoints: "The test result does not contain enough valid points to draw a characteristic curve.",
    smooth: "Smoothed trend", raw: "Measured points", toggleRaw: "Show measured points", toggleSmooth: "Smooth curves",
    fixed: "Fixed model ranges", invalidAxes: "The test result is missing valid axis ranges.",
    estimate: "Smoothed estimate", measured: "Measured value", points: "measurement points", legend: "Curve legend",
    hint: "Hover or touch to inspect five parameters. Use ← / → when the chart is focused. Scroll horizontally on small screens.",
    outside: "points outside the model ranges", hidden: "points after peak torque hidden", unavailable: "No valid readings",
    noSource: "No test-result JSON file has been configured.", loadError: "Unable to load characteristic-curve data",
  } : {
    speed: "转速", current: "电流", efficiency: "效率", power: "功率",
    torque: "扭矩", dataSource: "扭矩测试工装", noPoints: "测试结果中没有足够的有效测点，无法绘制特性曲线。",
    smooth: "平滑趋势", raw: "原始测点", toggleRaw: "恢复折线", toggleSmooth: "平滑曲线",
    fixed: "固定型号量程", invalidAxes: "测试结果缺少有效的坐标轴量程。",
    estimate: "平滑估算值", measured: "原始测量值", points: "个测量点", legend: "曲线图例",
    hint: "移动鼠标或触摸查看五项参数；聚焦图表后可用 ← / → 选点，小屏可横向滚动。",
    outside: "点超出型号量程", hidden: "个峰值后测点已隐藏", unavailable: "无有效读数",
    noSource: "未设置测试结果 JSON 文件。", loadError: "无法读取特性曲线数据",
  };
  const METRICS = [
    { key: "efficiency_pct", label: copy.efficiency, unit: "%", color: "#68b933", axisX: 58, labelX: 17, side: -1 },
    { key: "speed_rpm", label: copy.speed, unit: "RPM", color: "#8f49bc", axisX: 130, labelX: 87, side: -1 },
    { key: "current_a", label: copy.current, unit: "A", color: "#098cd1", axisX: 760, labelX: 815, side: 1 },
    { key: "power_w", label: copy.power, unit: "W", color: "#d6a20c", axisX: 862, labelX: 903, side: -1 },
  ];
  const SMOOTH_POINT_COUNT = 181;
  const SMOOTH_MIN_SAMPLES = 4;
  const SMOOTH_SERIES_KEYS = METRICS.map((metric) => metric.key);

  function element(name, attributes = {}, content = "") {
    const node = document.createElementNS(SVG_NS, name);
    Object.entries(attributes).forEach(([key, value]) => node.setAttribute(key, String(value)));
    node.textContent = content;
    return node;
  }

  function numeric(value) {
    if (value === null || value === undefined || value === "" || typeof value === "boolean") return null;
    const number = Number(value);
    return Number.isFinite(number) ? number : null;
  }

  function format(value, axis) {
    return Number.isFinite(value) ? value.toFixed(axis.decimals ?? 2) : "—";
  }

  // Ported from the torque-test fixture ui/static/app.js. Keep smoothing identical.
function clampNumber(value, minimum, maximum) {
  return Math.min(Math.max(value, minimum), maximum);
}

function medianValue(values) {
  if (!values.length) return null;
  const sorted = [...values].sort((first, second) => first - second);
  const middle = Math.floor(sorted.length / 2);
  return sorted.length % 2
    ? sorted[middle]
    : (sorted[middle - 1] + sorted[middle]) / 2;
}

function positiveSteps(points) {
  const steps = [];
  for (let index = 1; index < points.length; index += 1) {
    const step = points[index].torque_nm - points[index - 1].torque_nm;
    if (step > 1e-9) steps.push(step);
  }
  return steps;
}

// 平滑模式使用独立的趋势数据：按扭矩排序，并合并非常接近的测量点。
// 原始采集数组不会被排序或修改，峰值截断仍按真实采集顺序完成。
function prepareSmoothSource(points) {
  const sorted = points
    .filter((point) => Number.isFinite(point.torque_nm))
    .map((point) => ({ ...point, torque_nm: Number(point.torque_nm) }))
    .sort((first, second) => first.torque_nm - second.torque_nm);
  if (sorted.length < 2) return sorted;

  const typicalStep = medianValue(positiveSteps(sorted)) || 0.02;
  const mergeTolerance = clampNumber(typicalStep * 0.25, 0.002, 0.01);
  const groups = [];
  sorted.forEach((point) => {
    const group = groups.at(-1);
    if (!group || point.torque_nm - group.at(-1).torque_nm > mergeTolerance) {
      groups.push([point]);
    } else {
      group.push(point);
    }
  });

  return groups.map((group) => {
    const merged = { torque_nm: medianValue(group.map((point) => point.torque_nm)) };
    SMOOTH_SERIES_KEYS.forEach((key) => {
      const values = group
        .filter((point) => point[key] !== null && point[key] !== undefined)
        .map((point) => Number(point[key]))
        .filter(Number.isFinite);
      merged[key] = medianValue(values);
    });
    return merged;
  });
}

function localLinearEstimate(samples, x, robustWeights, neighborCount) {
  const distances = samples
    .map((sample, index) => ({ index, distance: Math.abs(sample.x - x) }))
    .sort((first, second) => first.distance - second.distance);
  const edge = distances[Math.min(neighborCount - 1, distances.length - 1)]?.distance || 0;
  const bandwidth = Math.max(edge * 1.000001, 1e-9);
  let sumWeight = 0;
  let sumX = 0;
  let sumXX = 0;
  let sumY = 0;
  let sumXY = 0;

  samples.forEach((sample, index) => {
    const distanceRatio = Math.abs(sample.x - x) / bandwidth;
    if (distanceRatio >= 1) return;
    const distanceWeight = (1 - distanceRatio ** 3) ** 3;
    const weight = distanceWeight * (robustWeights[index] ?? 1);
    const centeredX = sample.x - x;
    sumWeight += weight;
    sumX += weight * centeredX;
    sumXX += weight * centeredX * centeredX;
    sumY += weight * sample.y;
    sumXY += weight * centeredX * sample.y;
  });

  if (sumWeight <= 1e-12) return null;
  const determinant = sumWeight * sumXX - sumX * sumX;
  if (Math.abs(determinant) <= 1e-12) return sumY / sumWeight;
  return (sumY * sumXX - sumXY * sumX) / determinant;
}

function createLowessTrend(source, key, options = {}) {
  const samples = source
    .filter((point) => Number.isFinite(point[key]))
    .map((point) => ({ x: point.torque_nm, y: Number(point[key]) }));
  if (samples.length < SMOOTH_MIN_SAMPLES) return null;

  const neighborFraction = options.neighborFraction ?? 0.5;
  const minimumNeighbors = options.minimumNeighbors ?? 9;
  const robustIterations = options.robustIterations ?? 2;
  const neighborCount = Math.min(
    samples.length,
    Math.max(minimumNeighbors, Math.ceil(samples.length * neighborFraction)),
  );
  let robustWeights = samples.map(() => 1);
  for (let iteration = 0; iteration < robustIterations; iteration += 1) {
    const residuals = samples.map((sample) => {
      const estimate = localLinearEstimate(samples, sample.x, robustWeights, neighborCount);
      return Number.isFinite(estimate) ? Math.abs(sample.y - estimate) : 0;
    });
    const residualScale = (medianValue(residuals) || 0) * 6;
    if (residualScale <= 1e-9) break;
    robustWeights = residuals.map((residual) => {
      if (residual >= residualScale) return 0;
      return (1 - (residual / residualScale) ** 2) ** 2;
    });
  }

  const firstX = samples[0].x;
  const lastX = samples.at(-1).x;

  return (x) => {
    if (x < firstX || x > lastX) return null;
    const estimate = localLinearEstimate(samples, x, robustWeights, neighborCount);
    if (!Number.isFinite(estimate)) return null;
    if (key === "efficiency_pct") return clampNumber(estimate, 0, 100);
    if (["speed_rpm", "current_a", "power_w"].includes(key)) return Math.max(0, estimate);
    return estimate;
  };
}

function isotonicValues(values, increasing = true) {
  const direction = increasing ? 1 : -1;
  const blocks = [];
  values.forEach((value, index) => {
    blocks.push({ start: index, end: index, count: 1, mean: value * direction });
    while (blocks.length > 1 && blocks.at(-2).mean > blocks.at(-1).mean) {
      const right = blocks.pop();
      const left = blocks.pop();
      const count = left.count + right.count;
      blocks.push({
        start: left.start,
        end: right.end,
        count,
        mean: (left.mean * left.count + right.mean * right.count) / count,
      });
    }
  });
  const result = new Array(values.length);
  blocks.forEach((block) => {
    for (let index = block.start; index <= block.end; index += 1) {
      result[index] = block.mean * direction;
    }
  });
  return result;
}

function softenMonotonicValues(values, passes = 4) {
  let softened = [...values];
  for (let pass = 0; pass < passes; pass += 1) {
    softened = softened.map((value, index, current) => {
      if (index === 0 || index === current.length - 1) return value;
      return (current[index - 1] + 2 * value + current[index + 1]) / 4;
    });
  }
  return softened;
}

// Remove visually redundant anchors before interpolation. The retained points stay
// within the requested vertical error, while the resulting PCHIP curve has fewer
// small bends and therefore reads as one clean product-characteristic trend.
function simplifyTrendSamples(samples, tolerance = 1.25) {
  if (samples.length <= 2) return [...samples];
  const keptIndexes = new Set([0, samples.length - 1]);

  const simplifyRange = (startIndex, endIndex) => {
    if (endIndex - startIndex <= 1) return;
    const start = samples[startIndex];
    const end = samples[endIndex];
    const width = end.x - start.x;
    let largestError = -1;
    let splitIndex = -1;
    for (let index = startIndex + 1; index < endIndex; index += 1) {
      const ratio = width > 0 ? (samples[index].x - start.x) / width : 0;
      const expected = start.y + (end.y - start.y) * ratio;
      const error = Math.abs(samples[index].y - expected);
      if (error > largestError) {
        largestError = error;
        splitIndex = index;
      }
    }
    if (largestError <= tolerance || splitIndex < 0) return;
    keptIndexes.add(splitIndex);
    simplifyRange(startIndex, splitIndex);
    simplifyRange(splitIndex, endIndex);
  };

  simplifyRange(0, samples.length - 1);
  return [...keptIndexes]
    .sort((left, right) => left - right)
    .map((index) => samples[index]);
}

function pchipEndpointSlope(firstStep, secondStep, firstDelta, secondDelta) {
  let slope = ((2 * firstStep + secondStep) * firstDelta - firstStep * secondDelta)
    / (firstStep + secondStep);
  if (Math.sign(slope) !== Math.sign(firstDelta)) return 0;
  if (Math.sign(firstDelta) !== Math.sign(secondDelta) && Math.abs(slope) > Math.abs(3 * firstDelta)) {
    slope = 3 * firstDelta;
  }
  return slope;
}

function createShapePreservingTrend(samples) {
  if (samples.length < 2) return null;
  const steps = samples.slice(1).map((sample, index) => sample.x - samples[index].x);
  const deltas = steps.map((step, index) => (samples[index + 1].y - samples[index].y) / step);
  const slopes = new Array(samples.length).fill(0);
  if (samples.length === 2) {
    slopes[0] = deltas[0];
    slopes[1] = deltas[0];
  } else {
    slopes[0] = pchipEndpointSlope(steps[0], steps[1], deltas[0], deltas[1]);
    slopes[slopes.length - 1] = pchipEndpointSlope(
      steps.at(-1),
      steps.at(-2),
      deltas.at(-1),
      deltas.at(-2),
    );
    for (let index = 1; index < slopes.length - 1; index += 1) {
      const before = deltas[index - 1];
      const after = deltas[index];
      if (before === 0 || after === 0 || Math.sign(before) !== Math.sign(after)) continue;
      const firstWeight = 2 * steps[index] + steps[index - 1];
      const secondWeight = steps[index] + 2 * steps[index - 1];
      slopes[index] = (firstWeight + secondWeight)
        / (firstWeight / before + secondWeight / after);
    }
  }

  return (x) => {
    if (x < samples[0].x || x > samples.at(-1).x) return null;
    let low = 0;
    let high = samples.length - 1;
    while (high - low > 1) {
      const middle = Math.floor((low + high) / 2);
      if (samples[middle].x <= x) low = middle;
      else high = middle;
    }
    const step = samples[high].x - samples[low].x;
    const ratio = step > 0 ? (x - samples[low].x) / step : 0;
    const ratio2 = ratio * ratio;
    const ratio3 = ratio2 * ratio;
    const value = (2 * ratio3 - 3 * ratio2 + 1) * samples[low].y
      + (ratio3 - 2 * ratio2 + ratio) * step * slopes[low]
      + (-2 * ratio3 + 3 * ratio2) * samples[high].y
      + (ratio3 - ratio2) * step * slopes[high];
    return clampNumber(value, 0, 100);
  };
}

function createEfficiencyTrend(source) {
  const samples = source
    .filter((point) => Number.isFinite(point.efficiency_pct))
    .map((point) => ({ x: point.torque_nm, y: Number(point.efficiency_pct) }));
  if (samples.length < SMOOTH_MIN_SAMPLES) return null;

  const peakScores = samples.map((sample, index) => medianValue(
    samples.slice(Math.max(0, index - 1), Math.min(samples.length, index + 2))
      .map((point) => point.y),
  ));
  const peakIndex = peakScores.reduce(
    (best, value, index) => value > peakScores[best] ? index : best,
    0,
  );
  const rising = softenMonotonicValues(
    isotonicValues(samples.slice(0, peakIndex + 1).map((sample) => sample.y), true),
  );
  const falling = softenMonotonicValues(
    isotonicValues(samples.slice(peakIndex).map((sample) => sample.y), false),
  );
  const peakValue = Math.max(rising.at(-1), falling[0]);
  const adjusted = [
    ...rising.slice(0, -1),
    peakValue,
    ...falling.slice(1),
  ];
  const adjustedSamples = samples.map(
    (sample, index) => ({ x: sample.x, y: adjusted[index] }),
  );
  const risingAnchors = simplifyTrendSamples(adjustedSamples.slice(0, peakIndex + 1));
  const fallingAnchors = simplifyTrendSamples(adjustedSamples.slice(peakIndex));
  return createShapePreservingTrend([
    ...risingAnchors.slice(0, -1),
    ...fallingAnchors,
  ]);
}

function buildSmoothDisplayPoints(rawPoints) {
  const source = prepareSmoothSource(rawPoints);
  if (source.length < SMOOTH_MIN_SAMPLES) return [];
  const xMinimum = source[0].torque_nm;
  const xMaximum = source.at(-1).torque_nm;
  if (!(xMaximum > xMinimum)) return [];

  const trends = Object.fromEntries(
    SMOOTH_SERIES_KEYS.map((key) => [
      key,
      key === "efficiency_pct" ? createEfficiencyTrend(source) : createLowessTrend(source, key),
    ]),
  );
  if (!Object.values(trends).some(Boolean)) return [];

  return Array.from({ length: SMOOTH_POINT_COUNT }, (_, index) => {
    const ratio = index / (SMOOTH_POINT_COUNT - 1);
    const torque = xMinimum + (xMaximum - xMinimum) * ratio;
    const point = {
      torque_nm: torque,
      is_virtual: true,
      fit_index: index,
    };
    SMOOTH_SERIES_KEYS.forEach((key) => {
      const value = trends[key]?.(torque);
      point[key] = Number.isFinite(value) ? Number(value.toFixed(6)) : null;
    });
    return point;
  });
}

  function error(container, message) {
    container.replaceChildren();
    const notice = document.createElement("p");
    notice.className = "servo-chart-error";
    notice.textContent = message;
    container.append(notice);
  }

  const PLOT = { left: 130, right: 760, top: 32, bottom: 432 };
  const CHART = { width: 920, height: 492 };
  let chartId = 0;

  function html(name, className, text = "") {
    const node = document.createElement(name);
    node.className = className;
    node.textContent = text;
    return node;
  }

  // Keep peak detection in acquisition order, before sorting for smoothing.
  function measurementsThroughPeak(measurements) {
    const valid = measurements.map((point, index) => {
      const normalized = {
        sample_index: index,
        torque_nm: numeric(point.torque_nm),
        ...Object.fromEntries(METRICS.map((metric) => [metric.key, numeric(point[metric.key])])),
      };
      const power = normalized.power_w ?? numeric(point.raw?.power_w);
      normalized.power_w = power !== null ? Math.abs(power)
        : normalized.torque_nm !== null && normalized.speed_rpm !== null
          ? Number((normalized.torque_nm * normalized.speed_rpm * 2 * Math.PI / 60).toFixed(4)) : null;
      return normalized;
    }).filter((point) => point.torque_nm !== null);
    let peak = -Infinity;
    let peakIndex = -1;
    for (let index = 0; index < valid.length; index += 1) {
      if (valid[index].torque_nm > peak) {
        peak = valid[index].torque_nm;
        peakIndex = index;
      } else if (peak - valid[index].torque_nm > 0.15) break;
    }
    return { points: valid.slice(0, peakIndex + 1), hidden: valid.length - peakIndex - 1 };
  }

  // Same fixed-range tick distribution and decimal precision as the fixture.
  function axisTicks(axis) {
    const count = Math.max(1, Math.round((axis.max - axis.min) / axis.step));
    return Array.from({ length: count + 1 }, (_, index) =>
      Number((axis.min + (axis.max - axis.min) * index / count).toFixed(6)));
  }

  function interpolateSmoothPoint(torque, points) {
    if (!points.length || torque < points[0].torque_nm || torque > points.at(-1).torque_nm) return null;
    let low = 0;
    let high = points.length - 1;
    while (high - low > 1) {
      const middle = Math.floor((low + high) / 2);
      if (points[middle].torque_nm <= torque) low = middle;
      else high = middle;
    }
    const left = points[low];
    const right = points[high];
    const width = right.torque_nm - left.torque_nm;
    const ratio = width > 0 ? (torque - left.torque_nm) / width : 0;
    return {
      torque_nm: torque,
      ...Object.fromEntries(METRICS.map(({ key }) => [key,
        Number.isFinite(left[key]) && Number.isFinite(right[key])
          ? left[key] + (right[key] - left[key]) * ratio : null])),
    };
  }

  function render(container, result) {
    const prepared = measurementsThroughPeak(result.measurements || []);
    const rawPoints = prepared.points;
    if (rawPoints.length < 2) return error(container, copy.noPoints);
    const axes = result.range_profile?.axes;
    const allMetrics = [
      { key: "torque_nm", label: copy.torque, unit: "N·m", color: "#2a322b" },
      METRICS[1], METRICS[2], METRICS[0], METRICS[3],
    ];
    if (!axes || allMetrics.some(({ key }) => {
      const axis = axes[key];
      return !axis || ![axis.min, axis.max, axis.step].every(Number.isFinite)
        || axis.max <= axis.min || axis.step <= 0 || (axis.max - axis.min) / axis.step > 200
        || (axis.decimals !== undefined && (!Number.isInteger(axis.decimals) || axis.decimals < 0 || axis.decimals > 6));
    })) return error(container, copy.invalidAxes);
    const smoothPoints = buildSmoothDisplayPoints(rawPoints);
    let smooth = smoothPoints.length > 1;
    let points = smooth ? smoothPoints : rawPoints;
    let selectedIndex = 0;
    const mapX = (value) => PLOT.left + (value - axes.torque_nm.min) / (axes.torque_nm.max - axes.torque_nm.min) * (PLOT.right - PLOT.left);
    const mapY = (value, axis) => PLOT.bottom - (value - axis.min) / (axis.max - axis.min) * (PLOT.bottom - PLOT.top);
    const title = container.dataset.title || `${result.model || ""} T-N`;
    const header = html("div", "servo-chart-header");
    const heading = html("div", "servo-chart-heading");
    heading.append(html("strong", "servo-chart-title", title));
    const subtitle = html("p", "servo-chart-subtitle");
    heading.append(subtitle);
    const toggle = html("button", "servo-chart-toggle");
    toggle.type = "button";
    toggle.disabled = smoothPoints.length < 2;
    header.append(heading, toggle);
    const cards = html("div", "servo-chart-metrics");
    const cardValues = new Map();
    allMetrics.forEach((metric) => {
      const card = html("div", "servo-chart-card");
      card.style.setProperty("--servo-chart-color", metric.color);
      const label = html("span", "servo-chart-card-label", metric.label);
      const value = html("strong", "", "—");
      const reading = html("div", "servo-chart-card-reading");
      reading.append(value, html("span", "", metric.unit));
      card.append(label, reading);
      cardValues.set(metric.key, value);
      cards.append(card);
    });
    const legend = html("div", "servo-chart-legend");
    legend.setAttribute("aria-label", copy.legend);
    METRICS.forEach((metric) => {
      const item = html("span", "", `${metric.label} (${metric.unit})`);
      item.style.setProperty("--servo-chart-color", metric.color);
      legend.append(item);
    });
    const viewport = html("div", "servo-chart-viewport");
    const svg = element("svg", { viewBox: `0 0 ${CHART.width} ${CHART.height}`, role: "img", "aria-label": title, tabindex: 0 });
    viewport.append(svg);
    const tooltip = html("div", "servo-chart-tooltip");
    tooltip.hidden = true;
    const footer = html("div", "servo-chart-footer");
    const readout = html("span", "servo-chart-readout");
    footer.append(readout, html("span", "", copy.hint));
    const warning = html("p", "servo-chart-warning");
    const outside = rawPoints.filter((point) => allMetrics.some(({ key }) => Number.isFinite(point[key]) && (point[key] < axes[key].min || point[key] > axes[key].max))).length;
    const warnings = [];
    if (outside) warnings.push(`${outside} ${copy.outside}`);
    if (prepared.hidden) warnings.push(`${prepared.hidden} ${copy.hidden}`);
    METRICS.forEach(({ key, label }) => {
      if (rawPoints.every((point) => !Number.isFinite(point[key]))) warnings.push(`${label}: ${copy.unavailable}`);
    });
    warning.textContent = warnings.join(" · ");
    warning.hidden = !warnings.length;
    container.replaceChildren(header, cards, legend, viewport, tooltip, footer, warning);
    const clipId = `servo-plot-${++chartId}`;
    let hover;
    let hoverLine;
    let markers;

    function clearSelection() {
      tooltip.hidden = true;
      hover?.setAttribute("visibility", "hidden");
      cardValues.forEach((value) => { value.textContent = "—"; });
      readout.textContent = `${rawPoints.length} ${copy.points} · ${smooth ? copy.smooth : copy.raw}`;
    }

    function draw() {
      points = smooth ? smoothPoints : rawPoints;
      selectedIndex = 0;
      toggle.textContent = smooth ? copy.toggleRaw : copy.toggleSmooth;
      toggle.setAttribute("aria-pressed", String(smooth));
      subtitle.textContent = [result.serial_number, copy.fixed, smooth ? copy.smooth : copy.raw].filter(Boolean).join(" · ");
      svg.replaceChildren();
      const defs = element("defs");
      const clip = element("clipPath", { id: clipId });
      const plotRect = { x: PLOT.left, y: PLOT.top, width: PLOT.right - PLOT.left, height: PLOT.bottom - PLOT.top };
      clip.append(element("rect", plotRect));
      defs.append(clip);
      svg.append(defs, element("rect", { ...plotRect, fill: "#fff", stroke: "#aeb6ad" }));
      const line = (x1, y1, x2, y2, stroke, extra = {}) => svg.append(element("line", { x1, y1, x2, y2, stroke, ...extra }));
      const xTicks = axisTicks(axes.torque_nm);
      const speedTicks = axisTicks(axes.speed_rpm);
      const grid = (ticks, map, vertical) => ticks.forEach((value, index) => {
        const position = map(value);
        if (vertical) line(position, PLOT.top, position, PLOT.bottom, "#d8ddd7");
        else line(PLOT.left, position, PLOT.right, position, "#d8ddd7");
        if (index === ticks.length - 1) return;
        for (let minor = 1; minor < 5; minor += 1) {
          const p = map(value + (ticks[index + 1] - value) * minor / 5);
          if (vertical) line(p, PLOT.top, p, PLOT.bottom, "#eef1ed");
          else line(PLOT.left, p, PLOT.right, p, "#eef1ed");
        }
      });
      grid(xTicks, mapX, true);
      grid(speedTicks, (value) => mapY(value, axes.speed_rpm), false);
      xTicks.forEach((value) => {
        const x = mapX(value);
        line(x, PLOT.bottom, x, PLOT.bottom + 6, "#2a322b");
        svg.append(element("text", { x, y: PLOT.bottom + 22, "text-anchor": "middle", class: "servo-chart-tick", fill: "#2a322b" }, format(value, axes.torque_nm)));
      });
      svg.append(element("text", { x: (PLOT.left + PLOT.right) / 2, y: PLOT.bottom + 51, "text-anchor": "middle", class: "servo-chart-axis", fill: "#2a322b" }, `${copy.torque} (N·m)`));
      METRICS.forEach((metric) => {
        const axis = axes[metric.key];
        line(metric.axisX, PLOT.top, metric.axisX, PLOT.bottom, metric.color, { "stroke-width": 1.6 });
        axisTicks(axis).forEach((value) => {
          const y = mapY(value, axis);
          line(metric.axisX, y, metric.axisX + metric.side * 6, y, metric.color);
          svg.append(element("text", { x: metric.axisX + metric.side * 10, y: y + 4, "text-anchor": metric.side < 0 ? "end" : "start", fill: metric.color, class: "servo-chart-tick" }, format(value, axis)));
        });
        const center = (PLOT.top + PLOT.bottom) / 2;
        svg.append(element("text", { x: metric.labelX, y: center, fill: metric.color, "text-anchor": "middle", transform: `rotate(${metric.labelX > PLOT.right ? 90 : -90} ${metric.labelX} ${center})`, class: "servo-chart-axis" }, `${metric.label} (${metric.unit})`));
      });
      const series = element("g", { "clip-path": `url(#${clipId})` });
      METRICS.forEach((metric) => {
        let connected = false;
        const d = points.map((point) => {
          if (!Number.isFinite(point[metric.key])) { connected = false; return ""; }
          const command = connected ? "L" : "M";
          connected = true;
          return `${command}${mapX(point.torque_nm).toFixed(2)},${mapY(point[metric.key], axes[metric.key]).toFixed(2)}`;
        }).join(" ");
        series.append(element("path", { d, "data-series": metric.key, fill: "none", stroke: metric.color, "stroke-width": 2.6, "stroke-linejoin": "round", "stroke-linecap": "round", "vector-effect": "non-scaling-stroke" }));
        if (!smooth) points.forEach((point) => {
          if (Number.isFinite(point[metric.key])) series.append(element("circle", { cx: mapX(point.torque_nm), cy: mapY(point[metric.key], axes[metric.key]), r: 2.4, fill: "#fff", stroke: metric.color, "stroke-width": 1.2 }));
        });
      });
      svg.append(series);
      hover = element("g", { visibility: "hidden", "pointer-events": "none", "clip-path": `url(#${clipId})` });
      hoverLine = element("line", { y1: PLOT.top, y2: PLOT.bottom, stroke: "#5d675e", "stroke-dasharray": "4 4" });
      hover.append(hoverLine);
      markers = new Map(METRICS.map((metric) => {
        const marker = element("circle", { r: 4, fill: "#fff", stroke: metric.color, "stroke-width": 2 });
        hover.append(marker);
        return [metric.key, marker];
      }));
      svg.append(hover);
      clearSelection();
    }

    function select(point, clientX, clientY, showTooltip = true) {
      if (!point) return clearSelection();
      const x = mapX(point.torque_nm);
      hoverLine.setAttribute("x1", x);
      hoverLine.setAttribute("x2", x);
      hover.setAttribute("visibility", "visible");
      METRICS.forEach(({ key }) => {
        const marker = markers.get(key);
        marker.setAttribute("visibility", Number.isFinite(point[key]) ? "visible" : "hidden");
        if (Number.isFinite(point[key])) {
          marker.setAttribute("cx", x);
          marker.setAttribute("cy", mapY(point[key], axes[key]));
        }
      });
      allMetrics.forEach(({ key }) => { cardValues.get(key).textContent = format(point[key], axes[key]); });
      const mode = smooth ? copy.estimate : `${copy.measured} #${point.sample_index + 1}`;
      readout.textContent = `${mode} · ${copy.torque} ${format(point.torque_nm, axes.torque_nm)} N·m`;
      tooltip.replaceChildren(html("strong", "", mode));
      allMetrics.forEach((metric) => {
        const row = html("div", "servo-chart-tooltip-row");
        const label = html("span", "", metric.label);
        label.style.setProperty("--servo-chart-color", metric.color);
        row.append(label, html("b", "", `${format(point[metric.key], axes[metric.key])} ${metric.unit}`));
        tooltip.append(row);
      });
      tooltip.hidden = !showTooltip;
      if (!showTooltip) return;
      const bounds = container.getBoundingClientRect();
      const px = clientX - bounds.left;
      const py = clientY - bounds.top;
      const left = px + tooltip.offsetWidth + 20 > container.clientWidth ? px - tooltip.offsetWidth - 14 : px + 14;
      tooltip.style.left = `${clampNumber(left, 8, Math.max(8, container.clientWidth - tooltip.offsetWidth - 8))}px`;
      tooltip.style.top = `${clampNumber(py - tooltip.offsetHeight / 2, 8, Math.max(8, container.clientHeight - tooltip.offsetHeight - 8))}px`;
    }

    function update(event) {
      // Invert the actual SVG transform, including letterboxing and horizontal scrolling.
      const matrix = svg.getScreenCTM();
      if (!matrix) return;
      const cursor = new DOMPoint(event.clientX, event.clientY).matrixTransform(matrix.inverse());
      if (cursor.x < PLOT.left || cursor.x > PLOT.right || cursor.y < PLOT.top || cursor.y > PLOT.bottom) return clearSelection();
      const torque = axes.torque_nm.min + (cursor.x - PLOT.left) / (PLOT.right - PLOT.left) * (axes.torque_nm.max - axes.torque_nm.min);
      const point = smooth ? interpolateSmoothPoint(torque, points)
        : points.reduce((best, value) => Math.abs(value.torque_nm - torque) < Math.abs(best.torque_nm - torque) ? value : best);
      select(point, event.clientX, event.clientY);
    }
    svg.addEventListener("pointermove", update);
    svg.addEventListener("pointerdown", update);
    svg.addEventListener("pointerleave", clearSelection);
    svg.addEventListener("pointercancel", clearSelection);
    svg.addEventListener("blur", clearSelection);
    viewport.addEventListener("scroll", clearSelection);
    svg.addEventListener("keydown", (event) => {
      if (event.key === "Escape") return clearSelection();
      if (!["ArrowLeft", "ArrowRight", "Home", "End"].includes(event.key)) return;
      event.preventDefault();
      selectedIndex = event.key === "Home" ? 0 : event.key === "End" ? points.length - 1
        : clampNumber(selectedIndex + (event.key === "ArrowRight" ? 1 : -1), 0, points.length - 1);
      select(points[selectedIndex], 0, 0, false);
    });
    toggle.addEventListener("click", () => { smooth = !smooth; draw(); });
    draw();
  }
  async function initialise(container) {
    const source = container.dataset.source;
    if (!source) return error(container, copy.noSource);
    try {
      const response = await fetch(new URL(source, document.baseURI));
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      render(container, await response.json());
    } catch (exception) {
      error(container, `${copy.loadError} (${exception.message}).`);
    }
  }

  document.addEventListener("DOMContentLoaded", () => document.querySelectorAll(".servo-characteristic-chart").forEach(initialise));
})();
