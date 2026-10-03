# Magnetically Encoded HLS Servo - Memory Table

For HLS half-duplex TTL series servos. Two-byte fields are transmitted with the **low byte first**.

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

Servos use the FT-SCS proprietary protocol. Factory serial defaults: baud rate 1 Mbps, 8 data bits, no parity, 1 stop bit; configurable baud rate range 38400~1 Mbps, default communication address (station number) 1.

For the full frame format and instruction set, see [Bus Protocol](../protocol/index.md).

## 2 Servo Memory Table Definition

If a function address uses two bytes of data, the low byte is at the leading address and the high byte at the following address.

### 2.1 Version Information

| Address (DEC) | Address (HEX) | Function | Bytes | Initial value | Access | Range | Unit | Description |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0x00 | Firmware major version | 1 | 3 | R |  |  |  |
| 1 | 0x01 | Firmware minor version | 1 | – | R | 40 ~ 59 |  |  |
| 2 | 0x02 | END | 1 | 0 | R |  |  | 0 indicates little-endian storage structure |
| 3 | 0x03 | Servo major version | 1 | 10 | R |  |  |  |
| 4 | 0x04 | Servo minor version | 1 | – | R |  |  |  |

### 2.2 EPROM Configuration

| Address (DEC) | Address (HEX) | Function | Bytes | Initial value | Access | Range | Unit | Description |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | 0x05 | Main ID | 1 | 1 | R/W | 0~253 | ID | Unique main ID on the bus (first identifier) |
| 6 | 0x06 | Baud rate | 1 | 0 | R/W | 0~7 | None | 0-7 correspond to baud rates: 1000000(0), 500000(1), 250000(2), 128000(3), 115200(4), 76800(5), 57600(6), 38400(7) |
| 7 | 0x07 | Secondary ID | 1 | 0 | R/W | 0~253 | ID | Secondary ID (second identifier). It applies to write, abnormal write, abnormal execution and sync-write instructions; writing to the main ID also updates the secondary ID |
| 8 | 0x08 | Response status level | 1 | 1 | R/W | 0~1 | None | 0: no response packet for instructions other than READ and PING; 1: response packet for all instructions |
| 9 | 0x09 | Minimum angle limit | 2 | 0 | R/W | 0~4094 | 0.087° | 0 in multi-turn absolute position control |
| 11 | 0x0B | Maximum angle limit | 2 | 4095 | R/W | 1~4095 | 0.087° | 0 in multi-turn absolute position control |
| 13 | 0x0D | Maximum temperature limit | 1 | 70 | R/W | 0~100 | °C |  |
| 14 | 0x0E | Maximum input voltage | 1 | – | R/W | 0~254 | 0.1V |  |
| 15 | 0x0F | Minimum input voltage | 1 | 40 | R/W | 0~254 | 0.1V |  |
| 16 | 0x10 | Maximum torque | 2 | 980 | R/W | 0~1000 | 0.1% | Written to address 48 (torque limit) at power-on |
| 18 | 0x12 | Phase | 1 | – | R/W | 0~254 | None | Special function byte; do not modify unless specifically required |
| 19 | 0x13 | Unload condition | 1 | – | R/W | 0~254 | None | Set bit to 1 to enable the corresponding protection, set bit to 0 to disable it |
| 20 | 0x14 | LED alarm condition | 1 | – | R/W | 0~254 | None | Set bit to 1 to enable the flashing alarm, set bit to 0 to disable it |
| 21 | 0x15 | Position loop P (proportional) coefficient | 1 | – | R/W | 0~254 | None | Written to address 50 (Kp) at power-on |
| 22 | 0x16 | Position loop D (derivative) coefficient | 1 | – | R/W | 0~254 | None | Written to address 51 (Kd) at power-on |
| 23 | 0x17 | Position loop I (integral) coefficient | 1 | 0 | R/W | 0~254 | None | Written to address 52 (Ki) at power-on |
| 24 | 0x18 | Minimum startup torque | 1 | – | R/W | 0~254 | 0.1% | Sets the minimum output startup torque of the servo |
| 25 | 0x19 | Integral limit | 1 | 0 | R/W | 0~254 | None | Maximum integral = limit × 4; 0 disables the integral limit; effective in position mode 0 and mode 4 |
| 26 | 0x1A | Positive deadband | 1 | 1 | R/W | 0~16 | 0.087° | The minimum unit is one minimum resolution angle |
| 27 | 0x1B | Negative deadband | 1 | 1 | R/W | 0~16 | 0.087° | The minimum unit is one minimum resolution angle |
| 28 | 0x1C | Protection current | 2 | – | R/W | 0~2047 | 6.5mA | Written to address 44 (goal current) at power-on |
| 30 | 0x1E | Angle resolution | 1 | 1 | R/W | 1~128 | None | Magnification factor of the sensor's minimum resolution angle |
| 31 | 0x1F | Position offset | 2 | 0 | R/W | -4095~4095 | 0.087° | BIT15 is the direction bit; the remaining bits cover 0-4095 |
| 33 | 0x21 | Operating mode | 1 | 0 | R/W | 0~3 | None | 0: position servo mode (position + current limit); 1: constant-speed motor mode (constant speed + current limit); 2: constant-current motor mode (current limit, speed not controllable); 3: PWM open-loop speed mode |
| 34 | 0x22 | Current loop P (proportional) coefficient | 1 | – | R/W |  | None |  |
| 35 | 0x23 | Current loop I (integral) coefficient | 1 | – | R/W |  | None |  |
| 36 | 0x24 | Undefined | 1 | – | R/W | – | – | – |
| 37 | 0x25 | Velocity loop P (proportional) coefficient | 1 | – | R/W | 0~254 | None | Speed-loop proportional coefficient in constant-speed motor mode (mode 1) |
| 38 | 0x26 | Overcurrent protection time | 1 | 200 | R/W | 0~254 | 10ms |  |
| 39 | 0x27 | Velocity loop I (integral) coefficient | 1 | – | R/W | 0~254 | None | Speed-loop integral coefficient in constant-speed motor mode (mode 1) |

### 2.3 SRAM Control

| Address (DEC) | Address (HEX) | Function | Bytes | Initial value | Access | Range | Unit | Description |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 40 | 0x28 | Torque switch | 1 | 0 | R/W | 0~2 | None | Write 0: torque output off / free state; write 1: torque output on; write 2: damping output |
| 41 | 0x29 | Acceleration | 1 | 0 | R/W | 0~254 | 8.7°/s² | Run acceleration/deceleration of the servo; 0 means maximum acceleration |
| 42 | 0x2A | Goal position | 2 | 0 | R/W | -32767~32767 | 0.087° | Absolute position control; the maximum corresponds to the maximum effective angle; BIT15 is the direction bit |
| 44 | 0x2C | Goal current | 2 | Protection current (28) | R/W | -2047~2047 | 6.5mA | In modes other than mode 3, this value limits the maximum running current of the motor; in constant-current mode (mode 2) BIT15 is the current direction bit; in PWM open-loop speed mode (mode 3) the write range is -1000~1000 and BIT10 is the direction bit |
| 46 | 0x2E | Running speed | 2 | Factory default maximum speed | R/W | -32767~32767 | 0.732RPM | Controls the maximum running speed of the motor; 0 means stop; in constant-speed mode (1) BIT15 is the speed direction bit |
| 48 | 0x30 | Torque limit | 2 | Maximum torque (16) | R/W | 0~1000 | 0.1% | Can be modified to control the stall torque output |
| 50 | 0x32 | Kp | 1 | Position loop P coefficient (21) / velocity loop P coefficient (37) | R/W | 0~254 | None | Position servo mode: proportional coefficient of the position loop (1/8); constant-speed motor mode: proportional coefficient of the speed loop |
| 51 | 0x33 | Kd | 1 | Position loop D coefficient (22) | R/W | 0~254 | None | Position servo mode: derivative coefficient of the position loop (1/4); constant-speed motor mode: invalid |
| 52 | 0x34 | Ki | 1 | Velocity loop I coefficient (39) | R/W | 0~254 | None | Position servo mode: invalid; constant-speed motor mode: integral coefficient of the speed loop |
| 53 | 0x35 | Undefined | 1 | – | R/W | – | – |  |
| 54 | 0x36 | Undefined | 1 | – | R/W | – | – |  |
| 55 | 0x37 | Lock flag | 1 | 1 | R/W | 0~1 | None | Write 0 to close the write lock: values written to EPROM addresses persist after power-off; write 1 to open the write lock: values written to EPROM addresses do not persist |

### 2.4 SRAM Feedback

| Address (DEC) | Address (HEX) | Function | Bytes | Initial value | Access | Range | Unit | Description |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 56 | 0x38 | Present position | 2 | – | R | – | 0.087° | Absolute position feedback of the servo; BIT15 is the direction bit |
| 58 | 0x3A | Present speed | 2 | – | R | – | 0.732RPM | Rotational speed of the motor; BIT15 is the direction bit |
| 60 | 0x3C | Present load | 2 | – | R | – | 0.1% | Duty cycle of the output driving the motor; BIT10 is the direction bit |
| 62 | 0x3E | Present voltage | 1 | – | R | – | 0.1V | Current working voltage of the servo |
| 63 | 0x3F | Present temperature | 1 | – | R | – | °C | Current internal working temperature of the servo |
| 64 | 0x40 | Async write flag | 1 | 0 | R | – | None | Flag used with the async write instruction |
| 65 | 0x41 | Servo status | 1 | 0 | R | – | None | A bit set to 1 indicates the corresponding error; see Special Byte Explanation for details |
| 66 | 0x42 | Moving flag | 1 | 0 | R | – | None | BIT0: 1 while the servo is moving (above the moving speed threshold), 0 when stopped; BIT1: 1 while the servo is moving, 0 when the target is reached and the servo stops, stays 0 when no new goal position is written |
| 67 | 0x43 | Goal position | 2 | – | R | – | 0.087° | Current goal position |
| 69 | 0x45 | Present current | 2 | – | R | – | 6.5mA | Motor phase current feedback; BIT15 is the current direction bit |
| 71 | 0x47 | Undefined | 2 | – | R | – | – |  |
| 73 | 0x49 | Current offset | 2 | – | R | – | – | Current zero-point offset |

### 2.5 Factory Parameters

| Address (DEC) | Address (HEX) | Function | Bytes | Initial value | Access | Range | Unit | Description |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 77 | 0x4D | vFk(*10) | 1 | – | R | – | – | – |
| 78 | 0x4E | vKgI | 1 | – | R | – | – | – |
| 79 | 0x4F | pFk(*10) | 1 | – | R | – | – | – |
| 80 | 0x50 | Moving speed threshold | 1 | – | R | – | – | – |
| 81 | 0x51 | DTs(ms) | 1 | – | R | – | – | – |
| 82 | 0x52 | eFk(*10) | 1 | – | R | – | – | – |
| 83 | 0x53 | Vk(ms) | 1 | – | R | – | – | – |
| 84 | 0x54 | Maximum speed limit | 1 | – | R | – | – | – |
| 85 | 0x55 | Acceleration limit | 1 | – | R | – | – | – |
| 86 | 0x56 | Acceleration multiplier | 1 | – | R | – | – | – |

## 3 Special Byte Explanation

### 3.1 Servo Phase

**Bit (weight)**: Description

- BIT0 (1): Servo phase (firmware version <= 3.41); magnetic encoder support (firmware version >= 3.44): (0: AS5600, 1: MT6701)
- BIT1 (2): Current feedback direction phase; (0) forward, (1) reverse
- BIT2 (4): Driver bridge direction phase; (0) forward, (1) reverse
- BIT3 (8): Speed direction phase (firmware version <= 3.41)
- BIT4 (16): Angle feedback mode; (0) single-turn angle feedback, (1) full-angle feedback
- BIT5 (32): Driver bridge configuration, (0) independent H-bridge, (1) integrated H-bridge
- BIT6 (64): PWM frequency, (0) 24kHz, (1) 16kHz
- BIT7 (128): Position feedback direction phase, (0) forward, (1) reverse

!!! warning "Note"
    If multiple bits are set at the same time, the phase value is the sum of the bit values. Example: with an original phase value of 0, if the servo runs in reverse, the phase value is 128+4+2=134;

### 3.2 Servo Status

Servo status: 0 means normal, 1 means abnormal

**Bit (weight)**: Description

- BIT0 (1): Voltage status
- BIT1 (2): Magnetic encoder status
- BIT2 (4): Temperature status
- BIT3 (8): Current status
- BIT4 (16): -----
- BIT5 (32): -----
- BIT6 (64): -----
- BIT7 (128): -----

!!! warning "Note"
    If multiple statuses occur at the same time, the status value is the sum of the bit values. Example: over-voltage/under-voltage together with servo overheating gives a status value of 4+1=5;

### 3.3 Unload Condition

Unload condition: 0 means off, 1 means on

**Bit (weight)**: Description

- BIT0 (1): Voltage protection
- BIT1 (2): Magnetic encoder protection
- BIT2 (4): Overheat protection
- BIT3 (8): Overcurrent protection
- BIT4 (16): -----
- BIT5 (32): -----
- BIT6 (64): -----
- BIT7 (128): -----

!!! warning "Note"
    If multiple bits are set at the same time, the unload condition value is the sum of the bit values. Example: with voltage protection and overheat protection enabled together, the unload condition value is 4+1=5;

### 3.4 LED Alarm Condition

Alarm condition: 0 means off, 1 means on

**Bit (weight)**: Description

- BIT0 (1): Voltage alarm
- BIT1 (2): Magnetic encoder alarm
- BIT2 (4): Overheat alarm
- BIT3 (8): Overcurrent alarm
- BIT4 (16): -----
- BIT5 (32): -----
- BIT6 (64): -----
- BIT7 (128): -----

!!! warning "Note"
    If multiple bits are set at the same time, the alarm condition value is the sum of the bit values. Example: with the voltage alarm and the overheat alarm enabled together, the alarm condition value is 4+1=5;

!!! warning "Do not reuse addresses across families"
    Other series may use the same address with a different meaning (for example, SMS addresses 44–45 are PWM open-loop speed, not the goal current of this table). Return to [Bus Protocol](../protocol/index.md) and select the matching memory table.

## Source Definition

- [Official `HLSCL` header](https://github.com/ftservo/FTServo_Arduino/blob/main/src/HLSCL.h)
