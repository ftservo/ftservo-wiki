# SM-2912-C001

![SM-2912-C001](images/main.webp){ .ft-model-main-image }

Use this page to compare the main specifications of `SM-2912-C001` and plan power, control and mechanical integration.

[Back to SM catalog](../../datasheets/sm.md){ .md-button }

## Start your integration

| Your task | Start here | What to check |
| --- | --- | --- |
| Write control software | [Software integration](software.md) | Interface, application layer, read-first bring-up and validation record |
| Design a bracket or joint | [Mechanical integration](mechanical.md) | Drawings, CAD, datum, output shaft and cable clearance |
| Collect engineering files | [Resources and status](#resources) | Available files and outstanding information |

## Key specifications

| Item | Value |
| --- | --- |
| Input voltage | **9–12.6 V** |
| Stall torque | **12 kg·cm@12V** |
| Control interface | `RS-485` |
| Product family | `SMS` |
| Product model | `SM2912-C001` |
| Document revision | `A/0` |

!!! info "Selection note"
    Stall torque is a short-duration limit for product comparison, not a continuous operating point. Allow suitable margin for duty cycle, temperature, impact, acceleration and mechanism friction.

## Selection and use

1. Confirm the product label and document revision match this page.
2. Confirm the permitted supply range from this model’s formal documentation before selecting a regulated supply; a single catalog voltage does not establish a range. Size current for simultaneous operation.
3. Match the controller, wiring and SDK to the listed interface and product family.
4. Check mounting space, output shaft, travel and mechanical clearance before enabling torque.

For communication commands and software integration, continue with the [SDK guide](../../../sdk/index.md) and the protocol documentation for this product family.

<!-- official-specs:start -->
## Official model specifications

[FEETECH official product page](https://www.feetechrc.com/24v40kg-rs485-serial-bus-steering-gear) · Checked 2026-10-02. The complete model on the page is SM-2912-C001.

| Parameter | Manufacturer specification |
| --- | --- |
| Model | SM-2912-C001 |
| Storage Temperature Range | -30℃～80℃ |
| OperatinTemperatureRange | -15℃～70℃ |
| Size | A：40mm B：28mm C：42.3mm |
| Weight | 102± 1g |
| Horn Type | 6T/OD4.75mm |
| Gear Ratio | 1/241 |
| Gear material | 钢 Steel |
| Case material | Aluminium |
| Motor | Brushless Motor |
| Bearing type | 滚珠轴承 Ball bearings |
| Limit angle | No Limiter |
| Command signal | Digital Packet |
| Protocol Type | Half Duplex Asynchronous Serial Communication |
| Baud rate | 38400bps ~ 1 Mbps |
| voltage | 12V |
| No Load Speed | 0.092sec/60°(109RPM) |
| Running Current | ≦150mA |
| Stall torque | 22kg.cm |
| Stall Current (at locked) | 2.2A |
| Quiescent Current | 22mA |
| Rated Torgue | 7kg.cm |
| Rated Current | 700mA |
| Kt | 10kg.cm/A |
| Resolution | 0.088°(360°/4096) |

Attachment checks: PDF content model not verified: SM2912-C001-串型规格书-20260321.pdf

Other files linked by the manufacturer (model applicability unconfirmed):

- [SM2912-C001-串型规格书-20260321.pdf](https://www.feetechrc.com/Data/feetechrc/upload/file/20260706/6391895917187692344479707.pdf)

![SM-2912-C001 mechanical drawing](images/drawing.webp){ .ft-model-drawing }

[Open full-size drawing](images/drawing.webp)
<!-- official-specs:end -->

<!-- product-resources:start -->
## Resources and document status {#resources}

Local attachments are included in the model package; PDF specifications link to the manufacturer and are not bundled offline. Missing resources are not yet supplied; family guides do not verify model-specific settings.

| Resource | Status / file | Revision |
| --- | --- | --- |
| Model datasheet | Not supplied | — |
| Connector and pinout | Not supplied | — |
| Model memory table / firmware notes | Not supplied | — |
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
