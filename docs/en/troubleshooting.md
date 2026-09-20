# Troubleshooting

Start with the symptom you can observe. Change one variable at a time and record the result.

| Symptom | Start here | Result to establish |
| --- | --- | --- |
| FD / SDK cannot find a bus servo | [Communication](#not-found) | Separate port, wiring and device-response problems |
| Reads work but motion does not | [Motion](#no-motion) | Verify status, mode and target interpretation |
| Jitter, dropouts or intermittent failures | [Stability](#intermittent) | Identify supply, load or communication triggers |
| Device missing after an ID / baud change | [Configuration changes](#changed-id) | Align the device and host settings |
| PWM has no response or unexpected travel | [PWM](#pwm) | Confirm the model's signal requirements and control type |
| Works unloaded but binds after assembly | [Mechanics](#mechanical) | Locate interference, preload or zero mismatch |
| Still unresolved | [Support record](#support) | Prepare a minimal reproduction |

<span id="not-found"></span>

## FD or SDK cannot find the servo

Change one variable at a time:

1. Confirm the correct serial port exists and no other application owns it.
2. Match TTL/RS485 hardware and use a data-capable USB cable.
3. Power the servo from a compliant external supply and maintain ground reference.
4. Check baud rate and duplicate IDs.
5. Verify pinout, A/B or signal wiring and connector integrity.
6. Connect one servo and cross-check FD against the SDK Ping example.

<span id="no-motion"></span>

## Communication works but motion does not

Check supply current limiting, torque enable, operating mode, limits, zero speed/torque settings, series-specific register width/units and protection status. Read status and present position and record returned errors. Stop and support the load before inspecting the mechanism. Confirm power, wiring and clearance, then follow [First Motion](getting-started/first-motion.md). Use the [matching application layer](reference/index.md); do not try blind reset writes.

<span id="intermittent"></span>

## Jitter or intermittent packets

Inspect supply droop, common ground, cable length, connectors, branch topology, baud rate and half-duplex direction timing. Multi-servo startup transients are a frequent power problem.

<span id="changed-id"></span>

## Device disappeared after ID/baud change

Record the old settings, new settings and write result. Stop and support the load, connect only this device and read using the new ID and baud rate. The exact model's documentation determines whether a restart is needed and whether settings persist. If the result is uncertain, preserve the evidence instead of blindly writing more addresses.

## PWM has no response or unexpected travel {#pwm}

1. Check the full model and control type, such as position or continuous rotation. Pulse width is not a universal angle.
2. Verify model-specific pinout, power, ground, signal level, period and pulse range.
3. Inspect the actual controller output waveform and startup sequence, not only the configured values.
4. Check zero, horn and available travel through the [model guide](products/index.md), then follow [PWM Getting Started](getting-started/pwm.md).

A PWM interface does not use bus IDs, baud rates or serial register tables. Obtain missing model requirements before changing the signal.

<span id="mechanical"></span>

## Works unloaded but binds after assembly

Stop and support the load before loosening fasteners or disabling torque.

- Match the physical suffix to drawing / CAD revisions. Check the mounting face, shaft, horn and fasteners.
- Inspect screw length, axial preload, cable bends and interference throughout travel. Do not increase torque to force past a jam.
- Align mechanical zero, software zero, positive direction and soft limits. Commanded travel must remain within the mechanism's clearance.
- Record the position, direction, load and photos at the fault. Compare before and after assembly, and confirm a release method before controlled testing.

Use [Mechanics and Assembly](mechanical/index.md) for the handoff record. Do not estimate critical dimensions from product photos when official drawings or applicable CAD are missing.

<span id="support"></span>

## Prepare a support record

For support, provide full model and label photo, supply voltage/current limit, adapter, wiring photo, ID, baud rate, FD/SDK version, OS, minimal program, exact error and last successful step. Never include credentials or private data.

Copy the record below. Mark unknown fields as “unconfirmed” and irrelevant fields as “not applicable”.

```text
Full model / suffix:
Label photo / firmware / document revision:
Interface / adapter / controller:
Supply settings / current limit / wiring photo:
Bus ID / baud rate, or PWM signal settings:
OS / FD or SDK version:
Mechanism / horn / zero / load:
Last successful step:
Minimal reproduction steps and program:
Expected / actual result / exact error:
Checks already performed and their results:
```
