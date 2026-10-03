# MODBUS-RTU Protocol

## 1 Protocol overview

Communication uses the MODBUS-RTU protocol (national standard GB/T19582-2008). One master node controls multiple slave nodes; the bundled host software can configure 247 slave addresses (0 is the broadcast address, 1-247 are unicast addresses). The master can be a microcontroller, a PLC, a PC, etc.

## 2 Communication parameters

Factory default serial settings: baud rate defaults to 115200bps, 8 data bits, no parity, 1 stop bit; the baud rate is configurable in the range 4800~256k0bps, and the drive's default communication address (station number) is 1.

## 3 modbus-rtu frame format

This drive supports modbus 0x03 (read holding registers), 0x06 (write single register), 0x10 (write multiple registers), and 0x83 (exception code); the exception codes support 0x01 (operation code error) and 0x02 (address error).

### 3.1 Read holding registers 0x03

**Sent by the master:**

| Byte | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Content | Slave address | 0x03 | Register address high byte | Register address low byte | Read data length high byte | Read data length low byte | CRC high byte | CRC low byte |

Byte 1, slave address: slave address code (1~247)
Byte 2, 0x03: read register value function code
Bytes 3 and 4: start address of the registers to read
Bytes 5 and 6: read data length
Bytes 7 and 8: CRC16 checksum of bytes 1 to 6

**Normal response from the slave:**

| Byte | 1 | 2 | 3 | 4, 5 | 6, 7 |  | n-1, n | n+1 | n+2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Content | Slave address | 0x03 | Total register bytes | Register data 1 | Register data 2 | ... | Register data m | CRC high byte | CRC low byte |

Byte 1, slave address: slave address code (1~247)
Byte 2, 0x03: read register value function code
Byte 3: total number of register bytes from 4 to n (including 4 and n)
Bytes 4~n: the m register data values read, where m=(n-3)/2, n-1 is the high byte, and n is the low byte
Bytes n+1 and n+2: CRC16 checksum of bytes 1 to n

**Exception response from the slave:**

| Byte | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| Content | Slave address | 0x83 | 0x02 | CRC high byte | CRC low byte |

### 3.2 Write single register 0x06

**Sent by the master:**

| Byte | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Content | Slave address | 0x06 | Register address high byte | Register address low byte | Register data high byte | Register byte count low byte | CRC high byte | CRC low byte |

Byte 1, slave address: slave address code (1~247)
Byte 2, 0x06: write single register function code
Bytes 3 and 4: address of the register to write
Bytes 5 and 6: register data to write
Bytes 7 and 8: CRC16 checksum of bytes 1 to 6

**Normal response from the slave:**

| Byte | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Content | Slave address | 0x06 | Register address high byte | Register address low byte | Register data high byte | Register byte count low byte | CRC high byte | CRC low byte |

**Exception response from the slave:**

| Byte | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| Content | Slave address | 0x86 | Exception code | CRC high byte | CRC low byte |

Exception codes: 0x02 means the address requested by the master is invalid, 0x03 means the requested data is invalid

### 3.3 Write multiple registers 0x10

**Sent by the master:**

| Byte | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8, 9 | 10, 11 |  | n-1, n | n+1 | n+2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Content | Slave address | 0x10 | Register address high byte | Register address low byte | Register length high byte | Register length low byte | Total register bytes | Register data 1 | Register data 2 | ... | Register data m | CRC high byte | CRC low byte |

Byte 1, slave address: slave address code (1~247)
Byte 2, 0x03: response read function code
Bytes 3 and 4: address of the registers to write; 3 is the high byte and 4 is the low byte
Bytes 5 and 6: length m of the registers to write
Byte 7: total number of bytes from 8 to n (including 8 and n)
Bytes 8~n: the m register data values written, where m=(n-7)/2, n-1 is the high byte, and n is the low byte
Bytes n+1 and n+2: CRC16 checksum of bytes 1 to n

**Normal response from the slave:**

| Byte | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Content | Slave address | 0x10 | Register address high byte | Register address low byte | Register length high byte | Register length low byte value | CRC high byte | CRC low byte |

Byte 1, slave address: slave address code (1~247)
Byte 2, 0x10: write multiple registers function code
Bytes 3 and 4: address of the registers to write
Bytes 5 and 6: register length to write
Bytes 7 and 8: CRC16 checksum of bytes 1 to 6

**Exception response from the slave:**

| Byte | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| Content | Slave address | 0x90 | Exception code | CRC high byte | CRC low byte |

Exception codes: 0x02 means the address requested by the master is invalid, 0x03 means the requested data is invalid

### 3.4 Query bus slave device ID 0x11

**Sent by the master:**

| Byte | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |
| Content | Slave address | 0x11 | CRC high byte | CRC low byte |

Byte 1, slave address: slave address code (1~247); the broadcast ID 0 may be used for the query only when a single slave device is connected to the ID bus
Byte 2, 0x11: function code
Bytes 3 and 4: CRC16 checksum of bytes 1 to 3

**Normal response from the slave:**

| Byte | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Content | Slave address | 0x17 | 3 | Slave address | Status code high byte | Status code low byte | CRC high byte | CRC low byte |

Byte 1, slave address: slave address code (1~247)
Byte 2, 0x11: function code
Byte 3: number of valid bytes returned
Byte 4: slave address code (1~247)
Bytes 6 and 7: status code
Bytes 8 and 9: CRC16 checksum of bytes 1 to 6

### 3.5 Restart the slave device with the specified ID 0x41

**Sent by the master:**

| Byte | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |
| Content | Slave address | 0x41 | CRC high byte | CRC low byte |

Byte 1, slave address: slave address code (1~247); using 0 as the broadcast ID restarts all slave devices on the bus
Byte 2, 0x41: function code
Bytes 3 and 4: CRC16 checksum of bytes 1 to 3
