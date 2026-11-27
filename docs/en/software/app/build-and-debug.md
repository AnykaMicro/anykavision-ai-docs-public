# Build and Debug Instructions

```{note}
The companion Anyka_Glasses app was not included in this release: neither an installation package nor source code was provided. Developers may supply them in a later version. This page is currently for reference only.
```

## Introduction

This document explains how to package the Anyka Glasses app source code as an APK that can be installed on an Android phone.

### What Is the Anyka Glasses App?

Anyka Glasses is a mobile app for controlling smart glasses. It lets you:

- Connect to a smart-glasses device
- View photos and videos captured by the glasses
- Configure the glasses' features

### Technical Notes

- **Development framework**: The app uses Flutter, Google's cross-platform framework for developing both Android and iOS apps.
- **Release scope**: This release does not provide the Anyka_Glasses app source or installation package. Developers may supply them in a later version. This page describes how to package and debug the Android project and is for reference only. iOS is not currently supported.
- **Project structure**: The project may contain iOS-related configuration files, such as an anyBlue configuration. Flutter generates these automatically; they do not affect the Android build.

---

## Prerequisites

Before starting, install the following free tools from their official websites.

### 1. Flutter SDK (Required)

The Flutter SDK is the core toolkit for developing Flutter applications.

**Required version**: 3.3.3 or later (stable 3.19.x recommended)

**Download**: <https://flutter.dev/docs/get-started/install>

**Installation**:

1. Visit the link and choose the package for your operating system (Windows, macOS, or Linux).
2. Download and extract it to a directory such as `C:\flutter` or `~/flutter`.
3. Add `flutter/bin` to the system `PATH` environment variable (see "Configuring Environment Variables" below).

### 2. Android Studio (Required)

Android Studio is Google's official Android application development tool.

**Required version**: Hedgehog (2023.1.1) or later

**Download**: <https://developer.android.com/studio>

**Components to select during installation**:

- ☑ Android SDK
- ☑ Android SDK Platform (API 26-36)
- ☑ Android SDK Build-Tools
- ☑ Android SDK Command-line Tools

> **Tip:** If Android Studio is already installed, check or install missing components as follows:
>
> 1. Open Android Studio.
> 2. Select `Tools` → `SDK Manager` from the menu bar.
> 3. On `SDK Platforms`, select API 26-36.
> 4. On `SDK Tools`, select `Android SDK Build-Tools` and `Android SDK Command-line Tools`.
> 5. Click `Apply` to install them.

### 3. JDK (Java Development Kit) (Required)

The JDK is the Java development toolkit required to build Android applications.

**Required version**: JDK 11 or JDK 17

**Installation** (choose one):

- **Recommended**: Use the JDK bundled with Android Studio; no separate installation is required.
- Download and install a standalone JDK from <https://adoptium.net/>.

### 4. Android NDK (Required)

The NDK is Android's native development toolkit and is used to compile some low-level code.

**Required version**: 27.2.12479018

**Installation**:

1. Open Android Studio.
2. Select `Tools` → `SDK Manager` from the menu bar.
3. Switch to `SDK Tools`.
4. Select `NDK (Side by side)` and version `27.2.12479018`.
5. Click `Apply` to install it.

### 5. cmdline-tools (Required)

`cmdline-tools` contains the Android SDK command-line tools used to run Android commands in a terminal.

**Installation**:

1. Open Android Studio.
2. Select `Tools` → `SDK Manager` from the menu bar.
3. Switch to `SDK Tools`.
4. Select `Android SDK Command-line Tools (latest)`.
5. Click `Apply` to install it.

> **Note:** After installation, cmdline-tools is under `Android SDK directory/cmdline-tools/latest/bin/`.

---

## Configuring Environment Variables

Environment variables tell the computer where to find these tools. After configuration, their commands can be used from any directory.

### Windows

1. Right-click "This PC," select "Properties," and click "Advanced system settings."
2. Click "Environment Variables."
3. Under "System variables," click "New" and add:

| Variable | Value (adjust to your installation path) |
| -------- | ---------------------------------------- |
| `FLUTTER_HOME` | `C:\flutter` |
| `ANDROID_HOME` | `C:\Users\your-user-name\AppData\Local\Android\Sdk` |
| `JAVA_HOME` | `C:\Program Files\Android\Android Studio\jbr` |

4. Edit `Path` and add:
   - `%FLUTTER_HOME%\bin`
   - `%ANDROID_HOME%\platform-tools`
   - `%ANDROID_HOME%\cmdline-tools\latest\bin`

### macOS/Linux

1. Open a terminal.
2. Edit the appropriate configuration file for your shell:
   - Bash: `nano ~/.bashrc` or `nano ~/.bash_profile`
   - Zsh: `nano ~/.zshrc`
3. Append:

```bash
export FLUTTER_HOME=~/flutter
export ANDROID_HOME=~/Library/Android/sdk
export JAVA_HOME=/Applications/Android\ Studio.app/Contents/jbr/Contents/Home
export PATH=$PATH:$FLUTTER_HOME/bin:$ANDROID_HOME/platform-tools:$ANDROID_HOME/cmdline-tools/latest/bin
```

4. Save the file (`Ctrl+O`, `Enter`, then `Ctrl+X`).
5. Apply the configuration:
   - Bash: `source ~/.bashrc` or `source ~/.bash_profile`
   - Zsh: `source ~/.zshrc`

---

## Verifying the Installation

After configuration, verify that every tool is installed correctly.

### 1. Check the Flutter Environment

Open a terminal (CMD or PowerShell on Windows, Terminal on macOS/Linux) and run:

```bash
flutter doctor
```

This checks whether Flutter is configured correctly. Expected output resembles:

```
[✓] Flutter (Channel stable, 3.x.x, ...)
[✓] Android toolchain - develop for Android devices
[✓] Android Studio (version 2023.x)
[✓] Connected device (optional; required only for debugging)
```

**Notes**:

- `[✓]` means the check passed.
- `[✗]` means there is a problem that must be fixed according to the prompt.
- `[!]` is a warning and may not affect basic functionality.

If `[✗]` or `[!]` appears, follow the displayed instructions to resolve it.

### 2. Check Environment Variables

Run the commands for your platform:

```bash
# Windows
where flutter
where adb

# macOS/Linux
which flutter
which adb
```

If tool paths are displayed, the configuration succeeded.

---

## Installing Project Dependencies

### 1. Enter the Project Directory

In a terminal, switch to the project root that contains `pubspec.yaml`:

```bash
cd /path/to/anyka_ai
```

> Replace `/path/to/anyka_ai` with the actual project path.

### 2. Download Dependencies

Run:

```bash
flutter pub get
```

The command reads `pubspec.yaml` and downloads all required Dart and Flutter packages. Depending on network speed, this may take several minutes.

**Success indicator**: `Got dependencies!` or a similar message appears.

---

## Building the APK

After the prerequisites are ready, build the APK.

### Build Command

From the project root (`anyka_ai`), run:

```bash
flutter build apk --flavor glasses
```

**Build duration**:

- The first build may take 5-10 minutes, depending on computer performance.
- Later builds are faster, approximately 1-3 minutes.

### Locate the Generated APK

After a successful build, the APK is at:

```
build/app/outputs/apk/glasses/release/app-glasses-release.apk
```
