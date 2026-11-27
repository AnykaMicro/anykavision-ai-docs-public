# Logging

## Overview

&emsp;&emsp;The logging module is an infrastructure module that outputs records from each module and the system log.

<br/>

## API Reference

&emsp;&emsp;This module provides the APIs listed below.

| **Data structure** | **Description** |
| ------------ | -------- |
| MODULE_ID_E | Module ID |
| LOG_LEVEL_E | Log level |

<br/>

| **Function**        | **Description**         |
| ------------------------- | ---------------------- |
| AK_BASE_PrintGetVersion | Gets logging-module version information. |
| AK_BASE_PrintError | Outputs an error message. |
| AK_BASE_PrintWarning | Outputs a warning message. |
| AK_BASE_PrintNotice | Outputs a notice message. |
| AK_BASE_PrintNormal | Outputs a normal log message. |
| AK_BASE_PrintInfo | Outputs an info message. |
| AK_BASE_PrintDebug | Outputs a debug message. |
| AK_BASE_PrintErrorEx | Outputs an error message. |
| AK_BASE_PrintWarningEx | Outputs a warning message. |
| AK_BASE_PrintNoticeEx | Outputs a notice message. |
| AK_BASE_PrintNormalEx | Outputs a normal log message. |
| AK_BASE_PrintInfoEx | Outputs an info message. |
| AK_BASE_PrintDebugEx | Outputs a debug message. |
| AK_BASE_PrintSetLevel | Sets the real-time physical-serial-port log level. |
| AK_BASE_PrintSetSyslogLevel | Sets the system-log level. |

<br/>

## Data Structures

### MODULE_ID_E

&emsp;&emsp;【Notes】

&emsp;&emsp;Module IDs.

&emsp;&emsp;【Definition】

```c
typedef enum akMODULE_ID_E {
    MODULE_ID_MEMORY                 = 0x0,
    MODULE_ID_THREAD,
    MODULE_ID_LOG,
    MODULE_ID_COMMON,
    MODULE_ID_IPCSRV,
    MODULE_ID_AI,
    MODULE_ID_AO,
    MODULE_ID_VI,
    MODULE_ID_VO,
    MODULE_ID_TIMER,
    MODULE_ID_VPSS,
    MODULE_ID_DRV,
    MODULE_ID_TDE,
    MODULE_ID_VENC,
    MODULE_ID_VDEC,
    MODULE_ID_AENC,// 15
    MODULE_ID_ADEC,
    MODULE_ID_OSD,
    MODULE_ID_MUX,
    MODULE_ID_DEMUX,
    MODULE_ID_DVR,
    MODULE_ID_MD,
    MODULE_ID_GUI,
    MODULE_ID_AED,
    MODULE_ID_AUDIO_TOOL,

    MODULE_ID_VQE,

    MODULE_ID_APP_VIDEO,
    MODULE_ID_DVR_IDX,
    MODULE_ID_NET,
    MODULE_ID_OSAL,
    MODULE_ID_APP_MEM,
    MODULE_ID_APP_AUDIO,
    MODULE_ID_UUID,
    MODULE_ID_ATC_ECHO,
    MODULE_ID_ATC_ADEC,
    MODULE_ID_ATC_AENC,
    MODULE_ID_AKV_VENC,
    MODULE_ID_AKV_VDEC,
    MODULE_ID_AKV_MUX,
    MODULE_ID_AKV_DEMUX,
    MODULE_ID_SVP,
    MODULE_ID_AKV_CNN,
    MODULE_ID_FR,
    MODULE_ID_AUDIO_EFFECT,

    MODULE_ID_APP                     = 0xFE,
    MODULE_ID_ALL                     = 0xFF,
}MODULE_ID_E;
```

&emsp;&emsp;【Members】

| **Member**           | **Description**             |
| ---------------------- | -------------------- |
| MODULE_ID_MEMORY | Memory-management module ID |
| MODULE_ID_THREAD | Multithreading module ID |
| MODULE_ID_LOG | Logging module ID |
| MODULE_ID_COMMON | Common-services module ID |
| MODULE_ID_IPCSRV | Currently unused |
| MODULE_ID_AI | Audio-input module ID |
| MODULE_ID_AO | Audio-output module ID |
| MODULE_ID_VI | Video-input module ID |
| MODULE_ID_VO | Video-output module ID |
| MODULE_ID_TIMER | Internal timer video ID |
| MODULE_ID_VPSS | Video processing subsystem module ID |
| MODULE_ID_DRV | Driver-adaptation-layer ID |
| MODULE_ID_TDE | 2D image-engine module ID |
| MODULE_ID_VENC | Video-encoding module ID |
| MODULE_ID_VDEC | Video-decoding module ID |
| MODULE_ID_AENC | Audio-encoding module ID |
| MODULE_ID_ADEC | Audio-decoding module ID |
| MODULE_ID_OSD | Video-overlay module ID |
| MODULE_ID_MUX | Recording-mux module ID |
| MODULE_ID_DEMUX | Recording-demux module ID |
| MODULE_ID_DVR | Currently unused |
| MODULE_ID_MD | Motion-detection module ID |
| MODULE_ID_GUI | Currently unused |
| MODULE_ID_AED | RTSP module ID |
| MODULE_ID_AUDIO_TOOL | Audio tuning-tool module ID |
| MODULE_ID_VQE | Voice-quality enhancement module ID |
| MODULE_ID_APP_VIDEO | Video-stream-mode ID |
| MODULE_ID_DVR_IDX | Currently unused |
| MODULE_ID_NET | Network-adaptation-layer module ID |
| MODULE_ID_OSAL | Middleware-adaptation-layer module ID |
| MODULE_ID_APP_MEM | Extended memory-management module ID |
| MODULE_ID_APP_AUDIO | Audio-stream-mode module ID |
| MODULE_ID_UUID | Chip unique-ID module ID |
| MODULE_ID_ATC_ECHO | Echo-cancellation library logging ID |
| MODULE_ID_ATC_ADEC | ATC audio-decoding library logging ID |
| MODULE_ID_ATC_AENC | ATC audio-encoding library logging ID |
| MODULE_ID_AKV_VENC | ATC video-encoding library logging ID |
| MODULE_ID_AKV_VDEC | ATC video-decoding library logging ID |
| MODULE_ID_AKV_MUX | ATC recording-mux library logging ID |
| MODULE_ID_AKV_DEMUX | ATC recording-demux library logging ID |
| MODULE_ID_SVP | Smart-vision-processing module ID |
| MODULE_ID_AKV_CNN | ATC CNN library logging ID |
| MODULE_ID_FR | FR module ID |
| MODULE_ID_AUDIO_EFFECT | Audio-effects module ID |
| MODULE_ID_APP | User logging ID |
| MODULE_ID_ALL | Maximum module ID |

&emsp;&emsp;【Related Functions】

```c
    AK_S32 AK_BASE_PrintError(AK_S32 s32ModuleId, const AK_CHAR *pcFmt, ...);
    AK_S32 AK_BASE_PrintWarning(AK_S32 s32ModuleId, const AK_CHAR *pcFmt, ...);
    AK_S32 AK_BASE_PrintNotice(AK_S32 s32ModuleId, const AK_CHAR *pcFmt, ...);
    AK_S32 AK_BASE_PrintNormal(AK_S32 s32ModuleId, const AK_CHAR *pcFmt, ...);
    AK_S32 AK_BASE_PrintInfo(AK_S32 s32ModuleId, const AK_CHAR *pcFmt, ...);
    AK_S32 AK_BASE_PrintDebug(AK_S32 s32ModuleId, const AK_CHAR *pcFmt, ...);
    AK_S32 AK_BASE_PrintErrorEx(AK_S32 s32ModuleId, const AK_CHAR *pcFmt, ...);
    AK_S32 AK_BASE_PrintWarningEx(AK_S32 s32ModuleId, const AK_CHAR *pcFmt, ...);
    AK_S32 AK_BASE_PrintNoticeEx(AK_S32 s32ModuleId, const AK_CHAR *pcFmt, ...);
    AK_S32 AK_BASE_PrintNormalEx(AK_S32 s32ModuleId, const AK_CHAR *pcFmt, ...);
    AK_S32 AK_BASE_PrintInfoEx(AK_S32 s32ModuleId, const AK_CHAR *pcFmt, ...);
    AK_S32 AK_BASE_PrintDebugEx(AK_S32 s32ModuleId, const AK_CHAR *pcFmt, ...);
    AK_S32 AK_BASE_PrintSetLevel(AK_S32 s32ModuleId, AK_S32 s32Level);
    AK_S32 AK_BASE_PrintSetSyslogLevel(AK_S32 s32ModuleId, AK_S32 s32Level);
```

<br/>

### LOG_LEVEL_E

【Notes】

Log levels.

【Definition】

```c
typedef enum akLOG_LEVEL_E {
    LOG_LEVEL_RESERVED = 0,
    LOG_LEVEL_ERROR,
    LOG_LEVEL_WARNING,
    LOG_LEVEL_NOTICE,
    LOG_LEVEL_NORMAL,
    LOG_LEVEL_INFO,
    LOG_LEVEL_DEBUG,
}LOG_LEVEL_E;
```

【Members】

| **Member**       | **Description**     |
| ------------------ | ------------ |
| LOG_LEVEL_RESERVED | Reserved level |
| LOG_LEVEL_ERROR | Error level |
| LOG_LEVEL_WARNING | Warning level |
| LOG_LEVEL_NOTICE | Notice level |
| LOG_LEVEL_NORMAL | Normal level |
| LOG_LEVEL_INFO | Information level |
| LOG_LEVEL_DEBUG | Debug level |

【Related Functions】

```c
AK_S32 AK_BASE_PrintSetLevel(AK_S32 s32ModuleId, AK_S32 s32Level);
AK_S32 AK_BASE_PrintSetSyslogLevel(AK_S32 s32ModuleId, AK_S32 s32Level);
```

<br/>

## Getting Version Information

### **AK_BASE_PrintGetVersion**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets logging-module version information.

&emsp;&emsp;【Syntax】

```C
    const AK_CHAR* AK_BASE_PrintGetVersion(AK_VOID);
```

&emsp;&emsp;【Return Value】

| **Return value** | **Description**         |
| ---------------- | ---------------------- |
| Logging-module version information | Success. |
| NULL | Failure. |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_log.a or libplat_log.so

&emsp;&emsp;Header: ak_log.h

&emsp;&emsp;【Call Sequence】

&emsp;&emsp;This function may be called at any point.

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

<br/>

## Output by Log Level

### **AK_BASE_PrintError**

&emsp;&emsp;【Description】

&emsp;&emsp;Outputs an error message.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_PrintError(AK_S32 s32ModuleId, const AK_CHAR *pcFmt, ...);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**     | **Value range** | **Input/Output** |
| ------------------ | ------------------ | ------------------ | --------------------------------------- |
| s32ModuleId | Module ID of the caller | See enum module_id                | Input                                    |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0    | Success    |
| Other | See the error codes. |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------------- | -------------- |
| ERROR_TYPE_INVALID_ARG | invalid module_id input value |
| ERROR_TYPE_MALLOC_FAILED | Memory allocation failed |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_log.a or libplat_log.so

&emsp;&emsp;Header: ak_log.h

&emsp;&emsp;【Call Sequence】

&emsp;&emsp;This function may be called at any point.

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

<br/>

### **AK_BASE_PrintWarning**

&emsp;&emsp;【Description】

&emsp;&emsp;Outputs a warning message.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_PrintWarning(AK_S32 s32ModuleId, const AK_CHAR *pcFmt, ...);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**     | **Value range** | **Input/Output** |
| ------------------ | ------------------ | ------------------ | --------------------------------------- |
| s32ModuleId | Module ID of the caller | See enum module_id                | Input                                    |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0          | Success           |
| Other       | See the error codes. |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------------- | -------------- |
| ERROR_TYPE_INVALID_ARG | invalid module_id input value |
| ERROR_TYPE_MALLOC_FAILED | Memory allocation failed |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_log.a or libplat_log.so

&emsp;&emsp;Header: ak_log.h

&emsp;&emsp;【Call Sequence】

&emsp;&emsp;This function may be called at any point.

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

<br/>

### **AK_BASE_PrintNotice**

&emsp;&emsp;【Description】

&emsp;&emsp;Outputs a notice message.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_PrintNotice(AK_S32 s32ModuleId, const AK_CHAR *pcFmt, ...);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**     | **Value range** | **Input/Output** |
| ------------------ | ------------------ | ------------------ | --------------------------------------- |
| s32ModuleId | Module ID of the caller | See enum module_id                  | Input                                    |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0    | Success    |
| Other | See the error codes. |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------------- | -------------- |
| ERROR_TYPE_INVALID_ARG | invalid module_id input value |
| ERROR_TYPE_MALLOC_FAILED | Memory allocation failed |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_log.a or libplat_log.so

&emsp;&emsp;Header: ak_log.h

&emsp;&emsp;【Call Sequence】

&emsp;&emsp;This function may be called at any point.

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

<br/>

### **AK_BASE_PrintNormal**

&emsp;&emsp;【Description】

&emsp;&emsp;Outputs a normal log message.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_PrintNormal(AK_S32 s32ModuleId, const AK_CHAR *pcFmt, ...);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**     | **Value range** | **Input/Output** |
| ------------------ | ------------------ | ------------------ | --------------------------------------- |
| s32ModuleId | Module ID of the caller | See enum module_id                  | Input                                    |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0    | Success    |
| Other | See the error codes. |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------------- | -------------- |
| ERROR_TYPE_INVALID_ARG | invalid module_id input value |
| ERROR_TYPE_MALLOC_FAILED | Memory allocation failed |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_log.a or libplat_log.so

&emsp;&emsp;Header: ak_log.h

&emsp;&emsp;【Call Sequence】

&emsp;&emsp;This function may be called at any point.

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

<br/>

### **AK_BASE_PrintInfo**

&emsp;&emsp;【Description】

&emsp;&emsp;Outputs an info message.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_PrintInfo(AK_S32 s32ModuleId, const AK_CHAR *pcFmt, ...);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**     | **Value range** | **Input/Output** |
| ------------------ | ------------------ | ------------------ | --------------------------------------- |
| s32ModuleId | Module ID of the caller | See enum module_id                  | Input                                    |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0    | Success    |
| Other | See the error codes. |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------------- | -------------- |
| ERROR_TYPE_INVALID_ARG | invalid module_id input value |
| ERROR_TYPE_MALLOC_FAILED | Memory allocation failed |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_log.a or libplat_log.so

&emsp;&emsp;Header: ak_log.h

&emsp;&emsp;【Call Sequence】

&emsp;&emsp;This function may be called at any point.

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

<br/>

### **AK_BASE_PrintDebug**

&emsp;&emsp;【Description】

&emsp;&emsp;Outputs a debug message.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_PrintDebug(AK_S32 s32ModuleId, const AK_CHAR *pcFmt, ...);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**     | **Value range** | **Input/Output** |
| ------------------ | ------------------ | ------------------ | --------------------------------------- |
| s32ModuleId | Module ID of the caller | See enum module_id                  | Input                                    |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0    | Success    |
| Other | See the error codes. |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------------- | -------------- |
| ERROR_TYPE_INVALID_ARG | invalid module_id input value |
| ERROR_TYPE_MALLOC_FAILED | Memory allocation failed |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_log.a or libplat_log.so

&emsp;&emsp;Header: ak_log.h

&emsp;&emsp;【Call Sequence】

&emsp;&emsp;This function may be called at any point.

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

<br/>

### **AK_BASE_PrintErrorEx**

&emsp;&emsp;【Description】

&emsp;&emsp;Outputs an error message, including the function name and line number.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_PrintErrorEx(AK_S32 s32ModuleId, const AK_CHAR *pcFmt, ...);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**           | **Value range** | **Input/Output** |
| ------------ | ------------------ | ------------ | ------------- |
| s32ModuleId | Module ID of the caller | See enum module_id            | Input          |

&emsp;&emsp;【Return Value】

| **Return value**   | **Description**  |
| ------------ | --------- |
| 0    | Success    |
| Other | See the error codes. |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------- | -------- |
| ERROR_TYPE_INVALID_ARG | invalid module_id input value |
| ERROR_TYPE_MALLOC_FAILED | Memory allocation failed |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_log.a or libplat_log.so

&emsp;&emsp;Header: ak_log.h

&emsp;&emsp;【Call Sequence】

&emsp;&emsp;This function may be called at any point.

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

<br/>

### **AK_BASE_PrintWarningEx**

&emsp;&emsp;【Description】

&emsp;&emsp;Outputs a warning message, including the function name and line number.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_PrintWarningEx(AK_S32 s32ModuleId, const AK_CHAR *pcFmt, ...);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**           | **Value range** | **Input/Output** |
| ------------ | ------------------ | ------------ | ------------- |
| s32ModuleId | Module ID of the caller | See enum module_id            | Input          |

&emsp;&emsp;【Return Value】

| **Return value**   | **Description**  |
| ------------ | --------- |
| 0    | Success    |
| Other | See the error codes. |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------- | -------- |
| ERROR_TYPE_INVALID_ARG | invalid module_id input value |
| ERROR_TYPE_MALLOC_FAILED | Memory allocation failed |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_log.a or libplat_log.so

&emsp;&emsp;Header: ak_log.h

&emsp;&emsp;【Call Sequence】

&emsp;&emsp;This function may be called at any point.

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

<br/>

### **AK_BASE_PrintNoticeEx**

&emsp;&emsp;【Description】

&emsp;&emsp;Outputs a notice message, including the function name and line number.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_PrintNoticeEx(AK_S32 s32ModuleId, const AK_CHAR *pcFmt, ...);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**           | **Value range** | **Input/Output** |
| ------------ | ------------------ | ------------ | ------------- |
| s32ModuleId | Module ID of the caller | See enum module_id            | Input          |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**  |
| ---------- | --------- |
| 0    | Success    |
| Other | See the error codes. |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------- | -------- |
| ERROR_TYPE_INVALID_ARG | invalid module_id input value |
| ERROR_TYPE_MALLOC_FAILED | Memory allocation failed |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_log.a or libplat_log.so

&emsp;&emsp;Header: ak_log.h

&emsp;&emsp;【Call Sequence】

&emsp;&emsp;This function may be called at any point.

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

<br/>

### **AK_BASE_PrintNormalEx**

&emsp;&emsp;【Description】

&emsp;&emsp;Outputs a normal log message, including the function name and line number.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_PrintNormalEx(AK_S32 s32ModuleId, const AK_CHAR *pcFmt, ...);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**           | **Value range** | **Input/Output** |
| ------------ | ------------------ | ------------ | ------------- |
| s32ModuleId | Module ID of the caller | See enum module_id            | Input          |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**  |
| ---------- | --------- |
| 0    | Success    |
| Other | See the error codes. |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------- | -------- |
| ERROR_TYPE_INVALID_ARG | invalid module_id input value |
| ERROR_TYPE_MALLOC_FAILED | Memory allocation failed |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_log.a or libplat_log.so

&emsp;&emsp;Header: ak_log.h

&emsp;&emsp;【Call Sequence】

&emsp;&emsp;This function may be called at any point.

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

<br/>

### **AK_BASE_PrintInfoEx**

&emsp;&emsp;【Description】

&emsp;&emsp;Outputs an info message, including the function name and line number.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_PrintInfoEx(AK_S32 s32ModuleId, const AK_CHAR *pcFmt, ...);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**           | **Value range** | **Input/Output** |
| ------------ | ------------------ | ------------ | ------------- |
| s32ModuleId | Module ID of the caller | See enum module_id            | Input          |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**  |
| ---------- | --------- |
| 0    | Success    |
| Other | See the error codes. |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------- | -------- |
| ERROR_TYPE_INVALID_ARG | invalid module_id input value |
| ERROR_TYPE_MALLOC_FAILED | Memory allocation failed |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_log.a or libplat_log.so

&emsp;&emsp;Header: ak_log.h

&emsp;&emsp;【Call Sequence】

&emsp;&emsp;This function may be called at any point.

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

<br/>

### **AK_BASE_PrintDebugEx**

&emsp;&emsp;【Description】

&emsp;&emsp;Outputs a debug message, including the function name and line number.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_PrintDebugEx(AK_S32 s32ModuleId, const AK_CHAR *pcFmt, ...);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**           | **Value range** | **Input/Output** |
| ------------ | ------------------ | ------------ | ------------- |
| s32ModuleId | Module ID of the caller | See enum module_id            | Input          |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**  |
| ---------- | --------- |
| 0    | Success    |
| Other | See the error codes. |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------- | -------- |
| ERROR_TYPE_INVALID_ARG | invalid module_id input value |
| ERROR_TYPE_MALLOC_FAILED | Memory allocation failed |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_log.a or libplat_log.so

&emsp;&emsp;Header: ak_log.h

&emsp;&emsp;【Call Sequence】

&emsp;&emsp;This function may be called at any point.

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

<br/>

## Setting Log Levels

### **AK_BASE_PrintSetLevel**

&emsp;&emsp;【Description】

&emsp;&emsp;Sets the real-time physical-serial-port log level. Messages at or below the configured level are printed.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_PrintSetLevel(AK_S32 s32ModuleId, AK_S32 s32Level);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| s32ModuleId | Module ID to configure | See enum module_id | Input |
| s32Level | Log level | See enum LOG_LEVEL | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0    | Success    |
| Other | See the error codes. |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------------- | -------------- |
| ERROR_TYPE_INVALID_ARG | Invalid module_id or level input value |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_log.a or libplat_log.so

&emsp;&emsp;Header: ak_log.h

&emsp;&emsp;【Call Sequence】

&emsp;&emsp;This function may be called at any point.

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

<br/>

### **AK_BASE_PrintSetSyslogLevel**

&emsp;&emsp;【Description】

&emsp;&emsp;Sets the level for messages saved to the system log at /var/log/messages. Messages at or below the configured level are saved there.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_PrintSetSyslogLevel(AK_S32 s32ModuleId, AK_S32 s32Level);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**       | **Value range** | **Input/Output** |
| ------------ | -------------- | ------------ | ------------- |
| s32ModuleId | Module ID to configure | See enum module_id | Input |
| s32Level | Log level | See enum LOG_LEVEL | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**  |
| ---------- | --------- |
| 0    | Success    |
| Other | See the error codes. |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------- | -------- |
| ERROR_TYPE_INVALID_ARG | Invalid module_id or level input value |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_log.a or libplat_log.so

&emsp;&emsp;Header: ak_log.h

&emsp;&emsp;【Call Sequence】

&emsp;&emsp;This function may be called at any point.

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

<br/>

### /var/platform Description

The /var/platform directory exposes the current module configuration parameters and status. Its parameters are described below.

#### stat

| Parameter | Description |
| ------- | ----------- |
| Version | LOG library version |
