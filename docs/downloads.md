# 下载中心

## 完整开发资料包

推荐使用 Git 同时获取 Wiki 和官方 SDK：

```bash
git clone --recurse-submodules https://github.com/ftservo/ftservo-wiki.git
```

已下载但 SDK 目录为空时：

```bash
git submodule update --init --recursive
```

[打开 Wiki GitHub 仓库](https://github.com/ftservo/ftservo-wiki){ .md-button .md-button--primary }

## 舵机产品资料

- [按 HD、HL、PWM、SC、SM、ST 系列浏览产品规格](products/datasheets/index.md)
- [查看原始型号表](https://github.com/ftservo/ftservo-wiki/blob/main/FTServos/%E5%9E%8B%E5%8F%B7.xlsx)

## 官方 SDK

| SDK | 在线仓库 |
| --- | --- |
| Arduino / ESP32 | [FTServo_Arduino](https://github.com/ftservo/FTServo_Arduino) |
| Python | [FTServo_Python](https://github.com/ftservo/FTServo_Python) |
| Linux C++ | [FTServo_Linux](https://github.com/ftservo/FTServo_Linux) |
| STM32 HAL | [FTServo_stm32HAL](https://github.com/ftservo/FTServo_stm32HAL) |

## 软件与技术资料

- [FD 软件与调试板软件下载](https://www.feetechrc.com/service/software.html)
- [用户手册、通信协议和内存表](https://www.feetechrc.com/service.html)
- [现有在线文档](http://doc.feetech.cn/#/f?q=2506a8cb7928)

!!! tip "为什么不用 GitHub 的 Download ZIP？"
    普通 ZIP 通常不包含 Git 子模块中的 SDK 内容。希望把完整项目交给 AI 或离线开发时，请使用上面的 `--recurse-submodules` 命令；或者分别下载四个 SDK。
