# ST-3215-C018

![ST-3215-C018](images/main.webp){ .ft-model-main-image }

Use this page to compare the main specifications of `ST-3215-C018` and plan power, control and mechanical integration.

[Back to ST catalog](../../datasheets/st.md){ .md-button }

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
| Stall torque | **30 kg·cm@12V** |
| Control interface | `TTL` |
| Product family | `STS` |
| Product model | `ST-3215-C018` |
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

[FEETECH official product page](https://www.feetechrc.com/525603) · Checked 2026-10-02. The complete model on the page is ST-3215-C018.

!!! warning "Claims requiring confirmation"
    gear: website table gives steel, attached PDF gives copper; a new filter value is withheld pending revision confirmation.
    voltageMin: website table gives 4.0, attached PDF gives 12.0; a new filter value is withheld pending revision confirmation.
    voltageMax: website table gives 14.0, attached PDF gives 12.0; a new filter value is withheld pending revision confirmation.

| Parameter | Manufacturer specification |
| --- | --- |
| Model | ST-3215-C018 |
| Storage Temperature Range | -30℃～80℃ |
| Operating Temperature Range | -20℃～60℃ |
| Size | A：45.2mm B：24.7mm C：35mm |
| Weight | 55± 1g |
| Gear type | 钢齿steel Gear |
| Limit angle | NO limit |
| Bearing | 滚珠轴承Ball bearings |
| Horn gear spline | 25T/OD5.9mm |
| Horn type | Plastic,POM |
| Case | PA+GF |
| Connector wire | 15CM |
| Motor | Core Motor |
| Operating Voltage Range | 4-14V |
| No load speed | 0.222sec/60°@12V |
| Runnig current(at no load) | 180 mA@12V |
| Peak stall torque | 30kg.cm@12V |
| Rated torque | 10kg.cm@12V |
| Stall current | 2.7A@12V |
| Command signal | DigitalPacket |
| Protocol Type | Half Duplex Asynchronous Serial Communication |
| ID | 0-253 |
| Communication Speed | 38400bps ~ 1 Mbps |
| Running degree | 360° (when 0~4096) |
| Feedback | Load (负载),Position (位置) , Speed (工作速度)I nputVoltage (输入电压)，Current (工作电流) |

### Additional facts from the attached datasheet

[Official datasheet](https://www.feetechrc.com/Data/feetechrc/upload/file/20260622/6391772519923113075854851.pdf)

| Parameter | Specification | PDF page |
| --- | --- | --- |
| 角度传感器 Angle Sansor | 类型Type / 12Bits Magnetic Coding | 4 |
| 齿轮虚位Back Lash | ≦0.5° | 4 |
| 摇臂虚位The rocker | 0° | 4 |
| phantom 出力轴螺丝The rocker | M3X6 | 4 |
| screw 马达 Motor | Core Motor | 4 |
| 信号高电平电压 Signal high Voltage | 2V-5V | 8 |
| 信号低电平电压 Signal Low Voltage | 0.0V-0.45V | 8 |

![ST-3215-C018 mechanical drawing](images/drawing.webp){ .ft-model-drawing }

[Open full-size drawing](images/drawing.webp)
<!-- official-specs:end -->

<!-- product-resources:start -->
## Resources and document status {#resources}

Local attachments are included in the model package; PDF specifications link to the manufacturer and are not bundled offline. Missing resources are not yet supplied; family guides do not verify model-specific settings.

| Resource | Status / file | Revision |
| --- | --- | --- |
| Model datasheet | [View on manufacturer website (online)](https://www.feetechrc.com/Data/feetechrc/upload/file/20260622/6391772519923113075854851.pdf) | A/0 |
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
