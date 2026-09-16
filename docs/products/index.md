# 产品选型

不要只按“公斤扭矩”选舵机。一个可落地的选型至少要同时满足接口、电压、持续负载、速度、尺寸、行程、反馈和环境条件。

## 舵机选型器

<div id="ft-servo-selector" class="ft-selector" data-locale="zh">
  <div class="ft-selector-head">
    <div><strong>快速找到合适的飞特舵机</strong><span>当前提供 142 款产品，可按接口、电压和扭矩快速筛选。</span></div>
    <button type="button" class="ft-selector-reset" data-action="reset">重置条件</button>
  </div>
  <div class="ft-selector-controls">
    <label class="ft-selector-field ft-selector-search"><span>搜索型号</span><input type="search" data-filter="query" placeholder="例如 ST-3215 或 SMS" autocomplete="off"></label>
    <label class="ft-selector-field"><span>控制接口</span><select data-filter="interface"><option value="">全部接口</option></select></label>
    <label class="ft-selector-field"><span>产品系列</span><select data-filter="family"><option value="">全部系列</option></select></label>
    <label class="ft-selector-field"><span>输入电压</span><select data-filter="voltage"><option value="">全部电压</option></select></label>
    <label class="ft-selector-field"><span>最低堵转扭矩 kg·cm</span><input type="number" data-filter="torque" min="0" step="0.1" placeholder="不限"></label>
    <label class="ft-selector-field"><span>排序</span><select data-filter="sort"><option value="model">型号名称</option><option value="torque-desc">扭矩从高到低</option><option value="torque-asc">扭矩从低到高</option><option value="voltage">电压从低到高</option></select></label>
  </div>
  <div class="ft-selector-status" role="status" aria-live="polite">正在载入型号资料…</div>
  <div class="ft-selector-results"></div>
  <button type="button" class="ft-selector-more" data-action="more" hidden>显示更多</button>
  <noscript>此选型器需要浏览器启用 JavaScript。你仍可使用下方的产品规格目录。</noscript>
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
