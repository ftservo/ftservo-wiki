# Downloads

## Complete development bundle

Clone the Wiki and all official SDKs together:

```bash
git clone --recurse-submodules https://github.com/ftservo/ftservo-wiki.git
```

If an existing checkout has empty SDK directories:

```bash
git submodule update --init --recursive
```

[Open the Wiki repository](https://github.com/ftservo/ftservo-wiki){ .md-button .md-button--primary }

## Servo product resources

- [Browse product specifications by HD, HL, PWM, SC, SM and ST series](products/datasheets/index.md)
- [Open the source model list](https://github.com/ftservo/ftservo-wiki/blob/main/FTServos/%E5%9E%8B%E5%8F%B7.xlsx)

## Official SDKs

| SDK | Official repository |
| --- | --- |
| Arduino / ESP32 | [FTServo_Arduino](https://github.com/ftservo/FTServo_Arduino) |
| Python | [FTServo_Python](https://github.com/ftservo/FTServo_Python) |
| Linux C++ | [FTServo_Linux](https://github.com/ftservo/FTServo_Linux) |
| STM32 HAL | [FTServo_stm32HAL](https://github.com/ftservo/FTServo_stm32HAL) |

- [FD and adapter software](https://www.feetechrc.com/service/software.html)
- [Manuals, protocols and memory tables](https://www.feetechrc.com/service.html)
- [Legacy documentation](http://doc.feetech.cn/#/f?q=2506a8cb7928)

!!! tip "Why not Download ZIP?"
    A regular GitHub ZIP does not normally include Git submodule content. Use `--recurse-submodules` when handing the complete project to an AI tool or working offline, or download each SDK separately.
