# User Guide

```{note}
The companion Anyka_Glasses app was not included in this release: neither an installation package nor source code was provided. Developers may supply them in a later version. This page is currently for reference only.
```

## 1. Product Overview

Anyka\_Glasses is a mobile app integrating AI conversation, real-time video transmission, image recognition, and media management. It connects a mobile device over Bluetooth to provide convenient, intelligent interaction. This guide describes the features and their operation.

## 2. Binding a Device

Bind the device before first use.

### 2.1 First Binding

To bind and pair a device with the phone app for the first time:

1. **Start the app:** Open Anyka\_Glasses on the phone.
2. **Open the binding screen:** Tap the `+` icon in the upper-right corner of the home page or the "Bind device" button in the center.
3. **Scan:** The system automatically searches for nearby Bluetooth devices.
4. **Select:** Find and tap your smart-glasses model in the device list.
5. **Confirm:** Select "Pair" in the Bluetooth pairing-request dialog.
6. **Wait:** Binding finishes when the screen reports a successful connection.

**Notes:**

1. Make sure the phone's Bluetooth and Wi-Fi are enabled.
2. Keep the device within 10 m of the phone.
3. If the device cannot be found, check that it is discoverable.

![Home screen with no bound device](../../../zh_CN/software/app/img/home-unpaired.jpeg)

Figure 2-1 Home screen with no bound device</br><br>

![Home screen with a bound device](../../../zh_CN/software/app/img/home-paired.jpeg)

Figure 2-2 Home screen with a bound device

> Text embedded in these source screenshots is in Chinese; the surrounding steps give the corresponding controls in English.

### 2.2 Connection-State Management

After binding succeeds, the device connection information is saved automatically. On later use, turn on the device and open the app; the system attempts to reconnect automatically. The home-page indicator displays the current connection state in real time.

## 3. AI Conversation

AI conversation requires License permission. There are two ways to obtain it:

1. Register an account on [Alibaba Cloud Model Studio](https://bailian.console.aliyun.com/), create an AI-conversation model, record its `APIKey`, `workspaceId`, and `AppId`, and enter them in the app's AI-conversation settings.
2. Apply for an Anyka License. If no License is available when opening AI conversation, the app displays a License-error message. Copy that information for the application. Restart the app after approval.

Enter API keys only at runtime. Do not commit them to source control or include them in screenshots or logs.

AI conversation supports image recognition and voice Q&A. For image recognition, first enable AI conversation, then double-press the device's capture button. The app uploads the image to the model for recognition. The result is announced by voice and also displayed on the "AI conversation" screen. AI-conversation mode times out after eight seconds and then exits automatically.

![AI-conversation screen](../../../zh_CN/software/app/img/ai-chat.jpeg)

Figure 3-1 AI-conversation screen

### 3.1 Starting the Feature

AI conversation can be started in either of two ways.

**On the device:**

1. Locate the K2 function button on the glasses frame.
2. Double-press it.
3. Begin speaking after the startup prompt sounds.

**On the phone:**

1. Open the app's home screen.
2. Tap "AI conversation."

### 3.2 AI Image-Recognition Procedure

AI image recognition is a core feature:

1. **Activate conversation:** Start AI conversation by either method above.
2. **Aim:** Point the glasses at the object or scene to recognize.
3. **Capture:** Double-press the capture button on the glasses.
4. **Upload and analyze:** The system uploads the image to the AI server automatically.
5. **Receive the result:** Listen to the recognition result and read it on the conversation screen.

![AI image recognition](../../../zh_CN/software/app/img/ai-image-recognition.png)

Figure 3-2 AI image recognition

### 3.3 Voice Q&A

In AI-conversation mode, ask a question by voice. The system analyzes it and returns a spoken answer.

## 4. Gallery Management

Open "Gallery" to view photos and videos stored on the device.

![Gallery-management screen](../../../zh_CN/software/app/img/gallery.png)

Figure 4-1 Gallery-management screen

### 4.1 Browsing the Gallery

Gallery management lets you:

1. Browse device photos and videos chronologically.
2. View file details such as capture time and file size.

### 4.2 Importing Files

To import media files from the device to the phone:

1. Open "Gallery."
2. Tap "Import media files" at the bottom.
3. Wait for transfer to complete.
4. The app reports "X files imported successfully."

### 4.3 Managing Files

To select files in a batch:

1. Long-press a photo or video to enter multi-select mode.
2. Tap each file to operate on.
3. Delete the selected files as needed.

## 5. Live Video

Open "Live video" and wait briefly for the device's real-time video. Landscape full-screen playback is supported; tap the video area to switch full-screen mode.

![Live-video screen](../../../zh_CN/software/app/img/live-video.png)

Figure 5-1 Live-video screen

## 6. Settings

![Settings screen](../../../zh_CN/software/app/img/settings.jpg)

Figure 6-1 Settings screen

### 6.1 Version Information and Hidden Settings

View the current app version. Tap the version number five times within three seconds to reveal hidden settings. These settings are intended for device debugging, development tests, and advanced customization; ordinary users normally do not need them.

1. **Conversation settings**

   - Phone AI conversation: Enable or disable phone-side AI conversation.
   - Uplink audio playback: Play the audio stream uploaded by the device in real time.
   - Downlink audio playback: Play the audio stream sent to the device in real time.
   - Half-duplex interaction: Switch the conversation interaction mode.
   - Conversation timeout: Set a timeout from 3 to 60 seconds.

2. **Bluetooth and connection settings**

   - Bluetooth scan rules: Configure Bluetooth-device scan filters.
   - BLE downlink: Select the data-transmission method.
   - BLE connection type: Select the Bluetooth connection mode.

3. **Audio, device, and image debugging**

   - Device audio loopback: Enable or disable the audio-loopback test.
   - Save uplink PCM: Choose whether to save raw PCM uploaded by the device.
   - Stabilization zoom: Set the video-stabilization zoom ratio from 1 to 2.

4. **Debugging and logs**

   - P2P connection logs: Show or hide detailed P2P logs.

5. **RTSP live-video settings**

   - Live-video timeout: Set the RTSP timeout from 1 to 30 minutes.

6. **Recording settings**

   - Timed-recording duration: Set 1-600 seconds. The device accepts any positive duration; a value less than or equal to zero records for 600 seconds.

7. **UVC mode**

   - UVC mode: Select the required UVC mode from the drop-down menu.

8. **OTA test**

   - OTA stress test: Enable or disable OTA-upgrade stress testing.

### 6.2 OTA Upgrade

The firmware-upgrade feature updates device firmware. It currently supports OTA upgrades of AK1090-series firmware. Separate Chinese and English firmware variants may be flashed as needed; neither was included in this release (see Section 7), and developers may supply them in a later version.

Procedure:<br>
1. Place the upgrade package in phone storage.<br>
2. In the app, open "Settings" → "OTA upgrade" → "Bluetooth firmware OTA upgrade."<br>
3. Tap the arrow button, select the upgrade-package file from the phone, and wait for completion.

This is a vendor procedure; OTA and firmware behavior have not been verified on physical hardware in this release.

![OTA device-version screen](../../../zh_CN/software/app/img/ota-firmware-versions.jpeg)

Figure 6-2 Device-version information in OTA upgrade

![OTA screen with no upgrade file selected](../../../zh_CN/software/app/img/ota-no-file-selected.jpeg)

Figure 6-3 No OTA upgrade file selected

![OTA screen with an upgrade file selected](../../../zh_CN/software/app/img/ota-file-selected.jpeg)

Figure 6-4 OTA upgrade file selected

### 6.3 AI-Conversation Settings

![AI-key settings](../../../zh_CN/software/app/img/ai-key-settings.jpeg)

Figure 6-5 AI-key settings

If you have an Alibaba Cloud Model Studio AI model, enter its API Key, Workspace Id, App Id, and other required credentials. AI conversation becomes available after the settings succeed. If you do not have or do not want to create a model, apply to an Anyka FAE for License permission.

Enter credentials only at runtime; never commit them or expose them in screenshots or logs.

### 6.4 Unbinding

The unbind action is the last item in the card below Help. For safety, tapping it opens a confirmation dialog; confirm before the current device binding is removed.

## 7. Obtaining the Software

The Anyka_Glasses APK and the Chinese and English AK1090-series firmware variants were not included in this release. Developers may upload these packages and add download links here in a later version.
