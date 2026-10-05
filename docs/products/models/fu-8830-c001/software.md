# FU-8830-C001 · 程序开发

[型号概览与资料](main.md) · [结构设计](mechanical.md)

控制接口：**CAN**。先将完整型号后缀与实物标签核对。

<!-- official-control:start -->
## 官网型号控制参数

[官网来源](https://www.feetechrc.com/503338) · 2026-10-02

| 参数 | 官网规格原文（含测试条件） |
| --- | --- |
| 控制信号Command signal | Pulse width modulation |
| 通讯协议 Communication Protocol | UAVCAN |
| 控制系统类型 Control System Type | Digital comparator |
| 脉冲宽度范围Pulse width range | 500~2500 μ sec |
| 中立位置Stop position | 1500 μ sec |
| 操作角度Running degree | 180±5°(at 500→2500μsec) |
| 旋转方向Rotating direction | 逆时针 Counterclockwise(在1500→2000 μsec) |

寄存器写入仍需本完整型号与固件对应的内存表；此规格表不能替代内存表。
<!-- official-control:end -->

## 选择应用层

本 Wiki 目前没有 CAN / UAVCAN 的应用层教程。现有 `SCSCL`、`SMS_STS`、`HLSCL` 三套内存表都针对 TTL 或 RS485 总线产品，不能用于本型号；CAN 接口本身也不能证明兼容其中任何一套。

取得本型号的 CAN / UAVCAN 协议资料与对应固件版本后，再确定报文格式、节点地址、参数索引与单位，然后才考虑写入配置。

| 开发环境 | 已有指南 |
| --- | --- |
| PC / 树莓派 / Jetson | [Python](../../../sdk/python.md) |
| Arduino / ESP32 / PlatformIO | [Arduino / ESP32](../../../sdk/arduino.md) |
| Linux C++ / STM32 HAL | [Linux](../../../sdk/linux.md) / [STM32](../../../sdk/stm32.md) |

以上为共享 SDK 教程，示例以 TTL / RS485 总线产品为主；本资料包尚未提供经本型号实物验证的 CAN 专用示例。

## 先读后动的联调顺序

1. 按[供电与接线](../../../getting-started/wiring.md)及[调试板与适配器](../../../tools/adapters.md)确认电源、共地与 CAN 接线（CAN_H / CAN_L、终端电阻、总线拓扑）。CAN 需要收发器，不能直接接到普通串口或 TTL 调试板。
2. 先只连接一只舵机、脱开机构负载并留出上电动作空间，按确认过的资料设定节点地址与波特率；本页不假定出厂默认值。
3. 核实固件与协议资料版本，先只做状态读取和只读查询，记录返回值与超时，再考虑写入。
4. 确认使能状态、控制模式、单位以及软件 / 机械限位。本型号**没有机械限位**，行程完全由控制与机构限制，必须先在空载状态下确认有效的位置或脉宽范围。
5. 单机验证通过后，再加入唯一节点地址、有限重试、失联处理和多节点总线通信。

共享流程见[第一次运动](../../../getting-started/first-motion.md)，异常定位见[常见问题](../../../troubleshooting.md)。

## 必须补齐的型号信息

查看[资料清单](main.md#resources)。除非已有文件并明确注明适用范围，否则针序、CAN 报文格式、控制限制、保护阈值、固件行为和型号验证代码仍需确认。缺失值不等于零，也不等于默认值。

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
