# Arduino / ESP32 SDK

官方仓库：[ftservo/FTServo_Arduino](https://github.com/ftservo/FTServo_Arduino)。该库可用于 Arduino 和 ESP32，并可通过 Arduino Library Manager 获取。

## 安装方式

=== "Arduino IDE"

    打开库管理器，搜索 `FTServo` 并安装。然后从 **文件 → 示例 → FTServo** 打开与目标系列匹配的示例。

=== "完整 Wiki 仓库"

    将 `sdk/FTServo_Arduino` 作为本地库使用，或在 PlatformIO 中引用该目录。

## 半双工串口

总线通常是半双工通信。具体调试板或收发电路负责收发方向切换；MCU 的 UART 电平和接线必须与 TTL/RS485 物理层匹配。不要把 MCU 引脚直接接到不兼容电压或 RS485 A/B 线上。

## 示例选择

- SCS 系列使用 `SCSCL` 示例。
- STS 与 SMS 系列使用 `SMS_STS` 示例。
- HLS 系列使用 `HLSCL` 示例。
- 将示例中的串口对象、ID、波特率及目标值改成实际配置。

ESP32 通常有多个硬件串口，建议把 USB 日志和舵机总线分开。运行前先验证只读 Ping，再做小范围运动；不要从另一型号示例复制位置范围或寄存器地址。

