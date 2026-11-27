# 智能视觉处理

## 概述

智能视觉处理模块（SVP）支持人形、人脸检测。

用户自己通过VI模块接口去获取一帧数据(RGB_HWC格式)，或者从文件读出一帧数据，再将该种类型的数据送给SVP模块提供的接口经过神经网络流程的运算，最终输出检测目标的坐标。

<br/>

##  API参考

&emsp;&emsp;本模块提供以下API参考，如下表所示。

| **库接口 **                | **描述 **             |
| ----------------------- | ------------------- |
| SVP_ENV_MODE_E          | svp运行环境模式           |
| SVP_TARGET_TYPE_E       | svp检测目标类型           |
| SVP_MODEL_E             | 神经网络模型选择            |
| SVP_HD_PARAM_S          | 人形检测阈值              |
| SVP_FAS_PARAM_S         | 活体检测阈值              |
| SVP_FR_PARAM_S          | 人脸识别阈值              |
| SVP_GESTURE_RE_PARAM_S  | 手势分类阈值              |
| SVP_AI_ISP_PARAM_S      | AI ISP保留参数          |
| SVP_MODEL_PARAM_S       | SVP模型阈值             |
| SVP_MODEL_ATTR_S        | SVP模型属性             |
| SVP_CHN_ATTR_S          | SVP通道属性             |
| pfnSvpCusReadFunc       | 读取模型回调函数            |
| SVP_IMG_TYPE_E          | 检测输入图形数据类型          |
| SVP_POS_INFO_S          | 指定输入图形的特定区域做检测的位置信息 |
| SVP_IMG_INFO_S          | 待检测图形信息             |
| SVP_RECT_S              | 检测到的目标框信息           |
| SVP_HD_RESULT_S         | 人形检测结果输出结构体         |
| SVP_FAS_RESULT_S        | 活体检测结果输出结构体         |
| SVP_FR_RESULT_S         | 人脸识别结果输出结构体         |
| SVP_GESTURE_RESULT_S    | 手势分类结果输出结构体         |
| FACE_ANGLE_S            | 人脸角度结果输出结构体         |
| SVP_FACE_ANGLE_RESULT_S | 人脸角度分类结果输出结构体       |
| SVP_AI_ISP_RESULT_S     | AI ISP输出结构体         |
| SVP_OUTPUT_S            | SVP检测输出结构体          |
| SVP_BUFFER_S            | SVP模型数据结构体          |
| SVP_CONF_INFO_S         | SVP模型信息             |
| AK_MPI_SVP_GetVersion   | 获取svp库的版本号          |
| AK_MPI_SVP_CreateChn    | SVP创建通道             |
| AK_MPI_SVP_DestroyChn   | SVP销毁通道             |
| AK_MPI_SVP_Process      | SVP执行检测运算           |
| AK_MPI_SVP_Release      | 释放SVP输出的坐标数据        |
| AK_MPI_SVP_GetRaram     | 获取神经网络计算的阈值         |
| AK_MPI_SVP_SetRaram     | 设置神经网络计算的阈值         |
| <br/>                   |                     |

##  数据结构

###  AK_SVP_ENV_MODE_E

&emsp;&emsp;【说明】

&emsp;&emsp;SVP检测环境设置

&emsp;&emsp;【定义】

```C
typedef enum akSVP_ENV_MODE_E
{
    AK_SVP_DAY_MODE = 0,
    AK_SVP_NIGHT_MODE
}SVP_ENV_MODE_E;
```

&emsp;&emsp;【成员】

| **成员名称 **     | **描述 **                             |
| ----------------- | ------------------------------------- |
| AK_SVP_DAY_MODE   | 白天模式；KM02G系列芯片暂不支持模式设置 |
| AK_SVP_NIGHT_MODE | 夜晚模式；KM02G系列芯片暂不支持模式设置 |

&emsp;&emsp;【相关接口】

```text
    SVP_MODEL_ATTR_S结构体
```

<br/>

###  SVP_TARGET_TYPE_E

&emsp;&emsp;【说明】

&emsp;&emsp;检测或识别目标类型

&emsp;&emsp;【定义】

```C
    typedef enum akSVP_TARGET_TYPE_E
	{
		AK_SVP_HUMAN_SHAPE = 0,				/* 人形检测 */
		AK_SVP_HUMAN_FACE,					/* 人脸检测 */
		AK_SVP_PET,		                    /* 宠物检测 */
	}SVP_TARGET_TYPE_E;
```

&emsp;&emsp;【成员】

| **成员名称 **      | **描述 ** |
| ------------------ | --------- |
| AK_SVP_HUMAN_SHAPE | 人形检测  |
| AK_SVP_HUMAN_FACE  | 人脸检测  |
| AK_SVP_PET         | 宠物检测  |

&emsp;&emsp;【相关函数接口】

```text
    SVP_RECT_S结构体；
```

<br/>

### SVP_MODEL_E

&emsp;&emsp;【说明】

&emsp;&emsp;SVP模型选择

&emsp;&emsp;【定义】

```C
typedef enum akSVP_MODEL_E
{
    AK_SVP_MODEL_HUMAN_YOLOV5N_640 = 0,        /* DN150 人形检测 */
    AK_SVP_MODEL_DETECT,				   /* 检测类 */
    AK_SVP_MODEL_AI_ISP,                   /* AI ISP处理 暂不支持*/
    AK_SVP_MODEL_0X0A010001,                 /* 人脸遮挡分类 224*224 6个类别 3*/
    AK_SVP_MODEL_0X0A020003,                 /* 人脸识别 112x112 4*/
    AK_SVP_MODEL_0X0A010007,                 /* 非机动车分类 112x112 5*/
    AK_SVP_MODEL_0X0A010004,                 /* 手势分类 64x64 6*/
    AK_SVP_MODEL_0X0A000005,                 /* 横向人脸检测 320*180 7*/
    AK_SVP_MODEL_0X0A010000,                 /* 活体分类 224x224 8*/
    AK_SVP_MODEL_0X0A010005,                 /* 人脸多角度分类 224x224 9*/
    AK_SVP_MODEL_MAX                       /* 枚举上限 */
}SVP_MODEL_E;
```

&emsp;&emsp;【成员】

| **成员名称 **                      | **描述 **            |
| ------------------------------ | ------------------ |
| AK_SVP_MODEL_HUMAN_YOLOV5N_640 | DN150 人形检测，640*384 |
| AK_SVP_MODEL_DETECT            | 检测类模型              |
| AK_SVP_MODEL_AI_ISP            | AI ISP 处理(暂不支持)    |
| AK_SVP_MODEL_0X0A010001        | 人脸遮挡分类(暂不支持)       |
| AK_SVP_MODEL_0X0A020003        | 人脸识别(暂不支持)         |
| AK_SVP_MODEL_0X0A010007<br>    | 非机动车分类(暂不支持)       |
| AK_SVP_MODEL_0X0A010004<br>    | 手势分类(暂不支持)         |
| AK_SVP_MODEL_0X0A000005<br>    | 横向人脸检测(暂不支持)       |
| AK_SVP_MODEL_0X0A010000        | 活体分类(暂不支持)         |
| AK_SVP_MODEL_0X0A010005        | 人脸多角度分类(暂不支持)      |
| AK_SVP_MODEL_MAX               | 模型枚举最大值            |

​		【说明】

YOLOV5N_640目前有4个模型，各模型检测类别、分辨率和输入数据格式如下：

| YOLOV5N_640**模型名称 **      | **检测目标** | 分辨率     | 输入数据格式  |
| ------------------------- | -------- | ------- | ------- |
| model_0x0A000008_V4.0.00  | 人形 人脸    | 640*384 | RGB-CHW |
| model_0x0A000012_V1.0.02  | 人车非      | 640*384 | RGB-HWC |
| model_0x0A000013_V1.0.01  | 头肩       | 640*384 | RGB-HWC |
| model_0x0A000016_V1.00.00 | 头肩人脸     | 640*384 | RGB-HWC |
| model_0x0A00000E_V1.0.00  | 人形宠物     | 640*384 | RGB-HWC |

&emsp;&emsp;【相关接口】

```text
    SVP_MODEL_ATTR_S结构体
```

<br/>

### SVP_HD_PARAM_S

&emsp;&emsp;【说明】

&emsp;&emsp;SVP人形检测阈值设置

&emsp;&emsp;【定义】

```C
typedef struct akSVP_HD_PARAM_S
{
    AK_S32      s32ClassifyThreshold;
    AK_S32      s32IouThreshold;
}SVP_HD_PARAM_S;
```

&emsp;&emsp;【成员】

| **成员名称 **        | **描述 **                                                    |
| -------------------- | ------------------------------------------------------------ |
| s32ClassifyThreshold | 分类阈值，范围[1-1000]，越大越严格，结果越可靠，但漏检率会提高 |
| s32IouThreshold      | 交并比阈值，范围[1-10]，允许目标周围多个框的重合度，越高达到该阈值的框越少，过滤的越少，留下的框越多。 |

&emsp;&emsp;【相关接口】

```text
	SVP_MODEL_PARAM_S结构体；
```

<br/>

### SVP_FAS_PARAM_S

&emsp;&emsp;【说明】

&emsp;&emsp;SVP活体检测阈值设置

&emsp;&emsp;【定义】

```C
typedef struct akSVP_FAS_PARAM_S
{
    AK_S32 s32ConfidenceThreshold;
}SVP_FAS_PARAM_S;
```

&emsp;&emsp;【成员】

| **成员名称 **          | **描述 ** |
| ---------------------- | --------- |
| s32ConfidenceThreshold | 得分阈值  |

&emsp;&emsp;【相关接口】

```text
	SVP_MODEL_PARAM_S结构体；
```

<br/>

### SVP_FR_PARAM_S

&emsp;&emsp;【说明】

&emsp;&emsp;SVP人脸识别阈值设置

&emsp;&emsp;【定义】

```C
typedef struct akSVP_FR_PARAM_S
{
    AK_S32 s32CosDistanceThreshold;
}SVP_FR_PARAM_S;
```

&emsp;&emsp;【成员】

| **成员名称 **           | **描述 ** |
| ----------------------- | --------- |
| s32CosDistanceThreshold | 得分阈值  |

&emsp;&emsp;【相关接口】

```text
	SVP_MODEL_PARAM_S结构体；
```

<br/>

### SVP_GESTURE_RE_PARAM_S

&emsp;&emsp;【说明】

&emsp;&emsp;SVP手势识别阈值设置

&emsp;&emsp;【定义】

```C
typedef struct akSVP_GESTURE_RE_PARAM_S
{
    AK_S32 s32ConfidenceThreshold;
}SVP_GESTURE_RE_PARAM_S;
```

&emsp;&emsp;【成员】

| **成员名称 **              | **描述 ** |
| ---------------------- | ------- |
| s32ConfidenceThreshold | 得分阈值    |

&emsp;&emsp;【相关接口】

```text
	SVP_MODEL_PARAM_S结构体；
```

<br/>
### SVP_AI_ISP_PARAM_S

&emsp;&emsp;【说明】

&emsp;&emsp;AI ISP 参数设置

&emsp;&emsp;【定义】

```C
typedef struct akSVP_AI_ISP_PARAM_S
{
    AK_S32 s32Reserve;
}SVP_AI_ISP_PARAM_S;
```

&emsp;&emsp;【成员】

| **成员名称 ** | **描述 **       |
| ------------- | --------------- |
| s32Reserve    | AI ISP 参数阈值 |

&emsp;&emsp;【相关接口】

```text
	SVP_MODEL_PARAM_S结构体；
```

<br/>

### SVP_MODEL_PARAM_S

&emsp;&emsp;【说明】

&emsp;&emsp;SVP模型参数阈值属性

&emsp;&emsp;【定义】

```C
typedef struct akSVP_MODEL_PARAM_S
{
    union
    {
        SVP_HD_PARAM_S  stHdParam;
        SVP_FAS_PARAM_S stFasParam;
        SVP_FR_PARAM_S  stFrParam;
		SVP_GESTURE_RE_PARAM_S stGsParam;
        SVP_AI_ISP_PARAM_S stAiIspParam;
    }param;
}SVP_MODEL_PARAM_S;
```

&emsp;&emsp;【成员】

| **成员名称 **    | **描述 **                |
| ------------ | ---------------------- |
| param        | svp模型参数，为后续拓展使用union共用 |
| stHdParam    | 人形检测阈值参数               |
| stFasParam   | 活体检测阈值参数               |
| stFrParam    | 人脸识别阈值参数               |
| stGsParam    | 手势识别阈值参数               |
| stAiIspParam | AI ISP参数(暂不支持)         |

&emsp;&emsp;【相关接口】

```C
	SVP_MODEL_ATTR_S结构体
	AK_MPI_SVP_GetRaram();
	AK_MPI_SVP_SetParam();
```

<br/>

### SVP_MODEL_ATTR_S

&emsp;&emsp;【说明】

&emsp;&emsp;SVP模型属性

&emsp;&emsp;【定义】

```C
	typedef struct akSVP_MODEL_ATTR_S
	{
		SVP_ENV_MODE_E		enEnvMode;			/*环境模式，KM02G系列芯片不支持*/
		SVP_MODEL_E			enModelType;		/*检测模型类型*/
		SVP_MODEL_PARAM_S 	stModelParam;		/*模型阈值参数*/
	}SVP_MODEL_ATTR_S;
```

&emsp;&emsp;【成员】

| **成员名称 ** | **描述 **        |
| ------------- | ---------------- |
| enEnvMode     | 检测环境工作模式 |
| enModelType   | 目标检测模型类别 |
| stModelParam  | 检测模型阈值参数 |

&emsp;&emsp;【相关接口】

```C
	SVP_CHN_ATTR_S结构体;
```

<br/>

### SVP_CHN_ATTR_S

&emsp;&emsp;【说明】

&emsp;&emsp;SVP通道属性

&emsp;&emsp;【定义】

```C
	typedef struct akSVP_CHN_ATTR_S
	{
		AK_S32				s32ModelNum;		/*SVP 模型个数*/
		SVP_MODEL_ATTR_S	astModelAttr[];		/*模型属性*/
	}SVP_CHN_ATTR_S;
```

&emsp;&emsp;【成员】

| **成员名称 **  | **描述 **    |
| -------------- | ------------ |
| s32ModelNum    | SVP 模型个数 |
| astModelAttr[] | 模型属性     |

&emsp;&emsp;【相关接口】

```C
	AK_MPI_SVP_CreateChn();
```

<br/>

### pfnSvpCusReadFunc

&emsp;&emsp;【说明】

&emsp;&emsp;定义用于客制化的读取文件方式，用于支持客制化的AI网络

&emsp;&emsp;【定义】

```C
	typedef AK_S32 (*pfnSvpCusReadFunc)(AK_VOID *pvDstBuf, AK_S32 s32BufLen, const AK_CHAR *pcPath);
```

&emsp;&emsp;【成员】

| **成员名称 ** | **描述 **        |
| ------------- | ---------------- |
| pvDstBuf      | 数据存放地址     |
| s32BufLen     | 文件buf长度      |
| pcPath        | 配置模型文件路径 |

&emsp;&emsp;【相关接口】

```C
	AK_MPI_SVP_CreateChn();
```

<br/>

### SVP_IMG_TYPE_E

&emsp;&emsp;【说明】

&emsp;&emsp;检测输入图形数据类型

&emsp;&emsp;【定义】

```C
	typedef enum akSVP_IMG_TYPE_E
	{
        AK_SVP_IMG_YUV420SP = 0,            /* YUV420SP，NV12*/
        AK_SVP_IMG_RGB_LI,                   /*RGB line-interlaced format */
        AK_SVP_IMG_RGB_CHW,                   /*RGB RGB_CHW */
        AK_SVP_IMG_RGB_HWC                    /*RGB RGB_HWC */
	}SVP_IMG_TYPE_E;
```

&emsp;&emsp;【成员】

| **成员名称 **       | **描述 **                                               |
| ------------------- | ------------------------------------------------------- |
| AK_SVP_IMG_YUV420SP | NV12，YUV420SP格式                                      |
| AK_SVP_IMG_RGB_LI   | RGB line-interlaced 格式，可通过设定vi的channel类型输出 |
| AK_SVP_IMG_RGB_CHW  | RGB_CHW格式，可通过设定vpss的channel类型输出            |
| AK_SVP_IMG_RGB_HWC  | RGB_HWC格式，可通过设定vpss的channel类型输出            |

&emsp;&emsp;【相关接口】

```text
    SVP_IMG_INFO_S结构体
```

<br/>

### SVP_POS_INFO_S

&emsp;&emsp;【说明】

&emsp;&emsp;指定输入图形的特定区域做检测的位置信息 ，全幅检测需要把各个位置信息填写正确。

&emsp;&emsp;【定义】

```C
	typedef struct akSVP_POS_INFO_S
	{
        AK_S32 s32Left;
        AK_S32 s32Top;
        AK_S32 s32Width;
        AK_S32 s32Height;
	}SVP_POS_INFO_S;
```

&emsp;&emsp;【成员】

| **成员名称 ** | **描述 **                             |
| ------------- | ------------------------------------- |
| s32Left       | 输入图形指定检测区域的坐上角X坐标     |
| s32Top        | 输入图形指定检测区域的左上角Y坐标     |
| s32Width      | 输入图形指定检测区域从X坐标开始的宽度 |
| s32Height     | 输入图形指定检测区域从Y坐标开始的高度 |

&emsp;&emsp;【相关接口】

```text
	SVP_IMG_INFO_S结构体
```

<br/>

### SVP_IMG_INFO_S

&emsp;&emsp;【说明】

&emsp;&emsp;待检测图形位置信息

&emsp;&emsp;【定义】

```C
	typedef struct akSVP_IMG_INFO_S
	{
        AK_S32				s32ModelIndex;
        SVP_IMG_TYPE_E      enImgType;
        AK_S32              s32Width;
        AK_S32              s32Height;
        SVP_POS_INFO_S      stPosInfo;
        AK_U64              u64PhyAddr;
        AK_VOID             *pvVirAddr;
	} SVP_IMG_INFO_S;
```

&emsp;&emsp;【成员】

| **成员名称 ** | **描述 **                    |
| ------------- | ---------------------------- |
| s32ModelIndex | 模型内部索引 |
| enImgType | 输入图形的数据类型 |
| s32Width | 输入图形的分辨率宽度，取值取决于输入图片宽度 |
| s32Height | 输入图形的分辨率高度，取值取决于输入图片高度 |
| stPosInfo | 输入图形做区域检测的位置信息 |
| u64PhyAddr | 输入图形的起始物理地址 |
| pvVirAddr | 输入图形的起始虚拟地址 |
|&emsp;&emsp;【相关接口】||

```C
	AK_MPI_SVP_Process();
```

<br/>

### SVP_RECT_S

&emsp;&emsp;【说明】

&emsp;&emsp;输出的人形框坐标信息

&emsp;&emsp;【定义】

```C
	typedef struct akSVP_RECT_S	    //coordinate values
	{
        AK_U32 			 enLabel;
        AK_U16           u16Left;       //left_top point, horizontal axis, 左上角x值
        AK_U16           u16Top;        //left_top point, vertical axis,   左上角y值
        AK_U16           u16Right;      //right_bottom point, horizontal axis 右下角x值
        AK_U16           u16Bottom;     //right_bottom point, vertical axis   右下角y值
        AK_U32           u32Score;      // 识别出来的区域的得分
	}SVP_RECT_S;
```

&emsp;&emsp;【成员】

| **成员名称 ** | **描述 **      |
| ------------- | -------------- |
| enLabel       | 坐标分类的标识 |
| u16Left       | 坐标左上角x值  |
| u16Top        | 坐标左上角y值  |
| u16Right      | 坐标右下角x值  |
| u16Bottom     | 坐标右下角y值  |
| u32Score      | 检测结果的得分 |

&emsp;&emsp;【相关接口】

```text
	SVP_HD_RESULT_S结构体；
```

<br/>

### SVP_HD_RESULT_S

&emsp;&emsp;【说明】

&emsp;&emsp;人形检测结果输出结构体

&emsp;&emsp;【定义】

```C
	typedef struct akSVP_HD_RESULT_S
	{
        AK_S16 s16ModuleId;
        AK_S16 s16ModuleType;
        AK_S32 s32TotalNum;
        SVP_RECT_S *pstTargetBoxes;        //coordinate values,坐标信息数组
	}SVP_HD_RESULT_S;
```

&emsp;&emsp;【成员】

| **成员名称 **      | **描述 **  |
| -------------- | -------- |
| s16ModuleId    | 模型id     |
| s16ModuleType  | 模型类型     |
| s32TotalNum    | 检测目标输出个数 |
| pstTargetBoxes | 检测坐标框信息  |

&emsp;&emsp;【相关接口】

```C
	SVP_OUTPUT_S();
```

<br/>
### SVP_FAS_RESULT_S

&emsp;&emsp;【说明】

&emsp;&emsp;活体检测结果输出结构体

&emsp;&emsp;【定义】

```C
	typedef struct akSVP_FAS_RESULT_S
	{
        AK_U32 u32Label;
        AK_U32 u32Confidence;
	}SVP_FAS_RESULT_S;
```

&emsp;&emsp;【成员】

| **成员名称 **      | **描述 **  |
| -------------- | -------- |
| u32Label       | 类别标签     |
| u32Confidence  | 类别得分     |

&emsp;&emsp;【相关接口】

```C
	SVP_OUTPUT_S();
```

<br/>

### SVP_FR_RESULT_S

&emsp;&emsp;【说明】

&emsp;&emsp;人脸识别结果输出结构体

&emsp;&emsp;【定义】
```C
	typedef struct akSVP_FR_RESULT_S
	{
        AK_U32  u32DataLen;          //feature len;
        AK_S16 *pcData;            //feature values;
	}SVP_FR_RESULT_S;
```

&emsp;&emsp;【成员】

| **成员名称 **  | **描述 ** |
| ---------- | ------- |
| u32DataLen | 人脸特征长度  |
| pcData     | 人脸特征    |

&emsp;&emsp;【相关接口】

```C
	SVP_OUTPUT_S();
```

<br/>

### SVP_GESTURE_RESULT_S

&emsp;&emsp;【说明】

&emsp;&emsp;手势分类结果输出结构体

&emsp;&emsp;【定义】
```C
	typedef struct akSVP_GESTURE_RESULT_S
	{
        AK_U32 u32Label;
        AK_U32 u32Confidence;
	}SVP_GESTURE_RESULT_S;
```

&emsp;&emsp;【成员】

| **成员名称 **     | **描述 ** |
| ------------- | ------- |
| u32Label      | 手势类别    |
| u32Confidence | 手势得分    |

&emsp;&emsp;【相关接口】

```C
	SVP_OUTPUT_S();
```

<br/>

### FACE_ANGLE__S

&emsp;&emsp;【说明】

&emsp;&emsp;人脸角度结果输出结构体

&emsp;&emsp;【定义】
```C
	typedef struct akFACE_ANGLE_S
	{
        AK_U32 u32Label;
        AK_U32 u32Confidence;
	}FACE_ANGLE_S;
```

&emsp;&emsp;【成员】

| **成员名称 **     | **描述 ** |
| ------------- | ------- |
| u32Label      | 人脸角度类别  |
| u32Confidence | 人脸角度得分  |

&emsp;&emsp;【相关接口】

```C
	SVP_OUTPUT_S();
```
<br/>

### SVP_FACE_ANGLE_RESULT_S

&emsp;&emsp;【说明】

&emsp;&emsp;人脸角度分类结果输出结构体

&emsp;&emsp;【定义】
```C
	typedef struct akSVP_FACE_ANGLE_RESULT_S
	{
        AK_S32 s32TotalNum;
        FACE_ANGLE_S astFaceAngle[CLASSIFY_NUM];
	}SVP_FACE_ANGLE_RESULT_S;
```

&emsp;&emsp;【成员】

| **成员名称 **    | **描述 **  |
| ------------ | -------- |
| s32TotalNum  | 人脸角度类别总数 |
| astFaceAngle | 人脸角度信息   |

&emsp;&emsp;【相关接口】

```C
	SVP_OUTPUT_S();
```
<br/>

### SVP_AI_ISP_RESULT_S

&emsp;&emsp;【说明】

&emsp;&emsp;AI ISP输出结构体

&emsp;&emsp;【定义】

```C
	typedef struct akSVP_AI_ISP_RESULT_S
	{
        AK_U8 *u8Data;		/* yuv data */
	}SVP_AI_ISP_RESULT_S;
```

&emsp;&emsp;【成员】

| **成员名称 ** | **描述 **          |
| ------------- | ------------------ |
| u8Data        | AI ISP输出数据指针 |

&emsp;&emsp;【相关接口】

```C
	SVP_OUTPUT_S();
```

<br/>

### SVP_OUTPUT_S

&emsp;&emsp;【说明】

&emsp;&emsp;检测结果输出结构体

&emsp;&emsp;【定义】

```C
	typedef struct akSVP_OUTPUT_S
	{
        union{
            SVP_HD_RESULT_S stHdResult;
            SVP_FAS_RESULT_S stFasResult;
            SVP_FR_RESULT_S stFrResult;
            SVP_GESTURE_RESULT_S stGestureResult;
	        SVP_FACE_ANGLE_RESULT_S stFaceAngleResult;
            SVP_AI_ISP_RESULT_S stAispResult;
        }result;
        AK_S32  s32ModelType;
        AK_S32  s32ModelIndex;
	}SVP_OUTPUT_S;
```

&emsp;&emsp;【成员】

| **成员名称 **     | **描述 **           |
| ------------- | ----------------- |
| result        | 不同类型输出结构体，union共用 |
| s32ModelType  | 检测模型类型            |
| s32ModelIndex | 检测模型索引            |

&emsp;&emsp;【相关接口】

```C
	AK_MPI_SVP_Process();
	AK_MPI_SVP_Release();
```

<br/>

### SVP_BUFFER_S

&emsp;&emsp;【说明】

&emsp;&emsp;DMA buf 结构体

&emsp;&emsp;【定义】

```C
	typedef struct akSVP_BUFFER_S
    {
        AK_VOID		*pvData;		// virtual address of the buffer
        AK_U64      u64Pa;      	// physical address of the buffer
        AK_U32      u32Size;    	// size of the buffer
	}SVP_BUFFER_S;
```

&emsp;&emsp;【成员】

| **成员名称 ** | **描述 **      |
| ------------- | -------------- |
| pvData   | DMA虚拟内存地址 |
| u64Pa       | DMA物理内存地址 |
| u32Size   | DMA内存大小     |

&emsp;&emsp;【相关接口】

```text
	SVP_CONF_INFO_S结构体
```

<br/>

### SVP_CONF_INFO_S

&emsp;&emsp;【说明】

&emsp;&emsp;SVP 模型参数结构体

&emsp;&emsp;【定义】

```C
	typedef struct akSVP_CONF_INFO_S
    {
        union
        {
            AK_CHAR *pcConf;
            SVP_BUFFER_S *pstConfBuf;
        } conf_type;
        AK_S32 s32ConfMode;     // conf load mode, 0: path, 1: buffer
        pfnSvpCusReadFunc pfnReadFunc;
	}SVP_CONF_INFO_S;
```

&emsp;&emsp;【成员】

| **成员名称 ** | **描述 **                                     |
| ------------- | --------------------------------------------- |
| conf_type     | 模型参数                                      |
| s32ConfMode   | 模型参数类型，可选择配置路径或直接配置DMA地址 |
| pfnReadFunc   | 读取模型回调函数                              |

&emsp;&emsp;【相关接口】

```C
	AK_MPI_SVP_CreateChn();
```

<br/>

## 版本信息获取

###  AK_MPI_SVP_GetVersion

&emsp;&emsp;【描述】

&emsp;&emsp;获取svp库的版本号

&emsp;&emsp;【语法】

```C
	const AK_CHAR* AK_MPI_SVP_GetVersion(AK_VOID);
```

&emsp;&emsp;【参数】

| **参数名称 ** | **描述 ** | **取值范围 ** | **输入/输出 ** |
| ------------- | --------- | ------------- | -------------- |
| AK_VOID       | -         | -             | -              |

&emsp;&emsp;【返回值】

| **返回值 **   | **描述 ** |
| ------------- | --------- |
| svp模块版本号 | 成功      |
| NULL          | 失败      |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_svp.so或者libmpi_svp.a

​		头文件：ak_svp.h

<br/>

## 流程函数

###  AK_MPI_SVP_CreateChn

&emsp;&emsp;【描述】

&emsp;&emsp;创建一个SVP检测通道，每个检测通道对应一个句柄。KM02G系列芯片最多支持打开4个检测通道。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_MPI_SVP_CreateChn(AK_S32 s32HandleId, const SVP_CHN_ATTR_S *pstAttr, SVP_CONF_INFO_S *pstConfInfo);
```

&emsp;&emsp;【参数】

| **参数名称 ** | **描述 **        | **取值范围 ** | **输入/输出 ** |
| ------------- | ---------------- | ------------- | -------------- |
| s32HandleId   | SVP 检测通道句柄 | [0, 3]        | 输入           |
| pstAttr       | CHN属性配置参数  | 参考结构体    | 输入           |
| pstConfInfo   | 模型参数信息     | 参考结构体    | 输入           |

&emsp;&emsp;【返回值】

| **返回值 ** | **描述 **            |
| ----------- | -------------------- |
| 0           | 成功。               |
| 非0         | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码 **               | **描述 **   |
| ------------------------- | ----------- |
| ERROR_SVP_HANDLE_ID_ERROR | SVP句柄有误 |
| ERROR_TYPE_INVALID_ARG    | 参数错误    |
| ERROR_TYPE_NOT_INIT       | SVP未初始化 |

【需求】

&emsp;&emsp;库文件：libmpi_svp.so或者libmpi_svp.a

&emsp;&emsp;头文件：ak_svp.h

> **注意：**
>
AK_MPI_SVP_CreateChn()的通道ID只能被创建一次，同一个CHN id被多次创建，程序会报错。
>
KM02G系列芯片暂不支持客制化网络
>
> 配对函数: AK_MPI_SVP_DestroyChn()

&emsp;&emsp;【接口调用顺序】

```c
    AK_MPI_NPU_Init();
    AK_MPI_SVP_CreateChn(svp_chn_id, &attr, &pstConfInfo);
    while(1)
    {
	    AK_MPI_SVP_Process(svp_chn_id, &input, &output);
        AK_MPI_SVP_Release(&output);
    }
    AK_MPI_SVP_DestroyChn(svp_chn_id);
	AK_MPI_NPU_Deinit();
```

<br/>

###  AK_MPI_SVP_DestroyChn

&emsp;&emsp;【描述】

&emsp;&emsp;关闭一个检测通道

&emsp;&emsp;【语法】

```C
    AK_S32 AK_MPI_SVP_DestroyChn(AK_S32 s32HandleId);
```

&emsp;&emsp;【参数】

| **参数名称 ** | **描述 **        | **取值范围 ** | **输入/输出 ** |
| ------------- | ---------------- | ------------- | -------------- |
| s32HandleId   | SVP 检测通道句柄 | [0, 3]        | 输入           |

&emsp;&emsp;【返回值】

| **返回值 ** | **描述 **            |
| ----------- | -------------------- |
| 0           | 成功。               |
| 非0         | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码 **               | **描述 **   |
| ------------------------- | ----------- |
| ERROR_SVP_HANDLE_ID_ERROR | SVP句柄有误 |
| ERROR_TYPE_NOT_INIT       | SVP未初始化 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_svp.so或者libmpi_svp.a

&emsp;&emsp;头文件：ak_svp.h

> **注意：**与AK_MPI_SVP_CreateChn()配对使用。

&emsp;&emsp;【接口调用顺序】

```c
    AK_MPI_NPU_Init(void);
    AK_MPI_SVP_CreateChn(svp_chn_id, &attr, &pstConfInfo);
    while(1)
    {
	    AK_MPI_SVP_Process(svp_chn_id, &input, &output);
        AK_MPI_SVP_Release(&output);
    }
    AK_MPI_SVP_DestroyChn(svp_chn_id);
	AK_MPI_NPU_Deinit(void);
```

<br/>

### AK_MPI_SVP_Process

&emsp;&emsp;【描述】

&emsp;&emsp;开始进行图形检测

&emsp;&emsp;【语法】

```C
    AK_S32 AK_MPI_SVP_Process(AK_S32 s32HandleId,  SVP_IMG_INFO_S *pstInput,  SVP_OUTPUT_S *pstOutput);
```

&emsp;&emsp;【参数】

| **参数名称 ** | **描述 **              | **取值范围 **            | **输入/输出 ** |
| ------------- | ---------------------- | ------------------------ | -------------- |
| s32HandleId   | SVP检测通道句柄        | [0, 3]                   | 输入           |
| pstInput      | 待检测图形信息指针     | 参考SVP_IMG_INFO_S结构体 | 输入           |
| pstOutput     | 输出检测结果的数据指针 | 参考SVP_OUTPUT_S结构体   | 输出           |

&emsp;&emsp;【返回值】

| **返回值 ** | **描述 **            |
| ----------- | -------------------- |
| 0           | 成功。               |
| 非0         | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码 **               | **描述 **   |
| ------------------------- | ----------- |
| ERROR_TYPE_INVALID_ARG    | 参数有误    |
| ERROR_SVP_HANDLE_ID_ERROR | SVP句柄有误 |
| ERROR_TYPE_NOT_INIT       | SVP未初始化 |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_svp.so或者libmpi_svp.a

&emsp;&emsp;头文件：ak_svp.h

> **注意：**
>
需要在AK_MPI_SVP_CreateChn()之后调用
>
SVP模块对于输入的图片做全幅检测，图片分辨率与SVP要求的分辨率一致，并且数据类型为RGB_HWC时，系统整体效率最高，CPU负载最小。当输入图形分辨率需要做区域检测，分辨率或者数据格式不是RGB_HWC的时候，都需要CPU先做二次数据处理，然后才会进行图像识别，会对整体系统效率和CPU负载造成影响。
>
配对函数：AK_MPI_SVP_Release()
>

&emsp;&emsp;【接口调用顺序】

```c
    AK_MPI_NPU_Init();
    AK_MPI_SVP_CreateChn(svp_chn_id, &attr, &pstConfInfo);
    while(1)
    {
	    AK_MPI_SVP_Process(svp_chn_id, &input, &output);
        AK_MPI_SVP_Release(&output);
    }
    AK_MPI_SVP_DestroyChn(svp_chn_id);
	AK_MPI_NPU_Deinit();
```

<br/>

### AK_MPI_SVP_Release

&emsp;&emsp;【描述】

&emsp;&emsp;释放输出的坐标数据

&emsp;&emsp;【语法】

```C
    AK_S32 AK_MPI_SVP_Release(SVP_OUTPUT_S *pstOutput);
```

&emsp;&emsp;【参数】

| **参数名称 ** | **描述 **                  | **取值范围 ** | **输入/输出 ** |
| ------------- | -------------------------- | ------------- | -------------- |
| pstOutput     | 获取到未释放的输出坐标数据 | -             | 输入           |

&emsp;&emsp;【返回值】

| **返回值 ** | **描述 **            |
| ----------- | -------------------- |
| 0           | 成功。               |
| 非0         | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码 **             | **描述 **    |
| ----------------------- | ------------ |
| ERROR_TYPE_POINTER_NULL | 参数指针为空 |
| ERROR_TYPE_NOT_INIT     | SVP未初始化  |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_svp.so或者libmpi_svp.a

&emsp;&emsp;头文件：ak_svp.h

> **注意：**与AK_MPI_SVP_Process()配对使用。

&emsp;&emsp;【接口调用顺序】

```c
    AK_MPI_NPU_Init(void);
    AK_MPI_SVP_CreateChn(svp_chn_id, &attr, &pstConfInfo);
    while(1)
    {
	    AK_MPI_SVP_Process(svp_chn_id, &input, &output);
        AK_MPI_SVP_Release(&output);
    }
    AK_MPI_SVP_DestroyChn(svp_chn_id);
	AK_MPI_NPU_Deinit(void);
```

<br/>

## 设置/获取属性函数

### AK_MPI_SVP_GetRaram

&emsp;&emsp;【描述】

&emsp;&emsp;获取某通道模型的阈值参数。

&emsp;&emsp;【语法】

```C
    AK_S32 AK_MPI_SVP_GetRaram(AK_S32 s32HandleId, SVP_MODEL_PARAM_S *stModelParam);
```

&emsp;&emsp;【参数】

| **参数名称 ** | **描述 **        | **取值范围 **               | **输入/输出 ** |
| ------------- | ---------------- | --------------------------- | -------------- |
| s32HandleId   | SVP检测通道句柄  | [0, 3]]                     | 输入           |
| stModelParam  | 阈值参数获取输出 | 参考SVP_MODEL_PARAM_S结构体 | 输出           |

&emsp;&emsp;【返回值】

| **返回值 ** | **描述 **            |
| ----------- | -------------------- |
| 0           | 成功。               |
| 非0         | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码 **                    | **描述 **                  |
| ------------------------------ | -------------------------- |
| ERROR_SVP_HANDLE_ID_ERROR      | SVP句柄有误                |
| ERROR_TYPE_POINTER_NULL        | 参数指针为NULL             |
| ERROR_TYPE_NOT_INIT            | SVP未初始化                |
| ERROR_SVP_HANDLE_ERROR         | 该通道对应的handle句柄错误 |
| ERROR_SVP_HANDLE_ID_NOT_CREATE | HANDLE_ID未创建            |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_svp.so或者libmpi_svp.a

&emsp;&emsp;头文件：ak_svp.h

> **注意：**需要在AK_MPI_SVP_CreateChn()之后调用。

&emsp;&emsp;【接口调用顺序】

```c
    AK_MPI_NPU_Init(void);
    AK_MPI_SVP_CreateChn(svp_chn_id, &attr, &pstConfInfo);
    while(1)
    {
	    AK_MPI_SVP_Process(svp_chn_id, &input, &output);
        AK_MPI_SVP_Release(&output);
    }
    AK_MPI_SVP_DestroyChn(svp_chn_id);
	AK_MPI_NPU_Deinit(void);
```

<br/>

### AK_MPI_SVP_SetParam

&emsp;&emsp;【描述】

&emsp;&emsp;设置某通道模型阈值

&emsp;&emsp;【语法】

```C
    AK_S32 AK_MPI_SVP_SetParam(AK_S32 s32HandleId, SVP_MODEL_PARAM_S stModelParam);
```

&emsp;&emsp;【参数】

| **参数名称 ** | **描述 **       | **取值范围 **               | **输入/输出 ** |
| ------------- | --------------- | --------------------------- | -------------- |
| s32HandleId   | SVP检测通道句柄 | [0, 3]                      | 输入           |
| stModelParam  | 阈值参数设置    | 参考SVP_MODEL_PARAM_S结构体 | 输入           |

&emsp;&emsp;【返回值】

| **返回值 ** | **描述 **            |
| ----------- | -------------------- |
| 0           | 成功。               |
| 非0         | 失败，其值为错误码。 |

&emsp;&emsp;【错误码列表】

| **错误码 **                      | **描述 **                  |
| -------------------------------- | -------------------------- |
| ERROR_SVP_HANDLE_ID_ERROR        | SVP句柄有误                |
| ERROR_TYPE_INVALID_ARG           | 参数有误                   |
| ERROR_TYPE_NOT_INIT              | SVP未初始化                |
| ERROR_SVP_SET_IOU_THRESHOLD      | 设置IoU_threshold错误      |
| ERROR_SVP_SET_CLASSIFY_THRESHOLD | 设置classify_threshold错误 |
| ERROR_SVP_HANDLE_ERROR           | 该通道对应的handle句柄错误 |
| ERROR_SVP_HANDLE_ID_NOT_CREATE   | HANDLE_ID未创建            |

&emsp;&emsp;【需求】

&emsp;&emsp;库文件：libmpi_svp.so或者libmpi_svp.a

&emsp;&emsp;头文件：ak_svp.h

> **注意：**需要在AK_MPI_SVP_CreateChn()之后调用。

&emsp;&emsp;【接口调用顺序】

```c
    AK_MPI_NPU_Init(void);
    AK_MPI_SVP_CreateChn(svp_chn_id, &attr, &pstConfInfo);
    while(1)
    {
	    AK_MPI_SVP_Process(svp_chn_id, &input, &output);
        AK_MPI_SVP_Release(&output);
    }
    AK_MPI_SVP_DestroyChn(svp_chn_id);
	AK_MPI_NPU_Deinit(void);
```

<br/>

## 接口调用依赖关系

| **接口**              | 接口依赖关系                                       |
| --------------------- | -------------------------------------------------- |
| AK_MPI_SVP_GetVersion | 随时可以调用                                       |
| 其他接口              | AK_MPI_NPU_Init之后                                |
| AK_MPI_SVP_GetRaram   | AK_MPI_SVP_CreateChn之后,AK_MPI_SVP_DestroyChn之前 |
| AK_MPI_SVP_SetRaram   | AK_MPI_SVP_CreateChn之后,AK_MPI_SVP_DestroyChn之前 |
| AK_MPI_SVP_Process    | AK_MPI_SVP_CreateChn之后,AK_MPI_SVP_DestroyChn之前 |

&emsp;&emsp;【接口调用顺序】

```c
	AK_MPI_NPU_Init(void);
    AK_MPI_SVP_CreateChn(svp_chn_id, &attr, &pstConfInfo);
    while(1)
    {
	    AK_MPI_SVP_Process(svp_chn_id, &input, &output);
        AK_MPI_SVP_Release(&output);
    }
    AK_MPI_SVP_DestroyChn(svp_chn_id);
	AK_MPI_NPU_Deinit(void);
```

<br/>

## svp sample示例

运行demo前需要加载的驱动：firmware_class.ko  ak_npu.ko  ak_vi.ko  sensor_xxx.ko  ak_vicap.ko  ak_isp.ko  ak_pp.ko ，以GC5603的CIS为例，可以参考脚本gc5603.sh，具体命令如下：

​        insmod /usr/modules/ak_vi.ko

​        insmod /usr/modules/sensor_gc5603.ko

​        insmod /usr/modules/ak_vicap.ko

​        insmod /usr/modules/ak_isp.ko

​        insmod /usr/modules/ak_pp.ko

​        其他CIS请参考对应的加载脚本xxx.sh。

> **注意：**加载firmware_class.ko时应配参数 path=/mnt,/mnt为elf模型所在的路径，可自定义修改该路径。

​       insmod /lib/modules/5.10.111/kernel/drivers/base/firmware_loader/firmware_class.ko path=/mnt

​       insmod /usr/modules/ak_npu.ko

| **输入参数**       | **输入参数说明**                                |
| ------------------ | ----------------------------------------------- |
| help               | 帮助信息                                        |
| grp_index          | VPSS Group号                                    |
| chn_index          | VPSS chn 号                                     |
| frame_cnt          | 采集帧数 [0, 2^31 -1]                           |
| grep_res_index     | VPSS Group 分辨率，取值与sensor有关             |
| chn_res_index      | VPSS Chn 分辨率，模型输入要求的分辨率           |
| chn_framerate      | VPSS Chn 帧率                                   |
| chn_crop_x         | 通道裁剪起始x坐标                               |
| chn_crop_y         | 通道裁剪起始y坐标                               |
| chn_crop_w         | 通道裁剪宽度                                    |
| chn_crop_h         | 通道裁剪高度                                    |
| isp_config_path    | ISP config file 保存路径，默认为空，需要填写。  |
| frame_save_path    | 保存rgb图像的路径                               |
| elf_path           | elf模型文件路径                                 |
| data_type          | 采集输入给svp的图像格式 0:RGB_HWC, 1:RGB_CHW    |
| svp_rate           | 每几帧做一次svp检测                             |
| classify_threshold | 分类置信度阈值 [0, 1000]                        |
| iou_threshold      | iou过滤阈值 [0, 10]                             |
| filter_enable      | 是否开启人形过滤  0:disable  1:md  2:md+filter. |

<br/>

&emsp;&emsp;输出结果：输出打印检测到的目标的label，score，和box坐标。

## /var/platform说明

在板端运行应用后，通过执行下面的命令可以获取到当前应用调用的相关库版本号和参数设置

```shell
cat /var/platform/SVP/stat
# "nna_version":  "libak_nna V1.0.05",		NNA库版本号
# "nne_version":  "libak_nne V1.0.05",		NNE库版本号
# "svp_version":  "libmpi_svp V1.0.12"		SVP库版本号
```

```shell
cat /var/platform/SVP/param
# "chn0_id":      "0",						SVP handle id
# "chn0_param_path":      "yolov5n_640",	SVP 模型名
# "chn0_env_mode":        "0",				SVP 白天黑夜模式，暂不支持(0：白天 1：夜间)
# "chn0_model_type":      "2"				SVP 模型类型（1：480人形人脸模型 2：480宠物模型 3：640模型）
```

<br/>

## 错误码说明

| 错误代码   | 宏定义                         | 含义                       |
| ---------- | ------------------------------ | -------------------------- |
| 0x28000000 | ERROR_SVP_ALREADY_OPEN         | svp已经打开                |
| 0x28000001 | ERROR_SVP_HANDLE_ID_ERROR      | handle_id 错误             |
| 0x28000002 | ERROR_SVP_HANDLE_ERROR         | 该通道对应的handle句柄错误 |
| 0x28000003 | ERROR_SVP_NOT_CREATE           | svp没有创建                |
| 0x28000004 | ERROR_SVP_SET_PARAM            | 设置参数错误               |
| 0x28000005 | ERROR_SVP_GET_PARAM            | 获取参数错误               |
| 0x28000006 | ERROR_SVP_ALREADY_INIT         | svp已经初始化              |
| 0x28000007 | ERROR_SVP_ALREADY_DEINIT       | svp已经销毁                |
| 0x28000008 | ERROR_SVP_HANDLE_ID_NOT_CREATE | handle_id没有创建成功      |
| 0x28000009 | ERROR_TYPE_DMA_MALLOC_FAILED   | 分配DMA内存失败            |
| 0x2800000a | ERROR_SVP_GET_DMA_FD_FAILED    | 获取DMA句柄失败            |

<br/>
