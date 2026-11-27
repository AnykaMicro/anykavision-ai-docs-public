# Application Development Instructions

## Chapter 1. Overview

This document describes application development with the AI-glasses SDK and is intended to support development of glasses applications.

### 1.1 Product Version

The product version corresponding to this document is:

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

## Chapter 2. Overall Solution Design

### 2.1 System Block Diagram

![System block diagram](../../../zh_CN/software/board/img/system-block-diagram.png)

1. The AK1090-series chip controls KM02G-series power-on and power-off.
2. AK1090 and KM02G communicate over UART at 1,500,000 baud.
3. The Wi-Fi module is connected to KM02G.
4. The IMU, SD NAND, and CIS (sensor) are connected to KM02G.
5. The speaker and buttons are connected to AK1090.

> Labels embedded in the source figures on this page are in Chinese. The surrounding text explains the corresponding flow in English.

### 2.2 Software Architecture

The following figure shows the systems running on the KM02G cores:

![Systems running on the KM02G-series chip](../../../zh_CN/software/board/img/software-architecture.png)

The complete AI-glasses software solution uses a heterogeneous multicore architecture with three cooperating systems.

**AK1090-series Bluetooth chip**

- Runs AK1090-series firmware and handles Bluetooth communication.
- Communicates primarily with the phone app and KM02G.
- Provides basic functions such as audio playback.

**KM02G-series dual-core processor**

- **Core1 - Fastsys real-time subsystem**
  - Runs a lightweight real-time operating system.
  - Handles UART communication with AK1090.
  - Executes time-critical tasks such as rapid AE (automatic-exposure) convergence.
- **Core0 - Linux application system**
  - Runs a full Linux operating system.
  - Hosts the main AI-glasses application.
  - Processes complex algorithms and business logic.

**Inter-system communication**

- Bluetooth and KM02G exchange data over UART.
- The two KM02G cores exchange information using IPI (Inter-Processor Interrupt) communication.

This layered architecture decouples functions and balances real-time behavior with computing capacity.

**Note:** The SDK supports recording, photography, snapshot, and P2P modes, but only one mode may exist at a time. If no mode is sent after power-on, the default is USB mass-storage mode. Other commands may be combined and issued multiple times as appropriate for the selected mode.

---

### 2.3 Recording Flow

![Recording workflow](../../../zh_CN/software/board/img/chart-1.svg)

1. When AK1090 initiates a recording command through a button, it first powers on KM02G and sends a serial-port command. The KM02G RTT side acknowledges the message, starts the required operations, and forwards the recording command to Linux. Linux parses the command and starts the recording thread.
2. A stop-recording command follows the same command path. After receiving it, Linux saves the recording file and sends a completion command over IPI.
3. See `apps/ai_glass_demo/libVideoRecordCode` for the implementation.
4. The complete command interaction for recording is shown below.\
   ![Recording-command interaction flow](../../../zh_CN/software/board/img/chart-2.svg)

---

### 2.4 Photo Flow

![Photo workflow](../../../zh_CN/software/board/img/chart-3.svg)

Command interaction:

![Photo-command interaction flow](../../../zh_CN/software/board/img/chart-4.svg)

---

### 2.5 Snapshot Flow

![Snapshot workflow](../../../zh_CN/software/board/img/chart-5.svg)

**Note:** The snapshot flow is implemented on RTT; Linux does not participate.

---

### 2.6 P2P Flow

![P2P workflow](../../../zh_CN/software/board/img/chart-6.svg)

The P2P flow serves three functions:

1. P2P network provisioning
2. P2P image transfer
3. P2P live streaming

For the implementation, see `handle_wifi_p2p_mode` in `ai_glass_cmd_handle.c` in the `ai_glass_demo` application.

---

## Chapter 3. Linux Application

### 3.1 Directory and File Structure

Code location: `ai_glass_demo`

```
├── common
│   ├── config
│   │   ├── app_main_config.ini
│   │   ├── camera_gc13b0.ini
│   │   └── eis_gc13b0.ini
│   ├── inc
│   │   ├── ai_glass_cmd_handle.h
│   │   ├── ai_glass_cmd_ipi.h
│   │   ├── ai_glass_cmd_queue.h
│   │   ├── ai_glass_common.h
│   │   ├── ai_glass_isp_quick.h
│   │   ├── ai_glass_log.h
│   │   ├── ai_glass_time.h
│   │   ├── ak_list.h
│   │   ├── ftp_monitor.h
│   │   ├── fun_log.h
│   │   ├── fw_media_types.h
│   │   ├── ini_parser.h
│   │   ├── media_configs.h
│   │   ├── ring_buffer.h
│   │   ├── sdnand_manager.h
│   │   └── wifi_manager.h
│   └── src
│       ├── ai_glass_cmd_handle.c
│       ├── ai_glass_cmd_ipi.c
│       ├── ai_glass_cmd_queue.c
│       ├── ai_glass_common.c
│       ├── ai_glass_isp_quick.c
│       ├── ai_glass_log.c
│       ├── ai_glass_time.c
│       ├── ftp_monitor.c
│       ├── fun_log.c
│       ├── ini_parser.c
│       ├── media_configs.c
│       ├── ring_buffer.c
│       ├── sdnand_manager.c
│       └── wifi_manager.c
├── common.mk
├── libAudioRecordCode
│   ├── ak_sound_demo.c
│   └── ak_sound_demo.h
├── libLiveStreamCode
│   ├── ak_circular_buffer.h
│   ├── ak_rtsp_demo.c
│   ├── ak_rtsp_demo.h
│   ├── ak_rtsp_server_demo.c
│   └── ak_rtsp_server.h
├── libTakePhotoCode
│   ├── ak_dma_api.c
│   ├── ak_dma_api.h
│   ├── ak_snap_demo.c
│   ├── ak_snap_demo.h
│   ├── usb_webcam.c
│   ├── usb_webcam.h
│   ├── video.c
│   └── video.h
├── libVideoEis
│   ├── ak_sc7i22_cmd.h
│   ├── antiShake.c
│   ├── antiShake.h
│   ├── print_color_simple.h
│   ├── video_eis.c
│   └── video_eis.h
├── libVideoRecordCode
│   ├── ak_gyro_app.c
│   ├── ak_gyro_app.h
│   ├── ak_mux_sample.c
│   ├── ak_mux_sample.h
│   ├── ak_record_demo.c
│   └── ak_record_demo.h
├── main.c
└── Makefile
```

---

### 3.2 Source Files

1. `main.c` is the main entry point and message-processing center.
2. Directories whose names begin with `lib` provide module functions:
   - `libAudioRecordCode`: Audio recording
   - `libLiveStreamCode`: Live-streaming service
   - `libTakePhotoCode`: Photography
   - `libVideoEis`: Electronic image stabilization
   - `libVideoRecordCode`: Video recording
3. `common` contains feature-related files. `config` holds readable and writable common configuration installed at `/etc/config/` on the board; `inc` contains headers and `src` contains C source files.
   - `ai_glass_cmd_handle.c`: Primarily handles Linux-side command responses.
   - `ai_glass_cmd_ipi.c`: IPI inter-core communication.
   - `ai_glass_cmd_queue.c`: Message queues.
   - `ai_glass_common.c`: Common functions.
   - `ai_glass_isp_quick.c`: IPI video functions.
   - `ai_glass_log.c`: Logging.
   - `ai_glass_time.c`: Time functions.
   - `ftp_monitor.c`: FTP monitoring.
   - `fun_log.c`: Log functions.
   - `ini_parser.c`: INI parsing.
   - `media_configs.c`: Media configuration, including INI reading/writing.
   - `sdnand_manager.c`: SD NAND management.
   - `wifi_manager.c`: Wi-Fi functions.

---

### 3.3 IPI Inter-Core Communication Interfaces

`apps/ai_glass_demo/common/inc/ai_glass_cmd_ipi.h` defines application interfaces for RTT-Linux inter-core communication:

1. `int ai_glass_ipi_cmd_get` retrieves a message sent from RTT to Linux so the Linux application can perform a snapshot, recording, live-streaming, or other task.
2. `void ai_glass_ipi_cmd_completed` reports completion of a message obtained with `ai_glass_ipi_cmd_get`. It must be called after processing; otherwise, the next message cannot be obtained successfully.
3. `set_glass_info_v4` replies to a message sent from RTT to Linux.
4. `set_glass_info_v4_notify` proactively sends a notification to RTT.

---

### 3.4 Configuration Files

Configuration files are in `apps/ai_glass_demo/common/config` in the application source and are installed under `/etc/config/` on the device at runtime.

**1. Main application configuration: `app_main_config.ini`**

During compilation, `build_apps.sh` copies `apps/ai_glass_demo/common/config/app_main_config.ini` to `rootfs/config/`. At runtime it is `/etc/config/app_main_config.ini`. Modify this INI file to inspect module logs. Logs not printed to the console are stored in `/mnt/Log` on Linux.

```ini
[Common]
dmesg=0                   ; 0:disable 1:enable     kernel log
middle_log=0              ; 0:default 1:warn 2:warn 3:notice 4 and above:error   middleware log level
rtt_log=0                 ; 0:disable 1:enable     RTT system log
app_log=0                 ; 0:error 1:warn 2:info 3:debug   Linux application-demo log
app_log_save=0            ; 0:console 1:save file  output for middleware and Linux demo logs; 0 prints to console, 1 saves to file
power_off_time=0          ; poweroff_time for debug, in seconds

[DebugAp]
; Debug Wi-Fi access point. password is a WPA2 password (8-63 characters); with an empty password, image-debug and USB-photo modes do not start the AP
; Do not append comments to values: everything after = is part of the value
ssid=AI_GLASS_DEBUG
password=
```

Do not edit the Git-tracked `app_main_config.ini` directly. Copy it to `rootfs/config.local/` and edit the copy. During the build, files in that directory replace same-named files in `rootfs/config/` in the configuration image; see [Build Environment Configuration](build-environment.md).

Use a unique SSID and strong WPA2 password for each device or debugging session. Do not reuse production or corporate Wi-Fi credentials. After debugging, restore `image_debug_mode` to `0` and clear the debug-AP configuration from `rootfs/config.local/`.

**Note:** With this configuration, RTT and Linux kernel logs are written to `/mnt/Log`. They can also be displayed on the console: run `dmesg` for the Linux kernel log and `cat /dev/fastsys-log` for the RTT log.

---

**2. Camera configuration**

Files named `camera_xxx.ini` in `apps/ai_glass_demo/common/config/` configure the camera for different CIS types. The SDK build script `build_apps.sh` copies `camera_gc13b0.ini` as `camera.ini`. On the device it is `/etc/config/camera.ini`.

### [Camera]

```ini
; ISP parameters for photography
snap_isp_config=/fast/isp_gc13b0_mipi_2lane_av200.conf
; ISP parameters for recording (do not append comments to path values)
video_isp_config=/fast/isp_gc13b0_mipi_2lane_av200_30fps.conf
```

### [Record]

```ini
main_chn_width=2080         ; remote stabilization (default) resolution is 2080*1536
main_chn_height=1536        ; local stabilization requires cropping; change to 1600*1200
main_vi_width=2080
main_vi_height=1536
main_chn_fps=30
main_chn_target_kbps=20480  ; 20*1024
main_chn_max_kbps=20480
main_chn_gop_len=90
main_chn_enc_type=0         ; 0:h264 1:mjpeg 2:h265
main_chn_br_mode=5          ; 0:cbr 1:vbr 2:capped_vbr 5:avbr
eis_enable=0                ; 0 is remote stabilization (default): the device does not stabilize; the phone app does. This release lacks that app, so default recordings are unstabilized. 1 enables local stabilization; also change main_chn_width and main_chn_height accordingly
image_debug_mode=0          ; 0 disables image debugging. 1 enables it: if [DebugAp] password in app_main_config.ini is an 8-63 character WPA2 password, the device starts Wi-Fi in AP mode and an RTSP service for a phone/computer RTSP client. Without a password, neither AP nor RTSP starts
```

### [Rtsp]

```ini
main_chn_width=2080         ; local stabilization requires cropping: configure 1600*1200
main_chn_height=1536        ; with stabilization disabled, configure 2080*1536
main_vi_width=2080
main_vi_height=1536
main_chn_fps=30
main_chn_target_kbps=2048   ; 2*1024
main_chn_max_kbps=3072      ; 3*1024
main_chn_gop_len=60         ; 2*30
main_chn_enc_type=0         ; 0:h264 1:mjpeg 2:h265
main_chn_br_mode=5          ; 0:cbr 1:vbr 2:capped_vbr 5:avbr
eis_enable = 0              ; 0 disables stabilization; 1 enables local stabilization, and main_chn_width/main_chn_height must be changed accordingly
```

### [Photo]

```ini
main_chn_fps=10
main_org_width=3840         ; input width
main_org_height=2880        ; input height
main_res_width=4032         ; output width
main_res_height=3024        ; output height
main_jpg_slice_num=3        ; number of slice-encoding passes
main_org_slice_one_height=960   ; 2880/3 pixels per slice
main_jpg_slice_one_height=1008  ; 3024/3 pixels encoded per pass
```

---

**3. Gyroscope zero-offset calibration**

After flashing device firmware, calibrate the gyroscope's zero offset before first use to ensure that stabilization works correctly:

1. Place the glasses level and start recording. The application saves the gyroscope zero-offset calibration value to `/etc/config/eis_offset.cfg`; calibration is then complete.
2. If the glasses were not level, delete `/etc/config/eis_offset.cfg`, place them level, and repeat step 1.

This vendor calibration procedure has not been verified on physical hardware in this release.

---

## Chapter 4. Common Debugging Methods

### 4.1 RTSP On-Demand Stream

Stream URL: `rtsp://xx.xx.xx.xx/vs0`

```{warning}
Use this `rtsp://` debug stream only through a temporary, isolated DebugAp. Do not bridge, route, or port-forward the access point to an office network, production network, or the Internet. After debugging, disable `image_debug_mode` and clear the debug-AP configuration.
```

---

### 4.2 LED Debugging

```bash
# Steady on
echo 1 > /sys/devices/platform/leds/leds/state_led/brightness

# Off
echo 0 > /sys/devices/platform/leds/leds/state_led/brightness

# Flash: on for 100 ms, off for 200 ms
echo "on 100 200" > /sys/devices/platform/leds/leds/state_led/flash
```

### 4.3 General GPIO Configuration

```bash
# Export GPIO
echo xx > /sys/class/gpio/export

# Set output mode
echo out > /sys/class/gpio/gpioxx/direction

# Drive low
echo 0 > /sys/class/gpio/gpioxx/value

# Drive high
echo 1 > /sys/class/gpio/gpioxx/value
```

---

### 4.4 View Partitions

```bash
cat /proc/mtd
```

---

### 4.5 Local Device Stabilization or Remote Phone-App Stabilization

Set `eis_enable` under `[Record]` in `/etc/config/camera.ini` to select local device stabilization or remote phone-app stabilization.\
The default is remote app stabilization: `eis_enable=0`, and `main_chn_width`/`main_chn_height` match `main_vi_width`/`main_vi_height` at 2080×1536. The device saves an unstabilized original recording whose name includes `_origin`; Anyka_Glasses would stabilize it. That app was not included in this release, so the default configuration currently produces no stabilized recording. For local stabilization, set `eis_enable` to `1` and change `main_chn_width` and `main_chn_height` to 1600×1200.

---

### 4.6 Enable H.264/H.265 Recording

Change `main_chn_enc_type` under `[Record]` in `/etc/config/camera.ini`. MJPEG recording is currently unavailable.

---

### 4.7 Quickly Inspect Command Transmission and Reception

RTT mainly forwards commands; it handles only a few special commands such as snapshots. Log lines usually contain a prefix showing the direction:

- `[ipi->linux]`: RTT sends a command to Linux over IPI.
- `[linux->ipi]`: Linux sends a command to RTT over IPI.
- `[rtt->bt]`: RTT sends a command to Bluetooth.
