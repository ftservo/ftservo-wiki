# Linux

## Linux

官方仓库：[FTServo_Linux](https://github.com/ftservo/FTServo_Linux)

```bash
cd sdk/FTServo_Linux/src
cmake .
make

cd ../examples/SMS_STS/WritePos
cmake .
make
sudo ./WritePos /dev/ttyUSB0
```

上例只是官方 STS/SMS 示例入口。请按实际系列选择示例，并优先通过 udev/用户组配置串口权限，而不是让生产程序以 root 运行。集成项目时建议使用独立构建目录，避免源码树内构建产物进入版本库。
