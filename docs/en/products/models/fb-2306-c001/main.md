# FB-2306-C001

![FB-2306-C001](images/main.webp){ .ft-model-main-image }

Use this page to compare the main specifications of `FB-2306-C001` and plan power, control and mechanical integration.

[Back to PWM catalog](../../datasheets/pwm.md){ .md-button }

## Start your integration

| Your task | Start here | What to check |
| --- | --- | --- |
| Write control software | [Software integration](software.md) | Interface, application layer, read-first bring-up and validation record |
| Design a bracket or joint | [Mechanical integration](mechanical.md) | Drawings, CAD, datum, output shaft and cable clearance |
| Collect engineering files | [Resources and status](#resources) | Available files and outstanding information |

## Key specifications

| Item | Value |
| --- | --- |
| Input voltage | **9–12.6 V** |
| Stall torque | **6 kg·cm@12V** |
| Control interface | `PWM` |
| Product family | `FB` |
| Product model | `FB2306BL-C001` |
| Document revision | `A/0` |

!!! info "Selection note"
    Stall torque is a short-duration limit for product comparison, not a continuous operating point. Allow suitable margin for duty cycle, temperature, impact, acceleration and mechanism friction.

## Selection and use

1. Confirm the product label and document revision match this page.
2. Confirm the permitted supply range from this model’s formal documentation before selecting a regulated supply; a single catalog voltage does not establish a range. Size current for simultaneous operation.
3. Match the controller, wiring and PWM signal settings to the exact model documentation.
4. Check mounting space, output shaft, travel and mechanical clearance before enabling torque.

For control signals and first tests, continue with this model’s [software integration](software.md) page. PWM models do not use serial-bus SDKs.

<!-- official-motor:start -->
## Motor classification from the official brochure

Brushless coreless motor. [2024 FEETECH official brochure](https://www.feetechrc.com/Data/feetechrc/upload/file/20240706/2024%E9%A3%9E%E7%89%B9%E5%AE%A3%E4%BC%A0%E5%86%8C.pdf), PDF page 18; matched full model `FB-2306-C001`.
<!-- official-motor:end -->

<!-- official-specs:start -->
## Official model specifications

[FEETECH official product page](https://www.feetechrc.com/12v-6kg-digital-brushless-steering-gear-fb2306bl) · Checked 2026-10-02. The complete model on the page is FB-2306-C001.

| Parameter | Manufacturer specification |
| --- | --- |
| Model | FB-2306-C001 |
| Storage Temperature Range | -40℃～80℃ |
| Operating Temperature Range | -40℃～60℃ |
| Size | A：30.2mm B：14.6mm C：31.5mm . |
| Weight | 42.5g± 1g |
| Gear type | 钢 Steel |
| Limit angle | No limit |
| Bearing | 滚珠轴承 Ball bearings |
| Horn gear spline | 25T/4.95mm |
| Horn type | 0° |
| Case | Aluminium |
| Connector wire | 26±1CM |
| Motor | Brushless Motor |
| Operating Voltage Range | 6-14V |
| Idle current (at stopped) . | 35mA@12V |
| No load speed | 0.072sec/60°(140RPM)@12V |
| Runnig current(at no load) | 110mA@12V |
| Peak stall torque | 6kg.cm@12V |
| Rated torque | 2kg.cm@12V |
| Stall current | 1.25A@12V |
| Command si gnal | Pulse width modification |
| Control System Type | Digital comparator |
| Pulse width range | 1000~2000usec |
| Neutral Position | 1500 μsec |
| Running degree | 90° (at 1000→2000μsec) |
| Dead band width | ≤4 μsec |
| Feedback Voltage | 1000us→0.31V 1500us→1.64V 2000us→3.05V |
| Rotating direction | 顺时针 Clockwise(在1000→2000 μsec) |

### Additional facts from the attached datasheet

[Official datasheet](https://www.feetechrc.com/Data/feetechrc/upload/file/20260623/6391781923833114238495577.pdf)

| Parameter | Specification | PDF page |
| --- | --- | --- |
| 角度传感器 Angle Sensor | 类型Type / 12 Bite Magnetic Encoded | 4 |
| 齿轮虚位Back Lash | ≦0.5° | 4 |
| 摇臂虚位 The rocker phantom | 0° | 4 |
| 出力轴螺丝 The rocker screw | No | 4 |
| 两边角度差 Left&Right Travelling Angledeviation | ≤ 1° | 4 |
| 回中差 Centering Deviation | ≦1° | 4 |
| 信号周期 Signal Period | 20ms | 7 |
| 信号高电平电压 Signal high Voltage | 2V-5V | 7 |
| 信号低电平电压 Signal Low Voltage | 0.0V-0.45V | 7 |

![FB-2306-C001 mechanical drawing](images/drawing.webp){ .ft-model-drawing }

[Open full-size drawing](images/drawing.webp)
<!-- official-specs:end -->

<!-- product-resources:start -->
## Resources and document status {#resources}

Local attachments are included in the model package; PDF specifications link to the manufacturer and are not bundled offline. Missing resources are not yet supplied; family guides do not verify model-specific settings.

| Resource | Status / file | Revision |
| --- | --- | --- |
| Model datasheet | [View on manufacturer website (online)](https://www.feetechrc.com/Data/feetechrc/upload/file/20260623/6391781923833114238495577.pdf) | A/0 |
| Connector and pinout | Not supplied | — |
| Model memory table / firmware notes | Not applicable | — |
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
