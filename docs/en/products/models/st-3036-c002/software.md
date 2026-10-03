# ST-3036-C002 · Software integration

[Overview and files](main.md) · [Mechanical integration](mechanical.md)

Control interface: **TTL**. Confirm the full model suffix against the physical label.

<!-- official-control:start -->
## Model-specific control specifications

[Official source](https://www.feetechrc.com/512721) · 2026-10-02

| Parameter | Manufacturer specification |
| --- | --- |
| Command signal | Digital Packet |
| Protocol Type | Half Duplex Asynchronous Serial Communication |
| ID | 0-253 |
| Communication Speed | 38400bps ~ 1 Mbps |
| Neutral Position | 2048 |
| Running degree | 360°(when 0～4096) |
| Feedback | Load（负载）, Position（位置）,Speed（工作速度）, Input Voltage（输入电压）,Temperature（工作温度） |
| Resolution [deg/pulse] | 0.088°(360°/4096) |

Consult the exact firmware memory table for register writes; the specification table does not replace it.
<!-- official-control:end -->

## Choose the application layer

Family reference: **STS** → Python `sms_sts`; Arduino / C++ `SMS_STS`. Read the [family memory-table guide](../../../reference/parameter/memory-sts.md) and [packet protocol](../../../reference/protocol/index.md). This identifies the family entry point, not confirmed addresses, units or modes for this model and firmware.

| Development environment | Existing guide |
| --- | --- |
| PC / Raspberry Pi / Jetson | [Python](../../../sdk/python.md) |
| Arduino / ESP32 / PlatformIO | [Arduino / ESP32](../../../sdk/arduino.md) |
| Linux C++ / STM32 HAL | [Linux / STM32](../../../sdk/linux-stm32.md) |

These are shared SDK guides; no model-specific hardware-tested example is supplied in this package yet.

## Read first, then move

1. Confirm power, shared ground, connector pinout and the matching TTL or RS-485 interface using [wiring](../../../getting-started/wiring.md) and [adapter](../../../tools/adapters.md) guidance. Pinout drawings for the exact model take precedence over wire colors.
2. Connect one servo with the mechanism unloaded, keep clear of start-up movement, and confirm its current ID and baud rate using the documented discovery procedure. No default ID or baud rate is asserted here.
3. Verify the SDK class and firmware/memory-table revision; then run a unicast Ping and supported read-only queries. Log responses and timeouts before writing anything.
4. Establish torque-enable state, mode, units and software/mechanical limits. Use only a validated small motion with a matching example; never copy a position/register limit from another family.
5. Add unique IDs, bounded retries, communication-loss handling and multi-servo operation after single-servo validation.

See [first motion](../../../getting-started/first-motion.md) for the shared workflow and [troubleshooting](../../../troubleshooting.md) for diagnosis.

## Required model-specific information

Check the [resource table](main.md#resources). Pinout, control limits, protection thresholds, firmware behavior and model-tested code remain unconfirmed unless supplied and explicitly identified there. A missing value is not zero or a default.

## Record a reproducible integration

| Record | Your value |
| --- | --- |
| Full physical label / firmware | Record before testing |
| Controller, OS and toolchain | Record exact versions |
| SDK commit / example path (bus) or PWM configuration | Record exact revision and parameters |
| Supply / adapter / wiring revision | Record measured conditions |
| Initial state, command and expected result | Start with the smallest validated operation |
| Actual response, timeouts and stop behavior | Save logs; include test date and load condition |

Share this record with [technical support](main.md#support) when requesting a model-specific example.
