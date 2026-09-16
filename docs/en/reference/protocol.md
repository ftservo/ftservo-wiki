# Bus Protocol

FEETECH bus servos communicate with addressed serial packets. SCS/SCSCL, STS, SMS, and HLS share the basic instruction frame, but their physical interface, byte order, and memory tables are not fully interchangeable. Identify the correct application layer on [Series and Interfaces](../products/series.md) before development.

## Packet format

### Instruction packet

```text
0xFF 0xFF ID Length Instruction [Parameter 1 ... Parameter N] Checksum
```

### Status packet

```text
0xFF 0xFF ID Length Status [Data 1 ... Data N] Checksum
```

`Length` counts the instruction/status byte, parameters/data, and checksum. The checksum is:

```text
Checksum = ~(ID + Length + Instruction/Status + Parameters/Data) & 0xFF
```

The broadcast ID is `0xFE`. Broadcast and synchronized writes can address multiple servos. A broadcast command normally has no status response, so it cannot confirm execution by an individual device.

## Instructions

| Instruction | Code | Purpose |
| --- | ---: | --- |
| Ping | `0x01` | Check whether an ID is online |
| Read | `0x02` | Read consecutive addresses |
| Write | `0x03` | Write immediately |
| Reg Write | `0x04` | Stage a write for later execution |
| Reg Action | `0x05` | Execute staged writes |
| Recovery | `0x06` | Recovery operation; support depends on model |
| Reset | `0x0A` | Reset operation; support depends on model |
| Calibration | `0x0B` | Calibration operation; support depends on model |
| Sync Read | `0x82` | Read multiple devices |
| Sync Write | `0x83` | Write multiple devices |

Not every model or firmware implements every instruction. Validate address, length, and response behavior with one device before using a group operation.

## Baud-rate codes

The official SDK uses these codes:

| Code | Baud rate | Code | Baud rate |
| ---: | ---: | ---: | ---: |
| 0 | 1,000,000 | 6 | 57,600 |
| 1 | 500,000 | 7 | 38,400 |
| 2 | 250,000 | 8 | 19,200 |
| 3 | 128,000 | 9 | 14,400 |
| 4 | 115,200 | 10 | 9,600 |
| 5 | 76,800 | 11 | 4,800 |

After changing a servo's baud rate, the host and other devices on the same bus must use the same communication rate.

## Application layer and byte order

| Series | Physical interface | SDK layer | 16-bit serialization |
| --- | --- | --- | --- |
| SCS / SCSCL | Half-duplex TTL | `SCSCL` | High byte first |
| STS | Half-duplex TTL | `SMS_STS` | Low byte first |
| SMS | RS485 | `SMS_STS` | Low byte first |
| HLS | Half-duplex TTL | `HLSCL` | Low byte first |

The byte-order descriptions match the official SDK's `Host2SCS`/`SCS2Host` behavior. Use the read and write functions from the matching application layer to avoid reversing bytes manually.

## Memory tables

The same address can have a different meaning in another application layer:

- [SCSCL Memory Table](memory-scscl.md)
- [SMS / STS Memory Table](memory-sms-sts.md)
- [HLS Memory Table](memory-hls.md)

These pages list addresses defined by the current official SDK headers for integration and quick reference. Model-specific units, ranges, defaults, protection thresholds, and firmware differences remain subject to the individual model page and installed firmware.

## Recommended bring-up

1. Confirm TTL or RS485, supply range, pinout, and common ground.
2. Connect one servo and validate ID, baud rate, and byte order with Ping and read-only registers.
3. Test a RAM write with low speed and a small movement.
4. Only then change persistent settings such as ID, baud rate, mode, and limits.
5. For multi-servo operation, use unique IDs, an independent supply, and adequate wire gauge.

!!! danger "Confirm the exact model before writing"
    Do not interchange SCSCL, SMS/STS, and HLS memory tables. An incorrect persistent write can change the ID, baud rate, operating mode, or protection settings and may cause loss of communication or unexpected movement.

## Official resources

- [FTServo Arduino SDK](https://github.com/ftservo/FTServo_Arduino)
- [FEETECH protocol and memory-table service page](https://www.feetechrc.com/en/letter-of-agreement.html)
- [Debug Boards and Adapters](../tools/adapters.md)
