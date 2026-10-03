# SM-8524-C002 · Software integration

[Overview and files](main.md) · [Mechanical integration](mechanical.md)

This exact model uses **Modbus-RTU over RS-485**, according to its supplied model documentation.

<!-- official-control:start -->
## Model-specific control specifications

[Official source](https://www.feetechrc.com/24v-85kgcm-modbus-rtu舵机) · 2026-10-02

| Parameter | Manufacturer specification |
| --- | --- |
| Command signal | Digital Packet |
| Protocol Type | Modbus-RTU |
| ID | 0-253 |
| Communication Speed | 38400bps ~ 1Mbps |
| Running degree | 360° (when 0~ 4095) |
| Feedback | Load（负载）, Position（位 置）,Speed（工作速度）, Input Voltage（输入电压），Current（工作 电流）,Temperature（工作温度） |

Consult the exact firmware memory table for register writes; the specification table does not replace it.
<!-- official-control:end -->

## Select the matching protocol

Use a Modbus-RTU controller and the register table for this exact model and firmware. The SMS_STS application layer, packet layout, addresses, units and control modes must not be used for this model. Read the [Modbus-RTU protocol guide](../../../reference/protocol/modbus.md).

## Read first, then move

1. Verify the supply, shared ground, connector pinout, RS-485 wiring and mechanical clearance with this model's documents.
2. Connect one unloaded servo, keep torque disabled, and confirm its address and baud rate using the approved discovery procedure.
3. Read only documented registers with a matching Modbus-RTU client. Record the firmware and register-table revision.
4. Confirm units, limits and operating modes before writing any control registers. Enable torque only when it is safe to move.

## Missing model information

Request the exact register table, connector drawing and model-tested example through the [resource list](main.md#resources). No hardware test was performed during this documentation import.
