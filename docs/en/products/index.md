# Product Selection

Do not select a servo by headline stall torque alone. A viable choice must satisfy interface, voltage, continuous load, speed, size, travel, feedback and environment requirements together.

## Servo selector

<div id="ft-servo-selector" class="ft-selector" data-locale="en">
  <div class="ft-selector-head">
    <div><strong>Find the right FEETECH servo</strong><span>Browse 142 products by interface, input voltage and torque.</span></div>
    <button type="button" class="ft-selector-reset" data-action="reset">Reset filters</button>
  </div>
  <div class="ft-selector-controls">
    <label class="ft-selector-field ft-selector-search"><span>Search model</span><input type="search" data-filter="query" placeholder="For example ST-3215 or SMS" autocomplete="off"></label>
    <label class="ft-selector-field"><span>Control interface</span><select data-filter="interface"><option value="">All interfaces</option></select></label>
    <label class="ft-selector-field"><span>Product family</span><select data-filter="family"><option value="">All families</option></select></label>
    <label class="ft-selector-field"><span>Input voltage</span><select data-filter="voltage"><option value="">All voltages</option></select></label>
    <label class="ft-selector-field"><span>Minimum stall torque kg·cm</span><input type="number" data-filter="torque" min="0" step="0.1" placeholder="Any"></label>
    <label class="ft-selector-field"><span>Sort</span><select data-filter="sort"><option value="model">Model name</option><option value="torque-desc">Torque high to low</option><option value="torque-asc">Torque low to high</option><option value="voltage">Voltage low to high</option></select></label>
  </div>
  <div class="ft-selector-status" role="status" aria-live="polite">Loading model data…</div>
  <div class="ft-selector-results"></div>
  <button type="button" class="ft-selector-more" data-action="more" hidden>Show more</button>
  <noscript>This selector requires JavaScript. You can still use the product specifications catalog below.</noscript>
</div>

!!! info "Selection note"
    Use the results to compare products quickly. Open the model page for full specifications and allow design margin for load, duty cycle, temperature and mechanism conditions.

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

Use the [official product catalog](https://www.feetechrc.com/products.html) for application information, then compare candidate models in the [product specifications catalog](datasheets/index.md).

| Need | Start with | Note |
| --- | --- | --- |
| Conventional RC control | PWM series | Simple wiring; no bus addressing |
| Education and desktop robots | SCS / STS TTL | Daisy chaining and feedback; model details vary |
| Magnetic encoder/high resolution | STS TTL | Several models provide 360° magnetic sensing |
| Larger or electrically noisy systems | SMS RS485 | Differential bus; requires an RS485 interface |
| Specific high-performance TTL use | HLS TTL | Use the HLS application layer and memory table |

!!! note
    Product offerings change over time. Confirm current availability and application requirements with FEETECH before final selection.
