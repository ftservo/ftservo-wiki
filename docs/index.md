<div class="ft-hero" markdown>

# FEETECH 开发者 Wiki

找到你的舵机，接入控制程序，完成机械装配；每一步都能回到对应型号和资料。

<form class="ft-model-search" action="products/" method="get">
  <label for="home-model-query">已经拿到舵机？输入完整型号或标签名称。</label>
  <div><input id="home-model-query" type="search" name="model_query" placeholder="ST3215 / HLS3950M / HD-1910" required><button type="submit">查找型号</button></div>
</form>

[还没选型，先看产品](products/index.md) · [第一次使用，从这里开始](getting-started/index.md)

</div>

## 你现在要做什么？

<div class="grid cards" markdown>

-   :material-magnify: **选择或查找舵机**

    搜索型号、核对后缀，查看接口、参数与资料状态。

    [查找型号](products/index.md)

-   :material-power-plug: **连接第一只舵机**

    区分总线与 PWM，准备接线并完成空载最小验证。

    [选择入门路线](getting-started/index.md)

-   :material-console: **编写控制程序**

    按平台和系列找到教程，先读状态，再验证动作。

    [选择开发平台](sdk/index.md)

-   :material-ruler-square: **设计支架或关节**

    取得安装图与 STEP，核对基准、零位和全行程净空。

    [查看结构设计流程](mechanical/index.md)

-   :material-wrench: **解决当前问题**

    从找不到设备、不动作、抖动或装配干涉开始排查。

    [按现象排查](troubleshooting.md)

-   :material-download: **下载工程资料**

    查看真实附件、资料版本、离线资料包与官方 SDK。

    [查看下载资源](downloads.md)

</div>

## 型号、后缀与资料版本一起确认

系列教程提供接入入口，具体型号参数仍需正式资料支持。型号页会列出针序、安装图、CAD、示例和测试文件的状态；“待补充”就是尚未取得的资料。

[识别系列与接口](products/series.md) · [查协议与参数](reference/index.md) · [让 AI 协助开发](ai-development.md)

## 从首次连接走到真实机构

1. **确认身份**：实物完整型号、接口和对应资料版本。
2. **空载验证**：走匹配的[总线或 PWM 入门路线](getting-started/index.md)。
3. **程序接入**：使用匹配示例，保存实际配置与验证记录。
4. **机构装配**：完成[零位、行程与装配交接](mechanical/index.md)。
5. **记录结果**：异常时按[支持信息清单](troubleshooting.md#support)复现和反馈。

[飞特官网](https://www.feetechrc.com/) · [飞特 GitHub](https://github.com/ftservo) · [原在线文档](http://doc.feetech.cn/#/f?q=2506a8cb7928)
