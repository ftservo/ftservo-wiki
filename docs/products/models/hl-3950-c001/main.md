# HL-3950-C001

![HL-3950-C001](images/main.webp){ .ft-model-main-image }


本页提供 `HL-3950-C001` 的主要产品规格，便于完成供电、控制与机械集成选型。

[返回 HL 系列目录](../../datasheets/hl.md){ .md-button }

## 开始集成

| 我要做什么 | 从这里开始 | 需要确认什么 |
| --- | --- | --- |
| 编写控制程序 | [程序开发](software.md) | 接口、应用层、先读后动的联调步骤与验证记录 |
| 设计支架或关节 | [结构设计](mechanical.md) | 图纸、模型、基准、输出轴及线缆空间 |
| 收集工程文件 | [资料下载与完整性](#resources) | 已提供的附件与待补充资料 |

## 关键参数

| 项目 | 参数 |
| --- | --- |
| 输入电压 | **9–12.6 V** |
| 堵转扭矩 | **50 kg·cm@12V** |
| 控制接口 | `TTL` |
| 产品系列 | `HLS` |
| 产品型号 | `HLS3950M-C001` |
| 资料版本 | `A/0` |

## 专业选型参数

| 参数 | 规格 |
| --- | --- |
| 空载速度 | 75 rpm@12 V (0.133 s/60°) |
| 位置控制范围 | 0–360° |
| 连续旋转 | 支持，使用电机模式 |
| 电机 | 空心杯（官网未明确有刷/无刷，分类待确认） |
| 齿轮 / 外壳 | 钢齿 / 全金属铝壳 |
| 输出轴型 | 双轴 |
| 尺寸 A × B × C | 45.22 × 24.72 × 35 mm |
| 最长边 | 45.22 mm |
| 重量 | 74.5 ± 1 g |

来源：[FEETECH HL-3950-C001](https://www.feetech.cn/563788.html)，核对日期 2026-10-01。位置控制范围与连续旋转分开记录；多圈模式的圈数掉电不保存。

<!-- official-specs:start -->
## 官网型号详细参数

[飞特官网型号页](https://www.feetechrc.com/563788) · 核对日期：2026-10-02；页面型号：HL-3950-C001。

| 参数 | 官网规格原文（含测试条件） |
| --- | --- |
| 型 号 Model： | HL-3950-C001 |
| 存储温度 Storage Temperature Range | -30℃～80℃ |
| 运行温度 Operating Temperature Range: | -20℃～60℃ |
| 温度 Temperature Range: | 25℃ ±5℃ |
| 湿度 Humidity Range: | 65%±10% |
| 尺寸 Size: | A：45.22mm B：24.72mm C：35mm |
| 重量 Weight: | 74.5± 1g |
| 齿轮类型 Gear type: | 钢齿steel Gear |
| 机构极限角度 Limit angle: | No limit |
| 轴承 Bearing: | 滚珠轴承 Ball bearings |
| 出力轴 Horn gear spline: | 25T/OD5.9mm |
| 减速比Gear Ratio： | 1/345 |
| 外壳 Case: | Aluminium |
| 舵机线 Connector wire: | 15CM |
| 马达 Motor: | Coreless Motor |
| 额定工作电压 Rated Input Voltage： | 9V-12.6V |
| 空载速度 No load speed: | 0.133sec/60°(75RPM)@12V |
| 空载电流 Runnig current(at no load) : | 330mA@12V |
| 堵转扭矩 Peak stall torque: | 50kg.cm@12V |
| 堵转电流 Stall current: | 2.4A@12V |
| 额定负载Rated Load： | 12.5kg. cm@12V |
| 额定电流Rated current： | 600mA@12V |
| KT常数 | 20.8kg. cm/A |
| 电机内阻Terminal resistance： | 1.2 Ω |
| 运行模式 Operating Modes： | 模式0：角度伺服模式 （默认此模式，0-360度[敏感词]位置可控） Mode 0: Angle servo mode (default mode, absolute position controllable from 0-360 degrees) |
| 恒力输出 Constant force output： | 设定输出扭矩值，舵机可保持该扭矩(44号地址输入相对应的目标扭矩值，舵机可保持该扭矩) Set the output torque value, the servo can maintain this torque (input the target torque value corresponding to address 44, the servo can maintain this torque) |
| 多圈模式 Multi-Loop Mode： | [敏感词]精度下可以正负7圈[敏感词]位置控制，但掉电圈数不保存（扩大分辨率，圈数可翻倍） control of positive and negative 7 turns at the highest accuracy, but the umber of power failure turns is not saved (the resolution can be expanded, and the number of turns can be doubled) |
| 控制信号 Command signal: | Digital Packet |
| 协议类型 Protocol Type: | Half Duplex Asynchronous Serial Communication |
| ID范围 ID range: | 0-253(默认出厂值为“ID1”） |
| 通读速率 Communication Speed: | 38400bps ~ 1 Mbps（默认出厂波特率为1000000） |
| 控制算法 Control Algorithm： | PID（可自定义） |
| 中位 Neutral Position： | 180°（2048） |
| 旋转角度 Running degree: | 360° (when 0~4096) |
| 电子分辨率 Resolution [deg/pulse] | 0.088°(360°/4096) |
| 旋转方向 Rotating Direction： | Clockwise(0→4096） |
| 反馈 Feedback: | Load（负载）, Position（位置）,Speed（工作速度）, Input Voltage（输入电压），Current（工作电流）,Temperature（工作温度） |

### 规格书中的补充参数

[官网规格书](https://www.feetechrc.com/Data/feetechrc/upload/file/20260623/6391782924959146461426248.pdf)

| 参数 | 规格原文 | PDF 页码 |
| --- | --- | --- |
| 角度传感器 Angle Sansor | 类型Type / 12Bits Magnetic Coding | 4 |
| 齿轮虚位Back Lash | ≦0.5° | 4 |
| 摇臂虚位The rocker phantom | 0° | 4 |
| 出力轴螺丝 | M3X6 | 4 |
| The rocker screw 马达 Motor | Coreless Motor | 4 |
| 信号高电平电压 Signal high Voltage | 2V-5V | 8 |
| 信号低电平电压 Signal Low Voltage | 0.0V-0.45V | 8 |

![HL-3950-C001 机身尺寸图](images/drawing.webp){ .ft-model-drawing }

[查看原尺寸图纸](images/drawing.webp)
<!-- official-specs:end -->

## 实测特性曲线

下图读取本产品文件夹中的扭矩测试工装原始结果 `test-result.json`，按工装前端的固定型号量程，在同一绘图区显示转速、电流、效率和功率，各参数使用同色的独立纵轴。默认显示与工装一致的平滑趋势，可切换为原始折线；在曲线区域移动鼠标或触摸，可同步查看扭矩及四项参数，小屏可横向滚动。

<div class="servo-characteristic-chart" data-source="../test-result.json" data-title="HLS3950M T-N 实测特性曲线">
  <p class="servo-chart-loading">正在加载扭矩测试数据…</p>
</div>

!!! note "测试数据说明"
    本案例复用扭矩测试工装导出的原始 JSON `SN12212_20260818-195011_52de9cb9.json`；测试日期为 2026-08-18，结果文件序列号为 `SN12212`。曲线展示平滑趋势，不应替代产品规格书中的额定或堵转指标。

!!! info "选型提示"
    堵转扭矩是用于产品比较的短时极限值，不是持续工作点。最终设计请结合工作周期、温升、冲击、加速度和机构摩擦保留合适余量。

## 选型与使用

1. 核对实物标签与资料版本是否与本页一致。
2. 先从本型号正式资料确认允许输入范围，再选择稳压电源；目录中的单一电压值不能自动扩展成电压范围。电流按同时动作工况确认。
3. 控制器、接线方式和 SDK 必须匹配本页列出的接口与产品系列。
4. 使能扭矩前确认安装空间、输出轴、行程与机械限位。

通信指令和软件集成方法请继续查看 [SDK 指南](../../../sdk/index.md)以及对应产品系列的协议资料。

<!-- product-resources:start -->
## 资料下载与完整性 {#resources}

本地附件已收录在型号资料包中；PDF 规格书通过官网链接查看，不包含在离线包中。“待补充”表示尚未提供，系列教程不能代替型号专用参数确认。

| 资料 | 状态 / 文件 | 版本 |
| --- | --- | --- |
| 型号规格书 | [官网查看（需联网）](https://www.feetechrc.com/Data/feetechrc/upload/file/20260623/6391782924959146461426248.pdf) | A/0 |
| 接口与针序图 | 待补充 | — |
| 型号内存表 / 固件说明 | 待补充 | — |
| 2D 安装图 | [drawing.webp](images/drawing.webp) | — |
| STEP / 3D 模型 | 待补充 | — |
| 型号验证示例 | 待补充 | — |
| 原始测试数据 | [test-result.json](test-result.json) | — |
| 测试记录与条件说明 | [test-notes.md](tests/test-notes.md) | — |

[下载资料清单](manifest.json) · [申请缺失资料](#support)

需要包含中英文说明和已收录附件的离线 ZIP，参见[型号资料包导出](../../../downloads.md#product-packages)。
<!-- product-resources:end -->

## 申请资料与反馈问题 {#support}

向已有的飞特技术支持联系人提供完整标签型号及后缀、固件版本（如已知）和正在使用的资料版本。

- 程序问题：主控与系统、SDK 版本或提交号、适配器与接口、供电电压、已确认的 ID / 波特率（仅总线型号）、最小复现步骤及日志。
- 结构问题：图纸 / 模型版本、标注尺寸、所需行程、舵盘 / 支架、负载与力臂、工作周期及干涉位置。
- 缺少资料：直接说明资料表中的具体项目，例如“本型号 STEP 和带公差的安装图”。

本资料包当前提供规格摘要和集成检查步骤；文件可下载不代表已验证你的固件、负载工况或装配方案。
