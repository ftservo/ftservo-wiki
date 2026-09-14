# Troubleshooting

## FD or SDK cannot find the servo

Change one variable at a time:

1. Confirm the correct serial port exists and no other application owns it.
2. Match TTL/RS485 hardware and use a data-capable USB cable.
3. Power the servo from a compliant external supply and maintain ground reference.
4. Check baud rate and duplicate IDs.
5. Verify pinout, A/B or signal wiring and connector integrity.
6. Connect one servo and cross-check FD against the SDK Ping example.

## Communication works but motion does not

Check supply current limiting, torque enable, operating mode, limits, zero speed/torque settings, series-specific register width/units and protection status. Read status and present position before an unloaded small move.

## Jitter or intermittent packets

Inspect supply droop, common ground, cable length, connectors, branch topology, baud rate and half-duplex direction timing. Multi-servo startup transients are a frequent power problem.

## Device disappeared after ID/baud change

Power cycle with only that device connected and search at the new baud rate. If the result is uncertain, preserve the evidence instead of blindly writing more addresses.

For support, provide full model and label photo, supply voltage/current limit, adapter, wiring photo, ID, baud rate, FD/SDK version, OS, minimal program, exact error and last successful step. Never include credentials or private data.

