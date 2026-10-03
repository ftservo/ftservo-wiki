# UAVCAN Protocol

This page is a transcription of the official *UAVCAN Communication Protocol* document. The memory tables of each family are listed under [Memory Table Parameters](../parameter/index.md); the UAVCAN family memory table is at [UAVCAN memory table](../parameter/memory-fu.md).

## 1 UAVCAN protocol overview

UAVCAN is a lightweight protocol based on the CAN2.0B communication protocol, with a transfer rate of up to 1Mb/s. Through the CAN bus it provides a highly reliable communication method for aerospace and robotics applications. UAVCAN is a decentralized peer-to-peer network in which every peer (node) has a unique numeric identifier NODE_ID. UAVCAN nodes can communicate using any of the following methods:

- Message broadcast: the primary method of data exchange with publish/subscribe semantics.
- Service invocation: the communication method for peer request/response interaction.

UAVCAN can automatically split long transmitted data into multiple CAN frames through serialized message and service data structures, allowing nodes to exchange data structures of arbitrary size.

Communication uses CAN2.0B standard data frames. The factory default CAN baud rate is 1M, and the baud rate is configurable in the range 10K~1M; the communication address and CAN baud rate (communication station address) can be set through the host software.

## 2 UAVCAN instructions

**Message frame instructions:**

| UAVCAN instruction | UAVCAN signature | Description |  |
| --- | --- | --- | --- |
| 341(0x0155) | None | Node status instruction | Servo heartbeat instruction |
| 1020(0x03FC) | None | Torque switch instruction |  |
| 2011(0x07DB) | None | Single motor position control instruction |  |
| 2012(0x07DC) | 56 D7 8A D5 6C 8A 65 3A | Multi-motor position control instruction |  |
| 2013(0x07DD) | E4 81 9D 8E 5B 7B 80 65 | Data feedback instruction | Auto-report instruction |
| 2014(0x07DE) | None | Auto-report start/stop instruction |  |

**Service frame instructions:**

| UAVCAN instruction | UAVCAN signature | Description |
| --- | --- | --- |
| 250(0xFA) | 4F A9 E7 BE A3 6E B3 EC | Parameter read instruction, parameters are big-endian first |
| 251(0xFB) | 8C E7 80 A1 F9 E4 C7 68 | Parameter write instruction, parameters are big-endian first |
| 252(0xFC) | None | Servo restart instruction |

**Note: when data is transmitted in multi-frame format, the signature is prepended to the data for the CRC calculation**

### 2.1 Node status instruction

|  | CAN-ID | DLC | Data |
| --- | --- | --- | --- |
| Rx | 18015500+NODE_ID | 8 | Frame count (4 bytes), fault code (1 byte), status code (2 bytes), frame tail (1 byte) |

- CAN-ID: default value 0x18015564; the servo node ID (NODE_ID) defaults to 100, with a range of 1~127, used to identify the node status of different servos
- Frame count (4 bytes): a count value from 0 ~ (2^32-1), incremented by one for each frame sent
- Fault code (1 byte): values as follows
    - Fatal fault: 0xC0, magnetic encoder error, undervoltage
    - Major fault: 0x40, overload, overheating
    - Minor fault: 0x80, overvoltage
    - No fault: 0x00
- Status code (2 bytes): refer to the servo status code
- Frame tail (1 byte): C0+Transfer_ID, Transfer_ID ranges 0 ~ 31 and is incremented by one for each frame sent

**Note¹: the node status instruction is auto-reported at a default frequency of 1Hz; the frequency can be modified with the FC software**
**Note²: the servo NODE_ID on the bus must be unique, and can be modified with the FC software**

### 2.2 Torque switch instruction

|  | CAN-ID | DLC | Data |
| --- | --- | --- | --- |
| Tx | 1003FC01 | 3 | Servo channel (1 byte), torque instruction (1 byte), frame tail (1 byte) |

- Servo channel (1 byte): range 0 ~ 17
- Torque instruction (1 byte): 0 means release torque, 1 means engage torque
- Frame tail (1 byte): C0

**Note: the position instruction automatically engages the servo torque; this instruction can release the servo torque so the servo enters the free state**

### 2.3 Single motor position control instruction

|  | CAN-ID | DLC | Data |
| --- | --- | --- | --- |
| Tx | 1007DB01 | 4 | Servo channel (1 byte), position data (2 bytes), frame tail (1 byte) |

- Servo channel (1 byte): range 0 ~ 17
- Position data (2 bytes): range -8192 ~ 8191, corresponding to a 360-degree angle, 1LSB: sensor resolution, negative values in little-endian format are two's complement
- Frame tail (1 byte): C0

**Note: the servo's default channel is 0 and can be modified with the FC software**

### 2.4 Multi-motor position control instruction

#### 2.4.1 Controlling fewer than 3 servos

|  | CAN-ID | DLC | Data |
| --- | --- | --- | --- |
| Tx | 1007DC01 | 7 | Channel 0 position (2 bytes), channel 1 position (2 bytes), channel 2 position (2 bytes), frame tail (1 byte) |

- Channel x position (2 bytes): x ranges 0 ~ 2, position range -8192 ~ 8191, corresponding to a 360-degree angle, 1LSB: sensor resolution, negative values in little-endian format are two's complement
- Frame tail (1 byte): C0

**Note: the servo channels in the instruction can only be 0 ~ 2**

#### 2.4.2 Controlling more than 3 servos

|  | CAN-ID | DLC | Data |
| --- | --- | --- | --- |
| Tx1 | 1007DC01 | 8 | Checksum (2 bytes), channel 0 position (2 bytes), channel 1 position (2 bytes), channel 2 position (low byte), frame tail (1 byte) |
| Tx2 | 1007DC01 | 8 | Channel 2 position (high byte), channel 3 position (2 bytes), channel 4 position (2 bytes), channel 5 position (2 bytes), frame tail (1 byte) |
| Tx3 | 1007DC01 | 8 | Channel 6 position (2 bytes), channel 7 position (2 bytes), channel 8 position (2 bytes), channel 9 position (low byte), frame tail (1 byte) |
| Tx4 | 1007DC01 | 8 | Channel 9 position (high byte), channel 10 position (2 bytes), channel 11 position (2 bytes), channel 12 position (2 bytes), frame tail (1 byte) |
| Tx5 | 1007DC01 | 8 | Channel 13 position (2 bytes), channel 14 position (2 bytes), channel 15 position (2 bytes), channel 16 position (low byte), frame tail (1 byte) |
| Tx6 | 1007DC01 | 4 | Channel 16 position (high byte), channel 17 position (2 bytes), frame tail (1 byte) |

- Checksum (2 bytes): refer to the checksum chapter
- Channel x position (2 bytes): x ranges 0 ~ 17, position range -8192 ~ 8191, corresponding to a 360-degree angle, 1LSB: sensor resolution, negative values in little-endian format are two's complement
- Frame tail (1 byte):
    - Tx1: 80, start frame, BIT5 = 0
    - Tx2: 20, middle frame, BIT5 toggled relative to the previous frame
    - Tx3: 00, middle frame, BIT5 toggled relative to the previous frame
    - Tx4: 20, middle frame, BIT5 toggled relative to the previous frame
    - Tx5: 00, middle frame, BIT5 toggled relative to the previous frame
    - Tx6: 60, end frame, BIT5 toggled relative to the previous frame

**Note: the instructions above can control 18 servos; in practice the instructions can be increased or reduced according to the number of servo channels**

### 2.5 Data feedback auto-report instruction

|  | CAN-ID | DLC | Data |
| --- | --- | --- | --- |
| Rx1 | 1807DD00+NODE_ID | 8 | Checksum (2 bytes), servo channel (1 byte), target position (2 bytes), current position (2 bytes), frame tail (1 byte) |
| Rx2 | 1807DD00+NODE_ID | 8 | Servo voltage (2 bytes), servo current (2 bytes), servo PCB temperature (1 byte), servo motor temperature (1 byte), servo status (1 byte), frame tail (1 byte) |

- CAN-ID: default value 0x1807DD64; the servo node ID (NODE_ID) defaults to 100, with a range of 1~127, modifiable with the FC software, used to identify the feedback data of different servos
- Servo channel (1 byte): range 0 ~ 17, the servo default channel is 0, modifiable with the FC software
- Target position (2 bytes): range -8192 ~ 8191, corresponding to a 360-degree angle, 1LSB: sensor resolution, negative values in little-endian format are two's complement
- Current position (2 bytes): range -8192 ~ 8191, corresponding to a 360-degree angle, 1LSB: sensor resolution, negative values in little-endian format are two's complement
- Servo voltage (2 bytes): 1LSB:0.1V
- Servo current (2 bytes): 1LSB: current-sampling circuit resolution
- Servo PCB temperature (1 byte): temperature of the servo PCB MOS, 1LSB:1 degree
- Servo motor temperature (1 byte): 1LSB:1 degree; invalid if the servo motor has no temperature sensor
- Servo status (1 byte):
    - Bit0: 0 means normal, 1 means the driver is faulty, such as magnetic encoder error, automatic recovery when normal
    - Bit1: 0 means normal, 1 means a uavcan instruction error, CRC error, illegal instruction, or illegal frame, automatic recovery upon receiving a normal instruction
    - Bit2: 0 means normal, 1 means motor force loss
    - Bit3: 0 means normal, 1 means the motor is stalled/overloaded, automatic torque recovery when normal
    - Bit4: 0 means normal, 1 means the driver MOS is overheated, automatic recovery when the temperature is normal
    - Bit5: 0 abnormal, 1 means the motor is overheated, automatic recovery when the temperature is normal
    - Bit6: 0 means normal, 1 means undervoltage/overvoltage, automatic recovery when the voltage is normal
- Frame tail (1 byte):
    - Rx1: 80+Transfer_ID, start frame, BIT5 = 0
    - Rx2: 60+Transfer_ID, end frame, BIT5 toggled relative to the previous frame
    - Transfer_ID ranges 0 ~ 31; the frame tails above share the same Transfer_ID, which is incremented by one after every two complete frames received

**Note¹: the data feedback instruction is auto-reported at a default frequency of 10Hz; the frequency can be modified with the FC software**
**Note²: the servo NODE_ID on the bus must be unique; servo channels may be identical — identical channels generally refer to servos performing the same action; the servo NODE_ID and servo channel can be modified with the FC software**

### 2.6 Auto-report start/stop instruction

|  | CAN-ID | DLC | Data |
| --- | --- | --- | --- |
| Tx | 1007DE01 | 3 | Servo NODE_ID (1 byte), switch instruction (1 byte), frame tail (1 byte) |

- Servo NODE_ID (1 byte): range 0~127, 0 means all servos
- Switch instruction (1 byte): 0 means pause, 5 means start
- Frame tail (1 byte): C0

### 2.7 Parameter write instruction

|  | CAN-ID | DLC | Data |
| --- | --- | --- | --- |
| Tx | 10FB8081+(NODE_ID<<8) | 4+L*2 | Parameter address (2 bytes), parameter length L (1 byte), parameter data 1 (2 bytes) ... parameter data L (2 bytes), frame tail (1 byte) |
| Rx | 10FB0180+NODE_ID | 2 | Write status (1 byte), frame tail (1 byte) |

- CAN-ID:
    - Tx: 0x10FB8081+(NODE_ID<<8), NODE_ID defaults to 100, CAN-ID default value 0x10FBE481
    - Rx: 0x10FB0180+NODE_ID, NODE_ID defaults to 100, CAN-ID default value 0x10FB01E4
- Parameter address (2 bytes): refer to the memory table address
- Parameter length L (1 byte): parameter length L
- Parameter data 1 (2 bytes): refer to the memory table data
- Parameter data L (2 bytes): refer to the memory table data, L<=2
- Write status (1 byte): 0 means normal, 1 means invalid address, 2 means invalid parameter
- Frame tail (1 byte): C0

### 2.8 Parameter read instruction

|  | CAN-ID | DLC | Data |
| --- | --- | --- | --- |
| Tx | 10FA8081+(NODE_ID<<8) | 4 | Parameter address (2 bytes), parameter length L (1 byte), frame tail (1 byte) |
| Rx | 10FA0180+NODE_ID | 3+L*2 | Read status (1 byte), parameter length L (1 byte), parameter data 1 (2 bytes) ... parameter data L (2 bytes), frame tail (1 byte) |

- CAN-ID:
    - Tx: 0x10FA8081+(NODE_ID<<8), NODE_ID defaults to 100, CAN-ID default value 0x10FAE481
    - Rx: 0x10FA0180+NODE_ID, NODE_ID defaults to 100, CAN-ID default value 0x10FA01E4
- Parameter address (2 bytes): refer to the memory table address
- Parameter length L (1 byte): parameter length L
- Parameter data 1 (2 bytes): refer to the memory table data
- Parameter data L (2 bytes): refer to the memory table data, L<=2
- Write status (1 byte): 0 means normal, 1 means invalid address, 2 means invalid parameter
- Frame tail (1 byte): C0

## 3 UAVCAN protocol CRC check

**Note: this chapter covers the checksum calculation for multi-frame instructions; single-frame instructions may skip this section**

**The multi-frame data is composed as follows:**

| UAVCAN data frame 1 | UAVCAN data frame 2 | ... | UAVCAN data frame N |
| --- | --- | --- | --- |
| Byte0 ~ Byte7 | Byte0 ~ Byte7 | ... | Byte0 ~ ByteX |

- UAVCAN data frame 1: Byte0 and Byte1 are the CRC checksum (little-endian format), Byte2 ~ Byte6 are valid data, Byte7 is the frame tail
- UAVCAN data frame 2: Byte0 ~ Byte6 are valid data, Byte7 is the frame tail
- UAVCAN data frame N: Byte0 ~ Byte(X-1) are valid data, ByteX is the frame tail, X<8

**The data participating in the CRC calculation is composed as follows:**

| UAVCAN signature | UAVCAN data frame 1 | UAVCAN data frame 2 | ... | UAVCAN data frame N |
| --- | --- | --- | --- | --- |
| Signature (8 bytes) | Byte2 ~ Byte6 | Byte0 ~ Byte6 | ... | Byte0 ~ Byte(X-1) |

- UAVCAN signature: the signature differs per instruction; for signature encoding refer to UAVCAN instructions
- UAVCAN data frame 1: Byte2 ~ Byte6 valid data participate in the CRC calculation
- UAVCAN data frame 2: Byte0 ~ Byte6 valid data participate in the CRC calculation
- UAVCAN data frame N: Byte0 ~ Byte(X-1) valid data participate in the CRC calculation

**The CRC check algorithm is as follows:**

- Check format: CRC-16-CCITT-FALSE
- Reference: http://reveng.sourceforge.net/crc-catalogue/16.htm#crc.cat.crc-16-ccitt-false
- Initial value: 0xFFFF
- Polynomial: 0x1021
- Reflected: no
- XOR: 0

```cpp
/*
 * License: CC0, no copyright reserved.
 */

#include <iostream>
#include <cstdint>
#include <cassert>

class TransferCRC
{
    std::uint16_t value_;

public:
    TransferCRC()
      : value_(0xFFFFU)
    { }

    void add(std::uint8_t byte)
    {
        value_ ^= static_cast<std::uint16_t>(byte) << 8;
        for (std::uint8_t bit = 8; bit > 0; --bit)
        {
            if (value_ & 0x8000U)
            {
                value_ = (value_ << 1) ^ 0x1021U;
            }
            else
            {
                value_ = (value_ << 1);
            }
        }
    }

    void add(const std::uint8_t* bytes, unsigned len)
    {
        assert(bytes);
        while (len--)
        {
            add(*bytes++);
        }
    }

    std::uint16_t get() const { return value_; }
};

int main()
{
    TransferCRC crc;
    crc.add(reinterpret_cast<const std::uint8_t*>("123456789"), 9);
    std::cout << std::hex << "0x" << crc.get() << std::endl;
}
```
