# First Motion

This page covers bus servos with a confirmed application layer. Use FD or a matching official SDK example. For a PWM servo, follow [PWM Getting Started](pwm.md).

1. Unload the mechanism and clear the motion envelope.
2. Verify that the returned model/ID is the intended device.
3. Read present position before commanding a distant target.
4. Apply conservative speed and acceleration only if the exact model supports them.
5. Command a very small position offset.
6. Watch current, temperature, sound and feedback; remove actuator power on abnormal behavior.
7. Verify torque-disable/safe-release behavior before increasing travel.

## Raw position is not a universal angle

Resolution, center, range, multi-turn mode and direction encoding vary. Values such as `0`, `512`, `2048` or `4095` have no safe meaning without the exact model's memory table. Confirm raw range, counts per travel/revolution, operating mode, signed direction representation and mechanical soft limits before converting angles.

Continue with the [SDK guide](../sdk/index.md) or [protocol reference](../reference/protocol.md).
