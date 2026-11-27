# Video Stream Mode

## Overview

&emsp;&emsp;The video-stream-mode module provides common video wrappers and binds VPSS to VENC.

&emsp;&emsp;One source channel may bind multiple destination channels, but a destination channel may bind only one source channel.

<br/>

## API Reference

&emsp;&emsp;This module provides the APIs listed below.

| **Data structure**         | **Description**       |
| ---------------- | ------------ |
| EXT_CHN_S | Channel-information structure |
| BIND_MODE_E | Binding-mode enumeration |
| EXT_BIND_PARAM_S | Binding-parameter structure |

<br/>

| **Function**                     | **Description**               |
| ---------------------------- | -------------------- |
| AK_EXT_VIDEO_GetVersion | Gets the video-stream-mode library version. |
| AK_EXT_VIDEO_SetDstChnActive | Enables or disables a bound destination channel. |
| AK_EXT_VIDEO_VencGetStream | Gets video-stream data. |
| AK_EXT_VIDEO_BindChn | Binds channels. |
| AK_EXT_VIDEO_UnbindChn | Unbinds channels. |
| AK_EXT_VIDEO_SetCb | Sets a callback. |
| AK_EXT_VIDEO_UnsetCb | Removes a callback. |
| AK_EXT_VIDEO_SetChnAttr | Sets channel parameters. |
| <br/>                        |                      |

## Data Structures

### EXT_CHN_S

&emsp;&emsp;【Notes】

&emsp;&emsp;Channel-information structure.

&emsp;&emsp;【Definition】

```c
typedef struct akEXT_CHN_S
{
    MODULE_ID_E         enModId;            /* module id  */
    AK_S32              s32DevId;
    /* object id, chn id for vpss, encoder id for venc, decoder id for vdec*/
    AK_S32              s32ChnId;
}EXT_CHN_S;
```

&emsp;&emsp;【Members】

| **Member** | **Description**                                                                        |
| -------- | ----------------------------------------------------------------------------- |
| enModId | Module ID |
| s32DevId | Device ID                                                                          |
| s32ChnId | Channel ID. If enModId is VPSS, u32ChnId is the VPSS channel ID; if enModId is VENC, u32ChnId is the VENC channel ID. |
| <br/>    |                                                                               |

> **Source note:** Source-derived references to `APP_CHN_S`, `APP_BIND_PARAM`, and `u32ChnId` mean the supplied header's `EXT_CHN_S`, `EXT_BIND_PARAM_S`, and `s32ChnId`, respectively.

### BIND_MODE_E

&emsp;&emsp;【Notes】

&emsp;&emsp;Encoding-mode enumeration.

&emsp;&emsp;【Definition】

```c
typedef enum akBIND_MODE_E
{
    USER_MODE = 0x0,
    AUTO_MODE,
}BIND_MODE_E;
```

&emsp;&emsp;【Members】

| **Member**  | **Description**  |
| --------- | ------- |
| USER_MODE | User-space encoding mode |
| AUTO_MODE | Kernel-space encoding mode |

<br/>

### EXT_BIND_PARAM_S

&emsp;&emsp;【Notes】

&emsp;&emsp;Binding-parameter structure.

&emsp;&emsp;【Definition】

```c
typedef struct akEXT_BIND_PARAM_S
{
    AK_S32                      s32BPFrameRate;             /* frame rate control */
    AK_S32                      s32BPFrameDepth;            /* frame list max length*/
    BIND_MODE_E                 s32BPMode;                   /* bind mode */
}EXT_BIND_PARAM_S;
```

&emsp;&emsp;【Members】

| **Member**        | **Description**            |
| --------------- | ----------------- |
| s32BPFrameRate | Frame rate |
| s32BPFrameDepth | Maximum length of the encoded-data buffer list |
| s32BPMode | Encoding mode (0: user space; 1: kernel space) |

&emsp;&emsp;【Related Functions】

&emsp;&emsp;AK_EXT_VIDEO_BindChn

<br/>

## Interfaces

### AK_EXT_VIDEO_GetVersion

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the video-stream-mode library version.

&emsp;&emsp;【Syntax】

```c
    const AK_CHAR* AK_EXT_VIDEO_GetVersion(AK_VOID);
```

&emsp;&emsp;【Return Value】

| **Return value**   | **Description** |
| --------- | ------ |
| Video-stream-mode library version | Success |
| NULL      | Failure     |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libapp_video.a

&emsp;&emsp;Header: ak_video.h

<br/>

### AK_EXT_VIDEO_BindChn

&emsp;&emsp;【Description】

&emsp;&emsp;Binds a source channel to a destination channel.

​        When one source channel is bound to multiple encoders, all bindings must use either user-space encoding or kernel-space encoding; user-space and kernel-space encoding cannot be mixed.

&emsp;&emsp;【Syntax】

```c
AK_S32 AK_EXT_VIDEO_BindChn(const EXT_CHN_S *pstSrcChn,const EXT_CHN_S *pstDstChn,
                                            const EXT_BIND_PARAM_S *pstBparam);
```

&emsp;&emsp;【Parameters】

| **Parameter**  | **Description**    | **Value range**            | **Input/Output** |
| --------- | --------- | ------------------- | --------- |
| pstSrcChn | Source channel | See APP_CHN_S | Input |
| pstDstChn | Destination channel | See APP_CHN_S | Input |
| pstBparam | Binding parameters | See APP_BIND_PARAM | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0       | Success         |
| Nonzero      | Failure; the return value is an error code. |

&emsp;&emsp;【Error Code List】

| **Error code**                                     | **Description**                    |
| ------------------------------------------- | ------------------------- |
| ERROR_TYPE_INVALID_ARG                      | Invalid parameter                      |
| ERROR_EXT_VIDEO_WRONG_SRC_MODULE | Unsupported source-channel module |
| ERROR_EXT_VIDEO_INCORRECT_BIND_RELATION | Incorrect binding relationship |
| ERROR_EXT_VIDEO_DST_CHN_MUTLEPLE_BINDED | Destination channel bound multiple times |
| ERROR_EXT_VIDEO_SRC_CHN_OUTOF_RANGE | Source channel exceeds the maximum number of bound destination channels |
| ERROR_VI_INVALID_CHNID | Invalid VI channel ID |
| ERROR_VI_INVALID_DEVID | Invalid VI device ID |
| ERROR_VI_DEVID_NOT_OPEN | VI device not open |
| ERROR_VI_CHANNEL_NOT_EXIST | VI channel does not exist |
| ERROR_VENC_USER_NULL | VENC user does not exist |
| ERROR_EXT_VIDEO_SRC_DST_CHN_PARAM_NOT_MATCH | Source- and destination-channel resolutions do not match |
| ERROR_EXT_VIDEO_GENERATE_GOBJ_FAILED | Failed to construct video-binding structure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libapp_video.a

&emsp;&emsp;Header: ak_video.h

<br/>

### AK_EXT_VIDEO_UnbindChn

&emsp;&emsp;【Description】

&emsp;&emsp;Unbinds a source channel from a destination channel.

&emsp;&emsp;【Syntax】

```C
AK_S32 AK_EXT_VIDEO_UnbindChn(const EXT_CHN_S *pstSrcChn,const EXT_CHN_S *pstDstChn);
```

&emsp;&emsp;【Parameters】

| **Parameter**  | **Description**    | **Value range**       | **Input/Output** |
| --------- | --------- | -------------- | --------- |
| pstSrcChn | Source channel | See APP_CHN_S | Input |
| pstDstChn | Destination channel | See APP_CHN_S | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0       | Success         |
| Nonzero      | Failure; the return value is an error code. |

&emsp;&emsp;【Error Code List】

| **Error code**                                 | **Description**             |
| --------------------------------------- | ------------------ |
| ERROR_TYPE_INVALID_ARG                  | Invalid parameter               |
| ERROR_EXT_VIDEO_WRONG_SRC_MODULE | Unsupported source-channel module |
| ERROR_EXT_VIDEO_INCORRECT_BIND_RELATION | Incorrect binding relationship |
| ERROR_EXT_VIDEO_SRC_HHN_NOT_BINDED | Source channel not bound |
| ERROR_EXT_VIDEO_DST_CHN_NOT_BINDED | Destination channel not bound |
| ERROR_EXT_VIDEO_DST_CHN_NOT_DISABLED | Destination channel not disabled |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libapp_video.a

&emsp;&emsp;Header: ak_video.h

<br/>

### AK_EXT_VIDEO_SetDstChnActive

&emsp;&emsp;【Description】

&emsp;&emsp;Enables or disables a bound destination channel.

&emsp;&emsp;The destination channel must be bound before this interface can enable or disable it.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_EXT_VIDEO_SetDstChnActive(const EXT_CHN_S *pstChn, AK_S32 s32Enable);
```

&emsp;&emsp;【Parameters】

| **Parameter**  | **Description**    | **Value range**       | **Input/Output** |
| --------- | --------- | -------------- | --------- |
| pstChn | Destination channel | See APP_CHN_S | Input |
| s32Enable | Enable flag | 0: disable; 1: enable | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0       | Success         |
| Nonzero      | Failure; the return value is an error code. |

&emsp;&emsp;【Error Code List】

| **Error code**                            | **Description**        |
| ---------------------------------- | ------------- |
| ERROR_TYPE_INVALID_ARG             | Invalid parameter          |
| ERROR_EXT_VIDEO_DST_CHN_NOT_BINDED | Destination channel not bound |
| ERROR_VENC_USER_NULL | VENC user does not exist |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libapp_video.a

&emsp;&emsp;Header: ak_video.h

<br/>

### AK_EXT_VIDEO_VencGetStream

&emsp;&emsp;【Description】

&emsp;&emsp;Gets video-stream data.

&emsp;&emsp;【Syntax】

```C
AK_S32 AK_EXT_VIDEO_VencGetStream(const EXT_CHN_S *pstChn, VIDEO_STREAM_S *pstVideoStream);
```

&emsp;&emsp;【Parameters】

| **Parameter**       | **Description**    | **Value range**       | **Input/Output** |
| -------------- | --------- | -------------- | --------- |
| pstChn | Destination channel | See APP_CHN_S | Input |
| pstVideoStream | Stream data | - | Output |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0       | Success         |
| Nonzero      | Failure; the return value is an error code. |

&emsp;&emsp;【Error Code List】

| **Error code**                             | **Description**        |
| ----------------------------------- | ------------- |
| ERROR_TYPE_INVALID_ARG              | Invalid parameter          |
| ERROR_EXT_VIDEO_DST_CHN_NOT_BINDED | Destination channel not bound |
| ERROR_EXT_VIDEO_ENCODRE_HAS_NO_DATA | No encoded data        |
| ERROR_VENC_USER_NULL | Encoding user does not exist |
| ERROR_VENC_GET_STREAM_FAILED | Failed to get encoded frame |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libapp_video.a

&emsp;&emsp;Header: ak_video.h

<br/>

### AK_EXT_VIDEO_SetCb

&emsp;&emsp;【Description】

&emsp;&emsp;Sets the callback for a bound channel. It is called after data leaves the source channel and before it reaches each bound destination channel, acting as a shared preprocessing function for those destinations.

&emsp;&emsp;For `AK_EXT_VIDEO_SetCb`, `funcVideoDataCb` and `pvOutput` are both input parameters to `AK_EXT_VIDEO_SetCb`. `AK_EXT_VIDEO_SetCb` configures them for internal use; the `pvOutput` pointer produces output data only when `funcVideoDataCb` is invoked.

&emsp;&emsp;【Syntax】

```C
AK_S32 AK_EXT_VIDEO_SetCb(const EXT_CHN_S *pstChn, EXT_VIDEO_DATA_CB_S funcVideoDataCb, AK_VOID *pvOutput);
```

&emsp;&emsp;【Parameters】

| **Parameter**        | **Description**                                                                         | **Value range**       | **Input/Output** |
| --------------- | ------------------------------------------------------------------------------ | -------------- | --------- |
| pstChn | Source channel | See APP_CHN_S | Input |
| funcVideoDataCb | Callback | Non-null | Input |
| pvOutput | pvOutput parameter configured for funcVideoDataCb; see the callback declaration for its meaning. | Non-null | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0       | Success         |
| Nonzero      | Failure; the return value is an error code. |

&emsp;&emsp;【Error Code List】

| **Error code**   | **Description**      |
| --------- | ----------- |
| AK_FAILED | Source channel not found |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libapp_video.a

&emsp;&emsp;Header: ak_video.h

> **Note:** Declaration of the funcVideoDataCb callback.

<br/>

```c
typedef AK_VOID (*EXT_VIDEO_DATA_CB_S)(EXT_CHN_S *pstChn, AK_VOID *pvInput, AK_VOID *pvOutput);
```

<br/>

### AK_EXT_VIDEO_UnsetCb

&emsp;&emsp;【Description】

&emsp;&emsp;Removes the callback.

&emsp;&emsp;【Syntax】

```C
AK_S32 AK_EXT_VIDEO_UnsetCb(const EXT_CHN_S *pstChn);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**   | **Value range**       | **Input/Output** |
| -------- | -------- | -------------- | --------- |
| pstChn | Source channel | See APP_CHN_S | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0       | Success         |
| Nonzero      | Failure; the return value is an error code. |

&emsp;&emsp;【Error Code List】

| **Error code**   | **Description**      |
| --------- | ----------- |
| AK_FAILED | Source channel not found |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libapp_video.a

&emsp;&emsp;Header: ak_video.h

<br/>

### AK_EXT_VIDEO_SetChnAttr

&emsp;&emsp;【Description】

&emsp;&emsp;Sets channel parameters.

&emsp;&emsp;【Syntax】

```C
AK_S32 AK_EXT_VIDEO_SetChnAttr(const EXT_CHN_S *pstDstChn,
                               const EXT_BIND_PARAM_S *pstBparam);
```

&emsp;&emsp;【Parameters】

| **Parameter**  | **Description**    | **Value range**            | **Input/Output** |
| --------- | --------- | ------------------- | --------- |
| pstDstChn | Destination channel | See APP_CHN_S | Input |
| pstBparam | Channel parameters | See APP_BIND_PARAM | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0       | Success         |
| Nonzero      | Failure; the return value is an error code. |

&emsp;&emsp;【Error Code List】

| **Error code**                | **Description**       |
| ---------------------- | ------------ |
| ERROR_TYPE_INVALID_ARG | Invalid parameter         |
| AK_FAILED | Destination channel not found |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libapp_video.a

&emsp;&emsp;Header: ak_video.h

<br/>

## ak_video_sample Usage Example

Before running the sample, load ak_vi.ko, sensor_xxx.ko, ak_vicap.ko, ak_isp.ko, ak_pp.ko, ak_venc_adapter.ko, and ak_venc_bridge.ko with insmod. For the commands, see the description at the beginning of Chapter 7.

| **Input parameter** | **Description** |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| chn_index | VPSS channel ID [0: primary channel; 1: secondary channel] |
| frame_cnt | Number of frames captured from VI. |
| chn_res_index | VPSS channel resolution<br />[0 - 17] 0 - 320\*184; 1 - 320\*240; 2 - 640\*360; 3 - 640\*480; 4 - 736\*756; 5 - 1280\*720; 6 - 1280\*960; 7 - 1920\*1080; 8 - 2304\*1296; 9 - 2048\*1536; 10 - 2560\*1440; 11 - 2688\*1520; 12 - 2880\*1624; 13 - 2560\*1920; 14 - 2944\*1664; 15 - 3072\*1728; 16 - 3072\*2048; 17 - 3840\*2160 |
| chn_framerate | Frame rate |
| enc_type | Encoded output format: h264, h265, or jpeg |
| br_mode | Bit-rate control mode: 0 CBR; 1 VBR |
| target_kbps | Target bit rate |
| isp_config_path | ISP conf path |
| frame_save_path | Encoded-data output path |
| encode_mode | Encoding mode: 0 user space; 1 kernel-space full-frame mode |

<br/>

&emsp;&emsp;Output: the encoded video-bitstream file is saved in the specified path directory.

<br/>

## /var/platform Description

The /var/platform directory exposes the current module configuration parameters and status. Its parameters are described below.

### param

| Parameter | Description |
| ------------------------------- | ------------------------ |
| Chns%d:%d | chn src: source-channel module and channel IDs |
| Chnd%d:%d | chn dest: destination-channel module and channel IDs |
| Chns%d:%d_Chnd%d:%d_frame_rate | Frame rate |
| Chns%d:%d_Chnd%d:%d_frame_depth | Frame depth |
| Chns%d:%d_Chnd%d:%d_mode | Mode |

### stat

| Parameter | Description |
| -------------------------------- | ------------------ |
| version | Version |
| Chns%d:%d_Chnd%d:%d":    "bind", | Module status: bind / unbind |

<br/>

## Error Codes

| Error code | Macro | Meaning |
| ---------- | -------------------------------------------- | ------------- |
| 0x1a000000 | ERROR_EXT_VIDEO_WRONG_SRC_MODULE | Invalid source module |
| 0x1a000001 | ERROR_EXT_VIDEO_WRONG_MODULE_ID | Invalid module ID |
| 0x1a000002 | ERROR_EXT_VIDEO_INCORRECT_BIND_RELATION | Too many opens |
| 0x1a000003 | ERROR_EXT_VIDEO_DST_CHN_MUTLEPLE_BINDED | Destination channel bound multiple times |
| 0x1a000004 | ERROR_EXT_VIDEO_DST_CHN_NOT_BINDED | Destination channel not bound |
| 0x1a000005 | ERROR_EXT_VIDEO_SRC_HHN_NOT_BINDED | Source channel not bound |
| 0x1a000006 | ERROR_EXT_VIDEO_SRC_CHN_OUTOF_RANGE | Source channel out of range |
| 0x1a000007 | ERROR_EXT_VIDEO_SRC_DST_CHN_PARAM_NOT_MATCH | Source- and destination-channel parameters do not match |
| 0x1a000008 | ERROR_EXT_VIDEO_GENERATE_GOBJ_FAILED | GOBJ registration failed |
| 0x1a000009 | ERROR_EXT_VIDEO_GENERATE_OBJ_FAILED | OBJ registration failed |
| 0x1a00000a | ERROR_EXT_VIDEO_ENCODRE_HAS_NO_DATA | Encoder has no data |
| 0x1a00000b | ERROR_EXT_VIDEO_FRAME_COUNT_OUTOF_LIMITATION | Frame count exceeds limit |
| 0x1a00000c | ERROR_EXT_VIDEO_DST_CHN_NOT_DISABLED | Destination channel not disabled |

<br/>
