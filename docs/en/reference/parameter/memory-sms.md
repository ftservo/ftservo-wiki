# Magnetically Encoded SMS Servo - Memory Table

For SMS RS485 series servos. Two-byte fields are transmitted with the **low byte first**.

STS servos (half-duplex TTL) use different address definitions; see [STS Memory Table](memory-sts.md).

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

Servos use the FT-SCS proprietary protocol. Factory serial defaults: the SMS baud rate is 115200 on the RS485 bus; configurable baud rate range 38400~1 Mbps, default communication address (station number) 1.

For the full frame format and instruction set, see [Bus Protocol](../protocol/index.md).

## 2 Servo Memory Table Definition

If a function address uses two bytes of data, the low byte is at the leading address and the high byte at the following address

### 2.1 Version Information

| Address (DEC) | Address (HEX) | Function | Bytes | Initial value | Access | Range | Unit | Description |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0x00 | Firmware major version | 1 | – | R |  |  |  |
| 1 | 0x01 | Firmware minor version | 1 | – | R |  |  |  |
| 2 | 0x02 | END | 1 | 0 | R |  |  | 0 indicates little-endian storage structure |
| 3 | 0x03 | Servo major version | 1 | – | R |  |  |  |
| 4 | 0x04 | Servo minor version | 1 | – | R |  |  |  |

### 2.2 EPROM Configuration

| Address (DEC) | Address (HEX) | Function | Bytes | Initial value | Access | Range | Unit | Description |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | 0x05 | Servo ID | 1 | 1 | R/W | 0~253 | ID | Unique main ID on the bus |
| 6 | 0x06 | Baud rate | 1 | 0 | R/W | 0~7 | None | 0-7 correspond to baud rates: 1000000(0), 500000(1), 250000(2), 128000(3), 115200(4), 76800(5), 57600(6), 38400(7) |
| 7 | 0x07 | Response return delay | 1 | 0 | R/W | 0/50~253 | 2us | Maximum settable return delay 254*2=508us; 0 means the minimum return delay; a setting below 50 still defaults to 50 (100us) |
| 8 | 0x08 | Response status level | 1 | 1 | R/W | 0~1 | None | 0: no response packet for instructions other than READ and PING; 1: response packet for all instructions |
| 9 | 0x09 | Minimum angle limit | 2 | 0 | R/W | 0~4094 | 0.087° | 0 in multi-turn absolute position control |
| 11 | 0x0B | Maximum angle limit | 2 | 4095 | R/W | 1~4095 | 0.087° | 0 in multi-turn absolute position control |
| 13 | 0x0D | Maximum temperature limit | 1 | 70 | R/W | 0~100 | °C |  |
| 14 | 0x0E | Maximum input voltage | 1 | – | R/W | 0~254 | 0.1V |  |
| 15 | 0x0F | Minimum input voltage | 1 | 40 | R/W | 0~254 | 0.1V |  |
| 16 | 0x10 | Maximum torque | 2 | 1000 | R/W | 0~1000 | 0.1% | Written to address 48 (torque limit) at power-on |
| 18 | 0x12 | Phase | 1 | – | R/W | 0~254 | None | Special function byte; do not modify unless specifically required |
| 19 | 0x13 | Unload condition | 1 | – | R/W | 0~254 | None | Set bit to 1 to enable the corresponding protection, set bit to 0 to disable it |
| 20 | 0x14 | LED alarm condition | 1 | – | R/W | 0~254 | None | Set bit to 1 to enable the flashing alarm, set bit to 0 to disable it |
| 21 | 0x15 | Position loop P (proportional) coefficient | 1 | – | R/W | 0~254 | None | Proportional coefficient controlling the motor (1/4) |
| 22 | 0x16 | Position loop D (derivative) coefficient | 1 | – | R/W | 0~254 | None | Derivative coefficient controlling the motor (1/8) |
| 23 | 0x17 | Position loop I (integral) coefficient | 1 | 0 | R/W | 0~254 | None | Integral coefficient controlling the motor |
| 24 | 0x18 | Minimum startup torque | 1 | – | R/W | 0~254 | 0.1% | Sets the minimum output startup torque of the servo |
| 25 | 0x19 | Integral limit | 1 | 0 | R/W | 0~254 | None | Maximum integral = limit × 4; 0 disables the integral limit; effective in position mode 0 and mode 4 |
| 26 | 0x1A | Positive deadband | 1 | 1 | R/W | 0~16 | 0.087° | The minimum unit is one minimum resolution angle |
| 27 | 0x1B | Negative deadband | 1 | 1 | R/W | 0~16 | 0.087° | The minimum unit is one minimum resolution angle |
| 28 | 0x1C | Protection current | 2 | 511 | R/W | 0~2047 | 6.5mA | The maximum settable current is 500 * 6.5mA = 3250mA |
| 30 | 0x1E | Angle resolution | 1 | 1 | R/W | 1~128 | None | Magnification factor of the sensor's minimum resolution angle |
| 31 | 0x1F | Position offset | 2 | 0 | R/W | 0~8191 | 0.087° | 0~2047 represents 0~2047; 2048~4095 represents 0~-2047; 4096~6143 represents -2048~-4095; 6144~8191 represents -2048~-4095 (bias -4095~4095) |
| 33 | 0x21 | Operating mode | 1 | 0 | R/W | 0~2 | None | 0: position servo mode; 1: constant-speed motor mode; 2: PWM open-loop speed mode; 3: step mode |
| 34 | 0x22 | Holding torque | 1 | 20 | R/W | 0~254 | 1% | Torque output after entering overload protection; for example 20 means 20% of the maximum torque |
| 35 | 0x23 | Protection time | 1 | 200 | R/W | 0~254 | 10ms | Duration for which the load output exceeds the overload torque and is held; for example 200 means 2 seconds, maximum 2.5 seconds |
| 36 | 0x24 | Overload torque | 1 | 80 | R/W | 0~254 | 1% | Maximum torque value that starts the overload protection timer; for example 80 means 80% of the maximum torque |
| 37 | 0x25 | Velocity loop P (proportional) coefficient | 1 | – | R/W | 0~254 | None | Speed-loop proportional coefficient in constant-speed motor mode (mode 1) |
| 38 | 0x26 | Overcurrent protection time | 1 | 200 | R/W | 0~254 | 10ms | Maximum settable 254 * 10ms = 2540ms |
| 39 | 0x27 | Velocity loop I (integral) coefficient | 1 | – | R/W | 0~254 | None | Speed-loop integral coefficient in constant-speed motor mode (mode 1) |

### 2.3 SRAM Control

| Address (DEC) | Address (HEX) | Function | Bytes | Initial value | Access | Range | Unit | Description |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 40 | 0x28 | Torque switch | 1 | 0 | R/W | 0~2 | None | Write 0: torque output off; write 1: torque output on; write 128: calibrate the current position to 2048 |
| 41 | 0x29 | Acceleration | 1 | 0 | R/W | 0~254 | 8.7°/s² | Run acceleration/deceleration of the servo; 0 means maximum acceleration |
| 42 | 0x2A | Goal position | 2 | 0 | R/W | -32767~32767 | 0.087° | Absolute position control; the maximum corresponds to the maximum effective angle; BIT15 is the direction bit |
| 44 | 0x2C | PWM open-loop speed | 2 | 1000 | R/W | 0~1000 | 0.1% | Effective in PWM open-loop speed mode; BIT10 is the direction bit |
| 46 | 0x2E | Running speed | 2 | Factory default maximum speed | R/W | -32767~32767 | 0.732RPM/0.0146RPM | Controls the maximum running speed of the motor; BIT15 is the direction bit; 0 means the maximum speed by default and a phase setting of 0 means stop; the speed unit can be selected via the phase setting, either 0.732RPM or 0.0146RPM; when the unit is set to 0.0146RPM its precision is also 0.732RPM |
| 48 | 0x30 | Torque limit | 2 | Maximum torque (16), default 1000 | R/W | 0~1000 | 0.1% | This value can be modified in software to control the stall torque output |
| 50~54 | 0x32~0x36 | Undefined | 1 |  |  |  |  |  |
| 55 | 0x37 | Lock flag | 1 | 1 | R/W | 0~1 | None | Write 0 to close the write lock: values written to EEPROM addresses persist after power-off; write 1 to open the write lock: values written to EEPROM addresses do not persist |

### 2.4 SRAM Feedback

| Address (DEC) | Address (HEX) | Function | Bytes | Initial value | Access | Range | Unit | Description |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 56 | 0x38 | Present position | 2 | – | R | – | 0.087° | Absolute position feedback of the servo; BIT15 is the direction bit; in step mode 3 it returns the step difference between the present position and the goal position, with BIT15 as the direction bit |
| 58 | 0x3A | Present speed | 2 | – | R | – | 0.732RPM/0.0146RPM | Rotational speed of the motor; the unit follows the phase setting; BIT15 is the direction bit |
| 60 | 0x3C | Present load | 2 | – | R | – | 0.1% | Duty cycle of the output driving the motor; BIT10 is the direction bit |
| 62 | 0x3E | Present voltage | 1 | – | R | – | 0.1V | Current working voltage of the servo |
| 63 | 0x3F | Present temperature | 1 | – | R | – | °C | Current internal working temperature of the servo |
| 64 | 0x40 | Async write flag | 1 | 0 | R | – | None | Flag used with the async write instruction |
| 65 | 0x41 | Servo status | 1 | 0 | R | – | None | A bit set to 1 indicates the corresponding error |
| 66 | 0x42 | Moving flag | 1 | 0 | R | – | None | 1 while the servo is moving, 0 when the target is reached and the servo stops; stays 0 when no new goal position is written |
| 67 | 0x43 | Goal position | 2 | 0 | R | – | 0.087° | Current goal position |
| 69 | 0x45 | Present current | 2 | – | R | – | 6.5mA | Motor phase current feedback |
| 71 | 0x47 | Undefined | 2 | – | R | – | – |  |

### 2.5 Factory Parameters

| Address (DEC) | Address (HEX) | Function | Bytes | Initial value | Access | Range | Unit | Description |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 80 | 0x50 | Moving speed threshold | 1 | – | R | – | – |  |
| 81 | 0x51 | DTs(ms) | 1 | – | R | – | – |  |
| 82 | 0x52 | Speed unit coefficient | 1 | – | R | – | – |  |
| 83 | 0x53 | Hts(ns) | 1 | – | R | – | – | 20.83ns, valid for SMS servo firmware >= 2.54, other versions keep 0 |
| 84 | 0x54 | Maximum speed limit | 1 | – | R | – | – | Unit 0.732rpm |
| 85 | 0x55 | Acceleration limit | 1 | – | R | – | – |  |
| 86 | 0x56 | Acceleration multiplier | 1 | – | R | – | – | The acceleration multiplier takes effect when acceleration is 0; when both the multiplier and the acceleration are 0 the servo responds at the highest speed |

## 3 Special Byte Explanation

### 3.1 Servo Phase

**Bit (weight)**: Description

- BIT0 (1): Driver direction phase; (0) forward, (1) reverse
- BIT1 (2): Driver bridge mode; (0) none required, (1) brushed, takes effect after restart
- BIT2 (4): Speed unit, (0) 0.732RPM, (1) 0.0146RPM
- BIT3 (8): Speed mode; (0) speed 0 means stop, (1) speed 0 means the highest speed
- BIT4 (16): Angle feedback mode, (0) single-turn angle feedback, (1) full-angle feedback
- BIT5 (32): Voltage sampling, (0) 1.5K low-voltage sampling, (1) 1K high-voltage sampling
- BIT6 (64): PWM frequency, (0) 24kHz, (1) 16kHz
- BIT7 (128): Position feedback direction phase, (0) forward, (1) reverse

!!! warning "Note"
    If multiple bits are set at the same time, the phase value is the sum of the bit values. Example: with an original phase value of 0, if the servo runs in reverse, the phase value is 128+1=129;

### 3.2 Servo Status

Servo status: 0 means normal, 1 means abnormal

**Bit (weight)**: Description

- BIT0 (1): Voltage status
- BIT1 (2): Magnetic encoder status
- BIT2 (4): Temperature status
- BIT3 (8): Current status
- BIT4 (16): ----
- BIT5 (32): Load status
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
- BIT4 (16): ----
- BIT5 (32): Load overload
- BIT6 (64): -----
- BIT7 (128): -----

!!! warning "Note"
    If multiple bits are set at the same time, the unload condition value is the sum of the bit values. Example: with voltage protection and overheat protection enabled together, the unload condition value is 4+1=5;

### 3.4 LED Alarm Condition

LED alarm condition: 0 means off, 1 means on

**Bit (weight)**: Description

- BIT0 (1): Voltage alarm
- BIT1 (2): Magnetic encoder alarm
- BIT2 (4): Overheat alarm
- BIT3 (8): Overcurrent alarm
- BIT4 (16): ----
- BIT5 (32): Load overload alarm
- BIT6 (64): -----
- BIT7 (128): -----

!!! warning "Note"
    If multiple bits are set at the same time, the LED alarm condition value is the sum of the bit values. Example: with the voltage alarm and the overheat alarm enabled together, the alarm condition value is 4+1=5;

!!! warning "Do not reuse addresses across families"
    Other series may use the same address with a different meaning (for example, HLS addresses 44–45 are goal current, while this table uses PWM open-loop speed). Return to [Bus Protocol](../protocol/index.md) and select the matching memory table.

## Source Definition

- [Official `SMS_STS` header](https://github.com/ftservo/FTServo_Arduino/blob/main/src/SMS_STS.h)
