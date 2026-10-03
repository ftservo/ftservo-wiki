# Potentiometer SCSCL Servo - Memory Table

For SCS/SCSCL half-duplex TTL series servos. Two-byte fields are transmitted with the **high byte first**.

<style>
  .md-typeset table:not([class]) { display: table; width: 100%; table-layout: fixed; }
  .md-typeset table:not([class]) th { min-width: 0; padding: .6em .4em; }
  .md-typeset table:not([class]) td { min-width: 0; padding: .6em .4em; }
  .md-typeset table:not([class]) td, .md-typeset table:not([class]) th { overflow-wrap: anywhere; }
  .md-typeset table:not([class]) th:nth-child(1), .md-typeset table:not([class]) td:nth-child(1) { width: 46px; }
  .md-typeset table:not([class]) th:nth-child(2), .md-typeset table:not([class]) td:nth-child(2) { width: 46px; }
  .md-typeset table:not([class]) th:nth-child(3), .md-typeset table:not([class]) td:nth-child(3) { width: 54px; }
  .md-typeset table:not([class]) th:nth-child(4), .md-typeset table:not([class]) td:nth-child(4) { width: 40px; }
  .md-typeset table:not([class]) th:nth-child(5), .md-typeset table:not([class]) td:nth-child(5) { width: 72px; }
  .md-typeset table:not([class]) th:nth-child(6), .md-typeset table:not([class]) td:nth-child(6) { width: 30px; }
  .md-typeset table:not([class]) th:nth-child(7), .md-typeset table:not([class]) td:nth-child(7) { width: 50px; }
  .md-typeset table:not([class]) th:nth-child(8), .md-typeset table:not([class]) td:nth-child(8) { width: 56px; }
  @media screen and (max-width: 40em) {
    .md-typeset table:not([class]) { table-layout: auto; }
    .md-typeset table:not([class]) th, .md-typeset table:not([class]) td { width: auto; }
  }
</style>

## 1 Servo Communication Protocol

Servos use the FT-SCS proprietary protocol. The default baud rate is 1 Mbps or 500 kbps over a TTL single-wire bus, 8 data bits, no parity, 1 stop bit; configurable baud rate range 38400~1 Mbps (500 kbps), default communication address (station number) 1.

[FT-SCS proprietary protocol](../protocol/index.md)

## 2 Servo Memory Table Definition

If a function address uses two bytes of data, the high byte is at the leading address and the low byte at the following address

### 2.1 Version Information

| Address (DEC) | Address (HEX) | Function | Bytes | Initial value | Access | Range | Unit | Description |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0x00 | Firmware major version | 1 | – | R |  |  |  |
| 1 | 0x01 | Firmware minor version | 1 | – | R |  |  |  |
| 2 | 0x02 | END | 1 | 1 | R |  |  | 1 indicates the big-endian storage structure |
| 3 | 0x03 | Servo major version | 1 | – | R |  |  |  |
| 4 | 0x04 | Servo minor version | 1 | – | R |  |  |  |

### 2.2 EPROM Configuration

| Address (DEC) | Address (HEX) | Function | Bytes | Initial value | Access | Range | Unit | Description |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | 0x05 | Servo ID | 1 | 1 | R/W | 0~253 | ID | Unique main ID on the bus |
| 6 | 0x06 | Baud rate | 1 | 0 | R/W | 0~7 | None | 0-7 correspond to baud rates: 1000000(0), 500000(1), 250000(2), 128000(3), 115200(4), 76800(5), 57600(6), 38400(7) |
| 7 | 0x07 | Undefined | 1 | – | R/W | – |  | ) |
| 8 | 0x08 | Response status level | 1 | 1 | R/W | 0~1 | None | 0: no response packet for instructions other than READ and PING; 1: response packet for all instructions |
| 9 | 0x09 | Minimum angle limit | 2 | 20 | R/W | 0~1023 | Step | Set the minimum running angle limit; the value must be smaller than the maximum angle limit, minimum angle limit = maximum angle limit = 0 enters motor mode |
| 11 | 0x0B | Maximum angle limit | 2 | 1003 | R/W | 1~1023 | Step | Set the maximum running angle limit; the value must be larger than the minimum angle limit, minimum angle limit = maximum angle limit = 0 enters motor mode |
| 13 | 0x0D | Maximum temperature limit | 1 | 70 | R/W | 0~100 | °C |  |
| 14 | 0x0E | Maximum input voltage | 1 | – | R/W | 0~254 | 0.1V | Maximum input voltage = minimum input voltage = 0 means voltage feedback is disabled |
| 15 | 0x0F | Minimum input voltage | 1 | 40 | R/W | 0~254 | 0.1V | Maximum input voltage = minimum input voltage = 0 means voltage feedback is disabled |
| 16 | 0x10 | Maximum torque | 2 | 1000 | R/W | 0~1000 | 0.1% | Written to address 48 (torque limit) at power-on |
| 18 | 0x12 | Phase | 1 | – | R/W | 0~254 | None | Special function byte; do not modify unless specifically required |
| 19 | 0x13 | Unload condition | 1 | – | R/W | 0~254 | None | Set bit to 1 to enable the corresponding protection, set bit to 0 to disable it |
| 20 | 0x14 | LED alarm condition | 1 | – | R/W | 0~254 | None | Set bit to 1 to enable the flashing LED alarm, set bit to 0 to disable the flashing LED alarm |
| 21 | 0x15 | Position loop P (proportional) coefficient | 1 | – | R/W | 0~254 | None | Proportional coefficient of the motor |
| 22 | 0x16 | Position loop D (derivative) coefficient | 1 | – | R/W | 0~254 | None | Derivative coefficient of the motor |
| 23 | 0x17 | Undefined | 1 | – | R/W | – | – |  |
| 24 | 0x18 | Minimum startup torque | 2 | – | R/W | 0~1000 | 0.1% | Sets the minimum output startup torque of the servo |
| 26 | 0x1A | Positive deadband | 1 | 1 | R/W | 0~16 | Step | The minimum unit is one minimum resolution angle |
| 27 | 0x1B | Negative deadband | 1 | 1 | R/W | 0~16 | Step | The minimum unit is one minimum resolution angle |
| 28~36 | 0x1C~0x24 | Undefined | 1 | – | R/W | – | – |  |
| 37 | 0x25 | Holding torque | 1 | 20 | R/W | 0~254 | 1% | Output torque after entering overload protection, e.g. 20 means 20% of the maximum torque |
| 38 | 0x26 | Protection time | 1 | 200 | R/W | 0~254 | 10ms | Duration for which the current load output stays above the overload torque, e.g. 200 means 2 seconds, maximum 2.5 seconds |
| 39 | 0x27 | Overload torque | 1 | 80 | R/W | 0~254 | 1% | Maximum torque threshold that starts the overload protection timer, e.g. 80 means 80% of the maximum torque |

### 2.3 SRAM Control

| Address (DEC) | Address (HEX) | Function | Bytes | Initial value | Access | Range | Unit | Description |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 40 | 0x28 | Torque switch | 1 | 0 | R/W | 0~2 | None | Write 0: torque output off / free state; write 1: torque output on; write 2: damping state |
| 41 | 0x29 | Undefined | 1 | – | R/W | – | – |  |
| 42 | 0x2A | Goal position | 2 | 0 | R/W | 0~1023 | Step | Each step is one minimum resolution angle; absolute position control; the maximum corresponds to the maximum effective angle |
| 44 | 0x2C | Running time | 2 | 0 | R/W | 0~9999/-1000~1000 | 1ms/0.1% | Time to move from the current position to the goal position; effective when the running speed is 0; in motor mode the running time sets the motor output PWM duty cycle, BIT10 is the direction bit |
| 46 | 0x2E | Running speed | 2 | Factory default maximum speed | R/W | 0~1000 | Step/s | Number of steps moved per unit time (per second) |
| 48 | 0x30 | Lock flag | 1 | 1 | R/W | 0~1 | None | Write 0 to close the write lock: values written to EPROM addresses persist after power-off; write 1 to open the write lock: values written to EPROM addresses do not persist |
| 49~56 | 0x32~0x36 | Undefined | 1 |  |  |  |  |  |

### 2.4 SRAM Feedback

| Address (DEC) | Address (HEX) | Function | Bytes | Initial value | Access | Range | Unit | Description |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 56 | 0x38 | Present position | 2 | – | R | – | Step | Current position in steps; each step is one minimum resolution angle; absolute position control, the maximum value corresponds to the maximum effective angle |
| 58 | 0x3A | Present speed | 2 | – | R | – | Step/s | Rotational speed of the motor, steps moved per unit time (per second) |
| 60 | 0x3C | Present load | 2 | – | R | – | 0.1% | Duty cycle of the output driving the motor; BIT10 is the direction bit |
| 62 | 0x3E | Present voltage | 1 | – | R | – | 0.1V | Current working voltage of the servo |
| 63 | 0x3F | Present temperature | 1 | – | R | – | °C | Current internal working temperature of the servo |
| 64 | 0x40 | Async write flag | 1 | 0 | R | – | None | Flag used with the async write instruction |
| 65 | 0x41 | Servo status | 1 | 0 | R | – | None | A bit set to 1 indicates the corresponding error |
| 66 | 0x42 | Moving flag | 1 | 0 | R | – | None | 1 while the servo is moving, 0 when the target is reached and the servo stops; stays 0 when no updated goal position is written |

### 2.5 Factory Parameters

| Address (DEC) | Address (HEX) | Function | Bytes | Initial value | Access | Range | Unit | Description |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 78 | 0x4E | PWM mode maximum step | 1 | 20 | R | – | None |  |
| 79 | 0x50 | Moving speed threshold*50 | 1 | 1 | R | – | None |  |
| 80 | 0x51 | DTs(ms) | 1 | 20 | R | – | None |  |
| 81 | 0x52 | Minimum speed limit*50 | 1 | 1 | R | – | None |  |
| 82 | 0x53 | Maximum speed limit*50 | 1 | – | R | – | None |  |
| 83 | 0x54 | Acceleration | 1 | 20 | R | – | None |  |

## 3 Special Byte Explanation

### 3.1 Servo Phase

**Bit (weight)**: Description

- BIT0 (1): Drive direction phase; (0) forward, (1) reverse
- BIT1 (2): ----
- BIT2 (4): ----
- BIT3 (8): Speed mode; (0) speed 0 means stop, (1) speed 0 means maximum speed
- BIT4 (16): ----
- BIT5 (32): PWM phase, (0) in phase, (1) inverted
- BIT6 (64): Voltage mode, (0) 1.5K low-voltage sampling, (1) 1K high-voltage sampling
- BIT7 (128): ----

!!! warning "Note"
    If multiple bits are set at the same time, the phase value is the sum of the bit values.

### 3.2 Servo Status

Servo status: 0 means normal, 1 means abnormal

**Bit (weight)**: Description

- BIT0 (1): Voltage status
- BIT1 (2): ----
- BIT2 (4): Temperature status
- BIT3 (8): ----
- BIT4 (16): ----
- BIT5 (32): Load status
- BIT6 (64): ----
- BIT7 (128): ----

!!! warning "Note"
    If multiple statuses occur at the same time, the status value is the sum of the bit values. Example: over-voltage/under-voltage together with servo overheating gives a status value of 4+1=5;

### 3.3 Unload Condition

Unload condition: 0 means off, 1 means on

**Bit (weight)**: Description

- BIT0 (1): Voltage protection
- BIT1 (2): ----
- BIT2 (4): Overheat protection
- BIT3 (8): ----
- BIT4 (16): ----
- BIT5 (32): Load overload
- BIT6 (64): ----
- BIT7 (128): ----

!!! warning "Note"
    If multiple bits are set at the same time, the unload condition value is the sum of the bit values. Example: with voltage protection and overheat protection enabled together, the unload condition value is 4+1=5;

### 3.4 LED Alarm Condition

LED alarm condition: 0 means off, 1 means on

**Bit (weight)**: Description

- BIT0 (1): Voltage alarm
- BIT1 (2): ----
- BIT2 (4): Overheat alarm
- BIT3 (8): ----
- BIT4 (16): ----
- BIT5 (32): Load overload alarm
- BIT6 (64): ----
- BIT7 (128): ----

!!! warning "Note"
    If multiple bits are set at the same time, the LED alarm condition value is the sum of the bit values. Example: with the voltage alarm and the overheat alarm enabled together, the alarm condition value is 4+1=5;

!!! warning "Do not reuse addresses across families"
    Other application layers may use the same address with a different meaning. Return to [Bus Protocol](../protocol/index.md) and select the matching memory table.

## Source Definition

- [Official `SCSCL` header](https://github.com/ftservo/FTServo_Arduino/blob/main/src/SCSCL.h)
