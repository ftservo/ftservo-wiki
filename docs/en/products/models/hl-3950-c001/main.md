# HL-3950-C001

Use this page to compare the main specifications of `HL-3950-C001` and plan power, control and mechanical integration.

[Back to HL catalog](../../datasheets/hl.md){ .md-button }

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
| Stall torque | **50 kg·cm@12V** |
| Control interface | `TTL` |
| Product family | `HLS` |
| Product model | `HLS3950M-C001` |
| Document revision | `A/0` |

## Measured characteristic curves

The chart reads the torque-test fixture's original `test-result.json` from this product folder and uses the fixture UI's fixed model ranges. Speed, current, efficiency and power share one plot, each with its own color-matched vertical axis. The default smoothed trends follow the fixture's processing; switch to measured points to see the original lines. Hover or touch to inspect torque and all four parameters together. Scroll horizontally on small screens.

<div class="servo-characteristic-chart" data-source="../test-result.json" data-title="HLS3950M measured T-N characteristic curves">
  <p class="servo-chart-loading">Loading torque-test data…</p>
</div>

!!! note "Test-data note"
    This example reuses the torque-test fixture's raw `SN12212_20260818-195011_52de9cb9.json` export. It was tested on 2026-08-18 with result serial number `SN12212`. The chart is a smoothed trend for that individual test and does not replace rated or stall specifications in the product datasheet.

!!! info "Selection note"
    Stall torque is a short-duration limit for product comparison, not a continuous operating point. Allow suitable margin for duty cycle, temperature, impact, acceleration and mechanism friction.

## Selection and use

1. Confirm the product label and document revision match this page.
2. Confirm the permitted supply range from this model’s formal documentation before selecting a regulated supply; a single catalog voltage does not establish a range. Size current for simultaneous operation.
3. Match the controller, wiring and SDK to the listed interface and product family.
4. Check mounting space, output shaft, travel and mechanical clearance before enabling torque.

For communication commands and software integration, continue with the [SDK guide](../../../sdk/index.md) and the protocol documentation for this product family.

<!-- product-resources:start -->
## Resources and document status {#resources}

Only files included in this model package have download links. Missing resources are not yet supplied; family guides do not verify model-specific settings.

| Resource | Status / file | Revision |
| --- | --- | --- |
| Model datasheet | Not supplied | — |
| Connector and pinout | Not supplied | — |
| Model memory table / firmware notes | Not supplied | — |
| 2D mounting drawing | Not supplied | — |
| STEP / 3D model | Not supplied | — |
| Model-tested example | Not supplied | — |
| Raw test data | [test-result.json](test-result.json) | — |
| Test record and conditions | [test-notes.md](tests/test-notes.md) | — |

[Package manifest](manifest.json) · [Request missing resources](#support)

For an offline ZIP with both languages and available attachments, see [product-package export](../../../downloads.md#product-packages).
<!-- product-resources:end -->

## Request resources or report an issue {#support}

Use your existing FEETECH technical-support contact and include the full label/model suffix, firmware version (if known), and the document revision you are using.

- Software: controller/OS, SDK version or commit, adapter/interface, supply voltage, confirmed ID/baud rate (bus models only), minimal reproduction and logs.
- Mechanics: drawing/CAD revision, marked dimensions, required travel, horn/bracket, load and lever arm, duty cycle, and the point of interference.
- Missing files: name the exact item in the resource table (for example, this model's STEP and a dimensioned mounting drawing).

This package currently provides a specification summary and integration checklists. File availability does not imply that your firmware, load case or assembly has been validated.
