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

Select `scscl`, `sms_sts` or `hls` for the actual series. Edit the port, baud rate and ID, then begin with Ping:

```bash
cd sms_sts
python ping.py
```

Windows ports look like `COM3`; Linux commonly uses `/dev/ttyUSB0` or `/dev/ttyACM0`; macOS commonly uses `/dev/cu.usbserial-*`. Configure normal serial-device permissions on Linux rather than running production control as root.

Keep port, baud rate, IDs and soft limits in configuration. Close the port and stop safely on exceptions. Unit-test conversions and range checks without hardware; validate communication and motion on the exact servo.

