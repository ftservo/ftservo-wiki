# Engineering resources

The Wiki currently provides a [datasheet directory](../products/datasheets/index.md), [protocol and memory-table guidance](../reference/protocol.md), [FD utility guidance](../tools/fd.md) and [official SDKs](../sdk/index.md). Mechanical design, continuous-load assessment and integration need engineering-approved resources for each exact model.

## Find resources by task

| Task | Current entry | Next resource to publish |
| --- | --- | --- |
| Confirm model and electrical limits | [Datasheets](../products/datasheets/index.md) | Approved sales-model to datasheet-revision mapping and filterable specifications |
| Size for continuous load | [Selection guide](../products/index.md) | Torque-speed, efficiency and temperature-rise curves, continuous and peak limits |
| Design mounting | Dimensions in datasheets | STEP, 2D mounting drawing, spline and horn dimensions, tolerances |
| Integrate a controller | [Power and wiring](../getting-started/wiring.md), [SDKs](../sdk/index.md) | Series-specific wiring, adapter list, runnable examples and test records |
| Troubleshoot | [Troubleshooting](../troubleshooting.md) | Model- and firmware-specific symptoms, logs and remedies |

## Publication rule

Each model page should identify the **full sales model, approved datasheet revision, publication date and engineering reviewer**. Voltage, pinout, registers, resolution, mechanical travel and protection settings must come from that exact model's approved documents. A PDF filename is only a document identifier.

Curves need test methods, conditions and raw data. CAD models need units, coordinate orientation, revision, dimension checks and licensing status. Copy the [model page template](model-template.md) and follow the [Wiki maintenance guide](../contributing.md) to publish Chinese and English pages for review.
