# 音频编码

## 概述

&emsp;&emsp;音频编码模块（AENC模块）主要负责原始音频数据按多种音频协议进行编码，然后输出音频码流。AENC模块支持多种编码格式。

<br/>

## API参考

&emsp;&emsp;本模块提供API参考，如下表所示。

| **数据结构**         | **描述**       |
| ---------------- | ------------ |
| AUDIO_TYPE_E     | 音频编码类型       |
| AENC_AAC_ATTR_E  | 音频AAC编码类型    |
| AENC_AAC_PARAM_S | 音频AAC编码属性结构体 |
| AENC_PARAM_S     | 音频编码open的参数  |
| FRAME_S          | 音频帧结构        |
| AENC_ENCODE_S    | 注册编码器结构体     |
| ENC_OUT_INFO     | 编码器输出属性结构体   |

<br/>

| **函数接口**                     | **描述**              |
| ---------------------------- | ------------------- |
| AK_MPI_AENC_GetVersion       | 获取音频编码库的版本号         |
| AK_MPI_AENC_GetEncVersion    | 获取ATC音频编码库的版本号      |
| AK_MPI_AENC_Open             | 打开音频编码              |
| AK_MPI_AENC_Close            | 关闭音频编码              |
| AK_MPI_AENC_SendFrame        | 发送要编码的音频帧           |
| AK_MPI_AENC_GetStream        | 获取一帧编码后的数据          |
| AK_MPI_AENC_ReleaseStream    | 释放一帧编码后的数据          |
| AK_MPI_AENC_SaveFile         | 保存AENC模块内部音频处理的过程文件 |
| K_MPI_AENC_ClearEncodeBuf    | 清除编码区的缓存            |
| AK_MPI_AENC_SendEndOfFrame   | 音频编码数据已经发送完成        |
| AK_MPI_AENC_RegisterEncoder  | 注册编码器               |
| AK_MPI_AENC_SetLibPrintLevel | 设置编码库打印等级           |
| AK_MPI_AENC_GetEncParam      | 获取编码器打开后的相关参数       |

<br/>

## 数据结构

### AUDIO_TYPE_E

&emsp;&emsp;【说明】

&emsp;&emsp;音频编解码类型。受库大小的限制，目前默认支持PCM、G711a/u，如需支持其他类型编解码，需要通过调用AK_MPI_AENC_RegisterEncoder来注册编码器。

&emsp;&emsp;【定义】

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

&emsp;&emsp;【成员】

| **成员名称**                  | **描述**    |
| ------------------------- | --------- |
| AK_AUDIO_TYPE_UNKNOWN     | 音频编解码缺省类型 |
| AK_AUDIO_TYPE_MIDI        | 不支持       |
| AK_AUDIO_TYPE_MP3         | MP3编码格式   |
| AK_AUDIO_TYPE_AMR         | AMR编码格式   |
| AK_AUDIO_TYPE_AAC         | AAC编码格式   |
| AK_AUDIO_TYPE_WMA         | WMA编码格式   |
| AK_AUDIO_TYPE_PCM         | PCM裸数据    |
| AK_AUDIO_TYPE_ADPCM_IMA   | 不支持       |
| AK_AUDIO_TYPE_ADPCM_MS    | 不支持       |
| AK_AUDIO_TYPE_ADPCM_FLASH | 不支持       |
| AK_AUDIO_TYPE_APE         | 不支持       |
| AK_AUDIO_TYPE_FLAC        | 不支持       |
| AK_AUDIO_TYPE_OGG_FLAC    | 不支持       |
| AK_AUDIO_TYPE_RA8LBR      | 不支持       |
| AK_AUDIO_TYPE_DRA         | 不支持       |
| AK_AUDIO_TYPE_OGG_VORBIS  | 不支持       |
| AK_AUDIO_TYPE_AC3         | 不支持       |
| AK_AUDIO_TYPE_PCM_ALAW    | G711a编码格式 |
| AK_AUDIO_TYPE_PCM_ULAW    | G711u编码格式 |
| AK_AUDIO_TYPE_SBC         | 不支持       |
| AK_AUDIO_TYPE_MSBC        | 不支持       |
| AK_AUDIO_TYPE_SPEEX       | 不支持       |
| AK_AUDIO_TYPE_SPEEX_WB    | 不支持       |
| AK_AUDIO_TYPE_OPUS        | 不支持       |
| AK_AUDIO_TYPE_G722        | 不支持       |
| AK_AUDIO_TYPE_VPWM        | 不支持       |
| AK_AUDIO_TYPE_G729A       | 不支持       |

<br/>

&emsp;&emsp;不同编码格式支持的采样率如下：

| 采样率（单声道） | PCM | AAC | AMR | G711A/U | MP3 |
| -------- | --- | --- | --- | ------- | --- |
| 8000     | 支持  | 支持  | 支持  | 支持      | 支持  |
| 11025    | 支持  | 支持  | 不支持 | 不支持     | 支持  |
| 12000    | 支持  | 支持  | 不支持 | 不支持     | 支持  |
| 16000    | 支持  | 支持  | 不支持 | 支持      | 支持  |
| 22050    | 支持  | 支持  | 不支持 | 不支持     | 支持  |
| 24000    | 支持  | 支持  | 不支持 | 不支持     | 支持  |
| 32000    | 支持  | 支持  | 不支持 | 不支持     | 支持  |
| 44100    | 支持  | 支持  | 不支持 | 不支持     | 支持  |
| 48000    | 支持  | 支持  | 不支持 | 不支持     | 支持  |

<br/>

&emsp;&emsp;双声道：

| 采样率（双声道） | PCM | AAC | AMR | G711A/U | MP3 |
| -------- | --- | --- | --- | ------- | --- |
| 8000     | 支持  | 支持  | 不支持 | 不支持     | 支持  |
| 11025    | 支持  | 支持  | 不支持 | 不支持     | 支持  |
| 12000    | 支持  | 支持  | 不支持 | 不支持     | 支持  |
| 16000    | 支持  | 支持  | 不支持 | 不支持     | 支持  |
| 22050    | 支持  | 支持  | 不支持 | 不支持     | 支持  |
| 24000    | 支持  | 支持  | 不支持 | 不支持     | 支持  |
| 32000    | 支持  | 支持  | 不支持 | 不支持     | 支持  |
| 44100    | 支持  | 支持  | 不支持 | 不支持     | 支持  |
| 48000    | 支持  | 支持  | 不支持 | 不支持     | 支持  |

&emsp;&emsp;【相关函数接口】

```c
AK_S32 AK_MPI_AENC_Open(AK_S32 s32AencUserId, const AENC_PARAM_S *pstParam);
```

<br/>

### AENC_AAC_ATTR_E

&emsp;&emsp;【说明】

&emsp;&emsp;AAC编码是否添加AAC头的属性。

&emsp;&emsp;【定义】

```c
typedef enum akAENC_AAC_ATTR_E
{
    AENC_AAC_RESERVED = 0,
    AENC_AAC_SAVE_FRAME_HEAD,
    AENC_AAC_CUT_FRAME_HEAD
} AENC_AAC_ATTR_E;
```

&emsp;&emsp;【成员】

| **成员名称**                 | **描述**          |
| ------------------------ | --------------- |
| AENC_AAC_RESERVED        | AAC编码属性初始值      |
| AENC_AAC_SAVE_FRAME_HEAD | AAC编码属性保留AAC编码头 |
| AENC_AAC_CUT_FRAME_HEAD  | AAC编码属性删除AAC编码头 |

&emsp;&emsp;【相关函数接口】

### AENC_AAC_PARAM_S

【说明】

AAC编码属性

【定义】

```c
typedef struct akAENC_AAC_PARAM_S
{
    AENC_AAC_ATTR_E enAacFrmHead;  //标识编码是否需要返回ADTS头
}AENC_AAC_PARAM_S;
```

【成员】

| **成员名称**     | **描述**   |
| ------------ | -------- |
| enAacFrmHead | AAC属性头枚举 |

【相关函数接口】

```c
AK_S32 AK_MPI_AENC_Open(AK_S32 s32AencUserId,const AENC_PARAM_S *pstParam);
```

### AENC_PARAM_S

&emsp;&emsp;【说明】

&emsp;&emsp;音频编码输入参数。

&emsp;&emsp;【定义】

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

&emsp;&emsp;【成员】

| **成员名称**     | **描述**   |
| ------------ | -------- |
| enSampleRate | 采样率      |
| enSampleBits | 采样精度     |
| enSoundMode  | 声道模式     |
| enType       | 音频编码类型   |
| unAencAttr   | 编码器属性联合体 |

&emsp;&emsp;【相关函数接口】

```c
AK_S32 AK_MPI_AENC_Open(AK_S32 s32AencUserId,const AENC_PARAM_S *pstParam);
```

<br/>

### FRAME_S

&emsp;&emsp;【说明】

&emsp;&emsp;音频pcm数据结构。

&emsp;&emsp;【定义】

```c
typedef struct akFRAME_S
{
        AK_U8 *pu8Data;    //frame data
        AK_U32 u32Len;        //frame len in bytes
        AK_U64 u64Ts;    //timestamp(ms)
        AK_U64 u64SeqNo;    //current frame sequence no.
}FRAME_S;
```

&emsp;&emsp;【成员】

| **成员名称** | **描述**                  |
| -------- | ----------------------- |
| u8Data   | 音频当前一帧pcm数据的指针，范围非空     |
| u32Len   | 音频当前一帧pcm数据的长度，范围大于等于0  |
| u64Ts    | 音频当前一帧pcm数据的时间戳，范围大于等于0 |
| u64SeqNo | 音频当前一帧pcm数据的序号，范围大于等于0  |

&emsp;&emsp;【相关函数接口】

```c
AK_S32 AK_MPI_AENC_SendFrame(AK_S32 s32AencUserId, const FRAME_S *pstPcmFrame,AK_U32 u32TimeOut);
```

<br/>

### AENC_ENCODE_S

&emsp;&emsp;【说明】

&emsp;&emsp;注册编码器结构体

&emsp;&emsp;【定义】

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

&emsp;&emsp;【成员】

| **成员名称**      | **描述**       |
| ------------- | ------------ |
| enType        | 编码类型         |
| pfnEncOpen    | 打开编码器的函数指针   |
| pfnEncProcess | 进行编码的函数指针    |
| pfnEncClose   | 关闭编码器的函数指针   |
| pfnEncReset   | 清除编码器数据的函数指针 |
| pfnEncFlush   | 结束编码的函数指针    |

&emsp;&emsp;【相关函数接口】

```c
AK_S32 AK_MPI_AENC_RegisterEncoder(AENC_ENCODE_S *pstEncoder);
```

### ENC_OUT_INFO

&emsp;&emsp;【说明】

&emsp;&emsp;编码器打开后输出属性结构体

&emsp;&emsp;【定义】

```c
typedef struct akENC_OUT_INFO
{
    AK_S32 s32SamplesPerFrame;  //每一帧pcm有多少个采样点
    AK_S32 s32FrameSize;        //输出编码后的长度
    AK_S32 s32BitRate;          //编码比特率
}ENC_OUT_INFO;
```

&emsp;&emsp;【成员】

| **成员名称**           | **描述**        |
| ------------------ | ------------- |
| s32SamplesPerFrame | 每一帧pcm有多少个采样点 |
| s32FrameSize       | 输出编码后的编码长度    |
| s32BitRate         | 编码比特率         |

&emsp;&emsp;【相关函数接口】

```c
AK_S32 AK_MPI_AENC_GetEncParam(AK_S32 s32AencUserId, ENC_OUT_INFO *stEncLenPam);
```

<br/>

## 版本信息获取

### AK_MPI_AENC_GetVersion

&emsp;&emsp;【描述】

&emsp;&emsp;打印音频编码库的版本号。

&emsp;&emsp;【语法】

```c
const AK_CHAR* AK_MPI_AENC_GetVersion(AK_VOID);
```

&emsp;&emsp;【返回值】

| **返回值**   | **描述** |
| --------- | ------ |
| 音频编码模块版本号 | 成功     |
| NULL      | 失败     |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_aenc.a/so

&emsp;&emsp;头文件：ak_aenc.h

&emsp;&emsp;【接口调用顺序】

&emsp;&emsp;任何位置都可以调用。

### AK_MPI_AENC_GetEncVersion

&emsp;&emsp;【描述】

&emsp;&emsp;获取音频编码库的版本号。

&emsp;&emsp;【语法】

```c
AK_CHAR *AK_MPI_AENC_GetEncVersion(AK_VOID);
```

&emsp;&emsp;【返回值】

| **返回值**  | **描述** |
| -------- | ------ |
| 音频编码库版本号 | 成功     |
| NULL     | 失败     |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_aenc.a/so  libakaudiocodec.a/so 或者libakaac.a/so libakamr.a/so libakmp3.a/so

&emsp;&emsp;头文件：ak_aenc.h

&emsp;&emsp;【接口调用顺序】

- open之后调用

### AK_MPI_AENC_SetLibPrintLevel

&emsp;&emsp;【描述】

&emsp;&emsp;设置音频编码库的打印等级

&emsp;&emsp;【语法】

```c
AK_S32 AK_MPI_AENC_SetLibPrintLevel(AK_U32 u32PrintLevel);
```

​        【参数】

| 参数名称          | 描述   | 取值范围                    | 输入/输出 |
| ------------- | ---- | ----------------------- | ----- |
| u32PrintLevel | 打印等级 | 可参考ATCLIB_PRINT_LEVEL_E | 输入    |

&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

​    【错误码】

| **错误码**                | **描述** |
| ---------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | 参数不合法  |

【需求】

&emsp;&emsp;库文件：libmpi_aenc.a/so  libakaudiocodec.a/so

&emsp;&emsp;头文件：ak_aenc.h ak_common_audio.h

&emsp;&emsp;【接口调用顺序】

&emsp;&emsp;任何位置都可以调用,建议在open之前调用

## 注册编码器函数

### AK_MPI_AENC_RegisterEncoder

​    【描述】

​        注册编码器

​    【语法】

```c
AK_S32 AK_MPI_AENC_RegisterEncoder(AENC_ENCODE_S *pstEncode);
```

​    【参数】

| **参数名称**  | **描述**    | **取值范围**        | **输入/输出** |
| --------- | --------- | --------------- | --------- |
| pstEncode | 注册编码属性结构体 | 参考AENC_ENCODE_S | 输入        |

​    【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

​    【错误码】

| **错误码**                 | **描述** |
| ----------------------- | ------ |
| ERROR_TYPE_POINTER_NULL | 参数为空   |
| ERROR_TYPE_INVALID_ARG  | 参数不合法  |

​    【举例】

```c
AENC_ENCODE_S pstEncode = {0};
    pstEncode.enType = AK_AUDIO_TYPE_MP3;
    pstEncode.pfnEncOpen = AENC_OpenMp3;  //编码器注册回调函数
    pstEncode.pfnEncClose = NULL;//编码器注册回调函数
    pstEncode.pfnEncFlush= NULL;//编码器注册回调函数
    pstEncode.pfnEncProcess= NULL;//编码器注册回调函数
    pstEncode.pfnEncReset= NULL;//编码器注册回调函数
ret = AK_MPI_AENC_RegisterEncoder(&pstEncode);
    if(ret) {
        AK_BASE_PrintErrorEx(MODULE_AENC,"AK_IMP_AENC_RegisterEecoder failed\n");
        return ret;
    }
//打开编码器
    AENC_PARAM_S stAencParam = {0};

    stAencParam.enType = AK_AUDIO_TYPE_MP3;    //编码类型
    stAencParam.enSampleBits = AK_AUDIO_SMPLE_BIT_16; //采样精度
    stAencParam.enSampleRate= AK_AUDIO_SAMPLE_RATE_16000; //采样率
    stAencParam.enSoundMode = AUDIO_SOUND_MODE_MONO;     //声道模式

    if(AK_MPI_AENC_Open(s32AencUserId, &stAencParam)) {
        AK_BASE_PrintErrorEx(MODULE_ID_APP, "AK_MPI_AENC_Open failed\n");
        return AK_FAILED;
    }
```

​    【需求】

&emsp;&emsp;库文件：libmpi_aenc.a/so  libakaudiocodec.a/so 或者 libakaac.a/so libakmp3.a/so libakamr.a/so

&emsp;&emsp;头文件：ak_aenc.h  aenc_mp3.h aenc_aac.h aenc_amr.h

【注意】

- 同一种编码协议不允许重复注册编码器，例如假如已注册 MP3编码器，不允许另
  外再注册一个 MP3编码器。
- 另外单独会分别提供一个MP3 AAC以及AMR的库和对应的头文件，其举例上的回调函数会在头文件里声明。
- 如果不是默认支持的编码格式，需要调用这个接口来注册编码器，在AK_MPI_AENC_Open之前，目前并不支持用户自带的编码器。
- AENC_ENCODE_S 关于这个结构体赋值，目前只支持AENC_OpenXXX,其他的参数可以不填。

## 打开/关闭模块

### AK_MPI_AENC_Open

&emsp;&emsp;【描述】

&emsp;&emsp;打开音频编码，支持多路编码，每个编码器对应一个句柄，支持同时编码4路音频。

&emsp;&emsp;【语法】

```c
AK_S32 AK_MPI_AENC_Open(AK_S32 s32AencUserId, const AENC_PARAM_S *pstParam);
```

​       【参数】

| 参数名称          | 描述         | 取值范围              | 输入/输出 |
| ------------- | ---------- | ----------------- | ----- |
| s32AencUserId | 音频编码模块句柄id | [0,3]             | 输入    |
| pstParam      | 音频编码输入参数   | 参考AENC_PARAM_S结构体 | 输入    |

​    【返回值】

| **返回值** | **描述** |
| ------- | ------ |
| 0       | 成功     |
| 其他      | 请参考错误码 |

   【错误码】

| 错误码                         | 描述              |
| --------------------------- | --------------- |
| ERROR_AENC_OPEN_TOO_MANY    | user的个数超过最大值    |
| ERROR_AENC_USER_NULL        | user handle 为空  |
| ERROR_TYPE_MALLOC_FAILED    | Malloc 失败       |
| ERROR_TYPE_POINTER_NULL     | 参数为空            |
| ERROR_AENC_NOT_SUPPORT_TYPE | 不支持的编码类型        |
| ERROR_TYPE_INVALID_ARG      | 参数不合法           |
| ERROR_AENC_OPEN_LIB_ERROR   | 打开编码库错误         |
| ERROR_AENC_RB_ERROR         | Ring buffer操作失败 |

​    【需求】

&emsp;&emsp;库文件：libmpi_aenc.a/so  libakaudiocodec.a/so 或者libakaac.a/so libakamr.a/so libakmp3.a/so

&emsp;&emsp;头文件：ak_aenc.h

&emsp;&emsp;【接口调用顺序】

![AENC接口调用顺序：Open、SendFrame、GetStream、ReleaseStream、Close](img/aenc-call-sequence.jpg)

&emsp;&emsp;【接口配对关系】

```c
AK_S32 AK_MPI_AENC_Close(AK_S32 s32AencUserId);
```

&emsp;&emsp;【注意】

&emsp;&emsp;可以open多次，每次open相当于增加一个新的用户，但是最多支持打开4个用户。

### AK_MPI_AENC_Close

&emsp;&emsp;【描述】

&emsp;&emsp;关闭音频编码。

&emsp;&emsp;【语法】

```c
AK_S32 AK_MPI_AENC_Close(AK_S32 s32AencUserId);
```

&emsp;&emsp;【参数】

| **参数名称**      | **描述**     | **取值范围** | **输入/输出** |
| ------------- | ---------- | -------- | --------- |
| s32AencUserId | 音频编码模块句柄ID | [0,3]    | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ------- | ------ |
| 0       | 成功     |
| 其他      | 请参考错误码 |

&emsp;&emsp;【错误码】

| **错误码**                    | **描述**           |
| -------------------------- | ---------------- |
| ERROR_AENC_USER_NULL       | user handle 为空   |
| ERROR_TYPE_POINTER_NULL    | 参数指针为空           |
| ERROR_AENC_CLOSE_LIB_ERROR | 解码库关闭错误          |
| ERROR_AENC_RB_ERROR        | Ring buffer 设置错误 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_aenc.a/so  libakaudiocodec.a/so 或者libakaac.a/so libakamr.a/so libakmp3.a/so

&emsp;&emsp;头文件：ak_aenc.h

&emsp;&emsp;【接口调用顺序】

![AENC接口调用顺序：Open、SendFrame、GetStream、ReleaseStream、Close](img/aenc-call-sequence.jpg)

&emsp;&emsp;【接口配对关系】

```c
   AK_S32 AK_MPI_AENC_Open(AK_S32 s32AencUserId,const AENC_PARAM_S *pstParam);
```

&emsp;&emsp;【注意】

&emsp;&emsp;调用AK_MPI_AENC_Close可以多次关闭。关闭不存在s32AencUserId，会报错。

<br/>

## 编码流程

### AK_MPI_AENC_SendFrame

&emsp;&emsp;【描述】

&emsp;&emsp;发送需要编码的音频帧。对于不同的编码格式，编码一帧数据需要的pcm长度对应如下：

&emsp;&emsp;【语法】

```c
AK_S32 AK_MPI_AENC_SendFrame(AK_S32 s32AencUserId, const FRAME_S *pstPcmFrame,AK_U32 u32TimeOut);
```

&emsp;&emsp;【参数】

| **参数名称**      | **描述**                                                     | **取值范围**                 | **输入/输出** |
| ------------- | ---------------------------------------------------------- | ------------------------ | --------- |
| s32AencUserId | 音频编码模块句柄id                                                 | [0,3]                    | 输入        |
| pstPcmFrame   | 待编码一帧数据                                                    | 参考struct FRAME_S结构体      | 输入        |
| u32TimeOut    | 获取数据超时时间：0表示非阻塞模式，<br />无数据时则返回报错；>0表示阻塞Timeout时间，超时则报错返回。 | 0或阻塞时间（阻塞单位;ms）[0,60000] | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码】

| **错误码**                      | **描述**         |
| ---------------------------- | -------------- |
| ERROR_AENC_USER_NULL         | user handle 为空 |
| ERROR_TYPE_POINTER_NULL      | 参数为空           |
| ERROR_TYPE_INVALID_ARG       | 参数不正确          |
| ERROR_AENC_LIST_CNT_TOO_MANY | 编码缓存区已满        |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_aenc.a/so  libakaudiocodec.a/so 或者libakaac.a/so libakamr.a/so libakmp3.a/so

&emsp;&emsp;头文件：ak_aenc.h

&emsp;&emsp;【接口调用顺序】

![AENC接口调用顺序：Open、SendFrame、GetStream、ReleaseStream、Close](img/aenc-call-sequence.jpg)

【注意】

- 调用该接口发送音频编码音频帧时，必须要先open。

- u32TimeOut等于0时，采用非阻塞模式获取数据，大于0时，阻塞u32TimeOut（ms）后,送不进去数据则超时并报错。

&emsp;&emsp;

### AK_MPI_AENC_GetStream

&emsp;&emsp;【描述】

&emsp;&emsp;获取一帧编码后的数据。

&emsp;&emsp;【语法】

```c
AK_S32 AK_MPI_AENC_GetStream(AK_S32 s32AencUserId, AUDIO_STREAM_S *pstStream, AK_U32 u32TimeOut);
```

&emsp;&emsp;【参数】

| **参数名称**      | **描述**                                                     | **取值范围**                 | **输入/输出** |
| ------------- | ---------------------------------------------------------- | ------------------------ | --------- |
| s32AencUserId | 音频编码模块句柄id                                                 | [0,3]                    | 输入        |
| pstStream     | 编码后的一帧数据                                                   | 参考AUDIO_STREAM_S结构体      | 输出        |
| u32TimeOut    | 获取数据超时时间：0表示非阻塞模式，<br />无数据时则返回报错；>0表示阻塞Timeout时间，超时则报错返回。 | 0或阻塞时间（阻塞单位;ms）[0,60000] | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码】

| **错误码**                  | **描述**         |
| ------------------------ | -------------- |
| ERROR_AENC_USER_NULL     | user handle 为空 |
| ERROR_TYPE_POINTER_NULL  | 参数为空           |
| ERROR_TYPE_INVALID_ARG   | 参数不正确          |
| ERROR_AENC_NO_DATA       | 没有编码数据         |
| ERROR_TYPE_MALLOC_FAILED | Malloc 失败      |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_aenc.a/so  libakaudiocodec.a/so 或者libakaac.a/so libakamr.a/so libakmp3.a/so

&emsp;&emsp;头文件：ak_aenc.h

&emsp;&emsp;【接口调用顺序】

![AENC接口调用顺序：Open、SendFrame、GetStream、ReleaseStream、Close](img/aenc-call-sequence.jpg)

​        【注意】

- u32TimeOut等于0时，采用非阻塞模式获取数据，大于0时，阻塞u32TimeOut（ms）后,没有数据则返回超时并报错。

<br/>

### AK_MPI_AENC_ReleaseStream

&emsp;&emsp;【描述】

&emsp;&emsp;释放一帧编码后的数据。

&emsp;&emsp;【语法】

```c
  AK_S32 AK_MPI_AENC_ReleaseStream(AK_S32 s32AencUserId, AUDIO_STREAM_S *pstStream);
```

&emsp;&emsp;【参数】

| **参数名称**      | **描述**     | **取值范围**         | **输入/输出** |
| ------------- | ---------- | ---------------- | --------- |
| s32AencUserId | 音频编码模块句柄id | [0,3]            | 输入        |
| pstStream     | 编码后的一帧数据   | 参考AUDIO_STREAM_S | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码】

| **错误码**                 | **描述** |
| ----------------------- | ------ |
| ERROR_TYPE_POINTER_NULL | 参数为空   |
| ERROR_TYPE_INVALID_ARG  | 参数不正确  |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_aenc.a/so  libakaudiocodec.a/so 或者libakaac.a/so libakamr.a/so libakmp3.a/so

&emsp;&emsp;头文件：ak_aenc.h

&emsp;&emsp;【接口调用顺序】

![AENC接口调用顺序：Open、SendFrame、GetStream、ReleaseStream、Close](img/aenc-call-sequence.jpg)

​        【注意】

### AK_MPI_AENC_SendEndOfFrame

&emsp;&emsp;【描述】

&emsp;&emsp;释放一帧编码后的数据。

&emsp;&emsp;【语法】

```c
AK_S32 AK_MPI_AENC_SendEndOfFrame(AK_S32 s32AencUserId);
```

&emsp;&emsp;【参数】

| 参数名称          | 描述         | 取值范围  | 输入/输出 |
| ------------- | ---------- | ----- | ----- |
| s32AencUserId | 音频编码模块句柄id | [0,3] | 输入    |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码】

| **错误码**                 | **描述** |
| ----------------------- | ------ |
| ERROR_TYPE_POINTER_NULL | 参数为空   |
| ERROR_TYPE_INVALID_ARG  | 参数不正确  |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_aenc.a/so  libakaudiocodec.a/so 或者libakaac.a/so libakamr.a/so libakmp3.a/so

&emsp;&emsp;头文件：ak_aenc.h

&emsp;&emsp;【接口调用顺序】

![AENC接口调用顺序：Open、SendFrame，结束时SendEndOfFrame，GetStream、ReleaseStream、Close](img/aenc-call-sequence-send-end-of-frame.jpg)

​        【注意】

## 调试接口

### AK_MPI_AENC_SaveFile

&emsp;&emsp;【描述】

&emsp;&emsp;保存AENC模块内部音频处理的过程文件。保存文件类型为两种：一是传给AENC模块的音频，一为经过AENC模块处理之后输出的音频。

&emsp;&emsp;【语法】

```c
AK_S32 AK_MPI_AENC_SaveFile(AK_S32 s32AencUserId, AUDIO_SAVE_FILE_INFO_S *pstSaveFileInfo);
```

&emsp;&emsp;【参数】

| 参数名称            | 描述         | 取值范围                        | 输入/输出 |
| --------------- | ---------- | --------------------------- | ----- |
| s32AencUserId   | 音频编码模块句柄id | [0,3]                       | 输入    |
| pstSaveFileInfo | 保存文件的信息    | 参考AUDIO_SAVE_FILE_INFO_S结构体 | 输入    |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ------- | ------ |
| 0       | 成功     |
| 其他      | 请参考错误码 |

&emsp;&emsp;【错误码】

| **错误码**                     | **描述**         |
| --------------------------- | -------------- |
| ERROR_TYPE_POINTER_NULL     | 参数为空           |
| ERROR_TYPE_INVALID_ARG      | 参数不正确          |
| ERROR_AENC_USER_NULL        | user handle 为空 |
| ERROR_TYPE_FILE_OPEN_FAILED | 打开文件失败         |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_aenc.a/so  libakaudiocodec.a/so 或者libakaac.a/so libakamr.a/so libakmp3.a/so

&emsp;&emsp;头文件：ak_aenc.h

&emsp;&emsp;【接口调用顺序】

![AENC接口调用顺序：Open、SaveFile、Close](img/aenc-call-sequence-save-file.jpg)

【注意】

- 当需要保存AENC模块处理过程的音频来查找问题时，可调用此接口

## 清除缓存

### AK_MPI_AENC_ClearEncodeBuf

&emsp;&emsp;【描述】

&emsp;&emsp;清除编码区的缓存。如在编码过程中出现暂停，重新编码时调用该接口可以清除之前未完成的编码操作的残留数据。

&emsp;&emsp;【语法】

```c
AK_S32 AK_MPI_AENC_ClearEncodeBuf(AK_S32 s32AencUserId);
```

&emsp;&emsp;【参数】

| **参数名称**      | **描述**     | **取值范围** | **输入/输出** |
| ------------- | ---------- | -------- | --------- |
| s32AencUserId | 音频编码模块句柄id | [0,3]    | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码】

| **错误码**              | **描述**         |
| -------------------- | -------------- |
| ERROR_AENC_USER_NULL | user handle 为空 |
| ERROR_AENC_RB_ERROR  | ring buffer错误  |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_aenc.a/so  libakaudiocodec.a/so 或者libakaac.a/so libakamr.a/so libakmp3.a/so

&emsp;&emsp;头文件：ak_aenc.h

&emsp;&emsp;【接口调用顺序】

![AENC接口调用顺序：Open、SendFrame、GetStream、ReleaseStream、ClearEncodeBuf、Close](img/aenc-call-sequence-clear-encode-buf.jpg)

## 获取参数

### AK_MPI_AENC_GetEncParam

​    【描述】

获取编码器打开后的参数

​    【语法】

```c
AK_S32 AK_MPI_AENC_GetEncParam(AK_S32 s32AencUserId, ENC_OUT_INFO *stEncLenPam);
```

​    【参数】

| 参数名称          | 描述         | 取值范围              | 输入/输出 |
| ------------- | ---------- | ----------------- | ----- |
| s32AencUserId | 音频编码模块句柄id | [0,3]             | 输入    |
| stEncLenPam   | 编码器参数      | 参考ENC_OUT_INFO结构体 | 输出    |

​    【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

​    【错误码】

| **错误码**              | **描述**         |
| -------------------- | -------------- |
| ERROR_AENC_USER_NULL | user handle 为空 |
| ERROR_AENC_RB_ERROR  | ring buffer错误  |

【需求】

&emsp;&emsp;库文件：libmpi_aenc.a/so  libakaudiocodec.a/so 或者libakaac.a/so libakamr.a/so libakmp3.a/so

&emsp;&emsp;头文件：ak_aenc.h

## 接口调用依赖

&emsp;&emsp;AENC模块对外提供的接口函数在调用时存在一定的依赖关系，如下表所示：

| **接口**                       | **接口依赖关系**           |
| ---------------------------- | -------------------- |
| AK_MPI_AENC_GetEncVersion    | 无依赖                  |
| AK_MPI_AENC_SetLibPrintLevel | 无依赖                  |
| AK_MPI_AENC_GetVersion       | AK_MPI_AENC_Open之后调用 |
| AK_MPI_AENC_Open             | -                    |
| AK_MPI_AENC_SendFrame        | AK_MPI_AENC_Open之后调用 |
| AK_MPI_AENC_GetStream        | AK_MPI_AENC_Open之后调用 |
| AK_MPI_AENC_ReleaseStream    | AK_MPI_AENC_Open之后调用 |
| AK_MPI_AENC_ClearEncodeBuf   | AK_MPI_AENC_Open之后调用 |
| AK_MPI_AENC_Close            | AK_MPI_AENC_Open之后调用 |
| AK_MPI_AENC_RegisterEncoder  | AK_MPI_AENC_Open之前调用 |
| AK_MPI_AENC_SaveFile         | AK_MPI_AENC_Open之后调用 |
| AK_MPI_AENC_SendEndOfFrame   | AK_MPI_AENC_Open之后调用 |
| AK_MPI_AENC_GetEncParam      | AK_MPI_AENC_Open之后调用 |

<br/>

## ak_aenc_sample使用示例

### sample命令和参数

运行此sample前，需要先insmod ak_pcm.ko，一般开启都会默认加载。

| 输入参数（短参） | 输入参数（长参）       | **输入参数说明**                                                                   |
| -------- | -------------- | ---------------------------------------------------------------------------- |
| h        | help           | 打印帮助信息。                                                                      |
| s        | sample-rate    | 音频采样率，支持8000和16000、 44100Hz、48000Hz采样率。                                      |
| p        | path           | PCM文件保存路径，无需指定文件名，在文件路径末尾要带"/"符号， 例如路径可以配置为: /mnt/。                          |
| t        | second         | 采集时间，以秒为单位。                                                                  |
| d        | device-type    | 设备类型,0:DEV_ADC,1:DEV_PDM,2:DEV_I2S0_AI。                                      |
| m        | config-file    | 音频配置文件全路径。                                                                   |
| n        | config-section | 音频配置文件section name， def_near：用于ai单麦克风；two_array_near：用于AI双麦克风; def_far：用于AO。 |
| f        | save-file      | 是否保存编码文件[0:不保存文件,1:保存文件]                                                     |
| e        | encode-type    | 编码类型[mp3 aac amr g711a g711u pcm]                                            |

### sample存储和文件命令

（1）sample输出的文件格式默认使用MP3格式。
（2）sample输出的文件默认存储到/mnt/目录下。
（3）sample输出的文件名默认使用yyyymmdd-ddmmss采样率通道数时长（ms）设备.mp3 。

### 应用案例

ak_aenc_sample -t 20 -s 16000 -e mp3 -d 0 -f 1 -p /mnt/ -m /etc/config/audio_config.ini -n def_near

## /var/platform说明

/var/platform目录用于查看当前模块的配置参数和状态信息，下面是该模块的/var/platform/的参数说明。

### param

| 参数        | 说明   |
| --------- | ---- |
| SoundMode | 采样率  |
| SoundMode | 声道模式 |
| SampleBit | 采样精度 |
| UserCnt   | 用户数  |
| AencType  | 编码类型 |

### stat

| 参数                | 说明               |
| ----------------- | ---------------- |
| Mp3Version        | MP3库版本号          |
| AudioCodecVersion | 编解码库版本号          |
| AencMpiVersion    | 平台编码库版本号         |
| BitRate           | 编码类型对应的比特率       |
| FrameSize         | 编码类型对应的编码输出长度    |
| SampleParFrame    | 编码类型对应的每帧编码需要的样点 |

<br/>

## 错误码说明

| 错误代码       | 宏定义                          | 含义     |
| ---------- | ---------------------------- | ------ |
| 0x0f000000 | ERROR_AENC_OPEN_LIB_ERROR    | 打开库失败  |
| 0x0f000001 | ERROR_AENC_CLOSE_LIB_ERROR   | 关闭库失败  |
| 0x0f000002 | ERROR_AENC_OPEN_TOO_MANY     | 打开太多句柄 |
| 0x0f000003 | ERROR_AENC_NOT_SUPPORT_TYPE  | 不支持的类型 |
| 0x0f000004 | ERROR_AENC_INVALID_PARAM     | 参数错误   |
| 0x0f000005 | ERROR_AENC_USER_NULL         | 用户为空   |
| 0x0f000006 | ERROR_AENC_LIST_CNT_TOO_MANY | 列表数太多  |
| 0x0f000007 | ERROR_AENC_RB_ERROR          | RB错误   |
| 0x0f000008 | ERROR_AENC_NO_DATA           | 没有数据   |
| 0x0f000009 | ERROR_AENC_AUDIO_CODEC_ERROR | 编码错误   |
| 0x0f00000a | ERROR_AENC_NOT_OPEN          | 模块没有打开 |

<br/>
