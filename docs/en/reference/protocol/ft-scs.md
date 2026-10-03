# FT-SCS Protocol (Servo SCS Communication Protocol)

This page is a transcription of the official *Servo SCS Communication Protocol*. It is the FT-SCS custom protocol — the instruction-frame and status-frame framework — shared by the SCS/SCSCL, STS, SMS, and HLS families described in [Bus Protocol](index.md). See [Memory Table Parameters](../parameter/index.md) for each family's memory table.

## 1 Protocol overview

The communication level uses a TTL level scheme compatible with high-speed communication and an RS485 scheme with strong noise immunity. Communication is still asynchronous duplex: sending and receiving are handled asynchronously.

The controller and the servos communicate in a request/response manner: the controller sends an instruction frame, and the servo returns a status frame.

A bus control network may contain multiple servos, so every servo is assigned a network-unique ID. The control instruction sent by the controller carries ID information; only the servo matching that ID receives the instruction in full and returns a response.

Communication is serial and asynchronous. One frame consists of 1 start bit, 8 data bits, and 1 stop bit, with no parity bit — 10 bits in total.

When a memory-table parameter uses a two-byte value range, the order of the two bytes depends on the servo type: potentiometer-type servos use big-endian format (high byte first, low byte last), while magnetic-encoder-type servos use little-endian format (low byte first, high byte last). Each servo differs slightly in features, so refer to the memory table of the specific model for actual control.

## 2 Instruction frame

| Header | ID | Length | Instruction | Parameter | Check Sum |
| --- | --- | --- | --- | --- | --- |
| 0xFF 0xFF | ID | Length | Instruction | Parameter1 ... Parameter N | Check Sum |

- Header: two consecutive 0xFF bytes indicate that a data packet has arrived.
- ID: every servo has an ID. The ID range is 0–253, expressed in hexadecimal as 0x00–0xFD.
- Broadcast ID: ID 254 is the broadcast ID. If the controller sends ID 254 (0xFE), all servos receive the instruction, but except for the PING instruction none of them returns a response (the broadcast PING instruction cannot be used when multiple servos are connected to the bus).
- Length: equals the number of parameters N to be sent plus 2, that is "N+2".
- Instruction: the function code of the packet; see section 4 Instruction types.
- Parameter: additional control information required by the instruction. A parameter supports up to two bytes to represent one memory value; for byte order refer to the servo's manual and memory control table (byte order differs between models).
- Check Sum: the checksum is calculated as follows

```text
Check Sum = ~(ID + Length + Instruction + Parameter 1 + ... Parameter N)
```

If the sum inside the parentheses exceeds 255, take the lowest byte. "~" means bitwise inversion.

## 3 Status frame

| Header | ID | Length | Status | Parameter | Check Sum |
| --- | --- | --- | --- | --- | --- |
| 0xFF 0xFF | ID | Length | ERROR | Parameter1 ... Parameter N | Check Sum |

The returned status frame contains the servo's current status ERROR. If the servo is not working normally, this byte reflects it (see the manual's memory control table for the meaning of each status). If ERROR is 0, the servo has no alarm information.

## 4 Instruction types

| Instruction | Function | Value | Parameter length |
| --- | --- | --- | --- |
| PING (query) | Query the working status | 0x01 | 0 |
| READ DATA (read) | Read data from the control table | 0x02 | 2 |
| WRITE DATA (write) | Write data into the control table | 0x03 | not less than 2 |
| REGWRITE DATA (asynchronous write) | Similar to WRITE DATA, but the control characters do not act immediately after being written, until the ACTION instruction arrives | 0x04 | not less than 4 |
| ACTION (execute asynchronous write) | Trigger the action written by REG WRITE | 0x05 | 0 |
| SYNCREAD DATA (synchronous read) | Used to query multiple servos at the same time | 0x82 | not less than 3 |
| SYNCWRITE DATA (synchronous write) | Used to control multiple servos at the same time | 0x83 | not less than 2 |
| RESET (status reset) | Reset the servo status (reset the servo turn count) | 0x0A | 0 |
| Position calibration | Recalibrate the current position to the instruction value | 0x0B | 0 |
| Parameter recovery instruction | Restore all servo parameters except the ID | 0x06 | 0 |
| Parameter backup instruction | Back up the current parameters, for use by the recovery instruction | 0x09 | 0 |
| Restart instruction | Used to restart the servo | 0x08 | 0 |

### 4.1 PING — query status instruction

- Function: read the servo's working status
- Length: 0x02
- Instruction: 0x01
- Parameter: none

The PING instruction uses the broadcast address, and the servo still returns a response.

**Example 1: read the working status of the servo with ID 1.**

Instruction frame: FF FF 01 02 01 FB (send in hexadecimal)

```text
Header: FF FF
ID: 01
Length: 02
Instruction: 01
Check Sum: FB
```

Status frame: FF FF 01 02 00 FC (displayed in hexadecimal)

```text
Header: FF FF
ID: 01
Length: 02
Status: 00
Check Sum: FC
```

### 4.2 READ DATA — read instruction

- Function: read data out of the servo memory control table
- Length: 0x04
- Instruction: 0x02
- Parameter 1: the start address of the data segment to be read out
- Parameter 2: the length of the data to be read

**Example 2: read the current position of the servo with ID 1 (low byte first, high byte last). The memory-table address of the position parameter is 0X38, spanning two consecutive bytes.**

Instruction frame: FF FF 01 04 02 38 02 BE (send in hexadecimal)

```text
Header: FF FF
ID: 01
Length: 04
Instruction: 02
Parameter: 38 02(current position address, read data length)
Check Sum: BE
```

Status frame: FF FF 01 04 00 18 05 DD (displayed in hexadecimal)

```text
Header: FF FF
ID: 01
Length: 04
Status: 00
Parameter: 18 05
Check Sum: DD
```

The two bytes read out are (little-endian structure): low byte L 0x18, high byte H 0x05. Combining the two bytes gives the 16-bit data 0X0518, which in decimal means the current position is 1304.

### 4.3 WRITE DATA — write instruction

- Function: write data to the servo memory control table
- Length: N+2 (N is the parameter length)
- Instruction: 0x03
- Parameter 1: the start address of the data segment to be written
- Parameter 2: the 1st data value to write
- Parameter 3: the 2nd data value to write
- ...
- Parameter N: the n-th data value to write, N=n+1

**Example 3: use the broadcast ID (0xFE) to set the ID of a servo with any number to 1. In the memory table, the address that stores the ID is 5.**

Instruction frame: FF FF FE 04 03 05 01 F4 (send in hexadecimal)

```text
Header: FF FF
ID: 01
Length: 04
Instruction: 03
Parameter: 05 01(ID address, new ID value)
Check Sum: F4
```

Because the instruction is sent with the broadcast ID, no data is returned. In addition, the memory table EPROM has a protection lock switch; it must be turned off (set to 0) before changing the ID, otherwise the example ID will not be saved after power-off. For details, consult the memory table or operation manual of the specific servo model.

**Example 4: control servo ID1 to rotate to position 2048 at a speed of 1000 steps per second. The start address of the goal position in the memory table is 0x2A, so six consecutive bytes of data are written starting at address 0x2A.**

```text
position data 0x0800(2048)
reserved data 0x0000(0)
speed data 0x03E8(1000)
```

Instruction frame: FF FF 01 09 03 2A 00 08 00 00 E8 03 D5 (send in hexadecimal)

```text
Header: FF FF
ID: 01
Length: 09
Instruction: 03
Parameter: 2A(start address)
00 08(position)
00 00(reserved)
E8 03(speed)
Check Sum: D5
```

Status frame: FF FF 01 02 00 FC (displayed in hexadecimal)

```text
Header: FF FF
ID: 01
Length: 02
Status: 00
Check Sum: FC
```

A returned working status of 0 means the servo received the instruction correctly and has started executing it. The ID of the sent instruction packet uses a non-broadcast ID (0xFE), so the servo returns a status packet after receiving the instruction.

### 4.4 REG WRITE — asynchronous write instruction

The REG WRITE instruction is similar to WRITE DATA, only the execution time differs. When a REG WRITE instruction frame is received, the received data is stored in a buffer for later use and the asynchronous write flag register is set to 1. When the ACTION instruction is received, the stored instruction is finally executed.

- Length: N+2 (N is the parameter length)
- Instruction: 0x04
- Parameter 1: the start address of the area to which data is to be written
- Parameter 2: the 1st data value to write
- Parameter 3: the 2nd data value to write
- Parameter N: the n-th data value to write, N=n+1

**Example 5: control servos ID1 to ID10 to rotate to position 2048 at a speed of 1000 per second.**

```text
ID 1: asynchronous write instruction frame: FF FF 01 09 04 2A 00 08 00 00 E8 03 D4
ID 1: status frame: FF FF 01 02 00 FC
ID 2: asynchronous write instruction frame: FF FF 02 09 04 2A 00 08 00 00 E8 03 D3
ID 2: status frame: FF FF 02 02 00 FB
ID 3: asynchronous write instruction frame: FF FF 03 09 04 2A 00 08 00 00 E8 03 D2
ID 3: status frame: FF FF 03 02 00 FA
ID 4: asynchronous write instruction frame: FF FF 04 09 04 2A 00 08 00 00 E8 03 D1
ID 4: status frame: FF FF 04 02 00 F9
ID 5: asynchronous write instruction frame: FF FF 05 09 04 2A 00 08 00 00 E8 03 D0
ID 5: status frame: FF FF 05 02 00 F8
ID 6: asynchronous write instruction frame: FF FF 06 09 04 2A 00 08 00 00 E8 03 CF
ID 6: status frame: FF FF 06 02 00 F7
ID 7: asynchronous write instruction frame: FF FF 07 09 04 2A 00 08 00 00 E8 03 CE
ID 7: status frame: FF FF 07 02 00 F6
ID 8: asynchronous write instruction frame: FF FF 08 09 04 2A 00 08 00 00 E8 03 CD
ID 8: status frame: FF FF 08 02 00 F5
ID 9: asynchronous write instruction frame: FF FF 09 09 04 2A 00 08 00 00 E8 03 CC
ID 9: status frame: FF FF 09 02 00 F4
ID10: asynchronous write instruction frame: FF FF 0A 09 04 2A 00 08 00 00 E8 03 CB
ID10: status frame: FF FF 0A 02 00 F3
```

### 4.5 ACTION — execute asynchronous write instruction

- Function: trigger the REG WRITE instruction
- Length: 0x02
- Instruction: 0x05
- Parameter: none

1. The ACTION instruction is very useful when controlling multiple servos at the same time.
2. When controlling multiple servos, using the ACTION instruction lets the first and last servos execute their respective actions at the same time, with no delay in between.
3. When sending the ACTION instruction to multiple servos, the broadcast ID (0xFE) is used, so sending this instruction returns no data frame.

**Example 6: after sending the asynchronous write instructions that control servos ID1 to ID10 to rotate to position 2048 at a speed of 1000 per second, the asynchronous write instruction must be executed.**

```text
instruction frame: FF FF FE 02 05 FA
status frame: none
```

### 4.6 SYNC WRITE — synchronous write instruction

- Function: used to control multiple servos at the same time.
- ID: 0xFE
- Length: (L+1)*n+4 (L: the data length sent to each servo, n: the number of servos)
- Instruction: 0x83
- Parameter 1: the start address of the data to be written
- Parameter 2: the length (L) of the data to be written
- Parameter 3: the ID of the 1st servo
- Parameter 4: the 1st data value written to the 1st servo
- Parameter 5: the 2nd data value written to the 1st servo
- ...
- Parameter L+3: the L-th data value written to the 1st servo
- Parameter L+4: the ID of the 2nd servo
- Parameter L+5: the 1st data value written to the 2nd servo
- Parameter L+6: the 2nd data value written to the 2nd servo
- ...
- Parameter 2L+4: the L-th data value written to the 2nd servo
- ...

Unlike the REG WRITE + ACTION instruction, its real-time performance is higher. A single SYNC WRITE instruction can modify the control table contents of multiple servos at once, whereas the REG WRITE + ACTION instruction does it step by step. Even so, when using the SYNC WRITE instruction, the length of the written data and the start address at which the data is saved must be the same.

**Example 7: write position 0x0800 time 0X0000 and speed 0x03E8 starting at address 0x2A for a total of 4 servos ID1-ID4 (low byte first, high byte last).**

Instruction frame: FF FF FE 20 83 2A 06 01 00 08 00 00 E8 03 02 00 08 00 00 E8 03 03 00 08 00 00 E8 03 04 00 08 00 00 E8 03 58 (send in hexadecimal)

```text
Header: FF FF
ID: FE
Valid data length: 20
Instruction: 83
Parameter 1: 
2A 06(start address, data length)
01 00 08 00 00 E8 03(ID1 servo instruction)
02 00 08 00 00 E8 03(ID2 servo instruction)
03 00 08 00 00 E8 03(ID3 servo instruction)
04 00 08 00 00 E8 03(ID4 servo instruction)
Check Sum: 58
```

### 4.7 SYNC READ — synchronous read instruction

- Function: used to query multiple servos at the same time.
- ID: 0xFE
- Length: n+4 (n is the number of servos)
- Instruction: 0x82
- Parameter 1: the start address of the data to be read
- Parameter 2: the length of the data to be read
- Parameter 3: the ID of the 1st servo
- Parameter 4: the ID of the 2nd servo
- ...
- Parameter N: the ID of the n-th servo, N=n+2

A single SYNC READ instruction can query the control table contents of multiple servos at once. The synchronous read instruction specifies the IDs of the servos to be queried, and the servos return status packets in the order of the IDs in the instruction packet. When using the SYNC READ instruction, the data length queried and the start address of the data must be the same for all servos (this instruction is available for some serial bus servos).

**Example 8: query the current position, current speed, current load, current voltage, and current temperature of a total of 2 servos ID1-ID2 (start address 0x38, 8 words of data in total, low byte first, high byte last).**

Instruction frame: FF FF FE 06 82 38 08 01 02 36

```text
Header: FF FF
ID: FE
Length: 06
Instruction: 82
Parameter: 
38 08(data start address, data length)
01 02(ID01 ID02)
Check Sum: 36
```

Status frame:

```text
ID01 servo: FF FF 01 0A 00 00 08 00 00 00 00 79 1E 55
ID02 servo: FF FF 02 0A 00 FF 07 00 00 00 00 77 23 53
```

Status frames can be decoded as for the read instruction.

### 4.8 RESET — status reset instruction

- Function: reset the servo status (reset the servo turn count)
- Length: 0x02
- Instruction: 0x0A
- Parameter: none

**Example 9: reset the servo with ID 01.**

```text
instruction frame: FF FF 01 02 0A F2(send in hexadecimal)
status frame: FF FF 01 02 00 FC(displayed in hexadecimal)
```

### 4.9 Position calibration instruction

- Function: recalibrate the current position to the set value
- Length: 0x02 or 0x04
- Instruction: 0x0B
- Parameter: none, or the set value

**Note: a position calibration instruction with no parameter means the current position is calibrated to the middle position; the calibration instruction is supported only by some servo models — see the table below for model support.**

**Example 10: recalibrate the current position to the middle position.**

```text
instruction frame: FF FF 01 02 0B F1(send in hexadecimal)
status frame: FF FF 01 02 00 FC(displayed in hexadecimal)
```

**Example 11: recalibrate the current position to 1024.**

Instruction frame: FF FF 01 04 0B 00 04 EB (send in hexadecimal)

```text
Header: FF FF
ID: 01
Length: 04
Instruction: 0B
Set value: 00 04(1024)
Check Sum: EB
```

Status frame: FF FF 01 02 00 FC (displayed in hexadecimal)

```text
Header: FF FF
ID: 01
Length: 02
Status: 00
Check Sum: FC
```

| Servo model | Firmware version | Effective condition | Remarks |
| --- | --- | --- | --- |
| SMS servo | <=2.54 | none | Supports middle-position calibration by writing 128 to the torque switch |
| STS servo | >=3.10 | none | Supports instructions with and without parameters, and middle-position calibration by writing 128 to the torque switch |
| HLS servo | >=3.43 | none | Supports instructions with and without parameters, but not middle-position calibration by writing 128 to the torque switch |

### 4.10 Parameter recovery instruction

- Function: restore all servo parameters except the ID
- Length: 0x02
- Instruction: 0x06
- Parameter: none

**Example 11: restore the servo parameters.**

```text
instruction frame: FF FF 01 02 06 F6(send in hexadecimal)
status frame: FF FF 01 02 00 FC(displayed in hexadecimal)
```

**Note: unlock the eprom parameters before restoring the servo parameters.**

### 4.11 Parameter backup instruction

- Function: parameter backup (for use by the parameter recovery instruction)
- Length: 0x02
- Instruction: 0x09
- Parameter: none

**Example 12: back up the servo parameters.**

```text
instruction frame: FF FF 01 02 09 F3(send in hexadecimal)
status frame: FF FF 01 02 00 FC(displayed in hexadecimal)
```

**Note: unlock the eprom parameters before backing up the servo parameters.**

### 4.12 Restart instruction

- Function: restart instruction (restart the servo)
- Length: 0x02
- Instruction: 0x08
- Parameter: none

**Example 13: restart the servo.**

```text
instruction frame: FF FF 01 02 08 F4(send in hexadecimal)
status frame: none(restart time about 1800ms)
```

**Note: turn off the torque switch before restarting the servo.**
