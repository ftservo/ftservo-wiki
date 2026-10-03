# CAN2.0A to FTSCS1.0 Protocol

This page is a transcription of the official《CAN2.0A转FTSCS1.0 协议》(CAN2.0A to FTSCS1.0 Protocol) document. FTSCS1.0 is the FT-SCS custom protocol (instruction frame and status frame structure) shared by all families in [Bus Protocol](index.md); see [FT-SCS Protocol](ft-scs.md). For the memory tables of each family, see [Memory Table Parameters](../parameter/index.md).

## 1. Protocol overview

This protocol is based on the CAN2.0A standard data frame: custom communication instructions are converted into the FTSCS1.0 custom protocol, so that all FEETECH custom-protocol bus servos can work together with CAN bus devices.

Communication uses CAN2.0A standard data frames. The factory default CAN baud rate is 1M, configurable in the range 100K~1M. The factory default CAN station number is 1; the CAN baud rate and the station address can both be set through CAN instructions. Since the FTSCS1.0 protocol is based on 485/TTL, the CAN converter must follow a strict question-answer communication rule, otherwise data conflicts may occur on the 485/TTL bus.

This conversion protocol must be used together with a specific FEETECH conversion module (such as the CAN2.0A-to-TTL single-bus module) to achieve the communication conversion function.

## 2. CAN2.0A frame format

| CAN-ID | DLC | Data1 Data2 ... Data n |
| --- | --- | --- |
| 11-bit CAN-ID | Data length, range 0~8 | 1 byte per data field, n<=8 |

CAN-ID structure:

| CAN-ID | BIT10 ... BIT6 | BIT5 ... BIT0 |
| --- | --- | --- |
|  | CAN instruction code | CAN station address |

- BIT5 ~ BIT0: CAN station number, range 0~63, where 0 is the broadcast address and 1~63 are unicast addresses
- BIT10 ~ BIT6: CAN instruction code, indicating the function of the CAN message to be sent

CAN instruction codes:

| Instruction code | Function | CAN-ID | Description |
| --- | --- | --- | --- |
| 0x01 | Memory table read instruction | 0x080+CAN station number |  |
| 0x02 | Memory table write instruction | 0x100+CAN station number |  |
| 0x03 | Position control instruction | 0x180+CAN station number |  |
| 0x04 | Synchronous read instruction | 0x200+CAN station number |  |
| 0x05 | Asynchronous control instruction | 0x280+CAN station number |  |
| 0x06 | Asynchronous action instruction | 0x300+CAN station number |  |
| 0x07 | Synchronous control instruction | 0x380+CAN station number |  |
| 0x08 | Synchronous action instruction | 0x400+CAN station number |  |
| 0x09 | Servo reply instruction | 0x480+CAN station number | Used to carry the servo reply data |
| 0x0A | CAN configuration instruction | 0x500+CAN station number |  |
| 0x0B | Servo calibration instruction | 0x580+CAN station number |  |

### 2.1 Memory table read instruction (0x01)

The memory table read instruction reads the servo memory table; at most 6 bytes can be read per instruction.

|  | CAN-ID | DLC | Data |
| --- | --- | --- | --- |
| Send | 0x080+CAN station number | 3 | Servo ID (1 byte), memory table address (1 byte), memory table length N (1 byte, N<=6) |
| Reply | 0x480+CAN station number | N+2 | Servo ID (1 byte), servo status (1 byte), memory table data 1 (1 byte) ... memory table data N (1 byte) |

### 2.2 Memory table write instruction (0x02)

The memory table write instruction writes data to the servo memory table; at most 6 bytes can be written per instruction.

|  | CAN-ID | DLC | Data |
| --- | --- | --- | --- |
| Send | 0x100+CAN station number | N+2 | Servo ID (1 byte), memory table address (1 byte), memory table data 1 (1 byte) ... memory table data N (1 byte, N<=6) |
| Reply | 0x480+CAN station number | 2 | Servo ID (1 byte), servo status (1 byte) |

### 2.3 Position control instruction (0x03)

The position control instruction controls the servo position. The input instruction includes: servo ID (1 byte), position (2 bytes), acceleration (1 byte), speed (2 bytes) and running current (2 bytes).

|  | CAN-ID | DLC | Data |
| --- | --- | --- | --- |
| Send | 0x180+CAN station number | 8 | Servo ID (1 byte), target position (2 bytes), running acceleration (1 byte), running speed (2 bytes), running current (2 bytes) |
| Reply | 0x480+CAN station number | 2 | Servo ID (1 byte), servo status (1 byte) |

### 2.4 Synchronous read instruction (0x04)

The synchronous read instruction can read the memory table data of up to 6 servos at the same time.

|  | CAN-ID | DLC | Data |
| --- | --- | --- | --- |
| Send | 0x200+CAN station number | n+2 | Memory table address (1 byte), memory table length N (1 byte, N<=6), servo ID1 (1 byte) ... servo IDn (1 byte, n<=6) |
| Reply | 0x480+CAN station number | N+2 | Servo ID (1 byte), servo status (1 byte), memory table data 1 (1 byte) ... memory table data N (1 byte) |

### 2.5 Asynchronous control instruction (0x05)

The asynchronous control instruction controls the servo position asynchronously. The input instruction includes: servo ID (1 byte), the input instruction includes position (2 bytes), acceleration (1 byte), speed (2 bytes) and running current (2 bytes).

|  | CAN-ID | DLC | Data |
| --- | --- | --- | --- |
| Send | 0x280+CAN station number | 8 | Servo ID (1 byte), target position (2 bytes), running acceleration (1 byte), running speed (2 bytes), running current (2 bytes) |
| Reply | 0x480+CAN station number | 2 | Servo ID (1 byte), servo status (1 byte) |

### 2.6 Asynchronous action instruction (0x06)

The asynchronous action instruction executes the buffered asynchronous control instructions.

|  | CAN-ID | DLC | Data |
| --- | --- | --- | --- |
| Send | 0x300+CAN station number | 0 | None |

### 2.7 Synchronous control instruction (0x07)

The synchronous control instruction controls the servo position synchronously. The input instruction includes: servo ID (1 byte), the input instruction includes position (2 bytes), acceleration (1 byte), speed (2 bytes) and running current (2 bytes). The input instruction is first buffered in the CAN converter; after the synchronous action instruction is received, it is converted into the servo synchronous control instruction and output.

|  | CAN-ID | DLC | Data |
| --- | --- | --- | --- |
| Send | 0x380+CAN station number | 8 | Servo ID (1 byte), target position (2 bytes), running acceleration (1 byte), running speed (2 bytes), running current (2 bytes) |

### 2.8 Synchronous action instruction (0x08)

After the CAN converter receives the synchronous action, it converts the buffered synchronous control instructions into the servo synchronous control instruction and outputs it.

Action instruction:

|  | CAN-ID | DLC | Data |
| --- | --- | --- | --- |
| Send | 0x400+CAN station number | 0 | None |

Clear instruction:

|  | CAN-ID | DLC | Data |
| --- | --- | --- | --- |
| Send | 0x400+CAN station number | 1 | 0 |

Query instruction:

|  | CAN-ID | DLC | Data |
| --- | --- | --- | --- |
| Send | 0x400+CAN station number | 1 | 1 |
| Reply | 0x400+CAN station number | 1 | Number of buffered instructions (1 byte) |

### 2.9 CAN configuration instruction (0x0A)

CAN configuration instruction:

|  | CAN-ID | DLC | Data |
| --- | --- | --- | --- |
| Send | 0x500+CAN station number | 3 | CAN baud rate (1 byte), CAN station number (1 byte), servo baud rate (1 byte) |
| Reply | 0x500+CAN station number | 8 | Baud rate (1 byte), CAN station number (1 byte), servo baud rate (1 byte), reserved (1 byte), firmware version (1 byte), firmware release year (1 byte), firmware distribution month (1 byte), firmware release day (1 byte) |

- CAN station number: 1~63
- Servo baud rate: 0~3, 0 means 1M, 1 means 500k, 2 means 250k, 3 means 115200
- CAN baud rate: 0~3, 0 means 1M, 1 means 500k, 2 means 250k, 3 means 100k

Return CAN configuration information:

|  | CAN-ID | DLC | Data |
| --- | --- | --- | --- |
| Send | 0x500+CAN station number | 0 | None |
| Reply | 0x500+CAN station number | 8 | Baud rate (1 byte), CAN station number (1 byte), servo baud rate (1 byte), reserved (1 byte), firmware version (1 byte), firmware release year (1 byte), firmware distribution month (1 byte), firmware release day (1 byte) |

**Note: configuration changes take effect after a restart**

### 2.10 Servo calibration instruction (0x0B)

Recalibrate the current position to the set value:

|  | CAN-ID | DLC | Data |
| --- | --- | --- | --- |
| Send | 0x580+CAN station number | 3 | Servo ID (1 byte), calibration position (2 bytes) |
| Reply | 0x480+CAN station number | 2 | Servo ID (1 byte), servo status (1 byte) |

Calibrate the current position to the midpoint:

|  | CAN-ID | DLC | Data |
| --- | --- | --- | --- |
| Send | 0x580+CAN station number | 1 | Servo ID (1 byte) |
| Reply | 0x480+CAN station number | 2 | Servo ID (1 byte), servo status (1 byte) |
