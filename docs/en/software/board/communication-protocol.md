# AI Camera-Glasses Communication Protocol

## 1. Protocol Overview

The AI camera glasses use a three-layer communication architecture consisting of the phone app, the AK1090-series chip, and the KM02G-series chip. AK1090 acts as the communication bridge and transparently forwards commands between the app and KM02G. This document defines the protocols among the three parties.

Notes:

1. In command lists, `\` means the command carries no parameter and `×` means no response is required.
2. Commands with a <span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">yellow background</span> are defined but still under development.
3. Commands between the app and KM02G can be added, deleted, or modified. When AK1090 requires no special handling, the existing AK1090 transparent-forwarding code can be reused without redevelopment.
4. When KM02G receives any command, called command A here, it:

   > 4.1 Returns `IND_ACK` to acknowledge successful receipt of command A.
   > 4.2 Executes command A.
   > 4.3 Returns the result in `IND_COMP` after command A completes.

Figure 1 shows the flow. The `IND_COMP` format depends on the result:

- If no additional result parameter is required, `IND_COMP` returns only `cmd_id` and `result`.
- If additional result parameters are required, they follow `cmd_id` and `result` in the same response.

See the `IND_COMP` command description for the detailed format.

<div align="center">

![General app/AK1090/KM02G command-interaction flow](../../../zh_CN/software/board/img/protocol-chart-1.svg)

Figure 1 General app/AK1090/KM02G command-interaction flow

</div>

> Labels embedded in the source figures are in Chinese. The surrounding numbered steps provide the English legend.

## 2. App-to-AK1090 Protocol

### 2.1 Message Format

| Field | Header marker | Command | Data length | Data | Checksum |
| ----- | ------------- | ------- | ----------- | ---- | -------- |
| Length | 1 byte | 1 byte | 2 bytes | N bytes (N \<= 504) | 4 bytes |
| Description | `@` | See the command lists below | Size of the data | Data | CRC32 checksum |

### 2.2 Command Lists

The following tables list all commands between the app (A) and AK1090 (B).

#### 2.2.1 Commands Initiated by the App

| Command | Description | Request parameters (A =&gt; B) | Response parameters (A &lt;= B) |
| ------- | ----------- | -------------------------------- | --------------------------------- |
| 0x01~0x7E | Reserved for special commands | \ | \ |
| 0x7F | AP provisioning | `uint8_t function;` // scenario for AP provisioning `char[] ssid;` // SSID, terminated by `\0` `char[] password;` // password, terminated by `\0` Values of `function`: 0x00: bind device; 0x01: gallery management; 0x02: live video; 0x03: RTSP image debugging; 0x04: RTSP recording debugging | \ |
| 0x80~0xF2 | Customer use | \ | \ |
| 0xF5 | User configuration, including USB-drive mode and recording settings | `uint8_t mode;` // default 0x01 `uint16_t duration;` // timed recording duration in seconds, default 60. Values of `mode`: 0x01: USB-drive mode; 0x02: UVC photo debugging; 0x03: UVC recording debugging | `uint8_t result;` 0x00: success; 0x01: failure |
| <span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">0xF6</span> | Factory-production-test mode | \ | `uint8_t result;` 0x00: success; 0x01: failure |
| 0xF7 | Factory-reset mode | \ | `uint8_t result;` 0x00: success; 0x01: failure |
| 0xF8 | Set local time, including time zone and time | `int16_t minutes;` // time-zone offset in minutes, for example -480 means UTC-8 `uint32_t tick;` // timestamp in seconds since 1970-01-01 00:00:00 UTC; can be parsed as RTC time | `uint8_t result;` 0x00: success; 0x01: failure |
| 0xF9 | AK1090-series OTA upgrade | \ | × |
| 0xFA | Get the AK1090-series firmware version | \ | `char[] version;` // terminated by `\0` |
| 0xFB | Unbind device | \ | `uint8_t result;` 0x00: success; 0x01: failure |
| 0xFC | Get device information | \ | `uint8_t battery;` // battery percentage |
| 0xFD | Force KM02G power-off | \ | `uint8_t result;` 0x00: success; 0x01: failure |
| 0xFE | Power on KM02G | \ | `uint8_t result;` 0x00: success (power-on ready); 0x01: failure |
| 0xFF | Transparent command. AK1090 packages a command from the app to KM02G and forwards it to KM02G | Command the app needs to send to KM02G | × |

#### 2.2.2 Commands Initiated by AK1090

| Command | Description | Request parameters (B =&gt; A) | Response parameters (B &lt;= A) |
| ------- | ----------- | -------------------------------- | --------------------------------- |
| 0xF3 | Request permission to power off KM02G | \ | `uint8_t result;` 0x00: the app allows AK1090 to power off KM02G; 0x01: the app does not allow it |
| 0xF4 | Device-state indication | `uint8_t status;` 0x01: device battery low; 0x02: KM02G power-on was not reported; 0x03: KM02G entered USB-drive or UVC mode; 0x04: KM02G is running another feature; 0x05: battery low, requesting the app to power off KM02G | × |
| 0xFF | Transparent command. AK1090 packages a KM02G-to-app command and forwards it to the app | Command KM02G needs to send to the app | × |

**Notes:**

1. When adding commands, allocate backward starting at 0xF2.
2. Either the app or AK1090 may initiate transparent command 0xFF.
3. A command that requires a response must be answered with the same command code. For example, after the app sends 0xFE to AK1090, AK1090 returns the result under command code 0xFE.
4. The 0xF6 command in this section (factory-production-test mode between the app and AK1090) is not the app-to-KM02G 0xF6 in Section 4.2.1, which corresponds to 0x76 start recording and is `APP_CMD_RECORD` in the SDK. The SDK defines factory-test commands as 0xF3 (`APP_CMD_FACTORY`) and 0x73 (`BT_CMD_FACTORY`); the Linux application does not currently handle them.

## 3. AK1090-to-KM02G Protocol

### 3.1 Message Format

<table border="1" style="border-collapse: collapse; font-family: monospace; text-align: center;">
  <tr><th>Section</th><th>Byte</th><th>0</th><th>1</th><th>2</th><th>3</th></tr>
  <tr><td rowspan="2">Head</td><td>0x00</td><td>SyncHead</td><td>Command</td><td colspan="2">ParamLen</td></tr>
  <tr><td>0x04</td><td colspan="4">Crc</td></tr>
  <tr><td>Parameter</td><td>0x08</td><td colspan="4">Payload data</td></tr>
  <tr><td>Parameter</td><td>0x0C</td><td colspan="4">Payload data</td></tr>
  <tr><td>Parameter</td><td>...</td><td colspan="4">...</td></tr>
</table>

Field definitions:

- `SyncHead`: One-byte synchronization header, fixed at 0xAA.
- `Command`: One-byte command or indication; see the command lists below.
- `ParamLen`: Two-byte parameter length; zero means no parameter.
- `Crc`: Check field for the payload.
- `Parameter`: 0-255 bytes of parameter content. The SDK's `quick_glass_info_t` parameter buffer is 255 bytes; the Linux application returns an error immediately when asked to send more than 255 bytes.

### 3.2 Command Lists

The following tables list all commands between AK1090 (B) and KM02G (K).

> **Note:** AK1090-to-KM02G command values must not exceed 0x7F.

#### 3.2.1 Commands Initiated by AK1090

| Command | Description | Request parameters (B =&gt; K) | Response parameters (B &lt;= K) |
| ------- | ----------- | -------------------------------- | --------------------------------- |
| 0x01 | Request KM02G power-off | \ | Additional `IND_COMP` parameter: `uint16_t timeout;` // delay before powering off KM02G, in seconds; default 0, meaning immediately. Power is removed only when the timeout expires. |
| 0x02 | Set local time, including time zone and time | `int16_t minutes;` // time-zone offset in minutes, e.g. -480 means UTC-8 `uint16_t year;` // year, e.g. 2023 `uint8_t month;` // 1-12 `uint8_t day;` // 1-31 `uint8_t hour;` // 0-23 `uint8_t min;` // 0-59 `uint8_t sec;` // 0-59 | \ |
| 0x03 | Define the mode used when USB is connected | `uint8_t mode;` // USB mode, effective only when connected to a computer; default 0x01. 0x01: USB-drive mode; 0x02: UVC photo debugging; 0x03: UVC recording debugging | Additional `IND_COMP` parameter: `uint8_t mode;` // active mode. 0x00: charging mode (USB charger); 0x01: USB-drive mode; 0x02: UVC photo debugging; 0x03: UVC recording debugging |
| 0x04 | Reserved for special commands | \ | \ |
| <span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">0x05</span> | Unbind device | \ | \ |
| <span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">0x06</span> | Get KM02G firmware version | \ | Additional `IND_COMP` parameter: `char[] version;` // terminated by `\0` |
| <span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">0x07</span> | Get photo, video, and audio counts | \ | Additional `IND_COMP` parameters: `uint16_t photo_count;` // photo count `uint16_t video_count;` // video count `uint16_t audio_count;` // audio count |
| 0x08 | AP provisioning | `uint8_t function;` // scenario `char[] ssid;` // terminated by `\0` `char[] password;` // terminated by `\0`. Values of `function`: 0x00: bind device; 0x01: gallery management; 0x02: live video; 0x03: RTSP image debugging; 0x04: RTSP recording debugging | \ |
| <span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">0x09</span> | Disconnect AP | \ | \ |
| <span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">0x0A</span> | P2P provisioning | `uint8_t function;` // scenario `char p2p_dev_name[];` // terminated by `\0`. Values of `function`: 0x00: bind device; 0x01: gallery management; 0x02: live video; 0x03: RTSP image debugging; 0x04: RTSP recording debugging. SDK command 0x8A distinguishes only 0x01 (gallery management) and 0x02 (live video); every other value, including 0x03 and 0x04, is handled as 0x00 (bind device), as described in Section 4.2.1. | \ |
| <span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">0x0B</span> | Disconnect P2P | \ | \ |
| <span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">0x0C</span> | KM02G OTA upgrade | \ | \ |
| 0x0D | Factory-reset mode | \ | \ |
| <span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">0x0E</span> | Get storage status | \ | Additional `IND_COMP` parameters: `uint32_t total;` // total SD NAND space in KB `uint32_t used;` // used SD NAND space in KB |
| <span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">0x0F</span> | Get the file count of a storage directory | \ | Additional `IND_COMP` parameter: `uint16_t count;` // file count |
| 0x10~0x1F | Reserved for special commands | \ | \ |
| 0x20~0x4F | Customer use | \ | \ |
| 0x50~0x72 | Reserved for special commands | \ | \ |
| <span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">0x73</span> | Factory-production-test mode | \ | \ |
| 0x74 | Take a photo | `int16_t minutes;` // time-zone offset in minutes, e.g. -480 means UTC-8 `uint16_t year;` // year, e.g. 2023 `uint8_t month;` // 1-12 `uint8_t day;` // 1-31 `uint8_t hour;` // 0-23 `uint8_t min;` // 0-59 `uint8_t sec;` // 0-59 | \ |
| 0x75 | Take a snapshot | \ | \ |
| 0x76 | Start video recording | `int32_t duration;` // duration in seconds. For values greater than zero, the SDK records for that duration without an upper limit; values less than or equal to zero mean 600 seconds. Recording stops automatically when time expires. Followed by `int16_t minutes;` // time-zone offset in minutes, e.g. -480 means UTC-8 `uint16_t year;` // year, e.g. 2023 `uint8_t month;` // 1-12 `uint8_t day;` // 1-31 `uint8_t hour;` // 0-23 `uint8_t min;` // 0-59 `uint8_t sec;` // 0-59 | \ |
| 0x77 | Stop video recording | \ | \ |
| <span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">0x78</span> | Start audio recording | `int32_t duration;` // recording duration in seconds `int32_t min_duration;` // minimum duration in seconds. The SDK uses only the low eight bits of both values, treating them as `uint8_t` (0-255 seconds). Recording stops automatically when time expires. | \ |
| <span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">0x79</span> | Stop audio recording | \ | \ |
| 0x7A | Acknowledge a received data packet | Reply to `IND_UPLOAD_HEAD` or `IND_UPLOAD_PACK`: `uint8_t result;` 0x00: received successfully; 0x01: receive failure | × |

````{only} anyka_review
```{admonition} Pending source clarification
:class: warning

The SDK defines AK1090 commands 0x01-0x03 and 0x73-0x7F (`BT_CMD_*`, `BT_IND_*`); its Linux app handles 0x01-0x03, 0x74, 0x76, and 0x77, and handles 0x78 and 0x79 only when `SOUND_REC_SUPPORT_ENABLE` is enabled (disabled by default). Commands 0x04-0x0F are not defined in the SDK. The SDK defines these functions as app commands instead: 0x85-0x8D correspond to 0x05-0x0D; 0x86, 0x88, and 0x8A-0x8D are implemented, while 0x85, 0x87, and 0x89 are defined but not implemented. Storage status and directory file count are app commands 0x82 and 0x83 (see Section 4.2.1). Anyka must confirm how AK1090 and RTT forward 0x04-0x0F.
```
````

#### 3.2.2 Commands Initiated by KM02G

| Command | Description | Request parameters (K =&gt; B) | Response parameters (K &lt;= B) |
| ------- | ----------- | -------------------------------- | --------------------------------- |
| 0x7B | `IND_READY`, indicating that KM02G has powered on and is ready | Initiated by the Linux application; no parameters | × |
| 0x7C | `IND_ACK`, command acknowledgement | Initiated by the small system: `uint8_t result;` 0x00: command received successfully; 0x01: command receive failure | × |
| 0x7D | `IND_UPLOAD_HEAD`, uploading data-header information and the first packet | Initiated by the small system. The parameter is the chunk data in each packet. See the `IND_UPLOAD_HEAD` and `IND_UPLOAD_PACK` format definitions. | × |
| 0x7E | `IND_UPLOAD_PACK`, uploading chunked data | Initiated by the small system. The parameter is the chunk data in each packet. See the `IND_UPLOAD_PACK` format definition. | × |
| 0x7F | `IND_COMP`, returning a command's execution result | Initiated by the Linux application or small system: `uint8_t cmd_id;` // copied from the `Command` received by KM02G `uint8_t result;` // execution result; see KM02G error codes. If the command result includes additional parameters, append them here. | × |

Examples:

1. After AK1090 sends 0x74 (take a photo) to KM02G, KM02G ultimately returns this `IND_COMP` byte stream: `0xAA 0x7F 0x0002 0x00000000 0x74 0x00`.
2. After AK1090 sends 0x01 (request KM02G power-off), if KM02G requests immediate power-off (0 seconds, or 0x0000), KM02G ultimately returns: `0xAA 0x7F 0x0004 0x00000000 0x01 0x00 0x0000`.
3. After the same 0x01 request, if KM02G requests power-off after 10 seconds (0x000A), it returns: `0xAA 0x7F 0x0004 0x00000000 0x01 0x00 0x000A`.

## 4. App-to-KM02G Protocol

### 4.1 Communication Format

The app and KM02G communicate indirectly; AK1090 transparently forwards every command. Figure 2 shows the flow.

For an app-to-KM02G command, called command B:

1. The app packages command B in the `Data` field of transparent command 0xFF.
2. The app sends the packaged 0xFF command to AK1090.
3. AK1090 extracts command B and forwards it to KM02G.

For a KM02G-to-app command, called command C:

1. KM02G sends command C to AK1090.
2. AK1090 applies the KM02G command-routing rules. If the command must go to the app, AK1090 packages it in the `Data` field of transparent command 0xFF.
3. AK1090 sends the packaged 0xFF command to the app.

<div align="center">

![Transparent command-forwarding flow](../../../zh_CN/software/board/img/protocol-chart-2.svg)

Figure 2 Transparent command-forwarding flow

</div>

> **Note:** App-to-KM02G command values must not be less than 0x80.

### 4.2 Command Lists

The following tables list all commands between the app (A) and KM02G (K).

#### 4.2.1 Commands Initiated by the App

<table border="1" style="border-collapse: collapse; font-family: monospace; text-align: center;">
  <tr><th>Command</th><th>Description</th><th>Request parameters (A =&gt; K)</th><th>Response parameters (A &lt;= K)</th></tr>
  <tr><td>0x81</td><td colspan="3">See AK1090-to-KM02G command 0x01.</td></tr>
  <tr><td>0x82</td><td>Get storage status</td><td>\</td><td><code>uint16_t used;</code> // used space in MB<br><code>uint16_t left;</code> // remaining space in MB</td></tr>
  <tr><td>0x83</td><td>Get the file count of a storage directory</td><td><code>uint8_t type;</code> // 0: all; 1: video; 2: image; 3: audio<br>(type 4 returns a file count of 0; values greater than 4 return no response)</td><td><code>int16_t file_count_type;</code> // same as requested type<br><code>int16_t file_count;</code> // file count</td></tr>
  <tr><td><span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">0x84</span></td><td colspan="3">Image import (`APP_CMD_IMPORT` is defined in the SDK but not implemented).</td></tr>
  <tr><td><span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">0x85</span></td><td colspan="3">See AK1090-to-KM02G command 0x05.</td></tr>
  <tr><td>0x86</td><td colspan="3">See AK1090-to-KM02G command 0x06.</td></tr>
  <tr><td><span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">0x87</span></td><td colspan="3">See AK1090-to-KM02G command 0x07.</td></tr>
  <tr><td>0x88</td><td>AP provisioning</td><td><code>uint8_t ap_ssid[64];</code> // terminated by <code>\0</code><br><code>uint8_t ap_password[64];</code> // terminated by <code>\0</code><br>(no function byte)</td><td>Same as AK1090-to-KM02G command 0x08.</td></tr>
  <tr><td><span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">0x89</span></td><td colspan="3">See AK1090-to-KM02G command 0x09.</td></tr>
  <tr><td>0x8A</td><td>P2P provisioning</td><td><code>uint8_t state;</code> // 0x00: bind device; 0x01: gallery import; 0x02: live video; other values are treated as bind-device<br><code>char p2p_dev_name[];</code> // P2P device name, parameter length minus 1, at most 63 bytes<br>(a 24-byte parameter uses the old format: device name only, handled as live video)</td><td>No response when state is 0x01; otherwise returns the execution result.</td></tr>
  <tr><td>0x8B</td><td colspan="3">See AK1090-to-KM02G command 0x0B.</td></tr>
  <tr><td>0x8C</td><td>KM02G OTA upgrade</td><td><code>uint8_t ota_file_path[128];</code> // upgrade-package path; must be under <code>/mnt/</code> and may contain only letters, digits, and <code>. _ - /</code></td><td>Returns 0x01 for an invalid path or 0x06 if the package does not exist. If checks pass, the upgrade starts immediately and no response is returned.</td></tr>
  <tr><td>0x8D</td><td colspan="3">See AK1090-to-KM02G command 0x0D.</td></tr>
  <tr><td><span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">0x8E</span></td><td colspan="3">Start RTSP (`APP_CMD_START_RTSP` is defined in the SDK but not implemented).</td></tr>
  <tr><td>0x8F</td><td colspan="3">Reserved (not defined in the SDK).</td></tr>
  <tr><td>0x90~0x9F</td><td colspan="3">Reserved for special commands.</td></tr>
  <tr><td>0xA0~0xCF</td><td colspan="3">Customer use.</td></tr>
  <tr><td>0xD0~0xF2</td><td colspan="3">Reserved for special commands.</td></tr>
  <tr><td><span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">0xF3</span></td><td colspan="3">See AK1090-to-KM02G command 0x73.</td></tr>
  <tr><td>0xF4</td><td colspan="3">See AK1090-to-KM02G command 0x74.</td></tr>
  <tr><td><span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">0xF5</span></td><td colspan="3">See AK1090-to-KM02G command 0x75.</td></tr>
  <tr><td>0xF6</td><td colspan="3">See AK1090-to-KM02G command 0x76.</td></tr>
  <tr><td>0xF7</td><td colspan="3">See AK1090-to-KM02G command 0x77.</td></tr>
  <tr><td><span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">0xF8</span></td><td colspan="3">See AK1090-to-KM02G command 0x78.</td></tr>
  <tr><td><span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">0xF9</span></td><td colspan="3">See AK1090-to-KM02G command 0x79.</td></tr>
  <tr><td>0xFA</td><td colspan="3">See AK1090-to-KM02G command 0x7A.</td></tr>
</table>

#### 4.2.2 Commands Initiated by KM02G

<table border="1" style="border-collapse: collapse; font-family: monospace; text-align: center;">
  <tr><th>Command</th><th>Description</th><th>Request parameters (K =&gt; A)</th><th>Response parameters (K &lt;= A)</th></tr>
  <tr><td>0xFB</td><td colspan="3">See AK1090-to-KM02G command 0x7B.</td></tr>
  <tr><td>0xFC</td><td colspan="3">See AK1090-to-KM02G command 0x7C.</td></tr>
  <tr><td><span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">0xFD</span></td><td colspan="3">See AK1090-to-KM02G command 0x7D.</td></tr>
  <tr><td><span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">0xFE</span></td><td colspan="3">See AK1090-to-KM02G command 0x7E.</td></tr>
  <tr><td>0xFF</td><td colspan="3">See AK1090-to-KM02G command 0x7F.</td></tr>
</table>

## 5. Other Definitions

### 5.1 KM02G Error Codes

<table border="1" style="border-collapse: collapse; font-family: monospace; text-align: center;">
  <tr><th>Error code</th><th>Description</th></tr>
  <tr><td>0x00</td><td>Success</td></tr>
  <tr><td>0x01</td><td>Invalid parameter</td></tr>
  <tr><td>0x02</td><td>Failed to set parameter</td></tr>
  <tr><td>0x03</td><td>Recording time too short</td></tr>
  <tr><td>0x04</td><td>Recording time too long</td></tr>
  <tr><td>0x05</td><td>Failed to write file</td></tr>
  <tr><td>0x06</td><td>Failed to read file</td></tr>
  <tr><td>0x07</td><td>Failed to create file</td></tr>
  <tr><td>0x08</td><td>Memory allocation failed</td></tr>
  <tr><td>0x09</td><td>Device busy</td></tr>
  <tr><td>0x0A</td><td>Timeout</td></tr>
  <tr><td>0x0B</td><td>SD NAND not mounted</td></tr>
  <tr><td>0x0C</td><td>Wi-Fi node failed</td></tr>
  <tr><td>0x0D</td><td>Failed to unmount SD NAND</td></tr>
  <tr><td>0x0E</td><td>Device not running</td></tr>
  <tr><td>0x0F</td><td>Insufficient device space</td></tr>
  <tr><td>0x10</td><td>Creation failed</td></tr>
  <tr><td>0x11</td><td>Formatting failed</td></tr>
  <tr><td>0x12</td><td>No file on the card</td></tr>
  <tr><td>0xFF</td><td>Unknown error</td></tr>
</table>

### 5.2 `IND_UPLOAD_HEAD` Format

<table border="1" style="border-collapse: collapse; font-family: monospace; text-align: center;">
  <tr><th>Section</th><th>Type</th><th>Size</th><th>Description</th><th>Example</th></tr>
  <tr><td>file_id</td><td>uint32_t</td><td>4</td><td>Unique file ID assigned by the initiator</td><td>1</td></tr>
  <tr><td>name</td><td>char[]</td><td>64</td><td>Original file name, including extension</td><td>"video.mp4"</td></tr>
  <tr><td>size</td><td>uint32_t</td><td>4</td><td>Total file size in bytes</td><td>104857600</td></tr>
  <tr><td>chunk_index</td><td>uint32_t</td><td>4</td><td>Current chunk index, starting at 0</td><td>1</td></tr>
  <tr><td>chunk_count</td><td>uint32_t</td><td>4</td><td>Total number of chunks</td><td>50</td></tr>
  <tr><td>payload</td><td>char[]</td><td>N</td><td>Per-packet data for the chunk</td><td></td></tr>
</table>

### 5.3 `IND_UPLOAD_PACK` Format

<table border="1" style="border-collapse: collapse; font-family: monospace; text-align: center;">
  <tr><th>Section</th><th>Type</th><th>Size</th><th>Description</th><th>Example</th></tr>
  <tr><td>file_id</td><td>uint32_t</td><td>4</td><td>Unique file ID assigned by the initiator</td><td>1</td></tr>
  <tr><td>chunk_index</td><td>uint32_t</td><td>4</td><td>Current chunk index, starting at 0</td><td>1</td></tr>
  <tr><td>payload</td><td>char[]</td><td>N</td><td>Per-packet data for the chunk</td><td></td></tr>
</table>

### 5.4 Additional Notes

- **KM02G command routing:** When AK1090 receives a KM02G command, it checks bit 7, the most significant bit of `Command`:
  > If bit 7 is 0, AK1090 handles the command itself.
  > If bit 7 is 1, AK1090 forwards the command to the app through transparent command 0xFF.
- KM02G cannot identify who initiated power-on (the app or AK1090). When the app initiates it, AK1090 must forward `IND_READY` to notify the app that KM02G power-on initialization has completed.
- `IND_UPLOAD_HEAD` and `IND_UPLOAD_PACK` use reliable transmission. After each packet, the sender must wait for a successful-receipt acknowledgement before sending the next packet.
- The phone app, AK1090, and KM02G currently do not perform CRC validation on received commands.
- All commands listed in this document are used by Anyka Micro. Customer-defined ranges are:
  > App to AK1090: 0x80-0xF2, 115 commands.
  > AK1090 to KM02G: 0x20-0x4F, 48 commands.
  > App to KM02G: 0xA0-0xCF, 48 commands.
