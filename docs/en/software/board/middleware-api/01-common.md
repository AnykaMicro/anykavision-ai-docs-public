# Common Services

## Overview

&emsp;&emsp;The common-services module implements basic platform functions, such as obtaining the current system time and converting time formats.

&emsp;&emsp;These functions are independent of one another and are managed together by the common-services module.

<br/>

## API Reference

&emsp;&emsp;This module provides the APIs listed below:

| **Function**             | **Description**                           |
| ------------------------ | ---------------------------------- |
| AK_BASE_CommonGetVersion | Gets common-module version information. |
| AK_BASE_SleepMs | Sleeps for the specified number of milliseconds. |
| AK_BASE_GetOstime | Gets the system time. |
| AK_BASE_GetOsTimeStamp | Gets the system timestamp. |
| AK_BASE_GetLocalDate | Gets the current date. |
| AK_BASE_SetLocalDate | Sets the current date. |
| AK_BASE_DiffMsTime | Gets the time difference. |
| AK_BASE_SecondsToString | Converts a timestamp to a string. |
| AK_BASE_SecondsToDate | Converts a timestamp to a date. |
| AK_BASE_DateToSeconds | Converts time information to a timestamp. |
| AK_BASE_DateToString | Converts time information to a string. |
| AK_BASE_StringToDate | Converts time information in string format to a structure. |
| AK_BASE_SdkInit | Initializes the Anyka SDK. |
| AK_BASE_SdkExit | Exits the Anyka SDK. |

<br/>

## Getting Version Information

### **AK_BASE_CommonGetVersion**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets common-module version information.

&emsp;&emsp;【Syntax】

```C
    const AK_CHAR* AK_BASE_CommonGetVersion(AK_VOID);
```

&emsp;&emsp;【Return Value】

| **Return value**     | **Description**                 |
| -------------- | ------------------------ |
| const AK_CHAR* | Common-module version information. |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_common.a

&emsp;&emsp;Header: ak_common.h

<br/>

## Time Operations

### **AK_BASE_SleepMs**

&emsp;&emsp;【Description】

&emsp;&emsp;Sleeps for the specified number of milliseconds.

&emsp;&emsp;【Syntax】

```C
    AK_VOID AK_BASE_SleepMs(const AK_S32 s32Ms);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------ | -------- | ------------ | ------------- |
| s32Ms | Number of milliseconds | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------- | -------- |
| AK_VOID    | -        |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------- | -------- |
| -          | -        |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_common.a

&emsp;&emsp;Header: ak_common.h

<br/>

### **AK_BASE_GetOstime**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the system time.

&emsp;&emsp;【Syntax】

```C
    AK_VOID AK_BASE_GetOstime(TIME_VAL_S *pstTv);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**       | **Value range** | **Input/Output** |
| ------------ | -------------- | ------------ | ------------- |
| pstTv | Output system time | - | Output |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------- | -------- |
| AK_VOID    | -        |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------- | -------- |
| -          | -        |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_common.a

&emsp;&emsp;Header: ak_common.h

【Related Structure Definition】

```C
typedef struct akTIME_VAL_S {
    AK_U64 u64Sec;     /* seconds */
    AK_U64 u64Usec;    /* microseconds */
}TIME_VAL_S;
```

【Members】

| **Member** | **Description** |
| ------------ | -------- |
| u64Sec | Seconds |
| u64Usec | Microseconds |

<br/>

### **AK_BASE_GetOsTimeStamp**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the system timestamp.

&emsp;&emsp;【Syntax】

```C
    time_t AK_BASE_GetOsTimeStamp(AK_VOID);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------ | -------- | ------------ | ------------- |
| AK_VOID      | -        | -            | -             |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**                                      |
| ---------- | --------------------------------------------- |
| time_t | Timestamp, equivalent to the value returned by Linux `time_t time(NULL);` |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------- | -------- |
| -          | -        |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_common.a

&emsp;&emsp;Header: ak_common.h

<br/>

### **AK_BASE_GetLocalDate**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the current date.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_GetLocalDate(DATE_S *pstDate);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**           | **Value range** | **Input/Output** |
| ------------ | ------------------ | ------------ | ------------- |
| pstDate | Output current local date | - | Output |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------- | -------- |
| 0          | Success     |
| Nonzero | Failure |

&emsp;&emsp;【Error Code List】

| **Error code**              | **Description** |
| ----------------------- | -------- |
| ERROR_TYPE_POINTER_NULL | Null parameter |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_common.a

&emsp;&emsp;Header: ak_common.h

<br/>

### **AK_BASE_SetLocalDate**

&emsp;&emsp;【Description】

&emsp;&emsp;Sets the current date.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_SetLocalDate(const DATE_S *pstDate);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------ | -------- | ------------ | ------------- |
| pstDate | Current date | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------- | -------- |
| 0          | Success     |
| Nonzero | Failure |

&emsp;&emsp;【Error Code List】

| **Error code**              | **Description** |
| ----------------------- | -------- |
| ERROR_TYPE_POINTER_NULL | Null parameter |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_common.a

&emsp;&emsp;Header: ak_common.h

<br/>

### **AK_BASE_DiffMsTime**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the time difference.

&emsp;&emsp;【Syntax】

```C
    long AK_BASE_DiffMsTime(const TIME_VAL_S *pstCurTime,
                    const TIME_VAL_S *pstPreTime);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**   | **Value range** | **Input/Output** |
| ------------ | ---------- | ------------ | ------------- |
| pstCurTime | Time to compare | - | Input |
| pstPreTime | Reference time | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**           |
| ---------- | ------------------ |
| long | Time difference in ms. |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------- | -------- |
| -          | -        |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_common.a

&emsp;&emsp;Header: ak_common.h

<br/>

### **AK_BASE_SecondsToString**

&emsp;&emsp;【Description】

&emsp;&emsp;Converts a timestamp to a string.

&emsp;&emsp;【Syntax】

```C
    AK_CHAR* AK_BASE_SecondsToString(time_t secs);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range**             | **Input/Output** |
| ------------ | -------- | ------------------------ | ------------- |
| secs | Timestamp | [-2147483648,2147483647] | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**                                                     |
| ---------- | ------------------------------------------------------------ |
| AK_CHAR* | Pointer to the output string in `yyyy-MM-dd HH:mm:ss` format.<br/>For example: `2016-04-06 10:06:06`. |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------- | -------- |
| -          | -        |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_common.a

&emsp;&emsp;Header: ak_common.h

<br/>

### **AK_BASE_SecondsToDate**

&emsp;&emsp;【Description】

&emsp;&emsp;Converts a timestamp to a date.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_SecondsToDate(time_t seconds, DATE_S *pstDate);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range**             | **Input/Output** |
| ------------ | -------- | ------------------------ | ------------- |
| seconds | Timestamp | [-2147483648,2147483647] | Input |
| pstDate | Time information | - | Output |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------- | -------- |
| 0          | Success     |
| Nonzero | Failure |

&emsp;&emsp;【Error Code List】

| **Error code**             | **Description** |
| ---------------------- | -------- |
| ERROR_TYPE_INVALID_ARG | Invalid parameter |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_common.a

&emsp;&emsp;Header: ak_common.h

<br/>

### **AK_BASE_DateToSeconds**

&emsp;&emsp;【Description】

&emsp;&emsp;Converts time information to a timestamp.

&emsp;&emsp;【Syntax】

```C
    time_t AK_BASE_DateToSeconds(const DATE_S *pstDate);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------ | -------- | ------------ | ------------- |
| pstDate | Time information | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**      |
| ---------- | ------------- |
| time_t | Timestamp in seconds. |
| -1         | Failure          |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------- | -------- |
| -          | -        |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_common.a

&emsp;&emsp;Header: ak_common.h

<br/>

### **AK_BASE_DateToString**

&emsp;&emsp;【Description】

&emsp;&emsp;Converts time information to a string.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_DateToString(const DATE_S *pstDate, AK_CHAR *pcStr);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**                          | **Value range** | **Input/Output** |
| ------------ | --------------------------------- | ------------ | ------------- |
| pstDate | Time information | - | Input |
| pcStr | Time string in `yyyyMMdd-HHmmss` format | - | Output |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------- | -------- |
| 0          | Success     |
| Nonzero | Failure |

&emsp;&emsp;【Error Code List】

| **Error code**              | **Description** |
| ----------------------- | -------- |
| ERROR_TYPE_POINTER_NULL | Null parameter |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_common.a

&emsp;&emsp;Header: ak_common.h

<br/>

### **AK_BASE_StringToDate**

&emsp;&emsp;【Description】

&emsp;&emsp;Converts time information in string format to a structure.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_StringToDate(const AK_CHAR *pcTimeStr, DATE_S *pstDate);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**                                    | **Value range** | **Input/Output** |
| ------------ | ------------------------------------------- | ------------ | ------------- |
| pcTimeStr | Time information as a string in `yyyyMMdd-HHmmss` format | - | Input |
| pstDate | Time information in structure format | - | Output |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------- | -------- |
| 0          | Success     |
| Nonzero | Failure |

&emsp;&emsp;【Error Code List】

| **Error code**              | **Description** |
| ----------------------- | -------- |
| ERROR_TYPE_POINTER_NULL | Null parameter |
| ERROR_TYPE_INVALID_ARG | Invalid parameter |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_common.a

&emsp;&emsp;Header: ak_common.h

<br/>

## SDK Initialization and Exit

### **AK_BASE_SdkInit**

&emsp;&emsp;【Description】

&emsp;&emsp;Initializes the Anyka SDK.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_SdkInit(SDK_RUN_CONFIG_S *pstConfig);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**          | **Value range** | **Input/Output** |
| ------------ | ----------------- | ------------ | ------------- |
| pstConfig | SDK initialization configuration | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------- | -------- |
| 0          | Success     |
| Nonzero | Failure |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------- | -------- |
| ERROR_TYPE_INVALID_ARG          | Invalid parameter        |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_common.a

&emsp;&emsp;Header: ak_common.h

> **Note:** This function must be called before using the Anyka SDK.

&emsp;&emsp;【Related Structure Definition】

```C
typedef struct akSDK_RUN_CONFIG_S {
    AK_S32 s32MemTraceFlag;
    AK_S32 s32DmaMemTraceFlag;
    // isp tool server flag, 0 : disable, 1 : enable
    AK_S32 s32IspToolServerFlag;
} SDK_RUN_CONFIG_S;
```

【Members】

| **Member**         | **Description**                                                     |
| -------------------- | ------------------------------------------------------------ |
| s32MemTraceFlag | Enables ordinary-memory tracing. Enable this flag to support ak_mem_get_used_total. |
| s32DmaMemTraceFlag | Enables DMA-memory tracing. Enable this flag to support ak_mem_dma_get_used. |
| s32IspToolServerFlag | Enables the ISP tuning tool service. `0`: disabled; `1`: enabled on default port 8765; values other than 0 and 1 in the range (1024, 65536) enable the service on the specified port. Enabling this flag is equivalent to calling AK_EXT_ITS_Start. |

> **Security note:** The ISP tool service is for debugging only. Keep `s32IspToolServerFlag` at `0` outside debugging environments. During debugging, enable it only on an isolated development network and restrict connecting devices with host and network firewalls. Changing the port number is not a substitute for access control.

### **AK_BASE_SdkExit**

&emsp;&emsp;【Description】

&emsp;&emsp;Exits the Anyka SDK.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_SdkExit(AK_VOID);
```

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------- | -------- |
| 0          | Success     |

&emsp;&emsp;【Error Code List】

| **Error code**          | **Description**      |
| ------------------- | ------------- |
| ERROR_TYPE_NOT_INIT | SDK not initialized |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_common.a

&emsp;&emsp;Header: ak_common.h

> **Note:** Use this function together with AK_BASE_SdkInit.
<br/>

### /var/platform Description

The /var/platform directory exposes the current module configuration parameters and status. Its parameters are described below.

#### stat

| Parameter | Description |
| ------- | -------------- |
| Version | COMMON library version |

<br/>

## Error Codes

| Error code | Macro | Description |
| -------- | ------------------------------- | ---------------- |
| 0 | ERROR_TYPE_NO_ERROR | No error |
| 0x100 | ERROR_TYPE_POINTER_NULL | Null pointer |
| 0x101    | ERROR_TYPE_INVALID_ARG          | Invalid parameter         |
| 0x102 | ERROR_TYPE_MALLOC_FAILED | malloc failed |
| 0x103 | ERROR_TYPE_PMEM_MALLOC_FAILED | pmem malloc failed |
| 0x104 | ERROR_TYPE_FUNC_NOT_SUPPORT | Function not supported |
| 0x105 | ERROR_TYPE_NOT_INIT | Not initialized |
| 0x106 | ERROR_TYPE_CALL_ORDER_WRONG | Incorrect call order |
| 0x107 | ERROR_TYPE_DEV_OPEN_FAILED | Failed to open device |
| 0x108 | ERROR_TYPE_DEV_INIT_FAILED | Failed to initialize device |
| 0x109 | ERROR_TYPE_DEV_CTRL_FAILED | Device operation failed |
| 0x10a | ERROR_TYPE_DEV_READ_FAILED | Failed to read device |
| 0x10b | ERROR_TYPE_DEV_WRITE_FAILED | Failed to write device |
| 0x10c | ERROR_TYPE_DEV_CLOSE_FAILED | Failed to close device |
| 0x10d | ERROR_TYPE_FILE_OPEN_FAILED | Failed to open file |
| 0x10e | ERROR_TYPE_FCNTL_FAILED | File operation failed |
| 0x10f | ERROR_TYPE_FILE_READ_FAILED | Failed to read file |
| 0x110 | ERROR_TYPE_FILE_WRITE_FAILED | Failed to write file |
| 0x111 | ERROR_TYPE_IOCTL_FAILED | IOCTL failed |
| 0x112 | ERROR_TYPE_CLOSE_FAILED | Close failed |
| 0x113 | ERROR_TYPE_GET_V4L2_PTR_FAILED | Failed to get V4L2 pointer |
| 0x114 | ERROR_TYPE_INVALID_USER | Invalid user |
| 0x115 | ERROR_TYPE_THREAD_CREATE_FAILED | Failed to create thread |
| 0x116 | ERROR_TYPE_POPEN_FAILED | POPEN failed |
| 0x117 | ERROR_TYPE_MEDIA_LIB_FAILED | Media library failed |
| 0x118 | ERROR_TYPE_NO_DATA | No data |
| 0x119 | ERROR_TYPE_EBUSY | Device busy |
| 0x11a | ERROR_TYPE_NO_ENOUGH_RESOURCE | Insufficient resources |
| 0x11b | ERROR_TYPE_NO_LEFT_SPACE | Insufficient space |

<br/>
