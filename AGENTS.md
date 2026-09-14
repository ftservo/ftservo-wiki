# FEETECH Wiki instructions for AI coding agents

This repository contains the bilingual FEETECH documentation site and official
SDKs as Git submodules.

## Ground rules

- Documentation source is `docs/`; Chinese files are at `docs/` and their
  English counterparts use the same path under `docs/en/`.
- Keep Chinese and English navigation and page coverage in sync.
- Never infer a servo's voltage, register address, resolution, current limit or
  mechanical limit from a different series. Use the exact model's official
  datasheet and memory table.
- SCS, STS/SMS and HLS application layers and memory tables are not
  interchangeable even when their packet protocol is similar.
- Treat motion as safety-critical: validate power, shared ground, interface,
  ID, baud rate and mechanical clearance before enabling torque.
- Do not commit generated `site/`, virtual environments, credentials or caches.
- Rust SDK work is intentionally out of scope until a separate design and test
  plan is approved.

## Verification

Run `mkdocs build --strict` after documentation changes. For SDK changes, use
the affected SDK's own build/test instructions and state the exact hardware
model used for any hardware test.

