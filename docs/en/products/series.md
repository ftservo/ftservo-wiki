# Series and Interfaces

!!! tip "First time here? Don't memorise the series names yet"
    Work out **what you want to build** first, then use "Quick orientation" below. Once you have a family, check exact models in the [product catalog](datasheets/index.md), or go back to the [product selector](index.md) and filter candidates.

## Quick orientation

| Your situation                                                                       | Start here    | Why                                                                                                                                                                                                                                                                                            |
| ------------------------------------------------------------------------------------ | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| First bus servo, or following an open-source project or tutorial                     | **STS**       | Largest model range and the most documentation and community examples; magnetic encoder with high resolution, so newcomers are least likely to get stuck                                                                                                                                       |
| Budget-sensitive small project: gripper, gimbal, RC conversion                       | **SCS**       | Entry-level position bus servo — low cost, good enough for basic tasks                                                                                                                                                                                                                         |
| Many servos, long cable runs, electrically noisy environment (large arms, humanoids) | **SMS**       | Differential RS485 communication; strong noise immunity, suited to long cables and daisy-chained servos                                                                                                                                                                                        |
| Microduck, Open Duck or similar lightweight bipeds                                   | **HD**        | Compact coreless motor + metal gears + dual-shaft structure; officially described as a "constant-force dual-shaft TTL bus servo" and built for lightweight bipeds                                                                                                                              |
| Force control, torque limiting or compliant gripping                                 | **HLS**       | Constant-current (constant-force) mode and software torque limiting are its core; ST and SM models also report position, speed and current, but constant force and compliant backdriving are mainly HLS territory — common in grippers, dexterous hands and human-robot interaction mechanisms |
| An existing CAN bus that needs long harnesses and higher protection                  | **FU**        | CAN (UAVCAN) bus; brushless high torque, titanium-gear metal case, high ingress protection                                                                                                                                                                                                     |
| Just plugging into an RC receiver, no code                                           | **PWM servo** | Classic pulse-width control with no bus ID addressing; see [PWM servos](#pwm-servos) below                                                                                                                                                                                                     |

## Not sure? Answer 6 questions

Work down the list and take the first "yes" as your answer:

| # | Ask yourself                                                                                          | If yes                   | If no                       |
| - | ----------------------------------------------------------------------------------------------------- | ------------------------ | --------------------------- |
| 1 | Do you need to read back position/temperature/load, or chain several servos on one bus?               | Go to question 2         | **PWM servo**               |
| 2 | Many servos, long cable runs, or a noisy environment?                                                 | **SMS** (RS485)          | Go to question 3            |
| 3 | Do you need current feedback for force control, torque limiting or compliant gripping?                | **HLS** (constant force) | Go to question 4            |
| 4 | Building a Microduck / Open Duck-style lightweight biped that needs a coreless motor and dual shafts? | **HD**                   | Go to question 5            |
| 5 | Already have a CAN bus and need long harnesses or higher protection?                                  | **FU** (CAN)             | Go to question 6            |
| 6 | Is budget the priority, and basic positioning all you need?                                           | **SCS**                  | **STS (mainstream choice)** |

## The model name tells you the family

FEETECH part numbers read "product series - model code - sequence code", and **the product series maps directly to the family** — one glance at a model tells you its interface and SDK:

| Product series                | Family     | Control interface | Memory hook                   |
| ----------------------------- | ---------- | ----------------- | ----------------------------- |
| `SC-`                         | SCS        | Half-duplex TTL   | Entry-level value             |
| `ST-`                         | STS        | Half-duplex TTL   | Mainstream all-rounder        |
| `SM-`                         | SMS        | RS485             | RS485, long runs, noisy sites |
| `HL-`                         | HLS        | Half-duplex TTL   | **HL** = **constant force**   |
| `HD-`                         | HD         | Half-duplex TTL   | Lightweight dual-shaft joint  |
| `FU-`                         | FU         | CAN / UAVCAN      | CAN networking                |
| `FT-` `FS-` `FB-` `FR-` `FI-` | PWM family | PWM signal        | No bus, no ID needed          |

!!! note "The number is not a performance grade"
    Digits in a model name are only identifiers and say nothing about torque or speed. Within one family, voltage, torque, speed and resolution can differ widely — use the [product catalog](datasheets/index.md) and the datasheet published with the product.

## The six bus families, one by one

### “STS” mainstream all-rounder

- **In one line**: the workhorse family of FEETECH bus servos, mostly magnetic-encoder, high-resolution or continuous-rotation models.
- **Representative models**: ST-3215-C001, ST-3025-C001 and others (see the [product catalog](datasheets/index.md)).
- **Good for**: education robots, desktop arms, gimbals and the vast majority of open-source robot projects; newcomers buying their first bus servo.
- **Not for**: very long cables or electrically noisy sites (look at SMS); projects where cost dominates and high resolution is unnecessary (look at SCS).
- **Getting started**: the SDK uses the `STS` application layer; check the [STS memory table](../reference/parameter/memory-sts.md) for your model before touching registers.

### “SCS” entry-level value

- **In one line**: a lower-resolution position bus servo and the value-priced way into the ecosystem.
- **Representative models**: SC-0090-C001, SC-1500-C022 and others.
- **Good for**: budget-limited small projects, simple grippers, gimbals and linked mechanisms — anything that only needs "position it and chain it".
- **Not for**: projects that need high-resolution positioning or precise speed control in continuous rotation (step up to STS).
- **Getting started**: the SDK uses the `SCSCL` application layer, whose register layout is **different** from `STS` — do not mix them; see the [SCSCL memory table](../reference/parameter/memory-scscl.md).

### “SMS” engineering reliability

- **In one line**: RS485 differential bus servos designed for longer cables and more demanding electrical environments.
- **Representative models**: SM-45BL-C001, SM-120B-C001 and others.
- **Good for**: large arms and humanoids with many servos and long wiring; industrial or lab environments with strong interference.
- **Not for**: short-run, few-servo toy-grade projects (TTL is simpler); users without an RS485 adapter need to buy one first.
- **Getting started**: you need an RS485 transceiver/adapter, and the A/B wires must not be swapped — see [debug boards and adapters](../tools/adapters.md); the register table for SMS (RS485) is the [SMS memory table](../reference/parameter/memory-sms.md).
- **The other one you must not mix up**: SMSMB follows the standard MODBUS-RTU protocol, whose addressing is completely different; its register table is the [SMSMB memory table](../reference/parameter/memory-smsmb.md). In the official current range, the MODBUS models under the `SM-` prefix are SM-120B-C003, SM-24BL-C015, SM-2924-C001 and SM-2924-C012, while the remaining `SM-` models use the serial (half-duplex) protocol — check which family your model belongs to before wiring.

### “HLS” premium constant force

- **In one line**: uses the HLS-specific `HLSCL` application layer and memory table, focused on force control and compliant interaction, with multi-turn positioning (±7 turns).
- **Representative models**: HL-2915-C001, HL-3606-C001 and others.
- **Good for**: grippers, dexterous hands and human-robot interaction; projects that read current back for force control, torque limiting or compliant backdriving.
- **Not for**: newcomers hoping to reuse STS/SCS tutorials and code unchanged (neither the application layer nor the memory table is compatible).
- **Getting started**: the SDK uses `HLSCL`; see the [HLS memory table](../reference/parameter/memory-hls.md).

### “HD” lightweight dual-shaft joint

- **In one line**: officially described as a "constant-force dual-shaft TTL bus servo" — compact coreless motor + metal gears + dual-shaft structure, supporting angle servo / constant speed / constant current (constant force) and multi-turn, aimed at Microduck and Open Duck-style lightweight bipeds.
- **Representative models**: HD-1910-C001.
- **Good for**: lightweight bipeds and small joints where weight and volume matter and metal gears are needed for durability; the official applications also list industrial equipment and robots with high-torque transmission.
- **Not for**: general arms, gimbals and other mainstream uses (STS covers far more models with far more documentation).
- **Getting started**: the SDK and memory table **follow the resources supplied with your model** — confirm the firmware and memory-table revision first; the register layout can be referenced against the [HLS memory table](../reference/parameter/memory-hls.md) for now.


### “FU” CAN bus networking

- **In one line**: CAN (UAVCAN) bus servos designed for multi-node networks, longer harnesses and higher ingress protection.
- **Representative models**: FU-8830-C001.
- **Good for**: multi-joint robots that already run a CAN bus and need centralised wiring and high real-time performance; outdoor or industrial sites with ingress-protection requirements.
- **Not for**: entry projects that just want one TTL cable and a few servos (a CAN transceiver is required, and the ecosystem and tutorials are thinner).
- **Getting started**: you need a CAN transceiver or a CAN-capable debug board — ordinary TTL debug boards and PWM testers are not substitutes. Node address, units and modes follow that model's CAN/UAVCAN documentation; the register table is the [UAVCAN memory table](../reference/parameter/memory-fu.md).

## Interfaces and capabilities

<style>

  .md-typeset .ft-series-compare table { display: table; width: 100%; table-layout: fixed; }

  .md-typeset .ft-series-compare table th { min-width: 0; padding: .6em .5em; }

  .md-typeset .ft-series-compare table td { min-width: 0; padding: .6em .5em; }

  .md-typeset .ft-series-compare table td, .md-typeset .ft-series-compare table th { overflow-wrap: anywhere; }

  .md-typeset .ft-series-compare table th:nth-child(1), .md-typeset .ft-series-compare table td:nth-child(1) { width: 6%; }

  .md-typeset .ft-series-compare table th:nth-child(2), .md-typeset .ft-series-compare table td:nth-child(2) { width: 10%; }

  .md-typeset .ft-series-compare table th:nth-child(3), .md-typeset .ft-series-compare table td:nth-child(3) { width: 10%; }

  .md-typeset .ft-series-compare table th:nth-child(4), .md-typeset .ft-series-compare table td:nth-child(4) { width: 11%; }

  .md-typeset .ft-series-compare table th:nth-child(5), .md-typeset .ft-series-compare table td:nth-child(5) { width: 8%; }

  .md-typeset .ft-series-compare table th:nth-child(6), .md-typeset .ft-series-compare table td:nth-child(6) { width: 8%; }

  .md-typeset .ft-series-compare table th:nth-child(7), .md-typeset .ft-series-compare table td:nth-child(7) { width: 18%; }

  .md-typeset .ft-series-compare table th:nth-child(8), .md-typeset .ft-series-compare table td:nth-child(8) { width: 29%; }

  @media screen and (max-width: 60em) {

    .md-typeset .ft-series-compare table { table-layout: auto; }

    .md-typeset .ft-series-compare table th, .md-typeset .ft-series-compare table td { width: auto; }

  }

</style>

<div class="ft-series-compare" markdown>

| Series | Physical layer  | SDK layer           | Memory table                                    | Positioning      | Angle   | Operating modes                                                                    | Key characteristics                                                                                                                              |
| ------ | --------------- | ------------------- | ----------------------------------------------- | ---------------- | ------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| STS    | Half-duplex TTL | `STS`               | [STS](../reference/parameter/memory-sts.md)     | Magnetic encoder | 0~360°  | Servo, multi-turn, continuous rotation, step                                       | Most models and most documentation; contactless magnetic encoding is wear-free and precise, with one-touch neutral calibration and fast response |
| SCS    | Half-duplex TTL | `SCSCL`             | [SCSCL](../reference/parameter/memory-scscl.md) | Potentiometer    | 0~300°  | Servo, motor mode (continuous rotation)                                            | Good value for the accuracy; suited to simple mechanisms and low-cost projects                                                                   |
| SMS    | RS485           | `SMS`               | [SMS](../reference/parameter/memory-sms.md)     | Magnetic encoder | 0~360°  | Servo, multi-turn, continuous rotation                                             | Differential bus with strong noise immunity and long reach; supports daisy chains and runs stably                                                |
| HD     | Half-duplex TTL | Per model resources | [HLS](../reference/parameter/memory-hls.md)     | Magnetic encoder | 0~360°  | Angle servo, multi-turn, constant speed, constant current (force), step            | Coreless motor + metal gears + dual-shaft output; compact and light, aimed at lightweight biped joints                                           |
| HLS    | Half-duplex TTL | `HLSCL`             | [HLS](../reference/parameter/memory-hls.md)     | Magnetic encoder | 0~360°  | Angle servo, multi-turn (±7 turns), constant speed, constant current (force), step | Software torque limiting and compliant force control; real-time status feedback and bus OTA firmware updates                                     |
| FU     | CAN (UAVCAN)    | UAVCAN              | [UAVCAN](../reference/parameter/memory-fu.md)   | Magnetic encoder | 180°±5° | Servo, constant speed, constant current, motor                                     | CAN real-time performance and fault tolerance; brushless high torque, titanium-gear metal case, IP66, with a PWM backup control interface        |

</div>

!!! info "Angles and modes in this table are family-level overviews"
    Models in the same family may support only some of them. The `FU` angle is taken from a current model (FU-8830-C001); always confirm on the model page. The "Memory table" column points to the family-level guide; `HD` has no dedicated memory-table page yet, and since its register layout is close to HLS the [HLS memory table](../reference/parameter/memory-hls.md) is used as a reference until the model resources confirm otherwise. `SMS` (RS485) and `SMSMB` (MODBUS-RTU) are two different memory tables whose addressing is not interchangeable. The `HD` and `HLS` "step" mode appears only in the official descriptions of some models; whether a given model supports it must be confirmed per model.

## PWM servos

Standard PWM signal control, with a potentiometer or a magnetic encoder sensing position (the official catalog lists 360° magnetic-encoder and feedback models as separate sub-classes); commonly 0~180° (some models 300°/360°, and continuous rotation can be customised). Only the basic servo angle mode, **no bus functionality**, one servo per connection and low cost — used in models and simple prototypes.

- PWM servos are normally driven by periodic pulses and are not addressed by a bus ID. Allowed pulse width, period, voltage, travel and optional feedback vary by model. Bus SDKs and the FD discovery workflow **do not apply** to ordinary PWM models.

## Starter checklist

1. **One mainstream model**: such as ST-3215-C001 — the best-documented choice, where problems are easiest to look up.
2. **A matching debug board**: TTL and SMS (RS485) servos share one `FE-URT2-C001`; FU servos use `FE-SCPC-C003`. See [debug boards and adapters](../tools/adapters.md).
3. **An independent power supply**: do not power servos from a dev board's 5 V pin; allow margin for the model's stall current and the number of servos moving at once.
4. **Common ground**: the debug board, the servo supply and the host controller must share ground.
5. **Walk through [Getting started](../getting-started/index.md)** once, then come back and write your own code.

## Common pitfalls

!!! warning "TTL and RS485 are not interchangeable by changing the baud rate"
    A TTL bus is single-ended half-duplex and needs a TTL debug board or a correctly designed single-wire half-duplex circuit; RS485 is differential and needs an RS485 transceiver with correct A/B wiring. Switching physical layers means switching models or adding the right transceiver/debug circuit — a software baud-rate change cannot do it. RS485 termination and topology must also be designed for the specific system.

!!! warning "Memory tables are not interchangeable"
    These families share a similar packet structure, but **register addresses, data meanings and capabilities are not all the same**. Never apply the STS memory table to SCS or HLS; always check the memory table for your exact model (see [Protocol and parameters](../reference/index.md)).

!!! warning "PWM servos and bus servos are two different things"
    A PWM servo is positioned by periodic pulses, has no bus ID, and cannot return data through a bus SDK. Bus SDKs and the FD discovery workflow do not apply to ordinary PWM models.

!!! note "Record everything before asking for support"
    Full model with suffix, label photo, rated voltage, physical interface, firmware/memory-table revision, current ID, current baud rate, debug-board model and host platform — this lets support staff and AI assistants locate the problem far faster.

## Where to go next

| You want to…                                   | Go here                                          |
| ---------------------------------------------- | ------------------------------------------------ |
| Keep comparing specifications and pick a model | [Product catalog](datasheets/index.md)           |
| Wire it up and get the servo moving            | [Getting started](../getting-started/index.md)   |
| Look up protocols, registers and memory tables | [Protocol and parameters](../reference/index.md) |
| Debug a dead link or an unresponsive servo     | [Troubleshooting](../troubleshooting.md)         |
| Find firmware, software and drivers            | [Downloads](../downloads.md)                     |
