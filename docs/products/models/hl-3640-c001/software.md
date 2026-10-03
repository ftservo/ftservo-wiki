# HL-3640-C001 · 程序开发

[型号概览与资料](main.md) · [结构设计](mechanical.md)

控制接口：**TTL**。先将完整型号后缀与实物标签核对。

<!-- official-control:start -->
## 官网型号控制参数

[官网来源](https://www.feetechrc.com/556986) · 2026-10-02

| 参数 | 官网规格原文（含测试条件） |
| --- | --- |
| 运行模式 Operating Modes： | 模式0：角度伺服模式 （默认此模式，0-360度[敏感词]位置可控） Mode 0: Angle servo mode (default mode, absolute position controllable from 0-360 degrees) |
| 多圈模式 Multi-Loop Mode： | [敏感词]精度下可以正负7圈[敏感词]位置控制，但掉电圈数不保存（扩大分辨率，圈数可翻倍） control of positive and negative 7 turns at the highest accuracy, but the umber of power failure turns is not saved (the resolution can be expanded, and the number of turns can be doubled) |
| 恒力输出 Constant force output： | 设定输出扭矩值，舵机可保持该扭矩(44号地址输入相对应的目标扭矩值，舵机可保持该扭矩) Set the output torque value, the servo can maintain this torque (input the target torque value corresponding to address 44, the servo can maintain this torque) |
| 控制信号 Command signal: | Digital Packet |
| 协议类型 Protocol Type: | Half Duplex Asynchronous Serial Communication |
| ID范围 ID range: | 0-253 |
| 通读速率 Communication Speed: | 38400bps ~ 1 Mbps |
| 控制算法 Control Algorithm： | PID |
| 中位 Neutral Position： | 180°（2048） |
| 旋转角度 Running degree: | 360° (when 0~4096) |
| 电子分辨率 Resolution [deg/pulse] | 0.088°(360°/4096) |
| 旋转方向 Rotating Direction： | Clockwise(0→4096） |
| 反馈 Feedback: | Load（负载）, Position（位置）,Speed（工作速度）, Input Voltage（输入电压），Current（工作电流）,Temperature（工作温度） |

寄存器写入仍需本完整型号与固件对应的内存表；此规格表不能替代内存表。
<!-- official-control:end -->

## 选择应用层

系列入口：**HLS** → Python `hls`；Arduino / C++ `HLSCL`。参阅[系列内存表指南](../../../reference/parameter/memory-hls.md)与[数据包协议](../../../reference/protocol/index.md)。这里仅确定系列入口，不代表已确认本型号及固件的寄存器地址、单位或模式。

| 开发环境 | 已有指南 |
| --- | --- |
| PC / 树莓派 / Jetson | [Python](../../../sdk/python.md) |
| Arduino / ESP32 / PlatformIO | [Arduino / ESP32](../../../sdk/arduino.md) |
| Linux C++ / STM32 HAL | [Linux / STM32](../../../sdk/linux-stm32.md) |

以上是共享 SDK 教程；本资料包目前尚未提供经本型号实物验证的专用示例。

## 先读后动的联调顺序

1. 按[供电与接线](../../../getting-started/wiring.md)及[适配器指南](../../../tools/adapters.md)确认电源、共地、针序与匹配的 TTL / RS-485 接口。具体型号针序图优先于线色经验。
2. 先只连接一只舵机、脱开机构负载并留出上电动作空间，按确认过的发现流程读取当前 ID 与波特率；本页不假定出厂默认值。
3. 核实 SDK 类及固件 / 内存表版本，先运行单播 Ping 和受支持的只读查询，记录返回值与超时，再考虑写入。
4. 确认扭矩使能状态、控制模式、单位及软件 / 机械限位。使用匹配示例进行已验证的小幅运动，不套用其他系列的位置范围或寄存器限制。
5. 单机验证通过后，再加入唯一 ID、有限重试、失联处理和多机控制。

共享流程见[第一次运动](../../../getting-started/first-motion.md)，异常定位见[常见问题](../../../troubleshooting.md)。

## 必须补齐的型号信息

查看[资料清单](main.md#resources)。除非已有文件并明确注明适用范围，否则针序、控制限制、保护阈值、固件行为和型号验证代码仍需确认。缺失值不等于零，也不等于默认值。

## 留下可复现的接入记录

| 记录项 | 项目填写内容 |
| --- | --- |
| 实物完整标签 / 固件 | 测试前记录 |
| 主控、系统、工具链 | 记录准确版本 |
| SDK 提交号 / 示例路径（总线）或 PWM 配置 | 记录代码版本及实际参数 |
| 电源 / 适配器 / 接线图版本 | 记录实测条件 |
| 初始状态、命令与预期结果 | 从最小已验证操作开始 |
| 实际响应、超时及停止行为 | 保存日志，注明日期与负载状态 |

申请型号专用示例时，将记录交给[技术支持](main.md#support)。
