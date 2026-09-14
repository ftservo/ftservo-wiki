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

