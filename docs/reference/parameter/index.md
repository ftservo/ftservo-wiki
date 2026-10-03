# 内存表参数

按控制协议浏览飞特舵机的内存表参数。每份内存表列出该系列寄存器的地址、长度、单位、取值范围、默认值和读写权限，点击系列可查看完整的内存表指南。

如果尚未确定系列，可先使用[产品选型器](../../products/index.md)按应用条件筛选，或在[协议与参数](../index.md)查看各系列的使用边界。

| 内存表 | 适用系列 | 协议 / 总线 | 寻址方式 | 内存表指南 |
| --- | --- | --- | --- | --- |
| SCSCL | SCS / SCSCL | TTL 半双工串行总线 | 按地址直接寻址 | [查看内存表](memory-scscl.md) |
| STS | STS | TTL 半双工串行总线 | 按地址直接寻址 | [查看内存表](memory-sts.md) |
| HLS | HLS | TTL 半双工串行总线 | 按地址直接寻址 | [查看内存表](memory-hls.md) |
| SMS | SMS | RS485 差分总线 | 按地址直接寻址 | [查看内存表](memory-sms.md) |
| SMSMB | SMSMB | MODBUS-RTU 标准协议(RS485) | MODBUS 寄存器地址 | [查看内存表](memory-smsmb.md) |
| SHC | SHC | CANopen 协议（CAN 总线） | 对象字典索引＋子索引 | [查看内存表](memory-shc.md) |
| UAVCAN | 磁编码 UAVCAN | UAVCAN 协议（CAN 总线） | 分页寄存器（页码×64＋序号） | [查看内存表](memory-fu.md) |

!!! warning "提示"
    各系列内存表地址结构互不通用：串行系列(SCSCL/STS/HLS/SMS)地址相近但不可混用，SMSMB、SHC、UAVCAN 采用完全不同的寻址方式。修改参数前请先确认型号对应的应用层与内存表版本，并以具体型号和固件的正式文件为准。
