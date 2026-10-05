# STM32 HAL

Official repository: [FTServo_stm32HAL](https://github.com/ftservo/FTServo_stm32HAL)

The upstream project provides STM32F103 and STM32F407 references based on CubeMX/HAL. Its defaults use USART2 for the servo at 1 Mbps and USART1 for 115200-bps logs. If CubeMX or UART configuration changes, adapt `ftUart_Send`, `ftUart_Read` and logging in `Core/Src/main.c`.

Regenerate/check HAL for the target MCU, implement send/receive/timeouts and half-duplex direction, use the right TTL/RS485 transceiver, inspect timing with a logic analyzer, and complete Ping before torque or motion writes.

