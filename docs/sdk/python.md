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

以下命令从 **`FTServo_Python` 源码根目录**运行。仅安装 PyPI 包不会建立这个源码示例目录；需要这些示例时，请使用上面的完整仓库方式获取源码。

先按[型号与应用层](index.md#application-layer)选择目录，打开对应 `ping.py`，将端口、波特率和目标 ID 改为已确认的配置。示例自带数值只是示例设置，不是所有舵机的出厂默认值。

=== "SCS / SCSCL"

    ```bash
    cd scscl
    python ping.py
    ```

=== "STS / SMS"

    ```bash
    cd sms_sts
    python ping.py
    ```

=== "HLS"

    ```bash
    cd hls
    python ping.py
    ```

切换系列前先返回源码根目录。PWM 不使用这些总线示例；应用层未确认的型号先补齐资料。

常见端口：Windows 为 `COM3` 等，Linux 常为 `/dev/ttyUSB0` 或 `/dev/ttyACM0`，macOS 常为 `/dev/cu.usbserial-*`。Linux 若出现权限错误，将当前用户加入系统对应串口组后重新登录；不要长期用 root 规避权限。

## 判断是否成功

- 打开端口或设置波特率成功，只说明主机串口配置完成，还不能证明舵机已响应。
- Ping 必须收到目标 ID 的成功响应，并检查通信返回值和设备错误；保留控制台输出。
- 核对响应与实物、配置一致后，再按对应内存表读取状态。Ping 成功不代表机械安装和运动参数已验证。

没有响应时进入[通信排查](../troubleshooting.md#not-found)。只有稳定读取并完成供电、接线和机械余量确认后，才进入[第一次运动](../getting-started/first-motion.md)。

## 开发建议

- 把端口、波特率、ID、软限位放入配置文件，不硬编码到业务逻辑。
- 所有打开端口的路径都要确保异常时关闭端口并停止运动。
- 批量控制优先使用 SDK 支持的同步写能力，避免逐台命令造成明显时间差。
- 单元测试可模拟转换和范围检查；真实通信与运动必须在指定型号硬件上验证。
