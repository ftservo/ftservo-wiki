# FT-3322-C001

![FT-3322-C001](images/main.webp){ .ft-model-main-image }

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
| Input voltage | 4.8–7.4 V |
| Stall torque | 22.9 kg·cm@7.4V |
| No-load speed | 0.093 s/60°（108 RPM）@7.4V |
| Travel / rotation | 180±5°（500→2500 μsec） |
| Control interface | PWM |
| Family | FT |
| Dimensions | 30 × 12 × 35 mm |
| Weight | 32.6 ± 2 g |
| Gears | Metal gears |
| Motor | Coreless motor |
| Document revision | A/0（Official page captured 2026-10-02） |

- [FEETECH model source](https://www.feetech.cn/728213)

!!! info "Selection note"
    Stall torque is a short-duration limit, not continuous operating torque. Confirm power, shared ground, interface and mechanical clearance before enabling torque.

<!-- official-specs:start -->
## Official model specifications

[FEETECH official product page](https://www.feetechrc.com/728213) · Checked 2026-10-02. The complete model on the page is FT-3322-C001.

| Parameter | Manufacturer specification |
| --- | --- |
| Model | FT-3322-C001 |
| Storage Temperature Range | -30℃～80℃ |
| Operating Temperature Range | -20℃～60℃ |
| Size | A: 30mm B: 12mm C: 35mm |
| Weight | 32.6±2g |
| Gear type | Metal Gear |
| Limit angle | No Limit |
| Bearing | 滚珠轴承 Ball bearings |
| Horn gear spline | 25T/4.95mm |
| Case | Aluminium |
| Connector wire | 25±0.5CM |
| Motor | Coreless Motor |
| Operating Voltage Range | 4.8V-7.4V |
| Idle current (at stopped) . | 6mA@7.4V |
| No load speed | 0.093sec/60°(108RPM)@7.4V |
| Runnig current(at no load) | 140mA@7.4V |
| Peak stall torque | 22.9kg.cm@7.4V |
| Rated torque | 7.6kg.cm@7.4V |
| Command signal | Pulse width modification |
| Amplifier type | Digital Comparator |
| Pulse width range | 500→2500 μsec |
| Stop position | 1500 μsec |
| Running degree | 180±5°(at 500→2500μsec) |
| Dead band width | ≤4 μsec |
| Rotating direction | 逆时针 Counterclockwise(在1500→2000 μsec) |

### Additional facts from the attached datasheet

[Official datasheet](https://www.feetechrc.com/Data/feetechrc/upload/file/20260623/6391782196214275119734720.pdf)

| Parameter | Specification | PDF page |
| --- | --- | --- |
| 角度传感器 Angle Sansor | 类型Type / Carbon-Film Potentiometer | 5 |
| 齿轮虚位Back Lash | ≦1.0° | 5 |
| 出力轴螺丝 The rocker screw | M2.3X5 | 5 |
| 两边角度差 Left&Right Travelling Angledeviation | ≤ 5° | 5 |
| 回中差 Centering Deviation | ≦2° | 5 |
| 信号周期 Signal Period | 20ms | 8 |
| 信号高电平电压 Signal high Voltage | 2V-5V | 8 |
| 信号低电平电压 Signal Low Voltage | 0.0V-0.45V | 8 |

![FT-3322-C001 mechanical drawing](images/drawing.webp){ .ft-model-drawing }

[Open full-size drawing](images/drawing.webp)
<!-- official-specs:end -->

<!-- product-resources:start -->
## Resources and document status {#resources}

Local attachments are included in the model package; PDF specifications link to the manufacturer and are not bundled offline. Missing resources are not yet supplied; family guides do not verify model-specific settings.

| Resource | Status / file | Revision |
| --- | --- | --- |
| Model datasheet | [View on manufacturer website (online)](https://www.feetechrc.com/Data/feetechrc/upload/file/20260623/6391782196214275119734720.pdf) | A/0 |
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
