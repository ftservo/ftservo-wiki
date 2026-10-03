# SM-45BL-C002

![SM-45BL-C002 产品主图](images/main.webp){ .ft-model-main-image }
`SM-45BL-C002` 是官方目录中的24V 45kg.cm Modbus-RTU 舵机。本页参数转录自飞特官网该型号产品页（2026-10-02 抓取），用于选型对比与集成规划。

[返回 SM 系列目录](../../datasheets/sm.md){ .md-button }

## 开始集成

| 我要做什么 | 从这里开始 | 需要确认什么 |
| --- | --- | --- |
| 编写控制程序 | [程序开发](software.md) | 接口、应用层、先读后动的联调步骤与验证记录 |
| 设计支架或关节 | [结构设计](mechanical.md) | 图纸、模型、基准、输出轴及线缆空间 |
| 收集工程文件 | [资料下载与完整性](#resources) | 已提供的附件与待补充资料 |

## 关键参数

| 项目 | 参数 |
| --- | --- |
| 输入电压 | **24 V** |
| 堵转扭矩 | **45 kg·cm@24V** |
| 空载速度 | 0.142 s/60°（70 RPM） |
| 行程 / 旋转 | 360°（0~4095，CW） |
| 控制接口 | `RS-485` |
| 产品系列 | `SMS` |
| 外形尺寸 | 46.5 × 28.5 × 34 mm |
| 重量 | 100 g |
| 齿轮 | 钢齿轮（减速比 353:1） |
| 电机 | 无刷电机 |
| 通信协议 | Modbus-RTU（RS-485 物理层），ID 0–253，38400bps ~ 1Mbps |
| 资料版本 | `A/0`（官方页面抓取日期 2026-10-02） |

!!! info "选型提示"
    堵转扭矩是用于产品比较的短时极限值，不是持续工作点。最终设计请结合工作周期、温升、冲击、加速度和机构摩擦保留合适余量。

!!! warning "本型号为 Modbus-RTU 协议"
    SM-45BL-C002 使用标准 **Modbus-RTU** 协议（RS-485 物理层），与 SMS 系列常用的 SMS_STS 内存表和数据包协议不是同一套。站内暂无 Modbus-RTU 寄存器文档，请以厂家提供的本型号寄存器表为准，不要套用 SMS_STS 的寄存器地址、单位或控制模式。

## 选型与使用

1. 核对实物标签与资料版本是否与本页一致。
2. 供电范围以本页参数表为准；目录电压标注不能自动扩展成电压范围，电流按同时动作工况确认。
3. 控制器、接线方式与控制协议必须匹配本完整型号后，再下发任何指令。
4. 使能扭矩前确认安装空间、输出轴、行程与机械限位。

通信指令和软件集成方法请继续查看 [SDK 指南](../../../sdk/index.md)以及对应产品系列的协议资料。

<!-- official-specs:start -->
## 官网型号详细参数

[飞特官网型号页](https://www.feetechrc.com/24v-45kg-rs485-serial-bus-steering-gear) · 核对日期：2026-10-02；页面型号：SM-45BL-C002。

| 参数 | 官网规格原文（含测试条件） |
| --- | --- |
| 型 号 Model： | SM-45BL-C002 |
| 存储温度 Storage Temperature Range | -30℃～80℃ |
| 运行温度 Operating Temperature Range: | -20℃～80℃ |
| 尺寸 Size: | A：46.5mm B：28.5mm C：34mm |
| 重量 Weight: | 100g |
| 齿轮类型 Gear type: | Steel Gear (Gear Ratio 353:1 ) |
| 机构极限角度 Limit angle: | NO Limiter |
| 轴承 Bearing: | 2 Ball bearings |
| 出力轴 Horn gear spline: | 25T (OD5.96mm) |
| 摆臂 Horn type: | Aluminium |
| 外壳 Case: | Aluminium |
| 舵机线 Connector wire: | 150mm ±5 mm |
| 马达 Motor: | Brushless motor |
| 工作电压Operating Voltage Range: | 24V |
| 空载速度 No load speed: | 0.142sec/ 60degree 70RPM |
| 空载电流 Runnig current(at no load) : | 160 mA@24V |
| 堵转扭矩 Peak stall torque: | 45kg.cm@24V |
| 额定扭矩 Rated torque: | 15kg.cm@24V |
| 堵转电流 Stall current: | 2300mA@24V |
| 额定负载Rated Load | 15kg. cm≤ |
| 额定电流Rated current | 900mm≤ |
| KM常数 | 19kg. cm/A |
| 电机内阻Terminal resistance | 7Ω |
| 控制信号 Command signal: | Bus Packet Communication RS485 |
| 协议类型 Protocol Type: | Modbus-RTU |
| ID范围 ID range: | 0-253 |
| 通读速率 Communication Speed: | 38400bps ~ 1 Mbps |
| 旋转角度 Running degree: | 360° (when 0~4095)-CW |
| 反馈 Feedback: | Position,Speed,Voltage,Load,Temperature |
| 位置传感器分辨率 Position Sensor Resolution: | 12Bits Magnetic Coding(360° /4096) |

附件核对（未纳入资料包）：Different model PDF: SM45BL-C001-串型规格书-20210111.pdf

官网其它关联附件（适用型号尚未核实）：

- [SM45BL-C001-串型规格书-20210111.pdf](https://www.feetechrc.com/Data/feetechrc/upload/file/20210630/6376066619149072575092101.pdf)

![SM-45BL-C002 机身尺寸图](images/drawing.webp){ .ft-model-drawing }

[查看原尺寸图纸](images/drawing.webp)
<!-- official-specs:end -->

<!-- product-resources:start -->
## 资料下载与完整性 {#resources}

本地附件已收录在型号资料包中；PDF 规格书通过官网链接查看，不包含在离线包中。“待补充”表示尚未提供，系列教程不能代替型号专用参数确认。

| 资料 | 状态 / 文件 | 版本 |
| --- | --- | --- |
| 型号规格书 | 待补充 | — |
| 接口与针序图 | 待补充 | — |
| 型号内存表 / 固件说明 | 待补充 | — |
| 2D 安装图 | [drawing.webp](images/drawing.webp) | — |
| STEP / 3D 模型 | 待补充 | — |
| 型号验证示例 | 待补充 | — |
| 原始测试数据 | 待补充 | — |
| 测试记录与条件说明 | 待补充 | — |

[下载资料清单](manifest.json) · [申请缺失资料](#support)

需要包含中英文说明和已收录附件的离线 ZIP，参见[型号资料包导出](../../../downloads.md#product-packages)。
<!-- product-resources:end -->
## 申请资料与反馈问题 {#support}

向已有的飞特技术支持联系人提供完整标签型号及后缀、固件版本（如已知）和正在使用的资料版本。

- 程序问题：主控与系统、SDK 版本或提交号、适配器与接口、供电电压、已确认的 ID / 波特率（仅总线型号）、最小复现步骤及日志。
- 结构问题：图纸 / 模型版本、标注尺寸、所需行程、舵盘 / 支架、负载与力臂、工作周期及干涉位置。
- 缺少资料：直接说明资料表中的具体项目，例如“本型号 STEP 和带公差的安装图”。

本资料包当前提供规格摘要和集成检查步骤；文件可下载不代表已验证你的固件、负载工况或装配方案。
