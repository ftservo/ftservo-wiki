# FD Servo Utility

FD is FEETECH's Windows utility for discovering servos, reading status, changing ID/baud rate, editing model-supported settings and running basic motion tests.

[Official software downloads](https://www.feetechrc.com/service/software.html){ .md-button .md-button--primary }

!!! note
    Versions, download methods and archive passwords may change. Use the official page; this repository does not redistribute binaries of uncertain origin or version.

## Connect

1. Choose a TTL or RS485 adapter to match the servo.
2. Install its USB serial driver and connect it to the PC.
3. With servo power off, connect the bus and external supply and verify polarity.
4. In FD, choose the COM port shown by Windows Device Manager.
5. Select the current baud rate, open the port and start discovery.
6. Stop discovery after the device appears, then select the target.

## Change an ID

```text
one servo only → discover → record original settings → change ID → save
→ power cycle → discover again → verify the new ID
```

After changing baud rate, change FD to the new rate as well. Every device on the final bus needs a unique ID and the same baud rate.

Before writing settings, save original values, distinguish RAM from persistent storage, use the exact-series memory table, follow restart requirements, and keep the first motion slow and unloaded.

If discovery fails, check the COM port, driver, port ownership, baud rate, external power, TTL/RS485 type, pinout, common ground, cable and duplicate IDs. Cross-check one servo with known-good power, cable and adapter.

