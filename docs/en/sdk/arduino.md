# Arduino / ESP32 SDK

Official repository: [ftservo/FTServo_Arduino](https://github.com/ftservo/FTServo_Arduino). It supports Arduino and ESP32 and is available through Arduino Library Manager.

In Arduino IDE, search Library Manager for `FTServo`, install it, and open an example matching the target series. A complete Wiki checkout also provides `sdk/FTServo_Arduino` for a local library or PlatformIO dependency.

Bus communication is normally half-duplex. The adapter/transceiver must manage the physical layer and direction correctly. Never connect MCU pins directly to an incompatible voltage or to RS485 A/B without a transceiver.

- Use `SCSCL` examples for SCS.
- Use `SMS_STS` examples for STS and SMS.
- Use `HLSCL` examples for HLS.
- Replace the serial object, ID, baud rate and targets with verified configuration.

On ESP32, keep USB logging and the servo bus on separate hardware UARTs when practical. Verify read-only Ping first, then a small unloaded move. Do not copy raw limits or register addresses from a different model.

