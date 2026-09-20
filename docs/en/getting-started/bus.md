# Bus servo setup

This flow is for a first test with a FEETECH bus servo. For an ordinary PWM servo, use a compatible PWM controller and the exact model's pulse range.

## Prepare

- One identified FEETECH bus servo
- A USB adapter matching its TTL or RS485 interface
- An independent supply meeting the model's voltage and current requirements
- Data-capable USB and bus cables
- A Windows PC for FD, or a Python/Arduino/Linux/STM32 development device

[Choose another setup route](index.md) · [PWM servo setup](pwm.md)

## First power-up

1. Remove the mechanical load and connect only one servo.
2. With power off, verify polarity, signal and ground pins.
3. Connect the adapter to the computer, then enable servo power.
4. Confirm the model's application layer and discovery procedure, then use matching FD / SDK Ping support at documented candidate baud rates.
5. Record the original ID and baud rate. Keep only this servo connected while changing its ID.
6. Verify the responding device's identity and stable status reads. Confirm mode, units, allowed range and mechanical clearance, then follow [First Motion](first-motion.md) for a small movement test.

!!! danger
    Do not power the motor from a computer USB port. Reverse polarity, overvoltage, prolonged stall, collisions and duplicate IDs can damage the servo, adapter or computer.

Next: [Power and wiring](wiring.md) · [FD](../tools/fd.md) · [First motion](first-motion.md) · [SDKs](../sdk/index.md)

