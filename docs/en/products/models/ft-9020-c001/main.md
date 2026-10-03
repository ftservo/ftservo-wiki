# FT-9020-C001

![FT-9020-C001](images/main.webp){ .ft-model-main-image }

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
| Input voltage | 9–12 V |
| Stall torque | 20 kg·cm@12V |
| No-load speed | 0.105 s/60°（95 RPM）@12V |
| Travel / rotation | 200±5°（500→2500 μsec） |
| Control interface | PWM |
| Family | FT |
| Dimensions | 30 × 15 × 37.5 mm |
| Weight | 46.8 ± 2 g |
| Gears | Metal gears（aluminum case） |
| Motor | Brushless motor |
| Document revision | A/0（Official page captured 2026-10-02） |

- [FEETECH model source](https://www.feetech.cn/6v-35kg-digital-steering-gear)

!!! info "Selection note"
    Stall torque is a short-duration limit, not continuous operating torque. Confirm power, shared ground, interface and mechanical clearance before enabling torque.

<!-- official-specs:start -->
## Official model specifications

[FEETECH official product page](https://www.feetechrc.com/6v-35kg-digital-steering-gear) · Checked 2026-10-02. The complete model on the page is FT-9020-C001.

| Parameter | Manufacturer specification |
| --- | --- |
| Model | FT-9020-C001 |
| Storage Temperature Range | -30℃～80℃ |
| Operating Temperature Range | -40℃～60℃ |
| Size | A: 30mm B: 15mm C: 37.5mm |
| Weight | 46.8±2 |
| Gear type | 钢 Steel |
| Limit angle | No limit |
| Bearing | 滚珠轴承 Ball bearings |
| Horn gear spline | 25T/5.95mm |
| Gear Ratio | 1/305 |
| Case | Aluminum |
| Connector wire | 26±1CM |
| Motor | Brushless Motor |
| Operating Voltage Range | 9V-12V |
| Idle current (at stopped) . | 36mA@12V |
| No load speed | 0.105sec/60° (95RPM)@12V |
| Runnig current(at no load) | 200mA@12V |
| Peak stall torque | 20kg.cm@12V |
| Rated torque | 6.4kg.cm@12V |
| Stall current | 400mA@12V |
| Command si gnal | Pulse width modification |
| Amplifier type | Digital Controller |
| Pulse width range | 500→2500 μsec |
| Stop position | 1500 μsec |
| Running degree | 200±5°(at 500→2500μsec) |
| Dead band width | ≤4 μsec |
| Rotating direction | 逆时针 Counterclockwise(在500→2500 μsec) |

Attachment checks: PDF content model not verified: FT-9020-C001.pdf

Other files linked by the manufacturer (model applicability unconfirmed):

- [FT-9020-C001.pdf](https://www.feetechrc.com/Data/feetechrc/upload/file/20260623/6391782351634931919819421.pdf)

![FT-9020-C001 mechanical drawing](images/drawing.webp){ .ft-model-drawing }

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
