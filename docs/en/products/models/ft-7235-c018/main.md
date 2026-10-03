# FT-7235-C018

![FT-7235-C018](images/main.webp){ .ft-model-main-image }

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
| Input voltage | 4–9 V |
| Stall torque | 34.2 kg·cm@8.4V |
| No-load speed | 0.098 s/60°（102 RPM）@8.4V |
| Travel / rotation | 180°（500~2500 μsec） |
| Control interface | PWM |
| Family | FT |
| Dimensions | 40.7 × 36.5 × 20.16 mm |
| Weight | 64.5 ± 1 g |
| Gears | Steel gears（aluminum middle case） |
| Motor | Coreless motor |
| Document revision | A/0（Official page captured 2026-10-02） |

- [FEETECH model source](https://www.feetech.cn/530069)

!!! info "Selection note"
    Stall torque is a short-duration limit, not continuous operating torque. Confirm power, shared ground, interface and mechanical clearance before enabling torque.

<!-- official-specs:start -->
## Official model specifications

[FEETECH official product page](https://www.feetechrc.com/530069) · Checked 2026-10-02. The complete model on the page is FT-7235-C018.

| Parameter | Manufacturer specification |
| --- | --- |
| Model | FT-7235-C018 |
| Storage Temperature Range | -20℃～80℃ |
| Operating Temperature Range | -10℃～60℃ |
| Size | A：40.7mm B：36.5mm C: 20.16mm |
| Weight | 64.5± 1g |
| Gear type | 钢 Steel |
| Limit angle | NO limit |
| Bearing | 滚珠轴承 Ball bearings |
| Horn gear spline | 25T/5.9mm |
| Gear Ratio | 1/275 |
| Case | Alumi num |
| Connector wire | 30±0.5CM |
| Motor | Coreless Motor |
| Operating Voltage Range | 4-9V |
| Idle current (atstopped) | 10mA@8.4V |
| No load speed | 0.098sec/60°(102RPM)@8.4V |
| Runnig current(at no load) | 340mA@8.4V |
| Peak stall torque | 34.2kg.cm@8.4V |
| Rated torque | 11.4kg.cm@8.4V |
| Stall current | 3.6A@8.4V |
| Command si gnal | Pulse width modification |
| Control System Type | Digital comparator |
| Pulse width range | 500~2500 μ sec |
| Stop position | 1500 μ sec |
| Running degree | 180°± 5°(at 500→2500μsec) |
| Dead band width | ≤4 μ sec |
| Rotating direction | 逆时针 Counterclockwi se (在1500→2500 μ sec) |
| Electronic Protection | 堵转8秒/Stall 8sec |

![FT-7235-C018 mechanical drawing](images/drawing.webp){ .ft-model-drawing }

[Open full-size drawing](images/drawing.webp)
<!-- official-specs:end -->

<!-- product-resources:start -->
## Resources and document status {#resources}

Local attachments are included in the model package; PDF specifications link to the manufacturer and are not bundled offline. Missing resources are not yet supplied; family guides do not verify model-specific settings.

| Resource | Status / file | Revision |
| --- | --- | --- |
| Model datasheet | Not supplied | — |
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
