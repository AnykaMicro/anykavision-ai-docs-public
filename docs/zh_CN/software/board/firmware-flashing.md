# 固件烧写

SDK 中执行 `make` 生成的 `tools/ota/update.bin` 是 OTA 升级包，包含 RAMFS 和 CONFIG 两个分区，通过产品板的 U 盘 OTA 目录升级。目前不提供预编译固件，编译方法见[编译环境配置](build-environment.md)。

## U 盘升级

````{only} anyka_review
```{admonition} TODO
:class: warning

以下步骤尚未在产品板上验证。SDK 中的应用不处理 U 盘升级（相关代码已注释），升级由出厂固件完成。待安凯确认出厂固件识别的文件名、是否需要先拔出 USB 线，以及串口提示文字。

These steps have not been verified on a board. The SDK app does not handle the USB-storage update (that code is commented out); the factory firmware does it. Anyka to confirm the file name the factory firmware looks for, whether the USB cable must be unplugged first, and the console messages.
```
````

````{only} not anyka_review
```{note}
以下 U 盘 OTA 升级步骤由出厂固件完成，尚未在实板环境下完成端到端验证。实际文件名、是否需先拔出 USB 线及串口提示文字请以实板出厂固件为准。
```
````

1. 产品板开机后，用 USB 2.0 数据线连接产品板的 Type-C 接口和电脑，产品板会在电脑上显示为 U 盘。
2. 把 `tools/ota/update.bin` 拷贝到 U 盘的 `OTA` 目录，等待自动升级。
3. 用串口工具查看升级过程：串口打印 `=== Starting OTA Upgrade ===` 表示升级开始；升级过程中产品板 LED 闪烁；串口打印 `Partial OTA Succeeded` 表示升级完成，随后设备自动重启。

```{warning}
`update.bin` 也包含配置分区。用 `ALLOW_LOCKED_ROOT=1 make` 生成的升级包会把已在使用的设备的 root 也锁定。
```

升级后，请在串口日志中确认配置分区（JFFS2，8 KiB 擦除块）挂载时没有错误。

## 恢复出厂设置

````{only} anyka_review
```{admonition} TODO
:class: warning

SDK 中由 APP 命令 0x8D 触发的恢复出厂设置会把存储（SD NAND）格式化为 FAT32，照片和视频会被清除。按键恢复出厂设置是否同样清除存储，待安凯确认。

The factory reset that APP command 0x8D triggers in the SDK formats the storage (SD NAND) as FAT32, erasing photos and videos. Anyka to confirm whether the button reset also erases the storage.
```
````

````{only} not anyka_review
```{warning}
执行恢复出厂设置可能会格式化设备存储（SD NAND）并清除已保存的照片和视频，操作前请先备份重要文件。
```
````

1. 开机状态下，断开设备的 USB 连接，连续快速按开机键 5 次。AK1090 系列芯片播报“开始恢复出厂设置”，串口打印“system recovery”，设备开始恢复出厂版本。
2. 恢复过程中串口会输出信息。恢复成功时，AK1090 系列芯片播报“恢复出厂设置成功”，串口打印“recovery finished”；恢复失败时，AK1090 系列芯片播报“恢复出厂设置失败”。
