# Python SDK

官方仓库：[ftservo/FTServo_Python](https://github.com/ftservo/FTServo_Python)

## 安装

=== "从完整 Wiki 仓库运行"

    ```bash
    git clone --recurse-submodules https://github.com/ftservo/ftservo-wiki.git
    cd ftservo-wiki/sdk/FTServo_Python
    python -m venv .venv
    # Linux/macOS: source .venv/bin/activate
    # Windows: .venv\Scripts\activate
    python -m pip install pyserial
    ```

=== "从 PyPI 安装"

    ```bash
    python -m pip install ftservo-python-sdk
    ```

## 运行官方示例

按系列进入 `scscl`、`sms_sts` 或 `hls` 目录，再修改示例中的串口、波特率和舵机 ID。

```bash
cd sms_sts
python ping.py
```

常见端口：Windows 为 `COM3` 等，Linux 常为 `/dev/ttyUSB0` 或 `/dev/ttyACM0`，macOS 常为 `/dev/cu.usbserial-*`。Linux 若出现权限错误，将当前用户加入系统对应串口组后重新登录；不要长期用 root 规避权限。

## 开发建议

- 把端口、波特率、ID、软限位放入配置文件，不硬编码到业务逻辑。
- 所有打开端口的路径都要确保异常时关闭端口并停止运动。
- 批量控制优先使用 SDK 支持的同步写能力，避免逐台命令造成明显时间差。
- 单元测试可模拟转换和范围检查；真实通信与运动必须在指定型号硬件上验证。

