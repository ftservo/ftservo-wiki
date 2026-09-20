# Mechanics and assembly

Start with the exact model's engineering files, then verify mounting interfaces, motion clearance and assembly. Software and mechanical developers should share the same model, drawing revision, zero position and permitted travel.

[Find a model and engineering files](../products/index.md){ .md-button .md-button--primary }
[Resource status and offline packages](../downloads.md#product-packages){ .md-button }

## Continue from your current task

| Task | Check or prepare | Completion result |
| --- | --- | --- |
| Assess fit | Model page → Mechanical integration → Resource table | Correct variant's envelope, mounting drawing and STEP; missing items identified |
| Design a bracket or horn | Datum, hole spacing, threads, engagement depth, shaft and horn | Traceable interface dimensions; no measurements inferred from photos |
| Check joint motion | Mechanical/electrical zero, direction, permitted travel and cable exit | Full-travel clearance with room for cables and connector access |
| Hand off the assembly | Assembly drawing, fasteners, loading, duty cycle and travel | An assembly and limit record usable by the control developer |

## Use engineering files correctly

- **2D mounting drawing**: verify units, datums, dimensions, tolerances, hole positions and fastening requirements for manufacturing interfaces.
- **STEP / 3D model**: verify revision and coordinates for assembly and collision checks. Ask the manufacturer to resolve conflicts with the drawing.
- **STL**: confirm units and scale for visualization or fit prototypes; the mesh does not establish manufacturing tolerances.
- **Product photos**: identify connector orientation, cable exit and the physical variant; they do not replace dimensioned drawings.

Check each model's resource table. When a file is marked “Not supplied”, request that exact model's file through your existing technical-support contact before manufacturing. Files from another suffix require separate confirmation.

## Shared mechanical and software handoff

| Item | Record |
| --- | --- |
| Identity and revisions | Full physical label, drawing/STEP/bracket revisions, firmware if known |
| Zero and direction | Mechanical datum, installed zero, positive direction and mapping to control zero |
| Motion bounds | Confirmed software limits, hard stops and clearance; leave unknown values unconfirmed |
| Loading | Direction, lever arm, inertia/load description, duty cycle and temperature conditions |
| Validation | Unloaded and assembled results, clearance screenshots, faults and stop behavior |

Stall torque is not a continuous rating. Radial/axial capacity, horn compatibility and fastener requirements need model-specific evidence. Complete [unloaded validation for the matching control interface](../getting-started/index.md) before attaching and gradually validating the mechanism.

## Assembly problems

See [interference and zero-position troubleshooting](../troubleshooting.md#mechanical), and include the full model, file revisions and annotated assembly screenshots. “Does not fit” or “cannot reach the angle” alone cannot distinguish a drawing, zero, software-limit or hardware-revision issue.
