# FD Servo Utility

FD is FEETECH's Windows utility for discovering servos, reading status, changing ID and baud rate, configuring model-supported settings, and running basic motion tests.

[Official software page](https://www.feetechrc.com/service/software.html){ .md-button .md-button--primary }
[Choose an adapter](adapters.md){ .md-button }

The official page currently lists FD 1.9.8.2 Offline and FD 1.9.8.3, together with software for FE-URT and FE-SCPC hardware. Choose software that matches the adapter and servo family. Versions, download methods, and archive passwords are maintained on the official page.

## Connect

1. Choose TTL, RS485, CAN, or PWM setup hardware to match the servo.
2. Install its driver and connect the adapter to the PC.
3. With servo power off, connect signal, ground, and the external supply; verify polarity and pinout.
4. Open FD and select the COM port shown by Windows Device Manager.
5. Select the servo's current baud rate and open the port.
6. Start discovery. Stop it after the device appears, then select the target.

## Change an ID or baud rate

```text
one servo only → discover → record original settings → edit and save
→ power cycle → discover with the new settings → verify
```

Devices on one bus need unique IDs and a common baud rate. After changing baud rate, switch FD to the new value before discovering the servo again.

## Change settings

FD fields depend on the servo model and memory table. Before writing:

- Save the original values or take a screenshot.
- Distinguish runtime fields from persistent settings.
- Open the matching memory table from [Bus Protocol](../reference/protocol.md); do not reuse addresses across families.
- Follow model-specific save and restart instructions after changing mode, limits, calibration, or protection.
- Keep the first movement slow, small, unloaded, and clear of people.

## Device not found

Check the COM port, driver, port ownership, baud rate, external power, interface type, pinout, common ground, cable, and duplicate IDs. If the problem remains, connect only one servo and cross-check with known-good adapter hardware, cable, and power.
