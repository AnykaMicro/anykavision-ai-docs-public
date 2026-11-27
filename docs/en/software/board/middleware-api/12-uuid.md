# UUID

## Overview

&emsp;&emsp;The chip unique-ID acquisition module (UUID module).

<br/>

## API Reference

&emsp;&emsp;This module provides the following APIs.

| **Function**                  | **Description**                 |
| ----------------------------- | ------------------------------- |
| AK_BASE_UuidGetVersion        | Gets the UUID version           |
| AK_BASE_UuidOpen              | Opens the UUID device           |
| AK_BASE_UuidClose             | Closes the UUID device          |
| AK_BASE_UuidGetGlobalId       | Gets data from the global_ID area |
| AK_BASE_UuidGetGlobalIdLength | Gets the global_ID length, in bytes |
<br/>

## Get Version Information

###  **AK_BASE_UuidGetVersion**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the version number of the UUID library.

&emsp;&emsp;【Syntax】

```C
    const AK_CHAR* AK_BASE_UuidGetVersion(AK_VOID);
```

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| -------------- | --------- |
| UUID module version number | Success |
| NULL           | Failure   |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libpalt_uuid.a, libplat_osal.a

&emsp;&emsp;Header: ak_uuid.h

<br/>

## Open/Close the Module

###  **AK_BASE_UuidOpen**

&emsp;&emsp;【Description】

&emsp;&emsp;Opens the UUID module.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_UuidOpen(AK_VOID);
```

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ----------- | ------------ |
| 0           | Success      |
| Other       | See the error codes |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_uuid.a, libplat_osal.a

&emsp;&emsp;Header: ak_uuid.h

> **Note:** This API permits only one `open` operation. Repeated calls return an error.

<br/>

### **AK_BASE_UuidClose**

&emsp;&emsp;【Description】

&emsp;&emsp;Closes the UUID module.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_UuidClose(AK_VOID);
```

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ----------- | ------------ |
| 0           | Success      |
| Other       | See the error codes |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_uuid.a, libplat_osal.a

&emsp;&emsp;Header: ak_uuid.h

> **Note:** This API permits only one `close` operation. Repeated calls return an error.

<br/>

## global_ID Area Operations

###  **AK_BASE_UuidGetGlobalId**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the data in the global ID area.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_UuidGetGlobalId(AK_U8** ppu8Buf);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**                 | **Value range** | **Input/Output** |
| ------------- | ------------------------------- | ------------- | -------------- |
| ppu8Buf       | Address of the pointer used to return global ID data | Double pointer | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ----------- | ------------ |
| 0           | Success      |
| Other       | See the error codes |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_uuid.a, libplat_osal.a

&emsp;&emsp;Header: ak_uuid.h

> **Note:** Call this API after `AK_BASE_UuidOpen`. Read the data through the returned double pointer before calling `AK_BASE_UuidClose`.

<br/>

### **AK_BASE_UuidGetGlobalIdLength**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the length of the global ID area, in bytes.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_UuidGetGlobalIdLength(AK_S32* ps32Length);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**                   | **Value range** | **Input/Output** |
| ------------- | --------------------------------- | ------------- | -------------- |
| ps32Length    | Receives the length of the global ID area, in bytes | Non-negative integer | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ----------- | ------------ |
| 0           | Success      |
| Other       | See the error codes |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_uuid.a, libplat_osal.a

&emsp;&emsp;Header: ak_uuid.h

> **Note:** Call this API after `AK_BASE_UuidOpen`.

<br/>

&emsp;&emsp;Example code:

```c
    #include "ak_uuid.h"
    #include <stdio.h>
    ....

    AK_BASE_PrintNormal(MODULE_ID_APP, "** uuid demo version: %s **\n",       AK_BASE_UuidGetVersion());
    int ret =-1;
    int length = -1;
    ret = AK_BASE_UuidOpen();					//if use uuid ,first must open uuid
    unsigned char* global_ptr;
    ret = AK_BASE_UuidGetGlobalId(&global_ptr);
    ret = AK_BASE_UuidGetGlobalIdLength(&length);
    for(int i =0;i< length;i++){
	  AK_BASE_PrintNoticeEx(MODULE_ID_APP," global_id=%x\n",global_ptr[i]);
    }
    AK_BASE_UuidClose();	  //close uuid ,will free the mempry which malloced in inner
```

<br/>

## Error Codes

| Error code | Macro                         | Description               |
| ---------- | ----------------------------- | ------------------------- |
| 0x20000000 | ERROR_UUID_INVALID_ARG        | Invalid argument          |
| 0x20000001 | ERROR_UUID_GLOBAL_ID_ZERO     | The global area is empty and cannot be read |
| 0x20000002 | ERROR_UUID_UNWRITABLE         | The custom area is not empty and cannot be written |
| 0x20000003 | ERROR_UUID_OTHERS             | Other errors, such as a data comparison error |
| 0x20000004 | ERROR_UUID_DEV_NOT_OPENED     | The UUID device is not open |
| 0x20000005 | ERROR_UUID_DEV_NOT_EXISTED    | The UUID device does not exist |
| 0x20000006 | ERROR_UUID_DEV_ALREADY_OPENED | The UUID device is already open |
| 0x20000007 | ERROR_UUID_UNKNOW             | Unknown error             |

<br/>
