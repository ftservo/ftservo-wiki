# Linux SDK

Official repository: [FTServo_Linux](https://github.com/ftservo/FTServo_Linux)

```bash
cd sdk/FTServo_Linux/src
cmake .
make

cd ../examples/SMS_STS/WritePos
cmake .
make
sudo ./WritePos /dev/ttyUSB0
```

This is the upstream STS/SMS example path, not a universal command. Choose the actual series. Configure udev/group permissions instead of running production software as root, and prefer out-of-source builds for integration.
