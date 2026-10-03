# Magnetically Encoded SMSMB Servo - Memory Table

For SMSMB series servos, which use the standard MODBUS-RTU protocol. MODBUS holding registers are 16-bit and two-byte fields are transmitted with the **high byte first**; "Address (PLC)" is the corresponding MODBUS holding-register address (4xxxx).

<style>
  .md-typeset table:not([class]) { display: table; width: 100%; table-layout: fixed; }
  .md-typeset table:not([class]) th { min-width: 0; padding: .6em .4em; }
  .md-typeset table:not([class]) td { min-width: 0; padding: .6em .4em; }
  .md-typeset table:not([class]) td, .md-typeset table:not([class]) th { overflow-wrap: anywhere; }
  .md-typeset table:not([class]) th:nth-child(1), .md-typeset table:not([class]) td:nth-child(1) { width: 44px; }
  .md-typeset table:not([class]) th:nth-child(2), .md-typeset table:not([class]) td:nth-child(2) { width: 44px; }
  .md-typeset table:not([class]) th:nth-child(3), .md-typeset table:not([class]) td:nth-child(3) { width: 54px; }
  .md-typeset table:not([class]) th:nth-child(4), .md-typeset table:not([class]) td:nth-child(4) { width: 76px; }
  .md-typeset table:not([class]) th:nth-child(5), .md-typeset table:not([class]) td:nth-child(5) { width: 38px; }
  .md-typeset table:not([class]) th:nth-child(6), .md-typeset table:not([class]) td:nth-child(6) { width: 80px; }
  .md-typeset table:not([class]) th:nth-child(7), .md-typeset table:not([class]) td:nth-child(7) { width: 34px; }
  .md-typeset table:not([class]) th:nth-child(8), .md-typeset table:not([class]) td:nth-child(8) { width: 64px; }
  .md-typeset table:not([class]) th:nth-child(9), .md-typeset table:not([class]) td:nth-child(9) { width: 60px; }
  @media screen and (max-width: 40em) {
    .md-typeset table:not([class]) { table-layout: auto; }
    .md-typeset table:not([class]) th, .md-typeset table:not([class]) td { width: auto; }
  }
</style>

## 1 Servo Communication Protocol

Servos use the standard MODBUS-RTU protocol. Factory serial defaults: baud rate 115200, 8 data bits, no parity, 1 stop bit; configurable baud rate range 9600~256 Kbps, default communication address (station number) 1.

For the full frame format and instruction set, see [Bus Protocol](../protocol/index.md).

## 2 Servo Memory Table Definition

### 2.1 Version Information

| Address (DEC) | Address (HEX) | Address (PLC) | Function | Bytes | Initial value | Access | Range | Unit | Description |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0x0 | 40001 | Firmware version | 2 | – | R |  |  |  |
| 1 | 0x1 | 40002 | Servo version | 2 | – | R |  |  |  |
| 2 | 0x2 | 40003 | Firmware release date (year) | 2 | – | R |  |  |  |
| 3 | 0x3 | 40004 | Firmware release date (month) | 2 | – | R |  |  |  |

### 2.2 EPROM Configuration

| Address (DEC) | Address (HEX) | Address (PLC) | Function | Bytes | Initial value | Access | Range | Unit | Description |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10 | 0x0A | 40011 | ID | 2 | 1 | R/W | 1~247 | ID | Unique identifier on the bus; no duplicate ID may appear on the same bus; ID 0 (0x00) is the broadcast ID |
| 11 | 0x0B | 40012 | Baud rate | 2 | 2 | R/W | 0~9 | None | 0-9 correspond to baud rates: 256000(0), 128000(1), 115200(2), 57600(3), 56000(4), 38400(5), 19200(6), 14400(7), 9600(8), 4800(9) |
| 12 | 0x0C | 40013 | Return delay | 2 | 500 | R/W | 0~500 | 1us | 0 means the minimum return delay; the maximum settable return delay is 500us |
| 13 | 0x0D | 40014 | Minimum angle limit | 2 | 0 | R/W | 0~4095 | 0.0879° | Sets the lower limit of the travel range; the value must be smaller than the maximum angle limit; 0 in multi-turn absolute position control |
| 14 | 0x0E | 40015 | Maximum angle limit | 2 | 4095 | R/W | 0~4095 | 0.0879° | Sets the upper limit of the travel range; the value must be greater than the minimum angle limit; 0 in multi-turn absolute position control |
| 15 | 0x0F | 40016 | Position calibration | 2 | 0 | R/W | -2047~2047 | 0.0879° | Calibration expressed range: -2047~2047; write 4 to fault reset (134) to auto-compute the centre position (2048); the calibration value is then stored to this address |
| 16 | 0x10 | 40017 | Operating mode | 2 | 0 | R/W | 0~4 | None | 0: servo mode 1: constant-speed mode 2: reserved 3: special mode (torque is switched off automatically when the goal position is reached) 4: stepper mode |
| 17 | 0x11 | 40018 | Position closed-loop P coefficient | 2 | – | R/W | 0~254 | None | Controls the proportional coefficient of the motor |
| 18 | 0x12 | 40019 | Position closed-loop D coefficient | 2 | – | R/W | 0~254 | None | Controls the derivative coefficient of the motor |
| 19 | 0x13 | 40020 | Position closed-loop I coefficient | 2 | 0 | R/W | 0~254 | None | Controls the integral coefficient of the motor |
| 20 | 0x14 | 40021 | Velocity loop P coefficient | 2 | – | R/W | 0~254 | None | Speed-loop proportional coefficient in constant-speed motor mode (mode 1) |
| 21 | 0x15 | 40022 | Velocity loop I coefficient | 2 | – | R/W | 0~254 | None | Speed-loop integral coefficient in constant-speed motor mode (mode 1) |

### 2.3 SRAM Control

| Address (DEC) | Address (HEX) | Address (PLC) | Function | Bytes | Initial value | Access | Range | Unit | Description |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 128 | 0x80 | 40129 | Goal position | 2 | 0 | R/W | -32768~32767 | 0.0879° | Absolute position control; the maximum corresponds to the maximum effective angle |
| 129 | 0x81 | 40130 | Torque switch | 2 | 0 | R/W | 0~1 | None | Write 0: torque output off; write 1: torque output on |
| 130 | 0x82 | 40131 | Acceleration | 2 | Acceleration default value | R/W | 0~65535 | 8.79°/s² | If set to 0 the servo accelerates at its maximum acceleration; assigned at power-on from the "acceleration default value (405)" |
| 131 | 0x83 | 40132 | Running speed | 2 | Speed default value | R/W | 0~65535 | 0.732RPM | Assigned at power-on from the "speed default value (406)" |
| 132 | 0x84 | 40133 | Torque limit | 2 | Torque limit default value | R/W | 0~1000 | 0.1% | The initial value is assigned at power-on from the torque limit default value (0x194); you can modify it to control the maximum torque output. Note that changing this torque limit also affects the rotation speed, reducing the maximum no-load speed proportionally |
| 133 | 0x85 | 40134 | Lock flag | 2 | 1 | R/W | 0~1/128 | None | Write 0 to close the EPROM write lock: values written to EPROM addresses persist after power-off; write 1 to open the write lock: values written to EPROM addresses do not persist; write 128 to close the factory-parameter write lock |
| 134 | 0x86 | 40135 | Fault reset | 2 | 0 | R/W | 0~65535 | None | Setting the corresponding bit to 1 resets that fault; on success the corresponding bit is cleared; see Special Byte Explanation for details |

### 2.4 SRAM Feedback

| Address (DEC) | Address (HEX) | Address (PLC) | Function | Bytes | Initial value | Access | Range | Unit | Description |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 256 | 0x100 | 40257 | Servo status | 2 | 0 | R | – | None | A bit set to 1 indicates the corresponding error; see Special Byte Explanation for details |
| 257 | 0x101 | 40258 | Present position | 2 | 0 | R | – | 0.0879° | Feedback of the present position; in absolute position control the maximum corresponds to the maximum effective angle |
| 258 | 0x102 | 40259 | Present speed | 2 | 0 | R | – | 0.732RPM | Rotational speed feedback of the motor |
| 259 | 0x103 | 40260 | Output PWM | 2 | 0 | R | – | 0.1% | Duty cycle of the output driving the motor |
| 260 | 0x104 | 40261 | Present voltage | 2 | 0 | R | – | 0.1V | Current working voltage of the servo |
| 261 | 0x105 | 40262 | Present temperature | 2 | 0 | R | – | °C | Current internal working temperature of the servo |
| 262 | 0x106 | 40263 | Moving flag | 2 | 0 | R | – | None | 1 while the servo is moving, 0 when the goal is reached and the servo stops |
| 263 | 0x107 | 40264 | Present current | 2 | 0 | R | – | 6.5mA | Maximum measurable current is 500 * 6.5mA = 3250mA |

### 2.5 Factory Parameters

| Address (DEC) | Address (HEX) | Address (PLC) | Function | Bytes | Initial value | Access | Range | Unit | Description |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 384 | 0x180 | 40385 | Moving detection threshold | 2 | – | Default | – | None | Servo factory default parameter |
| 385 | 0x181 | 40386 | D control time | 2 | – | Default | – | None | Servo factory default parameter |
| 386 | 0x182 | 40387 | Maximum speed limit | 2 | – | Default | 0~32767 | 0.732RPM | Servo factory default parameter |
| 387 | 0x183 | 40388 | H-bridge dead time | 2 | – | Default |  |  | Servo factory default parameter |
| 388 | 0x184 | 40389 | Acceleration limit | 2 | – | Default | 0~65535 | 8.79°/s² | Servo factory default parameter |
| 389 | 0x185 | 40390 | Startup torque | 2 | – | Default | 0~1000 | 0.1% | Sets the minimum output startup torque of the servo; 1000 = 100% * stall torque |
| 390 | 0x186 | 40391 | Clockwise deadband | 2 | – | Default | 0~32 | 0.0879° |  |
| 391 | 0x187 | 40392 | Counter-clockwise deadband | 2 | – | Default | 0~32 | 0.0879° |  |
| 392 | 0x188 | 40393 | Phase | 2 | – | Default | 0~255 | None | Special function byte; do not modify unless specifically required, see Special Byte Explanation for details |
| 393 | 0x189 | 40394 | Protection switch | 2 | – | Default | 0~255 | None | Set a bit to 1 to enable the corresponding protection, set it to 0 to disable it; see Special Byte Explanation for details |
| 394 | 0x18A | 40395 | LED alarm condition | 2 | – | Default | 0~255 | None | Set a bit to 1 to enable the flashing alarm, set it to 0 to disable it; see Special Byte Explanation for details |
| 395 | 0x18B | 40396 | Maximum temperature limit | 2 | – | Default | 0~100 | °C | Maximum working temperature limit; if set to 70 the maximum temperature is 70 °C; the setting resolution is 1 °C |
| 396 | 0x18C | 40397 | Maximum input voltage | 2 | – | Default | Minimum input voltage~360 | 0.1V | If set to 80 the maximum working voltage limit is 8.0V; the setting resolution is 0.1V |
| 397 | 0x18D | 40398 | Minimum input voltage | 2 | – | Default | 0~Maximum input voltage | 0.1V | If set to 40 the minimum working voltage limit is 4.0V; the setting resolution is 0.1V |
| 398 | 0x18E | 40400 | Overload current | 2 | – | Default | 0~511 | 6.5mA | Overload protection current of the servo |
| 399 | 0x18F | 40401 | Overcurrent protection time | 2 | – | Default | 0~5000 | 1ms | Longest working time with the current above the overload current |
| 400 | 0x190 | 40402 | Protection torque | 2 | – | Default | 0~1000 | 0.1% | Output torque after entering overload protection; e.g. 200 means 20% of the maximum torque |
| 401 | 0x191 | 40403 | Overload torque | 2 | – | Default | 0~1000 | 0.1% | Maximum torque threshold for triggering overload protection; e.g. 800 means 80% of the maximum torque |
| 402 | 0x192 | 40404 | Overload protection time | 2 | – | Default | 0~5000 | 1ms | Longest working time with the torque above the overload torque |
| 403 | 0x193 | 40405 | Angle resolution | 2 | 1 | Default | 1~128 | None | Magnification factor of the sensor's minimum resolution angle; changing it extends the control range |
| 404 | 0x194 | 40406 | Torque limit default value | 2 | 1000 | Default | 0~1000 | 0.1% | Power-on default for the torque limit |
| 405 | 0x195 | 40407 | Acceleration default value | 2 | – | Default | 0~65535 | 8.79°/s² | Power-on default for acceleration |
| 406 | 0x196 | 40408 | Speed default value | 2 | – | Default | 0~32767 | 0.732RPM | Power-on default for speed |

## 3 Special Byte Explanation

### 3.1 Servo Phase

**Bit (weight)**: Description

- BIT0 (1): Drive direction phase; (0) forward, (1) reverse
- BIT1 (2): Driver bridge mode; (0) brushless, (1) brushed, takes effect after reboot
- BIT2 (4): Torque auto switch; (0) auto-on, (1) command-on, firmware >= 20.9
- BIT3 (8): Automatic status reset; (0) auto reset, (1) command reset, firmware >= 20.9
- BIT4 (16): Angle feedback mode; (0) single-turn angle feedback, (1) full-angle feedback
- BIT5 (32): ----
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
- BIT4 (16): Torque status: 0 means torque off, 1 means torque on
- BIT5 (32): Load status

!!! warning "Note"
    If multiple statuses occur at the same time, the status value is the sum of the bit values. Example: over-voltage/under-voltage together with servo overheating gives a status value of 4+1=5;

### 3.3 Protection Switch

Unload condition: 0 means off, 1 means on

**Bit (weight)**: Description

- BIT0 (1): Voltage protection
- BIT1 (2): Magnetic encoder protection
- BIT2 (4): Overheat protection
- BIT3 (8): Overcurrent protection
- BIT4 (16): ----
- BIT5 (32): Load overload

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

!!! warning "Note"
    If multiple bits are set at the same time, the LED alarm condition value is the sum of the bit values. Example: with the voltage alarm and the overheat alarm enabled together, the alarm condition value is 4+1=5;

### 3.5 Fault Reset

Fault reset: 0 means invalid, 1 means reset

**Bit (weight)**: Description

- BIT0 (1): Reset overload fault; with auto-reset enabled, reversing the goal and closing the torque switch can reset the fault
- BIT1 (2): Reset overcurrent fault; with auto-reset enabled, reversing the goal and closing the torque switch can reset the fault
- BIT2 (4): Centre setting, the current position is set to the 2048 centre
- BIT3 (8): ----
- BIT4 (16): ----
- BIT5 (32): Reset over-voltage/under-voltage; once the voltage returns to normal, write 32 to reset the over-voltage/under-voltage status; with auto-reset enabled, the fault resets automatically once the voltage returns to normal
- BIT6 (64): Reset overheat status; once the temperature returns to normal, write 64 to reset the overheat status; with auto-reset enabled, the fault resets automatically once the temperature returns to normal
- BIT7 (128): Reset magnetic encoder status; once the magnetic encoder is connected normally, write 128 to reset the magnetic encoder status; with auto-reset enabled, the fault resets automatically once the magnetic encoder is connected normally

!!! warning "Note"
    If multiple bits are set at the same time, the values of reset-overload-fault and reset-overcurrent-fault are summed. Example: resetting the overload fault together with the overcurrent fault gives a reset value of 1+2=3;

!!! warning "Do not reuse addresses across families"
    Other series may use the same address with a different meaning (for example, HLS addresses 44–45 are goal current, while SMSMB addresses 132–133 are torque limit). Return to [Bus Protocol](../protocol/index.md) and select the matching memory table.
