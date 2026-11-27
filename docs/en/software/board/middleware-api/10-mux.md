# Multiplexing

## Overview

&emsp;&emsp;The multiplexing module (MUX module) combines audio-stream data and video-stream data (H264/H265/JPEG) into recorded data in MP4 or AVI format.

* **The supported combinations of audio and video formats for MP4 and AVI files are as follows:**

| File type | Video format      | Audio format               |
| ---- | -------------- | ---------------------- |
| MP4  | H264/H265      | AMR, AAC, g711a/u      |
| AVI  | H264/H265/JPEG | MP3, AAC, g711a/u, PCM |

<br/>

## API Reference

&emsp;&emsp;This module provides the following APIs.

| **Data structure** | **Description**                     |
| ----------------- | ------------------------------- |
| MUX_CONF_S        | Input parameters for media multiplexing |
| MUX_START_PARAM_S | Parameters supplied when media multiplexing starts |
| MUX_FILEINFO_S    | Video information returned after repairing a multiplexed video file |
| MUX_STATUS_E      | Status values returned by `ak_mux_get_status` while recording |
| MUX_NODE_E        | File types for files produced while recording |

<br/>

| **Function**                        | **Description**      |
| ------------------------------- | ------------------ |
| AK_MPI_MUX_Get_Version          | Prints the multiplexing-module version |
| AK_MPI_MUX_Open                 | Opens the media multiplexing library |
| AK_MPI_MUX_Close                | Closes the media multiplexing library |
| AK_MPI_MUX_Start                | Starts multiplexing; call for each new recording |
| AK_MPI_MUX_Stop                 | Stops multiplexing |
| AK_MPI_MUX_Add_Audio            | Adds audio for multiplexing |
| AK_MPI_MUX_Add_Video            | Adds video for multiplexing |
| AK_MPI_MUX_Print_Runtime_Status | Prints MUX-module debug information |
| AK_MPI_MUX_Fix_File             | Repairs a video file |
| AK_MPI_MUX_Pause                | Pauses multiplexing |
| AK_MPI_MUX_Continue             | Continues multiplexing |
| AK_MPI_MUX_Get_Status           | Gets the current multiplexing-library status |

<br/>

## Data Structures

### MUX_CONF_S

&emsp;&emsp;【Description】

&emsp;&emsp;Input parameters for media multiplexing.

&emsp;&emsp;【Definition】

```c
    typedef struct akMUX_CONF_S
    {
        /* video */
        VENC_OUTPUT_TYPE_E enVencOutputType;
        AK_U16 u16Width;
        AK_U16 u16Height;
        AK_U16 u16Fps;

        /* audio */
        AK_U8 u8CaptureAudio;
        enAudioType_E enAudioType;
        AUDIO_DATA_ATTR_S stAudioDataAttr;
        AK_S32 s32FrameLen;

        /* mux */
        MUX_TYPE_E enMuxType;
        MUX_DATA_DEST_E enMuxDataDest;
        AK_U32 u32RecordSec;
    }MUX_CONF_S;
```

&emsp;&emsp;【Members】

| **Member**         | **Description**                          |
| ---------------- | ------------------------------------ |
| enVencOutputType | Video type; see the definition of `VENC_OUTPUT_TYPE_E` |
| u16Width         | Image width |
| u16Height        | Image height |
| u16Fps           | Image frame rate |
| u8CaptureAudio   | Whether to multiplex audio; 0: do not multiplex audio, 1: multiplex audio |
| enAudioType      | Audio type; see `enum ak_enAudioType` |
| stAudioDataAttr  | Audio attributes; see `struct ak_audio_data_attr` |
| s32FrameLen      | Audio-data frame length |
| enMuxType        | Type of the multiplexed video file |
| enMuxDataDest    | Storage type for the multiplexed video file |
| u32RecordSec     | Duration of the multiplexed video file |
| <br/>            |                                      |

### MUX_START_PARAM_S

&emsp;&emsp;【Description】

&emsp;&emsp;Parameters supplied when media multiplexing starts.

&emsp;&emsp;【Definition】

```c
    typedef struct akMUX_START_PARAM_S
    {
        AK_S8 *ps8FilePath;
        AK_S32 s32BuffRecord;
        AK_S8 *ps8BuffRecord;
        AK_S32 s32BuffIndex;
        AK_S8 *ps8BuffIndex;
    }MUX_START_PARAM_S;
```

&emsp;&emsp;【Members】

| **Member**      | **Description**       |
| ------------- | ----------------- |
| ps8FilePath   | Full path of the recording file, including its path and file name |
| s32BuffRecord | Length of the buffer to which recording content is written |
| ps8BuffRecord | Address of the buffer to which recording content is written |
| s32BuffIndex  | Length of the buffer to which the recording index is written |
| ps8BuffIndex  | Address of the buffer to which the recording index is written |

<br/>

> **Note:** Pass the full file path in `ps8FilePath`. The user does not need to create the file; the MUX library creates the recording file.

<br/>

### MUX_FILEINFO_S

&emsp;&emsp;【Description】

&emsp;&emsp;Video information returned after a multiplexed video file is repaired.

&emsp;&emsp;【Definition】

```c
    typedef struct akMUX_FILEINFO_S
    {
        AK_U64 u64TotalMs ;
    }MUX_FILEINFO_S;
```

&emsp;&emsp;【Members】

| **Member**   | **Description** |
| ---------- | ---------- |
| u64TotalMs | Duration of the repaired recording file |

<br/>

### MUX_STATUS_E

&emsp;&emsp;【Description】

&emsp;&emsp;Status values returned by `ak_mux_get_status` while recording.

If the returned status is one of the following values:

MUX_STATUS_SYSERR
MUX_STATUS_MEMFULL
MUX_STATUS_SYNERR

the current multiplexing library cannot recover. Close the current recording file and start a new recording.

&emsp;&emsp;【Definition】

```c
typedef enum akMUX_STATUS_E
{
    MUX_STATUS_OPEN,
    MUX_STATUS_STOP,
    MUX_STATUS_DOING,
    MUX_STATUS_SYSERR,
    MUX_STATUS_MEMFULL,
    MUX_STATUS_SYNERR,
    MUX_STATUS_WAITING,
    MUX_STATUS_PAUSE,
    MUX_STATUS_NUM,
}MUX_STATUS_E;
```

&emsp;&emsp;【Members】

| **Member**           | **Description**                                                    |
| ------------------ | -------------------------------------------------------------- |
| MUX_STATUS_OPEN    | Media-library state after `AK_MPI_MUX_Start` is called but before recording starts; the library is open. |
| MUX_STATUS_STOP    | Media-library state after `AK_MPI_MUX_Stop` is called; the library is stopped. |
| MUX_STATUS_DOING   | Normal media-library state during multiplexing after `AK_MPI_MUX_Start` is called. |
| MUX_STATUS_SYSERR  | Media-library error state; this is generally returned when an error occurs during multiplexing. |
| MUX_STATUS_MEMFULL | Reported when, for example, `malloc` fails during multiplexing or the multiplexed media file exceeds the size limit. |
| MUX_STATUS_SYNERR  | Media-library resynchronization-failure state. |
| MUX_STATUS_WAITING | Media-library waiting state. |
| MUX_STATUS_PAUSE   | Media-library state after `ak_mux_pause` is called; the library is paused. To continue multiplexing after a pause, call `ak_mux_continue`. |
| MUX_STATUS_NUM     | Number of multiplexing-library states |

<br/>

### MUX_NODE_E

&emsp;&emsp;【Description】

&emsp;&emsp;File types for files produced while recording.

&emsp;&emsp;【Definition】

```c
    typedef enum akMUX_NODE_E {
        MUX_NODE_RECORD = 0x00,
        MUX_NODE_IDX,
        MUX_NODE_MP4_MOOV,
        MUX_NODE_MP4_STBL,
        MUX_NODE_NUM
    }MUX_NODE_E;
```

&emsp;&emsp;【Members】

| **Member**          | **Description**        |
| ----------------- | ------------------ |
| MUX_NODE_RECORD   | Recording-file content writes |
| MUX_NODE_IDX      | Recording-index information writes |
| MUX_NODE_MP4_MOOV | MOOV-information writes for an MP4 recording |
| MUX_NODE_MP4_STBL | STBL-information writes for an MP4 recording |
| MUX_NODE_NUM      | Number of file types produced during recording |

<br/>

## Get Version Information

### AK_MPI_MUX_Get_Version

&emsp;&emsp;【Description】

&emsp;&emsp;Prints the multiplexing-module version number.

&emsp;&emsp;【Syntax】

```c
    const AK_S8* AK_MPI_MUX_Get_Version(AK_VOID);
```

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ------- | ------ |
| Multiplexing-module version number | Success |
| NULL    | Failure  |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_mux.so and libakmedia.so, or libmpi_mux.a and libakmedia.a

&emsp;&emsp;Header: ak_mux.h

&emsp;&emsp;【Call order】

&emsp;&emsp;May be called at any point.

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

<br/>

## Open/Close the Module

### AK_MPI_MUX_Open

&emsp;&emsp;【Description】

&emsp;&emsp;Opens the media multiplexing library.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_MUX_Open(const MUX_CONF_S *pstMuxParam, AK_S32 *s32MuxHandleId);
```

&emsp;&emsp;【Parameters】

| **Parameter**       | **Description**      | **Value range**           | **Input/Output** |
| -------------- | ------------------- | --------------------- | --------- |
| pstMuxParam    | Multiplexing-library input parameters | See `struct akMUX_CONF_S` | Input |
| s32MuxHandleId | Handle ID returned when the media multiplexing library is opened | 0~3 | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ------- | ------ |
| 0       | Success |
| Other   | See the error codes |

&emsp;&emsp;【Error codes】

| **Error code**                     | **Description** |
| ------------------------------- | --------- |
| ERROR_TYPE_INVALID_ARG          | Invalid argument |
| ERROR_TYPE_MALLOC_FAILED        | `malloc` failed |
| ERROR_TYPE_POINTER_NULL         | Null argument |
| ERROR_MUX_OPEN_TOO_MANY         | Too many users |
| ERROR_MUX_SET_AUDIO_INPUT_ERROR | Invalid audio-multiplexing parameters |
| ERROR_MUX_SET_VIDEO_INPUT_ERROR | Invalid video-multiplexing parameters |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_mux.so and libakmedia.so, or libmpi_mux.a and libakmedia.a

&emsp;&emsp;Header: ak_mux.h

&emsp;&emsp;【Call order】

```c
    AK_MPI_MUX_Open(pstMuxParam, s32MuxHandleId);
    AK_MPI_MUX_Start( s32MuxHandleId, &stMuxStartParam );
    while(1){
        AK_MPI_MUX_Add_Video(s32MuxHandleId, video_stream);
        AK_MPI_MUX_Add_Audio(s32MuxHandleId, audio_stream);
    }
    AK_MPI_MUX_Stop(s32MuxHandleId);
    AK_MPI_MUX_Close(s32MuxHandleId);
```

&emsp;&emsp;【Paired APIs】

```c
    int AK_MPI_MUX_Close(int s32MuxHandleId);
```

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;`AK_MPI_MUX_Open` may be called multiple times. Each open operation adds a new user, up to a maximum of four users.

<br/>

### AK_MPI_MUX_Close

&emsp;&emsp;【Description】

&emsp;&emsp;Closes the media multiplexing library.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_MUX_Close(AK_S32 s32MuxHandleId);
```

&emsp;&emsp;【Parameters】

| **Parameter**       | **Description**      | **Value range** | **Input/Output** |
| -------------- | ------------------- | -------- | --------- |
| s32MuxHandleId | Handle ID returned when the media multiplexing library is opened | 0~3 | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ------- | ------ |
| 0 | Success |
| Other | See the error codes |

&emsp;&emsp;【Error codes】

| **Error code**         | **Description** |
| ------------------- | ------ |
| ERROR_MUX_USER_NULL | Null user pointer |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_mux.so and libakmedia.so, or libmpi_mux.a and libakmedia.a

&emsp;&emsp;Header: ak_mux.h

&emsp;&emsp;【Call order】

```c
    AK_MPI_MUX_Open(pstMuxParam, s32MuxHandleId);
    AK_MPI_MUX_Start(s32MuxHandleId, pstStartParam);
    while(1){
        AK_MPI_MUX_Add_Video(s32MuxHandleId, video_stream);
        AK_MPI_MUX_Add_Audio(s32MuxHandleId, audio_stream);
    }
    AK_MPI_MUX_Stop(s32MuxHandleId);
    AK_MPI_MUX_Close(s32MuxHandleId);
```

&emsp;&emsp;【Paired APIs】

```c
    int AK_MPI_MUX_Open(const struct akMUX_CONF_S *pstMuxParam, int *s32MuxHandleId);
```

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;`AK_MPI_MUX_Close` may be called multiple times. Closing a nonexistent `mux_handle_id` returns an error.

<br/>

## Multiplexing APIs

### AK_MPI_MUX_Start

&emsp;&emsp;【Description】

&emsp;&emsp;Starts multiplexing. Call this API each time a new recording begins.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_MUX_Start(AK_S32 s32MuxHandleId, MUX_START_PARAM_S *pstStartParam);
```

&emsp;&emsp;【Parameters】

| **Parameter**       | **Description**      | **Value range**              | **Input/Output** |
| -------------- | ------------------- | ------------------------ | --------- |
| s32MuxHandleId | Handle ID returned when the media multiplexing library is opened | 0~3 | Input |
| pstStartParam  | Input parameters for starting the multiplexing path | See the `akMUX_START_PARAM_S` structure | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ------- | ------- |
| 0       | Success   |
| Other   | See the error codes. |

&emsp;&emsp;【Error codes】

| **Error code**                  | **Description** |
| ---------------------------- | --------- |
| ERROR_TYPE_INVALID_ARG       | Invalid argument |
| ERROR_TYPE_MALLOC_FAILED     | `malloc` failed |
| ERROR_TYPE_POINTER_NULL      | Null argument |
| ERROR_MUX_OPEN_LIB_ERROR     | Failed to open the multiplexing library |
| ERROR_MUX_GET_LIB_INFO_ERROR | Failed to get multiplexing-library information |
| ERROR_MUX_START_LIB_ERROR    | Failed to start multiplexing |
| ERROR_MUX_USER_NULL          | Null user pointer |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_mux.so and libakmedia.so, or libmpi_mux.a and libakmedia.a

&emsp;&emsp;Header: ak_mux.h

&emsp;&emsp;【Call order】

```c
    AK_MPI_MUX_Open(pstMuxParam, s32MuxHandleId);
    AK_MPI_MUX_Start(s32MuxHandleId, pstStartParam);
    while(1){
        AK_MPI_MUX_Add_Video(s32MuxHandleId, video_stream);
        AK_MPI_MUX_Add_Audio(s32MuxHandleId, audio_stream);
    }
    AK_MPI_MUX_Stop(s32MuxHandleId);
    AK_MPI_MUX_Close(s32MuxHandleId);
```

&emsp;&emsp;【Paired APIs】

```c
    AK_S32 AK_MPI_MUX_Stop(AK_S32 s32MuxHandleId);
```

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The API is reentrant. Call `AK_MPI_MUX_Start` when each new recording begins and `AK_MPI_MUX_Stop` when recording finishes.

<br/>

### AK_MPI_MUX_Stop

&emsp;&emsp;【Description】

&emsp;&emsp;Stops multiplexing.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_MUX_Stop(AK_S32 s32MuxHandleId);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| -------------- | ------------------- | -------- | --------- |
| s32MuxHandleId | Handle ID returned when the media multiplexing library is opened | 0~3 | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ------- | ------ |
| 0 | Success |
| Other | See the error codes |

&emsp;&emsp;【Error codes】

| **Error code**               | **Description** |
| ------------------------- | ------- |
| ERROR_MUX_CLOSE_LIB_ERROR | Failed to close the multiplexing library |
| ERROR_MUX_STOP_LIB_ERROR  | Failed to stop multiplexing |
| ERROR_MUX_USER_NULL       | Null user pointer |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_mux.so and libakmedia.so, or libmpi_mux.a and libakmedia.a

&emsp;&emsp;Header: ak_mux.h

&emsp;&emsp;【Call order】

```c
    AK_MPI_MUX_Open(pstMuxParam, s32MuxHandleId);
    AK_MPI_MUX_Start(s32MuxHandleId, pstStartParam);
    while(1){
        AK_MPI_MUX_Add_Video(s32MuxHandleId, video_stream);
        AK_MPI_MUX_Add_Audio(s32MuxHandleId, audio_stream);
    }
    AK_MPI_MUX_Stop(s32MuxHandleId);
    AK_MPI_MUX_Close(s32MuxHandleId);
```

&emsp;&emsp;【Paired APIs】

```c
    AK_S32 AK_MPI_MUX_Start(AK_S32 s32MuxHandleId, MUX_START_PARAM_S *pstStartParam);
```

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The API is reentrant. Call `AK_MPI_MUX_Start` when each new recording begins and `AK_MPI_MUX_Stop` when recording finishes.

<br/>

### AK_MPI_MUX_Add_Audio

&emsp;&emsp;【Description】

&emsp;&emsp;Adds audio to the multiplexed output.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_MUX_Add_Audio(AK_S32 s32MuxHandleId, const AUDIO_STREAM_S *pstAudioStream);
```

&emsp;&emsp;【Parameters】

| **Parameter**       | **Description**      | **Value range**         | **Input/Output** |
| -------------- | ------------------- | ------------------- | --------- |
| s32MuxHandleId | Handle ID returned when the media multiplexing library is opened | 0~3 | Input |
| pstAudioStream | Audio-stream data | See the `AUDIO_STREAM_S` structure | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ------- | ------ |
| 0       | Success |
| Other   | See the error codes |

&emsp;&emsp;【Error codes】

| **Error code**                     | **Description** |
| ------------------------------- | --------- |
| ERROR_TYPE_INVALID_ARG          | Invalid argument |
| ERROR_TYPE_POINTER_NULL         | Null argument |
| ERROR_MUX_USER_NULL             | Null user pointer |
| ERROR_MUX_SET_AUDIO_INPUT_ERROR | Invalid audio-multiplexing parameters |
| ERROR_MUX_ADD_ERROR             | Multiplexing error |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libakmedia.a

&emsp;&emsp;Headers: media_demuxer_lib.h, medialib_global.h, medialib_struct.h

&emsp;&emsp;【Call order】

```c
    AK_MPI_MUX_Open(pstMuxParam, s32MuxHandleId);
    AK_MPI_MUX_Start(s32MuxHandleId, pstStartParam);
    while(1){
        AK_MPI_MUX_Add_Video(s32MuxHandleId, video_stream);
        AK_MPI_MUX_Add_Audio(s32MuxHandleId, audio_stream);
    }
    AK_MPI_MUX_Stop(s32MuxHandleId);
    AK_MPI_MUX_Close(s32MuxHandleId);
```

&emsp;&emsp;【Paired APIs】

&emsp;&emsp;When parsing a recording file, pair this API with the following API:

```c
    AK_MPI_MUX_Add_Video(s32MuxHandleId, video_stream);
```

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The API is reentrant.

> **Note:** For MP4 output, the multiplexing library stores each video frame's duration according to its timestamp, while audio frames are assumed to have equal duration. Video frames therefore do not have to be delivered continuously during multiplexing, but audio frames must be. If the library receives no audio frame during multiplexing, the application can insert silent audio frames (send all-zero PCM frames to the encoder to produce silent encoded frames) so that audio data continues to reach the library. Missing audio frames without inserted silent frames may cause the multiplexed MP4 audio and video to lose synchronization.

<br/>

### AK_MPI_MUX_Add_Video

&emsp;&emsp;【Description】

&emsp;&emsp;Adds video to the multiplexed output.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_MUX_Add_Video(AK_S32 s32MuxHandleId, const VIDEO_STREAM_S *pstVideoStream);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| -------------- | ------------------- | ------------------- | --------- |
| s32MuxHandleId | Handle ID returned when the media multiplexing library is opened | 0~3 | Input |
| pstVideoStream | Video-stream data | See the `VIDEO_STREAM_S` structure | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ------- | ------ |
| 0 | Success |
| Other | See the error codes |

&emsp;&emsp;【Error codes】

| **Error code** | **Description** |
| ------------------------------- | --------- |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_MUX_USER_NULL | Null user pointer |
| ERROR_MUX_SET_VIDEO_INPUT_ERROR | Invalid video-multiplexing parameters |
| ERROR_MUX_ADD_ERROR | Multiplexing error |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_mux.so and libakmedia.so, or libmpi_mux.a and libakmedia.a

&emsp;&emsp;Header: ak_mux.h

&emsp;&emsp;【Call order】

```c
    AK_MPI_MUX_Open(pstMuxParam, s32MuxHandleId);
    AK_MPI_MUX_Start(s32MuxHandleId, pstStartParam);
    while(1){
        AK_MPI_MUX_Add_Video(s32MuxHandleId, video_stream);
        AK_MPI_MUX_Add_Audio(s32MuxHandleId, audio_stream);
    }
    AK_MPI_MUX_Stop(s32MuxHandleId);
    AK_MPI_MUX_Close(s32MuxHandleId);
```

&emsp;&emsp;【Paired APIs】

&emsp;&emsp;When parsing a recording file, pair this API with the following API:

```c
    AK_MPI_MUX_Add_Audio(s32MuxHandleId, audio_stream);
```

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The API is reentrant.

<br/>

### AK_MPI_MUX_Pause

&emsp;&emsp;【Description】

&emsp;&emsp;Pauses recording while a recording is in progress.

&emsp;&emsp;【Syntax】

```c
AK_S32 AK_MPI_MUX_Pause(AK_S32 s32MuxHandleId);
```

&emsp;&emsp;【Parameters】

| **Parameter**       | **Description**      | **Value range** | **Input/Output** |
| -------------- | ------------------- | -------- | --------- |
| s32MuxHandleId | Handle ID returned when the media multiplexing library is opened | 0~3 | Input |

&emsp;【Return values】

| **Return value** | **Description** |
| ---------- | ------ |
| AK_SUCCESS | Success  |
| AK_FAILED  | Failure  |

&emsp;&emsp;【Error codes】

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_mux.so and libakmedia.so, or libmpi_mux.a and libakmedia.a

&emsp;&emsp;Header: ak_mux.h

&emsp;&emsp;【Call order】

```c
    AK_MPI_MUX_Open(pstMuxParam, s32MuxHandleId);
    AK_MPI_MUX_Start( s32MuxHandleId,mux_start_param);
    AK_MPI_MUX_Pause( s32MuxHandleId);
    AK_MPI_MUX_Continue( s32MuxHandleId );
    AK_MPI_MUX_Close(s32MuxHandleId);
```

&emsp;&emsp;【Paired APIs】

AK_MPI_MUX_Continue

&emsp;&emsp;【Reentrancy】
Not reentrant.

<br/>

### AK_MPI_MUX_Continue

&emsp;&emsp;【Description】

&emsp;&emsp;Resumes recording while a recording is in progress. The first video frame after recording resumes must be an I-frame.

&emsp;&emsp;【Syntax】

```c
AK_S32 AK_MPI_MUX_Continue(AK_S32 s32MuxHandleId);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| -------------- | ------------------- | -------- | --------- |
| s32MuxHandleId | Handle ID returned when the media multiplexing library is opened | 0~3 | Input |

&emsp;【Return values】

| **Return value** | **Description** |
| ---------- | ------ |
| AK_SUCCESS | Success |
| AK_FAILED | Failure |

&emsp;&emsp;【Error codes】

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_mux.so and libakmedia.so, or libmpi_mux.a and libakmedia.a

&emsp;&emsp;Header: ak_mux.h

&emsp;&emsp;【Call order】

```c
    AK_MPI_MUX_Open(pstMuxParam, s32MuxHandleId);
    AK_MPI_MUX_Start( s32MuxHandleId,mux_start_param);
    AK_MPI_MUX_Pause( s32MuxHandleId);
    AK_MPI_MUX_Continue( s32MuxHandleId );
    AK_MPI_MUX_Close(s32MuxHandleId);
```

&emsp;&emsp;【Paired APIs】

AK_MPI_MUX_Pause

&emsp;&emsp;【Reentrancy】
Not reentrant.

<br/>

### AK_MPI_MUX_Fix_File

&emsp;&emsp;【Description】

&emsp;&emsp;Repairs a recording file that was not saved completely because of a power failure or similar event.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_MUX_Fix_File( FILE *pFILERecord, FILE *pFILEIndex, FILE *pFILEMoov,
                                FILE *pFILEStbl, MUX_TYPE_E enMuxType, MUX_FILEINFO_S *pstMuxFileinfo );
```

&emsp;&emsp;【Parameters】

| **Parameter**       | **Description**  | **Value range**                  | **Input/Output** |
| -------------- | --------------- | ---------------------------- | --------- |
| pFILERecord    | Pointer to the open recording file | `FILE` pointer             | Input |
| pFILEIndex     | Pointer to the open AVI index file | `FILE` pointer             | Input |
| pFILEMoov      | Pointer to the open MP4 MOOV file | `FILE` pointer              | Input |
| pFILEStbl      | Pointer to the open MP4 STBL file | `FILE` pointer              | Input |
| enMuxType      | Recording-file type | MUX_TYPE_AVI \| MUX_TYPE_MP4     | Input |
| pstMuxFileinfo | Receives information about the repaired recording file | -        | Output |

&emsp;【Return values】

| **Return value** | **Description** |
| ---------- | ------ |
| AK_SUCCESS | Success |
| AK_FAILED | Failure |

&emsp;&emsp;【Error codes】

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_mux.so and libakmedia.so, or libmpi_mux.a and libakmedia.a

&emsp;&emsp;Header: ak_mux.h

&emsp;&emsp;【Call order】

This API does not depend on other APIs and is generally called when the application starts.

&emsp;&emsp;【Paired APIs】

&emsp;&emsp;【Reentrancy】
Not reentrant.

<br/>

## Debug API

### AK_MPI_MUX_Print_Runtime_Status

&emsp;&emsp;【Description】

&emsp;&emsp;Prints MUX-module debug information, including:

`add_audio_count`: number of times audio was added;

`add_video_count`: number of times video was added.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_MUX_Print_Runtime_Status(AK_S32 s32MuxHandleId);
```

&emsp;&emsp;【Parameters】

| **Parameter**       | **Description** | **Value range** | **Input/Output** |
| -------------- | --------- | -------- | --------- |
| s32MuxHandleId | MUX-module handle ID | [0,3] | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ---------- | ------ |
| AK_SUCCESS | Success |
| Other        | See the error codes |

&emsp;&emsp;【Error codes】

| **Error code** | **Description** |
| ------------------- | ------ |
| ERROR_MUX_USER_NULL | Null argument |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_mux.so and libakmedia.so, or libmpi_mux.a and libakmedia.a

&emsp;&emsp;Header: ak_mux.h

&emsp;&emsp;【Call order】

```c
    AK_MPI_MUX_Open(pstMuxParam, s32MuxHandleId);
    AK_MPI_MUX_Print_Runtime_Status(s32MuxHandleId);
    AK_MPI_MUX_Close(s32MuxHandleId);
```

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The API is reentrant.

<br/>

### AK_MPI_MUX_Get_Status

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the current status of the MUX module's media multiplexing library.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_MUX_Get_Status(AK_S32 s32MuxHandleId, MUX_STATUS_E *penMuxStatus );
```

&emsp;&emsp;【Parameters】

| **Parameter**       | **Description** | **Value range**    | **Input/Output** |
| -------------- | ------------- | -------------- | --------- |
| s32MuxHandleId | MUX-module handle ID | [0,3] | Input |
| penMuxStatus   | Receives the current media multiplexing-library status | akMUX_STATUS_E | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ---------- | ------ |
| AK_SUCCESS | Success |
| AK_FAILED  | Failed to get the status |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_mux.so and libakmedia.so, or libmpi_mux.a and libakmedia.a

&emsp;&emsp;Header: ak_mux.h

&emsp;&emsp;【Call order】

```c
    AK_MPI_MUX_Open(pstMuxParam, s32MuxHandleId);
    AK_MPI_MUX_Get_Status(s32MuxHandleId,penMuxStatus);
    AK_MPI_MUX_Close(s32MuxHandleId);
```

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The API is reentrant.

<br/>

## API Call Dependencies

&emsp;&emsp;The public APIs provided by the MUX module have the following call dependencies:

| **API**                            | **Dependency**           |
| ------------------------------- | -------------------- |
| AK_MPI_MUX_Get_Version          | No dependency           |
| AK_MPI_MUX_Open                 | Call at startup         |
| AK_MPI_MUX_Start                | Call after AK_MPI_MUX_Open  |
| AK_MPI_MUX_Add_Audio            | Call after AK_MPI_MUX_Start |
| AK_MPI_MUX_Add_Video            | Call after AK_MPI_MUX_Start |
| AK_MPI_MUX_Stop                 | Call after AK_MPI_MUX_Start |
| AK_MPI_MUX_Get_Status           | Call after AK_MPI_MUX_Start |
| AK_MPI_MUX_Print_Runtime_Status | Call after AK_MPI_MUX_Open  |
| AK_MPI_MUX_Close                | Call after AK_MPI_MUX_Open  |
| <br/>                           |                      |

## ak_mux_sample Usage Example

Before running this sample, load the capture-related drivers, including `ak_vi.ko`, `sensor_xxx.ko`, `ak_vicap.ko`, `ak_isp.ko`, and `ak_pp.ko`. This is normally done by running a script. For a GC5603 CIS, see `gc5603.sh`; the commands are:

​        insmod /usr/modules/ak_vi.ko

​        insmod /usr/modules/sensor_gc5603.ko

​        insmod /usr/modules/ak_vicap.ko

​        insmod /usr/modules/ak_isp.ko

​        insmod /usr/modules/ak_pp.ko

​        For another CIS, see its corresponding `xxx.sh` loading script.

Also load the encoding drivers `ak_venc_adapter.ko` and `ak_venc_bridge.ko`:

​        insmod /usr/modules/ak_venc_adapter.ko

​        insmod /usr/modules/ak_venc_bridge.ko

| **Input parameter** | **Description**                                                                                                                                         |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| path_save       | Path in which recordings are saved |
| record_sec      | Recording duration |
| record_num      | Number of recording files to create |
| ai_sample_rate  | AI sample rate <br/>Allowed values: 8000,11025,12000,16000,22050,24000,32000,44100,48000 |
| vi_isp_cfg      | Sensor configuration file; specify the full path. |
| vi_width        | VI resolution width |
| vi_height       | VI resolution height |
| vi_channel      | VI channel ID |
| vi_fps          | VI frame rate |
| venc_goplen     | Video-encoding I-frame interval |
| aenc_type       | Audio encoding format<br/>AVI allowed values: MP3:2, AAC:4, PCM:6, (g711a)PCM_ALAW:17, (g711u)PCM_ULAW:18<br/>MP4 allowed values: AMR:3, AAC:4, (g711a)PCM_ALAW:17, (g711u)PCM_ULAW:18 |
| venc_type       | VENC encoding type (allowed values: 0,H264 1,JPEG 2,H265) |
| muxType         | Multiplexed-file type<br/>Allowed values: 0,MUX_TYPE_AVI 1,MUX_TYPE_MP4. JPEG encoding supports AVI only. |
| path_template   | Directory template; default: %Y%M%D <br/>Tokens: %Y-year, %M-month, %D-day, %h-hour, %m-minute, %s-second, %S-recording length in ms |
| file_template   | File template; default: %Y%M%D.%h%m%s.%S <br/>Tokens: %Y-year, %M-month, %D-day, %h-hour, %m-minute, %s-second, %S-recording length in ms |
| path_tmp        | Temporary directory used during recording multiplexing |
| buff_video      | Buffer length for video awaiting multiplexing; default 2048k; 0 means unlimited |
| buff_audio      | Buffer length for audio awaiting multiplexing; default 128k; 0 means unlimited |
| ai_frame_len    | Audio frame length |
| vi_frame_depth  | Number of video-capture buffers, 2-4 |
| ai_conf_file    | AI configuration file |
| ai_conf_section | Configuration section used in the AI configuration file |

<br/>

## Error Codes

| Error code | Macro                             | Meaning        |
| ---------- | ------------------------------- | -------- |
| 0x12000000 | MUX_ERROR_OPEN_LIB_ERROR        | Failed to open the library |
| 0x12000001 | MUX_ERROR_CLOSE_LIB_ERROR       | Failed to close the library |
| 0x12000002 | MUX_ERROR_GET_LIB_INFO_ERROR    | Failed to get library information |
| 0x12000003 | MUX_ERROR_START_LIB_ERROR       | Failed to start the library |
| 0x12000004 | MUX_ERROR_STOP_LIB_ERROR        | Failed to stop the library |
| 0x12000005 | MUX_ERROR_OPEN_TOO_MANY         | Opened too many times |
| 0x12000006 | MUX_ERROR_USER_NULL             | Null user |
| 0x12000007 | MUX_ERROR_SET_AUDIO_INPUT_ERROR | Invalid audio-multiplexing parameters |
| 0x12000008 | MUX_ERROR_SET_VIDEO_INPUT_ERROR | Invalid video-multiplexing parameters |
| 0x12000009 | MUX_ERROR_ADD_ERROR             | Multiplexing error |
| 0x1200000a | MUX_ERROR_ADD_VIDEO_FIRST       | Add video first |
| 0x1200000b | MUX_ERROR_VALUE_INVAILD         | Invalid value |

<br/>
