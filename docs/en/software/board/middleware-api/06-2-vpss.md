# Video Processing Subsystem

## Overview

&emsp;&emsp;The video processing subsystem (VPSS) provides two main sets of functions:

&emsp;&emsp;1. Binding to VI to provide basic ISP operations (the flow section).

&emsp;&emsp;2. Providing image-effect processing functions (the effects section).

This section describes the data structures and interfaces for the flow section.

<br/>

## API Reference

&emsp;&emsp;This module provides the APIs listed below:

| **Library interface** | **Description** |
| --------------------------- | ---------------------- |
| VPSS_CHN_MODE_E | VPSS video-frame output mode |
| VPSS_WORK_MODE_E | VPSS operating mode |
| VPSS_GRP_ATTR_S | VPSS GROUP attributes |
| VPSS_CHN_ATTR_S | VPSS channel attributes |
| VPSS_FRAME_INFO_S | VPSS video-frame structure |
| AK_MPI_VPSS_GetVersion | Gets the VPSS library version. |
| AK_MPI_VPSS_GetConfVersion | Gets the ISPCONF file version. |
| AK_MPI_VPSS_CreateGrp | Creates a VPSS Group. |
| AK_MPI_VPSS_DestroyGrp | Destroys a VPSS Group. |
| AK_MPI_VPSS_StartGrp | Starts a VPSS Group. |
| AK_MPI_VPSS_StopGrp | Stops a VPSS Group. |
| AK_MPI_VPSS_SetGrpAttr | Sets VPSS Group attributes. |
| AK_MPI_VPSS_GetGrpAttr | Gets VPSS Group attributes. |
| AK_MPI_VPSS_SetChnAttr | Sets VPSS channel attributes. |
| AK_MPI_VPSS_GetChnAttr | Gets VPSS channel attributes. |
| AK_MPI_VPSS_EnableChn | Enables a VPSS channel. |
| AK_MPI_VPSS_DisableChn | Disables a VPSS channel. |
| AK_MPI_VPSS_BindChn | Binds the input VI channel. |
| AK_MPI_VPSS_GetFrame | Gets one processed image from a VPSS channel. |
| AK_MPI_VPSS_ReleaseFrame | Releases one VPSS-channel image. |
| AK_MPI_VPSS_GetGrpFrame | Gets one original RAW image from a VPSS GROUP. |
| AK_MPI_VPSS_ReleaseGrpFrame | Releases one VPSS GROUP RAW image. |

<br/>

## Data Structures

### **VPSS_CHN_MODE_E**

&emsp;&emsp;【Notes】

&emsp;&emsp;Video-frame output modes.

&emsp;&emsp;【Definition】

```c
typedef enum akVPSS_CHN_MODE_E
{
     VPSS_CHN_FRAME_MODE,  //frame mode is normal mode.
    VPSS_CHN_SLICE_MODE,  //slice mode for saving dma memory, just user in venc kernel-kernel mode.
    VPSS_CHN_MODE_TOTAL
}VPSS_CHN_MODE_E;
```

&emsp;&emsp;【Members】

| **Member**            | **Description**     |
| ------------------- | ---------- |
| VPSS_CHN_FRAME_MODE | FRAME-mode output. |
| VPSS_CHN_SLICE_MODE | SLICE-mode output. |
| VPSS_CHN_MODE_TOTAL | Total number of modes. |

&emsp;&emsp;【Related Functions】

```c
    AK_S32 AK_MPI_VPSS_SetChnAttr(AK_S32 s32VpssGrp, AK_S32 s32VpssChn, const VPSS_CHN_ATTR_S *pstVpssChnAttr);
    AK_S32 AK_MPI_VPSS_GetChnAttr(AK_S32 s32VpssGrp, AK_S32 s32ChnId, VPSS_CHN_ATTR_S *pstVpssChnAttr);
```

<br/>

### **VPSS_WORK_MODE_E**

&emsp;&emsp;【Notes】

&emsp;&emsp;VPSS operating modes.

&emsp;&emsp;【Definition】

```c
typedef enum akVPSS_WORK_MODE_E
{
    VPSS_WORK_USER,                    //Receive memory input, i.e., user space data input through AK_MPI_VPSS_SendFrame
    VPSS_WORK_AUTO,                    //Normal mode, data input from sensor.
    VPSS_WORK_TOTAL
}VPSS_WORK_MODE_E;
```

&emsp;&emsp;【Members】

| **Member**        | **Description**        |
| --------------- | ------------- |
| VPSS_WORK_USER | USER mode supports memory input. |
| VPSS_WORK_AUTO | Auto mode is the bound-stream mode. |
| VPSS_WORK_TOTAL | Total number of modes. |

&emsp;&emsp;【Related Functions】

```c
    AK_S32 AK_MPI_VPSS_CreateGrp(AK_S32 s32VpssGrp, const VPSS_GRP_ATTR_S *pstVpssGrpAttr);
```

<br/>

### **VPSS_GRP_ATTR_S**

&emsp;&emsp;【Notes】

&emsp;&emsp;VPSS GROUP attributes.

&emsp;&emsp;【Definition】

```c
typedef struct akVPSS_GRP_ATTR_S
{
    AK_U32                 u32Width;
    AK_U32                 u32Height;
    AK_U8                 pu8IspCfgPath[MAX_CFG_PATH_LEN];
    AK_S32               s32AttachSensorId;
    PIXEL_FORMAT_E          enInputPixFmt;
    VPSS_WORK_MODE_E     enWorkMode;
    ISP_DAY_NIGHT_MODE_E enLoadMode;
    AK_BOOL                 bEnGrpBypass;
    AK_BOOL                 bMirror;
    AK_BOOL                 bFlip;
}VPSS_GRP_ATTR_S;
```

&emsp;&emsp;【Members】

| **Member**          | **Description**                                                        |
| ----------------- | ------------------------------------------------------------- |
| u32Width | Input width |
| u32Height | Input height |
| pu8IspCfgPath | ISP configuration-file path |
| s32AttachSensorId | CIS ID, obtained through AK_MPI_VI_GetSensorId. |
| enInputPixFmt | Input-data pixel format |
| enWorkMode | VPSS GROUP operating mode: USER or Auto. |
| enLoadMode | ispconf subfile to load during initialization |
| bEnGrpBypass | Enables bypassing VPSS ISP processing. When enabled, RAW data can be obtained through AK_MPI_VPSS_GetGrpFrame. |
| bMirror | Whether to mirror horizontally |
| bFlip | Whether to flip vertically |

&emsp;&emsp;【Related Functions】

```c
    AK_S32 AK_MPI_VPSS_CreateGrp(AK_S32 s32VpssGrp, const VPSS_GRP_ATTR_S *pstVpssGrpAttr);
```

<br/>

### **VPSS_CHN_ATTR_S**

&emsp;&emsp;【Notes】

&emsp;&emsp;VPSS channel attributes. SLICE mode applies only to AUTO mode.

&emsp;&emsp;【Definition】

```c
typedef struct akVPSS_CHN_ATTR_S
{
    AK_U32                u32Width;
    AK_U32                u32Height;
    AK_U32                u32MaxBufSize;
    CROP_INFO_S            stCropInfo;
    PIXEL_FORMAT_E         enOutputPixFmt;
    VPSS_CHN_MODE_E        enChnMode;
    AK_U32                u32FrameDepth;
    AK_S32                s32Fps;
}VPSS_CHN_ATTR_S;
```

&emsp;&emsp;【Members】

| **Member**       | **Description**                   |
| -------------- | ------------------------ |
| u32Width | Output width |
| u32Height | Output height |
| u32MaxBufSize | Buffer size for the maximum resolution |
| stCropInfo | Channel crop information |
| enOutputPixFmt | Output pixel format |
| enChnMode | Channel output mode: FRAME or SLICE. |
| u32FrameDepth | Number of internally buffered frames |
| s32Fps | Channel frame-rate control |

&emsp;&emsp;【Related Functions】

```c
    AK_S32 AK_MPI_VPSS_SetChnAttr(AK_S32 s32VpssGrp, AK_S32 s32VpssChn, const VPSS_CHN_ATTR_S *pstVpssChnAttr);
    AK_S32 AK_MPI_VPSS_GetChnAttr(AK_S32 s32VpssGrp, AK_S32 s32ChnId, VPSS_CHN_ATTR_S *pstVpssChnAttr);
```

<br/>

### **VPSS_FRAME_INFO_S**

&emsp;&emsp;【Notes】

&emsp;&emsp;VPSS video-frame structure.

【Definition】

```c
typedef struct akVPSS_FRAME_INFO_S
{
    FRAME_S                stFrame;
    AK_U64                u64PhyAddr;
    PIXEL_FORMAT_E         enOutputPixFmt;
    AK_VOID                *pvMdInfo;
}VPSS_FRAME_INFO_S;
```

&emsp;&emsp;【Members】

| **Member**       | **Description**   |
| -------------- | -------- |
| stFrame | Frame-information structure |
| u64PhyAddr | Physical address where the frame is stored |
| enOutputPixFmt | Output pixel format |
| pvMdInfo | Motion-detection data |

&emsp;&emsp;【Related Functions】

```c
    AK_S32 AK_MPI_VPSS_GetFrame(AK_S32 s32VpssGrp, AK_S32 s32ChnId, VPSS_FRAME_INFO_S *pstFrameInfo, AK_S32 s32MilliSec);
```

<br/>

### VPSS_STITCH_MODE_E

&emsp;&emsp;【Notes】

&emsp;&emsp;Stitching-mode enumeration.

​        【Definition】

```c
typedef enum akVPSS_STITCH_MODE_E
{
    VPSS_STITCH_VERTICAL_MODE,        //stitch dual sensor can use slice mode.
    VPSS_STITCH_HORIZONTAL_MODE,    //stitch dual sensor can not use slice mode.
    VPSS_STITCH_MODE_TOTAL
}VPSS_STITCH_MODE_E;
```

&emsp;&emsp;【Members】

| **Member**                    | **Description** |
| --------------------------- | ------ |
| VPSS_STITCH_VERTICAL_MODE | Vertical stitching |
| VPSS_STITCH_HORIZONTAL_MODE | Horizontal stitching |
| VPSS_STITCH_MODE_TOTAL | Total number of stitching modes |

&emsp;&emsp;【Related Functions】

```c
    AK_S32 AK_MPI_VPSS_SetStitchChn(AK_S32 s32VpssGrp, AK_S32 s32ChnId, const VPSS_STITCH_ATTR_S *pstVpssStitchAttr);
```

<br/>

### VPSS_STITCH_CHN_S

&emsp;&emsp;【Notes】

&emsp;&emsp;Channels to stitch.

​        【Definition】

```c
typedef struct akVPSS_STITCH_CHN_S
{
    AK_S32                    s32VpssGrp;
    AK_S32                    s32VpssChn;
}VPSS_STITCH_CHN_S;
```

&emsp;&emsp;【Members】

| **Member**   | **Description**                                                    |
| ---------- | --------------------------------------------------------- |
| s32VpssGrp | VPSS GROUP ID [0,4]. In multi-camera mode, different devices use different group IDs.            |
| s32VpssChn | VPSS channel ID [0, 2]. By default, ChnId is 0 for the primary channel, 1 for the secondary channel, and 2 for the third channel. |

&emsp;&emsp;【Related Functions】

```c
    AK_S32 AK_MPI_VPSS_SetStitchChn(AK_S32 s32VpssGrp, AK_S32 s32ChnId, const VPSS_STITCH_ATTR_S *pstVpssStitchAttr);
```

<br/>

### VPSS_STITCH_ATTR_S

&emsp;&emsp;【Notes】

&emsp;&emsp;Stitched-channel attributes.

​        【Definition】

```c
typedef struct akVPSS_STITCH_ATTR_S
{
    VPSS_STITCH_MODE_E    enStitchmode;
    AK_U32                    u32StitchChnNum;
    VPSS_STITCH_CHN_S        astStitchChn[MAX_STITCH_CHN_NUM];
}VPSS_STITCH_ATTR_S;
```

&emsp;&emsp;【Members】

| **Member**        | **Description**                                                        |
| --------------- | ------------------------------------------------------------- |
| enStitchmode | Stitching mode |
| u32StitchChnNum | Number of channels to stitch. For example, u32StitchChnNum = 1 for two-camera stitching and u32StitchChnNum = 2 for three-camera stitching. |
| astStitchChn | Stitched-channel attributes |

&emsp;&emsp;【Related Functions】

```c
    AK_S32 AK_MPI_VPSS_SetStitchChn(AK_S32 s32VpssGrp, AK_S32 s32ChnId, const VPSS_STITCH_ATTR_S *pstVpssStitchAttr);
```

<br/>

## Getting Version Information

### **AK_MPI_VPSS_GetVersion**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the VPSS library version.

&emsp;&emsp;【Syntax】

```c
    const AK_CHAR *AK_MPI_VPSS_GetVersion(void);
```

&emsp;&emsp;【Return Value】

| **Return value**   | **Description** |
| --------- | ------ |
| VPSS module version | Success |
| NULL      | Failure     |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_vpss.a

&emsp;&emsp;Header: ak_vpss.h

<br/>

### **AK_MPI_VPSS_GetConfVersion**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the ISPCONF file version.

&emsp;&emsp;【Syntax】

```c
    const AK_CHAR *AK_MPI_VPSS_GetConfVersion(AK_S32 s32VpssGrp);
```

&emsp;&emsp;【Parameters】

| **Parameter**   | **Description**                                         | **Input/Output** |
| ---------- | ---------------------------------------------- | --------- |
| s32VpssGrp | VPSS group ID [0-4]. In multi-camera mode, different devices use different group IDs. | Input        |

&emsp;&emsp;【Return Value】

| **Return value**       | **Description** |
| ------------- | ------ |
| ISPCONF file version | Success |
| NULL          | Failure     |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_vpss.a

&emsp;&emsp;Header: ak_vpss.h

<br/>

### **AK_MPI_VPSS_CreateGrp**

&emsp;&emsp;【Description】

&emsp;&emsp;Creates a VPSS Group. Multiple channels internally time-multiplex the ISP hardware.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_VPSS_CreateGrp(AK_S32 s32VpssGrp, const VPSS_GRP_ATTR_S *pstVpssGrpAttr);
```

&emsp;&emsp;【Parameters】

| **Parameter**       | **Description**                                         | **Input/Output** |
| -------------- | ---------------------------------------------- | --------- |
| s32VpssGrp     | VPSS group ID [0-4]. In multi-camera mode, different devices use different group IDs. | Input        |
| pstVpssGrpAttr | VPSS group attributes                                   | Input        |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0       | Success         |
| Nonzero      | Failure; the value is an error code. |

&emsp;&emsp;【Error Code List】

| **Error code**                     | **Description**        |
| --------------------------- | ------------- |
| ERROR_TYPE_INVALID_ARG      | Invalid parameter          |
| ERROR_VPSS_GRP_CREATED_YET | Group already created |
| ERROR_VPSS_GRP_CREATE_FAIL | Group creation failed |
| ERROR_VPSS_ISP_DEV_OPEN | Failed to open ISP device |
| ERROR_VPSS_GET_PAD_ID | Failed to get PAD ID |
| ERROR_VPSS_GRPID_NO_FOUND   | Group ID not found   |
| ERROR_TYPE_MALLOC_FAILED | Memory allocation failed |
| ERROR_TYPE_FILE_READ_FAILED | Failed to read ISP conf file |
| ERROR_TYPE_DEV_INIT_FAILED | Failed to initialize ISP device |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_vpss.a

&emsp;&emsp;Header: ak_vpss.h

<br/>

### **AK_MPI_VPSS_DestroyGrp**

&emsp;&emsp;【Description】

&emsp;&emsp;Destroys a VPSS GROUP.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_VPSS_DestroyGrp(AK_S32 s32VpssGrp);
```

&emsp;&emsp;【Parameters】

| **Parameter**   | **Description**                                         | **Input/Output** |
| ---------- | ---------------------------------------------- | --------- |
| s32VpssGrp | VPSS GROUP ID [0,4]. In multi-camera mode, different devices use different group IDs. | Input        |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0       | Success.        |
| Nonzero      | Failure; the value is an error code. |

&emsp;&emsp;【Error Code List】

| **Error code**                   | **Description**      |
| ------------------------- | ----------- |
| ERROR_VPSS_NO_WORK        | VPSS not initialized    |
| ERROR_TYPE_INVALID_ARG    | Invalid parameter        |
| ERROR_VPSS_GRPID_NO_FOUND | Group ID not found |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_vpss.a

&emsp;&emsp;Header: ak_vpss.h

<br/>

### **AK_MPI_VPSS_StartGrp**

&emsp;&emsp;【Description】

&emsp;&emsp;Starts a VPSS GROUP.

&emsp;&emsp;To create a new channel after startGrp, first call stopGrp. startGrp initializes the channels already added to the group, so the group must be stopped before another channel can be added.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_VPSS_StartGrp(AK_S32 s32VpssGrp);
```

&emsp;&emsp;【Parameters】

| **Parameter**   | **Description**                                         | **Input/Output** |
| ---------- | ---------------------------------------------- | --------- |
| s32VpssGrp | VPSS GROUP ID [0,4]. In multi-camera mode, different devices use different group IDs. | Input        |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0       | Success.        |
| Nonzero      | Failure; the value is an error code. |

&emsp;&emsp;【Error Code List】

| **Error code**                        | **Description**      |
| ------------------------------ | ----------- |
| ERROR_VPSS_NO_WORK             | VPSS not initialized    |
| ERROR_TYPE_INVALID_ARG         | Invalid parameter        |
| ERROR_VPSS_GRPID_NO_FOUND      | Group ID not found |
| ERROR_VPSS_GRP_ENABLE_YET | Group already enabled |
| ERROR_VPSS_CHN_SET_BUF_FAIL    | Failed to set channel buffer   |
| ERROR_VPSS_CHN_ALLLOC_BUF_FAIL | Failed to allocate channel buffer   |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_vpss.a

&emsp;&emsp;Header: ak_vpss.h

<br/>

### **AK_MPI_VPSS_StopGrp**

&emsp;&emsp;【Description】

&emsp;&emsp;Stops a VPSS GROUP.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_VPSS_StopGrp(AK_S32 s32VpssGrp);
```

&emsp;&emsp;【Parameters】

| **Parameter**   | **Description**                                         | **Input/Output** |
| ---------- | ---------------------------------------------- | --------- |
| s32VpssGrp | VPSS GROUP ID [0,4]. In multi-camera mode, different devices use different group IDs. | Input        |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0       | Success.        |
| Nonzero      | Failure; the value is an error code. |

&emsp;&emsp;【Error Code List】

| **Error code**                   | **Description**      |
| ------------------------- | ----------- |
| ERROR_VPSS_NO_WORK        | VPSS not initialized    |
| ERROR_TYPE_INVALID_ARG    | Invalid parameter        |
| ERROR_VPSS_GRPID_NO_FOUND | Group ID not found |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_vpss.a

&emsp;&emsp;Header: ak_vpss.h

<br/>

### **AK_MPI_VPSS_SetGrpAttr**

&emsp;&emsp;【Description】

&emsp;&emsp;Sets VPSS group attributes.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_VPSS_SetGrpAttr(AK_S32 s32VpssGrp, const VPSS_GRP_ATTR_S *pstVpssGrpAttr);
```

&emsp;&emsp;【Parameters】

| **Parameter**       | **Description**                                         | **Input/Output** |
| -------------- | ---------------------------------------------- | --------- |
| s32VpssGrp     | VPSS GROUP ID [0,4]. In multi-camera mode, different devices use different group IDs. | Input        |
| pstVpssGrpAttr | VPSS group attributes                                   | Input        |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0       | Success.        |
| Nonzero      | Failure; the value is an error code. |

&emsp;&emsp;【Error Code List】

| **Error code**                   | **Description**      |
| ------------------------- | ----------- |
| ERROR_VPSS_NO_WORK        | VPSS not initialized    |
| ERROR_TYPE_INVALID_ARG    | Invalid parameter        |
| ERROR_VPSS_GRPID_NO_FOUND | Group ID not found |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_vpss.a

&emsp;&emsp;Header: ak_vpss.h

<br/>

### **AK_MPI_VPSS_GetGrpAttr**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets VPSS group attributes.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_VPSS_GetGrpAttr(AK_S32 s32VpssGrp, VPSS_GRP_ATTR_S *pstVpssGrpAttr);
```

&emsp;&emsp;【Parameters】

| **Parameter**       | **Description**                                         | **Input/Output** |
| -------------- | ---------------------------------------------- | --------- |
| s32VpssGrp     | VPSS GROUP ID [0,4]. In multi-camera mode, different devices use different group IDs. | Input        |
| pstVpssGrpAttr | VPSS group attributes                                   | Output        |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0       | Success.        |
| Nonzero      | Failure; the value is an error code. |

&emsp;&emsp;【Error Code List】

| **Error code**                   | **Description**      |
| ------------------------- | ----------- |
| ERROR_VPSS_NO_WORK        | VPSS not initialized    |
| ERROR_TYPE_INVALID_ARG    | Invalid parameter        |
| ERROR_VPSS_GRPID_NO_FOUND | Group ID not found |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_vpss.a

&emsp;&emsp;Header: ak_vpss.h

<br/>

### **AK_MPI_VPSS_SetChnAttr**

&emsp;&emsp;【Description】

&emsp;&emsp;Sets VPSS channel attributes.

&emsp;&emsp;Setting channel attributes and calling startGrp is equivalent to creating a channel.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_VPSS_SetChnAttr(AK_S32 s32VpssGrp, AK_S32 s32ChnId, const VPSS_CHN_ATTR_S *pstVpssChnAttr);
```

&emsp;&emsp;【Parameters】

| **Parameter**       | **Description**                                                    | **Input/Output** |
| -------------- | --------------------------------------------------------- | --------- |
| s32VpssGrp     | VPSS GROUP ID [0,4]. In multi-camera mode, different devices use different group IDs.            | Input        |
| s32ChnId       | VPSS channel ID [0, 2]. By default, ChnId is 0 for the primary channel, 1 for the secondary channel, and 2 for the third channel. | Input        |
| pstVpssChnAttr | VPSS channel attributes                                                 | Input        |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0       | Success         |
| Nonzero      | Failure; the value is an error code. |

&emsp;&emsp;【Error Code List】

| **Error code**                      | **Description**      |
| ---------------------------- | ----------- |
| ERROR_VPSS_NO_WORK           | VPSS not initialized    |
| ERROR_TYPE_INVALID_ARG       | Invalid parameter        |
| ERROR_VPSS_GRPID_NO_FOUND    | Group ID not found |
| ERROR_VPSS_CHN_REGISTER_FAIL | Channel registration failed      |
| ERROR_VPSS_CHN_OPEN | Failed to open channel |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_vpss.a

&emsp;&emsp;Header: ak_vpss.h

<br/>

### **AK_MPI_VPSS_GetChnAttr**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets VPSS channel attributes.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_VPSS_GetChnAttr(AK_S32 s32VpssGrp, AK_S32 s32ChnId, VPSS_CHN_ATTR_S *pstVpssChnAttr);
```

&emsp;&emsp;【Parameters】

| **Parameter**       | **Description**                                                    | **Input/Output** |
| -------------- | --------------------------------------------------------- | --------- |
| s32VpssGrp     | VPSS GROUP ID [0,4]. In multi-camera mode, different devices use different group IDs.            | Input        |
| s32ChnId       | VPSS channel ID [0, 2]. By default, ChnId is 0 for the primary channel, 1 for the secondary channel, and 2 for the third channel. | Input        |
| pstVpssChnAttr | VPSS channel attributes                                                 | Output        |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0       | Success.        |
| Nonzero      | Failure; the value is an error code. |

&emsp;&emsp;【Error Code List】

| **Error code**                   | **Description**      |
| ------------------------- | ----------- |
| ERROR_VPSS_NO_WORK        | VPSS not initialized    |
| ERROR_TYPE_INVALID_ARG    | Invalid parameter        |
| ERROR_VPSS_GRPID_NO_FOUND | Group ID not found |
| ERROR_VPSS_CHNID_NO_FOUND | Channel ID not found     |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_vpss.a

&emsp;&emsp;Header: ak_vpss.h

<br/>

### **AK_MPI_VPSS_EnableChn**

&emsp;&emsp;【Description】

&emsp;&emsp;Enables a VPSS channel.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_VPSS_EnableChn(AK_S32 s32VpssGrp, AK_S32 s32ChnId);
```

&emsp;&emsp;【Parameters】

| **Parameter**   | **Description**                                                    | **Input/Output** |
| ---------- | --------------------------------------------------------- | --------- |
| s32VpssGrp | VPSS GROUP ID [0,4]. In multi-camera mode, different devices use different group IDs.            | Input        |
| s32ChnId   | VPSS channel ID [0, 2]. By default, ChnId is 0 for the primary channel, 1 for the secondary channel, and 2 for the third channel. | Input        |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0       | Success.        |
| Nonzero      | Failure; the value is an error code. |

&emsp;&emsp;【Error Code List】

| **Error code**                        | **Description**      |
| ------------------------------ | ----------- |
| ERROR_VPSS_NO_WORK             | VPSS not initialized    |
| ERROR_TYPE_INVALID_ARG         | Invalid parameter        |
| ERROR_VPSS_GRPID_NO_FOUND      | Group ID not found |
| ERROR_VPSS_CHNID_NO_FOUND      | Channel ID not found     |
| ERROR_VPSS_GRP_NOT_ENABLE | Group not enabled |
| ERROR_VPSS_CHN_ENABLE_YET | Channel already enabled |
| ERROR_VPSS_CHN_ALLLOC_BUF_FAIL | Failed to allocate channel buffer   |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_vpss.a

&emsp;&emsp;Header: ak_vpss.h

<br/>

### **AK_MPI_VPSS_DisableChn**

&emsp;&emsp;【Description】

&emsp;&emsp;Disables a VPSS channel.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_VPSS_DisableChn(AK_S32 s32VpssGrp, AK_S32 s32ChnId);
```

&emsp;&emsp;【Parameters】

| **Parameter**   | **Description**                                                    | **Input/Output** |
| ---------- | --------------------------------------------------------- | --------- |
| s32VpssGrp | VPSS GROUP ID [0,4]. In multi-camera mode, different devices use different group IDs.            | Input        |
| s32ChnId   | VPSS channel ID [0, 2]. By default, ChnId is 0 for the primary channel, 1 for the secondary channel, and 2 for the third channel. | Input        |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0       | Success         |
| Nonzero      | Failure; the value is an error code. |

&emsp;&emsp;【Error Code List】

| **Error code**                   | **Description**      |
| ------------------------- | ----------- |
| ERROR_VPSS_NO_WORK        | VPSS not initialized    |
| ERROR_TYPE_INVALID_ARG    | Invalid parameter        |
| ERROR_VPSS_GRPID_NO_FOUND | Group ID not found |
| ERROR_VPSS_CHNID_NO_FOUND | Channel ID not found     |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_vpss.a

&emsp;&emsp;Header: ak_vpss.h

<br/>

### **AK_MPI_VPSS_BindChn**

&emsp;&emsp;【Description】

&emsp;&emsp;Binds the input VI channel.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_VPSS_BindChn( AK_S32 s32VpssGrp, AK_S32 s32LinkChnId);
```

&emsp;&emsp;【Parameters】

| **Parameter**     | **Description**                                         | **Input/Output** |
| ------------ | ---------------------------------------------- | --------- |
| s32VpssGrp   | VPSS GROUP ID [0,4]. In multi-camera mode, different devices use different group IDs. | Input        |
| s32LinkChnId | VI channel ID | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0       | Success.        |
| Nonzero      | Failure; the value is an error code. |

&emsp;&emsp;【Error Code List】

| **Error code**                   | **Description**      |
| ------------------------- | ----------- |
| ERROR_VPSS_NO_WORK        | VPSS not initialized    |
| ERROR_TYPE_INVALID_ARG    | Invalid parameter        |
| ERROR_VPSS_GRPID_NO_FOUND | Group ID not found |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_vpss.a

&emsp;&emsp;Header: ak_vpss.h

<br/>

### **AK_MPI_VPSS_GetFrame**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets one processed image from a VPSS channel.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_VPSS_GetFrame(AK_S32 s32VpssGrp, AK_S32 s32ChnId, VPSS_FRAME_INFO_S *pstFrameInfo, AK_S32 s32MilliSec);
```

&emsp;&emsp;【Parameters】

| **Parameter**     | **Description**                                                    | **Input/Output** |
| ------------ | --------------------------------------------------------- | --------- |
| s32VpssGrp   | VPSS GROUP ID [0,4]. In multi-camera mode, different devices use different group IDs.            | Input        |
| s32ChnId     | VPSS channel ID [0, 2]. By default, ChnId is 0 for the primary channel, 1 for the secondary channel, and 2 for the third channel. | Input        |
| pstFrameInfo | Video-frame structure                                                     | Output        |
| s32MilliSec  | Timeout: -1 blocks; 0 is nonblocking; >0 is the wait duration in ms.                                | Input        |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0       | Success.        |
| Nonzero      | Failure; the value is an error code. |

&emsp;&emsp;【Error Code List】

| **Error code**                   | **Description**      |
| ------------------------- | ----------- |
| ERROR_VPSS_NO_WORK        | VPSS not initialized    |
| ERROR_VPSS_CHN_NO_OPEN | Channel not open |
| ERROR_TYPE_INVALID_ARG | Invalid Dev parameter |
| ERROR_VPSS_GRPID_NO_FOUND | Group ID not found |
| ERROR_VPSS_CHNID_NO_FOUND | Channel ID not found     |
| ERROR_VPSS_GRP_NOT_ENABLE | Group not enabled |
| ERROR_VPSS_CHN_NOT_ENABLE | Channel not enabled |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_vpss.a

&emsp;&emsp;Header: ak_vpss.h

<br/>

### **AK_MPI_VPSS_ReleaseFrame**

&emsp;&emsp;【Description】

&emsp;&emsp;Releases one VPSS-channel image.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_VPSS_ReleaseFrame(AK_S32 s32VpssGrp, AK_S32 s32ChnId, VPSS_FRAME_INFO_S *pstFrameInfo);
```

&emsp;&emsp;【Parameters】

| **Parameter**     | **Description**                                                    | **Input/Output** |
| ------------ | --------------------------------------------------------- | --------- |
| s32VpssGrp   | VPSS GROUP ID [0,4]. In multi-camera mode, different devices use different group IDs.            | Input        |
| s32ChnId     | VPSS channel ID [0, 2]. By default, ChnId is 0 for the primary channel, 1 for the secondary channel, and 2 for the third channel. | Input        |
| pstFrameInfo | Video-frame structure                                                     | Output        |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0       | Success.        |
| Nonzero      | Failure; the value is an error code. |

&emsp;&emsp;【Error Code List】

| **Error code**                   | **Description**      |
| ------------------------- | ----------- |
| ERROR_VPSS_NO_WORK        | VPSS not initialized    |
| ERROR_TYPE_INVALID_ARG    | Invalid parameter        |
| ERROR_VPSS_GRPID_NO_FOUND | Group ID not found |
| ERROR_VPSS_CHNID_NO_FOUND | Channel ID not found     |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_vpss.a

&emsp;&emsp;Header: ak_vpss.h

<br/>

### **AK_MPI_VPSS_GetGrpFrame**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets one original RAW image from a VPSS GROUP.

&emsp;&emsp;VPSS bypass mode can be enabled to obtain original input data, but it uses 3DNR memory. Disable 3DNR first; while bypass is enabled, the PP channel cannot output YUV data.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_VPSS_GetGrpFrame(AK_S32 s32VpssGrp, VPSS_FRAME_INFO_S *pstFrameInfo, AK_S32 s32MilliSec);
```

&emsp;&emsp;【Parameters】

| **Parameter**     | **Description**                                         | **Input/Output** |
| ------------ | ---------------------------------------------- | --------- |
| s32VpssGrp   | VPSS GROUP ID [0,4]. In multi-camera mode, different devices use different group IDs. | Input        |
| pstFrameInfo | Video-frame structure                                          | Output        |
| s32MilliSec  | Timeout: -1 blocks; 0 is nonblocking; >0 is the wait duration in ms.                     | Input        |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0       | Success         |
| Nonzero      | Failure; the value is an error code. |

&emsp;&emsp;【Error Code List】

| **Error code**                    | **Description**      |
| -------------------------- | ----------- |
| ERROR_VPSS_NO_WORK         | VPSS not initialized    |
| ERROR_TYPE_INVALID_ARG     | Invalid parameter        |
| ERROR_VPSS_GRPID_NO_FOUND  | Group ID not found |
| ERROR_TYPE_MALLOC_FAILED   | Memory allocation failed      |
| ERROR_TYPE_DEV_CTRL_FAILED | Device operation failed |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_vpss.a

&emsp;&emsp;Header: ak_vpss.h

<br/>

### **AK_MPI_VPSS_ReleaseGrpFrame**

&emsp;&emsp;【Description】

&emsp;&emsp;Releases one VPSS GROUP RAW image.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_VPSS_ReleaseGrpFrame(AK_S32 s32VpssGrp, VPSS_FRAME_INFO_S *pstFrameInfo);
```

&emsp;&emsp;【Parameters】

| **Parameter**     | **Description**                                         | **Input/Output** |
| ------------ | ---------------------------------------------- | --------- |
| s32VpssGrp   | VPSS GROUP ID [0,4]. In multi-camera mode, different devices use different group IDs. | Input        |
| pstFrameInfo | Video-frame structure                                          | Output        |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0       | Success         |
| Nonzero      | Failure; the value is an error code. |

&emsp;&emsp;【Error Code List】

| **Error code**                | **Description** |
| ---------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid parameter   |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_vpss.a

&emsp;&emsp;Header: ak_vpss.h

<br/>

### AK_MPI_VPSS_SetStitchChn

&emsp;&emsp;【Description】

&emsp;&emsp;Sets a stitched channel.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_VPSS_SetStitchChn(AK_S32 s32VpssGrp, AK_S32 s32ChnId, const VPSS_STITCH_ATTR_S *pstVpssStitchAttr);
```

&emsp;&emsp;【Parameters】

| **Parameter**          | **Description**                                                    | **Input/Output** |
| ----------------- | --------------------------------------------------------- | --------- |
| s32VpssGrp        | VPSS GROUP ID [0,4]. In multi-camera mode, different devices use different group IDs.            | Input        |
| s32ChnId          | VPSS channel ID [0, 2]. By default, ChnId is 0 for the primary channel, 1 for the secondary channel, and 2 for the third channel. | Input        |
| pstVpssStitchAttr | Pointer to the stitched-channel structure | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0       | Success         |
| Nonzero      | Failure; the value is an error code. |

&emsp;&emsp;【Error Code List】

| **Error code**                   | **Description**      |
| ------------------------- | ----------- |
| ERROR_VPSS_NO_WORK        | VPSS not initialized    |
| ERROR_TYPE_INVALID_ARG    | Invalid parameter        |
| ERROR_VPSS_GRPID_NO_FOUND | Group ID not found |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_vpss.a

&emsp;&emsp;Header: ak_vpss.h

## Call Flow

```c
    /* Initialize VI */
    AK_MPI_VI_CreateDev(s32ViDev,&stViDevAttr);
    AK_MPI_VI_SetChnAttr(s32ViDev, 0, &stViChnAttr);

    /* Initialize VPSS */
    AK_MPI_VPSS_CreateGrp(s32GrpId, &stGrpAttr);
    AK_MPI_VPSS_SetChnAttr(s32GrpId, 0, &stVpssChnAttr);

    /* Bind VI and VPSS */
    AK_MPI_VI_BindVpssGrp(s32DevId, 0, s32DevId);
    AK_MPI_VPSS_BindChn(s32DevId, s32LinkChnId);

    /* Enable VI */
    AK_MPI_VI_EnableDev(s32ViDev);
    AK_MPI_VI_EnableChn(s32ViDev, 0);

    /* Enable VPSS */
    AK_MPI_VPSS_StartGrp(s32GrpId);
    AK_MPI_VPSS_EnableChn(s32GrpId, 0);

    /* Get and release frames */
    AK_MPI_VPSS_GetFrame(j, 0, &stFrame, 2000);
    AK_MPI_VPSS_ReleaseFrame(j, 0, &stFrame);

    /* Stop VPSS */
    AK_MPI_VPSS_DisableChn(s32GrpId, 0);
    AK_MPI_VPSS_StopGrp(s32GrpId);
    AK_MPI_VPSS_DestroyGrp(s32GrpId);

    /* Stop VI */
    AK_MPI_VI_DisableChn(s32ViDev, 0);
    AK_MPI_VI_DisableDev(s32ViDev);
    AK_MPI_VI_DestroyDev(s32ViDev);
```

<br/>

## VPSS Flow Example

### **ak_vpss_sample**

Before running this sample, load ak_vi.ko, sensor_xxx.ko, ak_vicap.ko, ak_isp.ko, and ak_pp.ko with insmod. For the commands, see the description at the beginning of Chapter 7.

| **Input parameter** | **Description** |
| --------------- | ------------------------------- |
| chn_index       | Channel ID                            |
| frame_cnt | Number of YUV frames to save |
| chn_res_index | Channel resolution ID |
| chn_framerate | Channel capture frame rate |
| isp_config_path | ISP configuration-file path; empty by default and must be specified |
| frame_save_path | Path for saving YUV image data |
| dev_cnt | Number of devices [1, 2]; default 1, use 2 for a dual-camera version |

<br/>

&emsp;&emsp;Output: the captured YUV data is saved in the specified path directory.

<br/>

## /var/platform Description

The /var/platform directory exposes the current module configuration parameters and status. Its parameters are described below.

### param

| Parameter | Description |
| ---------------------- | ---------------- |
| sensor_fps | Sensor frame rate |
| grp0_width | Group width |
| grp0_height | Group height |
| grp0_ispCfgPath | ISP conf path |
| grp0_sensorId          | sensor id        |
| grp0_inputPixFmt | Group input format |
| grp0_workMode | Group operating mode |
| grp0_bEnGrpBypass | Enable bypass |
| grp0_bMirror | Mirror |
| grp0_bFlip | Flip |
| grp0_chn0_width | Output-channel width |
| grp0_chn0_height | Output-channel height |
| grp0_chn0_maxBufSize | Maximum buffer size |
| grp0_chn0_outputPixFmt | Channel output format |
| grp0_chn0_chnMode | Channel operating mode |
| grp0_chn0_frameDepth | Number of capture buffers |
| grp0_chn0_fps | Channel frame rate |
| grp0_chn0_crop_x | Channel crop rectangle [x,y,w,h] |
| grp0_chn0_crop_y | Channel crop rectangle [x,y,w,h] |
| grp0_chn0_crop_w | Channel crop rectangle [x,y,w,h] |
| grp0_chn0_crop_h | Channel crop rectangle [x,y,w,h] |

### stat

| Parameter | Description |
| ---------------- | ----------- |
| version | VPSS library version |
| ispsdk_version | ISP SDK library version |
| mode | Current mode |
| grp0_status | Group status |
| grp0_chn0_status | Channel status |

<br/>

## Error Codes

| Error code | Macro | Meaning |
| ---------- | ------------------------------ | ----------- |
| 0x0a000000 | ERROR_VPSS_INVALID_GRPID | Invalid group ID |
| 0x0a000001 | ERROR_VPSS_GRPID_NO_FOUND | Group ID not found |
| 0x0a000002 | ERROR_VPSS_GRP_CREATE_FAIL | Group creation failed |
| 0x0a000003 | ERROR_VPSS_GRP_CREATED_YET | Group already created |
| 0x0a000004 | ERROR_VPSS_NO_WORK | Module not working |
| 0x0a000005 | ERROR_VPSS_GRP_NOT_DISABLE | Group not disabled |
| 0x0a000006 | ERROR_VPSS_GRP_NOT_ENABLE | Group not enabled |
| 0x0a000007 | ERROR_VPSS_GRP_ENABLE_YET | Group already enabled |
| 0x0a000008 | ERROR_VPSS_CHN_NOT_ENABLE      | Channel registration failed      |
| 0x0a000009 | ERROR_VPSS_CHN_ENABLE_YET | Channel already enabled |
| 0x0a00000a | ERROR_VPSS_CHN_REGISTER_FAIL   | Channel registration failed      |
| 0x0a00000b | ERROR_VPSS_CHNID_NO_FOUND | Channel ID not found |
| 0x0a00000c | ERROR_VPSS_CHN_SET_BUF_FAIL    | Failed to set channel buffer   |
| 0x0a00000d | ERROR_VPSS_CHN_ALLLOC_BUF_FAIL | Failed to allocate channel buffer   |
| 0x0a00000e | ERROR_VPSS_CHN_SET_QBUF_FAIL | Failed to set channel qbuf |
| 0x0a00000f | ERROR_VPSS_BIND_CHN | Channel binding error |
| 0x0a000010 | ERROR_VPSS_GET_PAD_ID | Error getting pad ID |
| 0x0a000011 | ERROR_VPSS_ISP_DEV_OPEN | Error opening ISP device |
| 0x0a000012 | ERROR_VPSS_CHN_OPEN | Failed to open channel |
| 0x0a000013 | ERROR_VPSS_CHN_NO_OPEN | Channel not open |
| 0x0a000014 | ERROR_VPSS_SENSOR_ID | Sensor ID error |
| 0x0a000015 | ERROR_VPSS_EXP_NOT_STABLE | Exposure not stable |

<br/>
