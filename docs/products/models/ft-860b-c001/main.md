# FT-860B-C001

![FT-860B-C001](images/main.webp){ .ft-model-main-image }

本页提供 `FT-860B-C001` 的主要产品规格，便于完成供电、控制与机械集成选型。

[返回 PWM 系列目录](../../datasheets/pwm.md){ .md-button }

## 开始集成

| 我要做什么 | 从这里开始 | 需要确认什么 |
| --- | --- | --- |
| 编写控制程序 | [程序开发](software.md) | 接口、应用层、先读后动的联调步骤与验证记录 |
| 设计支架或关节 | [结构设计](mechanical.md) | 图纸、模型、基准、输出轴及线缆空间 |
| 收集工程文件 | [资料下载与完整性](#resources) | 已提供的附件与待补充资料 |

## 关键参数

| 项目 | 参数 |
| --- | --- |
| 输入电压 | **7.4 V** |
| 堵转扭矩 | **60 kg·cm@7.4V** |
| 控制接口 | `PWM` |
| 产品系列 | `FT` |
| 产品型号 | `FT860BL-C001` |
| 资料版本 | `A/0` |

!!! info "选型提示"
    堵转扭矩是用于产品比较的短时极限值，不是持续工作点。最终设计请结合工作周期、温升、冲击、加速度和机构摩擦保留合适余量。

## 选型与使用

1. 核对实物标签与资料版本是否与本页一致。
2. 先从本型号正式资料确认允许输入范围，再选择稳压电源；目录中的单一电压值不能自动扩展成电压范围。电流按同时动作工况确认。
3. 控制器、接线方式和 PWM 输出参数必须匹配本完整型号的正式资料。
4. 使能扭矩前确认安装空间、输出轴、行程与机械限位。

控制信号与首次调试请继续查看本型号的[程序开发](software.md)；PWM 型号不使用串行总线 SDK。

<!-- official-specs:start -->
## 官网型号详细参数

[飞特官网型号页](https://www.feetechrc.com/535015) · 核对日期：2026-10-02；页面型号：FT-860B-C001。

| 参数 | 官网规格原文（含测试条件） |
| --- | --- |
| 型 号 Model： | FT-860B-C001 |
| 存储温度 Storage Temperature Range | -30℃～80℃ |
| 运行温度 Operating Temperature Range: | -20℃～60℃ |
| 尺寸 Size: | A：40mm B：20mm C: 39.9mm |
| 重量 Weight: | 84g± 2g |
| 齿轮类型 Gear type: | 钢 Steel |
| 机构极限角度 Limit angle: | No limit |
| 轴承 Bearing: | 滚珠轴承 Ball bearings |
| 出力轴 Horn gear spline: | 25T/5.9mm |
| 减速比Gear Ratio： | 1/356 |
| 外壳 Case: | Aluminum |
| 舵机线 Connector wire: | 30±0.5CM |
| 马达 Motor: | Brushless Motor |
| 工作电压Operating Voltage Range: | 6-9V |
| 静态电流Idle current (atstopped) | 12mA@8.4V |
| 空载速度 No load speed: | 0.086sec/60°(115RPM)@8.4V |
| 空载电流 Runnig current(at no load) : | 490mA@8.4V |
| 堵转扭矩 Peak stall torque: | 70kg.cm@8.4V |
| 额定扭矩 Rated torque: | 23kg.cm@8.4V |
| 控制信号Command signal | Pulse width modulation |
| 控制系统类型 Control System Type | Digital comparator |
| 脉冲宽度范围Pulse width range | 500~2500 μ sec |
| 中立位置Stop position | 1500 μ sec |
| 操作角度Running degree | 180±5°(at 500→2500μsec) |
| 死区宽度Dead band width | ≤4 μ sec |
| 旋转方向Rotating direction | 逆时针 Counterclockwise(在1500→2500 μsec) |
| 电子保护 Electronic Protection | 堵转8秒/Stall 8sec |

### 规格书中的补充参数

[官网规格书](https://www.feetechrc.com/Data/feetechrc/upload/file/20260623/6391782102979983311698911.pdf)

| 参数 | 规格原文 | PDF 页码 |
| --- | --- | --- |
| 角度传感器 Angle Sensor | 类型Type / Carbon-Film Potentiometer | 5 |
| 齿轮虚位Back Lash | ≦0.5° | 5 |
| 出力轴螺丝 The rocker screw | M3X6 | 5 |
| 两边角度差 Left&Right Travelling Angledeviation | ≤ 5° | 5 |
| 回中差 Centering Deviation | ≦2° | 5 |
| 信号周期 Signal Period | 20ms | 8 |
| 信号高电平电压 Signal high Voltage | 2V-5V | 8 |
| 信号低电平电压 Signal Low Voltage | 0.0V-0.45V | 8 |

![FT-860B-C001 机身尺寸图](images/drawing.webp){ .ft-model-drawing }

[查看原尺寸图纸](images/drawing.webp)
<!-- official-specs:end -->

<!-- product-resources:start -->
## 资料下载与完整性 {#resources}

本地附件已收录在型号资料包中；PDF 规格书通过官网链接查看，不包含在离线包中。“待补充”表示尚未提供，系列教程不能代替型号专用参数确认。

| 资料 | 状态 / 文件 | 版本 |
| --- | --- | --- |
| 型号规格书 | [官网查看（需联网）](https://www.feetechrc.com/Data/feetechrc/upload/file/20260623/6391782102979983311698911.pdf) | A/0 |
| 接口与针序图 | 待补充 | — |
| 型号内存表 / 固件说明 | 不适用 | — |
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
