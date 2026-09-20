# 飞特 Wiki 维护教程

> 本文件供飞特员工维护仓库，不参与 Wiki 网站构建。

型号资料整理、双语接入、附件清单与 ZIP 导出的完整流程见 [WIKI更新维护教程](WIKI更新维护教程.md)。可复制的文件夹模板见 [产品型号资料包模板](产品型号资料包模板/README.md)。

## 本地环境

```bash
git clone --recurse-submodules https://github.com/ftservo/ftservo-wiki.git
cd ftservo-wiki
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
python -m pip install -r requirements.txt
mkdocs serve
```

局域网预览可运行 `mkdocs serve -a 0.0.0.0:8000`，其他设备通过开发电脑的局域网 IP 和端口 `8000` 访问。

## 目录规则

- `docs/<路径>.md`：简体中文页面。
- `docs/en/<同路径>.md`：英文页面。
- `mkdocs.yml`：中英文导航与站点配置。
- `docs/assets/`：经过授权并适合网页发布的图片和小型附件。
- `sdk/`：官方 SDK 子模块。
- `docs/products/models/<型号-id>/`：型号概览、程序开发、结构设计和附件清单；英文同路径位于 `docs/en/`。
- `ENGINEERING_RESOURCES.md`：工程资料验收要求；模板统一维护在 `产品型号资料包模板/`。

新增公开页面时必须同时添加中英文文件和入口。型号页通过系列目录和选型器进入，子页通过 `main.md` 进入，不逐条加入全站导航。文件名使用小写英文与连字符。

## 产品页发布清单

1. 使用完整销售型号。
2. 参数来自已批准的产品资料，并记录资料版本和日期。
3. 接口、电压、针序、尺寸、重量、速度、扭矩和行程逐项复核。
4. 输入电压只按本完整型号的批准资料填写；不能仅因标注 12 V 或 24 V 就统一扩展为其他电压范围。
5. 协议链接指向正确的产品系列与内存表版本。
6. 图片、曲线和模型已获得发布授权，不包含客户资料。
7. 中英文数字、单位和安全提示保持一致。
8. 由产品、电气或机械工程师与 Wiki 维护者复审。

## 特性曲线

保存原始 JSON/CSV、测试方法和设备信息；工装 JSON 可接入交互曲线，静态图可作补充。注明型号/后缀、固件、供电、环境、测量次数、负载方式、单位与持续时间，缺项写未记录。堵转扭矩不能表述为持续工作扭矩。路径及清单规则见新版维护教程。

## 3D 模型

优先发布 STEP，并提供 2D 安装图。注明单位、坐标轴、机械零位、安装孔、输出轴或舵盘、线缆出口、版本和许可，由机械工程师对照实物校验关键尺寸。

## 提交与验证

```bash
python scripts/product_package.py validate
mkdocs build --strict
git diff --check
git switch -c docs/model-name
git add docs mkdocs.yml ENGINEERING_RESOURCES.md WIKI_MAINTENANCE.md
git commit -m "docs: update product documentation"
git push -u origin HEAD
```

在 GitHub 创建 Pull Request。合并到 `main` 后，由 GitHub Actions 执行严格构建并发布网站。

## 更新 SDK 子模块

```bash
git submodule update --remote sdk/FTServo_Python
git add sdk/FTServo_Python
git commit -m "chore: update Python SDK"
```

其他 SDK 替换对应路径。更新前审阅上游变更，更新后重新验证相关教程。
