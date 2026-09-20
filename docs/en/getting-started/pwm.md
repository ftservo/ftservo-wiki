# PWM servo setup

[Choose a setup route](index.md) · [Bus servo setup](bus.md)

Use this path only for an exact model documented as PWM-controlled. PWM does not use FD serial-bus discovery, device IDs, baud rates or SCS/STS/HLS registers.

## Confirm these inputs before power-up

| Required information | Confirm |
| --- | --- |
| Full model and behavior | Suffix, position-versus-speed control and document revision |
| Power and connector | Allowed supply range, current needs, connector orientation, pinout and shared ground |
| Control signal | Voltage level, period, pulse limits, neutral/stop setting and signal-loss behavior |
| Mechanical boundaries | Permitted travel, direction, clearance, load condition and power disconnect |

Check the [model resource table](../products/index.md). Without documented period or pulse limits, do not use another servo's settings or sweep an assumed full range.

## First validation

1. Wire with power off and PWM disabled. Confirm polarity, shared ground and signal voltage from the formal documents.
2. Disconnect linkages/load, leave clearance for possible start-up movement and arrange an immediate power disconnect.
3. Configure the confirmed period and neutral/stop setting. Do not equate angle zero with motor stop.
4. Apply only a confirmed minimal test signal and check the expected position/speed response.
5. Make a small change within documented bounds and record direction, response and faults. Establish software limits before attaching the mechanism.

## Completion record

Record the full model suffix, controller/toolchain, supply, pinout revision, actual period/pulse settings, unloaded result, stop method and date. A shared PWM library's defaults are not model-specific validation.

[Signal present but no response](../troubleshooting.md#pwm) · [Assembly and zero handoff](../mechanical/index.md)
