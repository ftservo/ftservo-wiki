# Debug Boards and Adapters

Debug boards connect a PC or controller to FEETECH servos. Confirm the servo's physical interface, supply voltage, and application before choosing hardware. TTL, RS485, CAN, and PWM are not directly interchangeable.

## Product overview

| Product | Main use | Interfaces and key specifications |
| --- | --- | --- |
| **FE-URT-2** `FE-URT2-C001` | USB to TTL/RS485 bus adapter for bus-servo setup with FD | USB Type-C; 2.54 mm UART header; 55.8 × 36.6 × 11.5 mm; 12.5 g |
| **FE-SCPC-C003** | CAN-bus and PWM-servo programming | USB-A 2.0; USB 5 V ±0.2 V supply; 50 bps–1 Mbps; 55.2 × 22.2 × 9.6 mm |
| **AJ-6A00-C001** | Adjustable DC supply for bench setup | 5–12 V input/output range; 48 × 27 × 15 mm |
| **FE-FRS1-C001** | Dual-mode PWM servo debugging | 4.8–25 V; 39 × 38 × 8 mm |
| **FE-SNIS-C001** | Isolated RS485 to RS485/TTL single-bus conversion | DC 6–24 V; 50 bps–1 Mbps; RS485 input and TTL/RS485 outputs; 47.3 × 31 × 13.2 mm |

[View official product information](https://www.feetechrc.com/serial-port-series-steering-gear_50681){ .md-button .md-button--primary }

## Choose an adapter

| Application | Recommended device |
| --- | --- |
| Discover, configure, and test TTL or RS485 bus servos on Windows | FE-URT-2 |
| Configure CAN-bus products or PWM servos | FE-SCPC-C003 |
| Basic PWM-servo setup and functional testing | FE-FRS1-C001 |
| Isolate RS485 or convert between RS485 and TTL single-bus signals | FE-SNIS-C001 |
| Add a 5–12 V adjustable bench supply | AJ-6A00-C001 |

## Connect FE-URT-2

1. Install the matching driver and FD from the [official software page](https://www.feetechrc.com/service/software.html).
2. Select TTL or RS485 to match the servo and verify the signal pinout.
3. With servo power off, connect signal, ground, and the external supply.
4. Power the servo from a suitable external supply and share ground between the PC adapter and supply.
5. Connect FE-URT-2 to the PC and identify its COM port in Windows Device Manager.
6. Open FD, choose the COM port and current servo baud rate, then discover devices.

!!! warning "Servo power"
    USB supplies the adapter and carries communication. Power the servo from an independent supply sized for the model. Do not route motor load current through the PC's USB port.

## Safe setup

- Turn servo power off before wiring or changing interfaces, and verify polarity and signal pinout.
- Connect one servo for initial setup and ensure that no IDs are duplicated.
- Keep the mechanism clear and begin with a slow, small, unloaded movement.
- Do not power hardware outside the adapter or servo voltage range.
- For unstable communication, check interface type, baud rate, common ground, cabling, supply drop, and termination.

Continue with [FD Servo Utility](fd.md) or [Bus Protocol](../reference/protocol.md).
