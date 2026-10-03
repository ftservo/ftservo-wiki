# FT-2806-C007

![FT-2806-C007](images/main.webp){ .ft-model-main-image }

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
| Input voltage | 4.8–8.4 V |
| Stall torque | 7.2 kg·cm@7.4V |
| No-load speed | 0.073 s/60°@7.4V |
| Travel / rotation | 180±5°（500→2500 μsec） |
| Control interface | PWM |
| Family | FT |
| Dimensions | 23 × 12 × 27.5 mm |
| Weight | 18.3 ± 2 g |
| Gears | Metal gears |
| Motor | Coreless motor |
| Document revision | A/0（Official page captured 2026-10-02） |

- [FEETECH model source](https://www.feetech.cn/500296)

!!! info "Selection note"
    Stall torque is a short-duration limit, not continuous operating torque. Confirm power, shared ground, interface and mechanical clearance before enabling torque.

<!-- official-specs:start -->
## Official model specifications

[FEETECH official product page](https://www.feetech.cn/500296) · Checked 2026-10-02. The complete model on the page is FT-2806-C007.

| Parameter | Manufacturer specification |
| --- | --- |
| Model | FT-2806-C007 |
| Storage Temperature Range | -30℃～70℃ |
| Operating Temperature Range | -20℃～60℃ |
| Size | A：23mm B：12mm C：27.5mm . |
| Weight | 18.3±2g |
| Gear type | Metal |
| Limit angle | No limit |
| Bearing | 滚珠轴承 Ball bearings |
| Horn gear spline | 25T/4.95mm |
| Horn type | Plastic,POM |
| Case | PA66+GF |
| Connector wire | 25±1CM |
| Motor | Coreless Motor |
| Operating Voltage Range | 4.8-8.4V |
| Idle current (at stopped) . | 6mA@7.4V |
| No load speed | 0. 073 sec/ 60°@7.4V |
| Runnig current(at no load) | 80mA@7.4V |
| Peak stall torque | 7.2kg.cm@7.4V |
| Rated torque | 2.4kg.cm@7.4V |
| Stall current | 2.0A@7.4V |
| Command si gnal | Pulse width modification |
| Amplifier type | Digital Controller |
| Pulse width range | 500→2500 μsec |
| Neutral Position | 1500 μsec |
| Running degree | 180±5°(at 500→2500μsec) |
| Dead band width | ≤4 μsec |
| Rotating direction | 逆时针 Counterclockwise(在500→2500 μsec) |

![FT-2806-C007 mechanical drawing](images/drawing.webp){ .ft-model-drawing }

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
