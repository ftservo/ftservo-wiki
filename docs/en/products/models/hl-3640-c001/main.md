# HL-3640-C001

![HL-3640-C001](images/main.webp){ .ft-model-main-image }

Use this page to compare the main specifications of `HL-3640-C001` and plan power, control and mechanical integration.

[Back to HL catalog](../../datasheets/hl.md){ .md-button }

## Start your integration

| Your task | Start here | What to check |
| --- | --- | --- |
| Write control software | [Software integration](software.md) | Interface, application layer, read-first bring-up and validation record |
| Design a bracket or joint | [Mechanical integration](mechanical.md) | Drawings, CAD, datum, output shaft and cable clearance |
| Collect engineering files | [Resources and status](#resources) | Available files and outstanding information |

## Key specifications

| Item | Value |
| --- | --- |
| Input voltage | **7.4 V** |
| Stall torque | **40 kg·cm@7.4V** |
| Control interface | `TTL` |
| Product family | `HLS` |
| Product model | `HLS3640M-C001` |
| Document revision | `A/0` |

!!! info "Selection note"
    Stall torque is a short-duration limit for product comparison, not a continuous operating point. Allow suitable margin for duty cycle, temperature, impact, acceleration and mechanism friction.

## Selection and use

1. Confirm the product label and document revision match this page.
2. Confirm the permitted supply range from this model’s formal documentation before selecting a regulated supply; a single catalog voltage does not establish a range. Size current for simultaneous operation.
3. Match the controller, wiring and SDK to the listed interface and product family.
4. Check mounting space, output shaft, travel and mechanical clearance before enabling torque.

For communication commands and software integration, continue with the [SDK guide](../../../sdk/index.md) and the protocol documentation for this product family.

<!-- official-specs:start -->
## Official model specifications

[FEETECH official product page](https://www.feetechrc.com/556986) · Checked 2026-10-02. The complete model on the page is HL-3640-C001.

| Parameter | Manufacturer specification |
| --- | --- |
| Model | HL-3640-C001 |
| Storage Temperature Range | -30℃～80℃ |
| Operating Temperature Range | -10℃～60℃ |
| Temperature Range | 25℃ ±5℃ |
| Humidity Range | 65%±10% |
| Size | A：40mm B：20mm C：43.05mm |
| Weight | 89± 1g |
| Gear type | 钢 Steel |
| Limit angle | No limit |
| Bearing | 滚珠轴承 Ball bearings |
| Horn gear spline | 25T/OD5.9mm |
| Gear Ratio | 1/378 |
| The rocker phantom | 0° |
| Case | Aluminium |
| Connector wire | 15CM |
| Motor | Coreless Motor |
| Rated Input Voltage | 5V-8.4V |
| No load speed | 0.22sec/60°(45RPM)@7.4V |
| Runnig current(at no load) | 150mA@7.4V |
| Peak stall torque | 40kg.cm@7.4V |
| Stall current | 3.3A@7.4V |
| Rated Load | 10kg. cm@7.4V |
| Rated current | 850mA@7.4V |
| KT | 12.0kg. cm/A |
| Terminal resistance | 1.02 Ω |
| Operating Modes | 模式0：角度伺服模式 （默认此模式，0-360度[敏感词]位置可控） Mode 0: Angle servo mode (default mode, absolute position controllable from 0-360 degrees) |
| Multi-Loop Mode | [敏感词]精度下可以正负7圈[敏感词]位置控制，但掉电圈数不保存（扩大分辨率，圈数可翻倍） control of positive and negative 7 turns at the highest accuracy, but the umber of power failure turns is not saved (the resolution can be expanded, and the number of turns can be doubled) |
| Constant force output | 设定输出扭矩值，舵机可保持该扭矩(44号地址输入相对应的目标扭矩值，舵机可保持该扭矩) Set the output torque value, the servo can maintain this torque (input the target torque value corresponding to address 44, the servo can maintain this torque) |
| Command signal | Digital Packet |
| Protocol Type | Half Duplex Asynchronous Serial Communication |
| ID | 0-253 |
| Communication Speed | 38400bps ~ 1 Mbps |
| Control Algorithm | PID |
| Neutral Position | 180°（2048） |
| Running degree | 360° (when 0~4096) |
| Resolution [deg/pulse] | 0.088°(360°/4096) |
| Rotating Direction | Clockwise(0→4096） |
| Feedback | Load（负载）, Position（位置）,Speed（工作速度）, Input Voltage（输入电压），Current（工作电流）,Temperature（工作温度） |

### Additional facts from the attached datasheet

[Official datasheet](https://www.feetechrc.com/Data/feetechrc/upload/file/20260623/6391782968644585868623266.pdf)

| Parameter | Specification | PDF page |
| --- | --- | --- |
| 角度传感器 Angle Sansor | 类型Type / 12Bits Magnetic Coding | 4 |
| 齿轮虚位Back Lash | ≦0.5° | 4 |
| 摇臂虚位 The rocker phantom | 0° | 4 |
| 出力轴螺丝 The rocker screw | M3X6 | 4 |
| 信号高电平电压 Signal high Voltage | 2V-5V | 8 |
| 信号低电平电压 Signal Low Voltage | 0.0V-0.45V | 8 |

![HL-3640-C001 mechanical drawing](images/drawing.webp){ .ft-model-drawing }

[Open full-size drawing](images/drawing.webp)
<!-- official-specs:end -->

<!-- product-resources:start -->
## Resources and document status {#resources}

Local attachments are included in the model package; PDF specifications link to the manufacturer and are not bundled offline. Missing resources are not yet supplied; family guides do not verify model-specific settings.

| Resource | Status / file | Revision |
| --- | --- | --- |
| Model datasheet | [View on manufacturer website (online)](https://www.feetechrc.com/Data/feetechrc/upload/file/20260623/6391782968644585868623266.pdf) | A/0 |
| Connector and pinout | Not supplied | — |
| Model memory table / firmware notes | Not supplied | — |
| 2D mounting drawing | [drawing.webp](images/drawing.webp) | — |
| STEP / 3D model | Not supplied | — |
| Model-tested example | Not supplied | — |
| Raw test data | Not supplied | — |
| Test record and conditions | Not supplied | — |

[Package manifest](manifest.json) · [Request missing resources](#support)

For an offline ZIP with both languages and available attachments, see [product-package export](../../../downloads.md#product-packages).
<!-- product-resources:end -->

## Request resources or report an issue {#support}

Use your existing FEETECH technical-support contact and include the full label/model suffix, firmware version (if known), and the document revision you are using.

- Software: controller/OS, SDK version or commit, adapter/interface, supply voltage, confirmed ID/baud rate (bus models only), minimal reproduction and logs.
- Mechanics: drawing/CAD revision, marked dimensions, required travel, horn/bracket, load and lever arm, duty cycle, and the point of interference.
- Missing files: name the exact item in the resource table (for example, this model's STEP and a dimensioned mounting drawing).

This package currently provides a specification summary and integration checklists. File availability does not imply that your firmware, load case or assembly has been validated.
