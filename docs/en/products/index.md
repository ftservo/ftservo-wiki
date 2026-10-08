# FEETECH servo specifications

Browse FEETECH servos by product series. Product cards show input voltage, stall torque and control interface; open a model for power, control and usage guidance.

If you have not selected a series, see [Series and interfaces](./series.md) for how the families differ, or use the [product selector](../index.md) to filter by application.

| Product series | Models | Series characteristics | Suitable applications | Catalog |
| --- | ---: | --- | --- | --- |
| HD | 1 | Compact TTL serial-bus servo with a coreless motor, metal gears, and dual-shaft structure | Microduck and Open Duck-style bipeds, lightweight joints, and embodied-AI prototypes | [View products](./datasheets/hd.md) |
| HL | 17 | HLS application layer and half-duplex TTL bus with position, speed, current, and other status feedback | Robot joints, coordinated axes, and automated mechanisms that need operating feedback | [View products](./datasheets/hl.md) |
| PWM | 86 | Standard PWM control without bus IDs, offered across a broad range of sizes and torque levels | RC models, gimbals, mechanisms, and single-axis position control | [View products](./datasheets/pwm.md) |
| FU | 1 | CAN (UAVCAN) bus with a brushless motor, titanium-gear metal housing, and IP66 protection | Multi-joint robots that need CAN networking, outdoor or industrial settings | [View products](./datasheets/fu.md) |
| SC | 18 | SCS/SCSCL application layer and half-duplex TTL bus with ID addressing and status reads | Education robots, compact arms, and small multi-servo systems | [View products](./datasheets/sc.md) |
| SM | 27 | SMS application layer and differential RS485 bus for longer cables and demanding electrical environments | Industrial automation, distributed joints, and longer-distance multi-servo links | [View products](./datasheets/sm.md) |
| ST | 20 | STS application layer and half-duplex TTL bus; many models use magnetic encoders or support high-resolution control | Robot joints, wheeled mechanisms, and projects that need detailed motion feedback | [View products](./datasheets/st.md) |

!!! info "Selection note"
    Models in the same series may use different input voltages, torque ratings, travel and dimensions. Use the individual model page and allow design margin for the real load and duty cycle.
