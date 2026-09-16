# Wiki 维护教程

本页供飞特员工和贡献者维护产品资料。根目录的 [CONTRIBUTING.md](https://github.com/ftservo/ftservo-wiki/blob/main/CONTRIBUTING.md) 提供同一流程的仓库版说明。

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

浏览器访问 `http://127.0.0.1:8000/`。保存 Markdown 后页面会自动刷新。

## 目录规则

- `docs/<路径>.md`：简体中文。
- `docs/en/<同一路径>.md`：英文。
- `mkdocs.yml`：两种语言的导航。
- `docs/assets/`：经过授权的图片、PDF 或小型附件。
- `sdk/`：官方 SDK 子模块，不直接在主仓库中复制源码。

新增页面时必须同时添加中英文文件，并分别加入 `mkdocs.yml` 的 `zh` 和 `en` 导航。文件名使用小写英文和连字符。

## 产品页发布清单

1. 使用完整销售型号，不只写系列俗称。
2. 参数来自已批准的数据表，记录文档版本/日期。
3. 接口、电压、针序、尺寸、重量、速度、扭矩和行程逐项复核。
4. 协议链接必须指向正确系列和内存表版本。
5. 图片已获授权且压缩为合适的 Web 格式；不要上传客户资料。
6. 中英文数字、单位和警告完全一致。
7. 由产品工程师和另一名维护者复审。

## 补充型号资料的实际步骤

1. 在 `FTServos/型号.xlsx` 与对应 PDF 中确认完整销售型号、规格书文件编号和有效版次；不能仅凭文件名配对。先由产品工程师审核映射。
2. 在 `docs/products/models/<型号小写文件名>.md` 建中文产品页，并在 `docs/en/products/models/` 建同名英文页。写明来源、版次、额定条件、接口、安装尺寸、适配 SDK 和安全注意事项；任何数值逐项引用该型号 PDF。
3. 将两页加入 `mkdocs.yml` 中英文导航，从[规格书目录](products/datasheets/index.md)链接到产品页。建立结构图、曲线与代码示例的互相链接。
4. 对特性曲线，先保存原始 CSV、测试方法和测试设备信息，再导出可读的 SVG/PNG。图上注明供电电压、环境温度、测量次数、负载方式、单位和连续运行条件；区分实测点、拟合线与额定边界。不要把堵转扭矩当连续工作扭矩。
5. 对 3D 模型，优先发布 STEP 与 PDF 安装图；注明单位、坐标轴、零位、安装孔、出力轴/舵盘、线缆出口、版本和许可。由机械工程师与实物及规格书尺寸交叉校验。
6. 提交前检查中英文数值和警示一致，运行 `mkdocs build --strict`，经产品、电气或机械工程师及 Wiki 维护者复审。

完整的资料类型、字段和验收方法可在[工程资源页](resources/index.md)查看。

## 提交与发布

```bash
git switch -c docs/model-name
git add docs mkdocs.yml
git commit -m "docs: add MODEL documentation"
git push -u origin HEAD
```

在 GitHub 创建 Pull Request。合并到 `main` 后，GitHub Actions 自动执行严格构建并发布 Pages；本项目不包含国内服务器部署。仓库管理员需要在 **Settings → Pages → Source** 中选择 **GitHub Actions**。

提交前执行：

```bash
mkdocs build --strict
git diff --check
```

## 更新 SDK 子模块

```bash
git submodule update --remote sdk/FTServo_Python
git add sdk/FTServo_Python
git commit -m "chore: update Python SDK"
```

其它 SDK 替换对应路径。更新前审阅 SDK 上游变更，更新后重新验证相关教程；不要让子模块指向未经发布或未测试的临时提交。
