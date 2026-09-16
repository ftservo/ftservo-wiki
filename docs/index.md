<div class="ft-hero" markdown>

# FEETECH 开发者 Wiki

从舵机选型、供电接线和 FD 调试，到 Python、Arduino、Linux 与 STM32 开发的一站式入口。

[选择舵机](products/index.md){ .md-button .md-button--primary }
[第一次运行](getting-started/index.md){ .md-button }

</div>

!!! warning "先确认具体型号"
    同系列的不同型号也可能使用不同电压、接口、行程或内存表。上电和写寄存器前，请核对产品标签、型号规格页及对应内存表。

<div class="grid cards" markdown>

-   :material-tune-variant: **产品选型**

    按接口、电压、扭矩、速度、尺寸、反馈和应用筛选。

    [打开选型指南](products/index.md)

-   :material-file-document-multiple: **产品规格**

    按 HD、HL、PWM、SC、SM、ST 系列浏览产品卡片和详细参数。

    [浏览产品规格](products/datasheets/index.md)

-   :material-power-plug: **五步快速开始**

    正确供电、连接调试板、搜索设备、低速测试、再接入 SDK。

    [开始连接](getting-started/index.md)

-   :material-console: **软件与 SDK**

    FD 上位机以及 Python、Arduino/ESP32、Linux C++、STM32 HAL SDK。

    [选择开发平台](sdk/index.md)

-   :material-robot-industrial: **让 AI 帮你开发**

    下载包含文档和 SDK 的完整仓库，向 AI 提供具体型号与目标，生成可验证的项目。

    [查看 AI 开发流程](ai-development.md)

</div>

## 推荐路线

<div class="ft-route">
  <a class="ft-route-step" href="products/">
    <span class="ft-route-number">01</span>
    <span class="ft-route-copy"><strong>确认型号与电气规格</strong><small>核对接口、输入电压、扭矩、尺寸和型号规格</small></span>
  </a>
  <a class="ft-route-step" href="getting-started/wiring/">
    <span class="ft-route-number">02</span>
    <span class="ft-route-copy"><strong>搭建安全测试环境</strong><small>单舵机、匹配的调试板、独立电源并可靠共地</small></span>
  </a>
  <a class="ft-route-step" href="getting-started/first-motion/">
    <span class="ft-route-number">03</span>
    <span class="ft-route-copy"><strong>完成第一次运动</strong><small>FD 搜索设备、设置唯一 ID，并进行低速空载测试</small></span>
  </a>
  <a class="ft-route-step" href="sdk/">
    <span class="ft-route-number">04</span>
    <span class="ft-route-copy"><strong>接入匹配的 SDK</strong><small>按系列和控制平台选择示例，先读状态再写入动作</small></span>
  </a>
  <a class="ft-route-step" href="troubleshooting/">
    <span class="ft-route-number">05</span>
    <span class="ft-route-copy"><strong>扩展到真实机构</strong><small>逐步加入机械负载、多舵机、限位和故障保护</small></span>
  </a>
</div>

## 官方入口

- [飞特官网](https://www.feetechrc.com/)
- [飞特 GitHub](https://github.com/ftservo)
- [原在线文档](http://doc.feetech.cn/#/f?q=2506a8cb7928)
- [下载中心](downloads.md)
