# SDK 总览

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

## 选择正确的类和示例

| 舵机系列 | Python 示例目录/类 | Arduino / C++ 应用层 |
| --- | --- | --- |
| SCS / SCSCL | `scscl` | `SCSCL` |
| STS / SMS | `sms_sts` | `SMS_STS` |
| HLS | `hls` | `HLSCL` |

!!! warning "API 相似不代表参数相同"
    不同系列的数据包可能兼容，但内存表存在差异。必须从目标系列示例开始，并用具体型号内存表确认地址、范围和单位。

## 通用联调顺序

1. 先用 FD 确认接口、ID、波特率和运动正常。
2. 从 SDK 的 `ping`/读取示例开始，只连接一只舵机。
3. 修改端口、ID 和波特率，不先改寄存器常量。
4. 能稳定读取后再做小位移写入。
5. 最后加入同步写、多机控制、异常超时和机械限位。

Rust SDK 已列入后续计划，本阶段不提供未经硬件验证的实现。

