# Memory Table Parameters

Browse FEETECH servo memory table parameters by control protocol. Each memory table lists the address, length, units, allowed range, default value and read/write permissions of that family's registers; open a family for the full memory-table guide.

If you have not selected a family, start with the [product selector](../../products/index.md), or review the boundaries of each family under [Protocol and parameters](../index.md).

| Memory table | Family | Protocol / bus | Addressing | Memory-table guide |
| --- | --- | --- | --- | --- |
| SCSCL | SCS / SCSCL | Half-duplex TTL serial bus | Direct addressing by address | [View memory table](memory-scscl.md) |
| STS | STS | Half-duplex TTL serial bus | Direct addressing by address | [View memory table](memory-sts.md) |
| HLS | HLS | Half-duplex TTL serial bus | Direct addressing by address | [View memory table](memory-hls.md) |
| SMS | SMS | Differential RS485 bus | Direct addressing by address | [View memory table](memory-sms.md) |
| SMSMB | SMSMB | Standard MODBUS-RTU (RS485) | MODBUS register addresses | [View memory table](memory-smsmb.md) |
| SHC | SHC | CANopen over CAN bus | Object-dictionary index plus sub-index | [View memory table](memory-shc.md) |
| UAVCAN | Magnetically encoded UAVCAN | UAVCAN over CAN bus | Paged registers (page ×64 + index) | [View memory table](memory-fu.md) |

!!! warning "Do not reuse addresses across families"
    Address structures are not interchangeable: the serial families (SCSCL/STS/HLS/SMS) use similar-looking addresses that must not be mixed, while SMSMB, SHC and UAVCAN use entirely different addressing schemes. Before changing a parameter, confirm the application layer and memory-table revision for your model, and treat the formal documentation for that model and firmware as authoritative.
