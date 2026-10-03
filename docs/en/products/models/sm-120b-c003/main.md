# SM-120B-C003

![SM-120B-C003](images/main.webp){ .ft-model-main-image }

Specifications transcribed from the supplied documentation for this exact model and suffix.

[Back to catalog](../../datasheets/sm.md){ .md-button }

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
| Input voltage | 24 V |
| Stall torque | 120 kg·cm@24V |
| No-load speed | 0.2 s/60°（50 RPM）@24V |
| Travel / rotation | 360°（0~4095） |
| Control interface | RS-485 |
| Family | SMS |
| Dimensions | 78 × 43 × 65.5 mm |
| Weight | 485 g |
| Gears | Steel gears（gear ratio 232:1） |
| Motor | Brushless motor |
| Communication | Modbus-RTU（RS-485 physical layer），ID 0–253，38400bps ~ 1Mbps |
| Document revision | A/0（Official page captured 2026-10-02） |

!!! warning "Modbus-RTU model"
    This exact model uses Modbus-RTU over RS-485. Obtain its own register table; SMS_STS addresses, units and control modes do not apply.

- [FEETECH model source](https://www.feetech.cn/24v-120kgcm-modbus-rtu舵机)

!!! info "Selection note"
    Stall torque is a short-duration limit, not continuous operating torque. Confirm power, shared ground, interface and mechanical clearance before enabling torque.

<!-- official-specs:start -->
## Official model specifications

[FEETECH official product page](https://www.feetech.cn/24v-120kgcm-modbus-rtu舵机) · Checked 2026-10-02. The complete model on the page is SM-120B-C003.

| Parameter | Manufacturer specification |
| --- | --- |
| Model | SM-120B-C003 |
| Storage Temperature Range | -30℃～80℃ |
| Operating Temperature Range | -20℃～80℃ |
| Size | A：78mm B：43mm C：65.5mm |
| Weight | 485g |
| Gear type | Steel Gear ( Gear Ratio 232:1 ) |
| Limit angle | NO limiter |
| Bearing | 2 Ball bearings |
| Horn gear spline | One character (OD10mm) |
| Horn type | steel |
| Case | Aluminium ( 7075) |
| Connector wire | 300mm ±5 mm |
| Motor | Brushless motor |
| Operating Voltage Range | 24V |
| No load speed | 0.2sec/ 60degree 50RPM@24V |
| Runnig current(at no load) | 200 mA@24V |
| Peak stall torque | 120kg.cm@24V |
| Rated torque | 40kg.cm@24V |
| Stall current | 4000mA@24V |
| Rated Load | 32kg. cm≤ |
| Rated current | 1000mm≤ |
| KM | 30kg. cm/A |
| Terminal resistance | 2.8Ω |
| Command signal | Bus Packet Communication RS485 |
| Protocol Type | Modbus-RTU |
| ID | 0-253 |
| Communication Speed | 38400bps ~ 1 Mbps |
| Running degree | 360° (when 0~4095) |
| Feedback | Load,Position,Speed,Input Voltage,Current,Temperature |
| Position Sensor Resolution | 12Bits Magnetic Coding(360° /4096 ） |

Attachment checks: Different model PDF: SM120BL specs-20191030.pdf

Other files linked by the manufacturer (model applicability unconfirmed):

- [SM120BL specs-20191030.pdf](https://www.feetech.cn/Data/feetechrc/upload/file/20200610/6372738662914383554063966.pdf)

![SM-120B-C003 mechanical drawing](images/drawing.webp){ .ft-model-drawing }

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
