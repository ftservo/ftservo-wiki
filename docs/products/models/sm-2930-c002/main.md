# SM-2930-C002

![SM-2930-C002 产品主图](images/main.webp){ .ft-model-main-image }
`SM-2930-C002` 是官方目录中的24V 30KG.CM RS485 串行总线舵机。本页参数转录自飞特官网该型号产品页（2026-10-02 抓取），用于选型对比与集成规划。

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
| 输入电压 | **16.8–25.2 V** |
| 堵转扭矩 | **30 kg·cm@24V** |
| 空载速度 | 0.083 s/60°（120 RPM）@24V |
| 行程 / 旋转 | 官方参数表未标注 |
| 控制接口 | `RS-485` |
| 产品系列 | `SMS` |
| 外形尺寸 | 40 × 28 × 92.2 mm |
| 重量 | 230 ± 5 g |
| 齿轮 | 钢齿轮 |
| 电机 | 无刷电机 |
| 通信协议 | RS-485 半双工异步串行，官方标注 254 个 ID 可选，38400bps ~ 1Mbps |
| 资料版本 | `A/0`（官方页面抓取日期 2026-10-02） |

!!! info "选型提示"
    堵转扭矩是用于产品比较的短时极限值，不是持续工作点。最终设计请结合工作周期、温升、冲击、加速度和机构摩擦保留合适余量。

## 选型与使用

1. 核对实物标签与资料版本是否与本页一致。
2. 供电范围以本页参数表为准；目录电压标注不能自动扩展成电压范围，电流按同时动作工况确认。
3. 控制器、接线方式与控制协议必须匹配本完整型号后，再下发任何指令。
4. 使能扭矩前确认安装空间、输出轴、行程与机械限位。

通信指令和软件集成方法请继续查看 [SDK 指南](../../../sdk/index.md)以及对应产品系列的协议资料。

<!-- official-specs:start -->
## 官网型号详细参数

[飞特官网型号页](https://www.feetechrc.com/503950) · 核对日期：2026-10-02；页面型号：SM-2930-C002。

| 参数 | 官网规格原文（含测试条件） |
| --- | --- |
| 型 号 Model： | SM-2930-C002 |
| 存储温度 Storage Temperature Range | -40℃～80℃ |
| 运行温度 OperatinTemperatureRange: | -40℃～60℃ |
| 尺寸 Size: | A：40mm B：28mm C：92.2mm |
| 重量 Weight: | 230± 5g |
| 齿轮类型 Gear type: | 钢 Steel |
| 机构极限角度 Limit angle: | No Limit |
| 轴承类型 Bearing type： | 滚珠轴承 Ball bearings |
| 大扭矩High torque： | 30Kg.cm |
| 宽工作电压Wide operating voltage： | 16.8V-25.2V 供电 |
| 马达 Motor: | Brushless Motor |
| 高分辨率High resolution： | 12 位编码器（360 度 0.088°） |
| 伺服控制模式Servo control mode: | 转动范围0-360°及多圈任意[敏感词]角度 |
| 控制信号 Command signal： | Digital Packet |
| ID范围 ID range： | 254个ID地址可选 |
| 波特率Baud rate： | 38400bps ~ 1 Mbps |
| 额定负载 Rated Torgue： | 10kg.cm |
| 额定电流 Rated Current： | 600mA |
| 空载速度No Load Speed： | 0.083sec/60°(120RPM)@24V |
| 静态电流Quiescent Current： | 24mA@24V |
| 空载电流No-load current： | ≦120mA@24V |
| 堵转电流Stall current： | 1.6A@24V |
| 分辨率Resolution [deg/pulse]： | 0.088°(360°/4096) |
| 堵转扭矩Stall torque： | 30kg.cm@24V |
| 反馈 Feedback： | Load（负载）, Position（位置）,Speed（工作速度）, Input Voltage（输入电压），Current（工作电流）,Temperature（工作温度） |

附件核对（未纳入资料包）：PDF content model not verified: SM-2930-C002.pdf

官网其它关联附件（适用型号尚未核实）：

- [SM-2930-C002.pdf](https://www.feetechrc.com/Data/feetechrc/upload/file/20260622/6391773551419635012270594.pdf)

![SM-2930-C002 机身尺寸图](images/drawing.webp){ .ft-model-drawing }

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
