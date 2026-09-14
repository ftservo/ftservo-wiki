# Power and Wiring

```text
Computer USB ── USB adapter ── TTL/RS485 bus ── servo
                              │                 │
                              └── ground ───────┤
External regulated supply (+/-) ────────────────┘
```

USB carries communication; an external supply powers the actuator. Always use the adapter and servo manuals for pin order—wire colors alone are not a specification.

## Power

- Stay inside the exact model's voltage range.
- Budget current for simultaneous peak loads with margin.
- Thin/long wiring and poor connectors cause voltage drop, resets and packet errors.
- Group power for larger systems, add appropriate local decoupling and maintain a reliable common reference.
- Disconnect power before inserting or rewiring devices.

## Bus rules

- IDs must be unique and baud rates equal on one bus.
- Match TTL devices to TTL hardware and RS485 devices to RS485 hardware.
- Avoid long star branches and loose connectors; engineer RS485 termination for link length and baud rate.

| Check | Confirm |
| --- | --- |
| Model | Full suffix matches the label |
| Voltage | Supply matches the exact datasheet |
| Pins | V+, GND and signal/A/B are correct |
| Interface | TTL-to-TTL or RS485-to-RS485 |
| Mechanics | Shaft can move without collision or pinch risk |
| Bus | Only one new servo for the first test |

