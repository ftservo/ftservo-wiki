# Develop with AI

This repository places tutorials, constraints and official SDKs in one context so repository-aware tools such as Codex, Claude Code or Cursor can use real APIs instead of guessing the protocol.

## Get the complete context

```bash
git clone --recurse-submodules https://github.com/ftservo/ftservo-wiki.git
cd ftservo-wiki
```

Open the entire folder in the AI tool. It should read `AGENTS.md`, relevant documentation, matching SDK examples and the exact model's memory table.

Provide the full servo model and series, product specification page, TTL or RS485 interface, adapter, port, supply, ID, baud rate, target platform and toolchain, desired behavior, motion limits, timeout and safe-stop behavior, completed FD tests and exact errors.

## Prompt template

```text
Read AGENTS.md, the relevant docs, and the README plus same-series examples in
sdk/<matching-sdk> before editing.

Hardware: <full model>, <TTL or RS485>, supply <voltage>, ID <ID>, baud <rate>,
adapter <model>, port <port>.
Platform: <OS/MCU/framework and versions>.
Goal: <behavior>.
Safety limits: <position, speed, timeout and emergency-stop policy>.

First list the registers, units and ranges confirmed from exact-model sources;
do not guess missing facts. Build a minimal project from the nearest official
example with configuration, timeout, error handling, safe stop and README.
Implement read-only Ping first, then a small low-speed move. Finish with tests
that need no hardware, real-hardware steps, and unresolved human checks.
```

## Review generated code

Confirm the correct `SCSCL`, `SMS_STS` or `HLSCL` layer; audit every address, width, unit and range; prevent startup jumps; handle exceptions, Ctrl+C, disconnects and timeouts safely; and test without hardware before one unloaded servo.

!!! danger
    AI can produce syntactically correct code with incorrect registers. A hardware-qualified person must review motion commands and verify them where actuator power can be removed immediately.

## Future Rust SDK

Treat Rust as a separate project: freeze a support matrix and packet test vectors, design serial abstraction, typed memory tables and error/timeouts, add cross-platform CI, then validate every supported series on real hardware. This release intentionally includes no misleading stub SDK.
