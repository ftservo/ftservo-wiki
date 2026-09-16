# Model page template

Product engineering must first approve the mapping from sales model to active datasheet. Copy the structure below for each model. Replace every `pending review` field with a sourced and approved value before publication. Submit the Chinese page and its same-path English page together.

```markdown
# Full sales model

> Applies to: document ID, revision, release date, firmware, reviewer

## Product role

State control method, intended mechanism and main limitations.

## Key specifications

| Item | Value and unit | Conditions | Source page |
| --- | --- | --- | --- |
| Supply voltage | pending review | pending review | pending review |
| Rated and peak torque | pending review | pending review | pending review |
| Speed | pending review | pending review | pending review |
| Size and mass | pending review | pending review | pending review |

## Power interface and wiring

Pinout, shared ground, protection and adapter, sourced from the exact model.

## Mounting and motion

Holes, shaft, horn, mechanical zero, clearance, STEP and 2D drawing.

## Performance curves

Plots, conditions, sample count, continuous and peak limits, raw CSV and method.

## Control and development

Matching protocol, memory table, firmware, SDK layer and tested example.

## Downloads and versions

Active datasheet, drawing, CAD, data and revision log.

## Troubleshooting

Only guidance verified for this model and applicable revision.
```

Link the new page from the [datasheet directory](../products/datasheets/index.md), add it to both language navigation trees and follow the [maintenance guide](../contributing.md) for strict build and engineering review. Remove all `pending review` rows from the published page.
