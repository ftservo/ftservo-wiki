# 系列与接口

!!! tip "第一次来？先别背系列名"
    先想清楚**你要做什么**，再看下面的「快速定向」。确定系列后，去[产品规格目录](datasheets/index.md)核对具体型号，或回到[产品选型](index.md)用选型器筛选。

## 快速定向

| 你的场景 | 从这里开始 | 为什么 |
| --- | --- | --- |
| 第一次玩总线舵机，或跟着开源项目、教程做 | **STS** | 型号最多、资料与社区案例最丰富，磁编码高分辨率，新人最不容易踩坑 |
| 预算敏感的小型项目：夹爪、云台、遥控改造 | **SCS** | 入门级位置总线舵机，成本低、功能够用 |
| 舵机数量多、走线长、环境干扰强（大型机械臂、人形机器人） | **SMS** | RS485 差分通信，抗干扰强，适合长线缆和多机串联 |
| 做 Microduck、Open Duck 这类轻量双足机器人 | **HD** | 紧凑空心杯 + 金属齿轮 + 双轴结构，官网口径为「恒力双轴 TTL 总线舵机」，为轻量双足而生 |
| 要做力控、限力或柔顺夹持 | **HLS** | 恒流（恒力）模式与扭矩软件限幅是它的核心；位置/速度/电流等状态反馈 ST、SM 多款也有，但恒力与柔顺拖动以 HLS 为主，夹爪、灵巧手、人机交互机构常用 |
| 已有 CAN 总线系统，要长线束组网和较高防护 | **FU** | CAN（UAVCAN）总线，无刷大扭矩，钛齿金属壳，防护等级高 |
| 只想接遥控接收机，不写代码 | **PWM 舵机** | 传统脉宽控制，没有总线 ID 寻址，见下方 [PWM 舵机](#pwm) |

## 拿不定主意？回答问题定向

从上往下逐条问自己，第一个「是」就是你的答案：

| # | 问自己 | 答「是」 | 答「否」 |
| --- | --- | --- | --- |
| 1 | 需要读回位置/温度/负载，或要把多个舵机串起来控制吗？ | 继续第 2 问 | **PWM 舵机** |
| 2 | 舵机多、走线长、环境干扰强吗？ | **SMS**（RS485） | 继续第 3 问 |
| 3 | 要读回电流做力控、限力或柔顺夹持吗？ | **HLS**（恒力） | 继续第 4 问 |
| 4 | 做 Microduck / Open Duck 这类轻量双足，需要空心杯 + 双轴吗？ | **HD** | 继续第 5 问 |
| 5 | 已有 CAN 总线，要长线束组网或较高防护吗？ | **FU**（CAN） | 继续第 6 问 |
| 6 | 预算优先、只需要基础定位能力吗？ | **SCS** | **STS（主流推荐）** |

## 型号开头就是系列

FEETECH 型号写作「产品系列-型号编码-序列编码」，**产品系列直接对应所属系列**，看到一个型号就能判断它的接口和 SDK：

| 型号开头 | 所属系列 | 控制接口 | 记忆点 |
| --- | --- | --- | --- |
| `SC-` | SCS | TTL 半双工 | 入门经济款 |
| `ST-` | STS | TTL 半双工 | 主力全能款 |
| `SM-` | SMS | RS485 | RS485、远距离、强干扰 |
| `HL-` | HLS | TTL 半双工 | **HL** = **恒力** |
| `HD-` | HD | TTL 半双工 | 轻量双轴关节 |
| `FU-` | FU | CAN / UAVCAN | CAN 组网 |
| `FT-` `FS-` `FB-` `FR-` `FI-` | PWM 系列 | PWM 信号 | 无总线，不需要 ID |

!!! note "编号不是性能"
    型号里的数字只是编号，不代表扭矩或速度。同一系列下不同型号的电压、扭矩、速度、分辨率差异可能很大——选型时请以[产品规格目录](datasheets/index.md)和随产品发布的数据表为准。


## 六个系列逐个看

### “STS” 主流全能款

- **一句话定位**：FEETECH 总线舵机的主力系列，多为磁编码、高分辨率或连续旋转产品。
- **代表型号**：ST-3215-C001、ST-3025-C001 等（以[产品规格目录](datasheets/index.md)为准）。
- **适合**：教育机器人、桌面机械臂、云台，以及绝大多数开源机器人项目；第一次入手总线舵机的新人。
- **不适合**：超长线缆或强干扰现场（改看 SMS）；对成本极度敏感、又不需要高分辨率的场合（改看 SCS）。
- **上手提示**：SDK 使用 `STS` 应用层；写代码前先核对当前型号对应的 [STS 内存表](../reference/parameter/memory-sts.md)，再动寄存器。

### “SCS” 入门经济款

- **一句话定位**：分辨率较低的位置总线舵机，性价比入门之选。
- **代表型号**：SC-0090-C001、SC-1500-C022 等。
- **适合**：预算敏感的小型项目、简单夹爪、云台与联动结构；只需要「能定位、能串联」的基础功能。
- **不适合**：需要高分辨率定位、或需要精确控制连续旋转速度的项目（升级 STS）。
- **上手提示**：SDK 使用 `SCSCL` 应用层，与 `STS` 的寄存器布局**不同**，不要混用；寄存器地址见 [SCSCL 内存表](../reference/parameter/memory-scscl.md)。

### “SMS” 工程可靠款

- **一句话定位**：RS485 差分总线舵机，为更长线缆和更复杂的电气环境而设计。
- **代表型号**：SM-45BL-C001、SM-120B-C001 等。
- **适合**：大型机械臂、人形机器人等舵机多、走线长的系统；工业或实验环境干扰较强的现场。
- **不适合**：短距离、舵机数量少的小玩具级项目（TTL 更省事）；手头没有 RS485 调试板的用户需要先配一块。
- **上手提示**：需要 RS485 收发器/调试板，A/B 接线不可接反，见[调试板与适配器](../tools/adapters.md)；SMS（RS485）的寄存器表见 [SMS 内存表](../reference/parameter/memory-sms.md)。
- **别混用的另一套**：SMSMB 用的是 MODBUS-RTU 标准协议，寻址方式与 SMS 完全不同，寄存器表见 [SMSMB 内存表](../reference/parameter/memory-smsmb.md)。按官网现售型号，`SM-` 前缀下的 Modbus 款有 SM-120B-C003、SM-24BL-C015、SM-2924-C001、SM-2924-C012，其余的 SM- 型号走串行（Half-duplex）协议——看到型号先核对它属于哪一套。

### “HLS” 高性能恒力款

- **一句话定位**：使用 HLS 系列专用的 `HLSCL` 应用层与内存表，主打力控与柔顺交互，支持多圈（±7 圈）定位。
- **代表型号**：HL-2915-C001、HL-3606-C001 等。
- **适合**：夹爪、灵巧手、人机交互机构；需要读取电流做力控、限力或柔顺拖动的项目。
- **不适合**：想直接沿用 STS/SCS 教程与代码就跑起来的新手（应用层与内存表都不通用）。
- **上手提示**：SDK 使用 `HLSCL`；寄存器表见 [HLS 内存表](../reference/parameter/memory-hls.md)。

### “HD” 轻量双轴关节款

- **一句话定位**：官网口径为「恒力双轴 TTL 总线舵机」——紧凑型空心杯 + 金属齿轮 + 双轴结构，支持角度伺服/恒速/恒流（恒力）与多圈，面向 Microduck、Open Duck 类轻量双足机器人。
- **代表型号**：HD-1910-C001。
- **适合**：对重量和体积敏感的轻量双足、小型关节，且需要金属齿轮的耐用性；官网给出的应用场景还包括工业设备与机器人等大扭力传动。
- **不适合**：常规机械臂、云台等通用场景（STS 覆盖面更广、资料更多）。
- **上手提示**：SDK 与内存表**以型号配套资料为准**，入手前先确认固件与内存表版本；寄存器布局可先参考 [HLS 内存表](../reference/parameter/memory-hls.md)。

### “FU” CAN 总线组网款

- **一句话定位**：CAN（UAVCAN）总线舵机，为多节点组网、较长线束和高防护场景设计。
- **代表型号**：FU-8830-C001。
- **适合**：已有 CAN 总线架构、需要集中布线与高实时性的多关节机器人；对防护等级有要求的户外或工业场景。
- **不适合**：只想要一根 TTL 线接几颗舵机的入门项目（需要 CAN 收发器，生态与教程相对少）。
- **上手提示**：需要 CAN 收发器或支持 CAN 的调试板，普通 TTL 调试板和 PWM 测试器不能替代；节点地址、单位与模式以该型号 CAN/UAVCAN 资料为准，寄存器表见 [UAVCAN 内存表](../reference/parameter/memory-fu.md)。


## 接口与性能

<style>
  .md-typeset .ft-series-compare table { display: table; width: 100%; table-layout: fixed; }
  .md-typeset .ft-series-compare table th { min-width: 0; padding: .6em .5em; }
  .md-typeset .ft-series-compare table td { min-width: 0; padding: .6em .5em; }
  .md-typeset .ft-series-compare table td, .md-typeset .ft-series-compare table th { overflow-wrap: anywhere; }
  .md-typeset .ft-series-compare table th:nth-child(1), .md-typeset .ft-series-compare table td:nth-child(1) { width: 6%; }
  .md-typeset .ft-series-compare table th:nth-child(2), .md-typeset .ft-series-compare table td:nth-child(2) { width: 10%; }
  .md-typeset .ft-series-compare table th:nth-child(3), .md-typeset .ft-series-compare table td:nth-child(3) { width: 10%; }
  .md-typeset .ft-series-compare table th:nth-child(4), .md-typeset .ft-series-compare table td:nth-child(4) { width: 11%; }
  .md-typeset .ft-series-compare table th:nth-child(5), .md-typeset .ft-series-compare table td:nth-child(5) { width: 8%; }
  .md-typeset .ft-series-compare table th:nth-child(6), .md-typeset .ft-series-compare table td:nth-child(6) { width: 8%; }
  .md-typeset .ft-series-compare table th:nth-child(7), .md-typeset .ft-series-compare table td:nth-child(7) { width: 18%; }
  .md-typeset .ft-series-compare table th:nth-child(8), .md-typeset .ft-series-compare table td:nth-child(8) { width: 29%; }
  @media screen and (max-width: 60em) {
    .md-typeset .ft-series-compare table { table-layout: auto; }
    .md-typeset .ft-series-compare table th, .md-typeset .ft-series-compare table td { width: auto; }
  }
</style>

<div class="ft-series-compare" markdown>

| 系列 | 物理层 | SDK 应用层 | 内存表 | 位置传感 | 角度 | 工作模式 | 核心特点 |
|---|---|---|---|---|---|---|---|
| STS | TTL 半双工 | `STS` | [STS](../reference/parameter/memory-sts.md) | 磁编码 | 0~360° | 伺服、多圈、连续转、步进 | 型号最多、资料最全；无接触磁编码高精度无磨损，支持一键中位校准，响应快 |
| SCS | TTL 半双工 | `SCSCL` | [SCSCL](../reference/parameter/memory-scscl.md) | 电位器 | 0~300° | 伺服、电机模式（连续转） | 性价比高、精度一般，适合简易机构与低成本项目 |
| SMS | RS485 | `SMS` | [SMS](../reference/parameter/memory-sms.md) | 磁编码 | 0~360° | 伺服、多圈、连续转 | 差分总线抗干扰强、传输距离远，支持多机串联，运行稳定性高 |
| HD | TTL 半双工 | 以型号配套资料为准 | [HLS](../reference/parameter/memory-hls.md) | 磁编码 | 0~360° | 角度伺服、多圈、恒速、恒流（恒力）、步进 | 空心杯电机 + 金属齿轮 + 双轴输出，紧凑轻量，面向轻量双足关节 |
| HLS | TTL 半双工 | `HLSCL` | [HLS](../reference/parameter/memory-hls.md) | 磁编码 | 0~360° | 角度伺服、多圈（±7 圈）、恒速、恒流（恒力）、步进 | 扭矩软件限幅、柔顺力控，实时状态反馈，支持总线 OTA 升级 |
| FU | CAN(UAVCAN) | UAVCAN | [UAVCAN](../reference/parameter/memory-fu.md) | 磁编码 | 180°±5° | 伺服、恒速、恒流、电机 | CAN 实时性与容错性好；无刷大扭矩、钛齿金属壳、IP66，带 PWM 备用控制接口 |

</div>

!!! info "表里的角度与模式是系列级概览"
    同一系列的不同型号可能只支持其中一部分。`FU` 的角度按现售型号（FU-8830-C001）标注，实际以型号页为准。「内存表」列指向该系列的系列级指南；`HD` 暂无独立内存表页，其寄存器布局与 HLS 相近，暂以 [HLS 内存表](../reference/parameter/memory-hls.md) 为参考，最终以型号配套资料为准。`SMS`（RS485）与 `SMSMB`（MODBUS-RTU）是两套不同的内存表，寻址方式不通用。`HD`、`HLS` 的「步进」模式只在部分型号的官网描述中出现，是否支持以具体型号为准。

## PWM 舵机

标准 PWM 信号控制，电位器或磁编码采集位置（官网将 360° 磁编码、带反馈款单列子类），常见 0~180°（部分型号 300°/360°，也可定制连续转）。只有基础伺服角度模式，**无总线功能**，单舵机独立接线，成本低廉，用于模型、简易样机。

- PWM 舵机通常由周期脉冲控制目标位置，不通过总线 ID 寻址。不同型号的允许脉宽、周期、电压、行程以及是否支持反馈可能不同。总线 SDK 与 FD 扫描流程**不适用于**普通 PWM 型号。

## 新手起步清单

1. **一只主流型号**：如 ST-3215-C001——资料最多，出问题最容易搜到答案。
2. **配套调试板**：TTL 与 SMS（RS485）舵机共用一块 `FE-URT2-C001`；FU 舵机用 `FE-SCPC-C003`。见[调试板与适配器](../tools/adapters.md)。
3. **独立电源**：不要用开发板的 5V 引脚直接给舵机供电；按型号堵转电流和同时动作数量留余量。
4. **共地**：调试板、舵机电源、控制平台必须共地。
5. **按[开始使用](../getting-started/index.md)走一遍**，再回来对照写自己的代码。

## 常见误区

!!! warning "TTL 和 RS485 不能靠改波特率互换"
    TTL 总线是单端半双工，需要 TTL 调试板或正确设计的单线半双工电路；RS485 是差分总线，需要 RS485 收发器和正确的 A/B 接线。换物理接口要换舵机型号或加对应收发/调试电路，软件改波特率解决不了。另外 RS485 的终端电阻与拓扑要按具体系统设计。

!!! warning "内存表不通用"
    这些系列的数据包协议有相似之处，但**寄存器地址、数据意义和能力并非全部相同**。不要把 STS 的内存表直接套到 SCS 或 HLS 上，务必查当前型号对应的内存表（见[协议参数](../reference/index.md)）。

!!! warning "PWM 舵机和总线舵机是两类东西"
    PWM 舵机由周期脉冲控制位置，没有总线 ID，不能用总线 SDK 读回数据。总线 SDK 与 FD 扫描流程不适用于普通 PWM 型号。

!!! note "提交技术支持前先记录"
    完整型号、标签照片、额定电压、物理接口、固件/内存表版本、当前 ID、当前波特率、调试板型号和控制平台——这些信息能让支持人员和 AI 助手更快帮你定位问题。

## 下一步去哪

| 你想… | 去这里 |
| --- | --- |
| 继续比较具体参数、锁定型号 | [产品规格目录](datasheets/index.md) |
| 动手接线、让舵机动起来 | [开始使用](../getting-started/index.md) |
| 查协议、寄存器与内存表 | [协议参数](../reference/index.md) |
| 遇到通信不上、舵机无响应 | [故障排查](../troubleshooting.md) |
| 找固件、软件与驱动 | [资料下载](../downloads.md) |
