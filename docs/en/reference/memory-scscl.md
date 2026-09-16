# SCSCL Memory Table

For SCS/SCSCL half-duplex TTL servos. A 16-bit value is serialized high byte first.

The addresses below match the `SCSCL` application layer in the official FEETECH SDK. Read and write two-byte values with this layer's byte order.

## Read-only persistent area

| Address | Length | Name | Access |
| ---: | ---: | --- | --- |
| 3–4 | 2 bytes | Model/version identifier | Read only |

## Writable persistent area

| Address | Length | Name | Access |
| ---: | ---: | --- | --- |
| 5 | 1 byte | Device ID | Read/write |
| 6 | 1 byte | Baud-rate code | Read/write |
| 9–10 | 2 bytes | Minimum angle limit | Read/write |
| 11–12 | 2 bytes | Maximum angle limit | Read/write |
| 26 | 1 byte | Clockwise deadband | Read/write |
| 27 | 1 byte | Counterclockwise deadband | Read/write |

## Writable runtime area

| Address | Length | Name | Access |
| ---: | ---: | --- | --- |
| 40 | 1 byte | Torque enable | Read/write |
| 42–43 | 2 bytes | Goal position | Read/write |
| 44–45 | 2 bytes | Goal time | Read/write |
| 46–47 | 2 bytes | Goal speed | Read/write |
| 48 | 1 byte | Lock flag | Read/write |

## Read-only status area

| Address | Length | Name | Access |
| ---: | ---: | --- | --- |
| 56–57 | 2 bytes | Present position | Read only |
| 58–59 | 2 bytes | Present speed | Read only |
| 60–61 | 2 bytes | Present load | Read only |
| 62 | 1 byte | Present voltage | Read only |
| 63 | 1 byte | Present temperature | Read only |
| 66 | 1 byte | Moving status | Read only |
| 69–70 | 2 bytes | Present current | Read only |

## Usage notes

- Addresses are decimal. A two-byte field occupies the listed start address and the next address.
- Persistent fields change device configuration. Record the original value and connect only one servo before changing ID, baud rate, mode, limits, or offset.
- The table covers commonly exposed addresses in the current official SDK. Units, ranges, defaults, and write conditions depend on the exact model and firmware.
- Read the model identifier and current settings before writing. Keep the first movement slow, small, and unloaded.

!!! warning "Do not reuse addresses across families"
    The same address can mean something else in another application layer. Return to [Bus Protocol](protocol.md) and select the matching memory table.

## Source definition

- [Official `SCSCL` header](https://github.com/ftservo/FTServo_Arduino/blob/main/src/SCSCL.h)
