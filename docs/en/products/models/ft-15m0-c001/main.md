# FT-15M0-C001

![FT-15M0-C001](images/main.webp){ .ft-model-main-image }

Use this page to compare the main specifications of `FT-15M0-C001` and plan power, control and mechanical integration.

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
| Input voltage | **6 V** |
| Stall torque | **15 kg·cm@6V** |
| Control interface | `PWM` |
| Product family | `FT` |
| Product model | `FT15M-C001` |
| Document revision | `A/0` |

!!! info "Selection note"
    Stall torque is a short-duration limit for product comparison, not a continuous operating point. Allow suitable margin for duty cycle, temperature, impact, acceleration and mechanism friction.

## Selection and use

1. Confirm the product label and document revision match this page.
2. Confirm the permitted supply range from this model’s formal documentation before selecting a regulated supply; a single catalog voltage does not establish a range. Size current for simultaneous operation.
3. Match the controller, wiring and PWM signal settings to the exact model documentation.
4. Check mounting space, output shaft, travel and mechanical clearance before enabling torque.

For control signals and first tests, continue with this model’s [software integration](software.md) page. PWM models do not use serial-bus SDKs.

<!-- official-specs:start -->
## Official model specifications

[FEETECH official product page](https://www.feetechrc.com/15kgcm-digital-180-degree-dual-axis-robot-steering-gear-ft15m) · Checked 2026-10-02. The complete model on the page is FT-15M0-C001.

| Parameter | Manufacturer specification |
| --- | --- |
| Model | FT-15M0-C001 |
| Storage Temperature Range | -20℃～80℃ |
| Operating Temperature Range | -10℃～60℃ |
| Size | A：40.2mm B：20.2mm C：40.1mm |
| Weight | 61.8± 1g |
| Gear type | 铜 Copper |
| Limit angle | NO limit |
| Bearing | 滚珠轴承 Ball bearings |
| Horn gear spline | 25T/5.9mm |
| Case | Aluminum |
| Connector wire | 30±0.5CM |
| Motor | 铁芯电机Core Motor |
| Operating Voltage Range | 4-8.4V |
| No load speed | 0.161sec/60°(62RPM)@7.4V |
| Runnig current(at no load) | 140mA@7.4V |
| Peak stall torque | 19.5kg.cm@7.4V |
| Rated torque | 6.5kg.cm@7.4V |
| Stall current | 2.8A@7.4V |
| Command signal | Pulse width modification |
| Control System Type | Digital comparator |
| Pulse width range | 500→2500 μsec |
| Neutral position | 1500 μsec |
| Operating Travel | 180° (士5° ) (when 500~ 2500 μsec) |
| Dead band width | ≤4 μsec |
| Rotating direction | 逆时针 Counterclockwise(在500→2500 μsec) |

### Additional facts from the attached datasheet

[Official datasheet](https://www.feetechrc.com/Data/feetechrc/upload/file/20260623/6391782445820760809963450.pdf)

| Parameter | Specification | PDF page |
| --- | --- | --- |
| 角度传感器 Angle Sansor | 类型Type / Carbon-Film Potentiometer | 4 |
| 齿轮虚位Back Lash | ≦0.5° | 4 |
| 摇臂虚位 The rocker phantom | 0° | 4 |
| 出力轴螺丝 The rocker screw | M3X6 | 4 |
| 两边角度差 Left&Right Travelling Angledeviation | ≤ 5° | 4 |
| 回中差 Centering Deviation | ≦1° | 4 |
| 信号周期 Signal Period | 20ms | 7 |
| 信号高电平电压 Signal high Voltage | 2V-5V | 7 |
| 信号低电平电压 Signal Low Voltage | 0.0V-0.45V | 7 |

![FT-15M0-C001 mechanical drawing](images/drawing.webp){ .ft-model-drawing }

[Open full-size drawing](images/drawing.webp)
<!-- official-specs:end -->

<!-- product-resources:start -->
## Resources and document status {#resources}

Local attachments are included in the model package; PDF specifications link to the manufacturer and are not bundled offline. Missing resources are not yet supplied; family guides do not verify model-specific settings.

| Resource | Status / file | Revision |
| --- | --- | --- |
| Model datasheet | [View on manufacturer website (online)](https://www.feetechrc.com/Data/feetechrc/upload/file/20260623/6391782445820760809963450.pdf) | A/0 |
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
