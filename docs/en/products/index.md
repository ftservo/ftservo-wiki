# Product Selection

Do not select a servo by headline stall torque alone. A viable choice must satisfy interface, voltage, continuous load, speed, size, travel, feedback and environment requirements together.

## Six filters

1. **Control**: use PWM for conventional pulse control; use a bus servo for addressing, daisy chaining, feedback and configuration.
2. **Physical interface**: TTL is common inside compact robots; consider RS485 for longer links or noisy environments. Match the existing controller.
3. **Power**: use the exact model's rated voltage and size the supply for peak current and simultaneous motion.
4. **Mechanics**: calculate torque at the real lever arm, including gravity, acceleration, friction, impacts and margin.
5. **Motion**: verify speed, travel, continuous-rotation requirements, resolution and encoder type.
6. **Integration**: verify envelope, shaft, mass, mounting, gears, protection and operating temperature.

## Torque estimate

```text
required torque (kg·cm) ≈ load (kg) × arm (cm) × safety factor
```

A 1 kg load at 10 cm is 10 kg·cm statically. Real mechanisms need allowance for dynamics and should not operate continuously near stall torque.

## Selection worksheet

| Constraint | Requirement | Candidate |
| --- | --- | --- |
| Interface | PWM / TTL / RS485 / other | |
| Supply | V | |
| Continuous/peak torque | kg·cm or N·m | |
| Speed | s/60° or RPM | |
| Motion | limited / multi-turn / continuous | |
| Feedback | position / speed / load / voltage / temperature | |
| Maximum size and mass | mm / g | |
| Platform | PC / Arduino / ESP32 / Linux / STM32 | |

Use the [official product catalog](https://www.feetechrc.com/products.html) to shortlist models, then open the [datasheet directory](datasheets/index.md) and verify the exact PDF cover model and revision. A document filename may differ from the sales model.

| Need | Start with | Note |
| --- | --- | --- |
| Conventional RC control | PWM series | Simple wiring; no bus addressing |
| Education and desktop robots | SCS / STS TTL | Daisy chaining and feedback; model details vary |
| Magnetic encoder/high resolution | STS TTL | Several models provide 360° magnetic sensing |
| Larger or electrically noisy systems | SMS RS485 | Differential bus; requires an RS485 interface |
| Specific high-performance TTL use | HLS TTL | Use the HLS application layer and memory table |

!!! note
    The catalog changes over time. Final selection must use the current product page, sales confirmation and approved exact-model datasheet.
