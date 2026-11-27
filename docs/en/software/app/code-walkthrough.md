# Code Walkthrough

```{note}
The companion Anyka_Glasses app was not included in this release: neither an installation package nor source code was provided. Developers may supply them in a later version. This page is currently for reference only.
```

## 1. Project Overview

This is a multi-platform **Flutter + GetX** application designed to work with smart glasses and camera devices. Its main capabilities are:

1. Device binding and Bluetooth connection management (dual BLE/SPP modes)
2. Live video preview (RTSP), media import and management, and video stabilization
3. AI conversation (voice Q&A and AI image understanding through Alibaba Cloud Model Studio)
4. Call recording and translation, EQ debugging, and OTA firmware upgrades

**Technology stack:**

- Flutter + GetX (state management, routing, and dependency injection)
- easy_localization (Chinese/English internationalization)
- flutter_bluetooth_serial (classic SPP Bluetooth) / flutter_blue_plus (Bluetooth Low Energy)
- fijkplayer (local plugin for RTSP video playback)
- Native Android Kotlin: P2P/FTP data channels, Alibaba Cloud Model Studio LLM, and OPUS audio coding/decoding

Business code is concentrated in `lib/app/` and `android/app/src/main/kotlin/`.

---

## 2. Architecture Layers

```
Flutter UI layer (Pages + Views)
    ↓
Controller layer (GetX Controller, business logic)
    ↓
ServiceFactory (singleton service facade, hides implementation differences)
    ↓
AnykaService abstract interface
    ├── FlutterService (Flutter-side Bluetooth + protocol implementation)
    └── NativeService (calls native Android through MethodChannel; not currently used)
    ↓
Native Android layer (Bluetooth, P2P/FTP, LLM, and audio coding/decoding)
```

- A **Controller** interacts only with `ServiceFactory.getInstance()` and does not depend directly on a Bluetooth library or MethodChannel.
- **ServiceFactory** chooses the Flutter or native implementation at runtime according to `AppConstants.useNativeBlueTooth`, and supports hot switching.
- **AppConstants** (`lib/app/common/data/app_constants.dart`) centrally manages global configuration switches such as the Bluetooth type, heartbeat interval, AI-conversation timeout, and stabilization zoom ratio, making debugging and feature trimming easier.

---

## 3. `lib/app` Directory Structure

### 1. `bindings/`

GetX dependency-injection configuration. Controllers and services are injected on demand during routing.

- `initial_binding.dart`: Global initialization binding at application startup.
- `repository_bindings.dart`: Data-layer bindings.

When adding a module, normally create its Binding class here and register it in `routes/app_pages.dart`.

---

### 2. `bluetooth/`

The core Bluetooth abstraction layer, which hides low-level BLE and SPP differences.

| File | Description |
| ---- | ----------- |
| `base_bluetooth.dart` | Abstract Bluetooth base class defining common interfaces for scanning, connecting, and sending/receiving data |
| `ble_bluetooth.dart` | BLE implementation using flutter_blue_plus |
| `spp_bluetooth.dart` | Classic Bluetooth SPP implementation using flutter_bluetooth_serial |
| `bluetooth_manager.dart` | Singleton manager that holds the active Bluetooth instance and exposes a common operation interface |
| `blue_protocol_helper.dart` | Device communication-protocol wrapper that assembles/disassembles every Bluetooth command, including AI conversation, EQ, OTA, P2P provisioning, and heartbeat commands |

**Switching Bluetooth type:** Set `AppConstants.bluetoothConnectType` to `BluetoothType.spp` or `BluetoothType.ble` at runtime; business code does not need to change.

---

### 3. `common/`

Shared project infrastructure and UI components.

- **`data/app_constants.dart`**: Global constants and runtime configuration switches (see Section 2).
- **`views/`**:
  - `any_page_title.dart`: Common page title bar with a back button and a slot for right-side actions.
  - `anyka_toast_view.dart`: Custom Toast appearance.
  - `log_text_view.dart`: Debug-log display component.
  - `photo_detail_page.dart`: Full-screen image preview with left/right paging.
- **`observer/`**: GetX reactive-observer helper classes.

---

### 4. `routes/`

Centralized GetX routing.

- `app_routes.dart`: Route constant strings for every page, such as `AppRoutes.home` and `AppRoutes.eq`.
- `app_pages.dart`: A `GetPage` list that binds each route string to a page Widget and Binding.

To add a page: (1) add a constant to `app_routes.dart`; (2) add a `GetPage` to `app_pages.dart`; and (3) create a Binding class.

---

### 5. `services/`

The business-service layer and bridge between Flutter and the native layer.

| File | Description |
| ---- | ----------- |
| `anyka_service.dart` | Abstract base interface defining all Bluetooth operations and device-control interfaces, as well as data models such as `BluetoothDeviceInfo`, `BluetoothConnectionStatus`, and `ChatStatus` |
| `flutter_service.dart` | Flutter implementation of `AnykaService`; handles Bluetooth protocol parsing, heartbeats, creation/closure of call-recording files, buffered Opus audio sending, and the P2P provisioning state machine |
| `native_service.dart` | Native implementation of `AnykaService`; forwards operations through MethodChannel for native Android processing; not currently used |
| `service_factory.dart` | Factory singleton that creates and holds a `FlutterService` or `NativeService` according to configuration and supports hot switching at runtime |

**Key responsibilities of `flutter_service.dart`:**

- Bluetooth packet parsing (`_handleBluetoothProtocolFromDevice`) for all device commands, including AI conversation, EQ, OTA, call recording, P2P, and heartbeat commands.
- Call-recording file management: creates OPUS, WAV, and LOG files and calls native Android methods for OPUS-to-PCM decoding and WAV-header writing.
- Buffered Opus-data transmission.
- P2P provisioning state machine: KM02G power-on → P2P provisioning → P2P connection → KM02G power-off after success or failure. A `Completer` and timeout `Timer` manage the full flow.

---

### 6. `utils/`

Utilities and infrastructure to reuse when developing features.

| File | Description |
| ---- | ----------- |
| `dialog_util.dart` | Common Dialog, ProgressDialog, and Toast wrapper using Get.dialog + FToast; supports iOS and Material styles |
| `audio_util.dart` | PCM/WAV file creation and writing |
| `audio_play_util.dart` | Audio playback wrapper around just_audio |
| `audio_record_util.dart` | Phone-microphone recording wrapper around the record plugin |
| `opus_util.dart` | Flutter-side OPUS coding/decoding |
| `method_channel_util.dart` | Singleton Flutter-to-native MethodChannel wrapper supporting multiple registered message receivers |
| `data_store_util.dart` | SharedPreferences wrapper for local persistent data |
| `permission_util.dart` | Location, Bluetooth, storage, and other permission requests |
| `aes_decryptor.dart` | AES decryption, including License-verification use cases |
| `network_util.dart` | Network-status detection and Wi-Fi information retrieval |
| `flavors.dart` | Multi-flavor build configuration for differences between anyBlue and glasses channels |
| `log/logger_util.dart` | Global logging utility for centralized debug output |

---

## 4. `lib/app/modules` Feature Modules

Every module follows the standard GetX structure: `pages/` (UI) + `controllers/` (business logic) + `bindings/` (dependency injection).

---

### 1. `home/`

The application home page and navigation entry point for all other feature modules.

- Displays device connection state, battery level, and firmware version.
- Provides entry cards for AI conversation, gallery management, live video, settings, and other features.
- Loads the last bound device automatically and attempts to restore its connection state.

---

### 2. `aiChat/`

AI-conversation module. Android invokes the large model; Flutter presents the results.

**Features:**

- **Voice Q&A**: Obtains an Opus audio stream from the device's AK1090-series chip or the phone microphone, sends it to Alibaba Cloud Model Studio, and plays the TTS reply for the user through the AK1090-series chip.
- **AI image understanding**: Uses an AK1090-series command to trigger device capture. The AK1090-series chip transfers image data to the app, which calls the model for image understanding and returns text.
- **Chat UI**: IM-style window that distinguishes user and AI roles and displays the text Q&A history.

**Controller responsibilities:**

- Conversation state: `idle → userAsking → recognizing → aiReplying → idle`, with automatic reset on timeout.
- Handles the callback indicating that AI-reply playback has completed.

---

### 3. `blueToothConnect/`

Device binding and Bluetooth connection, required before using any Bluetooth-dependent feature.

**Flow:**

1. Check and request location permission (required for Android Bluetooth scanning) and Bluetooth permission.
2. Call `ServiceFactory.getInstance().startScan()` and display discovered devices in real time, including RSSI and pairing state.
3. Filter by a device-name prefix. The default is `"AK"`; it can be changed in settings.
4. When the user selects a device, perform the handshake (`handShake`), connect, and save the binding information to SharedPreferences.

---

### 4. `bluetoothOta/`

AK1090-series OTA firmware upgrade for the AK1090-series controller.

- Sends the firmware file to the device in packets through Bluetooth.
- Supports single-ear and dual-ear modes (`isTwoEarBudOta`).
- Displays upgrade progress, retries failures, and automatically disconnects and prompts for a restart after the upgrade.
- Usually opened from the settings or upgrade module.

---

### 5. `media_import/`

Imports photos and videos from the device to the phone gallery over Wi-Fi P2P + FTP.

**Full flow:**

1. Flutter sends a P2P provisioning command, triggering KM02G power-on → P2P provisioning → P2P connection.
2. After P2P connects, FTPUtil scans the device's image and video directories over FTP.
3. Files are downloaded in batches by type, with progress updated through `DialogUtil.showProgressDialog`.
4. The UI is updated after download.
5. At the end, KM02G powers off and P2P disconnects.

---

### 6. `rtsp/`

Live-video preview module.

- After the P2P connection is established, the device pushes an RTSP video stream and the app plays it with the local `fijkplayer` plugin.
- Supports portrait/landscape switching and full-screen mode.
- The live-stream timeout can be configured in the settings debug menu (`AppConstants.rtspLiveTimeout`).

> **Security:** Use FTP and `rtsp://` only on a temporary, isolated, direct device-to-phone P2P network. Do not bridge or route the connection to an office network, production network, or the Internet. Disconnect P2P immediately after media transfer or live preview.

---

### 7. `eq/`

EQ debugging module for device-side audio-processing parameters.

**Data structure:**

- `EQType`, such as A2DP or HFP uplink/downlink, contains multiple `EQGroup` values. Each group contains multiple `EQParam` frequency-band parameters: type, frequency, gain, and Q value.

**Core functions:**

- Read the current EQ configuration from the device with `getEqGroupInfoFromDevice` (3-second timeout).
- After parameters are edited in the UI, send every EQ type to the device at once with `setAllEqTypeToDevice` (5-second timeout and 2-second cooldown between settings).
- A2DP supports up to eight configuration groups; other types support at most one.
- Add, rename, and delete EQ groups.

---

### 8. `callManagement/`

Call-recording management module.

- Listens for a device call-recording request (`cmdDeviceEnterCallMode`) or starts recording from the app.
- Recording data is transmitted over Bluetooth as OPUS. The app writes both `.opus` and `.wav` files in parallel; native Android decodes OPUS to PCM and writes the WAV data.
- Writes a `.log` file containing each packet's sequence number and continuity for packet-loss debugging.
- Browses and plays call-recording files.
- Works with `callTranslate` to translate recordings.

---

### 9. `callTranslate/`

Call-translation module.

- Receives call audio-stream data (`cmdCallTranslateData`) for both near-end and far-end channels.
- Implements delayed audio-data loopback (`callTranslateDataSendBackDelayTime`, 2 seconds by default) to simulate a real call-translation scenario.
- Displays source and translated text by caller/callee role.

---

### 10. `settings/`

Settings module with system-level feature entry points.

- Displays the AK1090-series firmware version and app version.
- Unbinds the device by clearing local binding information and restoring factory settings.
- Provides an OTA-upgrade entry point.
- Provides a help page.
- **Hidden debug menu**: Tap the version number five times within three seconds to unlock:
  - Enable or disable phone-side AI conversation
  - P2P connection logging
  - RTSP live-stream timeout
  - UVC mode configuration
  - Bluetooth scan-filter keyword
  - Call-translation data-loopback delay

---

### 11. `upgrade/`

Camera (KM02G-series) firmware-upgrade module, distinct from `bluetoothOta`, which upgrades AK1090-series firmware.

- Pushes a camera-firmware file to a specified device directory over P2P/FTP.
- Sends the OTA-upgrade command and listens for progress callbacks.
- An AK1090-series command reports upgrade success or failure so the Flutter UI can update.

---

## 5. `android/` Directory Structure (Native Android)

### 1. `app/src/main/kotlin/com/anyka/ai/`

| File/directory | Description |
| -------------- | ----------- |
| `AiApplication.kt` | Initializes the Application and registers global libraries such as BlankJ Utils |
| `ForegroundService.kt` | Foreground service that keeps the app alive and monitors Bluetooth connection state |
| `ServiceManager.kt` | Native service manager coordinating child-module initialization and destruction |
| `activity/` | MainActivity, which registers all MethodChannel handlers |
| `bluetooth/` | Native Android SPP/BLE implementation; not currently used |
| **`llm/`** | Alibaba Cloud Model Studio integration |
| **`p2p/connection/`** | P2P + FTP data-channel implementation |
| `utils/` | Native utilities |

**`llm/` directory (AI-conversation core):**

- `BaiLianLLM.kt`: Alibaba Cloud Model Studio SDK wrapper that manages License authorization and SDK initialization.
- `BaiLianLLMHelper.kt`: AI-conversation controller implementing the full voice ASR, LLM Q&A, and TTS-synthesis flow and managing long-lived WebSocket connections and conversation state.
- `UploadPhotoUtil.kt`: Uploads image data received from the device to the Model Studio server for image understanding.

**`p2p/connection/` directory (media-import core):**

- `P2PConnection.kt`: Manages Wi-Fi P2P device discovery, connection, and timeout retries, and reports connection results and progress to Flutter through MethodChannel.
- `FTPUtil.kt`: Wraps FTP transfer, batch-downloads images/videos, and updates progress in real time.
- `FTPClientHelper.kt`: Wraps low-level FTP client operations including connect, upload, download, list, and delete.

**`utils/` directory (native utilities):**

- `OpusUtil.kt`: OPUS audio coding/decoding through a JNI native library, including encoder management, PCM decoding, and multistream decoding.
- `AudioPlayer.kt`: Native audio player responsible for TTS-reply playback and silent-frame insertion.
- `MethodChannelUtil.kt`: Native MethodChannel wrapper that registers and dispatches calls from Flutter.

---

### 2. `videoStabilization/`

Independent video-stabilization Library Module.

- Accepts a video file or directory, identifies videos that satisfy format requirements such as resolution and frame rate, and stabilizes them.
- Produces stabilized video files and is integrated into the main app as an AAR.
- Configure the stabilization zoom ratio with `AppConstants.stabilizationZoom` (default: 1.25).

---

## 6. Internationalization (i18n)

The app uses **easy_localization** for Chinese and English localization.

- Translation files are `assets/translations/zh.json` and `assets/translations/en.json`.
- Keys use namespaces such as `bt_connect.title`, `eq.set_timeout`, and `bt_service.callback_timeout`.
- Flutter code calls the top-level `tr('namespace.key')` function. Use easy_localization's `tr()` rather than GetX's `.tr` extension because the two conflict.
- Native Android uses `values/strings.xml` (default English) and `values-zh/strings.xml` (Chinese), read through `Utils.getApp().getString(R.string.xxx)`.
