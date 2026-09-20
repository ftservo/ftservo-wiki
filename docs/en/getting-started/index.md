# Get started

Confirm the full physical model first, then choose the matching control path. Software bring-up and mechanical design have separate entry points.

[Find my model](../products/index.md){ .md-button .md-button--primary }
[I am designing mechanics](../mechanical/index.md){ .md-button }

## Choose a control path

| Interface confirmed by the model documents | Start here | First completion check |
| --- | --- | --- |
| TTL / RS-485 bus | [Bus servo setup](bus.md) | Confirm one servo's identity and read-only communication before a small motion |
| PWM | [PWM servo setup](pwm.md) | Confirm pinout and signal settings before neutral/stop and small-response checks |
| Model or interface unknown | [Model and family identification](../products/series.md) | Obtain documents matching the physical suffix before experimental wiring or commands |

## Keep a result at each stage

| Stage | Required input | Record on completion | If blocked |
| --- | --- | --- | --- |
| Model identification | Label, suffix and document revision | Physical/document identity mapping | Request missing information from the model page |
| Wiring | Supply, pinout, adapter/controller and ground | Wiring photos and actual configuration | [Power and wiring](wiring.md) |
| Minimal validation | No load, clearance, confirmed control settings | Identity/PWM response, faults and stop method | [Troubleshooting by symptom](../troubleshooting.md) |
| Software integration | Validated configuration and matching example | Platform, code revision and reproducible record | [Software development](../sdk/index.md) |
| Mechanical integration | Drawings, model, zero and permitted travel | Assembly and clearance record | [Mechanics and assembly](../mechanical/index.md) |

Some models currently have only a specification summary; dedicated pinouts, CAD or examples are not supplied. Check the model's resource status rather than substituting generic settings for missing information.
