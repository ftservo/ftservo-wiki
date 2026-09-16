<div class="ft-hero" markdown>

# FEETECH Developer Wiki

One path from servo selection, power and FD setup to Python, Arduino, Linux and STM32 development.

[Choose a servo](products/index.md){ .md-button .md-button--primary }
[Run your first test](getting-started/index.md){ .md-button }

</div>

!!! warning "Identify the exact model first"
    Models in one series may still use different voltages, interfaces, travel or memory tables. Before applying power or writing a register, verify the label, exact-model datasheet and memory table.

<div class="grid cards" markdown>

-   :material-tune-variant: **Product selection**

    Filter by interface, voltage, torque, speed, dimensions, feedback and application.

    [Open the guide](products/index.md)

-   :material-file-document-multiple: **Servo datasheets**

    Browse the 185 PDFs in the HL, PWM, SC, SM and ST source folders; verify each cover model and revision.

    [Browse datasheets](products/datasheets/index.md)

-   :material-power-plug: **Five-step startup**

    Power safely, connect an adapter, discover one device, test slowly, then use an SDK.

    [Start here](getting-started/index.md)

-   :material-console: **Tools and SDKs**

    FD plus official Python, Arduino/ESP32, Linux C++ and STM32 HAL SDKs.

    [Choose a platform](sdk/index.md)

-   :material-robot-industrial: **Develop with AI**

    Give an AI tool the complete repository, exact hardware facts and a safe verification plan.

    [AI workflow](ai-development.md)

</div>

## Recommended path

```text
Confirm model and electrical specifications
       ↓
One unloaded servo + adapter + independent power supply
       ↓
Discover in FD, assign a unique ID, test at low speed
       ↓
Start from the matching SDK example
       ↓
Add mechanical load, multiple servos and safety limits
```

## Official resources

- [FEETECH website](https://www.feetechrc.com/)
- [FEETECH on GitHub](https://github.com/ftservo)
- [Legacy online documentation](http://doc.feetech.cn/#/f?q=2506a8cb7928)
- [Downloads](downloads.md)
- [Engineering resources and publication backlog](resources/index.md)
