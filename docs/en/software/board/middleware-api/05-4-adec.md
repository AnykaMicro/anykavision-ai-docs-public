# Audio Decoding

## Overview

&emsp;&emsp;The audio-decoding module (ADEC) decodes audio data sent to it and outputs decoded raw PCM data. ADEC supports multiple decoding formats.

<br/>

## API Reference

&emsp;&emsp;This module provides the APIs listed below.

| **Data structure**         | **Description**   |
| ---------------- | -------- |
| AUDIO_TYPE_E | Audio codec type |
| ADEC_PARAM_S | Audio-decoding input parameters |
| FRAME_S | Audio-frame structure |
| ADEC_AAC_PARAM_S | AAC decoding format |
| DEC_BUF_STATUS_S | Decoder buffer information |
| ADEC_DECODE_S | Decoder-registration structure |

<br/>

| **Function**                       | **Description**              |
| ------------------------------ | ------------------- |
| AK_MPI_ADEC_GetVersion | Gets the audio-decoding library version. |
| AK_MPI_ADEC_Open | Opens audio decoding. |
| AK_MPI_ADEC_Close | Closes audio decoding. |
| AK_MPI_ADEC_SetOutputPcmLen | Sets the decoded output-data length. |
| AK_MPI_ADEC_ClearDecodeBuf | Clears the decoding buffer. |
| AK_MPI_ADEC_SendStream | Sends audio for decoding. |
| AK_MPI_ADEC_GetFrame | Gets one frame of decoded data. |
| AK_MPI_ADEC_ReleaseFrame | Releases one frame of decoded data. |
| AK_MPI_ADEC_SendEndofStream | Tells the decoder that all audio-decoding data has been sent. |
| AK_MPI_ADEC_PrintRuntimeStatus | Prints ADEC debug information. |
| AK_MPI_ADEC_SaveFile | Saves intermediate files from ADEC audio processing. |
| AK_MPI_ADEC_GetBufStatus | Gets decoder buffer information. |
| AK_MPI_ADEC_RegisterDecoder | Registers a decoder. |
| AK_MPI_ADEC_SetLibPrintLevel | Sets the decoding-library log level. |

> **Source note:** The source lists `AK_MPI_ADEC_PrintRuntimeStatus`, but this page has no corresponding API section and the supplied public headers do not declare it. Later source headings and call-order text spell the end-of-stream API as `AK_MPI_ADEC_SendEndOfStream`; use the case-sensitive name declared by the syntax and header: `AK_MPI_ADEC_SendEndofStream`.

## Data Structures

### AUDIO_TYPE_E

&emsp;&emsp;【Notes】

&emsp;&emsp;Audio codec types. PCM and G711a/u are supported by default. To support other codec types, register an encoder by calling AK_MPI_ADEC_RegisterEncoder.

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

&emsp;&emsp;The sample rates supported by each decoding format are shown below:

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

【Related Interfaces】

```c
AK_S32 AK_MPI_ADEC_Open(AK_S32 s32AdecUserId,const ADEC_PARAM_S *pstParam);
```

<br/>

### ADEC_PARAM_S

&emsp;&emsp;【Notes】

&emsp;&emsp;Audio-decoding input parameters.

&emsp;&emsp;【Definition】

```c
typedef struct akADEC_PARAM_S
{
        AUDIO_TYPE_E enType;
        AUDIO_SAMPLE_RATE_E enSampleRate;
        AUDIO_SAMPLE_BIT_E enSampleBits;
        AUDIO_SOUND_MODE_E enSoundMode;
            union {
            ADEC_AAC_PARAM_S stAacParam;
             } unAdecAttr;
}ADEC_PARAM_S;
```

&emsp;&emsp;【Members】

| Member | Description |
| ------------ | ------- |
| enType | Audio decoding type |
| enSampleRate | Audio sample rate |
| enSampleBits | Audio sample precision |
| enSoundMode | Audio channel mode |
| unAdecAttr | Decoding-attribute union |

&emsp;&emsp;【Related Functions】

```c
AK_S32 AK_MPI_ADEC_Open(AK_S32 s32AdecUserId,const ADEC_PARAM_S *pstParam,);
```

<br/>

### FRAME_S

&emsp;&emsp;【Notes】

&emsp;&emsp;Output frame after audio decoding.

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

| Member | Description |
| -------- | ------------- |
| pu8Data | Pointer to one frame of decoded audio data |
| u32Len | Length of one frame of decoded audio data |
| u64Ts | Timestamp of one frame of decoded audio data |
| u64SeqNo | Sequence number of one frame of decoded audio data |

&emsp;&emsp;【Related Functions】

```c
AK_S32 AK_MPI_ADEC_GetFrame(AK_S32 s32AdecUserId, FRAME_S *pstPcmFrame, AK_U32 u32TimeOut);
AK_S32 AK_MPI_ADEC_ReleaseFrame(AK_S32 s32AdecUserId, FRAME_S *pstPcmFrame);
```

### DEC_BUF_STATUS_S

&emsp;&emsp;【Notes】

&emsp;&emsp;Decoder buffer information, including total buffer size and current data size.

&emsp;&emsp;【Definition】

```c
typedef struct akDEC_BUF_STATUS_S
{
    AK_S32 s32BufTotalLen;
    AK_S32 s32BufRemainLen;
} DEC_BUF_STATUS_S;
```

&emsp;&emsp;【Members】

| Member | Description |
| --------------- | ------------------ |
| s32BufTotalLen | Total decoder input-buffer size |
| s32BufRemainLen | Remaining decoder input-buffer size |

​    【Related Functions】

```c
AK_S32 AK_MPI_ADEC_GetBufStatus(AK_S32 s32AdecUserId, DEC_BUF_STATUS_S *pstBufStatus)
```

<br/>

### ADEC_AAC_PARAM_S

&emsp;&emsp;【Notes】

&emsp;&emsp;AAC decoding format.

&emsp;&emsp;【Definition】

```c
typedef struct akADEC_AAC_PARAM_S
{
    AK_U16 u16AacStreamFormat;
}ADEC_AAC_PARAM_S;
```

&emsp;&emsp;【Members】

| **Member**           | **Description**                                                                                                                                                                                                                                           |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| u16AacStreamFormat | AAC decoding-mode parameter.<br/>0: auto detect: the library determines the stream format from its initial bytes.<br/>1: adts: every frame has a header. During decoding, a corrupt frame can be skipped and decoding can continue at the next frame. This format is common in network transmission and media files; because corrupt and missing whole or partial frames are unavoidable in transmission, adts is a good choice.<br/>2: adif: only the start of the file has a header, followed by a raw bitstream. This older storage format is now rarely used.<br/>3: raw: a raw bitstream without any frame headers. |

&emsp;&emsp;【Related Functions】

```c
AK_S32 AK_MPI_ADEC_Open(AK_S32 s32AdecUserId,const ADEC_PARAM_S *pstParam);
```

​        【Note】

- Because raw and adif lack frame headers, the library cannot determine audio-frame boundaries or validate stream errors and must assume the stream is completely correct. A single incorrect bit causes a decoder error and prevents further decoding.

## Getting Version Information

### AK_MPI_ADEC_GetVersion

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the audio-decoding module version.

&emsp;&emsp;【Syntax】

```c
const AK_CHAR* AK_MPI_ADEC_GetVersion(AK_VOID);
```

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ------- | ------ |
| 0       | Success     |
| Other      | See the error codes. |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libakaudiocodec.a

&emsp;&emsp;Header: ak_adec.h

&emsp;&emsp;【Call Sequence】

&emsp;&emsp;This function may be called at any point.

### AK_MPI_ADEC_GetEncVersion

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the audio-encoding library version.

&emsp;&emsp;【Syntax】

```c
AK_CHAR *AK_MPI_ADEC_GetEncVersion(AK_VOID);
```

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ------- | ------ |
| 0       | Success     |
| Other      | See the error codes. |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_adec.a/so and libakaudiocodec.a/so, or libakaac.a/so, libakamr.a/so, and libakmp3.a/so

&emsp;&emsp;Header: ak_adec.h

&emsp;&emsp;【Call Sequence】

- Call after open.

### **AK_MPI_ADEC_SetLibPrintLevel**

&emsp;&emsp;【Description】

&emsp;&emsp;Sets the audio codec-library log level.

&emsp;&emsp;【Syntax】

```c
AK_S32 AK_MPI_ADEC_SetLibPrintLevel(AK_U32 u32PrintLevel);
```

&emsp;&emsp;【Parameters】

| Parameter | Description | Value range | Input/Output |
| ------------- | ---- | ----------------------- | ----- |
| s32PrintLevel | Log level | See ATCLIB_PRINT_LEVEL_E | Input |

【Return Value】

| **Return value** | **Description** |
| ------- | ------ |
| 0       | Success     |
| Other      | See the error codes. |

&emsp;【Error Codes】&emsp;

| **Error code**                | **Description** |
| ---------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid parameter  |

【Requirements】

&emsp;&emsp;Libraries: libmpi_adec.a/so and libakaudiocodec.a/so, or libakaac.a/so, libakamr.a/so, and libakmp3.a/so

&emsp;&emsp;Header: ak_adec.h

&emsp;&emsp;【Call Sequence】

&emsp;&emsp;This function may be called at any point.

<br/>

## Registering a Decoder

### **AK_MPI_ADEC_RegisterDecoder**

【Description】

Registers a decoder.

【Syntax】

```c
AK_S32 AK_MPI_ADEC_RegisterDecoder(ADEC_DECODE_S * pstDecode);
```

【Parameters】

| **Parameter**  | **Description**     | **Value range**        | **Input/Output** |
| --------- | ---------- | --------------- | --------- |
| pstDecode | Decoder-registration attribute structure | See ADEC_DECODE_S | Input |

【Return Value】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0       | Success         |
| Nonzero      | Failure; the return value is an error code. |

【Error Codes】

| **Error code**                 | **Description** |
| ----------------------- | ------ |
| ERROR_TYPE_POINTER_NULL | Null parameter   |
| ERROR_TYPE_INVALID_ARG  | Invalid parameter  |

【Requirements】

Libraries: libmpi_adec.a/so and libakaudiocodec.a/so, or libakaac.a/so, libakamr.a/so, and libakmp3.a/so

Headers: ak_adec.h, or adec_amr.h, adec_mp3.h, and adec_aac.h

【Call Sequence】

Call before AK_MPI_ADEC_Open.

【Example】

ADEC_ENCODE_S stMyDecoder = {0};

stMyDecoder.enType = AK_AUDIO_TYPE_MP3;

stMyDecoder.pfnDecOpen = ADEC_OpenMp3;

AK_IMP_ADEC_RegisterDecoder(&stMyDecoder);

```c
ADEC_ENCODE_S stMyDecoder = {0};
stMyDecoder.enType = AK_AUDIO_TYPE_MP3;// Decoding type
stMyDecoder.pfnDecOpen = ADEC_OpenMp3;// Decoder registration callback
ret = AK_IMP_ADEC_RegisterEncoder(&pstEncode);
    if(ret) {
        AK_BASE_PrintErrorEx(MODULE_ADEC,"AK_IMP_ADEC_RegisterEncoder failed\n");
        return ret;
    }

    ADEC_PARAM_S stAdecParam = {0};
    stAdecParam.enType = s32DecType;
    stAdecParam.enSampleBits = AK_AUDIO_SMPLE_BIT_16;
    stAdecParam.enSampleRate = s32SampleRate;
    stAdecParam.enSoundMode = s32SoundMode;


    /* Open the decoder */
    if (AK_MPI_ADEC_Open(s32AdecUserId,&stAdecParam)) {
        AK_BASE_PrintErrorEx(MODULE_ID_APP, "AK_MPI_ADEC_Open failed\n");
        return AK_FAILED;
    }
```

【Note】

- A decoding protocol cannot be registered more than once. For example, after registering an MP3 decoder, another MP3 decoder cannot be registered.
- Separate MP3, AAC, and AMR libraries and their corresponding headers are provided. The example callback functions are declared in those headers.
- For an encoding format that is not supported by default, call this interface before AK_MPI_AENC_Open to register the encoder. User-provided encoders are not currently supported.
- When assigning ADEC_DECODE_S, only ADEC_OpenXXX is currently supported; the other parameters may be omitted.

## Opening and Closing the Module

### AK_MPI_ADEC_Open

&emsp;&emsp;【Description】

&emsp;&emsp;Opens audio decoding. Multiple decoding channels are supported, with one handle per decoder and up to 4 audio channels decoded concurrently.

&emsp;&emsp;【Syntax】

```c
AK_S32 AK_MPI_ADEC_Open(AK_S32 s32AdecUserId,const ADEC_PARAM_S *pstParam);
```

&emsp;&emsp;【Parameters】

| Parameter | Description | Value range | Input/Output |
| ------------- | ---------- | ------------------------ | ----- |
| s32AdecUserId | Audio-decoding module handle ID | [0,3] | Input |
| pstParam | Audio-decoding input parameters | See struct ADEC_PARAM_S | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ------- | ------ |
| 0       | Success     |
| Other      | See the error codes. |

&emsp;&emsp;【Error Codes】

| **Error code**                   | **Description**       |
| ------------------------- | ------------ |
| ERROR_TYPE_POINTER_NULL   | Null parameter pointer       |
| ERROR_TYPE_INVALID_ARG    | Invalid parameter        |
| ERROR_ADEC_OPEN_TOO_MANY | Number of users exceeds the maximum |
| ERROR_TYPE_MALLOC_FAILED  | Malloc failed    |
| ERROR_ADEC_OPEN_LIB_ERROR | Error opening decoding library |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_adec.a/so and libakaudiocodec.a/so, or libakaac.a/so, libakamr.a/so, and libakmp3.a/so

&emsp;&emsp;Header: ak_adec.h

&emsp;&emsp;【Call Sequence】

![ADEC call sequence: Open, SendStream, GetFrame, ReleaseFrame, Close](../../../../zh_CN/software/board/middleware-api/img/adec-call-sequence.jpg)

&emsp;&emsp;【Paired Interface】

```c
AK_S32 AK_MPI_ADEC_Close(AK_S32 s32AdecUserId);
```

### AK_MPI_ADEC_Close

&emsp;&emsp;【Description】

&emsp;&emsp;Closes audio decoding.

&emsp;&emsp;【Syntax】

```c
AK_S32 AK_MPI_ADEC_Close(AK_S32 s32AdecUserId);
```

&emsp;&emsp;【Parameters】

| Parameter | Description | Value range | Input/Output |
| ------------- | ---------- | ----- | ----- |
| s32AdecUserId | Audio-decoding module handle ID | [0,3] | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0       | Success         |
| Nonzero      | Failure; the return value is an error code. |

&emsp;&emsp;【Error Codes】

| **Error code**              | **Description**         |
| -------------------- | -------------- |
| ERROR_ADEC_USER_NULL | Null user handle |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_adec.a/so and libakaudiocodec.a/so, or libakaac.a/so, libakamr.a/so, and libakmp3.a/so

&emsp;&emsp;Header: ak_adec.h

&emsp;&emsp;【Call Sequence】

![ADEC call sequence: Open, SendStream, GetFrame, ReleaseFrame, Close](../../../../zh_CN/software/board/middleware-api/img/adec-call-sequence.jpg)

&emsp;&emsp;【Paired Interface】

```c
AK_S32 AK_MPI_ADEC_Open(AK_S32 s32AdecUserId,const ADEC_PARAM_S *pstParam);
```

<br/>

## Decoding Flow

### AK_MPI_ADEC_SendStream

&emsp;&emsp;【Description】

&emsp;&emsp;Sends audio for decoding.

&emsp;&emsp;【Syntax】

```c
AK_S32 AK_MPI_ADEC_SendStream(AK_S32 s32AdecUserId, const AK_U8 *pu8Data,const AK_U32 u32Len, AK_U32 u32TimeOut);
```

&emsp;&emsp;【Parameters】

| Parameter | Description | Value range | Input/Output |
| ------------- | ---------------------------------------------------------- | ------------------------ | ----- |
| s32AdecUserId | Audio-decoding module handle ID | [0,3] | Input |
| pu8Data | Address containing the audio data to decode | Data length equals len | Input |
| u32Len | Length of the audio bitstream to decode | Less than 4096 | Input |
| u32TimeOut | Data timeout: 0 selects nonblocking mode and returns an error if no data is available;<br />a value >0 blocks for the timeout and returns an error when it expires. | 0 or blocking duration in ms [0,60000] | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0       | Success         |
| Nonzero      | Failure; the return value is an error code. |

&emsp;&emsp;【Error Codes】

| **Error code**                         | **Description**         |
| ------------------------------- | -------------- |
| ERROR_TYPE_POINTER_NULL         | Null parameter pointer         |
| ERROR_ADEC_SEND_STREAM_ERROR | Send-stream error |
| ERROR_ADEC_SEND_STREAM_NO_SPACE | Insufficient decoding space |
| ERROR_ADEC_USER_NULL            | Null user handle |
| ERROR_TYPE_INVALID_ARG          | Invalid parameter          |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_adec.a/so and libakaudiocodec.a/so, or libakaac.a/so, libakamr.a/so, and libakmp3.a/so

&emsp;&emsp;Header: ak_adec.h

&emsp;&emsp;【Call Sequence】

![ADEC call sequence: Open, SendStream, GetFrame, ReleaseFrame, Close](../../../../zh_CN/software/board/middleware-api/img/adec-call-sequence.jpg)

【Note】

​    The function is reentrant. Call it after AK_MPI_ADEC_Open.

### AK_MPI_ADEC_GetFrame

&emsp;&emsp;【Description】

&emsp;&emsp;Gets one frame of decoded data.

&emsp;&emsp;【Syntax】

```C
AK_S32 AK_MPI_ADEC_GetFrame(AK_S32 s32AdecUserId, FRAME_S *pstPcmFrame, AK_U32 u32TimeOut);
```

&emsp;&emsp;【Parameters】

| Parameter | Description | Value range | Input/Output |
| ------------- | ---------------------------------------------------------- | ------------------------ | ----- |
| s32AdecUserId | Audio-decoding module handle ID | [0,3] | Input |
| pstPcmFrame | One frame of decoded data | See struct FRAME_S | Input |
| u32TimeOut | Data timeout: 0 selects nonblocking mode and returns an error if no data is available;<br />a value >0 blocks for the timeout and returns an error when it expires. | 0 or blocking duration in ms [0,60000] | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0       | Success         |
| Nonzero      | Failure; the return value is an error code. |

&emsp;&emsp;【Error Codes】

| **Error code**                      | **Description**               |
| ---------------------------- | -------------------- |
| ERROR_TYPE_POINTER_NULL      | Null parameter pointer               |
| ERROR_TYPE_INVALID_ARG       | Invalid parameter                |
| ERROR_ADEC_STREAM_END | All decoded data has been output |
| ERROR_ADEC_USER_NULL         | Null user handle       |
| ERROR_ADEC_GET_FRAME_NO_DATA | No space in get-frame buffer |
| ERROR_ADEC_ATC_LIB_ERROR | Decoding-library error |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_adec.a/so and libakaudiocodec.a/so, or libakaac.a/so, libakamr.a/so, and libakmp3.a/so

&emsp;&emsp;Header: ak_adec.h

&emsp;&emsp;【Call Sequence】

![ADEC call sequence: Open, SendStream, GetFrame, ReleaseFrame, Close](../../../../zh_CN/software/board/middleware-api/img/adec-call-sequence.jpg)

​        【Note】

- When a decoded bitstream is bound to AO playback, sending data for decoding and obtaining decoded data for AO playback must occur in different threads. Each thread may perform only its respective send or get-and-play operation.

### AK_MPI_ADEC_ReleaseFrame

&emsp;&emsp;【Description】

&emsp;&emsp;Releases one frame of decoded data.

&emsp;&emsp;【Syntax】

```c
AK_S32 AK_MPI_ADEC_ReleaseFrame(AK_S32 s32AdecUserId, FRAME_S *pstPcmFrame);
```

&emsp;&emsp;【Parameters】

| Parameter | Description | Value range | Input/Output |
| ------------- | ----------- | ---------------- | ----- |
| s32AdecUserId | Audio-decoding module handle ID | [0,3] | Input |
| pstPcmFrame | One frame of decoded data | See struct FRAME_S | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0       | Success         |
| Nonzero      | Failure; the return value is an error code. |

&emsp;&emsp;【Error Codes】

| **Error code**                 | **Description**         |
| ----------------------- | -------------- |
| ERROR_TYPE_POINTER_NULL | Null parameter pointer         |
| ERROR_ADEC_USER_NULL    | Null user handle |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_adec.a/so and libakaudiocodec.a/so, or libakaac.a/so, libakamr.a/so, and libakmp3.a/so

&emsp;&emsp;Header: ak_adec.h

&emsp;&emsp;【Call Sequence】

![ADEC call sequence: Open, SendStream, GetFrame, ReleaseFrame, Close](../../../../zh_CN/software/board/middleware-api/img/adec-call-sequence.jpg)

<br/>

### AK_MPI_ADEC_SendEndOfStream

&emsp;&emsp;【Description】

&emsp;&emsp;Tells the decoder that all audio-decoding data has been sent.

&emsp;&emsp;【Syntax】

```c
AK_S32 AK_MPI_ADEC_SendEndofStream(AK_S32 s32AdecUserId);
```

&emsp;&emsp;【Parameters】

| **Parameter**      | **Description**     | **Value range** | **Input/Output** |
| ------------- | ---------- | -------- | --------- |
| s32AdecUserId | Audio-decoding module handle ID | [0,3] | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0       | Success         |
| Nonzero      | Failure; the return value is an error code. |

&emsp;&emsp;【Error Codes】

| **Error code**                         | **Description**         |
| ------------------------------- | -------------- |
| ERROR_ADEC_USER_NULL            | Null user handle |
| ERROR_ADEC_ATC_LIB_ERROR | Decoding-library setup error |
| ERROR_ADEC_SEND_STREAM_NO_START | Decoding data has not started being sent |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_adec.a/so and libakaudiocodec.a/so, or libakaac.a/so, libakamr.a/so, and libakmp3.a/so

&emsp;&emsp;Header: ak_adec.h

&emsp;&emsp;【Call Sequence】

![ADEC call sequence: Open, SendStream, SendEndOfStream at completion, GetFrame, ReleaseFrame, Close](../../../../zh_CN/software/board/middleware-api/img/adec-call-sequence-send-end-of-stream.jpg)

​    【Note】

- This interface sets the audio codec-library buffer to \_SD_BM_ENDING, so all data remaining in the buffer is decoded. The final decoded frame may therefore be shorter than one full frame.
- Call AK_MPI_ADEC_SendEndOfStream in the same thread as AK_MPI_ADEC_SendStream.

## Getting Buffer Status

### AK_MPI_ADEC_GetBufStatus

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the remaining and total sizes of the decoder input buffer.

&emsp;&emsp;【Syntax】

```c
AK_S32 AK_MPI_ADEC_GetBufStatus(AK_S32 s32AdecUserId, DEC_BUF_STATUS_S *pstBufStatus);
```

&emsp;&emsp;【Parameters】

| Parameter | Description | Value range | Input/Output |
| ------------- | ----------- | --------------------- | ----- |
| s32AdecUserId | Audio-decoding module handle | [0,3] | Input |
| pstBufStatus | Stores buffer data | See DEC_BUF_STATUS_S | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0       | Success         |
| Nonzero      | Failure; the return value is an error code. |

&emsp;&emsp;【Error Codes】

| **Error code**                  | **Description**         |
| ------------------------ | -------------- |
| ERROR_ADEC_USER_NULL     | Null user handle |
| ERROR_ADEC_ATC_LIB_ERROR | Failed to get decoding-library function |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_adec.a/so and libakaudiocodec.a/so, or libakaac.a/so, libakamr.a/so, and libakmp3.a/so

&emsp;&emsp;Header: ak_adec.h

## Debugging Interface

### AK_MPI_ADEC_SaveFile

&emsp;&emsp;【Description】

&emsp;&emsp;Saves intermediate files from ADEC audio processing. Four file types are saved: audio passed to ADEC, audio before it is passed to the decoding library, decoded PCM audio, and PCM audio output after ADEC processing.

&emsp;&emsp;【Syntax】

```c
AK_S32 AK_MPI_ADEC_SaveFile(AK_S32 s32AdecUserId, AUDIO_SAVE_FILE_INFO_S *pstSaveFileInfo);
```

&emsp;&emsp;【Parameters】

| Parameter | Description | Value range | Input/Output |
| --------------- | -------- | --------------------------- | ----- |
| s32AdecUserId | Audio-decoding module handle | [0,3] | Input |
| pstSaveFileInfo | Information about the file to save | See AUDIO_SAVE_FILE_INFO_S | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0       | Success         |
| Nonzero      | Failure; the return value is an error code. |

&emsp;&emsp;【Error Codes】

| **Error code**                 | **Description**         |
| ----------------------- | -------------- |
| ERROR_ADEC_USER_NULL    | Null user handle |
| ERROR_TYPE_POINTER_NULL | Null parameter pointer         |
| ERROR_TYPE_INVALID_ARG  | Invalid parameter          |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_adec.a/so and libakaudiocodec.a/so, or libakaac.a/so, libakamr.a/so, and libakmp3.a/so

&emsp;&emsp;Header: ak_adec.h

&emsp;&emsp;【Call Sequence】

![ADEC call sequence: Open, SaveFile, Close](../../../../zh_CN/software/board/middleware-api/img/adec-call-sequence-save-file.jpg)

​        【Note】

​    Call this interface when audio from ADEC processing must be saved for troubleshooting.

## Setting Decoding Attributes

### AK_MPI_ADEC_SetOutputPcmLen

&emsp;&emsp;【Description】

&emsp;&emsp;Sets the decoded output-data length. The valid range of out_pcm_len is shown below:

&emsp;【Syntax】

```C
AK_S32 AK_MPI_ADEC_SetOutputPcmLen(AK_S32 s32AdecUserId, AK_U32 u32OutPcmLen);
```

&emsp;&emsp;【Parameters】

| Parameter | Description | Value range | Input/Output |
| ------------- | ------------------- | ----------- | ----- |
| s32AdecUserId | Audio-decoding module handle ID | [0,3] | Input |
| u32OutPcmLen | Length of decoded output data, in bytes | [320, 4096] | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0       | Success         |
| Nonzero      | Failure; the return value is an error code. |

&emsp;&emsp;【Error Codes】

| Error code | Description |
| ----------------------- | -------------- |
| ERROR_TYPE_POINTER_NULL | Null parameter pointer         |
| ERROR_TYPE_INVALID_ARG | Invalid parameter |
| ERROR_ADEC_USER_NULL    | Null user handle |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_adec.a/so and libakaudiocodec.a/so, or libakaac.a/so, libakamr.a/so, and libakmp3.a/so

&emsp;&emsp;Header: ak_adec.h

&emsp;&emsp;【Call Sequence】

![ADEC call sequence: Open, SetOutputPcmLen, SendStream, GetFrame, ReleaseFrame, Close](../../../../zh_CN/software/board/middleware-api/img/adec-call-sequence-set-output-pcm-len.jpg)

​    【Note】

​    If this interface is not called, each decoded output uses the default length.

<br/>

## Clearing the Buffer

### AK_MPI_ADEC_ClearDecodeBuf

&emsp;&emsp;【Description】

&emsp;&emsp;Clears the decoding buffer. After decoding is paused, clear the buffer; otherwise, data from the previous decoding operation remains during the next playback.

&emsp;&emsp;【Syntax】

```C
AK_S32 AK_MPI_ADEC_ClearDecodeBuf(AK_S32 s32AdecUserId);
```

&emsp;&emsp;【Parameters】

| Parameter | Description | Value range | Input/Output |
| ------------- | ---------- | ----- | ----- |
| s32AdecUserId | Audio-decoding module handle ID | [0,3] | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0       | Success         |
| Nonzero      | Failure; the return value is an error code. |

&emsp;&emsp;【Error Codes】

| **Error code**                  | **Description**          |
| ------------------------ | --------------- |
| ERROR_TYPE_POINTER_NULL  | Null parameter pointer          |
| ERROR_ADEC_ATC_LIB_ERROR | Decoding-library setup error |
| ERROR_ADEC_RB_ERROR | Ring-buffer operation error |
| ERROR_ADEC_USER_NULL     | Null user handle  |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_adec.a/so and libakaudiocodec.a/so, or libakaac.a/so, libakamr.a/so, and libakmp3.a/so

&emsp;&emsp;Header: ak_adec.h

&emsp;&emsp;【Call Sequence】

![ADEC call sequence: Open, SendStream, GetFrame, ReleaseFrame, ClearDecodeBuf, Close](../../../../zh_CN/software/board/middleware-api/img/adec-call-sequence-clear-decode-buf.jpg)

​        【Note】

<br/>

## Interface Call Dependencies

&emsp;&emsp;The ADEC interfaces have the call dependencies shown below:

| **Interface** | **Dependency** |
| ---------------------------- | ------------------------------- |
| AK_MPI_ADEC_GetVersion | None |
| AK_MPI_ADEC_Open             | -                               |
| AK_MPI_ADEC_SetOutputPcmLen | May be called after AK_MPI_ADEC_Opem |
| AK_MPI_ADEC_SendStream | May be called after AK_MPI_ADEC_Opem |
| AK_MPI_ADEC_GetFrame | May be called after AK_MPI_ADEC_Opem |
| AK_MPI_ADEC_ReleaseFrame | Call after AK_MPI_ADEC_GetFrame |
| AK_MPI_ADEC_SendEndOfStream | Call after AK_MPI_ADEC_SendStream; takes effect immediately |
| AK_MPI_ADEC_ClearDecodeBuf | Call after AK_MPI_ADEC_SendStream; takes effect immediately |
| AK_MPI_ADEC_Close | May be called at any point after AK_MPI_ADEC_Opem; takes effect immediately |
| AK_MPI_ADEC_SaveFile | May be called at any point after AK_MPI_ADEC_Opem; takes effect immediately |
| AK_MPI_ADEC_GetBufStatus | May be called at any point after AK_MPI_ADEC_Opem; takes effect immediately |
| AK_MPI_ADEC_RegisterDecoder | May be called before AK_MPI_ADEC_Opem |
| AK_MPI_AENC_SetLibPrintLevel | No dependency; recommended before AK_MPI_ADEC_Opem |

> **Source note:** In this source-derived table, `AK_MPI_ADEC_Opem` means `AK_MPI_ADEC_Open`, and `AK_MPI_AENC_SetLibPrintLevel` means the page/header-declared `AK_MPI_ADEC_SetLibPrintLevel`.

## ak_adec_sample Usage Example

### Sample Command and Parameters

Before running this sample, load ak_pcm.ko with insmod. It is normally loaded by default at startup.

| Short option | Long option | Description |
| -------- | -------------- | ----------------------------------------- |
| h | help | Prints help. |
| s | sample-rate | Sample rate; supports 8000 Hz, 16000 Hz, 44100 Hz, and 48000 Hz. |
| d | dev-sel | Playback device: 0:DAC, 1:I2S0. |
| p | play-file | Name of the file to decode and play. |
| f | config-file | Absolute path and name of the configuration file. |
| t | config-section | Configuration section string to select. |
| e | decode-type | Decoding type [mp3 aac amr g711a g711u pcm]. |

### Sample Storage and File Naming

(1) Sample input uses MP3 format by default.
(2) The default sample input is /mnt/adec_test.mp3.

### Example

 ak_adec_sample -s 16000 -d 0 -e mp3 -p /mnt/xxx.mp3 -f /etc/config/audio_config.ini -t def_far

## /var/platform Description

The /var/platform directory exposes the current module configuration parameters and status. Its parameters are described below.

### param

| Parameter | Description |
| ---------- | ------- |
| OutPcmLen | Decoded output length |
| SampleRate | Sample rate |
| SoundMode | Channel mode |
| SampleBit | Sample precision |
| UserCnt | Number of users |
| AdecType | Decoding type |

### stat

| Parameter | Description |
| ----------------- | -------- |
| Mp3Version | MP3 library version |
| AudioCodecVersion | Codec library version |
| AdecMpiVersion | Platform decoding-library version |

<br/>

## Error Codes

| Error code | Macro | Meaning |
| ---------- | ------------------------------- | ------------ |
| 0x10000000 | ERROR_ADEC_OPEN_LIB_ERROR | Failed to open library |
| 0x10000001 | ERROR_ADEC_CLOSE_LIB_ERROR | Failed to close library |
| 0x10000002 | ERROR_ADEC_OPEN_TOO_MANY | Too many open handles |
| 0x10000003 | ERROR_ADEC_USER_NULL | Null user |
| 0x10000004 | ERROR_ADEC_RB_ERROR | RB error |
| 0x10000005 | ERROR_ADEC_ATC_LIB_ERROR | Algorithm-library error |
| 0x10000006 | ERROR_ADEC_SEND_STREAM_ERROR | Error sending stream |
| 0x10000007 | ERROR_ADEC_GET_FRAME_NO_DATA | No data when getting frame |
| 0x10000008 | ERROR_ADEC_SEND_STREAM_NO_SPACE | No space for sending stream |
| 0x10000009 | ERROR_ADEC_STREAM_END | End of stream |
| 0x1000000a | ERROR_ADEC_SEND_STREAM_NO_START | Stream sending not started |

<br/>
