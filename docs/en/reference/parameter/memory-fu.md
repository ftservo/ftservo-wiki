# Magnetically Encoded UAVCAN Servo - Memory Table

For magnetically encoded UAVCAN (CAN bus) servos. Register data is 16-bit and transmitted in **big-endian** order (high byte first).

<style>
  .md-typeset table:not([class]) { display: table; width: 100%; table-layout: fixed; }
  .md-typeset table:not([class]) th { min-width: 0; padding: .6em .4em; }
  .md-typeset table:not([class]) td { min-width: 0; padding: .6em .4em; }
  .md-typeset table:not([class]) td, .md-typeset table:not([class]) th { overflow-wrap: anywhere; }
  .md-typeset table:not([class]) th:nth-child(1), .md-typeset table:not([class]) td:nth-child(1) { width: 36px; }
  .md-typeset table:not([class]) th:nth-child(2), .md-typeset table:not([class]) td:nth-child(2) { width: 36px; }
  .md-typeset table:not([class]) th:nth-child(3), .md-typeset table:not([class]) td:nth-child(3) { width: 96px; }
  .md-typeset table:not([class]) th:nth-child(4), .md-typeset table:not([class]) td:nth-child(4) { width: 80px; }
  .md-typeset table:not([class]) th:nth-child(5), .md-typeset table:not([class]) td:nth-child(5) { width: 84px; }
  @media screen and (max-width: 40em) {
    .md-typeset table:not([class]) { table-layout: auto; }
    .md-typeset table:not([class]) th, .md-typeset table:not([class]) td { width: auto; }
  }
</style>

## 1 Communication Protocol

Servos use the UAVCAN communication protocol. The factory default CAN baud rate is 1M, configurable in the range 20K~1M. The communication address, CAN baud rate and communication station address can be set with the host software.

## 2 UAVCAN Command Examples

UAVCAN communication protocol

The following commands follow the CAN2.0B standard; the default motor NODE_ID is 100 (0x64)

```
Single-motor position command: 1807DB01(frame ID):00 64 05 D5(data)
Priority: 18
Frame type: 07DB(2011)
Frame source ID: 01
Frame data: 00 64 05, motor channel (00), position data (0564)
Frame tail: D5

Multi-motor position command:
1807DC01(frame ID):8E 82 64 05 00 00 00 97(data)
1807DC01(frame ID):00 00 00 00 00 00 00 37(data)
1807DC01(frame ID):00 00 00 00 00 00 00 17(data)
1807DC01(frame ID):00 00 00 00 00 00 00 37(data)
1807DC01(frame ID):00 00 00 00 00 00 00 17(data)
1807DC01(frame ID):00 00 00 77(data)
Priority: 18
Frame type: 07DC(2012)
Frame source ID: 01
CRC check: 8E 82
Frame data:
64 05 00 00 00
00 00 00 00 00 00 00
00 00 00 00 00 00 00
00 00 00 00 00 00 00
00 00 00 00 00 00 00
00 00 00
(cmd[0]=0564,cmd[1]=0000,cmd[2]=0000......cmd[17]=0000)
Frame tail:
97/37/17/37/17/77

Automatic report feedback command:
1807DD64(frame ID):A1 04 00 CC 0C CD 0C 80(data)
1807DD64(frame ID):45 00 00 00 2A 00 00 60(data)
Priority: 18
Frame type: 07DD(2013)
Frame source ID: 64
CRC check: A1 04
Frame data:
00 CC 0C CD 0C
45 00 00 00 2A 00 00
(Servo_ID:00,POS_CMD:0CCC,POS_SENSOR:0CCD,VOLTAGE:0045,CURRENT:0000,PCB_Temp:2A,MOTOR_Temp:00,StatusInfo:00)
Frame tail: 80/60

Node status command: 18015564(frame ID):50 03 00 00 00 00 00 D0(data)
Priority: 18
Frame type: 0155(341)
Frame source ID: 64
Frame data: 50 03 00 00 00 00 00
(uptime_sec:00000350,health:0,mode:0,sub_mode:0,vendor_specific_status_code:0)
Frame tail: D0

Torque control command: 1803FC01 (frame ID):00 00 D6(data)
Priority: 18
Frame type: 03FC(1020)
Frame source ID: 01
Frame data: 00 00 D6, motor channel (00), torque command (00, 00 means torque off)
Frame tail: D6

Read hardware version number command:
Request: 18FAE481(frame ID):00 00 02 C0(data)
Response: 18FA0164(frame ID):00 02 4E 28 07 D1 C0(data)
Request frame priority: 18
Request frame type: FA(250)
Request frame source ID: 01
Request frame target ID: 64
Request frame data: 00 01 02 C0(parameter address:0001,parameter length:02)
Request frame tail: C0
Response frame priority: 18
Response response frame type: FA(250)
Response frame source ID: 64
Response frame target ID: 01
Response frame data: 00 02 4E 28 07 D1(read status:00,parameter length:02,parameter data 0:4E28,parameter data 1:07D1)
Response frame tail: C0
```

## 3 Servo Memory Table Definition

!!! note ""
    Register addresses use a paged structure: each page holds 64 registers, and a register address consists of the page number plus the index — for example page 1, index 2 is addressed as 1*64+2=66. All registers in the table can be accessed over MODBUS-RTU and UAVCAN.

### 3.1 Version Information

Storage area: SRAM, access: read only, read/write condition: none

| Page | Index | Function | Range | Default | Value description |
| --- | --- | --- | --- | --- | --- |
| 0 | 0 | Product model high byte |  | 20008 |  |
| 0 | 1 | Product model low byte |  | 2001 |  |
| 0 | 2 | Firmware version high byte |  | 2050 |  |
| 0 | 3 | Firmware version low byte |  | 513xx | xx=00~99 |
| 0 | 4 | Byte order |  | 1 | Big-endian |
| 0 | 5 | SN1 |  | 0 |  |
| 0 | 6 | SN2 |  | 0 |  |
| 0 | 7 | SN3 |  | 0 |  |
| 0 | 8 | SN4 |  | 0 |  |

### 3.2 Control Parameters

Storage area: SRAM, access: read/write, read/write condition: none

| Page | Index | Function | Range | Default | Value description |
| --- | --- | --- | --- | --- | --- |
| 1 | 0 | Reserved address |  | 0 |  |
| 1 | 1 | Reserved address |  | 0 |  |
| 1 | 2 | Target position high byte | 0~65535 | 0 | 1=0.02197 deg, -8192~8192 (output shaft -180 deg ~ 180 deg) |
| 1 | 3 | Target position low byte | 0~65535 | 0 | 1=0.02197 deg, -8192~8192 (output shaft -180 deg ~ 180 deg) |
| 1 | 4 | Running acceleration | 0~2000 | Default acceleration | Output-shaft acceleration, 1=2.1972 deg/s², 0 means the maximum default value |
| 1 | 5 | Running speed | -600~600 | Default running speed | Output-shaft speed, 1=0.1831rpm, 0 means stop |
| 1 | 6 | Running current | -625~625 | Default running current | Supply current while running, 1=6.5mA |
| 1 | 7 | Torque limit | 0~4800 | Default torque limit | The default value is 4800 |
| 1 | 8 | Status reset | 0~65535 | 0 | See the bit description under "Status reset" |
| 1 | 9 | Torque switch | 0~1 | 0 | 0 switches torque off, 1 switches torque on; in servo mode 0 the UAVCAN command switches torque on automatically |
| 1 | 10 | Read/write lock flag | 0~11 | 0 | Unlock flag for writes to the EPROM parameter area; the unlock value is the corresponding page number |
| 1 | 11 | Read/write lock password | -32768~32767 | 0 |  |
| 1 | 12 | CAN function switch bits | 0~7 | CAN function switch bits default | See the bit description under "CAN function switch bits" |

**Status reset**: 0 invalid, 1 resets the corresponding fault

**Bit / weight**: Description

- BIT10 (1024): Reset the turn count
- BIT15 (32768): Zero calibration

!!! warning "Note"
    To reset a fault, set 1 in the corresponding position, then convert it to a value and write that value to the corresponding address. Example: to recover from an over-temperature and over-current fault, write 1 in the corresponding positions, obtaining the binary pattern *0000 0000 0000 1100", converted to the hexadecimal value: 000C; write this value to the status reset (1-8) address with a command.

**CAN function switch bits**: 0 invalid, 1 valid

**Bit / weight**: Description

- BIT0: Master switch for automatic reporting of the node status command
- BIT1: ----
- BIT2: Switch for automatic reporting of the feedback command

### 3.3 Status Parameters

Storage area: SRAM, access: read only, read/write condition: none

| Page | Index | Function | Range | Default | Value description |
| --- | --- | --- | --- | --- | --- |
| 2 | 0 | Reserved address |  | -- |  |
| 2 | 1 | Reserved address |  | -- |  |
| 2 | 2 | Current position high byte | 0~65535 | -- | Same unit as the target position |
| 2 | 3 | Current position low byte | 0~65535 | -- | Same unit as the target position |
| 2 | 4 | Servo single-turn position | -32768~32767 | -- | 1=360/16384=0.02197° |
| 2 | 5 | Reserved address |  |  |  |
| 2 | 6 | Current servo speed | -32768~32767 | -- | 1=0.1831rpm |
| 2 | 7 | Reserved address |  | 0 |  |
| 2 | 8 | Current bus current | -2048~2047 | -- | Same unit as the running current |
| 2 | 9 | Current voltage | 0~400 | -- | 1=0.1V |
| 2 | 10 | Current MOS temperature | 0~100 | -- | 1=1 degree Celsius |
| 2 | 11 | Current load | 0~5000 | -- | Servo drive PWM duty cycle, unit 1=0.02% |
| 2 | 12 | Servo status | 0~65535 | -- | See the bit description under "Servo status" |
| 2 | 13 | Reserved address |  | -- |  |
| 2 | 14 | Current motor temperature | 0~100 | -- | 1=1 degree Celsius |
| 2 | 15~21 | Reserved address |  | -- |  |
| 2 | 22 | Input signal pulse width (us) |  | -- | Unit: microseconds |
| 2 | 23 | Input signal period (us) |  | -- | Unit: microseconds |
| 2 | 24 | Encoder status code |  | -- | BIT0~1 (0: normal, 1: magnetic field too strong, 2: magnetic field too weak), BIT2: button pressed, BIT3: speed too high |
| 2 | 25 | Encoder error count |  | -- | Count of output-shaft encoder communication errors |

**Servo status**: 0 means normal, 1 means abnormal

**Bit / weight**: Description

- BIT0 (1): Over-voltage, recovers automatically once the voltage is normal
- BIT1 (2): Under-voltage, recovers automatically once the voltage is normal
- BIT2 (4): Driver MOS over-temperature, recovers automatically once the temperature is normal
- BIT3 (8): Over-current, recovers automatically once the detected driver output torque is below the safe torque
- BIT5 (64): Magnetic encoder error, recovers automatically once the magnetic encoder is normal
- BIT7 (128): Torque state, 0 means torque off, 1 means torque on
- BIT8 (256): Movement state, 0 means stopped, 1 means moving
- BIT9 (512): Target out of range, recovers automatically after receiving a normal target position
- BIT12 (4096): Target-reached state, 0 means the target is reached
- BIT13 (8192): Motor MOS over-temperature, recovers automatically once the temperature is normal
- BIT14 (32768): Damping state, 1 means the damping state is entered

!!! warning "Note"
    If several states occur at the same time, the motor status value is the sum of the individual state values. Example: torque on together with over-voltage gives a status value of 128+1=129;

### 3.4 Communication Parameters

Storage area: EPROM, access: read/write, read/write condition: torque switch=0 && read/write lock flag=3

| Page | Index | Function | Range | Default | Value description |
| --- | --- | --- | --- | --- | --- |
| 3 | 0 | Serial main ID | 1~247 | 1 | Unique identity code on the bus; no duplicate ID may appear on the same bus; 0 is the broadcast ID |
| 3 | 1 | Reserved address |  | 0 |  |
| 3 | 2 | Serial baud rate | 2~10 | 4 | 2-10 correspond to baud rates: 256000(2), 128000(3), 115200(4), 57600(5), 38400(6), 19200(7), 14400(8), 9600(9), 4800(10) |
| 3 | 3 | Reserved address |  | 0 |  |
| 3 | 4 | Reserved address |  | 0 |  |
| 3 | 5 | Serial return delay | 0~1000 | 500 | Unit: milliseconds |
| 3 | 6 | Reserved address |  | 0 |  |
| 3 | 7 | CAN communication timeout | 0~1000 | 100 | Unit: milliseconds |
| 3 | 8 | CAN baud rate | 0~9 | 8 | 0-9 correspond to baud rates: 10K(0), 20K(1), 50K(2), 100K(3), 125K(4), 250K (5), 500K(6), 800K(7), 1M(8), 83.3K(9) |
| 3 | 9 | CAN driver-side ID | 1~125 | 100 | Unique NODE-ID used to identify the servo |
| 3 | 10 | CAN controller-side ID | 1~125 | 1 | Controller NODE-ID; the controller's NODE-ID must match this register value, otherwise the servo cannot receive controller commands |
| 3 | 11 | Reserved address | 0 | 0 |  |
| 3 | 12 | Auto-report rate | 0~32767 | 100 | Unit: milliseconds; the interval of the automatic feedback-report command; 0 stops reporting |
| 3 | 13~17 | Reserved address |  | 0 |  |
| 3 | 18 | CAN heartbeat rate | 0~32767 | 1000 | Unit: milliseconds; the interval of the automatic status-report command; 0 stops reporting |
| 3 | 19 | Reserved address | 0 | 0 |  |
| 3 | 20 | CAN channel ID | 0~17 | 0 | UAVCAN position command channel ID |

### 3.5 Configuration Parameters

Storage area: EPROM, access: read/write, read/write condition: torque switch=0 && read/write lock flag=4

| Page | Index | Function | Range | Default | Value description |
| --- | --- | --- | --- | --- | --- |
| 4 | 0 | Operating mode | 0~5 | 0 | 0 servo mode, 1 constant-speed mode, 2 constant-current mode, 3 RCPWM servo mode (effective after restart), 4 reserved, 5 motor mode, 6 RCPWM constant-speed mode (effective after restart) |
| 4 | 1 | Default running speed | 0~32767 | -- | Same unit as the running speed |
| 4 | 2 | Default running acceleration | 0~32767 | -- | Same unit as the running acceleration; 0 means the acceleration parameter is not effective |
| 4 | 3 | Default maximum running current | 0~4095 | -- | Same unit as the running current |
| 4 | 4 | Default maximum output torque | 0~4800 | 4800 | Same unit as the maximum output torque |
| 4 | 5 | Reserved address |  | 0 |  |
| 4 | 6 | Reserved address |  | 0 |  |
| 4 | 7 | Positive-direction position deadband | 0~128 | 2 | Same unit as the target position |
| 4 | 8 | Negative-direction position deadband | 0~128 | 2 | Same unit as the target position |
| 4 | 9 | Minimum angle limit | -8192~0 | 0 | Same unit as the target position; minimum angle limit = maximum angle limit means the angle is unlimited; not effective in RCPWM mode |
| 4 | 10 | Maximum angle limit | 0~8191 | 0 | Same unit as the target position; minimum angle limit = maximum angle limit means the angle is unlimited; not effective in RCPWM mode |
| 4 | 11 | Output-shaft position offset | -32768~32767 | 0 | Same unit as the target position |
| 4 | 12 | Reserved address |  |  |  |
| 4 | 13 | CAN function switch bits default | 0~7 | 5 | See the bit description under "CAN function switch bits" |
| 4 | 14 | Configuration phase | 0~32768 | 0 | Reserved address |

### 3.6 RCPWM Parameters

Storage area: EPROM, access: read/write, read/write condition: torque switch=0 && read/write lock flag=4

| Page | Index | Function | Range | Default | Value description |
| --- | --- | --- | --- | --- | --- |
| 5 | 0 | Minimum input signal pulse width | 500~2500 | 500 | Unit: microseconds |
| 5 | 1 | Maximum input signal pulse width | 500~2500 | 2500 | Unit: microseconds |
| 5 | 2 | Positive-direction signal pulse width | 0~1000 | 1000 | Unit: microseconds |
| 5 | 3 | Negative-direction signal pulse width | 0~1000 | 1000 | Unit: microseconds |
| 5 | 4 | Signal minimum angle | -8192~0 | -8192 | Same unit as the target position; PWM signal pulse-width-to-angle mapping; UAVCAN position command 0~1000 angle mapping |
| 5 | 5 | Signal maximum angle | 0~8191 | 8191 | Same unit as the target position; PWM signal pulse-width-to-angle mapping; UAVCAN position command 0~1000 angle mapping |
| 5 | 6 | Signal resolution | 1~16 | 2 | Unit: microseconds |
| 5 | 7 | Signal fine tuning | -128~128 | 0 | Unit: microseconds |
| 5 | 8 | Signal-loss protection | 0~2 | 0 | 0 no torque on signal loss, 1 return to the signal-loss protection position on signal loss, 2 hold the current position on signal loss |
| 5 | 9 | Signal-loss protection position | -32768~32767 | 0 | Same unit as the target position |
| 5 | 10 | Signal dead band | 0~128 | 50 | RCPWM signal dead band in RCPWM speed mode |
| 5 | 11 | Reserved address |  | 0 |  |
| 5 | 12 | Reserved address |  | 0 |  |
| 5 | 13 | Signal modulation coefficient | 0~512 | 15 | Effective when the signal modulation function is enabled; the larger the weight, the faster the adjustment response |
| 5 | 14 | Signal phase | 0~65535 | 0 | See the bit description under "Signal phase" |

**Signal phase**: 0 means off, 1 means on

**Bit / weight**: Description

- BIT0 (1): ----
- BIT1 (2): ----
- BIT2 (4): In RCPWM constant-speed mode, the signal-versus-rotation-direction phase; 0 means forward, 1 means reverse
- BIT3 (8): In RCPWM servo mode, the signal-versus-target-position phase; 0 means forward, 1 means reverse
- BIT4 (16): RCPWM signal modulation function bit, effective for firmware version >=2050.51303; 0 means off, 1 means on (once on, the weight is adjusted with the signal modulation coefficient parameter); switch this bit off for a fast response

### 3.7 Protection Parameters

Storage area: EPROM, access: read/write, read/write condition: torque switch=0 && read/write lock flag=7

| Page | Index | Function | Range | Default | Value description |
| --- | --- | --- | --- | --- | --- |
| 7 | 0 | Torque-off condition | 0~65535 | 7 | See the bit description under "LED alarm condition / torque-off condition" |
| 7 | 1 | LED alarm condition | 0~65535 | 12295 | See the bit description under "LED alarm condition / torque-off condition" |
| 7 | 2 | Maximum MOS temperature limit | 0~100 | 70 | 1=1 degree Celsius |
| 7 | 3 | MOS protection temperature difference | 0~10 | 2 | 1=1 degree Celsius; over-temperature alarm recovery temperature = maximum MOS temperature limit − MOS protection temperature difference |
| 7 | 4 | MOS over-temperature protection time | 0~32767 | 50 | Time unit: milliseconds |
| 7 | 5 | Minimum input voltage | 0~400 | 80 | 1=0.1V |
| 7 | 6 | Maximum input voltage | 0~400 | 280 | 1=0.1V |
| 7 | 7 | Protection voltage difference | 0~20 | 5 | Under-voltage alarm recovery voltage = minimum voltage + protection voltage difference; over-voltage alarm recovery voltage = maximum voltage − protection voltage difference |
| 7 | 8 | Under-voltage protection time | 0~32767 | 100 | Time unit: milliseconds |
| 7 | 9 | Over-voltage protection time | 0~32767 | 1000 | Time unit: milliseconds |
| 7 | 10~12 | Reserved address | 0 | 0 |  |
| 7 | 13 | Protection current | 0~4095 | 1000 | Same unit as the running current |
| 7 | 14 | Over-current protection time | 0~32767 | 1000 | Time unit: milliseconds |
| 7 | 15 | Safe torque | 0~4095 | 0 | Maximum torque output after entering over-current protection; the servo exits over-current protection when its output torque falls below this value |
| 7 | 16~18 | Reserved address |  |  |  |
| 7 | 19 | Maximum motor temperature limit | 0~100 | 0 | 1=1 degree Celsius; 0 means the temperature sensor input is switched off |
| 7 | 20 | Motor temperature difference | 0~10 | 2 | 1=1 degree Celsius; over-temperature alarm recovery temperature = maximum motor temperature limit − motor protection temperature difference |
| 7 | 21 | Motor over-temperature protection time | 0~32768 | 50 | Time unit: milliseconds |

**LED alarm condition / torque-off condition**: 0 means off, 1 means on

**Bit / weight**: Description

- BIT0 (1): Over-voltage alarm / over-voltage protection
- BIT1 (2): Under-voltage alarm / under-voltage protection
- BIT2 (4): MOS over-temperature alarm / MOS over-temperature protection, motor over-temperature alarm / motor over-temperature protection
- BIT3 (8): Over-current alarm / over-current protection
- BIT6 (64): End magnetic encoder error alarm / end magnetic encoder error protection

### 3.8 PID Parameters

Storage area: EPROM, access: read/write, read/write condition: torque switch=0 && read/write lock flag=8

| Page | Index | Function | Range | Default | Value description |
| --- | --- | --- | --- | --- | --- |
| 8 | 0 | Position loop P | 0~1000 | 48 |  |
| 8 | 1 | Position loop D | 0~1000 | 32 |  |
| 8 | 2 | Position loop I | 0~1000 | 0 |  |
| 8 | 3 | Position loop integral limit | 0~5000 | 0 | 0 means no limit |
| 8 | 4 | Reserved address |  | 0 |  |
| 8 | 5 | Velocity loop P | 0~1000 | 20 |  |
| 8 | 6 | Velocity loop I | 0~1000 | 20 |  |
| 8 | 7 | Reserved address |  | 0 |  |
| 8 | 8 | Current loop P | 0~1000 | 0 | Reserved address |
| 8 | 9 | Current loop I | 0~1000 | 1 |  |

!!! warning "Do not reuse addresses across families"
    This table uses a paged address structure of "page × 64 + index", which is completely different from the linear addresses of the FT-SCS families (SMS/STS/HLS/SCSCL) and must not be applied across families. Return to [Bus Protocol](../protocol/index.md) and select the matching memory table.
