# SDK Overview

Confirm the interface and application layer on the [model page](../products/index.md), then choose a platform. These SDKs target serial-bus servos; start with [PWM Getting Started](../getting-started/pwm.md) for PWM control. TTL / RS485 alone does not identify a register table.

| Platform | Tutorial | First verification goal |
| --- | --- | --- |
| PC / Raspberry Pi / Jetson with Python | [Python SDK](python.md) | Open the port and receive the intended device's Ping response |
| Arduino / ESP32 | [Arduino / ESP32 SDK](arduino.md) | Confirm communication using a matching read-only example |
| Linux C++ / STM32 HAL | [Linux / STM32 SDK](linux-stm32.md) | Confirm serial direction control and device response |
| Hardware verification before coding | [FD Tool](../tools/fd.md) | Confirm interface, ID, baud rate and read results |

## Get the official SDKs

Official SDKs are included as Git submodules under `sdk/`:

```bash
git clone --recurse-submodules https://github.com/ftservo/ftservo-wiki.git
```

| Platform | Local path | Official repository | Best for |
| --- | --- | --- | --- |
| Python | `sdk/FTServo_Python` | [FTServo_Python](https://github.com/ftservo/FTServo_Python) | PC, Raspberry Pi, Jetson, prototypes |
| Arduino / ESP32 | `sdk/FTServo_Arduino` | [FTServo_Arduino](https://github.com/ftservo/FTServo_Arduino) | Arduino IDE, PlatformIO, ESP32 |
| Linux C++ | `sdk/FTServo_Linux` | [FTServo_Linux](https://github.com/ftservo/FTServo_Linux) | Native Linux applications |
| STM32 HAL | `sdk/FTServo_stm32HAL` | [FTServo_stm32HAL](https://github.com/ftservo/FTServo_stm32HAL) | STM32CubeMX / HAL firmware |

## Choose the matching application layer {#application-layer}

| Servo series | Python example | Arduino/C++ layer |
| --- | --- | --- |
| SCS / SCSCL | `scscl` | `SCSCL` |
| STS / SMS | `sms_sts` | `SMS_STS` |
| HLS | `hls` | `HLSCL` |

!!! warning
    Similar APIs do not imply identical memory tables. Begin with the matching series example and verify all addresses, ranges and units against the exact model.

## Integration sequence

1. Confirm power and wiring through [Bus Getting Started](../getting-started/bus.md), then verify interface, ID, baud rate and reads in FD.
2. Connect one servo and begin with the SDK's Ping / read example.
3. Set the confirmed port, ID and baud rate before changing register constants.
4. After stable reads and clearance checks, follow [First Motion](../getting-started/first-motion.md).
5. Add synchronized multi-servo control, exception handling and mechanical limits.

A Rust SDK is planned separately and is intentionally not stubbed here.

A shared tutorial does not mean every model has been hardware-validated. Record the full model, firmware, SDK version and results. Use [Troubleshooting](../troubleshooting.md) and its copyable support record for failures. Agree on [zero, travel and limits](../mechanical/index.md) with the mechanical engineer before assembly.
