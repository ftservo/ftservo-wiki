# SDK 总览

先在[型号页](../products/index.md)确认接口与应用层，再选择开发平台。下列 SDK 面向串行总线舵机；PWM 控制从 [PWM 入门](../getting-started/pwm.md)开始。仅知道 TTL / RS485 接口，不能据此确定寄存器表。

| 我要使用的平台 | 开始教程 | 首个验证目标 |
| --- | --- | --- |
| PC / 树莓派 / Jetson + Python | [Python SDK](python.md) | 打开端口并收到目标设备的 Ping 响应 |
| Arduino / ESP32 | [Arduino / ESP32 SDK](arduino.md) | 用匹配应用层的只读示例确认通信 |
| Linux C++ / STM32 HAL | [Linux / STM32 SDK](linux-stm32.md) | 确认串口收发方向与设备响应 |
| 暂不写程序，先验证硬件 | [FD 调试工具](../tools/fd.md) | 确认接口、ID、波特率及读取结果 |

## 获取官方 SDK

本项目通过 `sdk/` 下的 Git 子模块携带飞特官方 SDK。完整下载命令：

```bash
git clone --recurse-submodules https://github.com/ftservo/ftservo-wiki.git
```

| 平台 | 目录 | 官方仓库 | 适合场景 |
| --- | --- | --- | --- |
| Python | `sdk/FTServo_Python` | [FTServo_Python](https://github.com/ftservo/FTServo_Python) | PC、树莓派、Jetson、快速验证 |
| Arduino / ESP32 | `sdk/FTServo_Arduino` | [FTServo_Arduino](https://github.com/ftservo/FTServo_Arduino) | Arduino IDE、PlatformIO、ESP32 |
| Linux C++ | `sdk/FTServo_Linux` | [FTServo_Linux](https://github.com/ftservo/FTServo_Linux) | Linux 原生 C/C++ 项目 |
| STM32 HAL | `sdk/FTServo_stm32HAL` | [FTServo_stm32HAL](https://github.com/ftservo/FTServo_stm32HAL) | STM32CubeMX / HAL 固件 |

## 选择正确的类和示例 {#application-layer}

| 舵机系列 | Python 示例目录/类 | Arduino / C++ 应用层 |
| --- | --- | --- |
| SCS / SCSCL | `scscl` | `SCSCL` |
| STS / SMS | `sms_sts` | `SMS_STS` |
| HLS | `hls` | `HLSCL` |

!!! warning "API 相似不代表参数相同"
    不同系列的数据包可能兼容，但内存表存在差异。必须从目标系列示例开始，并用具体型号内存表确认地址、范围和单位。

## 通用联调顺序

1. 按[总线入门](../getting-started/bus.md)确认供电和接线，先用 FD 确认接口、ID、波特率和读取正常。
2. 从 SDK 的 `ping`/读取示例开始，只连接一只舵机。
3. 修改端口、ID 和波特率，不先改寄存器常量。
4. 能稳定读取且机构余量已确认后，按[第一次运动](../getting-started/first-motion.md)做小位移写入。
5. 最后加入同步写、多机控制、异常超时和机械限位。

Rust SDK 已列入后续计划，本阶段不提供未经硬件验证的实现。

共享教程不代表每个型号都已经完成实机验证。联调通过后，将完整型号、固件、SDK 版本及结果写入项目记录；失败时按[故障现象](../troubleshooting.md)定位，并附上可复制的支持记录。装配前与结构工程师对齐[零位、行程和限位](../mechanical/index.md)。
