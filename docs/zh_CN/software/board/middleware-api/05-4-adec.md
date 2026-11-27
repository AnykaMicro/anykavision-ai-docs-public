# 音频解码

## 概述

&emsp;&emsp;音频解码模块（ADEC模块）主要负责把发送到音频解码模块的音频数据进行解码，然后输出解码后的PCM裸数据。ADEC模块支持多种解码格式。

<br/>

## API参考

&emsp;&emsp;本模块提供API参考，如下表所示。

| **数据结构**         | **描述**   |
| ---------------- | -------- |
| AUDIO_TYPE_E     | 音频编解码类型  |
| ADEC_PARAM_S     | 音频解码输入参数 |
| FRAME_S          | 音频帧结构    |
| ADEC_AAC_PARAM_S | aac解码格式  |
| DEC_BUF_STATUS_S | 解码模块缓存信息 |
| ADEC_DECODE_S    | 注册解码器结构体 |

<br/>

| **函数接口**                       | **描述**              |
| ------------------------------ | ------------------- |
| AK_MPI_ADEC_GetVersion         | 获取音频解码库的版本号         |
| AK_MPI_ADEC_Open               | 打开音频解码              |
| AK_MPI_ADEC_Close              | 关闭音频解码              |
| AK_MPI_ADEC_SetOutputPcmLen    | 设置解码后输出数据的长度        |
| AK_MPI_ADEC_ClearDecodeBuf     | 清除解码区的缓存            |
| AK_MPI_ADEC_SendStream         | 发送要解码的音频            |
| AK_MPI_ADEC_GetFrame           | 获取一帧解码后的数据          |
| AK_MPI_ADEC_ReleaseFrame       | 释放一帧解码后的数据          |
| AK_MPI_ADEC_SendEndofStream    | 告诉解码器音频解码数据已经发送完成   |
| AK_MPI_ADEC_PrintRuntimeStatus | 打印ADEC模块的debug信息    |
| AK_MPI_ADEC_SaveFile           | 保存ADEC模块内部音频处理的过程文件 |
| AK_MPI_ADEC_GetBufStatus       | 获取解码模块缓存区信息         |
| AK_MPI_ADEC_RegisterDecoder    | 注册解码器               |
| AK_MPI_ADEC_SetLibPrintLevel   | 设置解码库打印等级           |
| <br/>                          |                     |

## 数据结构

### AUDIO_TYPE_E

&emsp;&emsp;【说明】

&emsp;&emsp;音频编解码类型。目前默认支持PCM、G711a/u，如需支持其他类型编解码，需要通过调用AK_MPI_ADEC_RegisterEncoder来注册编码器。

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

&emsp;&emsp;不同解码格式支持的采样率如下：

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

【相关接口】

```c
AK_S32 AK_MPI_ADEC_Open(AK_S32 s32AdecUserId,const ADEC_PARAM_S *pstParam);
```

<br/>

### ADEC_PARAM_S

&emsp;&emsp;【说明】

&emsp;&emsp;音频解码输入参数。

&emsp;&emsp;【定义】

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

&emsp;&emsp;【成员】

| 成员名称         | 描述      |
| ------------ | ------- |
| enType       | 音频解码类型  |
| enSampleRate | 音频采样率   |
| enSampleBits | 音频采集精度  |
| enSoundMode  | 音频声道模式  |
| unAdecAttr   | 解码属性联合体 |

&emsp;&emsp;【相关函数接口】

```c
AK_S32 AK_MPI_ADEC_Open(AK_S32 s32AdecUserId,const ADEC_PARAM_S *pstParam,);
```

<br/>

### FRAME_S

&emsp;&emsp;【说明】

&emsp;&emsp;音频解码后输出帧。

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

| 成员名称     | 描述            |
| -------- | ------------- |
| pu8Data  | 音频解码后一帧数据的指针  |
| u32Len   | 音频解码后一帧数据的长度  |
| u64Ts    | 音频解码后一帧数据的时间戳 |
| u64SeqNo | 音频解码后一帧数据的序号  |

&emsp;&emsp;【相关函数接口】

```c
AK_S32 AK_MPI_ADEC_GetFrame(AK_S32 s32AdecUserId, FRAME_S *pstPcmFrame, AK_U32 u32TimeOut);
AK_S32 AK_MPI_ADEC_ReleaseFrame(AK_S32 s32AdecUserId, FRAME_S *pstPcmFrame);
```

### DEC_BUF_STATUS_S

&emsp;&emsp;【说明】

&emsp;&emsp;解码模块缓存信息。包括缓存总大小，缓存区当前数据大小。

&emsp;&emsp;【定义】

```c
typedef struct akDEC_BUF_STATUS_S
{
    AK_S32 s32BufTotalLen;
    AK_S32 s32BufRemainLen;
} DEC_BUF_STATUS_S;
```

&emsp;&emsp;【成员】

| 成员名称            | 描述                 |
| --------------- | ------------------ |
| s32BufTotalLen  | 获取解码器输入buffer的总大小  |
| s32BufRemainLen | 获取解码器输入buffer的剩余大小 |

​    【相关函数接口】

```c
AK_S32 AK_MPI_ADEC_GetBufStatus(AK_S32 s32AdecUserId, DEC_BUF_STATUS_S *pstBufStatus)
```

<br/>

### ADEC_AAC_PARAM_S

&emsp;&emsp;【说明】

&emsp;&emsp;aac解码格式。

&emsp;&emsp;【定义】

```c
typedef struct akADEC_AAC_PARAM_S
{
    AK_U16 u16AacStreamFormat;
}ADEC_AAC_PARAM_S;
```

&emsp;&emsp;【成员】

| **成员名称**           | **描述**                                                                                                                                                                                                                                           |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| u16AacStreamFormat | aac解码模式参数。<br/>0：auto detect 是库根据流最开始的几个字节，自行判断流的格式；<br/>1：adts 每帧都有一个头，解码时，即使帧内有错误，也能跳过有问题的帧，找到下一帧继续解码。网络传输和媒体文件中多是这个格式。传输中不可避免会出现错帧和丢帧（丢整帧或者半帧），用 adts 格式是好的选择；<br/>2：adif 只在文件开头有一个头，后面就是裸码流，此格式是比较旧的存储格式，现在基本不会使用；<br/>3：raw 即裸码流，是不带任何帧头的流。 |

&emsp;&emsp;【相关函数接口】

```c
AK_S32 AK_MPI_ADEC_Open(AK_S32 s32AdecUserId,const ADEC_PARAM_S *pstParam);
```

​        【注意】

- 由于 raw 和 adif 缺少帧头，库无法确定音频帧的边界，也无法校验流中的错误，只能假定流是完全正确的来进行解码。流的内容中只要错一个bit，解码库就会报错而没法继续往下解码。

## 版本信息获取

### AK_MPI_ADEC_GetVersion

&emsp;&emsp;【描述】

&emsp;&emsp;获取音频解码模块的版本号。

&emsp;&emsp;【语法】

```c
const AK_CHAR* AK_MPI_ADEC_GetVersion(AK_VOID);
```

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ------- | ------ |
| 0       | 成功     |
| 其他      | 请参考错误码 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libakaudiocodec.a

&emsp;&emsp;头文件：ak_adec.h

&emsp;&emsp;【接口调用顺序】

&emsp;&emsp;任何位置都可以调用。

### AK_MPI_ADEC_GetEncVersion

&emsp;&emsp;【描述】

&emsp;&emsp;获取音频编码库的版本号。

&emsp;&emsp;【语法】

```c
AK_CHAR *AK_MPI_ADEC_GetEncVersion(AK_VOID);
```

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ------- | ------ |
| 0       | 成功     |
| 其他      | 请参考错误码 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_adec.a/so  libakaudiocodec.a/so 或者libakaac.a/so libakamr.a/so libakmp3.a/so

&emsp;&emsp;头文件：ak_adec.h

&emsp;&emsp;【接口调用顺序】

- open之后调用

### **AK_MPI_ADEC_SetLibPrintLevel**

&emsp;&emsp;【描述】

&emsp;&emsp;设置音频编解码库的打印等级

&emsp;&emsp;【语法】

```c
AK_S32 AK_MPI_ADEC_SetLibPrintLevel(AK_U32 u32PrintLevel);
```

&emsp;&emsp;【参数】

| 参数名称          | 描述   | 取值范围                    | 输入/输出 |
| ------------- | ---- | ----------------------- | ----- |
| s32PrintLevel | 打印等级 | 可参考ATCLIB_PRINT_LEVEL_E | 输入    |

【返回值】

| **返回值** | **描述** |
| ------- | ------ |
| 0       | 成功     |
| 其他      | 请参考错误码 |

&emsp;【错误码】&emsp;

| **错误码**                | **描述** |
| ---------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | 参数不合法  |

【需求】

&emsp;&emsp;库文件：libmpi_adec.a/so、libakaudiocodec.a/so  或者libakaac.a/so libakamr.a/so libakmp3.a/so

&emsp;&emsp;头文件：ak_adec.h

&emsp;&emsp;【接口调用顺序】

&emsp;&emsp;任何位置都可以调用。

<br/>

## 注册解码器函数

### **AK_MPI_ADEC_RegisterDecoder**

【描述】

注册解码器

【语法】

```c
AK_S32 AK_MPI_ADEC_RegisterDecoder(ADEC_DECODE_S * pstDecode);
```

【参数】

| **参数名称**  | **描述**     | **取值范围**        | **输入/输出** |
| --------- | ---------- | --------------- | --------- |
| pstDecode | 注册解码器属性结构体 | 参考ADEC_DECODE_S | 输入        |

【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

【错误码】

| **错误码**                 | **描述** |
| ----------------------- | ------ |
| ERROR_TYPE_POINTER_NULL | 参数为空   |
| ERROR_TYPE_INVALID_ARG  | 参数不合法  |

【需求】

库文件：libmpi_adec.a/so、libakaudiocodec.a/so  或者libakaac.a/so libakamr.a/so libakmp3.a/so

头文件：ak_adec.h 或者adec_amr.h adec_mp3.h adec_aac.h

【接口调用顺序】

在AK_MPI_ADEC_Open前调用

【举例】

ADEC_ENCODE_S stMyDecoder = {0};

stMyDecoder.enType = AK_AUDIO_TYPE_MP3;

stMyDecoder.pfnDecOpen = ADEC_OpenMp3;

AK_MPI_ADEC_RegisterDecoder(&stMyDecoder);

```c
ADEC_ENCODE_S stMyDecoder = {0};
stMyDecoder.enType = AK_AUDIO_TYPE_MP3;//解码类型
stMyDecoder.pfnDecOpen = ADEC_OpenMp3;//解码器注册回调函数
ret = AK_MPI_ADEC_RegisterDecoder(&pstEncode);
    if(ret) {
        AK_BASE_PrintErrorEx(MODULE_ADEC,"AK_MPI_ADEC_RegisterDecoder failed\n");
        return ret;
    }

    ADEC_PARAM_S stAdecParam = {0};
    stAdecParam.enType = s32DecType;
    stAdecParam.enSampleBits = AK_AUDIO_SMPLE_BIT_16;
    stAdecParam.enSampleRate = s32SampleRate;
    stAdecParam.enSoundMode = s32SoundMode;


    /* 打开解码器*/
    if (AK_MPI_ADEC_Open(s32AdecUserId,&stAdecParam)) {
        AK_BASE_PrintErrorEx(MODULE_ID_APP, "AK_MPI_ADEC_Open failed\n");
        return AK_FAILED;
    }
```

【注意】

- 同一种解码协议不允许重复注册解码器，例如假如已注册 MP3解码器，不允许另
  外再注册一个 MP3 解码器。
- 另外单独会分别提供一个MP3 AAC以及AMR的库和对应的头文件，其举例上的回调函数会在头文件里声明。
- 如果不是默认支持的编码格式，需要调用这个接口来注册编码器，在AK_MPI_AENC_Open之前，目前并不支持用户自带的编码器。
- ADEC_DECODE_S 关于这个结构体赋值，目前只支持ADEC_OpenXXX,其他的参数可以不填。

## 打开/关闭模块

### AK_MPI_ADEC_Open

&emsp;&emsp;【描述】

&emsp;&emsp;打开音频解码。支持多路解码，每个解码器对应一个句柄。支持同时解码4路音频。

&emsp;&emsp;【语法】

```c
AK_S32 AK_MPI_ADEC_Open(AK_S32 s32AdecUserId,const ADEC_PARAM_S *pstParam);
```

&emsp;&emsp;【参数】

| 参数名称          | 描述         | 取值范围                     | 输入/输出 |
| ------------- | ---------- | ------------------------ | ----- |
| s32AdecUserId | 音频解码模块句柄id | [0,3]                    | 输入    |
| pstParam      | 音频解码输入参数   | 参考struct ADEC_PARAM_S结构体 | 输入    |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ------- | ------ |
| 0       | 成功     |
| 其他      | 请参考错误码 |

&emsp;&emsp;【错误码】

| **错误码**                   | **描述**       |
| ------------------------- | ------------ |
| ERROR_TYPE_POINTER_NULL   | 参数指针为空       |
| ERROR_TYPE_INVALID_ARG    | 参数不正确        |
| ERROR_ADEC_OPEN_TOO_MANY  | user的个数超过最大值 |
| ERROR_TYPE_MALLOC_FAILED  | Malloc 失败    |
| ERROR_ADEC_OPEN_LIB_ERROR | 打开解码库错误      |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_adec.a/so、libakaudiocodec.a/so  或者libakaac.a/so libakamr.a/so libakmp3.a/so

&emsp;&emsp;头文件：ak_adec.h

&emsp;&emsp;【接口调用顺序】

![ADEC接口调用顺序：Open、SendStream、GetFrame、ReleaseFrame、Close](img/adec-call-sequence.jpg)

&emsp;&emsp;【接口配对关系】

```c
AK_S32 AK_MPI_ADEC_Close(AK_S32 s32AdecUserId);
```

### AK_MPI_ADEC_Close

&emsp;&emsp;【描述】

&emsp;&emsp;关闭音频解码。

&emsp;&emsp;【语法】

```c
AK_S32 AK_MPI_ADEC_Close(AK_S32 s32AdecUserId);
```

&emsp;&emsp;【参数】

| 参数名称          | 描述         | 取值范围  | 输入/输出 |
| ------------- | ---------- | ----- | ----- |
| s32AdecUserId | 音频解码模块句柄id | [0,3] | 输入    |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码】

| **错误码**              | **描述**         |
| -------------------- | -------------- |
| ERROR_ADEC_USER_NULL | user handle 为空 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_adec.a/so、libakaudiocodec.a/so  或者libakaac.a/so libakamr.a/so libakmp3.a/so

&emsp;&emsp;头文件：ak_adec.h

&emsp;&emsp;【接口调用顺序】

![ADEC接口调用顺序：Open、SendStream、GetFrame、ReleaseFrame、Close](img/adec-call-sequence.jpg)

&emsp;&emsp;【接口配对关系】

```c
AK_S32 AK_MPI_ADEC_Open(AK_S32 s32AdecUserId,const ADEC_PARAM_S *pstParam);
```

<br/>

## 解码流程

### AK_MPI_ADEC_SendStream

&emsp;&emsp;【描述】

&emsp;&emsp;发送要解码的音频。

&emsp;&emsp;【语法】

```c
AK_S32 AK_MPI_ADEC_SendStream(AK_S32 s32AdecUserId, const AK_U8 *pu8Data,const AK_U32 u32Len, AK_U32 u32TimeOut);
```

&emsp;&emsp;【参数】

| 参数名称          | 描述                                                         | 取值范围                     | 输入/输出 |
| ------------- | ---------------------------------------------------------- | ------------------------ | ----- |
| s32AdecUserId | 音频解码模块句柄id                                                 | [0,3]                    | 输入    |
| pu8Data       | 带解码的音频数据存放的地址                                              | 数据长度等于len                | 输入    |
| u32Len        | 待解码音频流数据长度                                                 | 小于4096                   | 输入    |
| u32TimeOut    | 获取数据超时时间：0表示非阻塞模式，<br />无数据时则返回报错；>0表示阻塞Timeout时间，超时则报错返回。 | 0或阻塞时间（阻塞单位;ms）[0,60000] | 输入    |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码】

| **错误码**                         | **描述**         |
| ------------------------------- | -------------- |
| ERROR_TYPE_POINTER_NULL         | 参数指针为空         |
| ERROR_ADEC_SEND_STREAM_ERROR    | Send stream 出错 |
| ERROR_ADEC_SEND_STREAM_NO_SPACE | 解码空间不足         |
| ERROR_ADEC_USER_NULL            | user handle 为空 |
| ERROR_TYPE_INVALID_ARG          | 参数不正确          |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_adec.a/so、libakaudiocodec.a/so  或者libakaac.a/so libakamr.a/so libakmp3.a/so

&emsp;&emsp;头文件：ak_adec.h

&emsp;&emsp;【接口调用顺序】

![ADEC接口调用顺序：Open、SendStream、GetFrame、ReleaseFrame、Close](img/adec-call-sequence.jpg)

【注意】

​    函数可重入，在调用AK_MPI_ADEC_Open之后调用；

### AK_MPI_ADEC_GetFrame

&emsp;&emsp;【描述】

&emsp;&emsp;获取一帧解码后的数据。

&emsp;&emsp;【语法】

```C
AK_S32 AK_MPI_ADEC_GetFrame(AK_S32 s32AdecUserId, FRAME_S *pstPcmFrame, AK_U32 u32TimeOut);
```

&emsp;&emsp;【参数】

| 参数名称          | 描述                                                         | 取值范围                     | 输入/输出 |
| ------------- | ---------------------------------------------------------- | ------------------------ | ----- |
| s32AdecUserId | 音频解码模块句柄id                                                 | [0,3]                    | 输入    |
| pstPcmFrame   | 获取到解码后的一帧数据                                                | 参考struct FRAME_S         | 输入    |
| u32TimeOut    | 获取数据超时时间：0表示非阻塞模式，<br />无数据时则返回报错；>0表示阻塞Timeout时间，超时则报错返回。 | 0或阻塞时间（阻塞单位;ms）[0,60000] | 输入    |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码】

| **错误码**                      | **描述**               |
| ---------------------------- | -------------------- |
| ERROR_TYPE_POINTER_NULL      | 参数指针为空               |
| ERROR_TYPE_INVALID_ARG       | 参数不正确                |
| ERROR_ADEC_STREAM_END        | 解码数据已经全部送出           |
| ERROR_ADEC_USER_NULL         | user handle 为空       |
| ERROR_ADEC_GET_FRAME_NO_DATA | get frame buffer没有空间 |
| ERROR_ADEC_ATC_LIB_ERROR     | 解码库错误                |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_adec.a/so、libakaudiocodec.a/so  或者libakaac.a/so libakamr.a/so libakmp3.a/so

&emsp;&emsp;头文件：ak_adec.h

&emsp;&emsp;【接口调用顺序】

![ADEC接口调用顺序：Open、SendStream、GetFrame、ReleaseFrame、Close](img/adec-call-sequence.jpg)

​        【注意】

- 某一路码流解码后绑定ao播放时，发送待解码数据和获取解码后的数据使用ao进行播放必须是不同的线程，而且这两个线程只能做单独的发送待解码数据和获取解码后数据播放的操作。

### AK_MPI_ADEC_ReleaseFrame

&emsp;&emsp;【描述】

&emsp;&emsp;释放一帧解码后的数据。

&emsp;&emsp;【语法】

```c
AK_S32 AK_MPI_ADEC_ReleaseFrame(AK_S32 s32AdecUserId, FRAME_S *pstPcmFrame);
```

&emsp;&emsp;【参数】

| 参数名称          | 描述          | 取值范围             | 输入/输出 |
| ------------- | ----------- | ---------------- | ----- |
| s32AdecUserId | 音频解码模块句柄id  | [0,3]            | 输入    |
| pstPcmFrame   | 获取到解码后的一帧数据 | 参考struct FRAME_S | 输入    |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码】

| **错误码**                 | **描述**         |
| ----------------------- | -------------- |
| ERROR_TYPE_POINTER_NULL | 参数指针为空         |
| ERROR_ADEC_USER_NULL    | user handle 为空 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_adec.a/so、libakaudiocodec.a/so  或者libakaac.a/so libakamr.a/so libakmp3.a/so

&emsp;&emsp;头文件：ak_adec.h

&emsp;&emsp;【接口调用顺序】

![ADEC接口调用顺序：Open、SendStream、GetFrame、ReleaseFrame、Close](img/adec-call-sequence.jpg)

<br/>

### AK_MPI_ADEC_SendEndofStream

&emsp;&emsp;【描述】

&emsp;&emsp;告知解码器音频解码数据已经发送完成。

&emsp;&emsp;【语法】

```c
AK_S32 AK_MPI_ADEC_SendEndofStream(AK_S32 s32AdecUserId);
```

&emsp;&emsp;【参数】

| **参数名称**      | **描述**     | **取值范围** | **输入/输出** |
| ------------- | ---------- | -------- | --------- |
| s32AdecUserId | 音频解码模块句柄id | [0,3]    | 输入        |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码】

| **错误码**                         | **描述**         |
| ------------------------------- | -------------- |
| ERROR_ADEC_USER_NULL            | user handle 为空 |
| ERROR_ADEC_ATC_LIB_ERROR        | 解码库设置错误        |
| ERROR_ADEC_SEND_STREAM_NO_START | 未开始发生解码数据      |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_adec.a/so、libakaudiocodec.a/so  或者libakaac.a/so libakamr.a/so libakmp3.a/so

&emsp;&emsp;头文件：ak_adec.h

&emsp;&emsp;【接口调用顺序】

![ADEC接口调用顺序：Open、SendStream，结束时SendEndOfStream，GetFrame、ReleaseFrame、Close](img/adec-call-sequence-send-end-of-stream.jpg)

​    【注意】

- 调用此接口可以把音频编解码库的缓冲区设置为\_SD_BM_ENDING，即只要缓冲区有数据都会解码，所以最后解码出来的帧长度有可能不够一个帧长的长度。
- AK_MPI_ADEC_SendEndofStream函数的调用需要跟AK_MPI_ADEC_SendStream函数在同一个线程进行调用。

## 缓存状态获取

### AK_MPI_ADEC_GetBufStatus

&emsp;&emsp;【描述】

&emsp;&emsp;获取解码器输入buffer的剩余大小以及其总大小

&emsp;&emsp;【语法】

```c
AK_S32 AK_MPI_ADEC_GetBufStatus(AK_S32 s32AdecUserId, DEC_BUF_STATUS_S *pstBufStatus);
```

&emsp;&emsp;【参数】

| 参数名称          | 描述          | 取值范围                  | 输入/输出 |
| ------------- | ----------- | --------------------- | ----- |
| s32AdecUserId | 音频解码模块句柄    | [0,3]                 | 输入    |
| pstBufStatus  | 保存buffer的数据 | 参考DEC_BUF_STATUS_S结构体 | 输入    |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码】

| **错误码**                  | **描述**         |
| ------------------------ | -------------- |
| ERROR_ADEC_USER_NULL     | user handle 为空 |
| ERROR_ADEC_ATC_LIB_ERROR | 获取解码库功能失败      |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_adec.a/so、libakaudiocodec.a/so  或者libakaac.a/so libakamr.a/so libakmp3.a/so

&emsp;&emsp;头文件：ak_adec.h

## 调试接口

### AK_MPI_ADEC_SaveFile

&emsp;&emsp;【描述】

&emsp;&emsp;保存ADEC模块内部音频处理的过程文件。保存的文件分为四类：一类是传给ADEC模块的音频，一类是保存送给解码库前的音频，一类是保存解码后的PCM音频，还有一类是ADEC模块处理后输出的PCM音频。

&emsp;&emsp;【语法】

```c
AK_S32 AK_MPI_ADEC_SaveFile(AK_S32 s32AdecUserId, AUDIO_SAVE_FILE_INFO_S *pstSaveFileInfo);
```

&emsp;&emsp;【参数】

| 参数名称            | 描述       | 取值范围                        | 输入/输出 |
| --------------- | -------- | --------------------------- | ----- |
| s32AdecUserId   | 音频解码模块句柄 | [0,3]                       | 输入    |
| pstSaveFileInfo | 保存文件的信息  | 参考AUDIO_SAVE_FILE_INFO_S结构体 | 输入    |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码】

| **错误码**                 | **描述**         |
| ----------------------- | -------------- |
| ERROR_ADEC_USER_NULL    | user handle 为空 |
| ERROR_TYPE_POINTER_NULL | 参数指针为空         |
| ERROR_TYPE_INVALID_ARG  | 参数不正确          |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_adec.a/so、libakaudiocodec.a/so  或者libakaac.a/so libakamr.a/so libakmp3.a/so

&emsp;&emsp;头文件：ak_adec.h

&emsp;&emsp;【接口调用顺序】

![ADEC接口调用顺序：Open、SaveFile、Close](img/adec-call-sequence-save-file.jpg)

​        【注意】

​    当需要保存adec处理过程的音频来查找问题的时候，可以调用这个接口。

## 设置解码属性接口

### AK_MPI_ADEC_SetOutputPcmLen

&emsp;&emsp;【描述】

&emsp;&emsp;设置解码后输出数据的长度。out_pcm_len的取值范围如下：

&emsp;【语法】

```C
AK_S32 AK_MPI_ADEC_SetOutputPcmLen(AK_S32 s32AdecUserId, AK_U32 u32OutPcmLen);
```

&emsp;&emsp;【参数】

| 参数名称          | 描述                  | 取值范围        | 输入/输出 |
| ------------- | ------------------- | ----------- | ----- |
| s32AdecUserId | 音频解码模块句柄id          | [0,3]       | 输入    |
| u32OutPcmLen  | 设置输出时解码的数据长度，单位byte | [320, 4096] | 输入    |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码】

| 错误码                     | 描述             |
| ----------------------- | -------------- |
| ERROR_TYPE_POINTER_NULL | 参数指针为空         |
| ERROR_TYPE_INVALID_ARG  | 参数非法           |
| ERROR_ADEC_USER_NULL    | user handle 为空 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_adec.a/so、libakaudiocodec.a/so  或者libakaac.a/so libakamr.a/so libakmp3.a/so

&emsp;&emsp;头文件：ak_adec.h

&emsp;&emsp;【接口调用顺序】

![ADEC接口调用顺序：Open、SetOutputPcmLen、SendStream、GetFrame、ReleaseFrame、Close](img/adec-call-sequence-set-output-pcm-len.jpg)

​    【注意】

​    不调用此接口默认每次输出的解码数据长度是默认值。

<br/>

## 缓存区清理

### AK_MPI_ADEC_ClearDecodeBuf

&emsp;&emsp;【描述】

&emsp;&emsp;清除解码区的缓存。解码暂停之后，需要清除解码缓存区的数据，否则下一次播放时会留有上一次解码的数据。

&emsp;&emsp;【语法】

```C
AK_S32 AK_MPI_ADEC_ClearDecodeBuf(AK_S32 s32AdecUserId);
```

&emsp;&emsp;【参数】

| 参数名称          | 描述         | 取值范围  | 输入/输出 |
| ------------- | ---------- | ----- | ----- |
| s32AdecUserId | 音频解码模块句柄id | [0,3] | 输入    |

&emsp;&emsp;【返回值】

| **返回值** | **描述**     |
| ------- | ---------- |
| 0       | 成功         |
| 非0      | 失败，返回值为错误码 |

&emsp;&emsp;【错误码】

| **错误码**                  | **描述**          |
| ------------------------ | --------------- |
| ERROR_TYPE_POINTER_NULL  | 参数指针为空          |
| ERROR_ADEC_ATC_LIB_ERROR | 解码库设置错误         |
| ERROR_ADEC_RB_ERROR      | Ring buffer操作出错 |
| ERROR_ADEC_USER_NULL     | user handle 为空  |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_adec.a/so、libakaudiocodec.a/so  或者libakaac.a/so libakamr.a/so libakmp3.a/so

&emsp;&emsp;头文件：ak_adec.h

&emsp;&emsp;【接口调用顺序】

![ADEC接口调用顺序：Open、SendStream、GetFrame、ReleaseFrame、ClearDecodeBuf、Close](img/adec-call-sequence-clear-decode-buf.jpg)

​        【注意】

<br/>

## 接口调用依赖关系

&emsp;&emsp;ADEC模块对外提供的接口函数在调用时存在一定的依赖关系，如下表所示：

| **接口**                       | **接口依赖关系**                      |
| ---------------------------- | ------------------------------- |
| AK_MPI_ADEC_GetVersion       | 无依赖                             |
| AK_MPI_ADEC_Open             | -                               |
| AK_MPI_ADEC_SetOutputPcmLen  | AK_MPI_ADEC_Opem之后可以调用          |
| AK_MPI_ADEC_SendStream       | AK_MPI_ADEC_Opem之后可以调用          |
| AK_MPI_ADEC_GetFrame         | AK_MPI_ADEC_Opem之后可以调用          |
| AK_MPI_ADEC_ReleaseFrame     | AK_MPI_ADEC_GetFrame之后调用        |
| AK_MPI_ADEC_SendEndofStream  | AK_MPI_ADEC_SendStream之后调用，立即生效 |
| AK_MPI_ADEC_ClearDecodeBuf   | AK_MPI_ADEC_SendStream之后调用，立即生效 |
| AK_MPI_ADEC_Close            | AK_MPI_ADEC_Opem之后随时可以调用，立即生效   |
| AK_MPI_ADEC_SaveFile         | AK_MPI_ADEC_Opem之后随时可以调用，立即生效   |
| AK_MPI_ADEC_GetBufStatus     | AK_MPI_ADEC_Opem之后随时可以调用，立即生效   |
| AK_MPI_ADEC_RegisterDecoder  | AK_MPI_ADEC_Opem之前可以调用          |
| AK_MPI_AENC_SetLibPrintLevel | 无依赖，建议在AK_MPI_ADEC_Opem之前调用     |
| <br/>                        |                                 |

## ak_adec_sample使用示例

### sample命令和参数

运行此sample前，需要先insmod ak_pcm.ko，一般开启都会默认加载。

| 输入参数（短参） | 输入参数（长参）       | 输入参数说明                                    |
| -------- | -------------- | ----------------------------------------- |
| h        | help           | 打印帮助信息。                                   |
| s        | sample-rate    | 采样率，支持8000Hz、16000Hz、 44100Hz、48000Hz采样率。 |
| d        | dev-sel        | 选择播放设备，0：DAC，1：I2S0。                      |
| p        | play-file      | 解码播放的文件名称                                 |
| f        | config-file    | config 文件的绝对路径和名称                         |
| t        | config-section | 选取的section字符串                             |
| e        | decode-type    | 解码类型[mp3 aac amr g711a g711u pcm]         |

### sample存储和文件命令

（1）sample输入的文件格式默认使用MP3格式。
（2）sample输入的文件默认播放/mnt/adec_test.mp3

### 应用案例

 ak_adec_sample -s 16000 -d 0 -e mp3 -p /mnt/xxx.mp3 -f /etc/config/audio_config.ini -t def_far

## /var/platform说明

/var/platform目录用于查看当前模块的配置参数和状态信息，下面是该模块的/var/platform/的参数说明。

### param

| 参数         | 说明      |
| ---------- | ------- |
| OutPcmLen  | 解码输出的长度 |
| SampleRate | 采样率     |
| SoundMode  | 声道模式    |
| SampleBit  | 采样精度    |
| UserCnt    | 用户数     |
| AdecType   | 解码类型    |

### stat

| 参数                | 说明       |
| ----------------- | -------- |
| Mp3Version        | MP3库版本号  |
| AudioCodecVersion | 编解码库版本号  |
| AdecMpiVersion    | 平台解码库版本号 |

<br/>

## 错误码说明

| 错误代码       | 宏定义                             | 含义           |
| ---------- | ------------------------------- | ------------ |
| 0x10000000 | ERROR_ADEC_OPEN_LIB_ERROR       | 打开库失败        |
| 0x10000001 | ERROR_ADEC_CLOSE_LIB_ERROR      | 关闭库失败        |
| 0x10000002 | ERROR_ADEC_OPEN_TOO_MANY        | 打开太多句柄       |
| 0x10000003 | ERROR_ADEC_USER_NULL            | 用户为空         |
| 0x10000004 | ERROR_ADEC_RB_ERROR             | RB错误         |
| 0x10000005 | ERROR_ADEC_ATC_LIB_ERROR        | 算法库错误        |
| 0x10000006 | ERROR_ADEC_SEND_STREAM_ERROR    | 发送stream错误   |
| 0x10000007 | ERROR_ADEC_GET_FRAME_NO_DATA    | 获取帧没有数据      |
| 0x10000008 | ERROR_ADEC_SEND_STREAM_NO_SPACE | 发送stream没有空间 |
| 0x10000009 | ERROR_ADEC_STREAM_END           | stream 结束    |
| 0x1000000a | ERROR_ADEC_SEND_STREAM_NO_START | 发送stream没有开启 |

<br/>
