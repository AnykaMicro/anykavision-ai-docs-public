# 解析

## 概述

&emsp;&emsp;解析模块（DEMUX）主要负责从视频文件中分别提取音频和视频流或把纯音频文件解析成以帧为单位的音频流。

<br/>

## API 参考

&emsp;&emsp;本模块提供以下API参考，如下表所示。

| **数据结构**       | **描述**                   |
| -------------------------- | -------------------------------- |
| DEMUX_CONF_S | 媒体解析库的输入参数             |
| DEMUX_DATA_SOURCE_E | 媒体解析库的类型                 |
| DEMUX_VIDEO_INFO_S | 媒体库解析后得到的视频信息       |
| DEMUX_AUDIO_INFO_S | 媒体库解析后得到的音频信息 |
| DEMUX_DATA_TYPE_E | 媒体库解析得到的数据流类型       |
| DEMUX_STREAM_S | 媒体库解析得到的数据流属性       |
| DEMUX_DIRECTION_E | 解析时从跳转位置找I帧的方向      |

<br/>

| **函数接口**       | **描述**                   |
| -------------------------- | -------------------------------- |
| AK_MPI_DEMUX_Get_Version       | 获取demux模块的版本号            |
| AK_MPI_DEMUX_Open              | 打开媒体解析库                   |
| AK_MPI_DEMUX_Close             | 关闭媒体解析库                   |
| AK_MPI_DEMUX_Get_Total_Time    | 获取要解析的文件的总时长，单位ms |
| AK_MPI_DEMUX_Get_Video_Info | 获取要解析文件的视频信息         |
| AK_MPI_DEMUX_Get_Audio_Info    | 获取要解析文件的音频信息         |
| AK_MPI_DEMUX_Get_Data          | 获取解析后的数据                 |
| AK_MPI_DEMUX_Get_Video         | 获取解析后的视频数据             |
| AK_MPI_DEMUX_Get_Audio         | 获取解析后的音频数据             |
| AK_MPI_DEMUX_Free_Data         | 释放获取到的数据                 |
| AK_MPI_DEMUX_Seek_To_Keyframe  | 跳转到指定位置进行解析           |
<br/>

## 数据结构

### DEMUX_CONF_S

&emsp;&emsp;【说明】

&emsp;&emsp;媒体解析库的输入参数。

&emsp;&emsp;【定义】

```c
    typedef struct akDEMUX_CONF_S
    {
        AK_VOID *pvFromDIR;// file_fd or socket
        DEMUX_DATA_SOURCE_E enDemuxDataSource;
        AK_U64 u64StartMs;
    }DEMUX_CONF_S;
```

&emsp;&emsp;【成员】

| **成员名称** | **描述**                                               |
| ------------------ | ------------------------------------------------------------ |
| pvFromDIR           | 可以传入文件通过fopen后得到的文件句柄，也能够传入socket的指针 |
| enDemuxDataSource        | 用户指定文件的源是本地文件还是网络的流                       |
| u64StartMs           | 指定demux从哪个时间点开始，时间是ms <br/>如果ms=0：表示从文件开头进行解析；<br/>ms>0:表示从文件的ms处开始解析。 |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_DEMUX_Open(const DEMUX_CONF_S *pstDemuxConf, AK_S32 *s32DemuxHandleId);
```

<br/>

### DEMUX_DATA_SOURCE_E

&emsp;&emsp;【说明】

&emsp;&emsp;媒体解析库的类型，解析的数据来源仅仅支持DEMUX_DATA_FROM_LOCAL_FILE本地文件模式。

&emsp;&emsp;【定义】

```c
    typedef enum akDEMUX_DATA_SOURCE_E
    {
        DEMUX_DATA_FROM_UNKNOWN = 0x00,
        DEMUX_DATA_FROM_LOCAL_FILE,
        DEMUX_DATA_FROM_INTERNET
    }DEMUX_DATA_SOURCE_E;
```

&emsp;&emsp;【成员】

| **成员名称**         | **描述**           |
| -------------------------- | ------------------------ |
| DEMUX_DATA_FROM_UNKNOWN    | 缺省值                   |
| DEMUX_DATA_FROM_LOCAL_FILE | 解析的数据来源是本地文件 |
| DEMUX_DATA_FROM_INTERNET   | 解析的数据来源是网络     |

&emsp;&emsp;【相关结构体】

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

&emsp;&emsp;【说明】

&emsp;&emsp;媒体库解析后得到的视频信息。

&emsp;&emsp;【定义】

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

&emsp;&emsp;【成员】

| **成员名称** | **描述**                        |
| ------------------ | ------------------------------------- |
| u32Fps                | 视频帧率                              |
| enVencOutputType         | 视频类型，参考enum encode_output_penDemuxDataType |
| u16Width              | 视频的宽                              |
| u16Height             | 视频的高                              |
| dFps | 浮点数值表示的帧率 |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_DEMUX_Free_Data(AK_S32 s32DemuxHandleId,
DEMUX_VIDEO_INFO_S *pstDemuxVideoInfo);
```

<br/>

### DEMUX_AUDIO_INFO_S

&emsp;&emsp;【说明】

&emsp;&emsp;媒体库解析后得到的音频信息。

&emsp;&emsp;【定义】

```c
    typedef struct akDEMUX_AUDIO_INFO_S
    {
        AUDIO_DATA_ATTR_S stAudioDataAttr;
        AUDIO_TYPE_E enAudioType; //encode | decode audio penDemuxDataType
    }DEMUX_AUDIO_INFO_S;
```

&emsp;&emsp;【成员】

| **成员名称** | **描述**                                |
| ------------------ | --------------------------------------------- |
| stAudioDataAttr    | 音频数据的属性，参考AUDIO_DATA_ATTR_S |
| enAudioType         | 音频类型，参考AUDIO_TYPE_E              |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_DEMUX_Get_Audio_Info(AK_S32 s32DemuxHandleId,
                                       DEMUX_AUDIO_INFO_S *pstDemuxAudioInfo);
```

<br/>

### DEMUX_DATA_TYPE_E

&emsp;&emsp;【说明】

&emsp;&emsp;媒体库解析得到的数据流类型。

&emsp;&emsp;【定义】

```c
    typedef enum akDEMUX_DATA_TYPE_E
    {
        DEMUX_DATA_UNKNOW = 0x00,
        DEMUX_DATA_VIDEO,
        DEMUX_DATA_AUDIO
    }DEMUX_DATA_TYPE_E;
```

&emsp;&emsp;【成员】

| **成员名称** | **描述**           |
| ------------------ | ------------------------ |
| DEMUX_DATA_UNKNOW  | 缺省值                   |
| DEMUX_DATA_VIDEO   | 解析出来的数据是视频数据 |
| DEMUX_DATA_AUDIO   | 解析出来的数据是音频数据 |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_DEMUX_Get_Data(AK_S32 s32DemuxHandleId, DEMUX_DATA_TYPE_E *penDemuxDataType,
                                 DEMUX_STREAM_S *pstDemuxStream);
```

<br/>

### DEMUX_STREAM_S

&emsp;&emsp;【说明】

&emsp;&emsp;媒体库解析得到的数据流属性。视频流和音频流都使用此结构图，不同之处在于，当获取到的数据为视频流时，结构体里的成员frame_penDemuxDataType才有意义，如果获取的数据是音频流，frame_penDemuxDataType无意义。

&emsp;&emsp;【定义】

```c
    typedef struct akDEMUX_STREAM_S
    {
        AK_U8 *pu8Data;    // demux pstDemuxStream data
        AK_U32 u32Len;         // demux pstDemuxStream len in bytes
        AK_U64 u64Ts;    // demux timestamp(u64Ms)
        VIDEO_FRAME_TYPE_E enVideoFrameType;    // demux I or P frame
    }DEMUX_STREAM_S;
```

&emsp;&emsp;【成员】

| **成员名称** | **描述**                                               |
| ------------------ | ------------------------------------------------------------ |
| pu8Data               | 解析出来的数据地址                                           |
| u32Len                | 解析出来的数据长度                                           |
| u64Ts                 | 解析出来的数据的时间戳                                       |
| enVideoFrameType         | 视频帧是I帧还是P帧，参考enum video_frame_penDemuxDataType，这个成员只有在解析出来的流是视频流的情况下才有意义 |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_DEMUX_Get_Data(AK_S32 s32DemuxHandleId, DEMUX_DATA_TYPE_E *penDemuxDataType,
                             DEMUX_STREAM_S *pstDemuxStream);

    AK_S32 AK_MPI_DEMUX_Get_Video(AK_S32 s32DemuxHandleId, DEMUX_STREAM_S *pstDemuxStream);

    AK_S32 AK_MPI_DEMUX_Get_Audio(AK_S32 s32DemuxHandleId, DEMUX_STREAM_S *pstDemuxStream);

    AK_S32 AK_MPI_DEMUX_Free_Data(AK_S32 s32DemuxHandleId, DEMUX_STREAM_S *pstDemuxStream);
```

<br/>

### DEMUX_DIRECTION_E

&emsp;&emsp;【说明】

&emsp;&emsp;解析时从跳转位置找I帧的方向。因为在跳转解析的时候，必须要从I帧进行解析，此枚举指找I帧的方向。

&emsp;&emsp;【定义】

```c
    typedef enum akDEMUX_DIRECTION_E
    {
        DEMUX_DIRECTION_NEAREST = 0,    //seek to nearest key frame
        DEMUX_DIRECTION_LAST,            //seek to last key frame
        DEMUX_DIRECTION_NEXT            //seek to next key frame
    }DEMUX_DIRECTION_E;
```

&emsp;&emsp;【成员】

| **成员名称**      | **描述**            |
| ----------------------- | ------------------------- |
| DEMUX_DIRECTION_NEAREST | 解析库自己找距离最近的I帧 |
| DEMUX_DIRECTION_LAST    | 跳转到上一个I帧           |
| DEMUX_DIRECTION_NEXT    | 跳转到下一个I帧           |

&emsp;&emsp;【相关函数接口】

```c
    AK_S32 AK_MPI_DEMUX_Seek_To_Keyframe(AK_S32 s32DemuxHandleId, AK_U64 u64Ms,
                                        DEMUX_DIRECTION_E enDemuxDirection);
```

<br/>

## 版本信息获取

### AK_MPI_DEMUX_Get_Version

&emsp;&emsp;【描述】

&emsp;&emsp;获取DEMUX模块的版本号。

&emsp;&emsp;【语法】

```c
    const AK_S8* AK_MPI_DEMUX_Get_Version(AK_VOID);
```

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 解析模块版本号   | 成功           |
| NULL             | 失败           |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_demux.so、libakmedia.so或者libmpi_demux.a、libakmedia.a

&emsp;&emsp;头文件：ak_demux.h

&emsp;&emsp;【接口调用顺序】

&emsp;&emsp;任何位置都可调用。

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

<br/>

## 打开/关闭模块

### AK_MPI_DEMUX_Open

&emsp;&emsp;【描述】

&emsp;&emsp;打开媒体解析库。在打开视频文件时可以选择跳到某一个时间点开始解析，具体使用的参数为struct ak_demux_input中的start_ms。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_DEMUX_Open(const DEMUX_CONF_S *pstDemuxConf, AK_S32 *s32DemuxHandleId);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**            | **取值范围**        | **输入/输出** |
| ------------------ | ------------------------- | ------------------------- | ------------------- |
| pstDemuxConf        | 解析库输入参数            | 参考struct akDEMUX_CONF_S | 输入                  |
| s32DemuxHandleId    | 媒体解析库open的handle ID | 0~3                       | 输出                 |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0                | 成功           |
| 其他             | 请参考错误码   |

&emsp;&emsp;【错误码】

| **错误码**               | **描述**         |
| ------------------------------ | ---------------------- |
| ERROR_TYPE_INVALID_ARG         | 参数不合法             |
| ERROR_TYPE_MALLOC_FAILED       | Malloc 失败            |
| ERROR_TYPE_POINTER_NULL        | 参数为空               |
| ERROR_DEMUX_OPEN_LIB_ERROR     | 打开解析库失败         |
| ERROR_DEMUX_GET_LIB_INFO_ERROR | 获取录像信息失败       |
| ERROR_DEMUX_START_LIB_ERROR    | 解析开始失败           |
| ERROR_DEMUX_OPEN_TOO_MANY      | 打开解析模块的用户太多 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_demux.so、libakmedia.so或者libmpi_demux.a、libakmedia.a

&emsp;&emsp;头文件：ak_demux.h

&emsp;&emsp;【接口调用顺序】

```c
    AK_MPI_DEMUX_Open(&demux_param, &s32DemuxHandleId);
    while(1){
	  AK_MPI_DEMUX_Get_Data(s32DemuxHandleId, &penDemuxDataType, &stream);
	  //Do something
	  AK_MPI_DEMUX_Free_Data(s32DemuxHandleId, &stream);
    }
    AK_MPI_DEMUX_Close(s32DemuxHandleId);
```

&emsp;&emsp;【接口配对关系】

&emsp;&emsp;AK_MPI_DEMUX_Open与AK_MPI_DEMUX_Close配对使用。

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

> **注意：**调用AK_MPI_DEMUX_Open可以open多次，每次open相当于增加一个新的用户，但是最多支持打开4个用户。

<br/>

### AK_MPI_DEMUX_Close

&emsp;&emsp;【描述】

&emsp;&emsp;关闭媒体解析库。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_DEMUX_Close(AK_S32 s32DemuxHandleId);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**            | **取值范围** | **输入/输出** |
| ------------------ | ------------------------- | ------------------ | ------------------- |
| s32DemuxHandleId    | 媒体解析库open的handle ID | 0~3                | 输入                |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0                | 成功           |
| 其他             | 请参考错误码   |

&emsp;&emsp;【错误码】

| **错误码**            | **描述** |
| --------------------------- | -------------- |
| ERROR_DEMUX_CLOSE_LIB_ERROR | 关闭解析库失败 |
| ERROR_DEMUX_STOP_LIB_ERROR  | 解析停止失败   |
| ERROR_DEMUX_USER_NULL       | 用户句柄为空   |
| ERROR_DEMUX_LIB_HANDLE_NULL | 解析库句柄为空 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_demux.so、libakmedia.so或者libmpi_demux.a、libakmedia.a

&emsp;&emsp;头文件：ak_demux.h

&emsp;&emsp;【接口调用顺序】

```c
    AK_MPI_DEMUX_Open(&demux_param, &s32DemuxHandleId);
    while(1){
	  AK_MPI_DEMUX_Get_Data(s32DemuxHandleId, &penDemuxDataType, &stream);
	  //Do something
	  AK_MPI_DEMUX_Free_Data(s32DemuxHandleId, &stream);
    }
    AK_MPI_DEMUX_Close(s32DemuxHandleId);
```

&emsp;&emsp;【接口配对关系】

&emsp;&emsp;AK_MPI_DEMUX_Open与AK_MPI_DEMUX_Close配对使用。

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

> **注意：**调用AK_MPI_DEMUX_Close可以多次关闭。关闭不存在时s32DemuxHandleId会报错。

<br/>

## 解析操作接口

### AK_MPI_DEMUX_Get_Total_Time

&emsp;&emsp;【描述】

&emsp;&emsp;获取要解析的文件的总时长，单位ms。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_DEMUX_Get_Total_Time(AK_S32 s32DemuxHandleId, AK_U64 *u64TotalTimeMs);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**               | **取值范围** | **输入/输出** |
| ------------------ | ---------------------------- | ------------------ | ------------------- |
| s32DemuxHandleId    | 媒体解析库open的handle ID    | 0~3                | 输入                  |
| u64TotalTimeMs      | 要解析的文件的总时长，单位ms | 非空               | 输出                 |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0                | 成功           |
| 其他             | 请参考错误码   |

&emsp;&emsp;【错误码】

| **错误码**        | **描述** |
| ----------------------- | -------------- |
| ERROR_TYPE_POINTER_NULL | 参数为空       |
| ERROR_DEMUX_USER_NULL   | 用户句柄为空   |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_demux.so、libakmedia.so或者libmpi_demux.a、libakmedia.a

&emsp;&emsp;头文件：ak_demux.h

&emsp;&emsp;【接口调用顺序】

```c
    AK_MPI_DEMUX_Open(&demux_param, &s32DemuxHandleId);
    AK_S32 AK_MPI_DEMUX_Get_Total_Time(AK_S32 s32DemuxHandleId, AK_U64 *u64TotalTimeMs);
    AK_MPI_DEMUX_Close(s32DemuxHandleId);
```

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

<br/>

### AK_MPI_DEMUX_Get_Video_Info

&emsp;&emsp;【描述】

&emsp;&emsp;获取要解析文件的视频信息。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_DEMUX_Get_Video_Info(AK_S32 s32DemuxHandleId, DEMUX_VIDEO_INFO_S *pstDemuxVideoInfo);

```

&emsp;&emsp;【参数】

| **参数名称** | **描述**            | **取值范围**                    | **输入/输出** |
| ------------------ | ------------------------- | ------------------------------------- | ------------------- |
| s32DemuxHandleId    | 媒体解析库open的handle ID | 0~3                                   | 输入                  |
| pstDemuxVideoInfo   | 要解析的文件的视频信息    | 参考struct akDEMUX_VIDEO_INFO_S 结构体 | 输出                 |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0                | 成功           |
| 其他             | 请参考错误码   |

&emsp;&emsp;【错误码】

| **错误码**             | **描述** |
| ---------------------------- | -------------- |
| ERROR_TYPE_POINTER_NULL      | 参数为空       |
| ERROR_DEMUX_USER_NULL        | 用户句柄为空   |
| ERROR_DEMUX_VIDEO_TYPE_ERROR | 视频类型错误   |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_demux.so、libakmedia.so或者libmpi_demux.a、libakmedia.a

&emsp;&emsp;头文件：ak_demux.h

&emsp;&emsp;【接口调用顺序】

```c
    AK_MPI_DEMUX_Open(&demux_param, &s32DemuxHandleId);
    AK_MPI_DEMUX_Free_Data(s32DemuxHandleId, &pstDemuxVideoInfo);
    AK_MPI_DEMUX_Close(s32DemuxHandleId);
```

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

<br/>

### AK_MPI_DEMUX_Get_Audio_Info

&emsp;&emsp;【描述】

&emsp;&emsp;获取要解析文件的音频信息。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_DEMUX_Get_Audio_Info(AK_S32 s32DemuxHandleId, DEMUX_AUDIO_INFO_S *pstDemuxAudioInfo);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**            | **取值范围**                    | **输入/输出** |
| ------------------ | ------------------------- | ------------------------------------- | ------------------- |
| s32DemuxHandleId    | 媒体解析库open的handle ID | 0~3                                   | 输入                  |
| pstDemuxAudioInfo   | 要解析的文件的音频信息    | 参考struct akDEMUX_AUDIO_INFO_S 结构体 | 输出                 |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0                | 成功           |
| 其他             | 请参考错误码   |

&emsp;&emsp;【错误码】

| **错误码**             | **描述** |
| ---------------------------- | -------------- |
| ERROR_TYPE_POINTER_NULL      | 参数为空       |
| ERROR_DEMUX_USER_NULL        | 用户句柄为空   |
| ERROR_DEMUX_LIB_HANDLE_NULL  | 解析库句柄为空 |
| ERROR_DEMUX_AUDIO_TYPE_ERROR | 音频类型错误   |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_demux.so、libakmedia.so或者libmpi_demux.a、libakmedia.a

&emsp;&emsp;头文件：ak_demux.h

&emsp;&emsp;【接口调用顺序】

```c
    AK_MPI_DEMUX_Open(&demux_param, &s32DemuxHandleId);
    AK_MPI_DEMUX_Get_Audio_Info(s32DemuxHandleId, &pstDemuxAudioInfo);
    AK_MPI_DEMUX_Close(s32DemuxHandleId);
```

&emsp;&emsp;【接口重入性】

&emsp;&emsp;函数可重入。

<br/>

### AK_MPI_DEMUX_Get_Data

&emsp;&emsp;【描述】

&emsp;&emsp;获取解析后的数据。如果输出的penDemuxDataType是视频类型，那表示获取到这一帧数据是视频的数据，如果输出的penDemuxDataType是音频类型，表示获取到这一帧数据是音频的数据。

&emsp;&emsp;此接口内部是有策略的，内部会保存上一帧音频ts和上一帧视频的ts，如果上一帧音频ts>上一帧视频ts，会先获取视频的ts，反之，如果上一帧视频ts>上一帧音频ts，就会先获取音频ts。

&emsp;&emsp;策略流程图如图 3-1所示：

![图 3-1 策略流程图](img/demux-av-sync-strategy.png)

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_DEMUX_Get_Data(AK_S32 s32DemuxHandleId, DEMUX_DATA_TYPE_E *penDemuxDataType, DEMUX_STREAM_S *pstDemuxStream);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**            | **取值范围**          | **输入/输出** |
| ------------------ | ------------------------- | --------------------------- | ------------------- |
| s32DemuxHandleId    | 媒体解析库open的handle ID | 0~3                         | 输入                  |
| penDemuxDataType               | 解析后获取到的数据类型    | 参考enum akDEMUX_DATA_TYPE_E | 输出                 |
| pstDemuxStream       | 解析后的数据              | 参考struct akDEMUX_STREAM_S  | 输出                 |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0                | 成功           |
| 其他             | 请参考错误码   |

&emsp;&emsp;【错误码】

| **错误码**            | **描述** |
| --------------------------- | -------------- |
| ERROR_TYPE_POINTER_NULL     | 参数为空       |
| ERROR_TYPE_MALLOC_FAILED    | Malloc 失败    |
| ERROR_DEMUX_USER_NULL       | 用户句柄为空   |
| ERROR_DEMUX_LIB_HANDLE_NULL | 解析库句柄为空 |
| ERROR_DEMUX_AUDIO_END       | 解析音频结束   |
| ERROR_DEMUX_VIDEO_END       | 解析视频结束   |
| ERROR_DEMUX_LIB_ERROR       | 解析出错       |
| ERROR_DEMUX_NO_AUDIO        | 没有音频数据   |
| ERROR_DEMUX_NO_VIDEO        | 没有视频数据   |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_demux.so、libakmedia.so或者libmpi_demux.a、libakmedia.a

&emsp;&emsp;头文件：ak_demux.h

&emsp;&emsp;【接口调用顺序】

```c
    AK_MPI_DEMUX_Open(&demux_param, &s32DemuxHandleId);
    while(1){
	  AK_MPI_DEMUX_Get_Data(s32DemuxHandleId, &penDemuxDataType, &stream);
	  //Do something
	  AK_MPI_DEMUX_Free_Data(s32DemuxHandleId, &stream);
    }
    AK_MPI_DEMUX_Close(s32DemuxHandleId);
```

&emsp;&emsp;【接口配对关系】

&emsp;&emsp;AK_MPI_DEMUX_Get_Data与AK_MPI_DEMUX_Free_Data配对使用。

&emsp;&emsp;【接口重入性】

&emsp;&emsp;接口可重入。

<br/>

### AK_MPI_DEMUX_Free_Data

&emsp;&emsp;【描述】

&emsp;&emsp;获取解析后的视频数据。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_DEMUX_Free_Data(AK_S32 s32DemuxHandleId, DEMUX_STREAM_S *pstDemuxStream);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**            | **取值范围**         | **输入/输出** |
| ------------------ | ------------------------- | -------------------------- | ------------------- |
| s32DemuxHandleId    | 媒体解析库open的handle ID | 0~3                        | 输入                  |
| pstDemuxStream       | 解析后视频的数据          | 参考struct akDEMUX_STREAM_S | 输出                 |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0                | 成功           |
| 其他             | 请参考错误码   |

&emsp;&emsp;【错误码】

| **错误码**            | **描述** |
| --------------------------- | -------------- |
| ERROR_TYPE_POINTER_NULL     | 参数为空       |
| ERROR_TYPE_MALLOC_FAILED    | Malloc 失败    |
| ERROR_DEMUX_USER_NULL       | 用户句柄为空   |
| ERROR_DEMUX_LIB_HANDLE_NULL | 解析库句柄为空 |
| ERROR_DEMUX_VIDEO_END       | 解析视频结束   |
| ERROR_DEMUX_LIB_ERROR       | 解析出错       |
| ERROR_DEMUX_NO_VIDEO        | 没有视频数据   |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_demux.so、libakmedia.so或者libmpi_demux.a、libakmedia.a

&emsp;&emsp;头文件：ak_demux.h

&emsp;&emsp;【接口调用顺序】

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

&emsp;&emsp;【接口配对关系】

&emsp;&emsp;AK_MPI_DEMUX_Get_Data与AK_MPI_DEMUX_Free_Data配对使用。

&emsp;&emsp;【接口重入性】

&emsp;&emsp;接口可重入。

<br/>

### AK_MPI_DEMUX_Get_Audio

&emsp;&emsp;【描述】

&emsp;&emsp;获取解析后的音频数据。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_DEMUX_Get_Audio(AK_S32 s32DemuxHandleId, DEMUX_STREAM_S *pstDemuxStream);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**            | **取值范围**         | **输入/输出** |
| ------------------ | ------------------------- | -------------------------- | ------------------- |
| s32DemuxHandleId    | 媒体解析库open的handle ID | 0~3                        | 输入                |
| pstDemuxStream       | 解析后的音频数据          | 参考struct akDEMUX_STREAM_S | 输出                 |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0                | 成功           |
| 其他             | 请参考错误码   |

&emsp;&emsp;【错误码】

| **错误码**            | **描述** |
| --------------------------- | -------------- |
| ERROR_TYPE_POINTER_NULL     | 参数为空       |
| ERROR_TYPE_MALLOC_FAILED    | Malloc 失败    |
| ERROR_DEMUX_USER_NULL       | 用户句柄为空   |
| ERROR_DEMUX_LIB_HANDLE_NULL | 解析库句柄为空 |
| ERROR_DEMUX_AUDIO_END       | 解析音频结束   |
| ERROR_DEMUX_LIB_ERROR       | 解析出错       |
| ERROR_DEMUX_NO_AUDIO        | 没有音频数据   |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_demux.so、libakmedia.so或者libmpi_demux.a、libakmedia.a

&emsp;&emsp;头文件：ak_demux.h

&emsp;&emsp;【接口调用顺序】

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

&emsp;&emsp;【接口配对关系】

&emsp;&emsp;AK_MPI_DEMUX_Get_Audio与AK_MPI_DEMUX_Free_Data配对使用。

&emsp;&emsp;【接口重入性】

&emsp;&emsp;接口可重入。

<br/>

### AK_MPI_DEMUX_Free_Data

&emsp;&emsp;【描述】

&emsp;&emsp;释放获取到的数据。此接口与AK_MPI_DEMUX_Get_Data、AK_MPI_DEMUX_Get_Video、AK_MPI_DEMUX_Get_Audio这三个接口配合使用。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_DEMUX_Free_Data(AK_S32 s32DemuxHandleId, DEMUX_STREAM_S *pstDemuxStream);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**            | **取值范围**         | **输入/输出** |
| ------------------ | ------------------------- | -------------------------- | ------------------- |
| s32DemuxHandleId    | 媒体解析库open的handle ID | 0~3                        | 输入                |
| pstDemuxStream             | 解析后的数据              | 参考struct akDEMUX_STREAM_S | 输入                |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0                | 成功           |
| 其他             | 请参考错误码   |

&emsp;&emsp;【错误码】

| **错误码**            | **描述** |
| --------------------------- | -------------- |
| ERROR_TYPE_POINTER_NULL     | 参数为空       |
| ERROR_DEMUX_USER_NULL       | 用户句柄为空   |
| ERROR_DEMUX_LIB_HANDLE_NULL | 解析库句柄为空 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_demux.so、libakmedia.so或者libmpi_demux.a、libakmedia.a

&emsp;&emsp;头文件：ak_demux.h

&emsp;&emsp;【接口调用顺序】

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

&emsp;&emsp;【接口配对关系】

&emsp;&emsp;AK_MPI_DEMUX_Get_Data与AK_MPI_DEMUX_Free_Data配对使用。

&emsp;&emsp;或ak_demux_get_video与AK_MPI_DEMUX_Free_Data配对使用。

&emsp;&emsp;或AK_MPI_DEMUX_Get_Audio与AK_MPI_DEMUX_Free_Data配对使用。

&emsp;&emsp;【接口重入性】

&emsp;&emsp;接口可重入。

<br/>

### AK_MPI_DEMUX_Seek_To_Keyframe

&emsp;&emsp;【描述】

&emsp;&emsp;跳转到指定位置进行解析。由于跳转之后开始解析的位置必须是I帧的位置，所以不仅要定义跳转完成的时间，还需告知解析库找I帧的方向。

&emsp;&emsp;【语法】

```c
    AK_S32 AK_MPI_DEMUX_Seek_To_Keyframe(AK_S32 s32DemuxHandleId, AK_U64 u64Ms,
                                        DEMUX_DIRECTION_E enDemuxDirection);
```

&emsp;&emsp;【参数】

| **参数名称** | **描述**                                               | **取值范围**          | **输入/输出** |
| ------------------ | ------------------------------------------------------------ | --------------------------- | ------------------- |
| s32DemuxHandleId    | 媒体解析库open的handle ID                                    | 0~3                         | 输入                |
| u64Ms                 | 指定demux从现在的时间戳跳转到多少时间间隔的时间戳去。单位ms  | >0                          | 输入                |
| enDemuxDirection             | 跳转的方向，方向分为向前跳转和向后跳转，与ms参数结合，即向前跳转ms的时间或者向后跳转到ms的时间开始解析 | 参考enum DEMUX_DIRECTION_E | 输入                |

&emsp;&emsp;【返回值】

| **返回值** | **描述** |
| ---------------- | -------------- |
| 0                | 成功           |
| 其他             | 请参考错误码   |

&emsp;&emsp;【错误码】

| **错误码**            | **描述** |
| --------------------------- | -------------- |
| ERROR_TYPE_INVALID_ARG      | 参数不合法     |
| ERROR_TYPE_MALLOC_FAILED    | Malloc 失败    |
| ERROR_TYPE_POINTER_NULL     | 参数为空       |
| ERROR_DEMUX_USER_NULL       | 用户句柄为空   |
| ERROR_DEMUX_LIB_HANDLE_NULL | 解析库句柄为空 |
| ERROR_DEMUX_LIB_ERROR       | 解析出错       |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_demux.so、libakmedia.so或者libmpi_demux.a、libakmedia.a

&emsp;&emsp;头文件：ak_demux.h

&emsp;&emsp;【接口调用顺序】

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

&emsp;&emsp;【接口重入性】

&emsp;&emsp;接口可重入。

<br/>

## 接口调用依赖关系

&emsp;&emsp;DEMUX模块对外提供的接口函数在调用时存在一定的依赖关系，如下表所示：

| **接口**            | **接口依赖关系**                                       |
| ------------------------- | ------------------------------------------------------------ |
| AK_MPI_DEMUX_Get_Version      | 无依赖                                                       |
| AK_MPI_DEMUX_Open             | 开始时调用                                                   |
| AK_MPI_DEMUX_Get_Total_Time   | AK_MPI_DEMUX_Open之后调用                                        |
| AK_MPI_DEMUX_Free_Data   | AK_MPI_DEMUX_Open之后调用                          |
| AK_MPI_DEMUX_Get_Audio_Info   | AK_MPI_DEMUX_Open之后调用                          |
| AK_MPI_DEMUX_Seek_To_Keyframe | AK_MPI_DEMUX_Open之后调用                          |
| AK_MPI_DEMUX_Get_Data         | AK_MPI_DEMUX_Open之后调用                                        |
| AK_MPI_DEMUX_Get_Video        | AK_MPI_DEMUX_Open之后调用                                        |
| AK_MPI_DEMUX_Get_Audio        | AK_MPI_DEMUX_Open之后调用                                        |
| AK_MPI_DEMUX_Free_Data        | AK_MPI_DEMUX_Get_Data之后调用；或者ak_demux_get_video之后调用；或者AK_MPI_DEMUX_Get_Audio之后调用； |
| AK_MPI_DEMUX_Close            | AK_MPI_DEMUX_Open之后调用                                          |

<br/>

## ak_demux_sample使用示例

| **输入参数**   | **输入参数说明**                                             |
| -------------- | ----------------------------------------------------------- |
| path           | 解析出来的音频文件、视频文件保存路径                           |
| file           | 需要解析的文件全路径                                          |
| skip-serial    | 视频解码文件用于媒体播放器播放时,写入文件时需要跳过序列号和时间戳 |
| offset-ms    | 读文件时候的偏移值(ms) |

<br/>

## 错误码说明

| 错误代码   | 宏定义                         | 含义             |
| ---------- | ------------------------------ | ---------------- |
| 0x13000000 | DEMUX_ERROR_OPEN_LIB_ERROR     | 打开库失败       |
| 0x13000001 | DEMUX_ERROR_CLOSE_LIB_ERROR    | 关闭库失败       |
| 0x13000002 | DEMUX_ERROR_GET_LIB_INFO_ERROR | 获取库信息失败   |
| 0x13000003 | DEMUX_ERROR_START_LIB_ERROR    | 开启库失败       |
| 0x13000004 | DEMUX_ERROR_STOP_LIB_ERROR     | 停止库失败       |
| 0x13000005 | DEMUX_ERROR_OPEN_TOO_MANY      | 打开次数太多     |
| 0x13000006 | DEMUX_ERROR_USER_NULL          | 用户为空         |
| 0x13000007 | DEMUX_ERROR_LIB_HANDLE_NULL    | 库句柄为空       |
| 0x13000008 | DEMUX_ERROR_AUDIO_TYPE_ERROR   | 音频类型错误     |
| 0x13000009 | DEMUX_ERROR_VIDEO_TYPE_ERROR   | 视频类型错误     |
| 0x1300000a | DEMUX_ERROR_AUDIO_END          | 解析音频结束     |
| 0x1300000b | DEMUX_ERROR_VIDEO_END          | 解析视频结束     |
| 0x1300000c | DEMUX_ERROR_LIB_ERROR          | 解析出错         |
| 0x1300000d | DEMUX_ERROR_NO_AUDIO           | 没有音频数据     |
| 0x1300000e | DEMUX_ERROR_NO_VIDEO           | 没有视频数据     |
| 0x1300000f | DEMUX_ERROR_SRC_EOF            | 解析源文件已结束 |

<br/>
