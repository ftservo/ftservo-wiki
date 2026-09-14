# SDK Overview

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

| Servo series | Python example | Arduino/C++ layer |
| --- | --- | --- |
| SCS / SCSCL | `scscl` | `SCSCL` |
| STS / SMS | `sms_sts` | `SMS_STS` |
| HLS | `hls` | `HLSCL` |

!!! warning
    Similar APIs do not imply identical memory tables. Begin with the matching series example and verify all addresses, ranges and units against the exact model.

Start in FD, run a read-only Ping with one servo, then a small unloaded move. Add synchronized multi-servo motion, timeouts and mechanical limits only after stable communication. A Rust SDK is planned separately and is intentionally not stubbed here.

