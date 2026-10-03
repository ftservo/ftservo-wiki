# SHC Servo - Memory Table

## 1 Servo Communication Protocol

The servo uses the CANopen communication protocol. The factory default CAN baud rate is 125k, configurable in the range 20k~1Mbps, and the default communication address (node) is 1.

SDO commands can access every object dictionary entry of the servo to modify its parameters

PDO commands can control the servo quickly for positioning functions

SYNC commands can quickly and synchronously report the real-time status of all servos on the bus

RPDO1 by default maps the controlword and servo mode objects, used for servo torque switching and mode configuration

RPDO2 by default maps the target position object, used for servo position control

RPDO3 by default maps the target velocity object, used for servo velocity control

RPDO4 by default maps the rated-current object, used for servo rated-current control

TPDO2 by default maps the actual position object; SYNC commands can report the real-time position of all servos on the bus in real time

TPDO1, TPDO3 and TPDO4 have their default mapping switched off

## 2 Object Dictionary (OD)

The CANopen object dictionary (OD: Object Dictionary) is the most central concept of the CANopen protocol. The so-called object dictionary is an ordered group of objects that describes all parameters of the corresponding CANopen node, including where communication data is stored, which is also listed under its index; the object dictionary is addressed by index and sub-index.

<style>
  .md-typeset table:not([class]) { display: table; width: 100%; }
  .md-typeset table:not([class]) th { min-width: 0; padding: .6em .4em; }
  .md-typeset table:not([class]) td { min-width: 0; padding: .6em .4em; }
  .md-typeset table:not([class]) td, .md-typeset table:not([class]) th { overflow-wrap: anywhere; }
  .md-typeset table:not([class]):has(td:nth-child(9)) { table-layout: fixed; }
  .md-typeset table:not([class]):has(td:nth-child(9)) th:nth-child(1), .md-typeset table:not([class]):has(td:nth-child(9)) td:nth-child(1) { width: 48px; }
  .md-typeset table:not([class]):has(td:nth-child(9)) th:nth-child(2), .md-typeset table:not([class]):has(td:nth-child(9)) td:nth-child(2) { width: 40px; }
  .md-typeset table:not([class]):has(td:nth-child(9)) th:nth-child(3), .md-typeset table:not([class]):has(td:nth-child(9)) td:nth-child(3) { width: 96px; }
  .md-typeset table:not([class]):has(td:nth-child(9)) th:nth-child(4), .md-typeset table:not([class]):has(td:nth-child(9)) td:nth-child(4) { width: 34px; }
  .md-typeset table:not([class]):has(td:nth-child(9)) th:nth-child(5), .md-typeset table:not([class]):has(td:nth-child(9)) td:nth-child(5) { width: 38px; }
  .md-typeset table:not([class]):has(td:nth-child(9)) th:nth-child(6), .md-typeset table:not([class]):has(td:nth-child(9)) td:nth-child(6) { width: 68px; }
  .md-typeset table:not([class]):has(td:nth-child(9)) th:nth-child(7), .md-typeset table:not([class]):has(td:nth-child(9)) td:nth-child(7) { width: 92px; }
  .md-typeset table:not([class]):has(td:nth-child(9)) th:nth-child(8), .md-typeset table:not([class]):has(td:nth-child(9)) td:nth-child(8) { width: 58px; }
  @media screen and (max-width: 40em) {
    .md-typeset table:not([class]) { table-layout: auto; }
    .md-typeset table:not([class]) th, .md-typeset table:not([class]) td { width: auto; }
  }
</style>

### 3.1 Communication Object Sub-protocol Area

| Index | Sub-index | Object | Access | Type | Unit | Default | Mapped PDO | Description |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1000h | 00h | Device type | R | U32 | – | 00020192h | – | Standard value for a CIA402 device |
| 1001h | 00h | Error register | R | U8 | – | 0 | TPDO | See the special byte/bit explanation |
| 1002h | 00h | Servo status | R | U32 | – | 0 | TPDO | Servo-defined status; see the special byte/bit explanation |
| 1003h | 00h | Pre-defined error field | R/W | U8 | – | 0 | – | Number of errors that occurred; writing 00h clears the error history, writing a non-zero value returns SDO abort 0x06090030; see the special byte/bit explanation |
| 1003h | 01h | Pre-defined error field-1 | R | U32 | – | 0 | – | No error; a read returns SDO abort 0x08000024 |
| 1003h | 02h | Pre-defined error field-2 | R | U32 | – | 0 | – | No error; a read returns SDO abort 0x08000024 |
| 1003h | 03h | Pre-defined error field-3 | R | U32 | – | 0 | – | No error; a read returns SDO abort 0x08000024 |
| 1003h | 04h | Pre-defined error field-4 | R | U32 | – | 0 | – | No error; a read returns SDO abort 0x08000024 |
| 1003h | 05h | Pre-defined error field-5 | R | U32 | – | 0 | – | No error; a read returns SDO abort 0x08000024 |
| 1005h | 00h | SYNC message COB-ID | R | U32 | – | 00000080h | – | Modifying the SYNC COB-ID is not supported |
| 1008h | 00h | Device vendor name | R | str | – |  | – | 15-byte string |
| 1009h | 00h | Device hardware model | R | str | – |  | – | 15-byte string |
| 1010h | 00h | Save parameters | R | U8 | – | 1 | – |  |
| 1010h | 01h | Save all parameters | R/W | U32 | – | – | – | "save" saves all parameters to EPROM |
| 1011h | 00h | Restore parameters | R | U8 | – | 1 | – |  |
| 1011h | 01h | Restore all parameters | R/W | U32 | – | – | – | "load" restores all parameters to the factory defaults |
| 1014h | 00h | EMCY message COB-ID | R | U32 | – | 80h+NodeID | – |  |
| 1017h | 00h | Producer heartbeat time | R/W | U16 | 100ms | 0 | – | 0 stops the heartbeat function |
| 1018h | 00h | Identity object | R | U8 | – | 4 | – |  |
| 1018h | 01h | Servo vendor ID | R | U32 | – |  | – |  |
| 1018h | 02h | Servo model | R | U32 | – |  | – |  |
| 1018h | 03h | Servo firmware | R | U32 | – |  | – |  |
| 1018h | 04h | Servo serial number SN | R | U32 | – |  | – |  |
| 1200h | 00h | SDO server parameter | R | U8 | – | 2 | – |  |
| 1200h | 01h | TSDO object | R | U32 | – | NodeID+600h | – |  |
| 1200h | 02h | RSDO object | R | U32 | – | NodeID+580h | – |  |
| 1400h | 00h | RPDO1 communication parameter | R | U8 | – | 2 | – |  |
| 1400h | 01h | RPDO1 object | R | U32 | – | NodeID+200h | – |  |
| 1400h | 02h | Transmission type | R | U8 | – | FF | – | The servo updates the data immediately after receiving the RPDO |
| 1401h | 00h | RPDO2 communication parameter | R | U8 | – | 2 | – |  |
| 1401h | 01h | RPDO2 object | R | U32 | – | NodeID+300h | – |  |
| 1401h | 02h | Transmission type | R | U8 | – | FF | – | The servo updates the data immediately after receiving the RPDO |
| 1402h | 00h | RPDO3 communication parameter | R | U8 | – | 2 | – |  |
| 1402h | 01h | RPDO3 object | R | U32 | – | NodeID+400h | – |  |
| 1402h | 02h | Transmission type | R | U8 | – | FF | – | The servo updates the data immediately after receiving the RPDO |
| 1403h | 00h | RPDO4 communication parameter | R | U8 | – | 2 | – |  |
| 1403h | 01h | RPDO4 object | R | U32 | – | NodeID+500h | – |  |
| 1403h | 02h | Transmission type | R | U8 | – | FF | – | The servo updates the data immediately after receiving the RPDO |
| 1600h | 00h | RPDO1 mapping parameter | R/W | U8 | – | 2 | – | Number of mapped object addresses; 0 disables mapping, value range 0~4 |
| 1600h | 01h | Mapped object address 1 | R/W | U32 | – | 0x60400010 | – | Mapped object address |
| 1600h | 02h | Mapped object address 2 | R/W | U32 | – | 0x60600008 | – | Mapped object address |
| 1600h | 03h | Mapped object address 3 | R/W | U32 | – |  | – | Mapped object address |
| 1600h | 04h | Mapped object address 4 | R/W | U32 | – |  | – | Mapped object address |
| 1601h | 00h | RPDO2 mapping parameter | R/W | U8 | – | 1 | – | Number of mapped object addresses; 0 disables mapping, value range 0~4 |
| 1601h | 01h | Mapped object address 1 | R/W | U32 | – | 0x607a0020 | – | Mapped object address |
| 1601h | 02h | Mapped object address 2 | R/W | U32 | – |  | – | Mapped object address |
| 1601h | 03h | Mapped object address 3 | R/W | U32 | – |  | – | Mapped object address |
| 1601h | 04h | Mapped object address 4 | R/W | U32 | – |  | – | Mapped object address |
| 1602h | 00h | RPDO3 mapping parameter | R/W | U8 | – | 1 | – | Number of mapped object addresses; 0 disables mapping, value range 0~4 |
| 1602h | 01h | Mapped object address 1 | R/W | U32 | – | 0x60ff0020 | – | Mapped object address |
| 1602h | 02h | Mapped object address 2 | R/W | U32 | – |  | – | Mapped object address |
| 1602h | 03h | Mapped object address 3 | R/W | U32 | – |  | – | Mapped object address |
| 1602h | 04h | Mapped object address 4 | R/W | U32 | – |  | – | Mapped object address |
| 1603h | 00h | RPDO4 mapping parameter | R/W | U8 | – | 1 | – | Number of mapped object addresses; 0 disables mapping, value range 0~4 |
| 1603h | 01h | Mapped object address 1 | R/W | U32 | – | 0x60750020 | – | Mapped object address |
| 1603h | 02h | Mapped object address 2 | R/W | U32 | – |  | – | Mapped object address |
| 1603h | 03h | Mapped object address 3 | R/W | U32 | – |  | – | Mapped object address |
| 1603h | 04h | Mapped object address 4 | R/W | U32 | – |  | – | Mapped object address |
| 1800h | 00h | TPDO1 communication parameter | R | U8 | – | 2 | – |  |
| 1800h | 01h | TPDO1 object | R | U32 | – | NodeID+180h | – |  |
| 1800h | 02h | Transmission type | R | U8 | – | 1 | – | The servo reports the TPDO immediately after receiving SYNC |
| 1801h | 00h | TPDO2 communication parameter | R | U8 | – | 2 | – |  |
| 1801h | 01h | TPDO2 object | R | U32 | – | NodeID+280h | – |  |
| 1801h | 02h | Transmission type | R | U8 | – | 1 | – | The servo reports the TPDO immediately after receiving SYNC |
| 1802h | 00h | TPDO3 communication parameter | R | U8 | – | 2 | – |  |
| 1802h | 01h | TPDO3 object | R | U32 | – | NodeID+380h | – |  |
| 1802h | 02h | Transmission type | R | U8 | – | 1 | – | The servo reports the TPDO immediately after receiving SYNC |
| 1803h | 00h | TPDO4 communication parameter | R | U8 | – | 2 | – |  |
| 1803h | 01h | TPDO4 object | R | U32 | – | NodeID+480h | – |  |
| 1803h | 02h | Transmission type | R | U8 | – | 1 | – | The servo reports the TPDO immediately after receiving SYNC |
| 1A00h | 00h | TPDO1 mapping parameter | R/W | U8 | – | 0 | – | Number of mapped object addresses; 0 disables mapping, value range 0~4 |
| 1A00h | 01h | Mapped object address 1 | R/W | U32 | – | 0x60410010 | – | Mapped object address |
| 1A00h | 02h | Mapped object address 2 | R/W | U32 | – | 0x60610008 | – | Mapped object address |
| 1A00h | 03h | Mapped object address 3 | R/W | U32 | – | 0x603f0010 | – | Mapped object address |
| 1A00h | 04h | Mapped object address 4 | R/W | U32 | – |  | – | Mapped object address |
| 1A01h | 00h | TPDO2 mapping parameter | R/W | U8 | – | 1 | – | Number of mapped object addresses; 0 disables mapping, value range 0~4 |
| 1A01h | 01h | Mapped object address 1 | R/W | U32 | – | 0x60630020 | – | Mapped object address |
| 1A01h | 02h | Mapped object address 2 | R/W | U32 | – | 0x606c0020 | – | Mapped object address |
| 1A01h | 03h | Mapped object address 3 | R/W | U32 | – |  | – | Mapped object address |
| 1A01h | 04h | Mapped object address 4 | R/W | U32 | – |  | – | Mapped object address |
| 1A02h | 00h | TPDO3 mapping parameter | R/W | U8 | – | 0 | – | Number of mapped object addresses; 0 disables mapping, value range 0~4 |
| 1A02h | 01h | Mapped object address 1 | R/W | U32 | – | 0x60780010 | – | Mapped object address |
| 1A02h | 02h | Mapped object address 2 | R/W | U32 | – |  | – | Mapped object address |
| 1A02h | 03h | Mapped object address 3 | R/W | U32 | – |  | – | Mapped object address |
| 1A02h | 04h | Mapped object address 4 | R/W | U32 | – |  | – | Mapped object address |
| 1A03h | 00h | TPDO4 mapping parameter | R/W | U8 | – | 0 | – | Number of mapped object addresses; 0 disables mapping, value range 0~4 |
| 1A03h | 01h | Mapped object address 1 | R/W | U32 | – |  | – | Mapped object address |
| 1A03h | 02h | Mapped object address 2 | R/W | U32 | – |  | – | Mapped object address |
| 1A03h | 03h | Mapped object address 3 | R/W | U32 | – |  | – | Mapped object address |
| 1A03h | 04h | Mapped object address 4 | R/W | U32 | – |  | – | Mapped object address |

### 3.2 Manufacturer-specific Sub-protocol Area

| Index | Sub-index | Object | Access | Type | Unit | Default | Mapped PDO | Description |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2000h | 00h | Servo NodeId | R/W | S8 | – | 1 | – | Takes effect immediately |
| 2001h | 00h | Servo baud rate | R/W | U8 | – | 4 | – | 0-7 correspond to baud rates: 1M(0), 800k(1), 500k(2), 250k(3), 125k(4), 100k(5), (50k)6, 20k(7); takes effect after restart |
| 2002h | 00h | Communication timeout | R/W | U8 | ms | 50 | – |  |
| 2003h | 00h | Default mode | R/W | S8 | – | 1 | – | See the special byte/bit explanation |
| 2004h | 00h | Torque limit | R/W | S16 | 0.02% | 4800 | – |  |
| 2005h | 00h | Start-up torque | R/W | S16 | 0.02% | 0 | – | Range: 0~255 |
| 2006h | 00h | Position dead band | R/W | u8 | 0.022 deg | 2 | – | The smallest unit is one minimum resolution angle |
| 2007h | 00h | Minimum angle limit | R/W | S16 | 0.022 deg | 0 | – | This value is 0 in multi-turn absolute position control |
| 2008h | 00h | Maximum angle limit | R/W | S16 | 0.022 deg | 0 | – | This value is 0 in multi-turn absolute position control |
| 2009h | 00h | Position offset | R/W | S16 | 0.022 deg | 0 | – | The smallest unit is one minimum resolution angle |
| 200Ah | 00h | Servo phase | R/W | U16 | – | – | – | Do not modify unless required; see the special byte/bit explanation |
| 200Bh | 00h | Protection switch | R/W | U16 | – | 7 | – | Setting the corresponding bit to 1 enables that protection, 0 disables it; see the special byte/bit explanation |
| 200Ch | 00h | LED alarm condition | R/W | U16 | – | 15 | – | Setting the corresponding bit to 1 enables the flashing alarm, 0 disables it; see the special byte/bit explanation |
| 200Dh | 00h | Maximum temperature limit | R/W | U16 | °C | 70 | – | Maximum operating temperature limit; if set to 70 the maximum temperature is 70 °C, resolution 1 °C |
| 200Eh | 00h | Minimum input voltage | R/W | U16 | 0.1V | – | – | If the minimum input voltage is set to 40, the minimum operating voltage limit is 4.0V, resolution 0.1V |
| 200Fh | 00h | Maximum input voltage | R/W | U16 | 0.1V | – | – | If the maximum input voltage is set to 260, the maximum operating voltage limit is 26.0V, resolution 0.1V |
| 2010h | 00h | Overload current | R/W | U16 | 6.5mA | – | – | Servo operating overload protection current |
| 2011h | 00h | Over-current protection time | R/W | U16 | 1ms | 3000 | – | Longest working time for which the operating current may exceed the overload current |
| 2012h | 00h | Protection torque | R/W | U16 | – | 0 | – | Reserved address |
| 2013h | 00h | Overload torque | R/W | U16 | – | 0 | – | Reserved address |
| 2014h | 00h | Overload protection time | R/W | U16 | – | 0 | – | Reserved address |
| 2015h | 00h | Position loop P proportional coefficient | R/W | U16 | – | 48 | – | Standard position mode (mode 1), closed-loop position proportional coefficient |
| 2016h | 00h | Position loop D derivative coefficient | R/W | U16 | – | 32 | – | Standard position mode (mode 1), closed-loop position derivative coefficient |
| 2017h | 00h | Position loop I integral coefficient | R/W | U16 | – | 0 | – | Standard position mode (mode 1), closed-loop position integral coefficient |
| 2018h | 00h | Position loop integral limit | R/W | U16 | – | 0 | – | Standard position mode (mode 1), maximum closed-loop position integral limit; 0 means no limit |
| 2019h | 00h | Velocity loop P proportional coefficient | R/W | U16 | – | 100 | – | Standard velocity mode (mode 3), velocity loop proportional coefficient |
| 201Ah | 00h | Velocity loop I integral coefficient | R/W | U16 | – | 100 | – | Standard velocity mode (mode 3), velocity loop integral coefficient |
| 201Bh | 00h | Current loop P proportional coefficient | R/W | U16 | – | – | – | Servo factory default parameter |
| 201Ch | 00h | Current loop I integral coefficient | R/W | U16 | – | – | – | Servo factory default parameter |
| 201Dh | 00h | Maximum speed limit | R/W | U16 | – | 0.183rpm | – | Servo factory default parameter |
| 201Eh | 00h | Maximum acceleration limit | R/W | U16 | 0.366rpm/s | – | – | Servo factory default parameter |
| 201Fh | 00h | Rated current limit | R/W | U16 | 6.5mA | – | – | Servo factory default parameter |
| 2020h | 00h | Maximum torque limit | R/W | S16 | – | 5000 | – | Do not modify unless required |
| 2021h | 00h | H-bridge dead time | R/W | U16 | – | – | – | Servo factory default parameter |
| 2022h | 00h | Derivative control time | R/W | U16 | ms | – | – | Servo factory default parameter |
| 2023h | 00h | Current sampling window time | R/W | U16 | – | – | – | Servo factory default parameter |
| 2024h | 00h | Movement detection threshold | R/W | U16 | – | – | – | Servo factory default parameter |
| 2025h | 00h | Six-step commutation threshold | R/W | U16 | – | – | – | Servo factory default parameter |
| 2026h | 00h | Velocity derivative time | R/W | U16 | ms | 20 | – | Servo factory default parameter |
| 2027h | 00h | Position filter coefficient | R/W | U16 | – | – | – | Servo factory default parameter |
| 2028h | 00h | Velocity filter coefficient | R/W | U16 | – | – | – | Servo factory default parameter |
| 2029h | 00h | Bus current filter coefficient | R/W | U16 | – | – | – | Servo factory default parameter |
| 202Ah | 00h | Position loop derivative filter coefficient | R/W | U16 | – | – | – | Servo factory default parameter |
| 202Bh | 00h | Current voltage | R | S16 | 0.1V | ? | TPDO | Current servo operating voltage |
| 202Ch | 00h | Current temperature | R | S16 | °C | ? | TPDO | Current internal operating temperature of the servo |
| 202Eh | 00h | Magnetic encoder status code | R | U16 | – | ? | – | Status code of the magnetic encoder itself |
| 202Fh | 00h | Encoder error count | R | U16 | – | ? | – | Magnetic encoder communication error count |
| 2031h | 00h | Bus current offset | R | U16 | 6.5mA | ? | – | Automatically detected at power-on |
| 2032h | 00h | Servo status reset | R/W | U16 | 0 | 0 | RPDO | Setting the corresponding bit to 1 resets that fault; the bit is cleared to 0 when the reset succeeds; see the special byte/bit explanation |
| 2033h | 00h | Servo vendor | Default | U32 | – | – | – | Servo factory default parameter |
| 2034h | 00h | Servo model | Default | U32 | – | – | – | Servo factory default parameter |

### 3.3 Standardised Device Sub-protocol Area

| Index | Sub-index | Object | Access | Type | Unit | Default | Mapped PDO | Description |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 603Fh | 00h | Error code | R | U16 | – | 0 | TPDO | See the definition in 1003h (pre-defined error field); can be reset to 0 through 6040h |
| 6040h | 00h | Controlword | R/W | U16 | – | 0 | RPDO | 0: switch servo torque off, 15: switch servo torque on, 11: quick fault stop |
| 6041h | 00h | Statusword | R | U16 | – | 0 | TPDO | See the CANopen communication protocol |
| 6060h | 00h | Modes of operation | R/W | S8 | – | Default mode (2003) | RPDO | See the special byte/bit explanation |
| 6061h | 00h | Modes of operation display | R | S8 | – | Default mode (2003) | TPDO | See the special byte/bit explanation |
| 6062h | 00h | Current target position | R | S32 | 0.022 deg | ? | TPDO |  |
| 6063h | 00h | Actual position | R | S32 | 0.022 deg | ? | TPDO |  |
| 606Ch | 00h | Actual velocity | R | S32 | – | ? | TPDO |  |
| 6072h | 00h | Torque limit | R/W | U16 | 0.02% | Torque limit (2004) | RPDO |  |
| 6074h | 00h | Actual torque | R/W | S16 | 0.02% | ? | TPDO |  |
| 6075h | 00h | Rated current | R/W | U32 | 6.5mA | Rated current limit (201F) | RPDO |  |
| 6078h | 00h | Current feedback | R | S16 | 6.5mA | ? | TPDO |  |
| 607Ah | 00h | Target position | R/W | S32 | 0.022 deg | – | RPDO | Servo positioning target position |
| 6083h | 00h | Profile acceleration | R/W | U32 | 0.366rpm/s | Maximum acceleration limit (201E) | RPDO | Acceleration and deceleration share this parameter |
| 6084h | 00h | Profile deceleration | R/W | U32 | 0.366rpm/s | – | RPDO | Not effective |
| 6085h | 00h | Quick-stop deceleration | R/W | U32 | 0.366rpm/s | – | RPDO | Quick-stop deceleration when 11 is written to the controlword |
| 60FFh | 00h | Target velocity | R/W | S32 | 0.183rpm | Maximum speed limit (201D) | RPDO |  |

## 3 Special Byte Explanation

### 3.1 Mode Definition

| Value | Mode | Description |
| --- | --- | --- |
| 1 | Standard position mode | Target position, velocity, rated current control, acceleration/deceleration control |
| 3 | Standard velocity mode | Velocity, rated current control, acceleration/deceleration control |
| 12 | Motor mode | Rated current control (0.02%), for servo testing |

### 3.2 Error Register Definition

**Bit / weight**: 0 means normal, 1 means abnormal

- BIT0 (1): ----
- BIT1 (2): Servo over-current
- BIT2 (4): Servo over-voltage/under-voltage
- BIT3 (8): Servo over-temperature
- BIT4 (16): ----
- BIT5 (32): ----
- BIT6 (64): ----
- BIT7 (128): Servo position sensor communication error

### 3.3 Pre-defined Error Field Definition

| Additional information | Error code |
| --- | --- |
| bit31 ~ bit16 | bit15 ~ bit0 |

| Error code | Alarm content |
| --- | --- |
| 0000h | Error reset or no error |
| 2300h | Motor over-current |
| 2311h | Motor overload |
| 3210h | Supply over-voltage |
| 3220h | Supply under-voltage |
| 4210h | Over-temperature alarm |
| 7306h | Encoder fault |

### 3.4 Servo Phase

**Bit / weight**: Description

- BIT0 (1): Drive direction phase; (0) forward, (1) reverse
- BIT1 (2): Position feedback direction phase, (0) forward, (1) reverse
- BIT2 (4): Brushless/brushed, (0) brushless, (1) brushed; takes effect after restart

### 3.5 Servo Status

\*Servo status: 0 means normal, 1 means abnormal

**Bit / weight**: Description

- BIT0 (1): Torque state: 0 means torque off, 1 means torque on
- BIT1 (2): Movement state: 0 the servo is moving, 1 the servo has stopped moving
- BIT2 (4): Target state: 0 the servo has reached the set target position, 1 the servo has not reached the set target position

### 3.6 LED Alarm Condition

LED alarm condition: 0 means off, 1 means on

**Bit / weight**: Description

- BIT0 (1): ----
- BIT1 (2): Over-current alarm
- BIT2 (4): Voltage alarm
- BIT3 (8): Over-temperature alarm
- BIT4 (16): ----
- BIT5 (32): ----
- BIT6 (64): ----
- BIT7 (128): Encoder alarm

### 3.7 Protection Switch

Unload condition: 0 means off, 1 means on

**Bit / weight**: Description

- BIT0 (1): ----
- BIT1 (2): Over-current alarm
- BIT2 (4): Voltage alarm
- BIT3 (8): Over-temperature alarm
- BIT4 (16): ----
- BIT5 (32): ----
- BIT6 (64): ----
- BIT7 (128): Encoder alarm

### 3.8 Status Reset

Fault reset: 0 invalid, 1 means reset

**Bit / weight**: Description

- BIT0 (1): ----
- BIT1 (2): Reset over-current fault
- BIT2 (4): Reset over-voltage/under-voltage; once the voltage returns to normal, writing 32 to the status reset resets the over-voltage/under-voltage state
- BIT3 (8): Reset over-temperature state; once the temperature returns to normal, writing 64 to the status reset resets the over-temperature state
- BIT4 (16): ----
- BIT5 (32): ----
- BIT6 (64): ----
- BIT7 (128): Reset magnetic encoder state; when the magnetic encoder is connected normally, writing 128 to the status reset resets the magnetic encoder state
- BIT14 (16384): Turn-count reset; writing 16384 to the status reset returns the servo to the single-turn position
- BIT15 (32768): Centre setting; writing 32768 to the status reset sets the current position as the 8192 centre
