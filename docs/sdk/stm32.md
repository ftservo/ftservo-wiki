# STM32 HAL

官方仓库：[FTServo_stm32HAL](https://github.com/ftservo/FTServo_stm32HAL)

官方示例基于 STM32CubeMX/HAL，包含 STM32F103 与 STM32F407 配置参考。默认示例使用 USART2 控制舵机（1 Mbps），USART1 输出日志（115200 bps）；重新生成或改 UART 后，要同步修改 `Core/Src/main.c` 中的 `ftUart_Send`、`ftUart_Read` 和日志重定向实现。

移植清单：

1. 用当前 CubeMX 版本检查并重新生成对应芯片 HAL 工程。
2. 适配发送、接收、超时和半双工方向控制。
3. 确认 UART 电平，TTL/RS485 使用正确收发器。
4. 用逻辑分析仪核对波特率和收发切换。
5. 先完成 Ping/读状态，再启用扭矩和位置写入。

