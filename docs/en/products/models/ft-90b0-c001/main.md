# FT-90B0-C001

![FT-90B0-C001](images/main.webp){ .ft-model-main-image }

Use this page to compare the main specifications of `FT-90B0-C001` and plan power, control and mechanical integration.

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
| Stall torque | **1.5 kg·cm@6V** |
| Control interface | `PWM` |
| Product family | `FT` |
| Product model | `FT90B-C001` |
| Document revision | `Contact us` |

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

[FEETECH official product page](https://www.feetechrc.com/15kg-low-voltage-drive-digital-9g-steering-gear) · Checked 2026-10-02. The complete model on the page is FT-90B0-C001.

| Parameter | Manufacturer specification |
| --- | --- |
| Model | FT-90B0-C001 |
| Storage Temperature Range | -30℃～80℃ |
| Operating Temperature Range | -20℃～70℃ |
| Size | A：22.5mm B：12.1mm C：22.4mm |
| Weight | 10.5g |
| Gear type | Plastic Gear |
| Limit angle | 180degree |
| Bearing | NO Ball bearings |
| Horn gear spline | 21T(4.86) |
| Horn type | Plastic,POM |
| Case | PC |
| Connector wire | 250mm ±5 mm（ JR）(Brown ,Red and Orange) |
| Motor | Metal brush motor |
| Operating Voltage Range | 3-6V |
| Idle current(at stopped) | 4mA-6mA |
| No load speed | 110RPM@6V |
| Runnig current(at no load) | 120 mA @6V |
| Peak stall torque | 1.5kg.cm@6V |
| Rated torque | 0.5kg.cm@6V |
| Stall current | 800mA@6V |
| Running degree | 180°(when 500～2500 μ sec) |

![FT-90B0-C001 mechanical drawing](images/drawing.webp){ .ft-model-drawing }

[Open full-size drawing](images/drawing.webp)
<!-- official-specs:end -->

<!-- product-resources:start -->
## Resources and document status {#resources}

Local attachments are included in the model package; PDF specifications link to the manufacturer and are not bundled offline. Missing resources are not yet supplied; family guides do not verify model-specific settings.

| Resource | Status / file | Revision |
| --- | --- | --- |
| Model datasheet | [View on manufacturer website (online)](https://www.feetechrc.com/Data/feetechrc/upload/file/20200612/6372758020556571544810589.pdf) | — |
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
