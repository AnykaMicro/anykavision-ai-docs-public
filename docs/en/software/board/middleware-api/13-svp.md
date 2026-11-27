# Smart Vision Processing

## Overview

The Smart Vision Processing (SVP) module supports human-shape and face detection.

The user obtains a frame of data (in RGB_HWC format) through the VI module API, or reads a frame from a file, and passes that data to an SVP module API. After neural-network processing, the API outputs the coordinates of the detected targets.

<br/>

## API Reference

&emsp;&emsp;This module provides the following APIs.

| **Library interface**      | **Description**       |
| ----------------------- | ------------------- |
| SVP_ENV_MODE_E          | SVP operating-environment mode |
| SVP_TARGET_TYPE_E       | SVP detection-target type |
| SVP_MODEL_E             | Neural-network model selection |
| SVP_HD_PARAM_S          | Human-shape detection thresholds |
| SVP_FAS_PARAM_S         | Liveness-detection threshold |
| SVP_FR_PARAM_S          | Face-recognition threshold |
| SVP_GESTURE_RE_PARAM_S  | Gesture-classification threshold |
| SVP_AI_ISP_PARAM_S      | Reserved AI ISP parameter |
| SVP_MODEL_PARAM_S       | SVP model thresholds |
| SVP_MODEL_ATTR_S        | SVP model attributes |
| SVP_CHN_ATTR_S          | SVP channel attributes |
| pfnSvpCusReadFunc       | Model-reading callback function |
| SVP_IMG_TYPE_E          | Input image-data type for detection |
| SVP_POS_INFO_S          | Position information specifying a region of the input image for detection |
| SVP_IMG_INFO_S          | Information about the image to detect |
| SVP_RECT_S              | Information about a detected target box |
| SVP_HD_RESULT_S         | Human-shape detection-result output structure |
| SVP_FAS_RESULT_S        | Liveness-detection-result output structure |
| SVP_FR_RESULT_S         | Face-recognition-result output structure |
| SVP_GESTURE_RESULT_S    | Gesture-classification-result output structure |
| FACE_ANGLE_S            | Face-angle-result output structure |
| SVP_FACE_ANGLE_RESULT_S | Face-angle-classification-result output structure |
| SVP_AI_ISP_RESULT_S     | AI ISP output structure |
| SVP_OUTPUT_S            | SVP detection-output structure |
| SVP_BUFFER_S            | SVP model-data structure |
| SVP_CONF_INFO_S         | SVP model information |
| AK_MPI_SVP_GetVersion   | Gets the SVP library version |
| AK_MPI_SVP_CreateChn    | Creates an SVP channel |
| AK_MPI_SVP_DestroyChn   | Destroys an SVP channel |
| AK_MPI_SVP_Process      | Performs SVP detection |
| AK_MPI_SVP_Release      | Releases coordinate data output by SVP |
| AK_MPI_SVP_GetRaram     | Gets neural-network computation thresholds |
| AK_MPI_SVP_SetRaram     | Sets neural-network computation thresholds |
| <br/>                   |                     |

> **Source note:** The Chinese source uses `AK_MPI_SVP_SetRaram` in this overview. The documented API and the supplied `ak_svp.h` header declare the setter as `AK_MPI_SVP_SetParam`; use that declared name.

## Data Structures

###  AK_SVP_ENV_MODE_E

&emsp;&emsp;【Description】

&emsp;&emsp;SVP detection-environment setting.

&emsp;&emsp;【Definition】

```C
typedef enum akSVP_ENV_MODE_E
{
    AK_SVP_DAY_MODE = 0,
    AK_SVP_NIGHT_MODE
}SVP_ENV_MODE_E;
```

&emsp;&emsp;【Members】

| **Member**         | **Description**                       |
| ----------------- | ------------------------------------- |
| AK_SVP_DAY_MODE   | Day mode; KM02G-series chips do not currently support mode configuration |
| AK_SVP_NIGHT_MODE | Night mode; KM02G-series chips do not currently support mode configuration |

&emsp;&emsp;【Related API】

```text
    SVP_MODEL_ATTR_S structure
```

<br/>

###  SVP_TARGET_TYPE_E

&emsp;&emsp;【Description】

&emsp;&emsp;Type of target to detect or recognize.

&emsp;&emsp;【Definition】

```C
    typedef enum akSVP_TARGET_TYPE_E
	{
		AK_SVP_HUMAN_SHAPE = 0,				/* Human-shape detection */
		AK_SVP_HUMAN_FACE,					/* Face detection */
		AK_SVP_PET,		                    /* Pet detection */
	}SVP_TARGET_TYPE_E;
```

&emsp;&emsp;【Members】

| **Member**          | **Description** |
| ------------------ | --------- |
| AK_SVP_HUMAN_SHAPE | Human-shape detection |
| AK_SVP_HUMAN_FACE  | Face detection |
| AK_SVP_PET         | Pet detection |

&emsp;&emsp;【Related function interface】

```text
    SVP_RECT_S structure;
```

<br/>

### SVP_MODEL_E

&emsp;&emsp;【Description】

&emsp;&emsp;SVP model selection.

&emsp;&emsp;【Definition】

```C
typedef enum akSVP_MODEL_E
{
    AK_SVP_MODEL_HUMAN_YOLOV5N_640 = 0,        /* DN150 human-shape detection */
    AK_SVP_MODEL_DETECT,				   /* Detection model */
    AK_SVP_MODEL_AI_ISP,                   /* AI ISP processing; not currently supported */
    AK_SVP_MODEL_0X0A010001,                 /* Face-occlusion classification, 224*224, 6 classes, 3 */
    AK_SVP_MODEL_0X0A020003,                 /* Face recognition, 112x112, 4 */
    AK_SVP_MODEL_0X0A010007,                 /* Non-motor-vehicle classification, 112x112, 5 */
    AK_SVP_MODEL_0X0A010004,                 /* Gesture classification, 64x64, 6 */
    AK_SVP_MODEL_0X0A000005,                 /* Horizontal face detection, 320*180, 7 */
    AK_SVP_MODEL_0X0A010000,                 /* Liveness classification, 224x224, 8 */
    AK_SVP_MODEL_0X0A010005,                 /* Multi-angle face classification, 224x224, 9 */
    AK_SVP_MODEL_MAX                       /* Maximum enumerator */
}SVP_MODEL_E;
```

&emsp;&emsp;【Members】

| **Member**                          | **Description**      |
| ------------------------------ | ------------------ |
| AK_SVP_MODEL_HUMAN_YOLOV5N_640 | DN150 human-shape detection, 640*384 |
| AK_SVP_MODEL_DETECT            | Detection model |
| AK_SVP_MODEL_AI_ISP            | AI ISP processing (not currently supported) |
| AK_SVP_MODEL_0X0A010001        | Face-occlusion classification (not currently supported) |
| AK_SVP_MODEL_0X0A020003        | Face recognition (not currently supported) |
| AK_SVP_MODEL_0X0A010007<br>    | Non-motor-vehicle classification (not currently supported) |
| AK_SVP_MODEL_0X0A010004<br>    | Gesture classification (not currently supported) |
| AK_SVP_MODEL_0X0A000005<br>    | Horizontal face detection (not currently supported) |
| AK_SVP_MODEL_0X0A010000        | Liveness classification (not currently supported) |
| AK_SVP_MODEL_0X0A010005        | Multi-angle face classification (not currently supported) |
| AK_SVP_MODEL_MAX               | Maximum model enumerator |

​		【Description】

The source states that YOLOV5N_640 currently has four models, but the table below lists five. Confirm the supported model set with the vendor. The listed detection classes, resolutions, and input-data formats are:

| YOLOV5N_640 **model name** | **Detection target** | Resolution | Input-data format |
| ------------------------- | -------- | ------- | ------- |
| model_0x0A000008_V4.0.00  | Human shape and face | 640*384 | RGB-CHW |
| model_0x0A000012_V1.0.02  | Human, vehicle, and non-motor vehicle | 640*384 | RGB-HWC |
| model_0x0A000013_V1.0.01  | Head and shoulders | 640*384 | RGB-HWC |
| model_0x0A000016_V1.00.00 | Head, shoulders, and face | 640*384 | RGB-HWC |
| model_0x0A00000E_V1.0.00  | Human shape and pet | 640*384 | RGB-HWC |

&emsp;&emsp;【Related API】

```text
    SVP_MODEL_ATTR_S structure
```

<br/>

### SVP_HD_PARAM_S

&emsp;&emsp;【Description】

&emsp;&emsp;SVP human-shape detection threshold settings.

&emsp;&emsp;【Definition】

```C
typedef struct akSVP_HD_PARAM_S
{
    AK_S32      s32ClassifyThreshold;
    AK_S32      s32IouThreshold;
}SVP_HD_PARAM_S;
```

&emsp;&emsp;【Members】

| **Member**            | **Description**                                              |
| -------------------- | ------------------------------------------------------------ |
| s32ClassifyThreshold | Classification threshold, range [1-1000]. A larger value is stricter and produces more reliable results, but increases the missed-detection rate. |
| s32IouThreshold      | Intersection-over-union threshold, range [1-10], controlling the permitted overlap among multiple boxes around a target. At higher values, fewer boxes reach the threshold, fewer are filtered, and more remain. |

&emsp;&emsp;【Related API】

```text
	SVP_MODEL_PARAM_S structure;
```

<br/>

### SVP_FAS_PARAM_S

&emsp;&emsp;【Description】

&emsp;&emsp;SVP liveness-detection threshold setting.

&emsp;&emsp;【Definition】

```C
typedef struct akSVP_FAS_PARAM_S
{
    AK_S32 s32ConfidenceThreshold;
}SVP_FAS_PARAM_S;
```

&emsp;&emsp;【Members】

| **Member**              | **Description** |
| ---------------------- | --------- |
| s32ConfidenceThreshold | Score threshold |

&emsp;&emsp;【Related API】

```text
	SVP_MODEL_PARAM_S structure;
```

<br/>

### SVP_FR_PARAM_S

&emsp;&emsp;【Description】

&emsp;&emsp;SVP face-recognition threshold setting.

&emsp;&emsp;【Definition】

```C
typedef struct akSVP_FR_PARAM_S
{
    AK_S32 s32CosDistanceThreshold;
}SVP_FR_PARAM_S;
```

&emsp;&emsp;【Members】

| **Member**               | **Description** |
| ----------------------- | --------- |
| s32CosDistanceThreshold | Score threshold |

&emsp;&emsp;【Related API】

```text
	SVP_MODEL_PARAM_S structure;
```

<br/>

### SVP_GESTURE_RE_PARAM_S

&emsp;&emsp;【Description】

&emsp;&emsp;SVP gesture-recognition threshold setting.

&emsp;&emsp;【Definition】

```C
typedef struct akSVP_GESTURE_RE_PARAM_S
{
    AK_S32 s32ConfidenceThreshold;
}SVP_GESTURE_RE_PARAM_S;
```

&emsp;&emsp;【Members】

| **Member**                  | **Description** |
| ---------------------- | ------- |
| s32ConfidenceThreshold | Score threshold |

&emsp;&emsp;【Related API】

```text
	SVP_MODEL_PARAM_S structure;
```

<br/>
### SVP_AI_ISP_PARAM_S

&emsp;&emsp;【Description】

&emsp;&emsp;AI ISP parameter setting.

&emsp;&emsp;【Definition】

```C
typedef struct akSVP_AI_ISP_PARAM_S
{
    AK_S32 s32Reserve;
}SVP_AI_ISP_PARAM_S;
```

&emsp;&emsp;【Members】

| **Member**     | **Description** |
| ------------- | --------------- |
| s32Reserve    | AI ISP parameter threshold |

&emsp;&emsp;【Related API】

```text
	SVP_MODEL_PARAM_S structure;
```

<br/>

### SVP_MODEL_PARAM_S

&emsp;&emsp;【Description】

&emsp;&emsp;SVP model-parameter threshold attributes.

&emsp;&emsp;【Definition】

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

&emsp;&emsp;【Members】

| **Member**        | **Description**          |
| ------------ | ---------------------- |
| param        | SVP model parameters; a shared union for future extension |
| stHdParam    | Human-shape detection threshold parameters |
| stFasParam   | Liveness-detection threshold parameters |
| stFrParam    | Face-recognition threshold parameters |
| stGsParam    | Gesture-recognition threshold parameters |
| stAiIspParam | AI ISP parameters (not currently supported) |

&emsp;&emsp;【Related API】

```C
	SVP_MODEL_ATTR_S structure
	AK_MPI_SVP_GetRaram();
	AK_MPI_SVP_SetParam();
```

<br/>

### SVP_MODEL_ATTR_S

&emsp;&emsp;【Description】

&emsp;&emsp;SVP model attributes.

&emsp;&emsp;【Definition】

```C
	typedef struct akSVP_MODEL_ATTR_S
	{
		SVP_ENV_MODE_E		enEnvMode;			/* Environment mode; not supported by KM02G-series chips */
		SVP_MODEL_E			enModelType;		/* Detection-model type */
		SVP_MODEL_PARAM_S 	stModelParam;		/* Model threshold parameters */
	}SVP_MODEL_ATTR_S;
```

&emsp;&emsp;【Members】

| **Member**     | **Description**  |
| ------------- | ---------------- |
| enEnvMode     | Detection-environment operating mode |
| enModelType   | Target-detection model type |
| stModelParam  | Detection-model threshold parameters |

&emsp;&emsp;【Related API】

```C
	SVP_CHN_ATTR_S structure;
```

<br/>

### SVP_CHN_ATTR_S

&emsp;&emsp;【Description】

&emsp;&emsp;SVP channel attributes.

&emsp;&emsp;【Definition】

```C
	typedef struct akSVP_CHN_ATTR_S
	{
		AK_S32				s32ModelNum;		/* Number of SVP models */
		SVP_MODEL_ATTR_S	astModelAttr[];		/* Model attributes */
	}SVP_CHN_ATTR_S;
```

&emsp;&emsp;【Members】

| **Member**      | **Description** |
| -------------- | ------------ |
| s32ModelNum    | Number of SVP models |
| astModelAttr[] | Model attributes |

&emsp;&emsp;【Related API】

```C
	AK_MPI_SVP_CreateChn();
```

<br/>

### pfnSvpCusReadFunc

&emsp;&emsp;【Description】

&emsp;&emsp;Defines a customizable file-reading method to support a custom AI network.

&emsp;&emsp;【Definition】

```C
	typedef AK_S32 (*pfnSvpCusReadFunc)(AK_VOID *pvDstBuf, AK_S32 s32BufLen, const AK_CHAR *pcPath);
```

&emsp;&emsp;【Members】

| **Member** | **Description** |
| ------------- | ---------------- |
| pvDstBuf      | Address at which data is stored |
| s32BufLen     | File-buffer length |
| pcPath        | Configured model-file path |

&emsp;&emsp;【Related API】

```C
	ak_svp_create_chn();
```

<br/>

### SVP_IMG_TYPE_E

&emsp;&emsp;【Description】

&emsp;&emsp;Input image-data type for detection.

&emsp;&emsp;【Definition】

```C
	typedef enum akSVP_IMG_TYPE_E
	{
        AK_SVP_IMG_YUV420SP = 0,            /* YUV420SP, NV12 */
        AK_SVP_IMG_RGB_LI,                   /*RGB line-interlaced format */
        AK_SVP_IMG_RGB_CHW,                   /*RGB RGB_CHW */
        AK_SVP_IMG_RGB_HWC                    /*RGB RGB_HWC */
	}SVP_IMG_TYPE_E;
```

&emsp;&emsp;【Members】

| **Member**           | **Description**                                         |
| ------------------- | ------------------------------------------------------- |
| AK_SVP_IMG_YUV420SP | NV12, YUV420SP format |
| AK_SVP_IMG_RGB_LI   | RGB line-interlaced format; output by configuring the VI channel type |
| AK_SVP_IMG_RGB_CHW  | RGB_CHW format; output by configuring the VPSS channel type |
| AK_SVP_IMG_RGB_HWC  | RGB_HWC format; output by configuring the VPSS channel type |

&emsp;&emsp;【Related API】

```text
    SVP_IMG_INFO_S structure
```

<br/>

### SVP_POS_INFO_S

&emsp;&emsp;【Description】

&emsp;&emsp;Position information specifying a region of the input image for detection. For full-frame detection, fill in each position field correctly.

&emsp;&emsp;【Definition】

```C
	typedef struct akSVP_POS_INFO_S
	{
        AK_S32 s32Left;
        AK_S32 s32Top;
        AK_S32 s32Width;
        AK_S32 s32Height;
	}SVP_POS_INFO_S;
```

&emsp;&emsp;【Members】

| **Member**     | **Description**                       |
| ------------- | ------------------------------------- |
| s32Left       | Upper-left X coordinate of the specified detection region in the input image |
| s32Top        | Upper-left Y coordinate of the specified detection region in the input image |
| s32Width      | Width of the specified detection region starting at its X coordinate |
| s32Height     | Height of the specified detection region starting at its Y coordinate |

&emsp;&emsp;【Related API】

```text
	SVP_IMG_INFO_S structure
```

<br/>

### SVP_IMG_INFO_S

&emsp;&emsp;【Description】

&emsp;&emsp;Information about the image to detect.

&emsp;&emsp;【Definition】

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

&emsp;&emsp;【Members】

| **Member**     | **Description**              |
| ------------- | ---------------------------- |
| s32ModelIndex | Internal model index |
| enImgType | Data type of the input image |
| s32Width | Input-image resolution width; the value depends on the input image width |
| s32Height | Input-image resolution height; the value depends on the input image height |
| stPosInfo | Position information for region detection in the input image |
| u64PhyAddr | Starting physical address of the input image |
| pvVirAddr | Starting virtual address of the input image |
|&emsp;&emsp;【Related API】||

```C
	AK_MPI_SVP_Process();
```

<br/>

### SVP_RECT_S

&emsp;&emsp;【Description】

&emsp;&emsp;Coordinates of an output human-shape box.

&emsp;&emsp;【Definition】

```C
	typedef struct akSVP_RECT_S	    //coordinate values
	{
        AK_U32 			 enLabel;
        AK_U16           u16Left;       // left_top point, horizontal axis; upper-left x value
        AK_U16           u16Top;        // left_top point, vertical axis; upper-left y value
        AK_U16           u16Right;      // right_bottom point, horizontal axis; lower-right x value
        AK_U16           u16Bottom;     // right_bottom point, vertical axis; lower-right y value
        AK_U32           u32Score;      // Score of the recognized region
	}SVP_RECT_S;
```

&emsp;&emsp;【Members】

| **Member**     | **Description** |
| ------------- | -------------- |
| enLabel       | Coordinate-classification label |
| u16Left       | Upper-left X coordinate |
| u16Top        | Upper-left Y coordinate |
| u16Right      | Lower-right X coordinate |
| u16Bottom     | Lower-right Y coordinate |
| u32Score      | Detection-result score |

&emsp;&emsp;【Related API】

```text
	SVP_HD_RESULT_S structure;
```

<br/>

### SVP_HD_RESULT_S

&emsp;&emsp;【Description】

&emsp;&emsp;Human-shape detection-result output structure.

&emsp;&emsp;【Definition】

```C
	typedef struct akSVP_HD_RESULT_S
	{
        AK_S16 s16ModuleId;
        AK_S16 s16ModuleType;
        AK_S32 s32TotalNum;
        SVP_RECT_S *pstTargetBoxes;        // Coordinate-value array
	}SVP_HD_RESULT_S;
```

&emsp;&emsp;【Members】

| **Member**          | **Description** |
| -------------- | -------- |
| s16ModuleId    | Model ID |
| s16ModuleType  | Model type |
| s32TotalNum    | Number of detected targets output |
| pstTargetBoxes | Detection-box information |

&emsp;&emsp;【Related API】

```C
	SVP_OUTPUT_S();
```

<br/>
### SVP_FAS_RESULT_S

&emsp;&emsp;【Description】

&emsp;&emsp;Liveness-detection-result output structure.

&emsp;&emsp;【Definition】

```C
	typedef struct akSVP_FAS_RESULT_S
	{
        AK_U32 u32Label;
        AK_U32 u32Confidence;
	}SVP_FAS_RESULT_S;
```

&emsp;&emsp;【Members】

| **Member** | **Description** |
| -------------- | -------- |
| u32Label       | Class label |
| u32Confidence  | Class score |

&emsp;&emsp;【Related API】

```C
	SVP_OUTPUT_S();
```

<br/>

### SVP_FR_RESULT_S

&emsp;&emsp;【Description】

&emsp;&emsp;Face-recognition-result output structure.

&emsp;&emsp;【Definition】
```C
	typedef struct akSVP_FR_RESULT_S
	{
        AK_U32  u32DataLen;          //feature len;
        AK_S16 *pcData;            //feature values;
	}SVP_FR_RESULT_S;
```

&emsp;&emsp;【Members】

| **Member**      | **Description** |
| ---------- | ------- |
| u32DataLen | Face-feature length |
| pcData     | Face features |

&emsp;&emsp;【Related API】

```C
	SVP_OUTPUT_S();
```

<br/>

### SVP_GESTURE_RESULT_S

&emsp;&emsp;【Description】

&emsp;&emsp;Gesture-classification-result output structure.

&emsp;&emsp;【Definition】
```C
	typedef struct akSVP_GESTURE_RESULT_S
	{
        AK_U32 u32Label;
        AK_U32 u32Confidence;
	}SVP_GESTURE_RESULT_S;
```

&emsp;&emsp;【Members】

| **Member**         | **Description** |
| ------------- | ------- |
| u32Label      | Gesture class |
| u32Confidence | Gesture score |

&emsp;&emsp;【Related API】

```C
	SVP_OUTPUT_S();
```

<br/>

### FACE_ANGLE__S

&emsp;&emsp;【Description】

&emsp;&emsp;Face-angle-result output structure.

&emsp;&emsp;【Definition】
```C
	typedef struct akFACE_ANGLE_S
	{
        AK_U32 u32Label;
        AK_U32 u32Confidence;
	}FACE_ANGLE_S;
```

&emsp;&emsp;【Members】

| **Member** | **Description** |
| ------------- | ------- |
| u32Label      | Face-angle class |
| u32Confidence | Face-angle score |

&emsp;&emsp;【Related API】

```C
	SVP_OUTPUT_S();
```
<br/>

### SVP_FACE_ANGLE_RESULT_S

&emsp;&emsp;【Description】

&emsp;&emsp;Face-angle-classification-result output structure.

&emsp;&emsp;【Definition】
```C
	typedef struct akSVP_FACE_ANGLE_RESULT_S
	{
        AK_S32 s32TotalNum;
        FACE_ANGLE_S astFaceAngle[CLASSIFY_NUM];
	}SVP_FACE_ANGLE_RESULT_S;
```

&emsp;&emsp;【Members】

| **Member**        | **Description** |
| ------------ | -------- |
| s32TotalNum  | Total number of face-angle classes |
| astFaceAngle | Face-angle information |

&emsp;&emsp;【Related API】

```C
	SVP_OUTPUT_S();
```
<br/>

### SVP_AI_ISP_RESULT_S

&emsp;&emsp;【Description】

&emsp;&emsp;AI ISP output structure.

&emsp;&emsp;【Definition】

```C
	typedef struct akSVP_AI_ISP_RESULT_S
	{
        AK_U8 *u8Data;		/* yuv data */
	}SVP_AI_ISP_RESULT_S;
```

&emsp;&emsp;【Members】

| **Member**     | **Description**    |
| ------------- | ------------------ |
| u8Data        | Pointer to AI ISP output data |

&emsp;&emsp;【Related API】

```C
	SVP_OUTPUT_S();
```

<br/>

### SVP_OUTPUT_S

&emsp;&emsp;【Description】

&emsp;&emsp;Detection-result output structure.

&emsp;&emsp;【Definition】

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

&emsp;&emsp;【Members】

| **Member**         | **Description**     |
| ------------- | ----------------- |
| result        | Shared union of output structures for different types |
| s32ModelType  | Detection-model type |
| s32ModelIndex | Detection-model index |

&emsp;&emsp;【Related API】

```C
	AK_MPI_SVP_Process();
	AK_MPI_SVP_Release();
```

<br/>

### SVP_BUFFER_S

&emsp;&emsp;【Description】

&emsp;&emsp;DMA buffer structure.

&emsp;&emsp;【Definition】

```C
	typedef struct akSVP_BUFFER_S
    {
        AK_VOID		*pvData;		// virtual address of the buffer
        AK_U64      u64Pa;      	// physical address of the buffer
        AK_U32      u32Size;    	// size of the buffer
	}SVP_BUFFER_S;
```

&emsp;&emsp;【Members】

| **Member** | **Description** |
| ------------- | -------------- |
| pvData   | DMA virtual-memory address |
| u64Pa    | DMA physical-memory address |
| u32Size  | DMA memory size |

&emsp;&emsp;【Related API】

```text
	SVP_CONF_INFO_S structure
```

<br/>

### SVP_CONF_INFO_S

&emsp;&emsp;【Description】

&emsp;&emsp;SVP model-parameter structure.

&emsp;&emsp;【Definition】

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

&emsp;&emsp;【Members】

| **Member**     | **Description**                               |
| ------------- | --------------------------------------------- |
| conf_type     | Model parameters |
| s32ConfMode   | Model-parameter type; select either a configuration path or direct DMA-address configuration |
| pfnReadFunc   | Model-reading callback function |

&emsp;&emsp;【Related API】

```C
	AK_MPI_SVP_CreateChn();
```

<br/>

## Get Version Information

###  AK_MPI_SVP_GetVersion

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the version number of the SVP library.

&emsp;&emsp;【Syntax】

```C
	const AK_CHAR* AK_MPI_SVP_GetVersion(AK_VOID);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------- | --------- | ------------- | -------------- |
| AK_VOID       | -         | -             | -              |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ------------- | --------- |
| SVP module version number | Success |
| NULL          | Failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_svp.so or libmpi_svp.a

​		Header: ak_svp.h

<br/>

## Flow Functions

###  AK_MPI_SVP_CreateChn

&emsp;&emsp;【Description】

&emsp;&emsp;Creates an SVP detection channel. Each detection channel corresponds to one handle. KM02G-series chips support at most four open detection channels.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_MPI_SVP_CreateChn(AK_S32 s32HandleId, const SVP_CHN_ATTR_S *pstAttr, SVP_CONF_INFO_S *pstConfInfo);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**  | **Value range** | **Input/Output** |
| ------------- | ---------------- | ------------- | -------------- |
| s32HandleId   | SVP detection-channel handle | [0, 3] | Input |
| pstAttr       | CHN attribute-configuration parameters | See the structure | Input |
| pstConfInfo   | Model-parameter information | See the structure | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description**      |
| ----------- | -------------------- |
| 0           | Success.              |
| Nonzero     | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**            | **Description** |
| ------------------------- | ----------- |
| ERROR_SVP_HANDLE_ID_ERROR | Invalid SVP handle |
| ERROR_TYPE_INVALID_ARG    | Invalid argument |
| ERROR_TYPE_NOT_INIT       | SVP is not initialized |

【Requirements】

&emsp;&emsp;Libraries: libmpi_svp.so or libmpi_svp.a

&emsp;&emsp;Header: ak_svp.h

> **Notes:**
>
Each channel ID can be created only once with `AK_MPI_SVP_CreateChn()`. Creating the same CHN ID multiple times causes an error.
>
KM02G-series chips do not currently support custom networks.
>
> Paired function: `AK_MPI_SVP_DestroyChn()`

&emsp;&emsp;【Call order】

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

&emsp;&emsp;【Description】

&emsp;&emsp;Closes a detection channel.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_MPI_SVP_DestroyChn(AK_S32 s32HandleId);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------- | ---------------- | ------------- | -------------- |
| s32HandleId | SVP detection-channel handle | [0, 3] | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ----------- | -------------------- |
| 0 | Success. |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code** | **Description** |
| ------------------------- | ----------- |
| ERROR_SVP_HANDLE_ID_ERROR | Invalid SVP handle |
| ERROR_TYPE_NOT_INIT | SVP is not initialized |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_svp.so or libmpi_svp.a

&emsp;&emsp;Header: ak_svp.h

> **Note:** Use together with `AK_MPI_SVP_CreateChn()`.

&emsp;&emsp;【Call order】

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

&emsp;&emsp;【Description】

&emsp;&emsp;Starts image detection.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_MPI_SVP_Process(AK_S32 s32HandleId,  SVP_IMG_INFO_S *pstInput,  SVP_OUTPUT_S *pstOutput);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**        | **Value range**          | **Input/Output** |
| ------------- | ---------------------- | ------------------------ | -------------- |
| s32HandleId   | SVP detection-channel handle | [0, 3] | Input |
| pstInput      | Pointer to information about the image to detect | See `SVP_IMG_INFO_S` | Input |
| pstOutput     | Data pointer for the output detection result | See `SVP_OUTPUT_S` | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ----------- | -------------------- |
| 0 | Success. |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code** | **Description** |
| ------------------------- | ----------- |
| ERROR_TYPE_INVALID_ARG    | Invalid argument |
| ERROR_SVP_HANDLE_ID_ERROR | Invalid SVP handle |
| ERROR_TYPE_NOT_INIT | SVP is not initialized |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_svp.so or libmpi_svp.a

&emsp;&emsp;Header: ak_svp.h

> **Notes:**
>
Call after `AK_MPI_SVP_CreateChn()`.
>
The SVP module is most efficient and imposes the lowest CPU load when it performs full-frame detection on an input image whose resolution matches the SVP requirement and whose data type is RGB_HWC. When region detection is required, or when the input resolution or data format is not RGB_HWC, the CPU must perform additional data processing before image recognition, which affects overall system efficiency and CPU load.
>
Paired function: `AK_MPI_SVP_Release()`.
>

&emsp;&emsp;【Call order】

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

&emsp;&emsp;【Description】

&emsp;&emsp;Releases the output coordinate data.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_MPI_SVP_Release(SVP_OUTPUT_S *pstOutput);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**            | **Value range** | **Input/Output** |
| ------------- | -------------------------- | ------------- | -------------- |
| pstOutput     | Unreleased output coordinate data obtained from detection | - | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ----------- | -------------------- |
| 0 | Success. |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**          | **Description** |
| ----------------------- | ------------ |
| ERROR_TYPE_POINTER_NULL | Null argument pointer |
| ERROR_TYPE_NOT_INIT     | SVP is not initialized |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_svp.so or libmpi_svp.a

&emsp;&emsp;Header: ak_svp.h

> **Note:** Use together with `AK_MPI_SVP_Process()`.

&emsp;&emsp;【Call order】

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

## Set/Get Attribute Functions

### AK_MPI_SVP_GetRaram

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the threshold parameters for a model on a channel.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_MPI_SVP_GetRaram(AK_S32 s32HandleId, SVP_MODEL_PARAM_S *stModelParam);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**  | **Value range**             | **Input/Output** |
| ------------- | ---------------- | --------------------------- | -------------- |
| s32HandleId   | SVP detection-channel handle | [0, 3]] | Input |
| stModelParam  | Receives the threshold parameters | See `SVP_MODEL_PARAM_S` | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ----------- | -------------------- |
| 0 | Success. |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                 | **Description**            |
| ------------------------------ | -------------------------- |
| ERROR_SVP_HANDLE_ID_ERROR      | Invalid SVP handle |
| ERROR_TYPE_POINTER_NULL        | Argument pointer is NULL |
| ERROR_TYPE_NOT_INIT            | SVP is not initialized |
| ERROR_SVP_HANDLE_ERROR         | Invalid handle corresponding to the channel |
| ERROR_SVP_HANDLE_ID_NOT_CREATE | HANDLE_ID has not been created |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_svp.so or libmpi_svp.a

&emsp;&emsp;Header: ak_svp.h

> **Note:** Call after `AK_MPI_SVP_CreateChn()`.

&emsp;&emsp;【Call order】

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

&emsp;&emsp;【Description】

&emsp;&emsp;Sets the model thresholds for a channel.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_MPI_SVP_SetParam(AK_S32 s32HandleId, SVP_MODEL_PARAM_S stModelParam);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range**             | **Input/Output** |
| ------------- | --------------- | --------------------------- | -------------- |
| s32HandleId   | SVP detection-channel handle | [0, 3] | Input |
| stModelParam  | Threshold-parameter settings | See `SVP_MODEL_PARAM_S` | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ----------- | -------------------- |
| 0 | Success. |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                   | **Description**            |
| -------------------------------- | -------------------------- |
| ERROR_SVP_HANDLE_ID_ERROR        | Invalid SVP handle |
| ERROR_TYPE_INVALID_ARG           | Invalid argument |
| ERROR_TYPE_NOT_INIT              | SVP is not initialized |
| ERROR_SVP_SET_IOU_THRESHOLD      | Failed to set `IoU_threshold` |
| ERROR_SVP_SET_CLASSIFY_THRESHOLD | Failed to set `classify_threshold` |
| ERROR_SVP_HANDLE_ERROR           | Invalid handle corresponding to the channel |
| ERROR_SVP_HANDLE_ID_NOT_CREATE   | HANDLE_ID has not been created |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_svp.so or libmpi_svp.a

&emsp;&emsp;Header: ak_svp.h

> **Note:** Call after `AK_MPI_SVP_CreateChn()`.

&emsp;&emsp;【Call order】

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

## API Call Dependencies

| **API**                | API dependency                                     |
| --------------------- | -------------------------------------------------- |
| AK_MPI_SVP_GetVersion | May be called at any time |
| Other APIs            | After AK_MPI_NPU_Init |
| AK_MPI_SVP_GetRaram   | After AK_MPI_SVP_CreateChn and before AK_MPI_SVP_DestroyChn |
| AK_MPI_SVP_SetRaram   | After AK_MPI_SVP_CreateChn and before AK_MPI_SVP_DestroyChn |
| AK_MPI_SVP_Process    | After AK_MPI_SVP_CreateChn and before AK_MPI_SVP_DestroyChn |

> **Source note:** The source dependency row spells the setter `AK_MPI_SVP_SetRaram`; the documented API and supplied header name it `AK_MPI_SVP_SetParam`. The dependency shown for that source row applies to `AK_MPI_SVP_SetParam`.

&emsp;&emsp;【Call order】

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

## SVP Sample

Before running the demo, load these drivers: `firmware_class.ko`, `ak_npu.ko`, `ak_vi.ko`, `sensor_xxx.ko`, `ak_vicap.ko`, `ak_isp.ko`, and `ak_pp.ko`. For a GC5603 CIS, see `gc5603.sh`; the commands are:

​        insmod /usr/modules/ak_vi.ko

​        insmod /usr/modules/sensor_gc5603.ko

​        insmod /usr/modules/ak_vicap.ko

​        insmod /usr/modules/ak_isp.ko

​        insmod /usr/modules/ak_pp.ko

​        For another CIS, see its corresponding `xxx.sh` loading script.

> **Note:** When loading `firmware_class.ko`, supply the `path=/mnt` parameter. `/mnt` is the path containing the ELF model and may be customized.

​       insmod /lib/modules/5.10.111/kernel/drivers/base/firmware_loader/firmware_class.ko path=/mnt

​       insmod /usr/modules/ak_npu.ko

| **Input parameter** | **Description**                                |
| ------------------ | ----------------------------------------------- |
| help               | Help information |
| grp_index          | VPSS Group number |
| chn_index          | VPSS channel number |
| frame_cnt          | Number of frames to capture [0, 2^31 -1] |
| grep_res_index     | VPSS Group resolution; the value depends on the sensor |
| chn_res_index      | VPSS channel resolution required by the model input |
| chn_framerate      | VPSS channel frame rate |
| chn_crop_x         | Starting X coordinate for channel cropping |
| chn_crop_y         | Starting Y coordinate for channel cropping |
| chn_crop_w         | Channel crop width |
| chn_crop_h         | Channel crop height |
| isp_config_path    | ISP configuration-file path; empty by default and must be specified |
| frame_save_path    | Path in which RGB images are saved |
| elf_path           | ELF model-file path |
| data_type          | Format of images captured and supplied to SVP: 0:RGB_HWC, 1:RGB_CHW |
| svp_rate           | Interval, in frames, between SVP detections |
| classify_threshold | Classification-confidence threshold [0, 1000] |
| iou_threshold      | IoU filtering threshold [0, 10] |
| filter_enable      | Whether to enable human-shape filtering: 0:disable, 1:md, 2:md+filter |

<br/>

&emsp;&emsp;Output: prints each detected target's label, score, and box coordinates.

## /var/platform Description

After running the application on the board, execute the following command to obtain the versions and parameter settings of the libraries used by the current application:

```shell
cat /var/platform/SVP/stat
# "nna_version":  "libak_nna V1.0.05",		NNA library version
# "nne_version":  "libak_nne V1.0.05",		NNE library version
# "svp_version":  "libmpi_svp V1.0.12"		SVP library version
```

```shell
cat /var/platform/SVP/param
# "chn0_id":      "0",						SVP handle id
# "chn0_param_path":      "yolov5n_640",	SVP model name
# "chn0_env_mode":        "0",				SVP day/night mode; not currently supported (0: day, 1: night)
# "chn0_model_type":      "2"				SVP model type (1: 480 human-shape/face model, 2: 480 pet model, 3: 640 model)
```

<br/>

## Error Codes

| Error code | Macro                          | Meaning                    |
| ---------- | ------------------------------ | -------------------------- |
| 0x28000000 | ERROR_SVP_ALREADY_OPEN         | SVP is already open |
| 0x28000001 | ERROR_SVP_HANDLE_ID_ERROR      | Invalid handle_id |
| 0x28000002 | ERROR_SVP_HANDLE_ERROR         | Invalid handle corresponding to the channel |
| 0x28000003 | ERROR_SVP_NOT_CREATE           | SVP has not been created |
| 0x28000004 | ERROR_SVP_SET_PARAM            | Failed to set parameters |
| 0x28000005 | ERROR_SVP_GET_PARAM            | Failed to get parameters |
| 0x28000006 | ERROR_SVP_ALREADY_INIT         | SVP is already initialized |
| 0x28000007 | ERROR_SVP_ALREADY_DEINIT       | SVP is already destroyed |
| 0x28000008 | ERROR_SVP_HANDLE_ID_NOT_CREATE | handle_id was not created successfully |
| 0x28000009 | ERROR_TYPE_DMA_MALLOC_FAILED   | Failed to allocate DMA memory |
| 0x2800000a | ERROR_SVP_GET_DMA_FD_FAILED    | Failed to get the DMA handle |

<br/>
