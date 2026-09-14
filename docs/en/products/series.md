# Series and Interfaces

## Bus servo families

| Series | Physical layer | SDK layer | Typical positioning |
| --- | --- | --- | --- |
| SCS / SCSCL | Half-duplex TTL | `SCSCL` | Common position bus servos; verify model resolution |
| STS | Half-duplex TTL | `SMS_STS` | Many magnetic-encoder, high-resolution or continuous models |
| SMS | RS485 | `SMS_STS` | Differential communication for more demanding wiring |
| HLS | Half-duplex TTL | `HLSCL` | HLS-specific application layer and memory table |

Packet formats can be related while register addresses and capabilities differ. Never apply one series' memory table to another.

## PWM servos

PWM servos normally receive position pulses without a bus ID. Allowed pulse width, period, voltage, travel and optional feedback vary by exact model. FD discovery and bus SDKs do not apply to ordinary PWM models.

## TTL and RS485 are not interchangeable

- TTL is commonly single-ended half-duplex and needs a compatible adapter or direction-control circuit.
- RS485 is differential and needs an RS485 transceiver with correct A/B wiring.
- Software baud-rate changes cannot convert one physical layer to the other.
- Keep controller, adapter, servo and power grounds referenced as specified; design RS485 topology and termination for the actual link.

Before support or AI development, record the full model, label, rated voltage, interface, firmware/memory-table version, ID, baud rate, adapter and host platform.

