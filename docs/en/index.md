<div class="ft-hero" markdown>

# FEETECH Developer Wiki

One path from servo selection, power and FD setup to Python, Arduino, Linux and STM32 development.

[Choose a servo](products/index.md){ .md-button .md-button--primary }
[Run your first test](getting-started/index.md){ .md-button }

</div>

!!! warning "Identify the exact model first"
    Models in one series may use different voltages, interfaces, travel or memory tables. Before applying power or writing a register, check the product label, model specifications and matching memory table.

<div class="grid cards" markdown>

-   :material-tune-variant: **Product selection**

    Filter by interface, voltage, torque, speed, dimensions, feedback and application.

    [Open the guide](products/index.md)

-   :material-file-document-multiple: **Product specifications**

    Browse product cards and detailed specifications by HD, HL, PWM, SC, SM and ST series.

    [Browse product specifications](products/datasheets/index.md)

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

<div class="ft-route">
  <a class="ft-route-step" href="products/">
    <span class="ft-route-number">01</span>
    <span class="ft-route-copy"><strong>Confirm the model and ratings</strong><small>Verify interface, input voltage, torque, dimensions and model specifications</small></span>
  </a>
  <a class="ft-route-step" href="getting-started/wiring/">
    <span class="ft-route-number">02</span>
    <span class="ft-route-copy"><strong>Build a safe test setup</strong><small>Use one servo, the correct adapter, independent power and a shared ground</small></span>
  </a>
  <a class="ft-route-step" href="getting-started/first-motion/">
    <span class="ft-route-number">03</span>
    <span class="ft-route-copy"><strong>Run the first motion</strong><small>Discover in FD, assign a unique ID and test unloaded at low speed</small></span>
  </a>
  <a class="ft-route-step" href="sdk/">
    <span class="ft-route-number">04</span>
    <span class="ft-route-copy"><strong>Use the matching SDK</strong><small>Choose by family and platform; read status before commanding motion</small></span>
  </a>
  <a class="ft-route-step" href="troubleshooting/">
    <span class="ft-route-number">05</span>
    <span class="ft-route-copy"><strong>Integrate the real mechanism</strong><small>Add load, multiple servos, limits and fault protection progressively</small></span>
  </a>
</div>

## Official resources

- [FEETECH website](https://www.feetechrc.com/)
- [FEETECH on GitHub](https://github.com/ftservo)
- [Legacy online documentation](http://doc.feetech.cn/#/f?q=2506a8cb7928)
- [Downloads](downloads.md)
