# Audio Encoding

## Overview

&emsp;&emsp;The audio-encoding module (AENC) encodes raw audio data using multiple audio protocols and outputs an audio bitstream. AENC supports multiple encoding formats.

<br/>

## API Reference

&emsp;&emsp;This module provides the APIs listed below.

| **Data structure**         | **Description**       |
| ---------------- | ------------ |
| AUDIO_TYPE_E | Audio encoding type |
| AENC_AAC_ATTR_E | AAC audio encoding type |
| AENC_AAC_PARAM_S | AAC audio encoding-attribute structure |
| AENC_PARAM_S | Parameters for opening audio encoding |
| FRAME_S | Audio-frame structure |
| AENC_ENCODE_S | Encoder-registration structure |
| ENC_OUT_INFO | Encoder output-attribute structure |

<br/>

| **Function**                     | **Description**              |
| ---------------------------- | ------------------- |
| AK_MPI_AENC_GetVersion | Gets the audio-encoding library version. |
| AK_MPI_AENC_GetEncVersion | Gets the ATC audio-encoding library version. |
| AK_MPI_AENC_Open | Opens audio encoding. |
| AK_MPI_AENC_Close | Closes audio encoding. |
| AK_MPI_AENC_SendFrame | Sends an audio frame for encoding. |
| AK_MPI_AENC_GetStream | Gets one frame of encoded data. |
| AK_MPI_AENC_ReleaseStream | Releases one frame of encoded data. |
| AK_MPI_AENC_SaveFile | Saves intermediate files from AENC audio processing. |
| K_MPI_AENC_ClearEncodeBuf | Clears the encoding buffer. |
| AK_MPI_AENC_SendEndOfFrame | Indicates that all audio-encoding data has been sent. |
| AK_MPI_AENC_RegisterEncoder | Registers an encoder. |
| AK_MPI_AENC_SetLibPrintLevel | Sets the encoding-library log level. |
| AK_MPI_AENC_GetEncParam | Gets parameters after the encoder is opened. |

> **Source note:** The source overview omits the initial `A` in `K_MPI_AENC_ClearEncodeBuf`. The API section and supplied header declare `AK_MPI_AENC_ClearEncodeBuf`.

<br/>

## Data Structures

### AUDIO_TYPE_E

&emsp;&emsp;【Notes】

&emsp;&emsp;Audio codec types. Because of library-size constraints, PCM and G711a/u are supported by default. To support other codec types, register an encoder by calling AK_MPI_AENC_RegisterEncoder.

&emsp;&emsp;【Definition】

```c
 typedef enum akAUDIO_TYPE_E
  {
    AK_AUDIO_TYPE_UNKNOWN,
    AK_AUDIO_TYPE_MIDI,
    AK_AUDIO_TYPE_MP3,
    AK_AUDIO_TYPE_AMR,
    AK_AUDIO_TYPE_AAC,
    AK_AUDIO_TYPE_WMA,
    AK_AUDIO_TYPE_PCM,
    AK_AUDIO_TYPE_ADPCM_IMA,
    AK_AUDIO_TYPE_ADPCM_MS,
    AK_AUDIO_TYPE_ADPCM_FLASH,
    AK_AUDIO_TYPE_APE,
    AK_AUDIO_TYPE_FLAC,
    AK_AUDIO_TYPE_OGG_FLAC,
    AK_AUDIO_TYPE_RA8LBR,
    AK_AUDIO_TYPE_DRA,
    AK_AUDIO_TYPE_OGG_VORBIS,
    AK_AUDIO_TYPE_AC3,
    AK_AUDIO_TYPE_PCM_ALAW,
    AK_AUDIO_TYPE_PCM_ULAW,
    AK_AUDIO_TYPE_SBC,
    AK_AUDIO_TYPE_MSBC,
    AK_AUDIO_TYPE_SPEEX,
    AK_AUDIO_TYPE_SPEEX_WB,
    AK_AUDIO_TYPE_OPUS,
    AK_AUDIO_TYPE_G722,
    AK_AUDIO_TYPE_VPWM,
    AK_AUDIO_TYPE_G729A,
    AK_AUDIO_TYPE_MAX
  }AUDIO_TYPE_E;
```

&emsp;&emsp;【Members】

| **Member**                  | **Description**    |
| ------------------------- | --------- |
| AK_AUDIO_TYPE_UNKNOWN | Default audio codec type |
| AK_AUDIO_TYPE_MIDI        | Unsupported       |
| AK_AUDIO_TYPE_MP3 | MP3 encoding format |
| AK_AUDIO_TYPE_AMR | AMR encoding format |
| AK_AUDIO_TYPE_AAC | AAC encoding format |
| AK_AUDIO_TYPE_WMA | WMA encoding format |
| AK_AUDIO_TYPE_PCM | Raw PCM data |
| AK_AUDIO_TYPE_ADPCM_IMA   | Unsupported       |
| AK_AUDIO_TYPE_ADPCM_MS    | Unsupported       |
| AK_AUDIO_TYPE_ADPCM_FLASH | Unsupported       |
| AK_AUDIO_TYPE_APE         | Unsupported       |
| AK_AUDIO_TYPE_FLAC        | Unsupported       |
| AK_AUDIO_TYPE_OGG_FLAC    | Unsupported       |
| AK_AUDIO_TYPE_RA8LBR      | Unsupported       |
| AK_AUDIO_TYPE_DRA         | Unsupported       |
| AK_AUDIO_TYPE_OGG_VORBIS  | Unsupported       |
| AK_AUDIO_TYPE_AC3         | Unsupported       |
| AK_AUDIO_TYPE_PCM_ALAW | G711a encoding format |
| AK_AUDIO_TYPE_PCM_ULAW | G711u encoding format |
| AK_AUDIO_TYPE_SBC         | Unsupported       |
| AK_AUDIO_TYPE_MSBC        | Unsupported       |
| AK_AUDIO_TYPE_SPEEX       | Unsupported       |
| AK_AUDIO_TYPE_SPEEX_WB    | Unsupported       |
| AK_AUDIO_TYPE_OPUS        | Unsupported       |
| AK_AUDIO_TYPE_G722        | Unsupported       |
| AK_AUDIO_TYPE_VPWM        | Unsupported       |
| AK_AUDIO_TYPE_G729A       | Unsupported       |

<br/>

&emsp;&emsp;The sample rates supported by each encoding format are shown below:

| Sample rate (mono) | PCM | AAC | AMR | G711A/U | MP3 |
| -------- | --- | --- | --- | ------- | --- |
| 8000     | Supported  | Supported  | Supported  | Supported      | Supported  |
| 11025    | Supported  | Supported  | Unsupported | Unsupported     | Supported  |
| 12000    | Supported  | Supported  | Unsupported | Unsupported     | Supported  |
| 16000    | Supported  | Supported  | Unsupported | Supported      | Supported  |
| 22050    | Supported  | Supported  | Unsupported | Unsupported     | Supported  |
| 24000    | Supported  | Supported  | Unsupported | Unsupported     | Supported  |
| 32000    | Supported  | Supported  | Unsupported | Unsupported     | Supported  |
| 44100    | Supported  | Supported  | Unsupported | Unsupported     | Supported  |
| 48000    | Supported  | Supported  | Unsupported | Unsupported     | Supported  |

<br/>

&emsp;&emsp;Stereo:

| Sample rate (stereo) | PCM | AAC | AMR | G711A/U | MP3 |
| -------- | --- | --- | --- | ------- | --- |
| 8000     | Supported  | Supported  | Unsupported | Unsupported     | Supported  |
| 11025    | Supported  | Supported  | Unsupported | Unsupported     | Supported  |
| 12000    | Supported  | Supported  | Unsupported | Unsupported     | Supported  |
| 16000    | Supported  | Supported  | Unsupported | Unsupported     | Supported  |
| 22050    | Supported  | Supported  | Unsupported | Unsupported     | Supported  |
| 24000    | Supported  | Supported  | Unsupported | Unsupported     | Supported  |
| 32000    | Supported  | Supported  | Unsupported | Unsupported     | Supported  |
| 44100    | Supported  | Supported  | Unsupported | Unsupported     | Supported  |
| 48000    | Supported  | Supported  | Unsupported | Unsupported     | Supported  |

&emsp;&emsp;【Related Functions】

```c
AK_S32 AK_MPI_AENC_Open(AK_S32 s32AencUserId, const AENC_PARAM_S *pstParam);
```

<br/>

### AENC_AAC_ATTR_E

&emsp;&emsp;【Notes】

&emsp;&emsp;Attribute controlling whether AAC encoding adds an AAC header.

&emsp;&emsp;【Definition】

```c
typedef enum akAENC_AAC_ATTR_E
{
    AENC_AAC_RESERVED = 0,
    AENC_AAC_SAVE_FRAME_HEAD,
    AENC_AAC_CUT_FRAME_HEAD
} AENC_AAC_ATTR_E;
```

&emsp;&emsp;【Members】

| **Member**                 | **Description**          |
| ------------------------ | --------------- |
| AENC_AAC_RESERVED | Initial AAC encoding-attribute value |
| AENC_AAC_SAVE_FRAME_HEAD | Retain the AAC encoding header |
| AENC_AAC_CUT_FRAME_HEAD | Remove the AAC encoding header |

&emsp;&emsp;【Related Functions】

### AENC_AAC_PARAM_S

【Notes】

AAC encoding attributes.

【Definition】

```c
typedef struct akAENC_AAC_PARAM_S
{
    AENC_AAC_ATTR_E enAacFrmHead;  // Whether encoding should return an ADTS header
}AENC_AAC_PARAM_S;
```

【Members】

| **Member**     | **Description**   |
| ------------ | -------- |
| enAacFrmHead | AAC header-attribute enumeration |

【Related Functions】

```c
AK_S32 AK_MPI_AENC_Open(AK_S32 s32AencUserId,const AENC_PARAM_S *pstParam);
```

### AENC_PARAM_S

&emsp;&emsp;【Notes】

&emsp;&emsp;Audio-encoding input parameters.

&emsp;&emsp;【Definition】

```c
typedef struct akAENC_PARAM_S
{
    AUDIO_SAMPLE_RATE_E enSampleRate;
    AUDIO_SAMPLE_BIT_E enSampleBits;
    AUDIO_SOUND_MODE_E enSoundMode;
    AUDIO_TYPE_E enType;       //encode/decode type
    union {
        AENC_AAC_PARAM_S stAacParam;
    } unAencAttr;
} AENC_PARAM_S;
```

&emsp;&emsp;【Members】

| **Member**     | **Description**   |
| ------------ | -------- |
| enSampleRate | Sample rate |
| enSampleBits | Sample precision |
| enSoundMode | Channel mode |
| enType | Audio encoding type |
| unAencAttr | Encoder-attribute union |

&emsp;&emsp;【Related Functions】

```c
AK_S32 AK_MPI_AENC_Open(AK_S32 s32AencUserId,const AENC_PARAM_S *pstParam);
```

<br/>

### FRAME_S

&emsp;&emsp;【Notes】

&emsp;&emsp;Audio PCM data structure.

&emsp;&emsp;【Definition】

```c
typedef struct akFRAME_S
{
        AK_U8 *pu8Data;    //frame data
        AK_U32 u32Len;        //frame len in bytes
        AK_U64 u64Ts;    //timestamp(ms)
        AK_U64 u64SeqNo;    //current frame sequence no.
}FRAME_S;
```

&emsp;&emsp;【Members】

| **Member** | **Description**                  |
| -------- | ----------------------- |
| u8Data | Pointer to the current audio frame's PCM data; non-null |
| u32Len | Length of the current audio frame's PCM data; >= 0 |
| u64Ts | Timestamp of the current audio frame's PCM data; >= 0 |
| u64SeqNo | Sequence number of the current audio frame's PCM data; >= 0 |

&emsp;&emsp;【Related Functions】

```c
AK_S32 AK_MPI_AENC_SendFrame(AK_S32 s32AencUserId, const FRAME_S *pstPcmFrame,AK_U32 u32TimeOut);
```

<br/>

### AENC_ENCODE_S

&emsp;&emsp;【Notes】

&emsp;&emsp;Encoder-registration structure.

&emsp;&emsp;【Definition】

```c
typedef struct akAENC_ENCODE_S
{
    AK_S32 enType; // T_AUDIO_TYPE
    AK_VOID* (*pfnEncOpen)(AK_VOID *pvOpenArg, AK_VOID *pstAttr);       // default to AENC_Open
    AK_S32 (*pfnEncProcess)(AK_VOID *pvEncHandle, AK_VOID *pvProcArg);  // default to AENC_Process
    AK_S32 (*pfnEncClose)(AK_VOID *pvEncHandle);                        // default to AENC_Close
    AK_S32 (*pfnEncReset)(AK_VOID *pvEncHandle);                        // default to AENC_Reset
    AK_S32 (*pfnEncFlush)(AK_VOID *pvEncHandle);                        // default to AENC_Last
} AENC_ENCODE_S;
```

&emsp;&emsp;【Members】

| **Member**      | **Description**       |
| ------------- | ------------ |
| enType | Encoding type |
| pfnEncOpen | Pointer to the function that opens the encoder |
| pfnEncProcess | Pointer to the encoding function |
| pfnEncClose | Pointer to the function that closes the encoder |
| pfnEncReset | Pointer to the function that clears encoder data |
| pfnEncFlush | Pointer to the function that finishes encoding |

&emsp;&emsp;【Related Functions】

```c
AK_S32 AK_MPI_AENC_RegisterEncoder(AENC_ENCODE_S *pstEncoder);
```

### ENC_OUT_INFO

&emsp;&emsp;【Notes】

&emsp;&emsp;Encoder output-attribute structure after opening.

&emsp;&emsp;【Definition】

```c
typedef struct akENC_OUT_INFO
{
    AK_S32 s32SamplesPerFrame;  // Number of PCM samples per frame
    AK_S32 s32FrameSize;        // Encoded output length
    AK_S32 s32BitRate;          // Encoding bit rate
}ENC_OUT_INFO;
```

&emsp;&emsp;【Members】

| **Member**           | **Description**        |
| ------------------ | ------------- |
| s32SamplesPerFrame | Number of PCM samples per frame |
| s32FrameSize | Encoded output length |
| s32BitRate | Encoding bit rate |

&emsp;&emsp;【Related Functions】

```c
AK_S32 AK_MPI_AENC_GetEncParam(AK_S32 s32AencUserId, ENC_OUT_INFO *stEncLenPam);
```

<br/>

## Getting Version Information

### AK_MPI_AENC_GetVersion

&emsp;&emsp;【Description】

&emsp;&emsp;Prints the audio-encoding library version.

&emsp;&emsp;【Syntax】

```c
const AK_CHAR* AK_MPI_AENC_GetVersion(AK_VOID);
```

&emsp;&emsp;【Return Value】

| **Return value**   | **Description** |
| --------- | ------ |
| Audio-encoding module version | Success |
| NULL      | Failure     |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libmpi_aenc.a/so

&emsp;&emsp;Header: ak_aenc.h

&emsp;&emsp;【Call Sequence】

&emsp;&emsp;This function may be called at any point.

### AK_MPI_AENC_GetEncVersion

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the audio-encoding library version.

&emsp;&emsp;【Syntax】

```c
AK_CHAR *AK_MPI_AENC_GetEncVersion(AK_VOID);
```

&emsp;&emsp;【Return Value】

| **Return value**  | **Description** |
| -------- | ------ |
| Audio-encoding library version | Success |
| NULL     | Failure     |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_aenc.a/so and libakaudiocodec.a/so, or libakaac.a/so, libakamr.a/so, and libakmp3.a/so

&emsp;&emsp;Header: ak_aenc.h

&emsp;&emsp;【Call Sequence】

- Call after open.

### AK_MPI_AENC_SetLibPrintLevel

&emsp;&emsp;【Description】

&emsp;&emsp;Sets the audio-encoding library log level.

&emsp;&emsp;【Syntax】

```c
AK_S32 AK_MPI_AENC_SetLibPrintLevel(AK_U32 u32PrintLevel);
```

​        【Parameters】

| Parameter | Description | Value range | Input/Output |
| ------------- | ---- | ----------------------- | ----- |
| u32PrintLevel | Log level | See ATCLIB_PRINT_LEVEL_E | Input |

&emsp;【Return Value】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0       | Success         |
| Nonzero      | Failure; the return value is an error code. |

​    【Error Codes】

| **Error code**                | **Description** |
| ---------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid parameter  |

【Requirements】

&emsp;&emsp;Libraries: libmpi_aenc.a/so and libakaudiocodec.a/so

&emsp;&emsp;Headers: ak_aenc.h and ak_common_audio.h

&emsp;&emsp;【Call Sequence】

&emsp;&emsp;May be called at any point; calling it before open is recommended.

## Registering an Encoder

### AK_MPI_AENC_RegisterEncoder

​    【Description】

​        Registers an encoder.

​    【Syntax】

```c
AK_S32 AK_MPI_AENC_RegisterEncoder(AENC_ENCODE_S *pstEncode);
```

​    【Parameters】

| **Parameter**  | **Description**    | **Value range**        | **Input/Output** |
| --------- | --------- | --------------- | --------- |
| pstEncode | Encoder-registration attribute structure | See AENC_ENCODE_S | Input |

​    【Return Value】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0       | Success         |
| Nonzero      | Failure; the return value is an error code. |

​    【Error Codes】

| **Error code**                 | **Description** |
| ----------------------- | ------ |
| ERROR_TYPE_POINTER_NULL | Null parameter   |
| ERROR_TYPE_INVALID_ARG  | Invalid parameter  |

​    【Example】

```c
AENC_ENCODE_S pstEncode = {0};
    pstEncode.enType = AK_AUDIO_TYPE_MP3;
    pstEncode.pfnEncOpen = AENC_OpenMp3;  // Encoder registration callback
    pstEncode.pfnEncClose = NULL;// Encoder registration callback
    pstEncode.pfnEncFlush= NULL;// Encoder registration callback
    pstEncode.pfnEncProcess= NULL;// Encoder registration callback
    pstEncode.pfnEncReset= NULL;// Encoder registration callback
ret = AK_IMP_AENC_RegisterEncoder(&pstEncode);
    if(ret) {
        AK_BASE_PrintErrorEx(MODULE_AENC,"AK_IMP_AENC_RegisterEecoder failed\n");
        return ret;
    }
// Open the encoder
    AENC_PARAM_S stAencParam = {0};

    stAencParam.enType = AK_AUDIO_TYPE_MP3;    // Encoding type
    stAencParam.enSampleBits = AK_AUDIO_SMPLE_BIT_16; // Sample precision
    stAencParam.enSampleRate= AK_AUDIO_SAMPLE_RATE_16000; // Sample rate
    stAencParam.enSoundMode = AUDIO_SOUND_MODE_MONO;     // Channel mode

    if(AK_MPI_AENC_Open(s32AencUserId, &stAencParam)) {
        AK_BASE_PrintErrorEx(MODULE_ID_APP, "AK_MPI_AENC_Open failed\n");
        return AK_FAILED;
    }
```

​    【Requirements】

&emsp;&emsp;Libraries: libmpi_aenc.a/so and libakaudiocodec.a/so, or libakaac.a/so, libakmp3.a/so, and libakamr.a/so

&emsp;&emsp;Headers: ak_aenc.h, aenc_mp3.h, aenc_aac.h, and aenc_amr.h

【Note】

- An encoder protocol cannot be registered more than once. For example, after registering an MP3 encoder, another MP3 encoder cannot be registered.
- Separate MP3, AAC, and AMR libraries and their corresponding headers are provided. The example callback functions are declared in those headers.
- For an encoding format that is not supported by default, call this interface before AK_MPI_AENC_Open to register the encoder. User-provided encoders are not currently supported.
- When assigning AENC_ENCODE_S, only AENC_OpenXXX is currently supported; the other parameters may be omitted.

## Opening and Closing the Module

### AK_MPI_AENC_Open

&emsp;&emsp;【Description】

&emsp;&emsp;Opens audio encoding. Multiple encoding channels are supported, with one handle per encoder and up to 4 audio channels encoded concurrently.

&emsp;&emsp;【Syntax】

```c
AK_S32 AK_MPI_AENC_Open(AK_S32 s32AencUserId, const AENC_PARAM_S *pstParam);
```

​       【Parameters】

| Parameter | Description | Value range | Input/Output |
| ------------- | ---------- | ----------------- | ----- |
| s32AencUserId | Audio-encoding module handle ID | [0,3] | Input |
| pstParam | Audio-encoding input parameters | See AENC_PARAM_S | Input |

​    【Return Value】

| **Return value** | **Description** |
| ------- | ------ |
| 0       | Success     |
| Other      | See the error codes. |

   【Error Codes】

| Error code | Description |
| --------------------------- | --------------- |
| ERROR_AENC_OPEN_TOO_MANY | Number of users exceeds the maximum |
| ERROR_AENC_USER_NULL        | Null user handle  |
| ERROR_TYPE_MALLOC_FAILED    | Malloc failed       |
| ERROR_TYPE_POINTER_NULL     | Null parameter            |
| ERROR_AENC_NOT_SUPPORT_TYPE | Unsupported encoding type |
| ERROR_TYPE_INVALID_ARG      | Invalid parameter           |
| ERROR_AENC_OPEN_LIB_ERROR | Error opening encoding library |
| ERROR_AENC_RB_ERROR         | Ring-buffer operation failed |

​    【Requirements】

&emsp;&emsp;Libraries: libmpi_aenc.a/so and libakaudiocodec.a/so, or libakaac.a/so, libakamr.a/so, and libakmp3.a/so

&emsp;&emsp;Header: ak_aenc.h

&emsp;&emsp;【Call Sequence】

![AENC call sequence: Open, SendFrame, GetStream, ReleaseStream, Close](../../../../zh_CN/software/board/middleware-api/img/aenc-call-sequence.jpg)

&emsp;&emsp;【Paired Interface】

```c
AK_S32 AK_MPI_AENC_Close(AK_S32 s32AencUserId);
```

&emsp;&emsp;【Note】

&emsp;&emsp;Open may be called multiple times. Each call adds a user, up to a maximum of 4 users.

### AK_MPI_AENC_Close

&emsp;&emsp;【Description】

&emsp;&emsp;Closes audio encoding.

&emsp;&emsp;【Syntax】

```c
AK_S32 AK_MPI_AENC_Close(AK_S32 s32AencUserId);
```

&emsp;&emsp;【Parameters】

| **Parameter**      | **Description**     | **Value range** | **Input/Output** |
| ------------- | ---------- | -------- | --------- |
| s32AencUserId | Audio-encoding module handle ID | [0,3] | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ------- | ------ |
| 0       | Success     |
| Other      | See the error codes. |

&emsp;&emsp;【Error Codes】

| **Error code**                    | **Description**           |
| -------------------------- | ---------------- |
| ERROR_AENC_USER_NULL       | Null user handle   |
| ERROR_TYPE_POINTER_NULL    | Null parameter pointer           |
| ERROR_AENC_CLOSE_LIB_ERROR | Error closing decoding library |
| ERROR_AENC_RB_ERROR        | Ring-buffer setup error |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_aenc.a/so and libakaudiocodec.a/so, or libakaac.a/so, libakamr.a/so, and libakmp3.a/so

&emsp;&emsp;Header: ak_aenc.h

&emsp;&emsp;【Call Sequence】

![AENC call sequence: Open, SendFrame, GetStream, ReleaseStream, Close](../../../../zh_CN/software/board/middleware-api/img/aenc-call-sequence.jpg)

&emsp;&emsp;【Paired Interface】

```c
   AK_S32 AK_MPI_AENC_Open(AK_S32 s32AencUserId,const AENC_PARAM_S *pstParam);
```

&emsp;&emsp;【Note】

&emsp;&emsp;AK_MPI_AENC_Close may be called multiple times. Closing a nonexistent s32AencUserId returns an error.

<br/>

## Encoding Flow

### AK_MPI_AENC_SendFrame

&emsp;&emsp;【Description】

&emsp;&emsp;Sends an audio frame for encoding. The PCM length required to encode one frame for each format is shown below:

&emsp;&emsp;【Syntax】

```c
AK_S32 AK_MPI_AENC_SendFrame(AK_S32 s32AencUserId, const FRAME_S *pstPcmFrame,AK_U32 u32TimeOut);
```

&emsp;&emsp;【Parameters】

| **Parameter**      | **Description**                                                     | **Value range**                 | **Input/Output** |
| ------------- | ---------------------------------------------------------- | ------------------------ | --------- |
| s32AencUserId | Audio-encoding module handle ID | [0,3] | Input |
| pstPcmFrame | One frame of data to encode | See struct FRAME_S | Input |
| u32TimeOut | Data timeout: 0 selects nonblocking mode and returns an error if no data is available;<br />a value >0 blocks for the timeout and returns an error when it expires. | 0 or blocking duration in ms [0,60000] | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0       | Success         |
| Nonzero      | Failure; the return value is an error code. |

&emsp;&emsp;【Error Codes】

| **Error code**                      | **Description**         |
| ---------------------------- | -------------- |
| ERROR_AENC_USER_NULL         | Null user handle |
| ERROR_TYPE_POINTER_NULL      | Null parameter           |
| ERROR_TYPE_INVALID_ARG       | Invalid parameter          |
| ERROR_AENC_LIST_CNT_TOO_MANY | Encoding buffer is full        |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_aenc.a/so and libakaudiocodec.a/so, or libakaac.a/so, libakamr.a/so, and libakmp3.a/so

&emsp;&emsp;Header: ak_aenc.h

&emsp;&emsp;【Call Sequence】

![AENC call sequence: Open, SendFrame, GetStream, ReleaseStream, Close](../../../../zh_CN/software/board/middleware-api/img/aenc-call-sequence.jpg)

【Note】

- Open the encoder before calling this interface to send an audio frame for encoding.

- When u32TimeOut is 0, data is sent in nonblocking mode. When it is greater than 0, the call blocks for u32TimeOut ms and reports a timeout error if the data cannot be sent.

&emsp;&emsp;

### AK_MPI_AENC_GetStream

&emsp;&emsp;【Description】

&emsp;&emsp;Gets one frame of encoded data.

&emsp;&emsp;【Syntax】

```c
AK_S32 AK_MPI_AENC_GetStream(AK_S32 s32AencUserId, AUDIO_STREAM_S *pstStream, AK_U32 u32TimeOut);
```

&emsp;&emsp;【Parameters】

| **Parameter**      | **Description**                                                     | **Value range**                 | **Input/Output** |
| ------------- | ---------------------------------------------------------- | ------------------------ | --------- |
| s32AencUserId | Audio-encoding module handle ID | [0,3] | Input |
| pstStream | One frame of encoded data | See AUDIO_STREAM_S | Output |
| u32TimeOut | Data timeout: 0 selects nonblocking mode and returns an error if no data is available;<br />a value >0 blocks for the timeout and returns an error when it expires. | 0 or blocking duration in ms [0,60000] | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0       | Success         |
| Nonzero      | Failure; the return value is an error code. |

&emsp;&emsp;【Error Codes】

| **Error code**                  | **Description**         |
| ------------------------ | -------------- |
| ERROR_AENC_USER_NULL     | Null user handle |
| ERROR_TYPE_POINTER_NULL  | Null parameter           |
| ERROR_TYPE_INVALID_ARG   | Invalid parameter          |
| ERROR_AENC_NO_DATA       | No encoded data         |
| ERROR_TYPE_MALLOC_FAILED | Malloc failed      |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_aenc.a/so and libakaudiocodec.a/so, or libakaac.a/so, libakamr.a/so, and libakmp3.a/so

&emsp;&emsp;Header: ak_aenc.h

&emsp;&emsp;【Call Sequence】

![AENC call sequence: Open, SendFrame, GetStream, ReleaseStream, Close](../../../../zh_CN/software/board/middleware-api/img/aenc-call-sequence.jpg)

​        【Note】

- When u32TimeOut is 0, data is obtained in nonblocking mode. When it is greater than 0, the call blocks for u32TimeOut ms and reports a timeout error if no data is available.

<br/>

### AK_MPI_AENC_ReleaseStream

&emsp;&emsp;【Description】

&emsp;&emsp;Releases one frame of encoded data.

&emsp;&emsp;【Syntax】

```c
  AK_S32 AK_MPI_AENC_ReleaseStream(AK_S32 s32AencUserId, AUDIO_STREAM_S *pstStream);
```

&emsp;&emsp;【Parameters】

| **Parameter**      | **Description**     | **Value range**         | **Input/Output** |
| ------------- | ---------- | ---------------- | --------- |
| s32AencUserId | Audio-encoding module handle ID | [0,3] | Input |
| pstStream | One frame of encoded data | See AUDIO_STREAM_S | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0       | Success         |
| Nonzero      | Failure; the return value is an error code. |

&emsp;&emsp;【Error Codes】

| **Error code**                 | **Description** |
| ----------------------- | ------ |
| ERROR_TYPE_POINTER_NULL | Null parameter   |
| ERROR_TYPE_INVALID_ARG  | Invalid parameter  |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_aenc.a/so and libakaudiocodec.a/so, or libakaac.a/so, libakamr.a/so, and libakmp3.a/so

&emsp;&emsp;Header: ak_aenc.h

&emsp;&emsp;【Call Sequence】

![AENC call sequence: Open, SendFrame, GetStream, ReleaseStream, Close](../../../../zh_CN/software/board/middleware-api/img/aenc-call-sequence.jpg)

​        【Note】

### AK_MPI_AENC_SendEndOfFrame

&emsp;&emsp;【Description】

&emsp;&emsp;Signals that all audio-encoding frames have been sent.

&emsp;&emsp;【Syntax】

```c
AK_S32 AK_MPI_AENC_SendEndOfFrame(AK_S32 s32AencUserId);
```

&emsp;&emsp;【Parameters】

| Parameter | Description | Value range | Input/Output |
| ------------- | ---------- | ----- | ----- |
| s32AencUserId | Audio-encoding module handle ID | [0,3] | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0       | Success         |
| Nonzero      | Failure; the return value is an error code. |

&emsp;&emsp;【Error Codes】

| **Error code**                 | **Description** |
| ----------------------- | ------ |
| ERROR_TYPE_POINTER_NULL | Null parameter   |
| ERROR_TYPE_INVALID_ARG  | Invalid parameter  |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_aenc.a/so and libakaudiocodec.a/so, or libakaac.a/so, libakamr.a/so, and libakmp3.a/so

&emsp;&emsp;Header: ak_aenc.h

&emsp;&emsp;【Call Sequence】

![AENC call sequence: Open, SendFrame, SendEndOfFrame at completion, GetStream, ReleaseStream, Close](../../../../zh_CN/software/board/middleware-api/img/aenc-call-sequence-send-end-of-frame.jpg)

​        【Note】

## Debugging Interface

### AK_MPI_AENC_SaveFile

&emsp;&emsp;【Description】

&emsp;&emsp;Saves intermediate files from AENC audio processing. Two file types are saved: audio passed to AENC and audio output after AENC processing.

&emsp;&emsp;【Syntax】

```c
AK_S32 AK_MPI_AENC_SaveFile(AK_S32 s32AencUserId, AUDIO_SAVE_FILE_INFO_S *pstSaveFileInfo);
```

&emsp;&emsp;【Parameters】

| Parameter | Description | Value range | Input/Output |
| --------------- | ---------- | --------------------------- | ----- |
| s32AencUserId | Audio-encoding module handle ID | [0,3] | Input |
| pstSaveFileInfo | Information about the file to save | See AUDIO_SAVE_FILE_INFO_S | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ------- | ------ |
| 0       | Success     |
| Other      | See the error codes. |

&emsp;&emsp;【Error Codes】

| **Error code**                     | **Description**         |
| --------------------------- | -------------- |
| ERROR_TYPE_POINTER_NULL     | Null parameter           |
| ERROR_TYPE_INVALID_ARG      | Invalid parameter          |
| ERROR_AENC_USER_NULL        | Null user handle |
| ERROR_TYPE_FILE_OPEN_FAILED | Failed to open file         |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_aenc.a/so and libakaudiocodec.a/so, or libakaac.a/so, libakamr.a/so, and libakmp3.a/so

&emsp;&emsp;Header: ak_aenc.h

&emsp;&emsp;【Call Sequence】

![AENC call sequence: Open, SaveFile, Close](../../../../zh_CN/software/board/middleware-api/img/aenc-call-sequence-save-file.jpg)

【Note】

- Call this interface when audio from AENC processing must be saved for troubleshooting.

## Clearing the Buffer

### AK_MPI_AENC_ClearEncodeBuf

&emsp;&emsp;【Description】

&emsp;&emsp;Clears the encoding buffer. If encoding is paused, call this interface when restarting to clear residual data from the incomplete encoding operation.

&emsp;&emsp;【Syntax】

```c
AK_S32 AK_MPI_AENC_ClearEncodeBuf(AK_S32 s32AencUserId);
```

&emsp;&emsp;【Parameters】

| **Parameter**      | **Description**     | **Value range** | **Input/Output** |
| ------------- | ---------- | -------- | --------- |
| s32AencUserId | Audio-encoding module handle ID | [0,3] | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0       | Success         |
| Nonzero      | Failure; the return value is an error code. |

&emsp;&emsp;【Error Codes】

| **Error code**              | **Description**         |
| -------------------- | -------------- |
| ERROR_AENC_USER_NULL | Null user handle |
| ERROR_AENC_RB_ERROR  | Ring-buffer error  |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_aenc.a/so and libakaudiocodec.a/so, or libakaac.a/so, libakamr.a/so, and libakmp3.a/so

&emsp;&emsp;Header: ak_aenc.h

&emsp;&emsp;【Call Sequence】

![AENC call sequence: Open, SendFrame, GetStream, ReleaseStream, ClearEncodeBuf, Close](../../../../zh_CN/software/board/middleware-api/img/aenc-call-sequence-clear-encode-buf.jpg)

## Getting Parameters

### AK_MPI_AENC_GetEncParam

​    【Description】

Gets the parameters after the encoder is opened.

​    【Syntax】

```c
AK_S32 AK_MPI_AENC_GetEncParam(AK_S32 s32AencUserId, ENC_OUT_INFO *stEncLenPam);
```

​    【Parameters】

| Parameter | Description | Value range | Input/Output |
| ------------- | ---------- | ----------------- | ----- |
| s32AencUserId | Audio-encoding module handle ID | [0,3] | Input |
| stEncLenPam | Encoder parameters | See ENC_OUT_INFO | Output |

​    【Return Value】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0       | Success         |
| Nonzero      | Failure; the return value is an error code. |

​    【Error Codes】

| **Error code**              | **Description**         |
| -------------------- | -------------- |
| ERROR_AENC_USER_NULL | Null user handle |
| ERROR_AENC_RB_ERROR  | Ring-buffer error  |

【Requirements】

&emsp;&emsp;Libraries: libmpi_aenc.a/so and libakaudiocodec.a/so, or libakaac.a/so, libakamr.a/so, and libakmp3.a/so

&emsp;&emsp;Header: ak_aenc.h

## Interface Call Dependencies

&emsp;&emsp;The AENC interfaces have the call dependencies shown below:

| **Interface** | **Dependency** |
| ---------------------------- | -------------------- |
| AK_MPI_AENC_GetEncVersion | None |
| AK_MPI_AENC_SetLibPrintLevel | None |
| AK_MPI_AENC_GetVersion | Call after AK_MPI_AENC_Open |
| AK_MPI_AENC_Open             | -                    |
| AK_MPI_AENC_SendFrame | Call after AK_MPI_AENC_Open |
| AK_MPI_AENC_GetStream | Call after AK_MPI_AENC_Open |
| AK_MPI_AENC_ReleaseStream | Call after AK_MPI_AENC_Open |
| AK_MPI_AENC_ClearEncodeBuf | Call after AK_MPI_AENC_Open |
| AK_MPI_AENC_Close | Call after AK_MPI_AENC_Open |
| AK_MPI_AENC_RegisterEncoder | Call before AK_MPI_AENC_Open |
| AK_MPI_AENC_SaveFile | Call after AK_MPI_AENC_Open |
| AK_MPI_AENC_SendEndOfFrame | Call after AK_MPI_AENC_Open |
| AK_MPI_AENC_GetEncParam | Call after AK_MPI_AENC_Open |

<br/>

## ak_aenc_sample Usage Example

### Sample Command and Parameters

Before running this sample, load ak_pcm.ko with insmod. It is normally loaded by default at startup.

| Short option | Long option | **Description** |
| -------- | -------------- | ---------------------------------------------------------------------------- |
| h | help | Prints help. |
| s | sample-rate | Audio sample rate; supports 8000, 16000, 44100 Hz, and 48000 Hz. |
| p | path | PCM output directory; do not specify a filename. End the path with `/`, for example `/mnt/`. |
| t | second | Capture duration in seconds. |
| d | device-type | Device type: 0:DEV_ADC, 1:DEV_PDM, 2:DEV_I2S0_AI. |
| m | config-file | Full path to the audio configuration file. |
| n | config-section | Audio configuration section name: def_near for AI with one microphone; two_array_near for AI with two microphones; def_far for AO. |
| f | save-file | Whether to save the encoded file [0: do not save, 1: save]. |
| e | encode-type | Encoding type [mp3 aac amr g711a g711u pcm]. |

### Sample Storage and File Naming

(1) Sample output uses MP3 format by default.
(2) Sample output is stored in /mnt/ by default.
(3) The default output filename is `yyyymmdd-ddmmss<sample-rate><channel-count><duration-ms><device>.mp3`.

### Example

ak_aenc_sample -t 20 -s 16000 -e mp3 -d 0 -f 1 -p /mnt/ -m /etc/config/audio_config.ini -n def_near

## /var/platform Description

The /var/platform directory exposes the current module configuration parameters and status. Its parameters are described below.

### param

| Parameter | Description |
| --------- | ---- |
| SoundMode | Sample rate |
| SoundMode | Channel mode |
| SampleBit | Sample precision |
| UserCnt | Number of users |
| AencType | Encoding type |

### stat

| Parameter | Description |
| ----------------- | ---------------- |
| Mp3Version | MP3 library version |
| AudioCodecVersion | Codec library version |
| AencMpiVersion | Platform encoding-library version |
| BitRate | Bit rate for the encoding type |
| FrameSize | Encoded output length for the encoding type |
| SampleParFrame | Samples required per encoded frame for the encoding type |

<br/>

## Error Codes

| Error code | Macro | Meaning |
| ---------- | ---------------------------- | ------ |
| 0x0f000000 | ERROR_AENC_OPEN_LIB_ERROR | Failed to open library |
| 0x0f000001 | ERROR_AENC_CLOSE_LIB_ERROR | Failed to close library |
| 0x0f000002 | ERROR_AENC_OPEN_TOO_MANY | Too many open handles |
| 0x0f000003 | ERROR_AENC_NOT_SUPPORT_TYPE | Unsupported type |
| 0x0f000004 | ERROR_AENC_INVALID_PARAM     | Invalid parameter   |
| 0x0f000005 | ERROR_AENC_USER_NULL | Null user |
| 0x0f000006 | ERROR_AENC_LIST_CNT_TOO_MANY | Too many list entries |
| 0x0f000007 | ERROR_AENC_RB_ERROR | RB error |
| 0x0f000008 | ERROR_AENC_NO_DATA | No data |
| 0x0f000009 | ERROR_AENC_AUDIO_CODEC_ERROR | Encoding error |
| 0x0f00000a | ERROR_AENC_NOT_OPEN | Module not open |

<br/>
