# Firmware Flashing

`tools/ota/update.bin`, which `make` builds in the SDK, is an OTA package holding the RAMFS and CONFIG partitions. You install it through the OTA folder on the reference board's USB storage. There is no prebuilt firmware; see [Build Environment Setup](build-environment.md) for how to build it.

## Update over USB storage

````{only} anyka_review
```{admonition} TODO
:class: warning

These steps have not been verified on a board. The SDK app does not handle the USB-storage update (that code is commented out); the factory firmware does it. Anyka to confirm the file name the factory firmware looks for, whether the USB cable must be unplugged first, and the console messages.
```
````

````{only} not anyka_review
```{note}
USB-storage OTA updates are handled by the factory firmware and have not yet been verified end-to-end on hardware. Confirm the expected file name, whether the USB cable must be unplugged first, and the console output against your board's factory firmware.
```
````

1. With the board powered on, connect its Type-C port to your PC with a USB 2.0 cable. The board appears on the PC as a USB drive.
2. Copy `tools/ota/update.bin` into the drive's `OTA` folder and wait for the update to start.
3. Watch the update on the serial console: `=== Starting OTA Upgrade ===` means the update has started; the board LED blinks while it runs; `Partial OTA Succeeded` means it is complete, and the device then reboots.

```{warning}
`update.bin` also carries the config partition. An update built with `ALLOW_LOCKED_ROOT=1 make` locks root on devices already in use.
```

After the update, check in the serial log that the config partition (JFFS2, 8 KiB erase blocks) mounts without errors.

## Factory reset

````{only} anyka_review
```{admonition} TODO
:class: warning

The factory reset that APP command 0x8D triggers in the SDK formats the storage (SD NAND) as FAT32, erasing photos and videos. Anyka to confirm whether the button reset also erases the storage.
```
````

````{only} not anyka_review
```{warning}
Factory reset may format the onboard storage (SD NAND) and erase saved photos and videos. Back up important files before proceeding.
```
````

1. With the device powered on and its USB cable unplugged, press the power key 5 times quickly. The AK1090 series chip announces "开始恢复出厂设置" (starting factory reset), the serial console prints "system recovery", and the device starts restoring the factory version.
2. The serial console prints progress during the reset. On success, the AK1090 series chip announces "恢复出厂设置成功" (factory reset succeeded) and the serial console prints "recovery finished"; on failure, it announces "恢复出厂设置失败" (factory reset failed).
