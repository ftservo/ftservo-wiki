# FT-90MR-C001

![FT-90MR-C001](images/main.webp){ .ft-model-main-image }

Use this page to compare the main specifications of `FT-90MR-C001` and plan power, control and mechanical integration.

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
| Stall torque | **2.3 kg·cm@6V** |
| Control interface | `PWM` |
| Product family | `FT` |
| Product model | `FT90MR-C001` |
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

[FEETECH official product page](https://www.feetechrc.com/18kg-digital-steering-gear-ft90mr) · Checked 2026-10-02. The complete model on the page is FT-90MR-C001.

!!! warning "Claims requiring confirmation"
    voltageMax: website table gives 6.0, attached PDF gives 8.4; a new filter value is withheld pending revision confirmation.

| Parameter | Manufacturer specification |
| --- | --- |
| Model | FT-90MR-C001 |
| Storage Temperature Range | -30℃～80℃ |
| Operating Temperature Range | -10℃～70℃ |
| Size | A：23.2mm B：12.1mm C:25.5mm |
| Weight | 12.5g |
| Gear type | Metal Gear |
| Limit angle | NO limit |
| Bearing | NO Ball bearings |
| Horn gear spline | 20T |
| Horn type | Plastic,POM |
| Case | ABS |
| Connector wire | 250mm |
| Motor | coremotor |
| Operating Voltage Range | 3-6V |
| Idle current (at stopped) . | 5mA-6mA |
| No load speed | 100RPM @6V |
| Runnig current(at no load) | 150 mA@6V |
| Peak stall torque | 2.15kg.cm@6V |
| Rated torque | 0.71kg.cm@6V |
| Stall current | 1000mA@6V |
| Command si gnal | Pulse width modification |
| Amplifier type | Digitalcompara tor |
| Pulse width range | 900~2100usec |
| Stop position | 1500 sec |
| Running degree | 360° Continuous Rotation |
| Dead band width | +/-25 μsec |
| Rotating direction | CCW(when 1500~ 2500 μsec) |

### Additional facts from the attached datasheet

[Official datasheet](https://www.feetechrc.com/Data/feetechrc/upload/file/20260623/6391782439748873876545492.pdf)

| Parameter | Specification | PDF page |
| --- | --- | --- |
| 角度传感器 Angle Sansor | 类型Type / NO | 4 |
| 齿轮虚位Back Lash | ≦2.0° | 4 |
| 摇臂虚位 The rocker phantom | 0° | 4 |
| 出力轴螺丝 The rocker screw | M2.0X4 | 4 |
| 信号周期 Signal Period | 20ms | 7 |
| 信号高电平电压 Signal high Voltage | 2V-5V | 7 |
| 信号低电平电压 Signal Low Voltage | 0.0V-0.45V | 7 |

![FT-90MR-C001 mechanical drawing](images/drawing.webp){ .ft-model-drawing }

[Open full-size drawing](images/drawing.webp)
<!-- official-specs:end -->

<!-- product-resources:start -->
## Resources and document status {#resources}

Local attachments are included in the model package; PDF specifications link to the manufacturer and are not bundled offline. Missing resources are not yet supplied; family guides do not verify model-specific settings.

| Resource | Status / file | Revision |
| --- | --- | --- |
| Model datasheet | [View on manufacturer website (online)](https://www.feetechrc.com/Data/feetechrc/upload/file/20260623/6391782439748873876545492.pdf) | A/0 |
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
