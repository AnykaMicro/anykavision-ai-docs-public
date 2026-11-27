# Demux

## Overview

&emsp;&emsp;The demux module (DEMUX) extracts the audio and video streams separately from a video file, or parses an audio-only file into a frame-based audio stream.

<br/>

## API Reference

&emsp;&emsp;This module provides the APIs listed in the following tables.

| **Data structure**       | **Description**                   |
| -------------------------- | -------------------------------- |
| DEMUX_CONF_S | Input parameters for the media demux library             |
| DEMUX_DATA_SOURCE_E | Media demux library data-source type                 |
| DEMUX_VIDEO_INFO_S | Video information obtained by the media library       |
| DEMUX_AUDIO_INFO_S | Audio information obtained by the media library |
| DEMUX_DATA_TYPE_E | Data-stream type obtained by the media library       |
| DEMUX_STREAM_S | Attributes of a data stream obtained by the media library       |
| DEMUX_DIRECTION_E | Direction in which to find an I-frame from the seek position      |

<br/>

| **Function**       | **Description**                   |
| -------------------------- | -------------------------------- |
| AK_MPI_DEMUX_Get_Version       | Gets the demux module version number            |
| AK_MPI_DEMUX_Open              | Opens the media demux library                   |
| AK_MPI_DEMUX_Close             | Closes the media demux library                   |
| AK_MPI_DEMUX_Get_Total_Time    | Gets the total duration of the file to demux, in ms |
| AK_MPI_DEMUX_Get_Video_Info | Gets video information for the file to demux         |
| AK_MPI_DEMUX_Get_Audio_Info    | Gets audio information for the file to demux         |
| AK_MPI_DEMUX_Get_Data          | Gets demuxed data                 |
| AK_MPI_DEMUX_Get_Video         | Gets demuxed video data             |
| AK_MPI_DEMUX_Get_Audio         | Gets demuxed audio data             |
| AK_MPI_DEMUX_Free_Data         | Frees retrieved data                 |
| AK_MPI_DEMUX_Seek_To_Keyframe  | Seeks to a specified position for demuxing           |
<br/>

## Data Structures

### DEMUX_CONF_S

&emsp;&emsp;【Notes】

&emsp;&emsp;Input parameters for the media demux library.

&emsp;&emsp;【Definition】

```c
    typedef struct akDEMUX_CONF_S
    {
        AK_VOID *pvFromDIR;// file_fd or socket
        DEMUX_DATA_SOURCE_E enDemuxDataSource;
        AK_U64 u64StartMs;
    }DEMUX_CONF_S;
```

&emsp;&emsp;【Members】

| **Member** | **Description**                                               |
| ------------------ | ------------------------------------------------------------ |
| pvFromDIR           | A file handle returned by `fopen`, or a pointer to a socket |
| enDemuxDataSource        | Specifies whether the source is a local file or a network stream                       |
| u64StartMs           | Specifies the demux start time in ms. <br/>If `ms=0`, demuxing starts at the beginning of the file.<br/>If `ms>0`, demuxing starts at `ms` in the file. |

&emsp;&emsp;【Related Functions】

```c
    AK_S32 AK_MPI_DEMUX_Open(const DEMUX_CONF_S *pstDemuxConf, AK_S32 *s32DemuxHandleId);
```

<br/>

### DEMUX_DATA_SOURCE_E

&emsp;&emsp;【Notes】

&emsp;&emsp;Media demux library data-source type. Only the `DEMUX_DATA_FROM_LOCAL_FILE` local-file mode is supported as a demux data source.

&emsp;&emsp;【Definition】

```c
    typedef enum akDEMUX_DATA_SOURCE_E
    {
        DEMUX_DATA_FROM_UNKNOWN = 0x00,
        DEMUX_DATA_FROM_LOCAL_FILE,
        DEMUX_DATA_FROM_INTERNET
    }DEMUX_DATA_SOURCE_E;
```

&emsp;&emsp;【Members】

| **Member**         | **Description**           |
| -------------------------- | ------------------------ |
| DEMUX_DATA_FROM_UNKNOWN    | Default value                   |
| DEMUX_DATA_FROM_LOCAL_FILE | The demux data source is a local file |
| DEMUX_DATA_FROM_INTERNET   | The demux data source is the network     |

&emsp;&emsp;【Related Structure】

```c
    typedef struct akDEMUX_CONF_S
    {
        AK_VOID *pvFromDIR;// file_fd or socket
        DEMUX_DATA_SOURCE_E enDemuxDataSource;
        AK_U64 u64StartMs;
    }DEMUX_CONF_S;
```

<br/>

### DEMUX_VIDEO_INFO_S

&emsp;&emsp;【Notes】

&emsp;&emsp;Video information obtained after parsing by the media library.

&emsp;&emsp;【Definition】

```c
    typedef struct akDEMUX_VIDEO_INFO_S
    {
        AK_U32 u32Fps;
        AK_S32 enVencOutputType;// enum encode_output_penDemuxDataType
        AK_U16 u16Width;
        AK_U16 u16Height;
        AK_DOUBLE dFps;
    }DEMUX_VIDEO_INFO_S;
```

&emsp;&emsp;【Members】

| **Member** | **Description**                        |
| ------------------ | ------------------------------------- |
| u32Fps                | Video frame rate                              |
| enVencOutputType         | Video type; see `enum encode_output_penDemuxDataType` |
| u16Width              | Video width                              |
| u16Height             | Video height                              |
| dFps | Frame rate represented as a floating-point value |

&emsp;&emsp;【Related Functions】

```c
    AK_S32 AK_MPI_DEMUX_Free_Data_Info(AK_S32 s32DemuxHandleId,
DEMUX_VIDEO_INFO_S *pstDemuxVideoInfo);
```

> **Source note:** Source-derived references to `AK_MPI_DEMUX_Free_Data_Info` mean the page/header-declared `AK_MPI_DEMUX_Get_Video_Info`.

<br/>

### DEMUX_AUDIO_INFO_S

&emsp;&emsp;【Notes】

&emsp;&emsp;Audio information obtained after parsing by the media library.

&emsp;&emsp;【Definition】

```c
    typedef struct akDEMUX_AUDIO_INFO_S
    {
        AUDIO_DATA_ATTR_S stAudioDataAttr;
        AUDIO_TYPE_E enAudioType; //encode | decode audio penDemuxDataType
    }DEMUX_AUDIO_INFO_S;
```

&emsp;&emsp;【Members】

| **Member** | **Description**                                |
| ------------------ | --------------------------------------------- |
| stAudioDataAttr    | Audio data attributes; see `AUDIO_DATA_ATTR_S` |
| enAudioType         | Audio type; see `AUDIO_TYPE_E`              |

&emsp;&emsp;【Related Functions】

```c
    AK_S32 AK_MPI_DEMUX_Get_Audio_Info(AK_S32 s32DemuxHandleId,
                                       DEMUX_AUDIO_INFO_S *pstDemuxAudioInfo);
```

<br/>

### DEMUX_DATA_TYPE_E

&emsp;&emsp;【Notes】

&emsp;&emsp;Data-stream type obtained by the media library.

&emsp;&emsp;【Definition】

```c
    typedef enum akDEMUX_DATA_TYPE_E
    {
        DEMUX_DATA_UNKNOW = 0x00,
        DEMUX_DATA_VIDEO,
        DEMUX_DATA_AUDIO
    }DEMUX_DATA_TYPE_E;
```

&emsp;&emsp;【Members】

| **Member** | **Description**           |
| ------------------ | ------------------------ |
| DEMUX_DATA_UNKNOW  | Default value                   |
| DEMUX_DATA_VIDEO   | The demuxed data is video data |
| DEMUX_DATA_AUDIO   | The demuxed data is audio data |

&emsp;&emsp;【Related Functions】

```c
    AK_S32 AK_MPI_DEMUX_Get_Data(AK_S32 s32DemuxHandleId, DEMUX_DATA_TYPE_E *penDemuxDataType,
                                 DEMUX_STREAM_S *pstDemuxStream);
```

<br/>

### DEMUX_STREAM_S

&emsp;&emsp;【Notes】

&emsp;&emsp;Attributes of a data stream obtained by the media library. Both video and audio streams use this structure. The difference is that the `frame_penDemuxDataType` member is meaningful only when the retrieved data is a video stream; it has no meaning for an audio stream.

&emsp;&emsp;【Definition】

```c
    typedef struct akDEMUX_STREAM_S
    {
        AK_U8 *pu8Data;    // demux pstDemuxStream data
        AK_U32 u32Len;         // demux pstDemuxStream len in bytes
        AK_U64 u64Ts;    // demux timestamp(u64Ms)
        VIDEO_FRAME_TYPE_E enVideoFrameType;    // demux I or P frame
    }DEMUX_STREAM_S;
```

&emsp;&emsp;【Members】

| **Member** | **Description**                                               |
| ------------------ | ------------------------------------------------------------ |
| pu8Data               | Address of the demuxed data                                           |
| u32Len                | Length of the demuxed data                                           |
| u64Ts                 | Timestamp of the demuxed data                                       |
| enVideoFrameType         | Whether the video frame is an I-frame or P-frame; see `enum video_frame_penDemuxDataType`. This member is meaningful only when the demuxed stream is a video stream. |

&emsp;&emsp;【Related Functions】

```c
    AK_S32 AK_MPI_DEMUX_Get_Data(AK_S32 s32DemuxHandleId, DEMUX_DATA_TYPE_E *penDemuxDataType,
                             DEMUX_STREAM_S *pstDemuxStream);

    AK_S32 AK_MPI_DEMUX_Get_Video(AK_S32 s32DemuxHandleId, DEMUX_STREAM_S *pstDemuxStream);

    AK_S32 AK_MPI_DEMUX_Get_Audio(AK_S32 s32DemuxHandleId, DEMUX_STREAM_S *pstDemuxStream);

    AK_S32 AK_MPI_DEMUX_Free_Data(AK_S32 s32DemuxHandleId, DEMUX_STREAM_S *pstDemuxStream);
```

<br/>

### DEMUX_DIRECTION_E

&emsp;&emsp;【Notes】

&emsp;&emsp;Direction in which to find an I-frame from the seek position. Because demuxing after a seek must begin at an I-frame, this enumeration specifies the I-frame search direction.

&emsp;&emsp;【Definition】

```c
    typedef enum akDEMUX_DIRECTION_E
    {
        DEMUX_DIRECTION_NEAREST = 0,    //seek to nearest key frame
        DEMUX_DIRECTION_LAST,            //seek to last key frame
        DEMUX_DIRECTION_NEXT            //seek to next key frame
    }DEMUX_DIRECTION_E;
```

&emsp;&emsp;【Members】

| **Member**      | **Description**            |
| ----------------------- | ------------------------- |
| DEMUX_DIRECTION_NEAREST | The demux library finds the nearest I-frame |
| DEMUX_DIRECTION_LAST    | Seeks to the preceding I-frame           |
| DEMUX_DIRECTION_NEXT    | Seeks to the following I-frame           |

&emsp;&emsp;【Related Functions】

```c
    AK_S32 AK_MPI_DEMUX_Seek_To_Keyframe(AK_S32 s32DemuxHandleId, AK_U64 u64Ms,
                                        DEMUX_DIRECTION_E enDemuxDirection);
```

<br/>

## Getting Version Information

### AK_MPI_DEMUX_Get_Version

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the DEMUX module version number.

&emsp;&emsp;【Syntax】

```c
    const AK_S8* AK_MPI_DEMUX_Get_Version(AK_VOID);
```

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| Demux module version number   | Success           |
| NULL             | Failure           |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_demux.so and libakmedia.so, or libmpi_demux.a and libakmedia.a

&emsp;&emsp;Header: ak_demux.h

&emsp;&emsp;【Call Sequence】

&emsp;&emsp;This function can be called at any point.

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

<br/>

## Opening and Closing the Module

### AK_MPI_DEMUX_Open

&emsp;&emsp;【Description】

&emsp;&emsp;Opens the media demux library. When opening a video file, demuxing can optionally begin at a specified time. The parameter used is `start_ms` in `struct ak_demux_input`.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_DEMUX_Open(const DEMUX_CONF_S *pstDemuxConf, AK_S32 *s32DemuxHandleId);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**            | **Value range**        | **Input/Output** |
| ------------------ | ------------------------- | ------------------------- | ------------------- |
| pstDemuxConf        | Demux library input parameters            | See `struct akDEMUX_CONF_S` | Input                  |
| s32DemuxHandleId    | Handle ID returned when the media demux library is opened | 0~3                       | Output                 |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0                | Success           |
| Other             | See the error codes.   |

&emsp;&emsp;【Error Codes】

| **Error code**               | **Description**         |
| ------------------------------ | ---------------------- |
| ERROR_TYPE_INVALID_ARG         | Invalid parameter             |
| ERROR_TYPE_MALLOC_FAILED       | Malloc failed            |
| ERROR_TYPE_POINTER_NULL        | Null parameter               |
| ERROR_DEMUX_OPEN_LIB_ERROR     | Failed to open the demux library         |
| ERROR_DEMUX_GET_LIB_INFO_ERROR | Failed to obtain recording information       |
| ERROR_DEMUX_START_LIB_ERROR    | Failed to start demuxing           |
| ERROR_DEMUX_OPEN_TOO_MANY      | Too many users have opened the demux module |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_demux.so and libakmedia.so, or libmpi_demux.a and libakmedia.a

&emsp;&emsp;Header: ak_demux.h

&emsp;&emsp;【Call Sequence】

```c
    AK_MPI_DEMUX_Open(&demux_param, &s32DemuxHandleId);
    while(1){
	  AK_MPI_DEMUX_Get_Data(s32DemuxHandleId, &penDemuxDataType, &stream);
	  //Do something
	  AK_MPI_DEMUX_Free_Data(s32DemuxHandleId, &stream);
    }
    AK_MPI_DEMUX_Close(s32DemuxHandleId);
```

&emsp;&emsp;【Paired Interface】

&emsp;&emsp;`AK_MPI_DEMUX_Open` and `AK_MPI_DEMUX_Close` are used as a pair.

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

> **Note:** `AK_MPI_DEMUX_Open` can be called multiple times. Each open adds a new user, but at most 4 users can be open.

<br/>

### AK_MPI_DEMUX_Close

&emsp;&emsp;【Description】

&emsp;&emsp;Closes the media demux library.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_DEMUX_Close(AK_S32 s32DemuxHandleId);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**            | **Value range** | **Input/Output** |
| ------------------ | ------------------------- | ------------------ | ------------------- |
| s32DemuxHandleId    | Handle ID returned when the media demux library is opened | 0~3                | Input                |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0                | Success           |
| Other             | See the error codes.   |

&emsp;&emsp;【Error Codes】

| **Error code**            | **Description** |
| --------------------------- | -------------- |
| ERROR_DEMUX_CLOSE_LIB_ERROR | Failed to close the demux library |
| ERROR_DEMUX_STOP_LIB_ERROR  | Failed to stop demuxing   |
| ERROR_DEMUX_USER_NULL       | Null user handle   |
| ERROR_DEMUX_LIB_HANDLE_NULL | Null demux library handle |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_demux.so and libakmedia.so, or libmpi_demux.a and libakmedia.a

&emsp;&emsp;Header: ak_demux.h

&emsp;&emsp;【Call Sequence】

```c
    AK_MPI_DEMUX_Open(&demux_param, &s32DemuxHandleId);
    while(1){
	  AK_MPI_DEMUX_Get_Data(s32DemuxHandleId, &penDemuxDataType, &stream);
	  //Do something
	  AK_MPI_DEMUX_Free_Data(s32DemuxHandleId, &stream);
    }
    AK_MPI_DEMUX_Close(s32DemuxHandleId);
```

&emsp;&emsp;【Paired Interface】

&emsp;&emsp;`AK_MPI_DEMUX_Open` and `AK_MPI_DEMUX_Close` are used as a pair.

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

> **Note:** `AK_MPI_DEMUX_Close` may be called multiple times. An error is reported for `s32DemuxHandleId` when closing a handle that does not exist.

<br/>

## Demux Operation Interfaces

### AK_MPI_DEMUX_Get_Total_Time

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the total duration of the file to demux, in ms.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_DEMUX_Get_Total_Time(AK_S32 s32DemuxHandleId, AK_U64 *u64TotalTimeMs);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**               | **Value range** | **Input/Output** |
| ------------------ | ---------------------------- | ------------------ | ------------------- |
| s32DemuxHandleId    | Handle ID returned when the media demux library is opened    | 0~3                | Input                  |
| u64TotalTimeMs      | Total duration of the file to demux, in ms | Non-null               | Output                 |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0                | Success           |
| Other             | See the error codes.   |

&emsp;&emsp;【Error Codes】

| **Error code**        | **Description** |
| ----------------------- | -------------- |
| ERROR_TYPE_POINTER_NULL | Null parameter       |
| ERROR_DEMUX_USER_NULL   | Null user handle   |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_demux.so and libakmedia.so, or libmpi_demux.a and libakmedia.a

&emsp;&emsp;Header: ak_demux.h

&emsp;&emsp;【Call Sequence】

```c
    AK_MPI_DEMUX_Open(&demux_param, &s32DemuxHandleId);
    AK_S32 AK_MPI_DEMUX_Get_Total_Time(AK_S32 s32DemuxHandleId, AK_U64 *u64TotalTimeMs);
    AK_MPI_DEMUX_Close(s32DemuxHandleId);
```

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

<br/>

### AK_MPI_DEMUX_Get_Video_Info

&emsp;&emsp;【Description】

&emsp;&emsp;Gets video information for the file to demux.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_DEMUX_Get_Video_Info(AK_S32 s32DemuxHandleId, DEMUX_VIDEO_INFO_S *pstDemuxVideoInfo);

```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**            | **Value range**                    | **Input/Output** |
| ------------------ | ------------------------- | ------------------------------------- | ------------------- |
| s32DemuxHandleId    | Handle ID returned when the media demux library is opened | 0~3                                   | Input                  |
| pstDemuxVideoInfo   | Video information for the file to demux    | See `struct akDEMUX_VIDEO_INFO_S` | Output                 |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0                | Success           |
| Other             | See the error codes.   |

&emsp;&emsp;【Error Codes】

| **Error code**             | **Description** |
| ---------------------------- | -------------- |
| ERROR_TYPE_POINTER_NULL      | Null parameter       |
| ERROR_DEMUX_USER_NULL        | Null user handle   |
| ERROR_DEMUX_VIDEO_TYPE_ERROR | Invalid video type   |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_demux.so and libakmedia.so, or libmpi_demux.a and libakmedia.a

&emsp;&emsp;Header: ak_demux.h

&emsp;&emsp;【Call Sequence】

```c
    AK_MPI_DEMUX_Open(&demux_param, &s32DemuxHandleId);
    AK_MPI_DEMUX_Free_Data_Info(s32DemuxHandleId, &pstDemuxVideoInfo);
    AK_MPI_DEMUX_Close(s32DemuxHandleId);
```

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

<br/>

### AK_MPI_DEMUX_Get_Audio_Info

&emsp;&emsp;【Description】

&emsp;&emsp;Gets audio information for the file to demux.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_DEMUX_Get_Audio_Info(AK_S32 s32DemuxHandleId, DEMUX_AUDIO_INFO_S *pstDemuxAudioInfo);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**            | **Value range**                    | **Input/Output** |
| ------------------ | ------------------------- | ------------------------------------- | ------------------- |
| s32DemuxHandleId    | Handle ID returned when the media demux library is opened | 0~3                                   | Input                  |
| pstDemuxAudioInfo   | Audio information for the file to demux    | See `struct akDEMUX_AUDIO_INFO_S` | Output                 |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0                | Success           |
| Other             | See the error codes.   |

&emsp;&emsp;【Error Codes】

| **Error code**             | **Description** |
| ---------------------------- | -------------- |
| ERROR_TYPE_POINTER_NULL      | Null parameter       |
| ERROR_DEMUX_USER_NULL        | Null user handle   |
| ERROR_DEMUX_LIB_HANDLE_NULL  | Null demux library handle |
| ERROR_DEMUX_AUDIO_TYPE_ERROR | Invalid audio type   |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_demux.so and libakmedia.so, or libmpi_demux.a and libakmedia.a

&emsp;&emsp;Header: ak_demux.h

&emsp;&emsp;【Call Sequence】

```c
    AK_MPI_DEMUX_Open(&demux_param, &s32DemuxHandleId);
    AK_MPI_DEMUX_Get_Audio_Info(s32DemuxHandleId, &pstDemuxAudioInfo);
    AK_MPI_DEMUX_Close(s32DemuxHandleId);
```

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

<br/>

### AK_MPI_DEMUX_Get_Data

&emsp;&emsp;【Description】

&emsp;&emsp;Gets demuxed data. If the output `penDemuxDataType` is a video type, the retrieved frame contains video data. If the output `penDemuxDataType` is an audio type, the retrieved frame contains audio data.

&emsp;&emsp;This interface applies an internal policy that retains the previous audio-frame timestamp and previous video-frame timestamp. If the previous audio timestamp is greater than the previous video timestamp, it obtains the video timestamp first. Conversely, if the previous video timestamp is greater than the previous audio timestamp, it obtains the audio timestamp first.

&emsp;&emsp;The policy flowchart is shown in Figure 3-1:

![Figure 3-1 Demux audio/video timestamp-selection policy flowchart](../../../../zh_CN/software/board/middleware-api/img/demux-av-sync-strategy.png)

> **Figure note:** The shared source figure contains Chinese labels. It illustrates the timestamp-comparison policy described above.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_DEMUX_Get_Data(AK_S32 s32DemuxHandleId, DEMUX_DATA_TYPE_E *penDemuxDataType, DEMUX_STREAM_S *pstDemuxStream);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**            | **Value range**          | **Input/Output** |
| ------------------ | ------------------------- | --------------------------- | ------------------- |
| s32DemuxHandleId    | Handle ID returned when the media demux library is opened | 0~3                         | Input                  |
| penDemuxDataType               | Type of the demuxed data    | See `enum akDEMUX_DATA_TYPE_E` | Output                 |
| pstDemuxStream       | Demuxed data              | See `struct akDEMUX_STREAM_S`  | Output                 |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0                | Success           |
| Other             | See the error codes.   |

&emsp;&emsp;【Error Codes】

| **Error code**            | **Description** |
| --------------------------- | -------------- |
| ERROR_TYPE_POINTER_NULL     | Null parameter       |
| ERROR_TYPE_MALLOC_FAILED    | Malloc failed    |
| ERROR_DEMUX_USER_NULL       | Null user handle   |
| ERROR_DEMUX_LIB_HANDLE_NULL | Null demux library handle |
| ERROR_DEMUX_AUDIO_END       | End of demuxed audio   |
| ERROR_DEMUX_VIDEO_END       | End of demuxed video   |
| ERROR_DEMUX_LIB_ERROR       | Demux error       |
| ERROR_DEMUX_NO_AUDIO        | No audio data   |
| ERROR_DEMUX_NO_VIDEO        | No video data   |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_demux.so and libakmedia.so, or libmpi_demux.a and libakmedia.a

&emsp;&emsp;Header: ak_demux.h

&emsp;&emsp;【Call Sequence】

```c
    AK_MPI_DEMUX_Open(&demux_param, &s32DemuxHandleId);
    while(1){
	  AK_MPI_DEMUX_Get_Data(s32DemuxHandleId, &penDemuxDataType, &stream);
	  //Do something
	  AK_MPI_DEMUX_Free_Data(s32DemuxHandleId, &stream);
    }
    AK_MPI_DEMUX_Close(s32DemuxHandleId);
```

&emsp;&emsp;【Paired Interface】

&emsp;&emsp;`AK_MPI_DEMUX_Get_Data` and `AK_MPI_DEMUX_Free_Data` are used as a pair.

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The interface is reentrant.

<br/>

### AK_MPI_DEMUX_Free_Data

> **Source note:** The source duplicates and mislabels this section as `AK_MPI_DEMUX_Free_Data`; its description and call sequence concern video retrieval. Use `AK_MPI_DEMUX_Get_Video` to retrieve video and the later `AK_MPI_DEMUX_Free_Data` interface to release retrieved data. The source's lowercase `ak_demux_get_video` likewise maps to the declared `AK_MPI_DEMUX_Get_Video`.

&emsp;&emsp;【Description】

&emsp;&emsp;Gets demuxed video data.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_DEMUX_Free_Data(AK_S32 s32DemuxHandleId, DEMUX_STREAM_S *pstDemuxStream);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**            | **Value range**         | **Input/Output** |
| ------------------ | ------------------------- | -------------------------- | ------------------- |
| s32DemuxHandleId    | Handle ID returned when the media demux library is opened | 0~3                        | Input                  |
| pstDemuxStream       | Demuxed video data          | See `struct akDEMUX_STREAM_S` | Output                 |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0                | Success           |
| Other             | See the error codes.   |

&emsp;&emsp;【Error Codes】

| **Error code**            | **Description** |
| --------------------------- | -------------- |
| ERROR_TYPE_POINTER_NULL     | Null parameter       |
| ERROR_TYPE_MALLOC_FAILED    | Malloc failed    |
| ERROR_DEMUX_USER_NULL       | Null user handle   |
| ERROR_DEMUX_LIB_HANDLE_NULL | Null demux library handle |
| ERROR_DEMUX_VIDEO_END       | End of demuxed video   |
| ERROR_DEMUX_LIB_ERROR       | Demux error       |
| ERROR_DEMUX_NO_VIDEO        | No video data   |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_demux.so and libakmedia.so, or libmpi_demux.a and libakmedia.a

&emsp;&emsp;Header: ak_demux.h

&emsp;&emsp;【Call Sequence】

```c
    AK_MPI_DEMUX_Open(&demux_param, &s32DemuxHandleId);
    while(1){
      AK_MPI_DEMUX_Get_Video(s32DemuxHandleId, &video_stream);
	  //Do something
	  AK_MPI_DEMUX_Free_Data(s32DemuxHandleId, &video_stream);
	  AK_MPI_DEMUX_Get_Audio(s32DemuxHandleId, &audio_stream);
      //Do something
	  AK_MPI_DEMUX_Free_Data(s32DemuxHandleId, &audio_stream);
    }
    AK_MPI_DEMUX_Close(s32DemuxHandleId);
```

&emsp;&emsp;【Paired Interface】

&emsp;&emsp;`AK_MPI_DEMUX_Get_Data` and `AK_MPI_DEMUX_Free_Data` are used as a pair.

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The interface is reentrant.

<br/>

### AK_MPI_DEMUX_Get_Audio

&emsp;&emsp;【Description】

&emsp;&emsp;Gets demuxed audio data.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_DEMUX_Get_Audio(AK_S32 s32DemuxHandleId, DEMUX_STREAM_S *pstDemuxStream);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**            | **Value range**         | **Input/Output** |
| ------------------ | ------------------------- | -------------------------- | ------------------- |
| s32DemuxHandleId    | Handle ID returned when the media demux library is opened | 0~3                        | Input                |
| pstDemuxStream       | Demuxed audio data          | See `struct akDEMUX_STREAM_S` | Output                 |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0                | Success           |
| Other             | See the error codes.   |

&emsp;&emsp;【Error Codes】

| **Error code**            | **Description** |
| --------------------------- | -------------- |
| ERROR_TYPE_POINTER_NULL     | Null parameter       |
| ERROR_TYPE_MALLOC_FAILED    | Malloc failed    |
| ERROR_DEMUX_USER_NULL       | Null user handle   |
| ERROR_DEMUX_LIB_HANDLE_NULL | Null demux library handle |
| ERROR_DEMUX_AUDIO_END       | End of demuxed audio   |
| ERROR_DEMUX_LIB_ERROR       | Demux error       |
| ERROR_DEMUX_NO_AUDIO        | No audio data   |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_demux.so and libakmedia.so, or libmpi_demux.a and libakmedia.a

&emsp;&emsp;Header: ak_demux.h

&emsp;&emsp;【Call Sequence】

```c
    AK_MPI_DEMUX_Open(&demux_param, &s32DemuxHandleId);
    while(1){
      AK_MPI_DEMUX_Get_Video(s32DemuxHandleId, &video_stream);
	  //Do something
	  AK_MPI_DEMUX_Free_Data(s32DemuxHandleId, &video_stream);
	  AK_MPI_DEMUX_Get_Audio(s32DemuxHandleId, &audio_stream);
      //Do something
	  AK_MPI_DEMUX_Free_Data(s32DemuxHandleId, &audio_stream);
    }
    AK_MPI_DEMUX_Close(s32DemuxHandleId);
```

&emsp;&emsp;【Paired Interface】

&emsp;&emsp;`AK_MPI_DEMUX_Get_Audio` and `AK_MPI_DEMUX_Free_Data` are used as a pair.

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The interface is reentrant.

<br/>

### AK_MPI_DEMUX_Free_Data

&emsp;&emsp;【Description】

&emsp;&emsp;Frees retrieved data. This interface is used with `AK_MPI_DEMUX_Get_Data`, `AK_MPI_DEMUX_Get_Video`, or `AK_MPI_DEMUX_Get_Audio`.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_DEMUX_Free_Data(AK_S32 s32DemuxHandleId, DEMUX_STREAM_S *pstDemuxStream);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**            | **Value range**         | **Input/Output** |
| ------------------ | ------------------------- | -------------------------- | ------------------- |
| s32DemuxHandleId    | Handle ID returned when the media demux library is opened | 0~3                        | Input                |
| pstDemuxStream             | Demuxed data              | See `struct akDEMUX_STREAM_S` | Input                |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0                | Success           |
| Other             | See the error codes.   |

&emsp;&emsp;【Error Codes】

| **Error code**            | **Description** |
| --------------------------- | -------------- |
| ERROR_TYPE_POINTER_NULL     | Null parameter       |
| ERROR_DEMUX_USER_NULL       | Null user handle   |
| ERROR_DEMUX_LIB_HANDLE_NULL | Null demux library handle |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_demux.so and libakmedia.so, or libmpi_demux.a and libakmedia.a

&emsp;&emsp;Header: ak_demux.h

&emsp;&emsp;【Call Sequence】

```c
    AK_MPI_DEMUX_Open(&demux_param, &s32DemuxHandleId);
    while(1){
	  AK_MPI_DEMUX_Get_Data(s32DemuxHandleId, &penDemuxDataType, &stream);
	  //Do something
	  AK_MPI_DEMUX_Free_Data(s32DemuxHandleId, &stream);
    }
    AK_MPI_DEMUX_Close(s32DemuxHandleId);
```

```c
    AK_MPI_DEMUX_Open(&demux_param, &s32DemuxHandleId);
    while(1){
      AK_MPI_DEMUX_Get_Video(s32DemuxHandleId, &video_stream);
	  //Do something
	  AK_MPI_DEMUX_Free_Data(s32DemuxHandleId, &video_stream);
	  AK_MPI_DEMUX_Get_Audio(s32DemuxHandleId, &audio_stream);
      //Do something
	  AK_MPI_DEMUX_Free_Data(s32DemuxHandleId, &audio_stream);
    }
    AK_MPI_DEMUX_Close(s32DemuxHandleId);
```

&emsp;&emsp;【Paired Interface】

&emsp;&emsp;`AK_MPI_DEMUX_Get_Data` and `AK_MPI_DEMUX_Free_Data` are used as a pair.

&emsp;&emsp;Alternatively, `ak_demux_get_video` and `AK_MPI_DEMUX_Free_Data` are used as a pair.

&emsp;&emsp;Alternatively, `AK_MPI_DEMUX_Get_Audio` and `AK_MPI_DEMUX_Free_Data` are used as a pair.

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The interface is reentrant.

<br/>

### AK_MPI_DEMUX_Seek_To_Keyframe

&emsp;&emsp;【Description】

&emsp;&emsp;Seeks to a specified position for demuxing. Because demuxing after a seek must begin at an I-frame, both the target time and the direction in which the demux library searches for an I-frame must be specified.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_DEMUX_Seek_To_Keyframe(AK_S32 s32DemuxHandleId, AK_U64 u64Ms,
                                        DEMUX_DIRECTION_E enDemuxDirection);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**                                               | **Value range**          | **Input/Output** |
| ------------------ | ------------------------------------------------------------ | --------------------------- | ------------------- |
| s32DemuxHandleId    | Handle ID returned when the media demux library is opened                                    | 0~3                         | Input                |
| u64Ms                 | Time interval from the current demux timestamp to the target timestamp, in ms  | >0                          | Input                |
| enDemuxDirection             | Seek direction, either forward or backward. Together with the `ms` parameter, this means seeking forward by `ms`, or seeking backward to `ms`, and then starting demuxing. | See `enum DEMUX_DIRECTION_E` | Input                |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0                | Success           |
| Other             | See the error codes.   |

&emsp;&emsp;【Error Codes】

| **Error code**            | **Description** |
| --------------------------- | -------------- |
| ERROR_TYPE_INVALID_ARG      | Invalid parameter     |
| ERROR_TYPE_MALLOC_FAILED    | Malloc failed    |
| ERROR_TYPE_POINTER_NULL     | Null parameter       |
| ERROR_DEMUX_USER_NULL       | Null user handle   |
| ERROR_DEMUX_LIB_HANDLE_NULL | Null demux library handle |
| ERROR_DEMUX_LIB_ERROR       | Demux error       |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_demux.so and libakmedia.so, or libmpi_demux.a and libakmedia.a

&emsp;&emsp;Header: ak_demux.h

&emsp;&emsp;【Call Sequence】

```c
    AK_MPI_DEMUX_Open(&demux_param, &s32DemuxHandleId);
    AK_MPI_DEMUX_Seek_To_Keyframe(s32DemuxHandleId, ms, DEMUX_DIRECTION_LAST);
    while(1){
	  AK_MPI_DEMUX_Get_Data(s32DemuxHandleId, &penDemuxDataType, &stream);
	  //Do something
	  AK_MPI_DEMUX_Free_Data(s32DemuxHandleId, &stream);
    }
    AK_MPI_DEMUX_Close(s32DemuxHandleId);
```

```c
    AK_MPI_DEMUX_Open(&demux_param, &s32DemuxHandleId);
    AK_MPI_DEMUX_Seek_To_Keyframe(s32DemuxHandleId, ms, DEMUX_DIRECTION_LAST);
    while(1){
      AK_MPI_DEMUX_Get_Video(s32DemuxHandleId, &video_stream);
	  //Do something
	  AK_MPI_DEMUX_Free_Data(s32DemuxHandleId, &video_stream);
	  AK_MPI_DEMUX_Get_Audio(s32DemuxHandleId, &audio_stream);
      //Do something
	  AK_MPI_DEMUX_Free_Data(s32DemuxHandleId, &audio_stream);
    }
    AK_MPI_DEMUX_Close(s32DemuxHandleId);
```

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The interface is reentrant.

<br/>

## Interface Call Dependencies

&emsp;&emsp;The public interface functions provided by the DEMUX module have the call dependencies shown in the following table:

| **Interface**            | **Call dependency**                                       |
| ------------------------- | ------------------------------------------------------------ |
| AK_MPI_DEMUX_Get_Version      | No dependency                                                       |
| AK_MPI_DEMUX_Open             | Called at the beginning                                                   |
| AK_MPI_DEMUX_Get_Total_Time   | Called after `AK_MPI_DEMUX_Open`                                        |
| AK_MPI_DEMUX_Free_Data_Info   | Called after `AK_MPI_DEMUX_Open`                          |
| AK_MPI_DEMUX_Get_Audio_Info   | Called after `AK_MPI_DEMUX_Open`                          |
| AK_MPI_DEMUX_Seek_To_Keyframe | Called after `AK_MPI_DEMUX_Open`                          |
| AK_MPI_DEMUX_Get_Data         | Called after `AK_MPI_DEMUX_Open`                                        |
| AK_MPI_DEMUX_Get_Video        | Called after `AK_MPI_DEMUX_Open`                                        |
| AK_MPI_DEMUX_Get_Audio        | Called after `AK_MPI_DEMUX_Open`                                        |
| AK_MPI_DEMUX_Free_Data        | Called after `AK_MPI_DEMUX_Get_Data`, `ak_demux_get_video`, or `AK_MPI_DEMUX_Get_Audio` |
| AK_MPI_DEMUX_Close            | Called after `AK_MPI_DEMUX_Open`                                          |

<br/>

## ak_demux_sample Usage Example

| **Input parameter**   | **Description**                                             |
| -------------- | ----------------------------------------------------------- |
| path           | Path in which to save the demuxed audio and video files                           |
| file           | Full path of the file to demux                                          |
| skip-serial    | When the decoded video file is intended for playback in a media player, skips the serial number and timestamp when writing the file |
| offset-ms    | Offset used when reading the file (ms) |

<br/>

## Error Codes

| Error code   | Macro                         | Meaning             |
| ---------- | ------------------------------ | ---------------- |
| 0x13000000 | DEMUX_ERROR_OPEN_LIB_ERROR     | Failed to open the library       |
| 0x13000001 | DEMUX_ERROR_CLOSE_LIB_ERROR    | Failed to close the library       |
| 0x13000002 | DEMUX_ERROR_GET_LIB_INFO_ERROR | Failed to get library information   |
| 0x13000003 | DEMUX_ERROR_START_LIB_ERROR    | Failed to start the library       |
| 0x13000004 | DEMUX_ERROR_STOP_LIB_ERROR     | Failed to stop the library       |
| 0x13000005 | DEMUX_ERROR_OPEN_TOO_MANY      | Too many opens     |
| 0x13000006 | DEMUX_ERROR_USER_NULL          | Null user         |
| 0x13000007 | DEMUX_ERROR_LIB_HANDLE_NULL    | Null library handle       |
| 0x13000008 | DEMUX_ERROR_AUDIO_TYPE_ERROR   | Invalid audio type     |
| 0x13000009 | DEMUX_ERROR_VIDEO_TYPE_ERROR   | Invalid video type     |
| 0x1300000a | DEMUX_ERROR_AUDIO_END          | End of demuxed audio     |
| 0x1300000b | DEMUX_ERROR_VIDEO_END          | End of demuxed video     |
| 0x1300000c | DEMUX_ERROR_LIB_ERROR          | Demux error         |
| 0x1300000d | DEMUX_ERROR_NO_AUDIO           | No audio data     |
| 0x1300000e | DEMUX_ERROR_NO_VIDEO           | No video data     |
| 0x1300000f | DEMUX_ERROR_SRC_EOF            | End of demux source file |

<br/>
