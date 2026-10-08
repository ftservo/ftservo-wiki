---
hide:
  - toc
---

# Product Selection

Do not select a servo by headline stall torque alone. A viable choice must satisfy interface, voltage, continuous load, speed, size, travel, feedback and environment requirements together.

Not sure which family you need? Start with [Families and interfaces](series.md) for how they differ in positioning, protocol and interface.

## Servo selector

<div id="ft-servo-selector" class="ft-selector" data-locale="en">
  <div class="ft-selector-head">
    <div><strong>Find your FEETECH servo</strong><span>Filter instantly and compare candidate models.</span></div>
    <div class="ft-selector-buttons"><button type="button" class="ft-selector-reset" data-action="advanced" aria-expanded="false" aria-controls="ft-professional-panel">Professional selection</button><button type="button" class="ft-selector-reset" data-action="reset">Reset filters</button></div>
  </div>
  <div class="ft-selector-layout">
    <aside id="ft-professional-panel" class="ft-selector-sidebar" aria-label="Professional filters" hidden>
      <div class="ft-sidebar-heading">Filters<small>Select multiple</small></div>
      <label class="ft-selector-field"><span>Search model</span><input type="search" data-filter="query" aria-label="Search model" autocomplete="off" placeholder="ST-3215 / HL-3950"></label>
      <fieldset class="ft-filter-group"><legend>Control interface</legend><div class="ft-filter-options" data-group="interface"></div></fieldset>
      <fieldset class="ft-filter-group"><legend>Product family</legend><div class="ft-filter-options" data-group="family"></div></fieldset>
      <fieldset class="ft-filter-group"><legend>Input voltage · V</legend><div class="ft-filter-options" data-group="voltage"></div></fieldset>
      <fieldset class="ft-filter-group ft-range-group"><legend>Stall torque <small>kg·cm</small></legend><div class="ft-range-pair"><label class="ft-selector-field"><span>Minimum</span><input type="number" data-filter="torque" aria-label="Minimum" min="0" step="0.1" placeholder="Any"></label><span class="ft-range-dash">—</span><label class="ft-selector-field"><span>Maximum</span><input type="number" data-filter="torqueMax" aria-label="Maximum" min="0" step="0.1" placeholder="Any"></label></div><div class="ft-range-sliders"><input class="ft-filter-slider" type="range" min="0" max="150" step="0.1" value="0" data-default="0" data-range-for="torque" aria-label="Stall torqueMinimum"><input class="ft-filter-slider" type="range" min="0" max="150" step="0.1" value="150" data-default="150" data-range-for="torqueMax" aria-label="Stall torqueMaximum"></div></fieldset>
      <fieldset class="ft-filter-group ft-range-group"><legend>No-load speed <small>rpm</small></legend><div class="ft-range-pair"><label class="ft-selector-field"><span>Minimum</span><input type="number" data-filter="speed" aria-label="Minimum" min="0" step="0.1" placeholder="Any"></label><span class="ft-range-dash">—</span><label class="ft-selector-field"><span>Maximum</span><input type="number" data-filter="speedMax" aria-label="Maximum" min="0" step="0.1" placeholder="Any"></label></div><div class="ft-range-sliders"><input class="ft-filter-slider" type="range" min="0" max="180" step="0.1" value="0" data-default="0" data-range-for="speed" aria-label="No-load speedMinimum"><input class="ft-filter-slider" type="range" min="0" max="180" step="0.1" value="180" data-default="180" data-range-for="speedMax" aria-label="No-load speedMaximum"></div></fieldset>
      <fieldset class="ft-filter-group ft-limit-group"><legend>Position range ≥ · °</legend><label class="ft-selector-field"><span>Minimum</span><input type="number" data-filter="positionRange" aria-label="Minimum" min="0" step="0.1" placeholder="Any"></label><input class="ft-filter-slider" type="range" min="0" max="360" step="0.1" value="0" data-default="0" data-range-for="positionRange" aria-label="Position range ≥ · °"></fieldset><fieldset class="ft-filter-group ft-limit-group"><legend>Longest edge ≤ · mm</legend><label class="ft-selector-field"><span>Maximum</span><input type="number" data-filter="maxEdge" aria-label="Maximum" min="0" step="0.1" placeholder="Any"></label><input class="ft-filter-slider" type="range" min="0" max="150" step="0.1" value="150" data-default="150" data-range-for="maxEdge" aria-label="Longest edge ≤ · mm"></fieldset><fieldset class="ft-filter-group ft-limit-group"><legend>Weight ≤ · g</legend><label class="ft-selector-field"><span>Maximum</span><input type="number" data-filter="weight" aria-label="Maximum" min="0" step="0.1" placeholder="Any"></label><input class="ft-filter-slider" type="range" min="0" max="500" step="0.1" value="500" data-default="500" data-range-for="weight" aria-label="Weight ≤ · g"></fieldset>
      <fieldset class="ft-filter-group"><legend>Continuous rotation</legend><div class="ft-filter-options" data-group="continuous"></div></fieldset>
      <fieldset class="ft-filter-group"><legend>Motor type</legend><div class="ft-filter-options" data-group="motor"></div></fieldset>
      <fieldset class="ft-filter-group"><legend>Gear material</legend><div class="ft-filter-options" data-group="gear"></div></fieldset>
      <fieldset class="ft-filter-group"><legend>Case material</legend><div class="ft-filter-options" data-group="case"></div></fieldset>
      <fieldset class="ft-filter-group"><legend>Shaft configuration</legend><div class="ft-filter-options" data-group="shaft"></div></fieldset>
      <p class="ft-filter-note">Blank means unrestricted; unknown values do not match. Voltage uses the catalog reference. Positioning span is separate from continuous rotation. Longest edge is the largest of three dimensions. Sliders: torque 0–150 kg·cm, speed 0–180 rpm; larger values can be entered.</p>
    </aside>
    <section class="ft-selector-main" aria-label="Selection results">
      <div class="ft-selector-controls ft-selector-basic">
        <label class="ft-selector-field"><span>Search model</span><input type="search" data-filter="query" aria-label="Search model" autocomplete="off" placeholder="ST-3215 / HL-3950"></label>
        <label class="ft-selector-field"><span>Control interface</span><select data-category="interface" aria-label="Control interface"><option value="">All</option></select></label><label class="ft-selector-field"><span>Product family</span><select data-category="family" aria-label="Product family"><option value="">All</option></select></label><label class="ft-selector-field"><span>Input voltage</span><select data-category="voltage" aria-label="Input voltage"><option value="">All</option></select></label>
        <label class="ft-selector-field"><span>Minimum stall torque · kg·cm</span><input type="number" data-filter="torque" aria-label="Minimum stall torque · kg·cm" min="0" step="0.1" placeholder="Any"></label>
        <label class="ft-selector-field"><span>Minimum no-load speed · rpm</span><input type="number" data-filter="speed" aria-label="Minimum no-load speed · rpm" min="0" step="0.1" placeholder="Any"></label>
      </div>
      <div class="ft-selector-toolbar"><div class="ft-selector-status" role="status" aria-live="polite">Loading models…</div><label class="ft-selector-sort"><span>Sort</span><select data-filter="sort" title="HLS and STS first; selected order within each group"><option value="recommended">Featured first</option><option value="model">Model</option><option value="torque-desc">Torque ↓</option><option value="torque-asc">Torque ↑</option><option value="speed-desc">Speed ↓</option><option value="weight-asc">Weight ↑</option></select></label></div>
      <div class="ft-results-scroll" tabindex="0" aria-label="Product list"><div class="ft-selector-results"></div><button type="button" class="ft-selector-more" data-action="more" hidden>Show more</button></div>
    </section>
  </div>
  <noscript>This selector requires JavaScript. The series catalog below remains available.</noscript>
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
