# Protocol and parameters

Use this section as a reference. For your first connection or run, start with [Get started](../getting-started/index.md). Model-specific addresses, units, modes and limits require the formal documentation for that model and firmware. All memory tables are summarized under [Memory Table Parameters](parameter/index.md).

| Confirmed family/interface | Reference | Boundary |
| --- | --- | --- |
| SCS / SCSCL | [SCSCL memory-table guide](parameter/memory-scscl.md) | Do not substitute STS/SMS or HLS addresses and units |
| STS | [STS memory-table guide](parameter/memory-sts.md) | Half-duplex TTL; confirm the exact model and firmware |
| SMS | [SMS memory-table guide](parameter/memory-sms.md) | RS485; same addresses as STS, different interface |
| HLS | [HLS memory-table guide](parameter/memory-hls.md) | Use the HLS application layer and matching document revision |
| SMSMB | [SMSMB memory-table guide](parameter/memory-smsmb.md) | Standard MODBUS-RTU protocol; addresses are not shared with the serial families |
| SHC | [SHC memory-table guide](parameter/memory-shc.md) | CANopen over CAN bus; addressed by object-dictionary index and sub-index, not shared with the serial families |
| UAVCAN | [UAVCAN memory-table guide](parameter/memory-fu.md) | CAN bus paged registers (page ×64 + index); address structure differs from all other families |
| PWM | [PWM getting started](../getting-started/pwm.md) | No serial-bus registers, IDs or baud rates |
| Application layer unconfirmed | [Find model resources](../products/index.md) | TTL / RS-485 alone does not establish memory-table compatibility |

## Look up a parameter

1. Confirm the full model suffix, firmware and formal memory-table revision.
2. Identify the address, length, units, allowed range and read/write permissions.
3. Check persistence, torque-enable state, operating mode and conditions for changes. Do not assume a temporary setting survives power loss.
4. Read through the matching application layer first; change one item only under confirmed conditions and record the result.

[Packet format and commands](protocol/index.md) support protocol diagnosis; [SDK guides](../sdk/index.md) support everyday development. Similar packet framing does not make memory tables interchangeable.
