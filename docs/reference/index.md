# 协议与参数

此处是查阅参考资料的入口。第一次接线或运行请先走[开始使用](../getting-started/index.md)；型号专用地址、单位、模式及限制以该型号和固件的正式文件为准。各系列内存表已汇总在[内存表参数](parameter/index.md)目录下。

| 已确认的控制系列 | 参考资料 | 使用边界 |
| --- | --- | --- |
| SCS / SCSCL | [SCSCL 内存表指南](parameter/memory-scscl.md) | 不能套用 STS/SMS 或 HLS 地址与单位 |
| STS | [STS 内存表指南](parameter/memory-sts.md) | 半双工 TTL；仍需核对具体型号、固件 |
| SMS | [SMS 内存表指南](parameter/memory-sms.md) | RS485；地址与 STS 相同，接口不同 |
| HLS | [HLS 内存表指南](parameter/memory-hls.md) | 使用 HLS 应用层与对应版本资料 |
| SMSMB | [SMSMB 内存表指南](parameter/memory-smsmb.md) | MODBUS-RTU 标准协议；地址与串行系列不通用 |
| SHC | [SHC 内存表指南](parameter/memory-shc.md) | CANopen 协议（CAN 总线）；以对象字典索引与子索引寻址，与串行系列地址结构不通用 |
| UAVCAN | [UAVCAN 内存表指南](parameter/memory-fu.md) | CAN 总线分页寄存器（页码×64＋序号）；与其他系列地址结构不通用 |
| PWM | [PWM 控制入门](../getting-started/pwm.md) | 不使用串行总线寄存器、ID 或波特率 |
| 应用层尚未确认 | [查找型号资料](../products/index.md) | 不能仅凭 TTL / RS-485 接口选择内存表 |

## 查参数的顺序

1. 确认完整型号与后缀、固件及正式内存表版本。
2. 找到参数的地址、长度、单位、取值范围和读写权限。
3. 核对持久化、扭矩使能、工作模式及修改条件，避免把暂存参数当作断电保存参数。
4. 先用匹配应用层读取验证，再在确认过的条件下修改单项并记录结果。

[数据包格式与指令](protocol/index.md)适合排查协议细节；[SDK 指南](../sdk/index.md)适合日常开发。共享的数据包外观并不意味着内存表互换。
