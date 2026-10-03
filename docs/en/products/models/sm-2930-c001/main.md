# SM-2930-C001

![SM-2930-C001](images/main.webp){ .ft-model-main-image }

Use this page to compare the main specifications of `SM-2930-C001` and plan power, control and mechanical integration.

[Back to SM catalog](../../datasheets/sm.md){ .md-button }

## Start your integration

| Your task | Start here | What to check |
| --- | --- | --- |
| Write control software | [Software integration](software.md) | Interface, application layer, read-first bring-up and validation record |
| Design a bracket or joint | [Mechanical integration](mechanical.md) | Drawings, CAD, datum, output shaft and cable clearance |
| Collect engineering files | [Resources and status](#resources) | Available files and outstanding information |

## Key specifications

| Item | Value |
| --- | --- |
| Input voltage | **18–25.2 V** |
| Stall torque | **30 kg·cm@24V** |
| Control interface | `RS-485` |
| Product family | `SMS` |
| Product model | `SM2930BL` |
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

[FEETECH official product page](https://www.feetechrc.com/552537) · Checked 2026-10-02. The complete model on the page is SM-2930-C001.

| Parameter | Manufacturer specification |
| --- | --- |
| Model | SM-2930-C001 |
| Storage Temperature Range | -40℃～80℃ |
| OperatinTemperatureRange | -40℃～60℃ |
| Size | A：40mm B：28mm C：45.8mm |
| Weight | 106± 3g |
| Gear type | 钢 Steel |
| Limit angle | No Limit |
| Bearing type | 滚珠轴承 Ball bearings |
| High torque | 30Kg.cm |
| Wide operating voltage | 16.8V-25.2V 供电 |
| Motor | Brushless Motor |
| High resolution | 12 位编码器（360 度 0.088°） |
| Servo control mode | 转动范围0-360°及多圈任意[敏感词]角度 |
| Command signal | Digital Packet |
| ID | 254个ID地址可选 |
| Baud rate | 38400bps ~ 1 Mbps |
| Continuous current | 0.8A |
| Rated Torgue | 10kg.cm |
| Rated Current | 600mA |
| No Load Speed | 0.081sec/60°(124RPM)@24V |
| Quiescent Current | 24mA@24V |
| No-load current | ≦120mA@24V |
| Stall current | 1.6A@24V |
| Resolution [deg/pulse] | 0.088°(360°/4096) |
| Stall torque | 30kg.cm@24V |
| Feedback | Load（负载）, Position（位置）,Speed（工作速度）, Input Voltage（输入电压），Current（工作电流）,Temperature（工作温度） |

### Additional facts from the attached datasheet

[Official datasheet](https://www.feetechrc.com/Data/feetechrc/upload/file/20260622/6391773554821206113895207.pdf)

| Parameter | Specification | PDF page |
| --- | --- | --- |
| 角度传感器 Angle Sansor | 类型Type / 12Bits Magnetic Coding | 4 |
| 齿轮虚位Back Lash | ≦0.5° | 4 |
| 出力轴螺丝 The rocker screw | M2.5X8 | 4 |
| 信号高电平电压 Signal high Voltage | +13V | 8 |
| 信号低电平电压 Signal Low Voltage | -8V | 8 |

![SM-2930-C001 mechanical drawing](images/drawing.webp){ .ft-model-drawing }

[Open full-size drawing](images/drawing.webp)
<!-- official-specs:end -->

<!-- product-resources:start -->
## Resources and document status {#resources}

Local attachments are included in the model package; PDF specifications link to the manufacturer and are not bundled offline. Missing resources are not yet supplied; family guides do not verify model-specific settings.

| Resource | Status / file | Revision |
| --- | --- | --- |
| Model datasheet | [View on manufacturer website (online)](https://www.feetechrc.com/Data/feetechrc/upload/file/20260622/6391773554821206113895207.pdf) | A/0 |
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
