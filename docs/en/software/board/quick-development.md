# Quick Development Guide

## Chapter 1. Overview

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

Follow [Build Environment Setup](build-environment.md) to download the KM02G SDK, install the cross toolchain, and configure root login on the device.

---

## Chapter 3. Firmware Build

Run `make` from the SDK root to create `tools/ota/update.bin`. Use `ALLOW_LOCKED_ROOT=1 make` if you are using the SDK's default locked root configuration.

If you changed only the demo application, run `make app` to generate `apps/ai_glass_demo/ai_glass_demo`.

## Chapter 4. Firmware Flashing

See [Firmware Flashing](firmware-flashing.md) for USB-drive updates and factory reset.

---

## Chapter 5. Features

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
