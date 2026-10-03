# FT-325B-C001

![FT-325B-C001](images/main.webp){ .ft-model-main-image }

Specifications transcribed from the supplied documentation for this exact model and suffix.

[Back to catalog](../../datasheets/pwm.md){ .md-button }

## Start your integration

| Your task | Start here | What to check |
| --- | --- | --- |
| Write control software | [Software integration](software.md) | Interface, application layer, read-first bring-up and validation record |
| Design a bracket or joint | [Mechanical integration](mechanical.md) | Drawings, CAD, datum, output shaft and cable clearance |
| Collect engineering files | [Resources and status](#resources) | Available files and outstanding information |

## Key specifications

| Parameter | Specification |
| --- | --- |
| --- | --- |
| Input voltage | 16–25 V |
| Stall torque | 325 kg·cm |
| No-load speed | 0.29 s/60°（34 RPM） |
| Travel / rotation | 180°（500~2500 μsec） |
| Control interface | PWM |
| Family | FT |
| Dimensions | 64 × 32.8 × 90 mm |
| Weight | 490 ± 5 g |
| Gears | Steel gears |
| Motor | Brushless motor |
| Document revision | A/0（Official page captured 2026-10-02） |

!!! warning "Source inconsistencies"
    The source table states 325 kg·cm@12V, but the supply range is 16–25 V. Confirm the torque test voltage with FEETECH.

- [FEETECH model source](https://www.feetech.cn/511209)

!!! info "Selection note"
    Stall torque is a short-duration limit, not continuous operating torque. Confirm power, shared ground, interface and mechanical clearance before enabling torque.

<!-- official-specs:start -->
## Official model specifications

[FEETECH official product page](https://www.feetechrc.com/511209) · Checked 2026-10-02. The complete model on the page is FT-325B-C001.

!!! warning "Claims requiring confirmation"
    Test voltage 12 V for stall torque is outside the listed operating range 16V-25V; source claim retained, conditions unconfirmed.
    Test voltage 12 V for no-load speed is outside the listed operating range 16V-25V; source claim retained, conditions unconfirmed.

| Parameter | Manufacturer specification |
| --- | --- |
| Model | FT-325B-C001 |
| Storage Temperature Range | -40℃～80℃ |
| Operating Temperature Range | -20℃～60℃ |
| Size | A: 64mm B: 32.8mm C: 90mm |
| Weight | 490g±5g |
| Gear type | 钢 Steel |
| Limit angle | NO limit |
| Bearing | 滚珠轴承 Ball bearings |
| Horn gear spline | 25T |
| Gear Ratio | 1/290 |
| Case | Aluminum |
| Connector wire | 43±1CM |
| Motor | Brushless Motor |
| Operating Voltage Range | 16V-25V |
| Idle current (atstopped) | 20mA@12V |
| No load speed | 0.29sec/60°(34RPM)@12V |
| Runnig current(at no load) | 260mA@12V |
| Peak stall torque | 325kg.cm@12 V |
| Rated torque | 108kg.cm@12V |
| Stall current | 10.2A@24V |
| Command si gnal | Pulse width modulation |
| Control System Type | Digital comparator |
| Pulse width range | 500~2500 μ sec |
| Stop position | 1500 μ sec |
| Running degree | 180±2°(at 500→2500μsec) |
| Dead band width | ≤4 μ sec |
| Rotating direction | 顺时针 Clockwise(在1500→2000μsec) |

### Additional facts from the attached datasheet

[Official datasheet](https://www.feetechrc.com/Data/feetechrc/upload/file/20260623/6391782035957570155043766.pdf)

| Parameter | Specification | PDF page |
| --- | --- | --- |
| 角度传感器 Angle Sensor | 类型Type / 12 Bite Magnetic Encoded | 4 |
| 齿轮虚位Back Lash | ≦0.5° | 4 |
| 出力轴螺丝 The rocker screw | M4X8 | 4 |
| 两边角度差 Left&Right Travelling Angledeviation | ≤ 2° | 4 |
| 回中差 Centering Deviation | ≦1° | 4 |
| 信号周期 Signal Period | 20ms | 7 |
| 信号高电平电压 Signal high Voltage | 2V-5V | 7 |
| 信号低电平电压 Signal Low Voltage | 0.0V-0.45V | 7 |

![FT-325B-C001 mechanical drawing](images/drawing.webp){ .ft-model-drawing }

[Open full-size drawing](images/drawing.webp)
<!-- official-specs:end -->

<!-- product-resources:start -->
## Resources and document status {#resources}

Local attachments are included in the model package; PDF specifications link to the manufacturer and are not bundled offline. Missing resources are not yet supplied; family guides do not verify model-specific settings.

| Resource | Status / file | Revision |
| --- | --- | --- |
| Model datasheet | [View on manufacturer website (online)](https://www.feetechrc.com/Data/feetechrc/upload/file/20260623/6391782035957570155043766.pdf) | A/0 |
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
