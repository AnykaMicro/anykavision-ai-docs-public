# AI拍摄眼镜通信协议

## 1 协议概述

AI拍摄眼镜采用三层通信架构：手机APP、AK1090系列芯片和KM02G系列芯片。AK1090系列芯片在此架构中承担通信桥梁的角色，通过透传机制实现手机APP与KM02G系列芯片之间的无缝命令交互。本文档将阐述这三者之间的通信协议。

说明：

1. 命令列表中的'\\'表示该命令不携带参数，'×'表示该命令无需接收响应；

2. 命令列表中部分命令采用<span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">黄色底纹</span>标识，表明该命令已完成定义但仍在开发中；

3. 手机APP与KM02G系列芯片之间的命令支持灵活配置，包括增加、删除和修改操作。当AK1090系列芯片无需特殊处理时，可直接复用现有AK1090系列芯片代码，无需重新开发；

4. KM02G系列芯片接收到任意命令（以命令A为例）时，遵循以下处理流程：

<!-- end list -->

> 4.1 首先返回IND\_ACK命令，确认已成功接收到命令A；
> 4.2 执行命令A；
> 4.3 命令A执行完成后，通过IND\_COMP命令返回执行结果。

如图1所示。其中，IND\_COMP命令的返回格式根据执行结果而定：

- 若执行结果无需附加参数，则IND\_COMP仅返回cmd\_id和result两个参数；

- 若执行结果需要附加参数，则在cmd\_id和result参数后追加相应的IND\_COMP附加参数，且一并返回。

详细格式定义请参考IND\_COMP命令说明。

<div align="center">

![APP/AK1090系列芯片与KM02G系列芯片命令交互通用流程图](img/protocol-chart-1.svg)

图1 APP/AK1090系列芯片与KM02G系列芯片命令交互通用流程图

</div>

## 2 APP与AK1090系列芯片通信协议

### 2.1 通信格式

| 字段  | 包头标志  | 命令码      | 数据长度     | 数据内容               | 校验和      |
| --- | ----- | -------- | -------- | ------------------ | -------- |
| 长度  | 1byte | 1byte    | 2bytes   | N bytes (N\<= 504) | 4bytes   |
| 说明  | ‘@’   | 详见下方命令列表 | 数据内容size | 数据内容               | CRC32位校验（当前未启用，详见5.4） |

### 2.2 命令列表

> APP(简称A)和AK1090系列芯片(简称B)的所有通信命令如下所示。

#### 2.2.1 APP发起的命令列表

| 命令码       | 命令说明                                | 请求参数（A =&gt; B）                                                                                                                                                    | 响应参数（A &lt;= B）                          |
| --------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------- |
| 0x01~0x7E | 保留为特殊命令使用                           | \                                                                                                                                                                  | \                                        |
| 0x7F      | AP配网                                | uint8_t function; //用于指示AP配网所作用的场景 char[] ssid;//保存ssid信息，以\0结尾 char[] password;//保存密码，以\0结尾 function值定义如下： 0x00：绑定设备 0x01：图库管理 0x02：视频直播 0x03：RTSP调图 0x04：RTSP调录像 | \                                        |
| 0x80~0xF2 | 客户使用                                | \                                                                                                                                                                  | \                                        |
| 0xF5      | 用户配置，含：U盘等模式配置、录像相关配置等              | uint8_t mode;//默认配置0x01 uint16_t duration;//录像定时时长，单位秒，默认60。 mode值定义如下： 0x01：U盘模式 0x02：UVC拍照调试 0x03：UVC录像调试                                                        | uint8_t result; 0x00：成功 0x01：失败          |
| <span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">0xF6</span>      | 工厂产测模式                              | \                                                                                                                                                                  | uint8_t result; 0x00：成功 0x01：失败          |
| 0xF7      | 恢复出厂模式                              | \                                                                                                                                                                  | uint8_t result; 0x00：成功 0x01：失败          |
| 0xF8      | 设置本地时间（含时区和时间）                      | int16_t minutes;//时区偏移分钟数 (如: -480表示UTC-8) uint32_t tick;//时间戳，从1970年1月1日00:00:00 UTC开始计算的秒数，可解析为RTC时间。                                                            | uint8_t result; 0x00：成功 0x01：失败          |
| 0xF9      | AK1090系列芯片OTA升级                             | \                                                                                                                                                                  | ×                                        |
| 0xFA      | 获取AK1090系列芯片固件版本号                           | \                                                                                                                                                                  | char[] version;//以\0结尾。                  |
| 0xFB      | 设备解绑                                | \                                                                                                                                                                  | uint8_t result; 0x00：成功 0x01：失败          |
| 0xFC      | 获取设备信息                              | \                                                                                                                                                                  | uint8_t battery; //电量百分比                 |
| 0xFD      | 强制KM02G系列芯片掉电                           | \                                                                                                                                                                  | uint8_t result; 0x00：成功 0x01：失败          |
| 0xFE      | 给KM02G系列芯片上电                            | \                                                                                                                                                                  | uint8_t result; 0x00：成功（上电ready） 0x01：失败 |
| 0xFF      | 透传命令。AK1090系列芯片需将APP给KM02G系列芯片的命令封装进来，并透传给KM02G系列芯片 | APP需发给KM02G系列芯片的命令                                                                                                                                                     | ×                                        |

#### 2.2.2 AK1090系列芯片发起的命令列表

| 命令码  | 命令说明                              | 请求参数（B =&gt; A）                                                                                          | 响应参数（B &lt;= A）                                          |
| ---- | --------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| 0xF3 | 请求允许掉电KM02G系列芯片                       | \                                                                                                        | uint8_t result; 0x00：APP允许AK1090系列芯片掉电KM02G系列芯片 0x01：APP不允许AK1090系列芯片掉电KM02G系列芯片 |
| 0xF4 | 设备状态指示                            | uint8_t status; 0x01：设备低电 0x02：未通知KM02G系列芯片上电 0x03: KM02G系列芯片进入U盘或UVC模式 0x04：KM02G系列芯片正在运行其他功能 0x05：低电，请求APP给KM02G系列芯片掉电 | ×                                                        |
| 0xFF | 透传命令。AK1090系列芯片需将KM02G系列芯片给APP的命令封装进来，并透传给APP | KM02G系列芯片需发给APP的命令                                                                                           | ×                                                        |

**说明：**

1. 如需增加命令，建议从0xF2开始往前加；
2. 透传命令0xFF的发起者可以是APP，也可以是AK1090系列芯片；
3. 对于需要响应的命令，必须使用接收到的相同命令码进行响应。例如：APP向AK1090系列芯片发送0xFE命令，AK1090系列芯片执行完此命令后，需使用0xFE命令码将执行结果返回给APP；
4. 本节的0xF6（工厂产测模式）是APP与AK1090系列芯片之间的命令，与4.2.1中APP发给KM02G系列芯片的0xF6（对应0x76启动录像，SDK中为 `APP_CMD_RECORD`）不是同一条命令。SDK中定义的工厂产测命令为0xF3（`APP_CMD_FACTORY`）和0x73（`BT_CMD_FACTORY`），Linux应用目前未处理。

## 3 AK1090系列芯片与KM02G系列芯片通信协议

### 3.1 通信格式

协议格式：

<table border="1" style="border-collapse: collapse; font-family: monospace; text-align: center;">
  <tr>
    <th>Section</th>
    <th>Byte</th>
    <th>0</th>
    <th>1</th>
    <th>2</th>
    <th>3</th>
  </tr>
  <tr>
    <td rowspan="2">Head</td>
    <td>0x00</td>
    <td>SyncHead</td>
    <td>Command</td>
    <td colspan="2">ParamLen</td>
  </tr>
  <tr>
    <td>0x04</td>
    <!-- 合并的单元格 -->
    <td colspan="4">Crc</td>
  </tr>
  <tr>
    <td>Parameter</td>
    <td>0x08</td>
    <td colspan="4">Payload data</td>
  </tr>
  <tr>
    <td>Parameter</td>
    <td>0x0C</td>
    <td colspan="4">Payload data</td>
  </tr>
  <tr>
    <td>Parameter</td>
    <td>...    </td>
    <td colspan="4">...    </td>
  </tr>
</table>

格式说明：

- SyncHead：同步头，长度为1个字节，内容固定为0xAA
- Command：命令字或指示字，长度为1个字节。详见下方命令列表
- ParamLen：参数长度，长度为2个字节，内容为0则表示不带参数
- Crc：校验位，校验payload的内容（当前未启用，可填 `0x00000000`，详见5.4）
- Parameter：参数内容，长度为0-255字节（SDK 中 `quick_glass_info_t` 的参数缓冲区为255字节，Linux应用发送超过255字节的参数时直接报错返回）

### 3.2 命令列表

AK1090系列芯片(简称B)和KM02G系列芯片(简称K)的所有通信命令如下所示。

> 注意：AK1090系列芯片与KM02G系列芯片的命令不能大于0x7F。

#### 3.2.1 AK1090系列芯片发起的命令列表

| Command   | 命令说明           | 请求参数（B =&gt; K）                                                                                                                                                                                                                         | 响应参数（B &lt;= K）                                                                                   |
| --------- | -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| 0x01      | 请求KM02G系列芯片掉电      | \                                                                                                                                                                                                                                       | IND_COMP附加参数如下： uint16_t timeout;//给KM02G系列芯片断电的超时时间，单位：秒，默认0（即马上掉电）。在超时时间到达时，才给KM02G系列芯片掉电。              |
| 0x02      | 设置本地时间（含时区和时间） | int16_t minutes; //时区偏移分钟数 (如: -480表示UTC-8) uint16_t year;//年(如:2023) uint8_t month;//月(1-12) uint8_t day;//日(1-31) uint8_t hour;//时(0-23) uint8_t min;//分(0-59) uint8_t sec;// 秒 (0-59)                                                | \                                                                                                 |
| 0x03      | 插入USB时的相关模式定义  | uint8_t mode;//USB模式配置，只在接电脑时生效。默认配置0x01 0x01：U盘模式 0x02：UVC拍照调试 0x03：UVC录像调试                                                                                                                                                            | IND_COMP附加参数如下： uint8_t mode;//当前生效的模式 0x00：充电模式（USB接充电器） 0x01：U盘模式 0x02：UVC拍照调试 0x03：UVC录像调试     |
| 0x04      | 保留特殊命令使用       | \                                                                                                                                                                                                                                       | \                                                                                                 |
| <span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">0x05 </span>     | 设备解绑           | \                                                                                                                                                                                                                                       | \                                                                                                 |
| <span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">0x06</span>      | 获取KM02G系列芯片固件版本号   | \                                                                                                                                                                                                                                       | IND_COMP附加参数如下： char[] version;//以\0结尾。                                                           |
| <span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">0x07 </span>     | 获取图片、视频数量和音频数量 | \                                                                                                                                                                                                                                       | IND_COMP附加参数如下： uint16_t photo_count;//图片数量uint16_t video_count;//视频数量uint16_t audio_count;//音频数量 |
| 0x08      | AP配网           | uint8_t function; //用于指示AP配网所作用的场景 char[] ssid;//保存ssid信息，以\0结尾 char[] password;//保存密码，以\0结尾 function值定义如下： 0x00：绑定设备 0x01：图库管理 0x02：视频直播 0x03：RTSP调图 0x04：RTSP调录像                                                                      | \                                                                                                 |
| <span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">0x09 </span>     | AP断连           | \                                                                                                                                                                                                                                       | \                                                                                                 |
| <span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">0x0A </span>     | P2P配网          | uint8_t function; //用于指示P2P配网所作用的场景 char p2p_dev_name[];//以\0结尾 function值定义如下： 0x00：绑定设备 0x01：图库管理 0x02：视频直播 0x03：RTSP调图 0x04：RTSP调录像。SDK中0x8A只区分0x01（图库管理）和0x02（视频直播），其他值（含0x03、0x04）均按0x00（绑定设备）处理（见4.2.1） | \                                                                                                 |
| <span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">0x0B </span>     | P2P断连          | \                                                                                                                                                                                                                                       | \                                                                                                 |
| <span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">0x0C </span>     | KM02G系列芯片 OTA升级    | \                                                                                                                                                                                                                                       | \                                                                                                 |
| 0x0D      | 恢复出厂模式         | \                                                                                                                                                                                                                                       | \                                                                                                 |
| <span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">0x0E </span>     | 获取存储状态         | \                                                                                                                                                                                                                                       | IND_COMP附加参数如下： uint32_t total;//SD NAND总空间，单位KB uint32_t used;//SD NAND已用空间，单位KB                 |
| <span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">0x0F </span>     | 获取存储中某个目录的文件数量 | \                                                                                                                                                                                                                                       | IND_COMP附加参数如下： uint16_t count;//文件数量                                                             |
| 0x10~0x1F | 保留为特殊命令使用      | \                                                                                                                                                                                                                                       | \                                                                                                 |
| 0x20~0x4F | 客户使用           | \                                                                                                                                                                                                                                       | \                                                                                                 |
| 0x50~0x72 | 保留为特殊命令使用      | \                                                                                                                                                                                                                                       | \                                                                                                 |
| <span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">0x73</span>      | 工厂产测模式         | \                                                                                                                                                                                                                                       | \                                                                                                 |
| 0x74      | 拍照             | int16_t minutes; //时区偏移分钟数 (如: -480表示UTC-8) uint16_t year;//年(如:2023) uint8_t month;//月(1-12) uint8_t day;//日(1-31) uint8_t hour;//时(0-23) uint8_t min;//分(0-59) uint8_t sec;// 秒 (0-59)                                                | \                                                                                                 |
| 0x75      | 抓拍             | \                                                                                                                                                                                                                                       | \                                                                                                 |
| 0x76      | 启动录像           | int32_t duration;//录像时长，单位秒。大于0时按该值录像，SDK不设上限；小于或等于0时按600秒录像。时间到会自动停止录像。 int16_t minutes; //时区偏移分钟数 (如: -480表示UTC-8) uint16_t year;//年(如:2023) uint8_t month;//月(1-12) uint8_t day;//日(1-31) uint8_t hour;//时(0-23) uint8_t min;//分(0-59) uint8_t sec;// 秒 (0-59) | \                                                                                                 |
| 0x77      | 停止录像           | \                                                                                                                                                                                                                                       | \                                                                                                 |
| <span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">0x78</span>      | 启动录音           | int32_t duration;//录音时长，单位秒 int32_t min_duration;//最短录音时长，单位秒。SDK只取这两个值的低8位（按uint8_t处理，即0-255秒）。时间到会自动停止录音。                                                                                                                                                                                          | \                                                                                                 |
| <span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">0x79</span>      | 停止录音           | \                                                                                                                                                                                                                                       | \                                                                                                 |
| 0x7A      | 对接收的数据包进行反馈    | 针对IND_UPLOAD_HEAD和IND_UPLOAD_PACK进行回复。如下： uint8_t result; 0x00：数据接收成功 0x01：数据接收失败                                                                                                                                                       | ×                                                                                                 |

````{only} anyka_review
```{admonition} TODO
:class: warning

SDK 定义了 AK1090 系列芯片命令 0x01–0x03 和 0x73–0x7F（`BT_CMD_*`、`BT_IND_*`），其中 Linux 应用处理 0x01–0x03、0x74、0x76 和 0x77；0x78、0x79 只有开启 `SOUND_REC_SUPPORT_ENABLE`（默认关闭）时才处理。0x04–0x0F 在 SDK 中没有定义。SDK 把这些功能定义为 APP 命令：0x85–0x8D 与 0x05–0x0D 的命令说明对应，其中 0x86、0x88、0x8A–0x8D 已实现，0x85、0x87、0x89 已定义但未实现；存储状态和目录文件数量是 APP 命令 0x82 和 0x83（见 4.2.1）。待安凯确认 AK1090 系列芯片和 RTT 如何转发 0x04–0x0F。

The SDK defines AK1090 commands 0x01–0x03 and 0x73–0x7F (`BT_CMD_*`, `BT_IND_*`); its Linux app handles 0x01–0x03, 0x74, 0x76 and 0x77, and 0x78 and 0x79 only when `SOUND_REC_SUPPORT_ENABLE` is on (off by default). 0x04–0x0F are not defined in the SDK. The SDK defines these functions as APP commands instead: 0x85–0x8D correspond to 0x05–0x0D; 0x86, 0x88 and 0x8A–0x8D are implemented, and 0x85, 0x87 and 0x89 are defined but not implemented. Storage status and directory file count are APP commands 0x82 and 0x83 (see 4.2.1). Anyka to confirm how the AK1090 and RTT forward 0x04–0x0F.
```
````

#### 3.2.2 KM02G系列芯片发起的命令列表

| Command | 命令说明                             | 请求参数（K =&gt; B）                                                                                                                        | 响应参数（K &lt;= B） |
| ------- | -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| 0x7B    | IND_READY命令，用于指示KM02G系列芯片已上电就绪       | 由linux应用发起。无参数                                                                                                                         | ×               |
| 0x7C    | IND_ACK命令，用于确认指示                 | 由小系统发起。参数如下：uint8_t result; 0x00：命令接收成功 0x01：命令接收失败                                                                                    | ×               |
| 0x7D    | IND_UPLOAD_HEAD命令，用于上传数据头信息及首包数据 | 由小系统发起。参数是每包的分包数据。详见IND_UPLOAD_PACK格式定义IND_UPLOAD_HEAD格式定义                                                                             | ×               |
| 0x7E    | IND_UPLOAD_PACK命令，用于上传分包数据       | 由小系统发起。参数是每包的分包数据。详见IND_UPLOAD_PACK格式定义                                                                                                | ×               |
| 0x7F    | IND_COMP命令，用于返回命令执行结果            | 由linux应用或小系统发起。参数如下： uint8_t cmd_id;//由KM02G系列芯片收到的Command值进行回填 uint8_t result;//命令执行结果，详见KM02G系列芯片错误码定义 //根据具体命令的执行结果，若存在附加参数，则将相应的附加参数附加至此处。 | ×               |

举例：

1. AK1090系列芯片向KM02G系列芯片发送0x74命令（拍照）后，KM02G系列芯片最终会返回的IND\_COMP命令码流为：0xAA 0x7F 0x0002 0x00000000 0x74 0x00。

2. AK1090系列芯片向KM02G系列芯片发送0x01命令（请求KM02G系列芯片掉电）后，如果KM02G系列芯片要求马上掉电（0秒，即0x0000），KM02G系列芯片最终会返回的IND\_COMP命令码流为：0xAA 0x7F 0x0004 0x00000000 0x01 0x00 0x0000。

3. AK1090系列芯片向KM02G系列芯片发送0x01命令（请求KM02G系列芯片掉电）后，如果KM02G系列芯片要求10秒（0x000A）后才掉电，那么返回的IND\_COMP命令码流为：0xAA 0x7F 0x0004 0x00000000 0x01 0x00 0x000A。

## 4 APP与KM02G系列芯片通信协议

### 4.1 通信格式

APP与KM02G系列芯片之间采用间接通信方式，所有命令交互均需通过AK1090系列芯片进行透传。透传流程如图2所示。

- APP向KM02G系列芯片发送命令（以命令B为例）的透传流程如下：

<!-- end list -->

1. APP将命令B封装至透传命令0xFF的“数据内容”字段中；

2. APP将封装后的0xFF命令发送至AK1090系列芯片；

3. AK1090系列芯片接收到0xFF命令后，提取其中的命令B并转发给KM02G系列芯片。

<!-- end list -->

- KM02G系列芯片向APP发送命令（以命令C为例）的透传流程如下：

<!-- end list -->

1. KM02G系列芯片将命令C发送至AK1090系列芯片；

2. AK1090系列芯片接收到命令C后，根据"KM02G系列芯片命令路由原则"，确定该命令需转发至APP，将其封装至透传命令0xFF的“数据内容”字段中；

3. AK1090系列芯片将封装后的0xFF命令发送给APP。

<div align="center">

![命令透传流程图](img/protocol-chart-2.svg)

图2 命令透传流程图

</div>

> 注意：APP与KM02G系列芯片之间的命令不能小于0x80。

### 4.2 命令列表

APP(简称A)和KM02G系列芯片(简称K)的所有通信命令如下所示。

#### 4.2.1 APP发起的命令列表

<table border="1" style="border-collapse: collapse; font-family: monospace; text-align: center;">
  <tr>
    <th>Command</th>
    <th>命令说明</th>
    <th>请求参数（A => K）</th>
    <th>响应参数（A <= K）</th>
  </tr>
  <tr>
    <td>0x81 </td>
    <td colspan="3">详见AK1090系列芯片和KM02G系列芯片的通信命令0x01</td>
  </tr>
  <tr>
    <td>0x82 </td>
    <td>获取存储状态</td>
    <td>\</td>
    <td>uint16_t used; //已用空间，单位MB<br>uint16_t left; //剩余空间，单位MB</td>
  </tr>
  <tr>
    <td>0x83 </td>
    <td>获取存储中某个目录的文件数量</td>
    <td>uint8_t type; //0：全部 1：视频 2：图片 3：音频<br>（type 为 4 时返回文件数量 0；大于 4 时不返回响应）</td>
    <td>int16_t file_count_type; //同请求的 type<br>int16_t file_count; //文件数量</td>
  </tr>
  <tr>
    <td><span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">0x84</span> </td>
    <td colspan="3">导图（SDK 中已定义为 APP_CMD_IMPORT，暂未实现）</td>
  </tr>
  <tr>
    <td><span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">0x85</span> </td>
    <td colspan="3">详见AK1090系列芯片和KM02G系列芯片的通信命令0x05</td>
  </tr>
  <tr>
    <td>0x86 </td>
    <td colspan="3">详见AK1090系列芯片和KM02G系列芯片的通信命令0x06</td>
  </tr>
  <tr>
    <td><span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">0x87</span> </td>
    <td colspan="3">详见AK1090系列芯片和KM02G系列芯片的通信命令0x07</td>
  </tr>
  <tr>
    <td>0x88 </td>
    <td>AP配网</td>
    <td>uint8_t ap_ssid[64]; //以\0结尾<br>uint8_t ap_password[64]; //以\0结尾<br>（不含 function 字节）</td>
    <td>同AK1090系列芯片和KM02G系列芯片的通信命令0x08</td>
  </tr>
  <tr>
    <td><span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">0x89</span> </td>
    <td colspan="3">详见AK1090系列芯片和KM02G系列芯片的通信命令0x09</td>
  </tr>
  <tr>
    <td>0x8A </td>
    <td>P2P配网</td>
    <td>uint8_t state; //0x00：绑定设备 0x01：图库导入 0x02：视频直播，其他值按绑定设备处理<br>char p2p_dev_name[]; //P2P 设备名，长度为参数长度减 1（最多 63 字节）<br>（参数长度为 24 字节时按旧格式处理：只有设备名，按视频直播执行）</td>
    <td>state 为 0x01 时不返回响应；其他情况返回执行结果</td>
  </tr>
  <tr>
    <td>0x8B </td>
    <td colspan="3">详见AK1090系列芯片和KM02G系列芯片的通信命令0x0B</td>
  </tr>
  <tr>
    <td>0x8C </td>
    <td>KM02G系列芯片 OTA升级</td>
    <td>uint8_t ota_file_path[128]; //升级包路径，须位于 /mnt/ 下，只能包含字母、数字和 . _ - /</td>
    <td>路径不合法时返回 0x01，升级包不存在时返回 0x06；检查通过后直接开始升级，不返回响应</td>
  </tr>
  <tr>
    <td>0x8D </td>
    <td colspan="3">详见AK1090系列芯片和KM02G系列芯片的通信命令0x0D</td>
  </tr>
  <tr>
    <td><span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">0x8E</span> </td>
    <td colspan="3">启动 RTSP（SDK 中已定义为 APP_CMD_START_RTSP，暂未实现）</td>
  </tr>
  <tr>
    <td>0x8F </td>
    <td colspan="3">保留（SDK 中未定义）</td>
  </tr>
  <tr>
    <td>0x90~0x9F</td>
    <td colspan="3">保留为特殊命令使用</td>
  </tr>
  <tr>
    <td>0xA0~0xCF</td>
    <td colspan="3">客户使用</td>
  </tr>
  <tr>
    <td>0xD0~0xF2</td>
    <td colspan="3">保留为特殊命令使用</td>
  </tr>
  <tr>
    <td><span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">0xF3</span> </td>
    <td colspan="3">详见AK1090系列芯片和KM02G系列芯片的通信命令0x73</td>
  </tr>
  <tr>
    <td>0xF4 </td>
    <td colspan="3">详见AK1090系列芯片和KM02G系列芯片的通信命令0x74</td>
  </tr>
  <tr>
    <td><span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">0xF5</span> </td>
    <td colspan="3">详见AK1090系列芯片和KM02G系列芯片的通信命令0x75</td>
  </tr>
  <tr>
    <td>0xF6 </td>
    <td colspan="3">详见AK1090系列芯片和KM02G系列芯片的通信命令0x76</td>
  </tr>
  <tr>
    <td>0xF7 </td>
    <td colspan="3">详见AK1090系列芯片和KM02G系列芯片的通信命令0x77</td>
  </tr>
  <tr>
    <td><span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">0xF8</span> </td>
    <td colspan="3">详见AK1090系列芯片和KM02G系列芯片的通信命令0x78</td>
  </tr>
  <tr>
    <td><span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">0xF9</span> </td>
    <td colspan="3">详见AK1090系列芯片和KM02G系列芯片的通信命令0x79</td>
  </tr>
  <tr>
    <td>0xFA </td>
    <td colspan="3">详见AK1090系列芯片和KM02G系列芯片的通信命令0x7A</td>
  </tr>
</table>

#### 4.2.2 KM02G系列芯片发起的命令列表

<table border="1" style="border-collapse: collapse; font-family: monospace; text-align: center;">
  <tr>
    <th>Command</th>
    <th>命令说明</th>
    <th>请求参数（K => A）</th>
    <th>响应参数（K <= A）</th>
  </tr>
  <tr>
    <td>0xFB </td>
    <td colspan="3">详见AK1090系列芯片和KM02G系列芯片的通信命令0x7B</td>
  </tr>
  <tr>
    <td>0xFC </td>
    <td colspan="3">详见AK1090系列芯片和KM02G系列芯片的通信命令0x7C</td>
  </tr>
  <tr>
    <td><span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">0xFD</span> </td>
    <td colspan="3">详见AK1090系列芯片和KM02G系列芯片的通信命令0x7D</td>
  </tr>
  <tr>
    <td><span style="background-color: #fff3b0; color: #1a1a1a; padding: 0 3px; border-radius: 2px;">0xFE</span> </td>
    <td colspan="3">详见AK1090系列芯片和KM02G系列芯片的通信命令0x7E</td>
  </tr>
  <tr>
    <td>0xFF </td>
    <td colspan="3">详见AK1090系列芯片和KM02G系列芯片的通信命令0x7F</td>
  </tr>
</table>

## 5 其他

### 5.1 KM02G系列芯片错误码定义

<table border="1" style="border-collapse: collapse; font-family: monospace; text-align: center;">
  <tr>
    <th>错误码</th>
    <th>说明</th>
  </tr>
  <tr>
    <td>0x00</td>
    <td>成功</td>
  </tr>
  <tr>
    <td>0x01</td>
    <td>参数无效</td>
  </tr>
  <tr>
    <td>0x02</td>
    <td>参数设置失败</td>
  </tr>
  <tr>
    <td>0x03</td>
    <td>录像时间过短</td>
  </tr>
  <tr>
    <td>0x04</td>
    <td>录像时间过长</td>
  </tr>
  <tr>
    <td>0x05</td>
    <td>写文件失败</td>
  </tr>
  <tr>
    <td>0x06</td>
    <td>读文件失败</td>
  </tr>
  <tr>
    <td>0x07</td>
    <td>创建文件失败</td>
  </tr>
  <tr>
    <td>0x08</td>
    <td>内存分配失败</td>
  </tr>
  <tr>
    <td>0x09</td>
    <td>设备忙</td>
  </tr>
  <tr>
    <td>0x0A</td>
    <td>超时</td>
  </tr>
  <tr>
    <td>0x0B</td>
    <td>SD nand未挂载</td>
  </tr>
  <tr>
    <td>0x0C</td>
    <td>WiFi节点失败</td>
  </tr>
  <tr>
    <td>0x0D</td>
    <td>卸载SD nand 失败</td>
  </tr>
  <tr>
    <td>0x0E</td>
    <td>设备未运行</td>
  </tr>
  <tr>
    <td>0x0F</td>
    <td>设备空间不足</td>
  </tr>
  <tr>
    <td>0x10</td>
    <td>创建失败</td>
  </tr>
  <tr>
    <td>0x11</td>
    <td>格式化失败</td>
  </tr>
  <tr>
    <td>0x12</td>
    <td>卡内无文件</td>
  </tr>
  <tr>
    <td>0xFF</td>
    <td>未知错误</td>
  </tr>
</table>

### 5.2 IND\_UPLOAD\_HEAD格式定义

<table border="1" style="border-collapse: collapse; font-family: monospace; text-align: center;">
  <tr>
    <th>Section</th>
    <th>Type</th>
    <th>Size</th>
    <th>Description</th>
    <th>Demo</th>
  </tr>
  <tr>
    <td>file_id</td>
    <td>uint32_t</td>
    <td>4</td>
    <td>文件唯一 ID，由发起者分配</td>
    <td>1</td>
  </tr>
  <tr>
    <td>name</td>
    <td>char[]</td>
    <td>64</td>
    <td>原文件名（含扩展名）</td>
    <td>“video.mp4”</td>
  </tr>
  <tr>
    <td>size</td>
    <td>uint32_t</td>
    <td>4</td>
    <td>文件总大小（字节）</td>
    <td>104857600</td>
  </tr>
  <tr>
    <td>chunk_index</td>
    <td>uint32_t</td>
    <td>4</td>
    <td>当前分片序号（从 0 开始）</td>
    <td>1</td>
  </tr>
  <tr>
    <td>chunk_count</td>
    <td>uint32_t</td>
    <td>4</td>
    <td>总分片数</td>
    <td>50</td>
  </tr>
  <tr>
    <td>payload</td>
    <td>char[]</td>
    <td>N</td>
    <td>分片的每包数据内容</td>
    <td></td>
  </tr>
</table>

### 5.3 IND\_UPLOAD\_PACK格式定义

<table border="1" style="border-collapse: collapse; font-family: monospace; text-align: center;">
  <tr>
    <th>Section</th>
    <th>Type</th>
    <th>Size</th>
    <th>Description</th>
    <th>Demo</th>
  </tr>
  <tr>
    <td>file_id</td>
    <td>uint32_t</td>
    <td>4</td>
    <td>文件唯一 ID，由发起者分配</td>
    <td>1</td>
  </tr>
  <tr>
    <td>chunk_index</td>
    <td>uint32_t</td>
    <td>4</td>
    <td>当前分片序号（从 0 开始）</td>
    <td>1</td>
  </tr>
  <tr>
    <td>payload</td>
    <td>char[]</td>
    <td>N</td>
    <td>分片的每包数据内容</td>
    <td></td>
  </tr>
</table>

### 5.4 补充说明

- KM02G系列芯片命令路由原则：AK1090系列芯片在接收KM02G系列芯片命令时，需检测Command字段的最高位bit7以确定命令路由：

<!-- end list -->

  > 最高位为0：表示该命令由AK1090系列芯片自身处理；

  > 最高位为1：表示该命令需转发至APP，此时AK1090系列芯片应通过透传命令0xFF将命令转发给APP。

<!-- end list -->

- 由于KM02G系列芯片在上电时无法识别具体的上电发起方（发起方可为APP或AK1090系列芯片），因此当APP作为上电发起方时，AK1090系列芯片需要将IND\_READY命令转发至APP，以通知APP KM02G系列芯片已完成上电初始化。

- IND\_UPLOAD\_HEAD和IND\_UPLOAD\_PACK命令采用可靠传输机制，每发送一个数据包后，必须等待对端返回数据接收成功的确认反馈，方可发送下一个数据包；

- 目前手机APP、AK1090系列芯片和KM02G系列芯片对接收的命令均未实施CRC校验机制。

- 本文档所列命令均为安凯微使用，客户可自定义的命令也有在列表中注明。汇总如下：

<!-- end list -->

  > APP与AK1090系列芯片之间，客户可自定义的命令为0x80\~0xF2，共115条；

  > AK1090系列芯片与KM02G系列芯片之间，客户可自定义的命令为0x20\~0x4F，共48条；

  > APP与KM02G系列芯片之间，客户可自定义的命令为0xA0\~0xCF，共48条。
