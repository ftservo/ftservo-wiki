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

## 型号资料包与离线导出 {#product-packages}

每个[型号页面](products/datasheets/index.md)均提供“程序开发”“结构设计”和资料状态表。下载链接只指向已收录文件；“待补充”意味着尚未提供，并非文件丢失。可将完整型号及所需项目交给已有的飞特技术支持联系人。

已克隆本仓库时，可在仓库根目录导出一个型号的中英文说明和已收录附件（需 Python，无第三方依赖）：

```bash
python scripts/product_package.py package --model hl-3950-c001 --output exports/hl-3950-c001.zip
```

替换为所需的小写型号 ID；输出文件必须尚不存在。ZIP 包含资源清单和 SHA-256 校验文件，缺失资料不会生成空附件。共享教程及交互曲线请在 Wiki 中使用；这个型号包不包含官方 SDK，需要 SDK 时使用上方的完整克隆方式。

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
