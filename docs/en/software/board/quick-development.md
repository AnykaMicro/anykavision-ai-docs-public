# Quick Development Guide

## Chapter 1. Overview

<<<<<<< prepare/developer-kit-1.0.0
This document introduces the AI-glasses SDK reference design and helps you quickly build, flash, and run the glasses application during development.

### 1.1 Product Version

| Chip | Operating system |
| ---- | ---------------- |
| KM02G series | Linux + RTT |

### 1.2 Hardware Version

| Hardware | Chips | Description |
| -------- | ----- | ----------- |
| Product board | KM02G series + AK1090 series | |

### 1.3 Abbreviations

- **APP**: The Anyka_Glasses phone application
- **BT**: Bluetooth module (AK1090 series)
- **RTT**: RT-Thread system running on the KM02G-series chip
- **LINUX**: Linux system running on the KM02G-series chip

---

## Chapter 2. Environment Setup

See [Build Environment Configuration](build-environment.md).

---

## Chapter 3. Firmware Build

### 3.1 Obtain the SDK and Prepare the Build

Follow [SDK Download](sdk-download.md) and [Build Environment Configuration](build-environment.md) to complete these preparations. The exact commands are in the SDK README:

1. Download and verify the released SDK source archive and the BusyBox and mtd-utils source archives from Release 1.0.0. Extract the SDK to a path containing no spaces.
2. Put the verified BusyBox and mtd-utils source archives in the SDK's `tools/` directory.
3. Until the toolchain public-redistribution gate passes, obtain a checksum-matched toolchain archive from Anyka and place it in `tools/`. Run `./scripts/get_toolchain.sh`, then add `/opt/riscv64-anyka-linux-musl/bin` to `PATH`.
4. The sanitized public source archive removes the old `rootfs/skeleton/etc/format_tool`, whose provenance and licensing were unresolved. Before generating a complete ramdisk or firmware image, separately obtain the approved V1.00 formatter from Anyka under suitable license terms. It must satisfy the executable-permission and SHA-256 requirements in [SDK Download](sdk-download.md). Pass it as `FORMAT_TOOL_BIN=/absolute/path/to/licensed/format_tool`; the fallback path is `rootfs/vendor/format_tool`. Do not run a full `make` or `make install` without it.
5. Only when generating a complete image, copy `rootfs/config/shadow` to `rootfs/config.local/` and set the password hash on the copy's `root` line using `openssl passwd -6`. Do not edit the Git-tracked `rootfs/config/shadow`. Use a unique strong password for each device or build; never ship a shared development password or commit or share password hashes.

### 3.2 Build the Application

The public source archive can run host-side tests and build the application:

```bash
make clean        # Clean
make test         # Run host-side tests
make app          # Build the app
```

Run `FORMAT_TOOL_BIN=/absolute/path/to/licensed/format_tool make` or the corresponding `make install` only after the separately supplied licensed vendor formatter and all complete-image inputs are ready. The SDK copies the selected tool into the image at `/etc/format_tool`. The resulting `update.bin`, `ramfs.img`, and `usr.jffs2` are under `tools/ota` and require the prescribed development-board validation.

## Chapter 4. Firmware Flashing

After a complete image has been built and validated, follow [Firmware Flashing](firmware-flashing.md) for USB-drive upgrade and factory-reset procedures. Physical-board, firmware, flashing, OTA, Wi-Fi, and USB behavior has not been verified for this documentation release.

---

## Chapter 5. Features
=======
1. Follow [Build Environment Setup](build-environment.md) to download the KM02G SDK, install the compiler and build `tools/ota/update.bin`.
2. **Flash the board**: see [Firmware Flashing](firmware-flashing.md).
>>>>>>> main

```{note}
The phone-app operations below (recording-duration settings, AI image recognition, gallery import, and live-video preview) require the Anyka_Glasses app. That app was not included in this release; developers may provide its installation package in a later version.
```

The following procedures are translated vendor instructions and are not physical-hardware test claims.

### 5.1 Take a Photo

**Operation:** Briefly press the function button once.\
**Prompts:** A "beep" plays when capture starts, and a shutter-click sound plays when it finishes.\
**Afterward:** The KM02G-series chip powers off after capture.

### 5.2 Record Video

**Operation:** Hold the function button for three seconds to start recording; briefly press it once to stop.\
**Prompts:** One chime plays when recording starts; two chimes play when it finishes.\
**Default duration:** One minute. To change it, tap the app version five times quickly and enter 1-600 seconds under timed-recording duration. The device accepts any positive duration; a value less than or equal to zero records for 600 seconds.\
**Afterward:** The KM02G-series chip powers off after recording.

### 5.3 AI Image Recognition

**Prerequisite:** Bind the phone to the glasses.\
**Operation:** Open the phone app, enter the AI image-recognition screen, and briefly press the function button twice. The image appears in the app; recognized text is displayed there and can also be played through the glasses speaker.\
**Afterward:** The KM02G-series chip powers off after recognition.

### 5.4 Power On and Off

Hold the power button for three seconds to power off; briefly press it once to power on. The literal Chinese device prompts are `关机` ("powering off") and `开机` ("powering on").

### 5.5 View Videos and Photos Captured by the Glasses

**Method 1:** Connect the glasses to a computer with a USB cable. They appear as a USB drive. Videos are under `USB-drive root/Videos/`; photos are under `USB-drive root/Pictures/`.

**Method 2:** Open the phone app, bind the glasses, and enter Gallery to import videos and photos to the phone.

### 5.6 Live Video Preview

Open the phone app, bind the glasses, and enter Live Video to view the device's real-time video.
