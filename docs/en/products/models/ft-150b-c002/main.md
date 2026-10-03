# FT-150B-C002

![FT-150B-C002](images/main.webp){ .ft-model-main-image }

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
| Input voltage | 10–16 V |
| Stall torque | 220 kg·cm@14.8V |
| No-load speed | 0.204 s/60°（49 RPM）@14.8V |
| Travel / rotation | 180°（600~2400 μsec） |
| Control interface | PWM |
| Family | FT |
| Dimensions | 64 × 33 × 72 mm |
| Weight | 401.5 ± 3 g |
| Gears | Steel gears |
| Motor | Brushless motor |
| Document revision | A/0（Official page captured 2026-10-02） |

!!! warning "Source inconsistencies"
    The source title states 12V / 150 kg·cm; its parameter table states 220 kg·cm@14.8V. Confirm the conflicting torque values with FEETECH.

- [FEETECH model source](https://www.feetech.cn/962328)

!!! info "Selection note"
    Stall torque is a short-duration limit, not continuous operating torque. Confirm power, shared ground, interface and mechanical clearance before enabling torque.

<!-- official-specs:start -->
## Official model specifications

[FEETECH official product page](https://www.feetechrc.com/962328) · Checked 2026-10-02. The complete model on the page is FT-150B-C002.

| Parameter | Manufacturer specification |
| --- | --- |
| Model | FT-150B-C002 |
| Storage Temperature Range | -40℃～80℃ |
| Operating Temperature Range | -20℃～60℃ |
| Size | A: 64mm B: 33mm C: 72mm |
| Weight | 401.5g±3g |
| Gear type | 钢 Steel |
| Limit angle | 200° |
| Bearing | 滚珠轴承 Ball bearings |
| Horn gear spline | 15T |
| Case | Aluminum |
| Connector wire | 50±1CM(黑红+黑红白） |
| Motor | Brushless Motor |
| Operating Voltage Range | 10V-16V |
| Idle current (atstopped) | 45mA@14.8V |
| No load speed | 0.204sec/60°(49RPM)@14.8V |
| Runnig current(at no load) | 480mA@14.8V |
| Peak stall torque | 220kg.cm@14.8V |
| Rated torque | 73kg.cm@14.8V |
| Stall current | 4100mA@14.8V |
| Command si gnal | Pulse width modulation |
| Control System Type | Digital comparator |
| Pulse width range | 600~2400 μ sec |
| Stop position | 1500 μ sec |
| Running degree | 180±2°(at 600→2400μsec) |
| Dead band width | ≤4 μ sec |
| Rotating direction | 逆时针 Counterclockwi se (在600→2400 μ sec) |

Attachment checks: PDF content model not verified: FT-150B-C002-规格书-20260310.pdf

Other files linked by the manufacturer (model applicability unconfirmed):

- [FT-150B-C002-规格书-20260310.pdf](https://www.feetechrc.com/Data/feetechrc/upload/file/20260407/6391116694392973979724512.pdf)

![FT-150B-C002 mechanical drawing](images/drawing.webp){ .ft-model-drawing }

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
