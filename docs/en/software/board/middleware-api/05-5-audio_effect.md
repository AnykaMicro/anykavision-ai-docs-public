# Audio Effects

## Overview

&emsp;&emsp;The audio quality-enhancement module (AUDIO_EFFECT) improves the raw PCM data from the AI and AO modules through resampling (RES), digital amplification (ASLC), and equalization (EQ). It also supports detection processing such as sound-level detection (VAD), software-based crying detection (CRY), NPU-based crying detection (AI_CRY, currently supporting only a 16 kHz sample rate), and keyword spotting (KWS, not currently supported).

<br/>

## API Reference

&emsp;&emsp;This module provides the APIs listed below.

### Structure List

| **Data structure**                       | **Description**                                             |
| ---------------------------------- | ---------------------------------------------------- |
| AUDIO_DATA_ATTR_S | Basic audio attributes |
| AUDIO_EFFECT_TYPE_E | Audio-effect processing type |
| AUDIO_EFFECT_REG_S | Registers RES/VAD/CRY/AI_CRY effect modules; ASLC and EQ do not require registration |
| AUDIO_EQ_ATTR_S | Audio equalizer parameters |
| AUDIO_ASLC_ATTR_S | Audio digital-amplification parameters |
| ARRAY_GEOMETRY_S | Microphone-array geometry |
| AUDIO_SSL_ATTR_S | Sound-source localization parameters |
| AUDIO_LSSL_ATTR_S | Uniform linear sound-source localization parameters |
| AUDIO_VAD_ATTR_S | Sound-level detection parameters |
| AUDIO_CRY_ATTR_S | Crying-detection parameters |
| AUDIO_AI_CRY_ATTR_S | AI crying-detection parameters |
| AUDIO_AI_KWS_ATTR_S | Keyword-spotting parameters |
| AUDIO_AI_KWSASR_ATTR_S | Keyword-spotting ASR parameters |
| SOUND_SPHERICAL_DIRECTION | Sound-source position in three-dimensional space |
| AUDIO_EFFECT_RESULT_S | AUDIO_EFFECT processing result |
| AUDIO_EFFECT_DATA_PROCESS_RESULT_S | Data-processing result shared by RES/EQ/ASLC |
| AUDIO_VAD_RESULT_S | Sound-level detection result |
| AUDIO_CRY_RESULT_S | Software-based crying-detection result |
| AUDIO_AI_CRY_RESULT_S | NPU-based crying-detection result |
| AUDIO_SSL_RESULT_S | Sound-source localization result |
| AUDIO_LSSL_RESULT_S | Uniform linear-array localization result |
| RESULT_S | EQ/ASLC/RES result |
| AUDIO_EFFECT_RESULT_S | Audio-effect processing result |
| AUDIO_AIKWS_RESULT_S | Keyword-spotting result |
| AUDIO_AIKWSASR_RESULT_S | Keyword-spotting ASR result |

<br/>

### Function List

| **Function**                         | **Description**                                                     |
| ------------------------------------ | ------------------------------------------------------------ |
| AK_MPI_AUDIO_EFFECT_GetVersion | Gets the module version. |
| AK_MPI_AUDIO_EFFECT_GetFilterVersion | Gets the libakaudiofilter library version. |
| AK_MPI_AUDIO_EFFECT_Register | Registers an audio-effect processing API. |
| AK_MPI_AUDIO_EFFECT_Init | Initializes audio-effect processing. |
| AK_MPI_AUDIO_EFFECT_DeInit | Deinitializes audio-effect processing. |
| AK_MPI_AUDIO_EFFECT_Process | Processes input audio-source data and outputs processed audio, or detects content in the audio and outputs detection results. |
| AK_MPI_AUDIO_EFFECT_SetLibPrintLevel | Sets the libaudiofilter log priority in the audio-effect module. |
| AK_MPI_AUDIO_EFFECT_SetAttr | Sets audio-effect parameters. |
| AK_MPI_AUDIO_EFFECT_GetAttr | Gets audio-effect parameters. |

<br/>

### Error Codes

AUDIO_EFFECT_ERROR_TYPE_E

| Error code | Description |
| ------------------------------------------------------------ | -------------------- |
| ERROR_AUDIO_EFFECT_OPEN_LIB_ERROR<br />= (MODULE_ID_AUDIO_EFFECT << 24) + 0 | Failed to open filter library |
| ERROR_AUDIO_EFFECT_LIB_ERROR | Filter interface call failed |
| ERROR_AUDIO_EFFECT_OUTBUF_LEN_ERROR | Invalid output-buffer length |
| ERROR_AUDIO_EFFECT_NO_MATCH_VAD_TYPE | VAD TYPE mismatch |
| ERROR_AUDIO_EFFECT_RESULT_NO_RETURN | No result returned |

## Structures and Enumerations

### AUDIO_EFFECT_ERROR_TYPE_E

&emsp;&emsp;【Notes】

&emsp;&emsp;AUDIO EFFECT error codes.

&emsp;&emsp;【Definition】

```c
enum akAUDIO_EFFECT_ERROR_TYPE_E
{
    ERROR_AUDIO_EFFECT_OPEN_LIB_ERROR = (MODULE_ID_AUDIO_EFFECT << 24) + 0,
    ERROR_AUDIO_EFFECT_LIB_ERROR,
    ERROR_AUDIO_EFFECT_OUTBUF_LEN_ERROR,
    ERROR_AUDIO_EFFECT_NO_MATCH_VAD_TYPE,
    ERROR_AUDIO_EFFECT_RESULT_NO_RETURN,
} AUDIO_EFFECT_ERROR_TYPE_E;
```

【Members】

| **Member**                         | **Description**                    |
| ------------------------------------ | --------------------------- |
| ERROR_AUDIO_EFFECT_OPEN_LIB_ERROR | Error opening filter library |
| ERROR_AUDIO_EFFECT_LIB_ERROR | Error calling filter-library interface |
| ERROR_AUDIO_EFFECT_OUTBUF_LEN_ERROR | Invalid outbuf length |
| ERROR_AUDIO_EFFECT_NO_MATCH_VAD_TYPE | No match for configured VAD type parameter |
| ERROR_AUDIO_EFFECT_RESULT_NO_RETURN | No result returned |

&emsp;&emsp;【Related Functions】

<br/>

### AUDIO_EFFECT_USER_MAX_NUM

&emsp;&emsp;【Notes】

&emsp;&emsp;Maximum number of AUDIO EFFECT channels.

&emsp;&emsp;【Definition】

```c
#define     AUDIO_EFFECT_USER_MAX_NUM   10
```

<br/>

### AUDIO_EFFECT_USER_MAX_NUM

&emsp;&emsp;【Notes】

&emsp;&emsp;Maximum number of microphones supported by audio-effect processing.

&emsp;&emsp;【Definition】

```c
#define     FILTER_ALGORITHM_MAX_MIC_NUM   4
```

> **Source note:** The second `AUDIO_EFFECT_USER_MAX_NUM` heading is a source typo; its definition is `FILTER_ALGORITHM_MAX_MIC_NUM`. Repeated source-derived parameter ranges that use `AUDIO_EFFECT_USER_NUM` mean the header-declared `AUDIO_EFFECT_USER_MAX_NUM`.

<br/>

### **AUDIO_DATA_ATTR_S**

&emsp;&emsp;【Notes】

&emsp;&emsp;Basic audio attributes.

&emsp;&emsp;【Definition】

```c
    typedef struct akAUDIO_DATA_ATTR_S
    {
        AUDIO_SAMPLE_RATE_E 		enSampleRate;
        AUDIO_SAMPLE_BIT_E  		enSampleBits;
        AUDIO_SOUND_MODE_E  		enSoundMode;
    } AUDIO_DATA_ATTR_S;
```

&emsp;&emsp;【Members】

| **Member** | **Description**     |
| ------------ | ------------ |
| enSampleRate | Audio sample rate |
| enSampleBits | Audio sample precision |
| enSoundMode | Number of audio channels |

&emsp;&emsp;【Related Functions】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_Init(	AK_S32      			s32EffectUserId,
                                    AUDIO_DATA_ATTR_S     	*pstAudioDataAttr,
                                    AUDIO_EFFECT_TYPE_E     enEffectType,
                                    AK_CHAR                 *pchFile,
                                    AK_CHAR                 *pchSection );

```

<br/>

### AUDIO_EFFECT_TYPE_E

&emsp;&emsp;【Notes】

&emsp;&emsp;Audio-effect processing types.

&emsp;&emsp;【Definition】

```c
	typedef enum akAUDIO_EFFECT_TYPE_E
	{
        AK_AUDIO_RESAMPLE = 0,
        AK_AUDIO_VAD,
        AK_AUDIO_CRY,
        AK_AUDIO_ASLC,
        AK_AUDIO_EQ,
        AK_AUDIO_AI_CRY,
		AK_AUDIO_SSL,
		AK_AUDIO_LSSL,
		AK_AUDIO_AI_KWS,
        AK_AUDIO_AI_KWSASR,
        AK_AUDIO_TYPE_NUM,
	} AUDIO_EFFECT_TYPE_E;
```

&emsp;&emsp;【Members】

| **Member**       | **Description**                                     |
| ------------------ | -------------------------------------------- |
| AK_AUDIO_RESAMPLE | Resampling effect type ID |
| AK_AUDIO_VAD | Sound-level detection type ID |
| AK_AUDIO_CRY | Software-based crying-detection type ID |
| AK_AUDIO_ASLC | Digital volume-amplification type ID |
| AK_AUDIO_EQ | Audio equalizer type ID |
| AK_AUDIO_AI_CRY | NPU-based crying-detection type ID (currently supports only a 16 kHz sample rate) |
| AK_AUDIO_SSL | Sound-source localization type ID |
| AK_AUDIO_LSSL | Uniform linear-array sound-source localization ID |
| AK_AUDIO_AI_KWS | Keyword-spotting ID |
| AK_AUDIO_AI_KWSASR | Keyword-spotting ASR ID |
| AK_AUDIO_TYPE_NUM | Total number of audio-effect processing types |

&emsp;&emsp;【Related Functions】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_Init(	AK_S32      			s32EffectUserId,
                                    AUDIO_DATA_ATTR_S     	*pstAudioDataAttr,
                                    AUDIO_EFFECT_TYPE_E     enEffectType,
                                    AK_CHAR                 *pchFile,
                                    AK_CHAR                 *pchSection );

```

<br/>

### AUDIO_EFFECT_REG_S

&emsp;&emsp;【Notes】

&emsp;&emsp;Registers an audio-effect module.

&emsp;&emsp;【Definition】

```c
typedef struct akAUDIO_EFFECT_REG_S {
    AUDIO_EFFECT_TYPE_E enEffectType;

    AK_VOID* (*EffectOpen)(
        AK_VOID             *pstOpenArg,
        AK_VOID             *pstEffectAttr
    );

    AK_S32 (*EffectClose)(AK_VOID *pstEffectHandle);

    AK_S32 (*EffectProcess)(
        AK_VOID             *pstEffectHandle,
        AK_VOID             *pstProcArg
    );
} AUDIO_EFFECT_REG_S;

```

&emsp;&emsp;【Members】

| **Member**  | **Description**                              |
| ------------- | ------------------------------------- |
| enEffectType | Audio-effect type; see AUDIO_EFFECT_TYPE_E |
| EffectOpen | Open callback; see the sublibrary header |
| EffectClose | Close callback; see the sublibrary header |
| EffectProcess | Audio-effect processing callback; see the sublibrary header |

&emsp;&emsp;【Related Functions】

```c
    AK_S32 AK_MPI_AUDIO_EFFECT_Register(AUDIO_EFFECT_REG_S *pstAudioEffect);

```

​	</br>

### AUDIO_SSL_ATTR_S

&emsp;&emsp;【Notes】

&emsp;&emsp;Sound-source localization attributes.

&emsp;&emsp;【Definition】

```c
typedef struct akAUDIO_SSL_ATTR_S {
    AK_U16                  u16FrameSize;   // frame size in bytes
    AK_U16                  u16Reserve1;//u16SoundSpeed;  // speed of sound // Notice: no use
    AK_U32                  u32Reserve2;//u32SrcNum;      // number of sound sources  // Notice: no use
    ARRAY_GEOMETRY_S        stArrayGeometry;
    AK_S32                  s32Reserve3;
} AUDIO_SSL_ATTR_S;
```

&emsp;&emsp;【Members】

| **Member**    | **Description** |
| --------------- | -------- |
| u16FrameSize | Frame size |
| u16Reserve1 | Reserved parameter |
| u32Reserve2 | Reserved parameter |
| stArrayGeometry | Microphone positions |
| s32Reserve3 | Reserved parameter |

&emsp;&emsp;【Related Functions】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_SetAttr( AK_S32                  s32EffectUserId,
                                    AUDIO_EFFECT_TYPE_E     enEffectType,
                                    AUDIO_EFFECT_ATTR_S     *pstEffectAttr );
AK_S32 AK_MPI_AUDIO_EFFECT_GetAttr(AK_S32                  s32EffectUserId,
                                   AUDIO_EFFECT_TYPE_E     enEffectType,
                                   AUDIO_EFFECT_ATTR_S     *pstEffectAttr);

```

​	【Note】

The related function interfaces do not currently support configuring this parameter.

</br>

### AUDIO_LSSL_ATTR_S

&emsp;&emsp;【Notes】

&emsp;&emsp;Uniform linear sound-source localization attributes.

&emsp;&emsp;【Definition】

```c
typedef struct akAUDIO_LSSL_ATTR_S {
    AK_U16                  u16FrameSize;   // frame size in bytes
    AK_U16                  u16Reserve;//u16SoundSpeed;  // speed of sound   // Notice: no use
    AK_U16                  u16NumMic;      // number of mic
    AK_U16                  u16MicSpace;
    AK_S32                  s32Thresh;
    AK_S32                  s32Level;
    AK_S32                  s32Reserve;
} AUDIO_LSSL_ATTR_S;
```

&emsp;&emsp;【Members】

| **Member**    | **Description**          |
| --------------- | ----------------- |
| u16FrameSize | Frame size |
| u16Reserve | Reserved parameter |
| u16NumMic | Number of microphones |
| stArrayGeometry | Microphone positions |
| u16MicSpace | Distance between microphones |
| s32Thresh | Threshold [0.00, 1.00] |
| s32Level | Sensitivity level [0,4] |
| s32Reserve | Reserved parameter |

&emsp;&emsp;【Related Functions】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_SetAttr( AK_S32                  s32EffectUserId,
                                    AUDIO_EFFECT_TYPE_E     enEffectType,
                                    AUDIO_EFFECT_ATTR_S     *pstEffectAttr );
AK_S32 AK_MPI_AUDIO_EFFECT_GetAttr(AK_S32                  s32EffectUserId,
                                   AUDIO_EFFECT_TYPE_E     enEffectType,
                                   AUDIO_EFFECT_ATTR_S     *pstEffectAttr);

```

​	【Note】

The related function interfaces do not currently support configuring this parameter.

</br>

### AUDIO_AI_KWS_ATTR_S

&emsp;&emsp;【Notes】

&emsp;&emsp;Keyword-spotting attributes.

&emsp;&emsp;【Definition】

```c
typedef struct akAUDIO_AI_KWS_ATTR_S {
    AK_U32                  u32AiKwsEna;     // enable AI keyword spotting
    AK_U16                  u16frameShift;   // Frame-step length in samples. 0: use default
    AK_U16                  u16frameSize;    // Frame length in samples. 0: use default
    AK_U16                  u16FftSize;      // FFT length in samples. 0: use default
    AK_U16                  u16Frames;
    AK_U16                  u16Bands;
    AK_U16                  s16Reserve;
    AK_S8                   *ps8ModelName;  // AI keyword-detection model name. 0: use default "model_aikws"
    AK_S32                  s32Reserve;
} AUDIO_AI_KWS_ATTR_S;
```

&emsp;&emsp;【Members】

| **Member**  | **Description**             |
| ------------- | -------------------- |
| u32AiKwsEna | Keyword-spotting length |
| u16frameShift | Frame-step length |
| u16frameSize | Frame length |
| u16FftSize | FFT length |
| u16Frames | Reserved parameter |
| u16Bands | Reserved parameter |
| s16Reserve | Reserved parameter |
| ps8ModelName | AI keyword-detection model name |
| s32Reserve | Reserved parameter |

&emsp;&emsp;【Related Functions】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_SetAttr( AK_S32                  s32EffectUserId,
                                    AUDIO_EFFECT_TYPE_E     enEffectType,
                                    AUDIO_EFFECT_ATTR_S     *pstEffectAttr );
AK_S32 AK_MPI_AUDIO_EFFECT_GetAttr(AK_S32                  s32EffectUserId,
                                   AUDIO_EFFECT_TYPE_E     enEffectType,
                                   AUDIO_EFFECT_ATTR_S     *pstEffectAttr);

```

​	【Note】

The related function interfaces do not currently support configuring this parameter.

</br>

### AUDIO_AI_KWS_ATTR_S

&emsp;&emsp;【Notes】

&emsp;&emsp;Keyword-spotting attributes.

&emsp;&emsp;【Definition】

```c
typedef struct akAUDIO_AI_KWSASR_ATTR_S {
    AK_U32                  u32AiKwsAsrEna;   // enable AI keyword spotting ASR
    AK_U16                  u16frameShift;   // Frame-step length in samples. 0: use default
    AK_U16                  u16frameSize;    // Frame length in samples. 0: use default
    AK_U16                  u16FftSize;      // FFT length in samples. 0: use default
    AK_U16                  u16Frames;
    AK_U16                  u16Bands;
    AK_U16                  s16Reserve;
    AK_S8                   *ps8ModelName;  // AI keyword-detection model name. 0: use default "model_aikws"
    AK_S32                  s32Reserve;
} AUDIO_AI_KWSASR_ATTR_S;
```

&emsp;&emsp;【Members】

| **Member**   | **Description**             |
| -------------- | -------------------- |
| u32AiKwsAsrEna | Keyword-spotting ASR length |
| u16frameShift | Frame-step length |
| u16frameSize | Frame length |
| u16FftSize | FFT length |
| u16Frames | Reserved parameter |
| u16Bands | Reserved parameter |
| s16Reserve | Reserved parameter |
| ps8ModelName | AI keyword-detection model name |
| s32Reserve | Reserved parameter |

&emsp;&emsp;【Related Functions】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_SetAttr( AK_S32                  s32EffectUserId,
                                    AUDIO_EFFECT_TYPE_E     enEffectType,
                                    AUDIO_EFFECT_ATTR_S     *pstEffectAttr );
AK_S32 AK_MPI_AUDIO_EFFECT_GetAttr(AK_S32                  s32EffectUserId,
                                   AUDIO_EFFECT_TYPE_E     enEffectType,
                                   AUDIO_EFFECT_ATTR_S     *pstEffectAttr);

```

​	【Note】

The related function interfaces do not currently support configuring this parameter.

​	</br>

### AUDIO_AI_CRY_ATTR_S

&emsp;&emsp;【Notes】

&emsp;&emsp;AI crying-detection attributes.

&emsp;&emsp;【Definition】

```c
typedef struct akAUDIO_AI_CRY_ATTR_S {
    AK_U16          u16FrameSize;    // samples. 0: use default
    AK_U16          u16FrameShift;   // samples. 0: use default
    AK_U16          u16FftSize;      // samples. 0: use default
    AK_U16          u16NBands;       // 0: use default
    AK_U16          u16NFrames;      // 0: use default
    AK_U32          u32LowFreq;      // 0: use default
    AK_U32          u32HighFreq;     // 0: use default
    AK_S8           *ps8ModelName;   // 0: use default mobilenetv1_aicrydet_opt
    AK_S32          s32Reserve;      //
    AK_U32          u32Probe;        // probe flag
    AK_S32          s32Reserve1;
    AK_S32          s32Level;        //cry detect level [0-5], 0: use default level 0
} AUDIO_AI_CRY_ATTR_S;
```

&emsp;&emsp;【Members】

| **Member**  | **Description**                |
| ------------- | ----------------------- |
| u16FrameSize | Reserved parameter; 0: use default |
| u16FrameShift | Reserved parameter; 0: use default |
| u16FftSize | Reserved parameter; 0: use default |
| u16NBands | Reserved parameter; 0: use default |
| u16NFrames | Reserved parameter; 0: use default |
| u32LowFreq | Reserved parameter; 0: use default |
| u32HighFreq | Reserved parameter; 0: use default |
| ps8ModelName | Crying-detection model name |
| s32Reserve | Reserved parameter |
| u32Probe | Reserved parameter |
| s32Reserve1 | Reserved parameter; 0: use default |
| s32Level | Detection level [0-5]; default 0 |

&emsp;&emsp;【Related Functions】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_SetAttr( AK_S32                  s32EffectUserId,
                                    AUDIO_EFFECT_TYPE_E     enEffectType,
                                    AUDIO_EFFECT_ATTR_S     *pstEffectAttr );
AK_S32 AK_MPI_AUDIO_EFFECT_GetAttr(AK_S32                  s32EffectUserId,
                                   AUDIO_EFFECT_TYPE_E     enEffectType,
                                   AUDIO_EFFECT_ATTR_S     *pstEffectAttr);

```

​	【Note】

The related function interfaces do not currently support configuring this parameter.

​	</br>

### AUDIO_CRY_ATTR_S

&emsp;&emsp;【Notes】

&emsp;&emsp;Traditional crying-detection algorithm attributes.

&emsp;&emsp;【Definition】

```c
typedef struct akAUDIO_CRY_ATTR_S {
    AK_S32          s32Reserve1;
    AK_S32          s32CryThresh;
    AK_S32          s32CryLevel;
    AK_S32          s32Reserve2;
} AUDIO_CRY_ATTR_S;
```

&emsp;&emsp;【Members】

| **Member** | **Description**   |
| ------------ | ---------- |
| s32Reserve1 | Reserved parameter |
| s32CryThresh | Threshold setting |
| s32CryLevel | Sensitivity level |
| s32Reserve2 | Reserved parameter |

&emsp;&emsp;【Related Functions】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_SetAttr( AK_S32                  s32EffectUserId,
                                    AUDIO_EFFECT_TYPE_E     enEffectType,
                                    AUDIO_EFFECT_ATTR_S     *pstEffectAttr );
AK_S32 AK_MPI_AUDIO_EFFECT_GetAttr(AK_S32                  s32EffectUserId,
                                   AUDIO_EFFECT_TYPE_E     enEffectType,
                                   AUDIO_EFFECT_ATTR_S     *pstEffectAttr);

```

​	【Note】

The related function interfaces do not currently support configuring this parameter.

​	</br>

### AUDIO_VAD_ATTR_S

&emsp;&emsp;【Notes】

&emsp;&emsp;Sound-level detection attributes.

&emsp;&emsp;【Definition】

```c
typedef struct akAUDIO_VAD_ATTR_S {
    AK_S32          s32Reserve1;
    AK_U32          u32Probe;
    AK_S32          s32VadThresh; // threshold of signal amplitude. use the form of AK32Q15(x.xx) to set it
    AK_S32          s32VadLevel;  // sensitivity level.[0, 4],smaller is more sensible
    AK_S32          s32Reserve2;
} AUDIO_VAD_ATTR_S;
```

&emsp;&emsp;【Members】

| **Member** | **Description**                |
| ------------ | ----------------------- |
| s32Reserve1 | Reserved parameter |
| u32Probe | Reserved parameter; 0: use default |
| s32VadThresh | Threshold [0.00, 1.00] |
| s32VadLevel | Sensitivity level [0,4] |
| s32Reserve2 | Reserved parameter |

&emsp;&emsp;【Related Functions】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_SetAttr( AK_S32                  s32EffectUserId,
                                    AUDIO_EFFECT_TYPE_E     enEffectType,
                                    AUDIO_EFFECT_ATTR_S     *pstEffectAttr );
AK_S32 AK_MPI_AUDIO_EFFECT_GetAttr(AK_S32                  s32EffectUserId,
                                   AUDIO_EFFECT_TYPE_E     enEffectType,
                                   AUDIO_EFFECT_ATTR_S     *pstEffectAttr);

```

​	【Note】

The related function interfaces do not currently support configuring this parameter.

​	</br>

### AUDIO_EFFECT_RESULT_S

&emsp;&emsp;【Notes】

&emsp;&emsp;AUDIO_EFFECT processing result.

&emsp;&emsp;【Definition】

```c
typedef struct akAUDIO_EFFECT_RESULT_S {
    AUDIO_EFFECT_TYPE_E                         u32EffectType;
    /* sizeof(AUDIO_EFFECT_DATA_PROCESS_RESULT_S) / sizeof(AUDIO_XXX_RESULT_S) */
    AK_U32                                      u32UnionBufSize;
    RESULT_S                                    unEffectResult;
} AUDIO_EFFECT_RESULT_S;
```

&emsp;&emsp;【Members】

| **Member**    | **Description**                                                     |
| --------------- | ------------------------------------------------------------ |
| u32EffectType | Required; AUDIO_EFFECT_TYPE_E |
| u32UnionBufSize | Required; length of the corresponding union.<br />For VAD, for example, set this to sizeof(AUDIO_VAD_RESULT_S). When parsing a specific result, cast to the VAD union to obtain it. |
| unEffectResult | Union of data-processing and detection results |

&emsp;&emsp;【Related Functions】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_Process( AK_S32                  s32EffectUserId,
                                    AK_U8                   *pu8InBuf,
                                    AK_U32                  u32InDataLen,
                                    AUDIO_EFFECT_RESULT_S   *pstEffectResult );

```

<br/>

### AUDIO_EFFECT_DATA_PROCESS_RESULT_S

&emsp;&emsp;【Notes】

&emsp;&emsp;Processing result for data-processing effects such as RES/ASLC/EQ.

&emsp;&emsp;【Definition】

```c
typedef struct akAUDIO_EFFECT_DATA_PROCESS_RESULT_S
{
    AK_U8           *pu8OutBuf;
    AK_U32          u32OutDataLen;
    AK_S32          s32Reserve;
} AUDIO_EFFECT_DATA_PROCESS_RESULT_S;
```

&emsp;&emsp;【Members】

| **Member**  | **Description**           |
| ------------- | ------------------ |
| pu8OutBuf | Start address of processed data |
| u32OutDataLen | Length of processed data |
| s32Reserve | Reserved |

&emsp;&emsp;【Related Functions】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_Process( AK_S32                  s32EffectUserId,
                                    AK_U8                   *pu8InBuf,
                                    AK_U32                  u32InDataLen,
                                    AUDIO_EFFECT_RESULT_S   *pstEffectResult );

```

<br/>

### AUDIO_VAD_RESULT_S

&emsp;&emsp;【Notes】

&emsp;&emsp;Sound-level detection result.

&emsp;&emsp;【Definition】

```c
/* vad result output*/
typedef struct akAUDIO_VAD_RESULT_S {
    AK_U64          u64TimeOffset;
    AK_S32          s32Reserve;
} AUDIO_VAD_RESULT_S;

```

&emsp;&emsp;【Members】

| **Member**  | **Description**                             |
| ------------- | ------------------------------------ |
| u64TimeOffset | Time offset of the detected result within the input frame |
| s32Reserve | Detailed sound-level detection result; not currently supported |

&emsp;&emsp;【Related Functions】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_Process( AK_S32                  s32EffectUserId,
                                    AK_U8                   *pu8InBuf,
                                    AK_U32                  u32InDataLen,
                                    AUDIO_EFFECT_RESULT_S   *pstEffectResult );

```

<br/>

### AUDIO_CRY_RESULT_S

&emsp;&emsp;【Notes】

&emsp;&emsp;Traditional-algorithm crying-detection result.

&emsp;&emsp;【Definition】

```c
typedef struct akAUDIO_CRY_RESULT_S {
    AK_U64          u64TimeOffset;
    AK_S32          s32Reserve;
} AUDIO_CRY_RESULT_S;
```

&emsp;&emsp;【Members】

| **Member**  | **Description**                             |
| ------------- | ------------------------------------ |
| u64TimeOffset | Time offset of the detected crying result within the input frame |
| s32Reserve | Reserved |

&emsp;&emsp;【Related Functions】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_Process( AK_S32                  s32EffectUserId,
                                    AK_U8                   *pu8InBuf,
                                    AK_U32                  u32InDataLen,
                                    AUDIO_EFFECT_RESULT_S   *pstEffectResult );

```

<br/>

### AUDIO_AI_CRY_RESULT_S

&emsp;&emsp;【Notes】

&emsp;&emsp;NPU-based crying-detection result.

&emsp;&emsp;【Definition】

```c
/* AI cry result output*/
typedef struct akAUDIO_AICRY_RESULT_S {
    AK_U64          u64TimeOffset;
    AK_S32          s32Reserve;
} AUDIO_AICRY_RESULT_S;
```

&emsp;&emsp;【Members】

| **Member**  | **Description**                             |
| ------------- | ------------------------------------ |
| u64TimeOffset | Time offset of the detected crying result within the input frame |
| s32Reserve | Reserved |

&emsp;&emsp;【Related Functions】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_Process( AK_S32                  s32EffectUserId,
                                    AK_U8                   *pu8InBuf,
                                    AK_U32                  u32InDataLen,
                                    AUDIO_EFFECT_RESULT_S   *pstEffectResult );

```

<br/>

### AUDIO_SSL_RESULT_S

&emsp;&emsp;【Notes】

&emsp;&emsp;Sound-source localization output.

&emsp;&emsp;【Definition】

```c
/* SSL result output*/
typedef struct akAUDIO_SSL_RESULT_S {
    AK_U64                      u64TimeOffset;
    AK_U32                      u32SrcNum;      // number of sound sources
    SOUND_SPHERICAL_DIRECTION   *pastSndSrcDir;
    AK_S32                      s32Reserve;
} AUDIO_SSL_RESULT_S;
```

&emsp;&emsp;【Members】

| **Member**              | **Description**                         |
| ------------------------- | -------------------------------- |
| u64TimeOffset | Time offset of the detected result within the input frame |
| u32SrcNum | Number of sound sources |
| SOUND_SPHERICAL_DIRECTION | See SOUND_SPHERICAL_DIRECTION |
| s32Reserve | Reserved |

&emsp;&emsp;【Related Functions】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_Process( AK_S32                  s32EffectUserId,
                                    AK_U8                   *pu8InBuf,
                                    AK_U32                  u32InDataLen,
                                    AUDIO_EFFECT_RESULT_S   *pstEffectResult );

```

<br/>

### AUDIO_LSSL_RESULT_S

&emsp;&emsp;【Notes】

&emsp;&emsp;Uniform linear-array sound-source localization output.

&emsp;&emsp;【Definition】

```c
/* SSL result output*/
typedef struct akAUDIO_LSSL_RESULT_S {
    AK_U64                      u64TimeOffset;
    AK_U32                      u32SrcNum;      // number of sound sources
    SOUND_SPHERICAL_DIRECTION   *pastSndSrcDir;
    AK_S32                      s32Reserve;
} AUDIO_LSSL_RESULT_S;
```

&emsp;&emsp;【Members】

| **Member**              | **Description**                         |
| ------------------------- | -------------------------------- |
| u64TimeOffset | Time offset of the detected result within the input frame |
| u32SrcNum | Number of sound sources |
| SOUND_SPHERICAL_DIRECTION | See SOUND_SPHERICAL_DIRECTION |
| s32Reserve | Reserved |

&emsp;&emsp;【Related Functions】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_Process( AK_S32                  s32EffectUserId,
                                    AK_U8                   *pu8InBuf,
                                    AK_U32                  u32InDataLen,
                                    AUDIO_EFFECT_RESULT_S   *pstEffectResult );

```

<br/>

### AUDIO_AIKWS_RESULT_S

&emsp;&emsp;【Notes】

&emsp;&emsp;Keyword-spotting output.

&emsp;&emsp;【Definition】

```c
typedef struct akAUDIO_AIKWS_RESULT_S {
    AK_U64          u64TimeOffset;
    AK_S16          s16ProbValue;
} AUDIO_AIKWS_RESULT_S;
```

&emsp;&emsp;【Members】

| **Member**  | **Description**                         |
| ------------- | -------------------------------- |
| u64TimeOffset | Time offset of the detected result within the input frame |
| s16ProbValue | Recognized keyword index |

&emsp;&emsp;【Related Functions】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_Process( AK_S32                  s32EffectUserId,
                                    AK_U8                   *pu8InBuf,
                                    AK_U32                  u32InDataLen,
                                    AUDIO_EFFECT_RESULT_S   *pstEffectResult );

```

<br/>

### AUDIO_AIKWSASR_RESULT_S

&emsp;&emsp;【Notes】

&emsp;&emsp;Keyword-spotting output.

&emsp;&emsp;【Definition】

```c
typedef struct akAUDIO_AIKWSASR_RESULT_S {
    AK_U64          u64TimeOffset;
    AK_S16          s16ProbValue;
    AK_S16          s16KeyWordResult;
} AUDIO_AIKWSASR_RESULT_S;
```

&emsp;&emsp;【Members】

|   **Member**    | **Description**                         |
| ----------------- | -------------------------------- |
| u64TimeOffset | Time offset of the detected result within the input frame |
| s16ProbValue | Recognized keyword index |
| s16KeyWordResult | ID of the specific recognized keyword |

&emsp;&emsp;【Related Functions】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_Process( AK_S32                  s32EffectUserId,
                                    AK_U8                   *pu8InBuf,
                                    AK_U32                  u32InDataLen,
                                    AUDIO_EFFECT_RESULT_S   *pstEffectResult );

```

<br/>

### AUDIO_VAD_RESULT_LIST_S

&emsp;&emsp;【Notes】

&emsp;&emsp;Linked list of sound-level detection results.

&emsp;&emsp;【Definition】

```c
typedef struct akAUDIO_VAD_RESULT_LIST_S {
    AUDIO_VAD_RESULT_S      *stResult;
    SLList                  *next;
} AUDIO_VAD_RESULT_LIST_S;
```

&emsp;&emsp;【Members】

| **Member** | **Description**                         |
| ------------ | -------------------------------- |
| stResult | Output result; see AUDIO_VAD_RESULT_S |
| next | Linked list |

&emsp;&emsp;【Related Functions】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_Process( AK_S32                  s32EffectUserId,
                                    AK_U8                   *pu8InBuf,
                                    AK_U32                  u32InDataLen,
                                    AUDIO_EFFECT_RESULT_S   *pstEffectResult );

```

<br/>

### AUDIO_CRY_RESULT_LIST_S

&emsp;&emsp;【Notes】

&emsp;&emsp;Linked list of crying-detection results.

&emsp;&emsp;【Definition】

```c
typedef struct akAUDIO_CRY_RESULT_LIST_S {
    AUDIO_CRY_RESULT_S      *stResult;
    SLList                  *next;
} AUDIO_CRY_RESULT_LIST_S;
```

&emsp;&emsp;【Members】

| **Member** | **Description**                         |
| ------------ | -------------------------------- |
| stResult | Output result; see AUDIO_CRY_RESULT_S |
| next | Linked list |

&emsp;&emsp;【Related Functions】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_Process( AK_S32                  s32EffectUserId,
                                    AK_U8                   *pu8InBuf,
                                    AK_U32                  u32InDataLen,
                                    AUDIO_EFFECT_RESULT_S   *pstEffectResult );

```

<br/>

### AUDIO_AICRY_RESULT_LIST_S

&emsp;&emsp;【Notes】

&emsp;&emsp;Linked list of AI crying-detection results.

&emsp;&emsp;【Definition】

```c
typedef struct akAUDIO_AICRY_RESULT_LIST_S {
    AUDIO_AICRY_RESULT_S      *stResult;
    SLList                  *next;
} AUDIO_AICRY_RESULT_LIST_S;
```

&emsp;&emsp;【Members】

| **Member** | **Description**                           |
| ------------ | ---------------------------------- |
| stResult | Output result; see AUDIO_AICRY_RESULT_S |
| next | Linked list |

&emsp;&emsp;【Related Functions】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_Process( AK_S32                  s32EffectUserId,
                                    AK_U8                   *pu8InBuf,
                                    AK_U32                  u32InDataLen,
                                    AUDIO_EFFECT_RESULT_S   *pstEffectResult );

```

<br/>

### AUDIO_SSL_RESULT_LIST_S

&emsp;&emsp;【Notes】

&emsp;&emsp;Linked list of sound-source localization results.

&emsp;&emsp;【Definition】

```c
typedef struct akAUDIO_SSL_RESULT_LIST_S {
    AUDIO_SSL_RESULT_S      *stResult;
    SLList                  *next;
} AUDIO_SSL_RESULT_LIST_S;
```

&emsp;&emsp;【Members】

| **Member** | **Description**                         |
| ------------ | -------------------------------- |
| stResult | Output result; see AUDIO_SSL_RESULT_S |
| next | Linked list |

&emsp;&emsp;【Related Functions】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_Process( AK_S32                  s32EffectUserId,
                                    AK_U8                   *pu8InBuf,
                                    AK_U32                  u32InDataLen,
                                    AUDIO_EFFECT_RESULT_S   *pstEffectResult );

```

<br/>

### AUDIO_LSSL_RESULT_LIST_S

&emsp;&emsp;【Notes】

&emsp;Linked list of uniform linear-array sound-source localization results.

&emsp;&emsp;【Definition】

```c
typedef struct akAUDIO_LSSL_RESULT_S {
    AUDIO_LSSL_RESULT_S      *stResult;
    SLList                  *next;
} AUDIO_LSSL_RESULT_LIST_S;
```

&emsp;&emsp;【Members】

| **Member** | **Description**                          |
| ------------ | --------------------------------- |
| stResult | Output result; see AUDIO_LSSL_RESULT_S |
| next | Linked list |

&emsp;&emsp;【Related Functions】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_Process( AK_S32                  s32EffectUserId,
                                    AK_U8                   *pu8InBuf,
                                    AK_U32                  u32InDataLen,
                                    AUDIO_EFFECT_RESULT_S   *pstEffectResult );

```

<br/>

### AUDIO_AIKWS_RESULT_LIST_S

&emsp;&emsp;【Notes】

&emsp;Linked list of keyword-spotting results.

&emsp;&emsp;【Definition】

```c
typedef struct akAUDIO_AIKWS_RESULT_LIST_S {
    AUDIO_AIKWS_RESULT_S    *stResult;
    SLList                  *next;
} AUDIO_AIKWS_RESULT_LIST_S;
```

&emsp;&emsp;【Members】

| **Member** | **Description**                           |
| ------------ | ---------------------------------- |
| stResult | Output result; see AUDIO_AIKWS_RESULT_S |
| next | Linked list |

&emsp;&emsp;【Related Functions】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_Process( AK_S32                  s32EffectUserId,
                                    AK_U8                   *pu8InBuf,
                                    AK_U32                  u32InDataLen,
                                    AUDIO_EFFECT_RESULT_S   *pstEffectResult );

```

<br/>

### AUDIO_AIKWSASR_RESULT_LIST_S

&emsp;&emsp;【Notes】

&emsp;Linked list of keyword-spotting ASR results.

&emsp;&emsp;【Definition】

```c
typedef struct akAUDIO_AIKWSASR_RESULT_LIST_S {
    AUDIO_AIKWSASR_RESULT_S    *stResult;
    SLList                  *next;
} AUDIO_AIKWSASR_RESULT_LIST_S;
```

&emsp;&emsp;【Members】

| **Member** | **Description**                             |
| ------------ | ------------------------------------ |
| stResult | Output result; see AUDIO_AIKWSASR_RESULT_S |
| next | Linked list |

&emsp;&emsp;【Related Functions】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_Process( AK_S32                  s32EffectUserId,
                                    AK_U8                   *pu8InBuf,
                                    AK_U32                  u32InDataLen,
                                    AUDIO_EFFECT_RESULT_S   *pstEffectResult );

```

<br/>

### RESULT_S

&emsp;&emsp;【Notes】

&emsp;&emsp;RES/EQ/ASLC output.

&emsp;&emsp;【Definition】

```c
typedef union akRESULT_S {
    AUDIO_EFFECT_DATA_PROCESS_RESULT_S      stDataProcessResult;// RES / ASLC / EQ
    void                                    *pstDetResult;      // detect result list
} RESULT_S;
```

&emsp;&emsp;【Members】

| **Member**                       | **Description**                                         |
| ---------------------------------- | ------------------------------------------------ |
| AUDIO_EFFECT_DATA_PROCESS_RESULT_S | Output result; see AUDIO_EFFECT_DATA_PROCESS_RESULT_S |
| pstDetResult | Detection result output |

&emsp;&emsp;【Related Functions】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_Process( AK_S32                  s32EffectUserId,
                                    AK_U8                   *pu8InBuf,
                                    AK_U32                  u32InDataLen,
                                    AUDIO_EFFECT_RESULT_S   *pstEffectResult );

```

> **Note:**
>
> pstDetResult is allocated and freed internally. If the application records its pointer address, do not access pstDetResult after AK_MPI_AUDIO_EFFECT_DeInit; doing so uses an invalid pointer address.

<br/>

## Getting Version Information

### AK_MPI_AUDIO_EFFECT_GetVersion

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the module version.

&emsp;&emsp;【Syntax】

```c
const AK_CHAR* AK_MPI_AUDIO_EFFECT_GetVersion(AK_VOID);
```

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------- | -------- |
| Module version | Success |
| NULL       | Failure     |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vqe.a and libakaudiofilter.a, or libplat_vqe.so and libakaudiofilter.so

&emsp;&emsp;Header: ak_audio_effect.h

&emsp;&emsp;【Call Sequence】

&emsp;&emsp;This function may be called at any point.

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

<br/>

### AK_MPI_AUDIO_EFFECT_GetFilterVersion

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the libakaudiofilter library version.

&emsp;&emsp;【Syntax】

```c
AK_CHAR* AK_MPI_AUDIO_EFFECT_GetFilterVersion(AK_VOID);
```

&emsp;&emsp;【Return Value】

| **Return value**               | **Description** |
| ------------------------ | -------- |
| libakaudiofilter library version | Success |
| NULL                     | Failure     |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vqe.a and libakaudiofilter.a, or libplat_vqe.so and libakaudiofilter.so

&emsp;&emsp;Header: ak_audio_effect.h

&emsp;&emsp;【Call Sequence】

&emsp;&emsp;This function may be called at any point.

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

<br/>

## Registering a Module

### AK_MPI_AUDIO_EFFECT_Register

&emsp;&emsp;【Description】

&emsp;&emsp;Registers an audio-effect processing API.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_AUDIO_EFFECT_Register(AUDIO_EFFECT_REG_S *pstAudioEffect);
```

&emsp;&emsp;【Parameters】

| **Parameter**   | **Description**             | **Value range**           | **Input/Output** |
| -------------- | -------------------- | ---------------------- | ------------- |
| pstAudioEffect | Configures audio-effect processing callbacks | See AUDIO_EFFECT_REG_S | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**     |
| ---------- | ------------ |
| 0          | Success         |
| Other       | See the error codes. |

&emsp;&emsp;【Error Codes】

| **Error code**          | **Description**               |
| ------------------- | ---------------------- |
| ERROR_VQE_USER_NULL | Null user pointer |
| ERROR_VQE_NO_USER | No current user |
| ERROR_VQE_LIB_ERROR | Error closing voice-quality enhancement library |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vqe.a and libakaudiofilter.a, or libplat_vqe.so and libakaudiofilter.so

&emsp;&emsp;Header: ak_audio_effect.h

&emsp;&emsp;【Call Sequence】

&emsp;&emsp;See the AK_MPI_AUDIO_EFFECT_Init example.

&emsp;&emsp;【Paired Interface】

&emsp;&emsp;None.

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

<br/>

## Initializing the Module

### **AK_MPI_AUDIO_EFFECT_Init**

&emsp;&emsp;【Description】

&emsp;&emsp;Initializes audio-effect processing.

&emsp;&emsp;【Syntax】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_Init(	AK_S32      			s32EffectUserId,
                                    AUDIO_DATA_ATTR_S     	*pstAudioDataAttr,
                                    AUDIO_EFFECT_TYPE_E     enEffectType,
                                    AK_CHAR                 *pchFile,
                                    AK_CHAR                 *pchSection );

```

&emsp;&emsp;【Parameters】

| **Parameter**    | **Description**           | **Value range**                                                 | **Input/Output** |
| --------------- | ------------------ | ------------------------------------------------------------ | ------------- |
|                  |                    |                                |               |
| s32EffectUserId | Audio-effect module user ID | [0, AUDIO_EFFECT_USER_NUM - 1] | Input |
| pstAudioDataAttr | Basic audio attributes | See AUDIO_DATA_ATTR_S | Input |
| enEffectType | Audio-effect type | See AUDIO_EFFECT_TYPE_E | Input |
| pchFile | Audio configuration filename | Non-null | Input |
| pchSection | Audio configuration section | Non-null | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**       |
| ---------- | -------------- |
| 0          | Success.         |
| Other       | See the error codes. |

&emsp;&emsp;【Error Codes】

| **Error code**              | **Description**     |
| ----------------------- | ------------ |
| ERROR_TYPE_POINTER_NULL | Null parameter pointer |
| ERROR_TYPE_INVALID_ARG  | Invalid parameter   |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_ai.so, libakaudiofilter.so, and libplat_vqe.so, or libplat_ai.a, libakaudiofilter.a, and libplat_vqe.a

&emsp;&emsp;Header: ak_ai.h

&emsp;&emsp;【Paired Interface】

```C
    AK_S32 AK_MPI_AUDIO_EFFECT_DeInit(AK_S32 s32EffectUserId);
```

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The interface is reentrant.

<br/>

## Destroying the Module

### AK_MPI_AUDIO_EFFECT_DeInit

&emsp;&emsp;【Description】

&emsp;&emsp;Deinitializes audio-effect processing.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_AUDIO_EFFECT_DeInit(AK_S32 s32EffectUserId);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**      | **Value range** | **Input/Output** |
| ------------ | ------------- | ------------ | ------------- |
| s32EffectUserId | Audio-effect module user ID | [0, AUDIO_EFFECT_USER_NUM - 1] | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**     |
| ---------- | ------------ |
| 0          | Success         |
| Other       | See the error codes. |

&emsp;&emsp;【Error Codes】

| **Error code**          | **Description**               |
| ------------------- | ---------------------- |
| ERROR_VQE_USER_NULL | Null user pointer |
| ERROR_VQE_NO_USER | No current user |
| ERROR_VQE_LIB_ERROR | Error closing voice-quality enhancement library |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vqe.a and libakaudiofilter.a, or libplat_vqe.so and libakaudiofilter.so

&emsp;&emsp;Header: ak_audio_effect.h

&emsp;&emsp;【Call Sequence】

&emsp;&emsp;See the AK_MPI_AUDIO_EFFECT_Init example.

&emsp;&emsp;【Paired Interface】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_Init(	AK_S32      			s32EffectUserId,
                                    AUDIO_DATA_ATTR_S     	*pstAudioDataAttr,
                                    AUDIO_EFFECT_TYPE_E     enEffectType,
                                    AK_CHAR                 *pchFile,
                                    AK_CHAR                 *pchSection );
```

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

<br/>

## Processing or Detecting Data

### AK_MPI_AUDIO_EFFECT_Process

&emsp;&emsp;【Description】

&emsp;&emsp;Processes input audio-source data and outputs processed audio, or detects content in the audio and outputs detection results.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_AUDIO_EFFECT_Process(AK_S32 s32EffectUserId,
                              AK_U8 *pu8InBuf, AK_U32 u32InDataLen,
                              AUDIO_EFFECT_RESULT_S   *pstEffectResult);
```

&emsp;&emsp;【Parameters】

| **Parameter**   | **Description**           | **Value range** | **Input/Output** |
| -------------- | ------------------ | ------------ | ------------- |
| s32EffectUserId | Audio-effect module user ID | [0, AUDIO_EFFECT_USER_NUM - 1] | Input |
| pu8InBuf | Pointer to input data | Non-null | Input |
| u32InDataLen | Input-data length | Greater than 0 | Input |
| pstEffectResult | Processing or detection result | See AUDIO_EFFECT_RESULT_S | Output |

&emsp;&emsp;【Return Value】

| **Error code**          | **Description**     |
| ------------------- | ------------ |
| ERROR_VQE_USER_NULL | Null user pointer |
| ERROR_VQE_NO_USER | No current user |
| ERROR_VQE_LIB_ERROR | Audio-effect library error |

After AK_SUCCESS is returned, pstEffectResult must still be parsed.

For data-processing effects such as RES/ASLC/EQ, parse unEffectResult in pstEffectResult as AUDIO_EFFECT_DATA_PROCESS_RESULT_S.

| AUDIO_EFFECT_DATA_PROCESS_RESULT_S member | **Description** |
| ------------------------------------------- | ------------------ |
| pu8OutBuf | Start address after processing |
| u32OutDataLen | Length of processed data |
| s32Reserve | Reserved |

For detection effects such as CRY/VAD/AI_CRY, parse unEffectResult in pstEffectResult as the corresponding detection result type. For VAD, for example, parse it as AUDIO_VAD_RESULT_LIST_S.

【Error Codes】

| **Error code**                 | **Description**           |
| -------------------------- | ------------------ |
| ERROR_TYPE_INVALID_ARG     | Invalid parameter         |
| ERROR_TYPE_MALLOC_FAILED   | Malloc failed        |
| ERROR_TYPE_POINTER_NULL    | Null parameter           |
| ERROR_VQE_USER_NULL | Null user pointer |
| ERROR_VQE_OUTBUF_LEN_ERROR | Invalid output-buffer size |
| ERROR_VQE_LIB_ERROR | Library runtime error |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vqe.a and libakaudiofilter.a, or libplat_vqe.so and libakaudiofilter.so

&emsp;&emsp;Header: ak_audio_effect.h

&emsp;&emsp;【Call Sequence】

&emsp;&emsp;See the AK_MPI_AUDIO_EFFECT_Init example.

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The interface is reentrant.

> **Note:**
>
> Process support for different effects and data organizations:
>
> |        | MONO | STEREO | QUEUE |
> | ------ | ---- | ------ | ----- |
> | RES    | YES  | YES    | NO    |
> | VAD    | YES  | NO     | NO    |
> | CRY    | YES  | NO     | NO    |
> | AI_CRY | YES  | NO     | NO    |
>
> To apply VAD or CRY to STEREO or QUEUE data, split the STEREO or QUEUE data into single-channel audio by following the AI data organization. Multiple single channels may be mixed into one channel or left separate, then processed with Process.
>
> After a multi-microphone array algorithm produces one audio channel, it may also be processed as MONO with Process for VAD, CRY, and AI_CRY.

<br/>

### AK_MPI_AUDIO_EFFECT_Reset

&emsp;&emsp;【Description】

&emsp;&emsp;Clears the internal audio-effect buffer.

&emsp;&emsp;【Syntax】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_Reset(AK_S32 s32EffectUserId);
```

【Parameters】

| **Parameter**    | **Description**           | **Value range**                   | **Input/Output** |
| --------------- | ------------------ | ------------------------------ | ------------- |
| s32EffectUserId | Audio-effect module user ID | [0, AUDIO_EFFECT_USER_NUM - 1] | Input |

&emsp;&emsp;【Return Value】

| **Return value**                   | **Description**                   |
| ---------------------------- | -------------------------- |
| ERROR_TYPE_INVALID_ARG | Invalid parameter |
| ERROR_AUDIO_EFFECT_LIB_ERROR | Internal audio-effect library interface call failed |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vqe.a and libakaudiofilter.a, or libplat_vqe.so and libakaudiofilter.so

&emsp;&emsp;Header: ak_audio_effect.h

&emsp;&emsp;【Call Sequence】

&emsp;After AK_MPI_AUDIO_EFFECT_Process.

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

​		【Note】

​		Currently supported only for the LSSL audio-effect type.

<br/>

## Setting Parameters

### AK_MPI_AUDIO_EFFECT_LoadConf

【Description】

&emsp;&emsp;Gets the relevant parameters from a configuration file and applies them.

&emsp;&emsp;【Syntax】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_LoadConf(AK_S32                  s32EffectUserId,
                                    AUDIO_EFFECT_TYPE_E     enEffectType,
                                    AK_CHAR                 *pchFile,
                                    AK_CHAR                 *pchSection);
```

【Parameters】

| **Parameter**    | **Description**           | **Value range**                   | **Input/Output** |
| --------------- | ------------------ | ------------------------------ | ------------- |
| s32EffectUserId | Audio-effect module user ID | [0, AUDIO_EFFECT_USER_NUM - 1] | Input |
| enEffectType | Audio-effect type | See AUDIO_EFFECT_TYPE_E | Input |
| pchFile | Audio configuration filename | Non-null | Input |
| pchSection | Audio configuration section | Non-null | Input |

【Return Value】

| **Return value**                   | **Description**                   |
| ---------------------------- | -------------------------- |
| ERROR_TYPE_INVALID_ARG | Invalid parameter |
| ERROR_AUDIO_EFFECT_LIB_ERROR | Internal audio-effect library interface call failed |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vqe.a and libakaudiofilter.a, or libplat_vqe.so and libakaudiofilter.so

&emsp;&emsp;Header: ak_audio_effect.h

&emsp;&emsp;【Call Sequence】

&emsp;After AK_MPI_AUDIO_EFFECT_Init.

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

### AK_MPI_AUDIO_EFFECT_SetAttr

【Description】

&emsp;&emsp;Sets audio-effect parameters.

&emsp;&emsp;【Syntax】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_SetAttr(AK_S32                  s32EffectUserId,
                                    AUDIO_EFFECT_TYPE_E     enEffectType,
                                    AUDIO_EFFECT_ATTR_S     *pstEffectAttr);
```

【Parameters】

| **Parameter**    | **Description**           | **Value range**                   | **Input/Output** |
| --------------- | ------------------ | ------------------------------ | ------------- |
| s32EffectUserId | Audio-effect module user ID | [0, AUDIO_EFFECT_USER_NUM - 1] | Input |
| enEffectType | Audio-effect type | See AUDIO_EFFECT_TYPE_E | Input |
| pstEffectAttr | Audio-effect configuration parameters | Non-null | Input |

【Return Value】

| **Return value**                   | **Description**                   |
| ---------------------------- | -------------------------- |
| ERROR_TYPE_INVALID_ARG | Invalid parameter |
| ERROR_AUDIO_EFFECT_LIB_ERROR | Internal audio-effect library interface call failed |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vqe.a and libakaudiofilter.a, or libplat_vqe.so and libakaudiofilter.so

&emsp;&emsp;Header: ak_audio_effect.h

&emsp;&emsp;【Call Sequence】

&emsp;After AK_MPI_AUDIO_EFFECT_Init.

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

​		【Note】

​		Currently supported only for the EQ, ASLC, and resample audio-effect types.

### AK_MPI_AUDIO_EFFECT_GetAttr

【Description】

&emsp;&emsp;Gets audio-effect parameters.

&emsp;&emsp;【Syntax】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_GetAttr(AK_S32                  s32EffectUserId,
                                   AUDIO_EFFECT_TYPE_E     enEffectType,
                                   AUDIO_EFFECT_ATTR_S     *pstEffectAttr);
```

【Parameters】

| **Parameter**    | **Description**           | **Value range**                   | **Input/Output** |
| --------------- | ------------------ | ------------------------------ | ------------- |
| s32EffectUserId | Audio-effect module user ID | [0, AUDIO_EFFECT_USER_NUM - 1] | Input |
| enEffectType | Audio-effect type | See AUDIO_EFFECT_TYPE_E | Input |
| pstEffectAttr | Audio-effect configuration parameters | Non-null | Output |

【Return Value】

| **Return value**                   | **Description**                   |
| ---------------------------- | -------------------------- |
| ERROR_TYPE_INVALID_ARG | Invalid parameter |
| ERROR_AUDIO_EFFECT_LIB_ERROR | Internal audio-effect library interface call failed |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vqe.a and libakaudiofilter.a, or libplat_vqe.so and libakaudiofilter.so

&emsp;&emsp;Header: ak_audio_effect.h

&emsp;&emsp;【Call Sequence】

&emsp;After AK_MPI_AUDIO_EFFECT_Init.

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

​		【Note】

​		Currently supported only for the EQ, ASLC, and resample audio-effect types.

<br/>

## Debugging

### AK_MPI_AUDIO_EFFECT_SetLibPrintLevel

&emsp;&emsp;【Description】

&emsp;&emsp;Sets the filter logging priority in the audio-effect module.

&emsp;&emsp;【Syntax】

```c
AK_S32 AK_MPI_AUDIO_EFFECT_SetLibPrintLevel(AK_U32 u32PrintLevel);
```

【Parameters】

| **Parameter**  | **Description**         | **Value range**                                  | **Input/Output** |
| ------------- | ---------------- | --------------------------------------------- | ------------- |
| u32PrintLevel | Logging priority to set | See ATCLIB_PRINT_LEVEL_E in ak_common_audio.h | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------- | -------- |
| AK_SUCCESS | Success     |
| AK_FAILED  | Failure     |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vqe.a and libakaudiofilter.a, or libplat_vqe.so and libakaudiofilter.so

&emsp;&emsp;Header: ak_audio_effect.h

&emsp;&emsp;【Call Sequence】

&emsp;&emsp;This function may be called at any point.

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

## Interface Call Dependencies

&emsp;&emsp;The AUDIO_EFFECT interfaces have the call dependencies shown below:

| **Function**                         | **Description**                               |
| ------------------------------------ | -------------------------------------- |
| AK_MPI_AUDIO_EFFECT_GetVersion | None |
| AK_MPI_AUDIO_EFFECT_GetFilterVersion | None |
| AK_MPI_AUDIO_EFFECT_Register | Call before AK_MPI_AUDIO_EFFECT_Init |
| AK_MPI_AUDIO_EFFECT_Init | Call after AK_MPI_AUDIO_EFFECT_Register |
| AK_MPI_AUDIO_EFFECT_DeInit | Call after AK_MPI_AUDIO_EFFECT_Process |
| AK_MPI_AUDIO_EFFECT_Reset | Call after AK_MPI_AUDIO_EFFECT_Process |
| AK_MPI_AUDIO_EFFECT_Process | Call after AK_MPI_AUDIO_EFFECT_Init |
| AK_MPI_AUDIO_EFFECT_SetLibPrintLevel | None |
| AK_MPI_AUDIO_EFFECT_SetAttr | Call before AK_MPI_AUDIO_EFFECT_Init |
| AK_MPI_AUDIO_EFFECT_GetAttr | Call before AK_MPI_AUDIO_EFFECT_Init |

<br/>

## Sample Notes

### 1 VAD Sample Command and Parameters

Before running this sample, load ak_pcm.ko with insmod. It is normally loaded by default at startup.

| Short option | Long option | **Description** |
| ---------------- | ------------------- | ------------------------------------------------------------ |
| h | help | Prints help. |
| s | sample-rate | Audio sample rate; supports 8000 and 16000. |
| p | path | PCM output directory; do not specify a filename. End the path with "/", for example /mnt/. |
| t | second | Capture duration in seconds. |
| d | device-type | Device type: 0:DEV_ADC, 1:DEV_PDM, 2:DEV_I2S0_AI. |
| f | config-file | Full path to the audio configuration file. |
| e | config-section | Audio configuration section name: def_near for AI with one microphone; two_array_near for AI with two microphones; def_far for AO. |
| i | vad-config -section | VAD configuration section name. |

<br/>

### VAD Sample Storage and File Naming

(1) Sample output uses PCM format by default.
(2) Sample output is stored in /mnt/ by default.
(3) The default output filename is yyyymmdd-ddmmss<sample-rate><channel-count><duration-ms><device>.pcm.

### VAD Sample Example

ak_vad_sample -s 16000 -p /mnt/ -t 20 -d 0 -f /etc/config/audio_config.ini -e def_near -i vad_1

<br/>

### 2 VQE Sample Command and Parameters

| Short option | Long option | **Description** |
| ---------------- | ------------------------ | ------------------------------------------------------------ |
| h | help | Prints help. |
| s | sample-rate | Audio sample rate; supports 8000 and 16000. |
| p | path | PCM output directory; do not specify a filename. End the path with "/", for example /mnt/. |
| t | second | Capture duration in seconds. |
| d | device-type | Device type: 0:DEV_ADC, 1:DEV_PDM, 2:DEV_I2S0_AI. |
| f | config-file | Full path to the audio configuration file. |
| e | config-section | Audio configuration section name: def_near for AI with one microphone; two_array_near for AI with two microphones; def_far for AO. |
| r | resample -config-section | Resample configuration section name. |
| a | aslc-config -section | ASLC configuration section name. |
| q | eq-config -section | EQ configuration section name. |
| v | probe-mode | Volume [-90~20 dB]. |

### VQE Sample Storage and File Naming

(1) Sample output uses PCM format by default.
(2) Sample output is stored in /mnt/ by default.
(3) The default output filename is yyyymmdd-ddmmss<sample-rate><channel-count><duration-ms><device>_<vqe-type>.pcm.

### VQE Sample Example

ak_vqe_sample -s 16000 -p /mnt/ -t 20 -d 0 -f /etc/config/audio_config.ini   -e def_near -r res_1 -a aslc_1 -q eq_1 -v 10

### 3 ssl_sample Command and Parameters

Before running this sample, load ak_pcm.ko with insmod. It is normally loaded by default at startup.

| Short option | Long option | **Description** |
| ---------------- | ---------------- | ------------------------------------------------------------ |
| h | help | Prints help. |
| s | sample-rate | Audio sample rate; supports 8000 and 16000. |
| p | path | PCM output directory; do not specify a filename. End the path with "/", for example /mnt/. |
| t | second | Capture duration in seconds. |
| d | device-type | Device type: 0:DEV_ADC, 1:DEV_PDM, 2:DEV_I2S0_AI. |
| f | config-file | Full path to the audio configuration file. |
| e | config-section | Audio configuration section name: def_near for AI with one microphone; two_array_near for AI with two microphones; def_far for AO. |

### SSL Sample Storage and File Naming

(1) Sample output uses PCM format by default.
(2) Sample output is stored in /mnt/ by default.
(3) The default output filename is yyyymmdd-ddmmss<sample-rate><channel-count><duration-ms><device>.pcm.

### SSL Sample Example

  ak_ssl_sample -s 16000 -p /mnt/ -t 20 -d 0 -f /etc/config/audio_config.ini -e def_lssl

Note:

### 4 cry_sample Command and Parameters

| Short option | Long option | **Description** |
| ---------------- | ------------------- | ------------------------------------------------------------ |
| h | help | Prints help. |
| s | sample-rate | Audio sample rate; supports 8000 and 16000. |
| p | path | PCM output directory; do not specify a filename. End the path with "/", for example /mnt/. |
| t | second | Capture duration in seconds. |
| d | device-type | Device type: 0:DEV_ADC, 1:DEV_PDM, 2:DEV_I2S0_AI. |
| f | config-file | Full path to the audio configuration file. |
| e | config-section | Audio configuration section name: def_near for AI with one microphone; two_array_near for AI with two microphones; def_far for AO. |
| c | cry-config- section | Crying-detection configuration section: ai_cry_1 for NPU-based detection; cry_1 for CPU-based detection. |
| m | detect-mode | 0: software-based crying detection; 1: NPU-based crying detection. |

### CRY Sample Storage and File Naming

(1) Sample output uses PCM format by default.
(2) Sample output is stored in /mnt/ by default.
(3) The default output filename is yyyymmdd-ddmmss<sample-rate><channel-count><duration-ms><device>.pcm.

### CRY Sample Example

ak_cry_sample -s 16000 -p /mnt/ -t 20 -d 0 -f /etc/config/audio_config.ini  -e def_near  -m 1 -c ai_cry_1

Note: In the ai_cry_1 section, modelName must be the full model path.

## /var/platform Description

The /var/platform directory exposes the current module configuration parameters and status. Its parameters are described below.

### var/platform/AUDIO_EFFECT/stat

| Parameter | Description |
| ------------------------ | -------------------- |
| AudioEffect_version | Platform audio-effect processing version |
| filter_version | Filter version |
| LineArraySsl_version | Uniform linear-array localization library version |
| SoundLevelDetect_version | Sound-level detection library version |
| AiCryDetect_version | AI crying-detection version |

### var/platform/VQE/stat

| Parameter | Description |
| --------------------------- | ---------------------------------- |
| vqe_version | Platform audio-effect processing version |
| filter_version | Filter version |
| NearJitterBufLen | AI jitter-buffer size |
| NearSampleRate | AI-side sample rate |
| NearHwSampleRate | Hardware sample rate |
| NearSoundMode | AI-side channel mode |
| NearSampleBits | AI-side sample precision |
| NearSyncedInputs | AI default: 0 |
| NearSyncBufLen | Default buffer size shared by AI and AO |
| NearSyncCompensate | AI default: 170 |
| NearVqe0_AslcLimit | AI amplification limit |
| NearVqe0_Volume | AI digital volume |
| NearVqe0_EqEnable | AI EQ enable |
| NearVqe0_EqBandsNum | Number of AI EQ filters |
| NearVqe0_EqPreGain | AI EQ pre-gain |
| NearVqe0_AgcEnable | AI AGC enable |
| NearVqe0_AgcLevel | AI AGC gain level |
| NearVqe0_AgcMaxGain | AI upper amplification limit for dynamic gain adjustment |
| NearVqe0_AgcMinGain | AI lower attenuation limit for dynamic gain adjustment |
| NearVqe0_NearSensitivity | AI sensitivity to near-end sound |
| NearVqe0_NrEnable | AI noise-reduction enable |
| NearVqe0_NoiseSuppressDb | AI noise-reduction strength |
| NearVqe0_AecEnable | AEC enable |
| NearVqe0_Tail | Default: 512 |
| NearVqe0_FarBreakdownThresh | Half-duplex/full-duplex switching threshold range |
| NearVqe0_AudioOutDigiGain | Output limiting |
| NearVqe0_AudioInDigiGain | Input limiting |
| FarJitterBufLen | AO jitter-buffer size |
| FarSampleRate | AO-side sample rate |
| FarHwSampleRate | Hardware sample rate |
| FarSoundMode | AO-side channel mode |
| FarSyncedInputs | AO default: 0 |
| FarSyncBufLen | Buffer size shared by AI and AO for AEC |
| FarSyncCompensate | Default: 170 |
| FarVqe0_AslcLimit | AO amplification limit |
| FarVqe0_Volume | AO digital volume |
| FarVqe0_EqEnable | AO EQ enable |
| FarVqe0_EqBandsNum | Number of AO EQ filters |
| FarVqe0_EqPreGain | AO EQ pre-gain |
| FarVqe0_NrEnable | AO noise-reduction enable |
| FarVqe0_NoiseSuppressDb | AO noise-reduction strength |

<br/>

## Error Codes

| Error code | Macro | Meaning |
| ---------- | ------------------------------- | ------------------ |
| 0x2b000000 | ERROR_AUDIO_EFFECT_OPEN_LIB_ERROR | Failed to open library |
| 0x2b000001 | ERROR_AUDIO_EFFECT_LIB_ERROR | Internal audio-effect library interface call failed |
| 0x2b000002 | ERROR_AUDIO_EFFECT_OUTBUF_LEN_ERROR | Invalid output-buffer length |
| 0x2b000003 | ERROR_AUDIO_EFFECT_NO_MATCH_VAD_TYPE | Sound-type mismatch |
| 0x2b000004 | ERROR_AUDIO_EFFECT_RESULT_NO_RETURN | No audio-effect processing result returned |

<br/>
