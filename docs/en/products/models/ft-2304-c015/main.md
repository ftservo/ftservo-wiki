# FT-2304-C015

![FT-2304-C015](images/main.webp){ .ft-model-main-image }

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
| Input voltage | 3.5–8.4 V |
| Stall torque | 3.2 kg·cm@6V |
| No-load speed | 0.08 s/60°@6V |
| Travel / rotation | 120°（800→2200 μsec） |
| Control interface | PWM |
| Family | FT |
| Dimensions | 23.5 × 8 × 23.4 mm |
| Weight | 11 ± 1 g |
| Gears | Metal gears |
| Motor | Coreless motor |
| Document revision | A/0（Official page captured 2026-10-02） |

- [FEETECH model source](https://www.feetech.cn/531935)

!!! info "Selection note"
    Stall torque is a short-duration limit, not continuous operating torque. Confirm power, shared ground, interface and mechanical clearance before enabling torque.

<!-- official-specs:start -->
## Official model specifications

[FEETECH official product page](https://www.feetechrc.com/531935) · Checked 2026-10-02. The complete model on the page is FT-2304-C015.

| Parameter | Manufacturer specification |
| --- | --- |
| Model | FT-2304-C015 |
| Storage Temperature Range | -30℃～80℃ |
| Operating Temperature Range | -20℃～60℃ |
| Size | A：23.5mm B：8mm C: 23.4mm |
| Weight | 11± 1g |
| Gear type | Metal Gear |
| Limit angle | NO limit |
| Bearing | 滚珠轴承 Ball bearings |
| Horn gear spline | 15T/3.9mm |
| Gear Ratio | 1/293 |
| Case | PA+Aluminum |
| Connector wire | 18CM |
| Motor | Coreless Motor |
| Operating Voltage Range | 3.5V-8.4V |
| Idle current (atstopped) | 10MA@6V |
| No load speed | 0.08sec/60°@6V |
| Runnig current(at no load) | 60mA@6V |
| Peak stall torque | 3.2kg.cm@6V |
| Rated torque | 1.0kg.cm@6V |
| Stall current | 1.2A@6V |
| Command si gnal | Pulse width modification |
| Amplifier type | Digital comparator |
| Pulse width range | 800~2200 μ sec |
| Stop position | 1500 μ sec |
| Running degree | 120°(at 800→2200μsec) |
| Dead band width | ≤4 μ sec |
| Rotating direction | 逆时针 Counterclockwi se (在1500→2000 μ sec) |

![FT-2304-C015 mechanical drawing](images/drawing.webp){ .ft-model-drawing }

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
