# Python SDK

Official repository: [ftservo/FTServo_Python](https://github.com/ftservo/FTServo_Python)

=== "Complete Wiki checkout"

    ```bash
    git clone --recurse-submodules https://github.com/ftservo/ftservo-wiki.git
    cd ftservo-wiki/sdk/FTServo_Python
    python -m venv .venv
    # Linux/macOS: source .venv/bin/activate
    # Windows: .venv\Scripts\activate
    python -m pip install pyserial
    ```

=== "PyPI"

    ```bash
    python -m pip install ftservo-python-sdk
    ```

## Run an official example

Run these commands from the **`FTServo_Python` source root**. Installing only the PyPI package does not create this source example directory; use the complete checkout above to obtain it.

Choose the [matching application layer](index.md#application-layer), edit that directory's `ping.py`, and set the confirmed port, baud rate and target ID. Values shipped in an example are example settings, not universal factory defaults.

=== "SCS / SCSCL"

    ```bash
    cd scscl
    python ping.py
    ```

=== "STS / SMS"

    ```bash
    cd sms_sts
    python ping.py
    ```

=== "HLS"

    ```bash
    cd hls
    python ping.py
    ```

Return to the source root before switching series. PWM does not use these bus examples. Obtain missing documentation before selecting an unconfirmed application layer.

Windows ports look like `COM3`; Linux commonly uses `/dev/ttyUSB0` or `/dev/ttyACM0`; macOS commonly uses `/dev/cu.usbserial-*`. Configure normal serial-device permissions on Linux rather than running production control as root.

## Check the result

- Opening the port or setting its baud rate only confirms host configuration; it does not establish that the servo responded.
- Ping must return a successful response from the target ID. Check communication results and device errors, and retain the console output.
- Match the response to the physical device and configuration before reading status through the correct memory table. Ping does not validate mechanical assembly or motion settings.

For no response, follow [communication troubleshooting](../troubleshooting.md#not-found). Proceed to [First Motion](../getting-started/first-motion.md) only after stable reads, power and wiring checks, and mechanical clearance checks.

## Development practices

Keep port, baud rate, IDs and soft limits in configuration. Close the port and stop safely on exceptions. Unit-test conversions and range checks without hardware; validate communication and motion on the exact servo.
