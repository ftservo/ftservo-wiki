---
hide:
  - toc
---

# 产品选型

不要只按“公斤扭矩”选舵机。一个可落地的选型至少要同时满足接口、电压、持续负载、速度、尺寸、行程、反馈和环境条件。

还没决定系列？先看[系列与接口](series.md)了解各系列的定位、协议与接口差异。

## 舵机选型器

<div id="ft-servo-selector" class="ft-selector" data-locale="zh">
  <div class="ft-selector-head">
    <div><strong>找到适合你的飞特舵机</strong><span>筛选条件即时生效，快速比较候选型号。</span></div>
    <div class="ft-selector-buttons"><button type="button" class="ft-selector-reset" data-action="advanced" aria-expanded="false" aria-controls="ft-professional-panel">专业选型</button><button type="button" class="ft-selector-reset" data-action="reset">重置条件</button></div>
  </div>
  <div class="ft-selector-layout">
    <aside id="ft-professional-panel" class="ft-selector-sidebar" aria-label="专业筛选条件" hidden>
      <div class="ft-sidebar-heading">筛选条件<small>同组可多选</small></div>
      <label class="ft-selector-field"><span>搜索型号</span><input type="search" data-filter="query" aria-label="搜索型号" autocomplete="off" placeholder="ST-3215 / HL-3950"></label>
      <fieldset class="ft-filter-group"><legend>控制接口</legend><div class="ft-filter-options" data-group="interface"></div></fieldset>
      <fieldset class="ft-filter-group"><legend>产品系列</legend><div class="ft-filter-options" data-group="family"></div></fieldset>
      <fieldset class="ft-filter-group"><legend>输入电压 · V</legend><div class="ft-filter-options" data-group="voltage"></div></fieldset>
      <fieldset class="ft-filter-group ft-range-group"><legend>堵转扭矩 <small>kg·cm</small></legend><div class="ft-range-pair"><label class="ft-selector-field"><span>下限</span><input type="number" data-filter="torque" aria-label="下限" min="0" step="0.1" placeholder="不限"></label><span class="ft-range-dash">—</span><label class="ft-selector-field"><span>上限</span><input type="number" data-filter="torqueMax" aria-label="上限" min="0" step="0.1" placeholder="不限"></label></div><div class="ft-range-sliders"><input class="ft-filter-slider" type="range" min="0" max="150" step="0.1" value="0" data-default="0" data-range-for="torque" aria-label="堵转扭矩下限"><input class="ft-filter-slider" type="range" min="0" max="150" step="0.1" value="150" data-default="150" data-range-for="torqueMax" aria-label="堵转扭矩上限"></div></fieldset>
      <fieldset class="ft-filter-group ft-range-group"><legend>空载速度 <small>rpm</small></legend><div class="ft-range-pair"><label class="ft-selector-field"><span>下限</span><input type="number" data-filter="speed" aria-label="下限" min="0" step="0.1" placeholder="不限"></label><span class="ft-range-dash">—</span><label class="ft-selector-field"><span>上限</span><input type="number" data-filter="speedMax" aria-label="上限" min="0" step="0.1" placeholder="不限"></label></div><div class="ft-range-sliders"><input class="ft-filter-slider" type="range" min="0" max="180" step="0.1" value="0" data-default="0" data-range-for="speed" aria-label="空载速度下限"><input class="ft-filter-slider" type="range" min="0" max="180" step="0.1" value="180" data-default="180" data-range-for="speedMax" aria-label="空载速度上限"></div></fieldset>
      <fieldset class="ft-filter-group ft-limit-group"><legend>位置控制范围 ≥ · °</legend><label class="ft-selector-field"><span>下限</span><input type="number" data-filter="positionRange" aria-label="下限" min="0" step="0.1" placeholder="不限"></label><input class="ft-filter-slider" type="range" min="0" max="360" step="0.1" value="0" data-default="0" data-range-for="positionRange" aria-label="位置控制范围 ≥ · °"></fieldset><fieldset class="ft-filter-group ft-limit-group"><legend>最长边 ≤ · mm</legend><label class="ft-selector-field"><span>上限</span><input type="number" data-filter="maxEdge" aria-label="上限" min="0" step="0.1" placeholder="不限"></label><input class="ft-filter-slider" type="range" min="0" max="150" step="0.1" value="150" data-default="150" data-range-for="maxEdge" aria-label="最长边 ≤ · mm"></fieldset><fieldset class="ft-filter-group ft-limit-group"><legend>重量 ≤ · g</legend><label class="ft-selector-field"><span>上限</span><input type="number" data-filter="weight" aria-label="上限" min="0" step="0.1" placeholder="不限"></label><input class="ft-filter-slider" type="range" min="0" max="500" step="0.1" value="500" data-default="500" data-range-for="weight" aria-label="重量 ≤ · g"></fieldset>
      <fieldset class="ft-filter-group"><legend>连续旋转</legend><div class="ft-filter-options" data-group="continuous"></div></fieldset>
      <fieldset class="ft-filter-group"><legend>电机类型</legend><div class="ft-filter-options" data-group="motor"></div></fieldset>
      <fieldset class="ft-filter-group"><legend>齿轮材质</legend><div class="ft-filter-options" data-group="gear"></div></fieldset>
      <fieldset class="ft-filter-group"><legend>外壳材质</legend><div class="ft-filter-options" data-group="case"></div></fieldset>
      <fieldset class="ft-filter-group"><legend>输出轴型</legend><div class="ft-filter-options" data-group="shaft"></div></fieldset>
      <p class="ft-filter-note">空白表示不限；缺失参数不匹配。电压按目录比较值筛选。位置控制范围不等于连续旋转能力；最长边取三边尺寸最大值。滑块扭矩 0–150 kg·cm、速度 0–180 rpm，输入框可填写更大值。</p>
    </aside>
    <section class="ft-selector-main" aria-label="选型结果">
      <div class="ft-selector-controls ft-selector-basic">
        <label class="ft-selector-field"><span>搜索型号</span><input type="search" data-filter="query" aria-label="搜索型号" autocomplete="off" placeholder="ST-3215 / HL-3950"></label>
        <label class="ft-selector-field"><span>控制接口</span><select data-category="interface" aria-label="控制接口"><option value="">全部</option></select></label><label class="ft-selector-field"><span>产品系列</span><select data-category="family" aria-label="产品系列"><option value="">全部</option></select></label><label class="ft-selector-field"><span>输入电压</span><select data-category="voltage" aria-label="输入电压"><option value="">全部</option></select></label>
        <label class="ft-selector-field"><span>最低堵转扭矩 · kg·cm</span><input type="number" data-filter="torque" aria-label="最低堵转扭矩 · kg·cm" min="0" step="0.1" placeholder="不限"></label>
        <label class="ft-selector-field"><span>最低空载速度 · rpm</span><input type="number" data-filter="speed" aria-label="最低空载速度 · rpm" min="0" step="0.1" placeholder="不限"></label>
      </div>
      <div class="ft-selector-toolbar"><div class="ft-selector-status" role="status" aria-live="polite">正在加载型号…</div><label class="ft-selector-sort"><span>排序</span><select data-filter="sort" title="HLS、STS 优先；各组内按所选指标排序"><option value="recommended">主推优先</option><option value="model">型号</option><option value="torque-desc">扭矩 ↓</option><option value="torque-asc">扭矩 ↑</option><option value="speed-desc">速度 ↓</option><option value="weight-asc">重量 ↑</option></select></label></div>
      <div class="ft-results-scroll" tabindex="0" aria-label="产品列表"><div class="ft-selector-results"></div><button type="button" class="ft-selector-more" data-action="more" hidden>显示更多</button></div>
    </section>
  </div>
  <noscript>此选型器需要 JavaScript；下方系列目录仍可查看。</noscript>
</div>

!!! info "选型提示"
    筛选结果用于快速比较产品。请进入型号页查看完整规格，并结合负载、工作周期、温升和机构条件保留设计余量。

## 六步筛选

1. **控制方式**：只需传统脉宽控制选 PWM；需要多机串联、读回位置/温度/负载或改参数，选总线舵机。
2. **物理接口**：短距离机器人内部总线通常选择 TTL；距离较长或干扰较强时优先评估 RS485；现有控制器接口必须匹配。
3. **供电**：确定额定工作电压，并按堵转电流和同时动作数量留足电源余量。
4. **机械性能**：用实际力臂计算所需扭矩，考虑冲击、重力、摩擦与加速度，保留安全系数。
5. **运动性能**：确认速度、角度范围、连续旋转需求、位置分辨率和是否需要磁编码器。
6. **结构与环境**：确认外形、轴型、重量、安装孔位、防护、齿轮材质和工作温度。

## 扭矩估算

静态负载的基础估算：

```text
所需扭矩 (kg·cm) ≈ 负载 (kg) × 力臂 (cm) × 安全系数
```

例如 1 kg 负载作用在 10 cm 力臂末端，理论静态扭矩为 10 kg·cm。真实机构还要考虑动态加速、姿态、摩擦和冲击；不要让舵机长期接近堵转扭矩运行。

## 选型记录表

| 条件 | 项目要求 | 候选型号 |
| --- | --- | --- |
| 控制接口 | PWM / TTL / RS485 / 其他 | |
| 工作电压 | V | |
| 所需持续/峰值扭矩 | kg·cm 或 N·m | |
| 目标速度 | s/60° 或 RPM | |
| 角度与模式 | 有限角 / 多圈 / 连续旋转 | |
| 反馈 | 位置 / 速度 / 负载 / 电压 / 温度 | |
| 最大尺寸和重量 | mm / g | |
| 控制平台 | PC / Arduino / ESP32 / Linux / STM32 | |

填写后可在[飞特产品中心](https://www.feetechrc.com/products.html)了解应用信息，再到[产品规格目录](datasheets/index.md)比较候选型号。

## 常见路线

| 需求 | 优先查看 | 说明 |
| --- | --- | --- |
| 低成本传统遥控 | PWM 系列 | 接线简单，不适合总线读回和多机寻址 |
| 教育机器人、桌面机械臂 | SCS / STS TTL | 可串联和读回；具体分辨率与电压看型号 |
| 高分辨率、磁编码反馈 | STS TTL | 多个型号提供 360° 磁编码能力 |
| 大型机构或强干扰环境 | SMS RS485 | 差分总线；需要 RS485 调试/控制接口 |
| 特定高性能 TTL 需求 | HLS TTL | 使用 HLS 对应 SDK 类与内存表 |

!!! note "系列名称不是完整规格"
    官方产品仍在更新，本 Wiki 不复制一张很快过期的全量价格/参数表。最终选型以官网当前产品页、销售确认和随产品发布的数据表为准。
