# ST-2000-C001

![ST-2000-C001](images/main.webp){ .ft-model-main-image }

Specifications transcribed from the supplied documentation for this exact model and suffix.

[Back to catalog](../../datasheets/st.md){ .md-button }

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
| Input voltage | 5.5–9 V |
| Stall torque | 24.3 kg·cm@8.4V |
| No-load speed | 0.147 s/60°（68 RPM）@8.4V |
| Travel / rotation | 360°（0~4095，12-bitmagnetic encoder） |
| Control interface | TTL |
| Family | STS |
| Dimensions | 40 × 20 × 40.8 mm |
| Weight | 62.1 ± 1 g |
| Gears | Copper gears |
| Motor | Iron-core motor |
| Communication | TTL half-duplex asynchronous serial，ID 0–253，38400bps ~ 1Mbps |
| Bearings and output shaft | Ball bearings；output shaft 25T/OD5.9mm；PH2.0-3P，cable length 15cm |
| Idle current | 32 mA@8.4V |
| Document revision | A/0（Official page captured 2026-10-02） |

!!! warning "Source inconsistencies"
    The supplied source records conflicting values. Confirm them with FEETECH before integration.

- [FEETECH model source](https://www.feetech.cn/525256)

!!! info "Selection note"
    Stall torque is a short-duration limit, not continuous operating torque. Confirm power, shared ground, interface and mechanical clearance before enabling torque.

<!-- official-specs:start -->
## Official model specifications

[FEETECH official product page](https://www.feetechrc.com/525256) · Checked 2026-10-02. The complete model on the page is ST-2000-C001.

| Parameter | Manufacturer specification |
| --- | --- |
| Model | ST-2000-C001 |
| Storage Temperature Range | -30℃～80℃ |
| Operating Temperature Range | -10℃～60℃ |
| Size | A：40mm B：20mm C：40.8mm |
| Weight | 62.1± 1g |
| Gear type | 铜 Copper |
| Limit angle | NO limit |
| Bearing | 滚珠轴承 Ball bearings |
| Horn gear spline | 25T/OD5.9mm |
| Case | Aluminium |
| Type | PH2.0-3P |
| Connector wire | 15cm |
| Motor | 铁芯电机Core Motor |
| Operating Voltage Range | 5.5V-9V |
| Idle | 32MA@8.4V |
| No load speed | 0.147sec/60° (68RPM)@8.4V |
| Runnig current(at no load) | 280mA@8.4V |
| Peak stall torque | 24.3kg.cm@8.4V |
| Rated torque | 8.1kg.cm@6V |
| Stall current | 2.6A@8.4V |
| Command signal | Digital Packet |
| Protocol Type | Half Duplex AsynchronousSerial Communication |
| ID | 0-253 |
| Communication Speed | 38400bps ~ 1 Mbps |
| Running degree | 360° (when 0~4095) |
| Feedback | Load（负载）, Position（位置）,Speed（工作速度）, InputVoltage（输入电压），Current（工作电流）,Temperature（工作温度） |
| Position Sensor Resolution | 12Bits Magnetic Coding(360° /4095） |

Attachment checks: Different model PDF: STS20-C001.pdf

Other files linked by the manufacturer (model applicability unconfirmed):

- [STS20-C001.pdf](https://www.feetechrc.com/Data/feetechrc/upload/file/20260622/6391772508455899421855510.pdf)

![ST-2000-C001 mechanical drawing](images/drawing.webp){ .ft-model-drawing }

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
