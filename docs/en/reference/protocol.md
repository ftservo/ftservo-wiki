# Protocol and Memory Tables

FEETECH bus servos use addressed serial packets. The SDKs wrap Ping, read, write and synchronized operations; inspect the matching SDK before reimplementing checksum, byte order, timeout and status handling.

| Layer | Verify |
| --- | --- |
| Physical | TTL or RS485, voltage levels, half-duplex direction, wiring, ground |
| Packet | ID, instruction, length, parameters, checksum, response policy |
| Memory table | Address, width, access, unit, range, persistence |

A common failure is successful packet communication with the wrong series' register address or unit.

Before every write, confirm full model, table revision, address, width, allowed range, RAM/persistent storage, torque-disable requirements and restart behavior. Keep a change record for IDs, baud rate, modes, limits and calibration.

- [Official service resources](https://www.feetechrc.com/service.html)
- [Legacy online documentation](http://doc.feetech.cn/#/f?q=2506a8cb7928)
- [Official SDK source](https://github.com/ftservo)

!!! danger
    Never guess a register without the exact model and memory-table revision. An incorrect persistent write can change ID, baud rate, operating mode or protection and may cause loss of communication or unexpected motion.

