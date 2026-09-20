# Protocol and parameters

Use this section as a reference. For your first connection or run, start with [Get started](../getting-started/index.md). Model-specific addresses, units, modes and limits require the formal documentation for that model and firmware.

| Confirmed family/interface | Reference | Boundary |
| --- | --- | --- |
| SCS / SCSCL | [SCSCL memory-table guide](memory-scscl.md) | Do not substitute STS/SMS or HLS addresses and units |
| STS / SMS | [SMS / STS memory-table guide](memory-sms-sts.md) | Confirm the exact model, firmware and physical interface |
| HLS | [HLS memory-table guide](memory-hls.md) | Use the HLS application layer and matching document revision |
| PWM | [PWM getting started](../getting-started/pwm.md) | No serial-bus registers, IDs or baud rates |
| Application layer unconfirmed | [Find model resources](../products/index.md) | TTL / RS-485 alone does not establish memory-table compatibility |

## Look up a parameter

1. Confirm the full model suffix, firmware and formal memory-table revision.
2. Identify the address, length, units, allowed range and read/write permissions.
3. Check persistence, torque-enable state, operating mode and conditions for changes. Do not assume a temporary setting survives power loss.
4. Read through the matching application layer first; change one item only under confirmed conditions and record the result.

[Packet format and commands](protocol.md) support protocol diagnosis; [SDK guides](../sdk/index.md) support everyday development. Similar packet framing does not make memory tables interchangeable.
