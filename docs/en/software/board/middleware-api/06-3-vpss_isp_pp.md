# Video Processing Subsystem (Image Effects)

## Overview

&emsp;&emsp;The image-effects portion of the video processing subsystem provides two main groups of functions:

&emsp;&emsp;1. Basic ISP operations, including exposure, white balance, focus, and 3DNR settings.

&emsp;&emsp;2. Advanced image-processing functions, including OSD, MD, effects, masks, and drawing.

<br/>

## API Reference

&emsp;&emsp;This module provides the following APIs:

| **Library interface**                 | **Description**             |
| ---------------------------------- | ------------------------- |
| ISP_MD_INFO_S                      | MD parameter structure |
| ISP_OD_INFO_S                      | OD parameter structure |
| ISP_EFFECT_TYPE_E                  | Effect-type enumeration |
| PP_MASK_TYPE_E                     | Privacy-mask type |
| PP_MASK_MASIC_ATTR_S               | Mosaic-block size |
| PP_MASK_COLOR_INFO_S               | Privacy-mask color-parameter structure |
| PP_RECTANGLE_AREA_S                | Rectangular-area parameter structure |
| PP_TRIANGLE_AREA_S                 | Triangular/diamond-area parameter structure |
| PP_MASK_AREA_S                     | Single privacy-mask area parameter structure |
| PP_MASK_AREA_INFO_S                | Privacy-mask area parameter structure |
| PP_SHAPE_TYPE_E                    | Shape type |
| PP_BOX_S                           | Single draw-box area parameter structure |
| PP_BOX_GROUP_S                     | Draw-box parameter structure |
| ISP_AF_ATTR_S                      | Autofocus information structure |
| ISP_AF_INFO_S                      | Autofocus statistics structure |
| ISP_OP_TYPE_E                      | Automatic/manual type |
| ISP_AE_EX_CONVER_ATTR_S            | External automatic-exposure convergence-control attributes |
| ISP_AE_STRGY_MODEL_E               | Automatic-exposure strategy mode |
| ISP_RAW_G_HIST_ATTR_S              | RAW-domain histogram structure |
| ISP_RGB_HIST_ATTR_S                | RGB-domain histogram structure |
| ISP_YUV_HIST_ATTR_S                | YUV-domain histogram structure |
| ISP_AE_STRGY_ATTR_S                | Automatic-exposure strategy attributes |
| ISP_AE_ROUTE_NODE_ATTR_S           | Automatic-exposure allocation-route node attributes |
| ISP_AE_ROUTE_ATTR_S                | Automatic-exposure allocation-route attributes |
| ISP_WDR_AE_ATTR_S                  | WDR automatic-exposure structure |
| ISP_AE_ATTR_S                      | Automatic-exposure parameter structure |
| ISP_ME_ATTR_S                      | Manual-exposure parameter structure |
| ISP_RAW_HIST_STAT_INFO_S           | RAW-domain histogram statistics |
| ISP_RGB_HIST_STAT_INFO_S           | RGB-domain histogram statistics |
| ISP_YUV_HIST_STAT_INFO_S           | YUV-domain histogram statistics |
| ISP_WDR_HIST_STAT_INFO_S           | Long/short-frame histogram statistics |
| ISP_AE_STAT_INFO_S                 | Automatic-exposure status information |
| ISP_AE_RUN_INFO_S                  | Automatic-exposure runtime-information structure |
| ISP_AWB_BLK_AVG_STAT_INFO_S        | Per-region RGB-channel average statistics |
| ISP_AWB_BLK_WP_STAT_INFO_S         | Per-region RGB-channel white-point average statistics |
| ISP_AWB_RUN_INFO_S                 | White-balance runtime-information structure |
| ISP_AWB_STAT_INFO_S                | White-balance statistics structure |
| ISP_MWB_ATTR_S                     | Manual white-balance parameter structure |
| ISP_AWB_ALGO_TYPE_E                | Automatic white-balance algorithm type |
| ISP_AWB_STAT_CALIB_PARA_S          | Automatic white-balance statistics parameters |
| ISP_AWB_ATTR_S                     | Automatic white-balance parameter structure |
| ISP_HDR_S                          | WDR information |
| ISP_HDR_ATTR_S                     | WDR information structure |
| ISP_GAIN_STAT_E                    | Gain status |
| ISP_FPS_LEVEL_S                    | Three-level frame-rate structure |
| ISP_3DNR_S                         | 3D noise-reduction information structure |
| ISP_3DNR_ATTR_S                    | 3D noise-reduction attribute structure |
| ISP_LENS_COEF_S                    | Coefficient structure |
| ISP_LSC_ATTR_S                     | Lens-shading-correction information structure |
| ISP_SENSOR_REG_INFO_S              | Sensor-register information structure |
| ISP_EX_ZWEIGHT_ATTR_S              | Extended-area weight structure |
| ISP_EFFECT_ATTR_S                  | YUV-effect structure |
| ISP_RGB_GAMMA_S                    | RGB gamma-curve structure |
| ISP_RGB_GAMMA_ATTR_S               | RGB gamma-parameter structure |
| ISP_CONTRAST_S                     | Manual-contrast parameter structure |
| ISP_AUTO_CONTRAST_S                | Automatic-contrast parameter structure |
| ISP_CONTRAST_ATTR_S                | Contrast-parameter structure |
| ISP_LCE_S                          | Local-contrast-enhancement parameters |
| ISP_LCE_ATTR_S                     | Local-contrast-enhancement parameter structure |
| ISP_Y_GAMMA_ATTR_S                 | Y-gamma parameter structure |
| ISP_DAY_NIGHT_MODE_E               | Day/night mode |
| ISP_NIGHT_TYPE_E                   | Night-vision type |
| ISP_IR_LED_NIGHT_PARAM_S           | IR night-vision software-photosensitivity parameters |
| ISP_WHITE_LED_NIGHT_PARAM_S        | White-light night-vision software-photosensitivity parameters |
| ISP_BLACKLIGHT_NIGHT_PARAM_S       | Black-light color-night-vision software-photosensitivity parameters |
| ISP_SOFT_PS_ATTR_S                 | Software-photosensitivity parameter structure |
| ISP_NON_INFRARED_RATIO_ATTR_S      | Parameters for calculating the non-infrared-block ratio |
| ISP_3D_NR_REF_SIZE_STAT_INFO       | 3DNR buffer-usage statistics structure |
| AK_MPI_ISP_GetIspSdkVersion        | Gets the ISP SDK library version |
| AK_MPI_ISP_GetOdInfo               | Gets data required by OD |
| AK_MPI_ISP_GetMdStat               | Gets MD statistics |
| AK_MPI_ISP_SetEffect               | Sets an effect |
| AK_MPI_ISP_GetEffect               | Gets an effect |
| AK_MPI_PP_MaskSetArea              | Sets a mask area |
| AK_MPI_PP_MaskGetArea              | Gets a mask area |
| AK_MPI_PP_MaskSetColor             | Sets the mask color |
| AK_MPI_PP_MaskGetColor             | Gets the mask color |
| AK_MPI_PP_SetBoxColorTable         | Sets the box-drawing palette |
| AK_MPI_PP_DrawBox                  | Sets box-drawing parameters |
| AK_MPI_ISP_SetAfAttr               | Sets the autofocus structure |
| AK_MPI_ISP_GetAfAttr               | Gets the autofocus structure |
| AK_MPI_ISP_GetAfStat               | Gets autofocus statistics |
| AK_MPI_ISP_GetExpType              | Gets exposure-type information |
| AK_MPI_ISP_SetExpType              | Sets exposure-type information |
| AK_MPI_ISP_GetAeRunInfo            | Gets automatic-exposure statistics |
| AK_MPI_ISP_GetAeAttr               | Gets automatic-exposure structure information |
| AK_MPI_ISP_SetAeAttr               | Sets automatic-exposure structure information |
| AK_MPI_ISP_GetAeConvergenceRate    | Gets the automatic-exposure convergence rate |
| AK_MPI_ISP_SetAeConvergenceRate    | Sets the automatic-exposure convergence rate |
| AK_MPI_ISP_CheckAeStable           | Checks whether automatic exposure is stable |
| AK_MPI_ISP_SetAeSuspend            | Suspends/resumes AE |
| AK_MPI_ISP_GetMeAttr               | Gets manual-exposure structure information |
| AK_MPI_ISP_SetMeAttr               | Sets manual-exposure structure information |
| AK_MPI_ISP_GetExZweightAttr        | Gets extended weight-coefficient information |
| AK_MPI_ISP_SetExZweightAttr        | Sets extended weight-coefficient information |
| AK_MPI_ISP_GetAwbStatInfo          | Gets white-balance statistics |
| AK_MPI_ISP_GetWbType               | Gets white-balance type information |
| AK_MPI_ISP_SetWbType               | Sets white-balance type information |
| AK_MPI_ISP_GetMwbAttr              | Gets manual white-balance structure information |
| AK_MPI_ISP_SetMwbAttr              | Sets manual white-balance structure information |
| AK_MPI_ISP_GetAwbAttr              | Gets automatic white-balance structure information |
| AK_MPI_ISP_SetAwbAttr              | Sets automatic white-balance structure information |
| AK_MPI_ISP_GetHdrAttr              | Gets WDR parameters |
| AK_MPI_ISP_SetHdrAttr              | Sets WDR parameters |
| AK_MPI_ISP_SetSoftPsParam          | Sets day/night switching parameters without a photosensor |
| AK_MPI_ISP_GetSoftPsLevel          | Gets the day/night level without a photosensor |
| AK_MPI_ISP_SwitchMode              | Switches day/night mode |
| AK_MPI_ISP_GetFpsCtrlStat          | Gets the frame-rate control status |
| AK_MPI_ISP_ChangeSensorFps         | Switches the sensor frame rate |
| AK_MPI_ISP_SetFpsLevel             | Sets the sensor's three frame-rate levels |
| AK_MPI_ISP_GetFpsLevel             | Gets the sensor's three frame-rate levels |
| AK_MPI_ISP_SetSensorFps            | Sets the sensor frame rate |
| AK_MPI_ISP_GetSensorFps            | Gets the sensor frame rate |
| AK_MPI_ISP_Get3dnrAttr             | Gets the 3DNR structure |
| AK_MPI_ISP_Set3dnrAttr             | Sets the 3DNR structure |
| AK_MPI_ISP_GetLscAttr              | Gets lens-shading-correction structure information |
| AK_MPI_ISP_SetLscAttr              | Sets lens-shading-correction structure information |
| AK_MPI_ISP_GetYuvEffectAttr        | Gets YUV-effect structure information |
| AK_MPI_ISP_SetYuvEffectAttr        | Sets YUV-effect structure information |
| AK_MPI_ISP_GetRgbGammaAttr         | Gets RGB-gamma structure information |
| AK_MPI_ISP_SetRgbGammaAttr         | Sets RGB-gamma structure information |
| AK_MPI_ISP_GetYgammaAttr           | Gets Y-gamma structure information |
| AK_MPI_ISP_SetYgammaAttr           | Sets Y-gamma structure information |
| AK_MPI_ISP_GetContrastAttr         | Gets contrast-structure information |
| AK_MPI_ISP_SetContrastAttr         | Sets contrast-structure information |
| AK_MPI_ISP_GetLceAttr              | Gets local-contrast-enhancement structure information |
| AK_MPI_ISP_SetLceAttr              | Sets local-contrast-enhancement structure information |
| AK_MPI_ISP_GetCurLumi              | Gets luminance |
| AK_MPI_ISP_SetForceAntiFlickerFlag | Sets the forced anti-flicker flag |
| AK_MPI_ISP_GetForceAntiFlickerFlag | Gets the forced anti-flicker flag |
| AK_MPI_ISP_SetAntiFlickerStrength  | Sets anti-flicker strength |
| AK_MPI_ISP_GetAntiFlickerStrength  | Gets anti-flicker strength |
| AK_MPI_ISP_GetRgbAverage           | Gets RGB averages |
| AK_MPI_ISP_GetSensorReg            | Gets a sensor-register value |
| AK_MPI_ISP_SwitchFlipMirror        | Sets flip/mirror relative to the initial ISP-configuration-file values |
| AK_MPI_ISP_GetFlipMirror           | Gets flip/mirror status relative to the initial ISP-configuration-file values |
| AK_MPI_ISP_WaitExpStable           | Waits for exposure to stabilize |
| AK_MPI_ISP_GetEv                   | Gets the ambient EV value |
| AK_MPI_ISP_GetRgbDis               | Gets the RGB difference value |
| AK_MPI_ISP_GetNonInfraredRatio     | Gets the percentage of valid blocks that are non-infrared |
| AK_MPI_ISP_Get3dnrRefSizeStat      | Gets 3DNR buffer-usage statistics |

<br/>

## Data Structures

### **ISP_MD_INFO_S**

&emsp;&emsp;【Description】

&emsp;&emsp;MD parameter structure.

&emsp;&emsp;【Definition】

```c
typedef struct akISP_MD_INFO_S {
    AK_U16  u16Stat[ISP_MD_DIMENSION_V_MAX][ISP_MD_DIMENSION_H_MAX];
} ISP_MD_INFO_S;
```

&emsp;&emsp;【Members】

| **Member**   | **Description**                                |
| -------- | ------------------------------------------- |
| u16Stat  | Motion-information statistics. The full frame is divided into 64\*36 blocks, and the difference between the current and previous frames is calculated for each block. |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_ISP_GetMdStat(AK_S32 s32GrpId, ISP_MD_INFO_S *pstMd);
```

<br/>

### **ISP_OD_INFO_S**

&emsp;&emsp;【Description】

&emsp;&emsp;OD parameter structure.

&emsp;&emsp;【Definition】

```c
typedef struct akISP_OD_INFO_S {
    AK_U32   u32AfStatics[8][16][5];
    AK_U32   u32RgbHist[256];
    AK_U64   u64RgbTotal;
} ISP_OD_INFO_S;
```

&emsp;&emsp;【Members】

| **Member**       | **Description** |
| ------------ | -------- |
| u32AfStatics | Autofocus statistics |
| u32RgbHist   | RGB histogram information |
| u64RgbTotal  | RGB statistics |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_ISP_GetOdInfo(AK_S32 s32GrpId, ISP_OD_INFO_S *pstOd);
```

<br/>

### **ISP_EFFECT_TYPE_E**

&emsp;&emsp;【Description】

&emsp;&emsp;Effect-type enumeration.

&emsp;&emsp;【Definition】

```c
typedef enum akISP_EFFECT_TYPE_E {
    /* HUE to WDR, value: [-50, 50], 0 means use the value in ISP config file */
    ISP_EFFECT_HUE = 0x00,
    ISP_EFFECT_BRIGHTNESS,
    ISP_EFFECT_SATURATION,
    ISP_EFFECT_CONTRAST,
    ISP_EFFECT_SHARP,
    ISP_EFFECT_HDR,

    ISP_POWER_HZ,        //50 or 60
    ISP_FLIP_MIRROR    //[0, 3]
} ISP_EFFECT_TYPE_E;
```

&emsp;&emsp;【Members】

| **Member**                | **Description**                                                              |
| --------------------- | ------------------------------------------------------------------------- |
| ISP_EFFECT_HUE        | Hue, [-50,50]; 0 uses the ISP-configuration-file value |
| ISP_EFFECT_BRIGHTNESS | Brightness, [-50,50]; 0 uses the ISP-configuration-file value. Depending on the target luminance in the active ISP configuration, the effective lower limit may not reach -50. |
| ISP_EFFECT_SATURATION | Saturation, [-50,50]; 0 uses the ISP-configuration-file value |
| ISP_EFFECT_CONTRAST   | Contrast, [-50,50]; 0 uses the ISP-configuration-file value |
| ISP_EFFECT_SHARP      | Sharpness, [-50,50]; 0 uses the ISP-configuration-file value |
| ISP_EFFECT_HDR        | WDR, [-50,50]; 0 uses the ISP-configuration-file value |
| ISP_POWER_HZ          | Power frequency, 50 or 60 |
| ISP_FLIP_MIRROR       | Flip/mirror: 0 normal, 1 flip only, 2 mirror only, 3 both flip and mirror |

&emsp;&emsp;【Related data types and function interfaces】

```c
    AK_S32 AK_MPI_ISP_SetEffect(AK_S32 s32GrpId, ISP_EFFECT_TYPE_E enType, AK_S32 s32Value);
    AK_S32 AK_MPI_ISP_GetEffect(AK_S32 s32GrpId, ISP_EFFECT_TYPE_E enType, AK_S32 *ps32Value);
```

<br/>

### **PP_MASK_TYPE_E**

&emsp;&emsp;【Description】

&emsp;&emsp;Privacy-mask type.

&emsp;&emsp;【Definition】

```c
typedef enum akPP_MASK_TYPE_E {
    PP_MASK_ORIGINAL_COLOR_RECTANGLE = 0,    /* masked with original color rectangle */
    PP_MASK_ORIGINAL_COLOR_TRIANGLE,        /* masked with original color triangle or diamond*/
    PP_MASK_MOSAIC_VIDEO_RECTANGLE,         /* masked with mosaic video data */
} PP_MASK_TYPE_E;
```

&emsp;&emsp;【Members】

| **Member**                           | **Description** |
| -------------------------------- | -------- |
| PP_MASK_ORIGINAL_COLOR_RECTANGLE | Solid-color rectangle |
| PP_MASK_ORIGINAL_COLOR_TRIANGLE  | Solid-color triangle/diamond |
| PP_MASK_MOSAIC_VIDEO_RECTANGLE   | Mosaic rectangle |

&emsp;&emsp;【Related data types and function interfaces】

&emsp;&emsp;PP_MASK_AREA_S

<br/>

### **PP_MASK_MASIC_ATTR_S**

&emsp;&emsp;【Description】

&emsp;&emsp;Mosaic-block size.

&emsp;&emsp;【Definition】

```c
typedef struct akPP_MASK_MASIC_ATTR_S{
    AK_U16    u16MosaiSizeHor;
    AK_U16    u16MosaiSizeVec;
} PP_MASK_MASIC_ATTR_S;
```

&emsp;&emsp;【Members】

| **Member**          | **Description**                                  |
| --------------- | --------------------------------------------- |
| u16MosaiSizeHor | Horizontal mosaic-block width, [0,7]: 0 means 1 pixel, 1 means 2 pixels, ..., and 7 means 128 pixels |
| u16MosaiSizeVec | Vertical mosaic-block width; reserved and not yet implemented |

&emsp;&emsp;【Related data types and function interfaces】

&emsp;&emsp;PP_MASK_COLOR_INFO_S

<br/>

### **PP_MASK_COLOR_INFO_S**

&emsp;&emsp;【Description】

&emsp;&emsp;Privacy-mask color-parameter structure.

&emsp;&emsp;【Definition】

```c
typedef struct akPP_MASK_COLOR_INFO_S {
    /* range [0, 0xff]. if 0xff mask video opaquely, then can not see image */
    AK_U8 u8Alpha;

    /* range [0, 0xff] */
    AK_U8 u8RColor;
    /* range [0, 0xff] */
    AK_U8 u8GColor;
    /* range [0, 0xff] */
    AK_U8 u8BColor;

    PP_MASK_MASIC_ATTR_S stMasicAttr;
} PP_MASK_COLOR_INFO_S;
```

&emsp;&emsp;【Members】

| **Member**      | **Description**                         |
| ----------- | ------------------------------------ |
| u8Alpha     | Mask opacity, range [0,0xff]; 255 fully masks the image |
| u8RColor    | Red component, range [0,0xff] |
| u8GColor    | Green component, range [0,0xff] |
| u8BColor    | Blue component, range [0,0xff] |
| stMasicAttr | Mosaic-block size |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_PP_MaskSetColor(AK_S32 s32GrpId, const PP_MASK_COLOR_INFO_S *pstColor);
    AK_S32 AK_MPI_PP_MaskGetColor(AK_S32 s32GrpId, PP_MASK_COLOR_INFO_S *pstColor);
```

<br/>

### **PP_RECTANGLE_AREA_S**

&emsp;&emsp;【Description】

&emsp;&emsp;Rectangular-area parameter structure.

【Definition】

```c
typedef struct akPP_RECTANGLE_AREA_S {
    AK_U16 u16X;
    AK_U16 u16Y;
    AK_U16 u16Width;
    AK_U16 u16Height;
} PP_RECTANGLE_AREA_S;
```

&emsp;&emsp;【Members】

| **Member**    | **Description** |
| --------- | ------ |
| u16X      | Upper-left X coordinate |
| u16Y      | Upper-left Y coordinate |
| u16Width  | Rectangle width |
| u16Height | Rectangle height |

&emsp;&emsp;【Related function interface】

&emsp;&emsp;PP_MASK_AREA_S

<br/>

### **PP_TRIANGLE_AREA_S**

&emsp;&emsp;【Description】

&emsp;&emsp;Triangular/diamond-area parameter structure.

【Definition】

```c
typedef struct akPP_TRIANGLE_AREA_S {
    AK_U16 u16X;
    AK_U16 u16Y;
    AK_U8  u8HalfWidth;
    AK_U8  u8Bitmap;
} PP_TRIANGLE_AREA_S;
```

&emsp;&emsp;【Members】

| **Member**      | **Description**                                                 |
| ----------- | ------------------------------------------------------------ |
| u16X        | X coordinate of the diamond center |
| u16Y        | Y coordinate of the diamond center |
| u8HalfWidth | Half the diamond diagonal length |
| u8Bitmap    | Diamond-subregion enable bitmap, [0,15]: bit 0 upper-left triangle, bit 1 upper-right, bit 2 lower-left, bit 3 lower-right |

&emsp;&emsp;【Related function interface】

&emsp;&emsp;PP_MASK_AREA_S

<br/>

### **PP_MASK_AREA_S**

&emsp;&emsp;【Description】

&emsp;&emsp;Single privacy-mask area parameter structure.

【Definition】

```c
typedef struct akPP_MASK_AREA_S {
    AK_U8                   u8Enable;
    PP_MASK_TYPE_E          enType;
    union
    {
        PP_RECTANGLE_AREA_S stRectangleArea;
        PP_TRIANGLE_AREA_S  stTriangleArea;
    };
} PP_MASK_AREA_S;
```

&emsp;&emsp;【Members】

| **Member**          | **Description** |
| --------------- | -------- |
| u8Enable        | Region enable |
| enType          | Region type |
| stRectangleArea | Rectangle parameters |
| stTriangleArea  | Triangle/diamond parameters |

&emsp;&emsp;【Related function interface】

&emsp;&emsp;PP_MASK_AREA_INFO_S

<br/>

### **PP_MASK_AREA_INFO_S**

&emsp;&emsp;【Description】

&emsp;&emsp;Privacy-mask area parameter structure.

&emsp;&emsp;【Definition】

```c
typedef struct akPP_MASK_AREA_INFO_S {
    PP_MASK_AREA_S stArea[PP_MASK_AREA_MAX];
    AK_U8          u8SyncToSubChn;
} PP_MASK_AREA_INFO_S;
```

&emsp;&emsp;【Members】

| **Member**         | **Description**        |
| -------------- | ------------------- |
| stArea         | Channel-area structure |
| u8SyncToSubChn | Whether to synchronize to the secondary channel: 0 no, 1 yes |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_PP_MaskSetArea(AK_S32 s32GrpId, AK_U32 u32ChnId, const PP_MASK_AREA_INFO_S *pstArea);
    AK_S32 AK_MPI_PP_MaskGetArea(AK_S32 s32GrpId, AK_U32 u32ChnId, PP_MASK_AREA_INFO_S *pstArea);
```

<br/>

### **PP_SHAPE_TYPE_E**

&emsp;&emsp;【Description】

&emsp;&emsp;Shape type.

&emsp;&emsp;【Definition】

```c
typedef enum akPP_SHAPE_TYPE_E {
    PP_SHAPE_TYPE_RECTANGLE_HOLLOW = 0,        /* rectangle hollow */
    PP_SHAPE_TYPE_RECTANGLE_SOLID,            /* rectangle solid */
    PP_SHAPE_TYPE_TRIANGLE_HOLLOW,            /* triangle or diamond hollow */
    PP_SHAPE_TYPE_TRIANGLE_SOLID,            /* triangle or diamond solid */
} PP_SHAPE_TYPE_E;
```

&emsp;&emsp;【Members】

| **Member**                         | **Description** |
| ------------------------------ | ---------- |
| PP_SHAPE_TYPE_RECTANGLE_HOLLOW | Hollow rectangle |
| PP_SHAPE_TYPE_RECTANGLE_SOLID  | Solid rectangle |
| PP_SHAPE_TYPE_TRIANGLE_HOLLOW  | Hollow diamond/triangle diagonal |
| PP_SHAPE_TYPE_TRIANGLE_SOLID   | Solid diamond/triangle |

&emsp;&emsp;【Related data types and function interfaces】

&emsp;&emsp;PP_BOX_S

<br/>

### **PP_BOX_S**

&emsp;&emsp;【Description】

&emsp;&emsp;Single draw-box area parameter structure.

【Definition】

```c
typedef struct akPP_BOX_S {
    AK_U8                   u8Enable;       //[0-1]
    PP_SHAPE_TYPE_E         enType;          //0 rectangle; 1 triangle or diamond
    AK_U16                  u16ColorId;    //[0-6]
    AK_U16                  u16LineWidth;  //[1-16]

    // -1 draw forever ; 0 not draw; >0 draw frame num
    AK_S32                  s32DrawFrameNum;

    union
    {
        PP_RECTANGLE_AREA_S stRectangleArea;
        PP_TRIANGLE_AREA_S  stTriangleArea;
    };
} PP_BOX_S;
```

&emsp;&emsp;【Members】

| **Member**          | **Description**             |
| --------------- | ------------------------ |
| u8Enable        | Region enable |
| enType          | Region type |
| u16ColorId      | Color index |
| u16LineWidth    | Line width |
| s32DrawFrameNum | Frame count: -1 draw continuously, 0 do not draw, >0 number of frames to draw |
| stRectangleArea | Rectangle parameters |
| stTriangleArea  | Triangle/diamond parameters |

&emsp;&emsp;【Related function interface】

&emsp;&emsp;PP_BOX_GROUP_S

<br/>

### **PP_BOX_GROUP_S**

&emsp;&emsp;【Description】

&emsp;&emsp;Box-drawing parameter structure.

&emsp;&emsp;【Definition】

```c
typedef struct akPP_BOX_GROUP_S {
    PP_BOX_S stBox[BOX_MAX_NUM];
} PP_BOX_GROUP_S;
```

&emsp;&emsp;【Members】

| **Member**   | **Description** |
| -------- | ------ |
| stBox    | Box-drawing parameters |

&emsp;&emsp;【Related function interface】

```c
    int AK_MPI_PP_DrawBox(AK_S32 s32GrpId, AK_U32 u32ChnId, PP_BOX_GROUP_S *pstBoxGroup);
```

<br/>

### **ISP_AF_ATTR_S**

&emsp;&emsp;【Description】

&emsp;&emsp;Autofocus information structure.

&emsp;&emsp;【Definition】

```c
typedef struct akISP_AF_ATTR_S {
    AK_U16  u16AfStatEnable;
    AK_U8   u8AfSpotlightLumTh;       //[0 ,255]
    AK_U8   u8AfSpotlightEdgeTh;   //[0 ,255]
    AK_U8   u8AfSpotlightEdgeGain; //[0, 15]
    AK_U8   u8AfClipTh;               //[0, 63]
    AK_U8   u8AfPeakCtrl;           //[0, 255]
    AK_U8   u8AfRshift;               //[0, 15]
} ISP_AF_ATTR_S;
```

&emsp;&emsp;【Members】

| **Member**                | **Description**  |
| --------------------- | ------------- |
| u16AfStatEnable       | Autofocus-module enable |
| u8AfSpotlightLumTh    | Spotlight-pixel statistics threshold |
| u8AfSpotlightEdgeTh   | Spotlight-edge decision threshold |
| u8AfSpotlightEdgeGain | Spotlight-edge suppression gain |
| u8AfClipTh            | Lower clipping limit for autofocus statistics |
| u8AfPeakCtrl          | Strong-edge weight |
| u8AfRshift            | Right-shift count applied before outputting pixel FV values |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_ISP_SetAfAttr(AK_S32 s32GrpId, ISP_AF_ATTR_S *pstAfAttr);
```

<br/>

### **ISP_AF_INFO_S**

&emsp;&emsp;【Description】

&emsp;&emsp;Autofocus statistics structure.

&emsp;&emsp;【Definition】

```c
typedef struct akISP_AF_INFO_S {
    AK_U32   u32AfStatics[8][16][5];
    AK_U8    u8AfLocalHighlight[64][128];
} ISP_AF_INFO_S;
```

&emsp;&emsp;【Members】

| **Member**             | **Description** |
| ------------------ | ------- |
| u32AfStatics       | AF statistics |
| u8AfLocalHighlight | Highlight statistics |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_ISP_GetAfStat(AK_S32 s32GrpId, ISP_AF_INFO_S *pstAfStat);
```

<br/>

### **ISP_OP_TYPE_E**

&emsp;&emsp;【Description】

&emsp;&emsp;Automatic/manual type.

&emsp;&emsp;【Definition】

```c
typedef enum akISP_OP_TYPE_E{
    ISP_OP_TYPE_MANUAL = 0,
    ISP_OP_TYPE_AUTO = 1,
    ISP_OP_TYPE_BUTT,
} ISP_OP_TYPE_E;
```

&emsp;&emsp;【Members】

| **Member**           | **Description**  |
| ------------------ | ------- |
| ISP_OP_TYPE_MANUAL | Manual |
| ISP_OP_TYPE_AUTO   | Automatic |
| ISP_OP_TYPE_BUTT   | Reserved; not currently used |

&emsp;&emsp;【Related data types and function interfaces】

<br/>

### **ISP_AE_EX_CONVER_ATTR_S**

&emsp;&emsp;【Description】

&emsp;&emsp;External automatic-exposure convergence-control attributes.

&emsp;&emsp;【Definition】

```c
typedef struct akISP_AE_EX_CONVER_ATTR_S {
    AK_U8    u8AeExConvergenceEn;
    AK_U16   u16ControlZone1;
    AK_U16   u16ControlZone2;
    AK_U16   u16ControlZone3;
    AK_U16   u16ControlZone4;
    AK_U16   u16ControlStep1;
    AK_U16   u16ControlStep2;
    AK_U16   u16ControlStep3;
    AK_U16   u16ControlStep4;
    AK_U16   u16ControlStepMax;
} ISP_AE_EX_CONVER_ATTR_S;
```

&emsp;&emsp;【Members】

| **Member**              | **Description**           |
| ------------------- | ---------------------- |
| u8AeExConvergenceEn | External AE-convergence control enable: 0 disabled, 1 enabled |
| u16ControlZone1     | AE-convergence control zone 1, [1,4096] |
| u16ControlZone2     | AE-convergence control zone 2, [1,4096] |
| u16ControlZone3     | AE-convergence control zone 3, [1,4096] |
| u16ControlZone4     | AE-convergence control zone 4, [1,4096] |
| u16ControlStep1     | AE-convergence control step 1, [1,512] |
| u16ControlStep2     | AE-convergence control step 2, [1,512] |
| u16ControlStep3     | AE-convergence control step 3, [1,512] |
| u16ControlStep4     | AE-convergence control step 4, [1,512] |
| u16ControlStepMax   | Inner AE-convergence threshold, [1,512] |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_ISP_GetAeAttr(AK_S32 s32GrpId, ISP_AE_ATTR_S *pstAeAttr);
    AK_S32 AK_MPI_ISP_SetAeAttr(AK_S32 s32GrpId, ISP_AE_ATTR_S *pstAeAttr);
```

<br/>

### **ISP_AE_STRGY_MODEL_E**

&emsp;&emsp;【Description】

&emsp;&emsp;Automatic-exposure strategy mode.

&emsp;&emsp;【Definition】

```c
typedef enum akISP_AE_STRGY_MODEL_E {
    ISP_AE_EXP_HIGHLIGHT_PRIOR = 0,
    ISP_AE_EXP_LOWLIGHT_PRIOR,
    ISP_AE_STRGY_MODEL_BUFF,
} ISP_AE_STRGY_MODEL_E;
```

&emsp;&emsp;【Members】

| **Member**                     | **Description** |
| -------------------------- | ---------- |
| ISP_AE_EXP_HIGHLIGHT_PRIOR | Highlight priority, i.e. strong-light suppression |
| ISP_AE_EXP_LOWLIGHT_PRIOR  | Low-light priority, i.e. backlight compensation |
| ISP_AE_STRGY_MODEL_BUFF    | Reserved |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_ISP_GetAeAttr(AK_S32 s32GrpId, ISP_AE_ATTR_S *pstAeAttr);
    AK_S32 AK_MPI_ISP_SetAeAttr(AK_S32 s32GrpId, ISP_AE_ATTR_S *pstAeAttr);
```

<br/>

### **ISP_RAW_G_HIST_ATTR_S**

&emsp;&emsp;【Description】

&emsp;&emsp;RAW-domain histogram structure.

&emsp;&emsp;【Definition】

```c
typedef struct akISP_RAW_G_HIST_ATTR_S{
    AK_U8  u8Enable;
    AK_U8  u8RawRshift;    //[0, 15]
    AK_U8  u8ZoneWeight[8][16];
} ISP_RAW_G_HIST_ATTR_S;
```

&emsp;&emsp;【Members】

| **Member**       | **Description** |
| ------------ | ------------ |
| u8Enable     | RAW histogram-statistics enable |
| u8RawRshift  | Right-shift count |
| u8ZoneWeight | RAW-domain automatic-exposure zone weight |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_ISP_GetAeAttr(AK_S32 s32GrpId, ISP_AE_ATTR_S *pstAeAttr);
    AK_S32 AK_MPI_ISP_SetAeAttr(AK_S32 s32GrpId, ISP_AE_ATTR_S *pstAeAttr);
```

<br/>

### **ISP_RGB_HIST_ATTR_S**

&emsp;&emsp;【Description】

&emsp;&emsp;RGB-domain histogram structure.

&emsp;&emsp;【Definition】

```c
typedef struct akISP_RGB_HIST_ATTR_S{
    AK_U8  u8RgbHistEnable;
    AK_U8  u8ZoneWeight[8][16];
} ISP_RGB_HIST_ATTR_S;
```

&emsp;&emsp;【Members】

| **Member**          | **Description** |
| --------------- | ------------ |
| u8RgbHistEnable | RGB histogram-statistics enable |
| u8ZoneWeight    | RGB-domain automatic-exposure zone weight |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_ISP_GetAeAttr(AK_S32 s32GrpId, ISP_AE_ATTR_S *pstAeAttr);
    AK_S32 AK_MPI_ISP_SetAeAttr(AK_S32 s32GrpId, ISP_AE_ATTR_S *pstAeAttr);
```

<br/>

### **ISP_YUV_HIST_ATTR_S**

&emsp;&emsp;【Description】

&emsp;&emsp;YUV-domain histogram structure.

&emsp;&emsp;【Definition】

```c
typedef struct akISP_YUV_HIST_ATTR_S{
    AK_U16  u16YuvHistEnable;
    AK_U8   u8ZoneWeight[8][16];
} ISP_YUV_HIST_ATTR_S;
```

&emsp;&emsp;【Members】

| **Member**           | **Description** |
| ---------------- | ------------ |
| u16YuvHistEnable | YUV histogram-statistics enable |
| u8ZoneWeight     | YUV-domain automatic-exposure zone weight |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_ISP_GetAeAttr(AK_S32 s32GrpId, ISP_AE_ATTR_S *pstAeAttr);
    AK_S32 AK_MPI_ISP_SetAeAttr(AK_S32 s32GrpId, ISP_AE_ATTR_S *pstAeAttr);
```

<br/>

### **ISP_AE_STRGY_ATTR_S**

&emsp;&emsp;【Description】

&emsp;&emsp;Automatic-exposure strategy attributes.

&emsp;&emsp;【Definition】

```c
typedef struct akISP_AE_STRGY_ATTR_S {
    AK_U32    u32HistWeight[16];
} ISP_AE_STRGY_ATTR_S;
```

&emsp;&emsp;【Members】

| **Member**        | **Description**     |
| ------------- | ---------------- |
| u32HistWeight | Automatic-exposure strategy weight table, [0,15] |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_ISP_GetAeAttr(AK_S32 s32GrpId, ISP_AE_ATTR_S *pstAeAttr);
    AK_S32 AK_MPI_ISP_SetAeAttr(AK_S32 s32GrpId, ISP_AE_ATTR_S *pstAeAttr);
```

<br/>

### ISP_AE_ROUTE_NODE_ATTR_S

&emsp;&emsp;【Description】

&emsp;&emsp;Automatic-exposure allocation-route node attributes.

&emsp;&emsp;【Definition】

```c
typedef struct akISP_AE_ROUTE_NODE_ATTR_S {
    AK_U32   u32ExpTime;
    AK_U32   u32Again;
    AK_U32   u32Dgain;
    AK_U32   u32IspDgain;
} ISP_AE_ROUTE_NODE_ATTR_S;
```

&emsp;&emsp;【Members】

| **Member**      | **Description**             |
| ----------- | ------------------------ |
| u32ExpTime  | Node exposure time, [1,65535] |
| u32Again    | Node sensor analog gain, [256,65535] |
| u32Dgain    | Node sensor digital gain, [256,65535] |
| u32IspDgain | Node ISP digital gain, [256,65535] |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_ISP_GetAeAttr(AK_S32 s32GrpId, ISP_AE_ATTR_S *pstAeAttr);
    AK_S32 AK_MPI_ISP_SetAeAttr(AK_S32 s32GrpId, ISP_AE_ATTR_S *pstAeAttr);
```

<br/>

### **ISP_AE_ROUTE_ATTR_S**

&emsp;&emsp;【Description】

&emsp;&emsp;Automatic-exposure allocation-route attributes.

&emsp;&emsp;【Definition】

```c
typedef struct akISP_AE_ROUTE_ATTR_S{
    AK_U8   u8AeRouteEn;
    AK_U8   u8AeRouteNodeNum;
    ISP_AE_ROUTE_NODE_ATTR_S  stAeRouteNode[10];
} ISP_AE_ROUTE_ATTR_S;
```

&emsp;&emsp;【Members】

| **Member**           | **Description**  |
| ---------------- | ------------- |
| u8AeRouteEn      | Exposure-route setting enable |
| u8AeRouteNodeNum | Number of exposure-route nodes, [1,16] |
| stAeRouteNode    | Exposure-route node attributes |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_ISP_GetAeAttr(AK_S32 s32GrpId, ISP_AE_ATTR_S *pstAeAttr);
    AK_S32 AK_MPI_ISP_SetAeAttr(AK_S32 s32GrpId, ISP_AE_ATTR_S *pstAeAttr);
```

<br/>

### **ISP_WDR_AE_ATTR_S**

&emsp;&emsp;【Description】

&emsp;&emsp;Automatic-exposure allocation-route attributes.

&emsp;&emsp;【Definition】

```c
typedef struct akISP_WDR_AE_ATTR_S
{
    AK_U16 u16ExpRatioType;
    AK_U16 u16ExpRatioLS;
    AK_U16 u16ExpRatioSVS;
    AK_U16 u16ExpRatioMax;
    AK_U16 u16ExpRatioMin;
    AK_U8  u8ExpRatioSpeed;
    AK_U8  u8ExpHighlightCtrl;
} ISP_WDR_AE_ATTR_S;
```

&emsp;&emsp;【Members】

| **Member**             | **Description**                       |
| ------------------ | ---------------------------------- |
| u16ExpRatioType    | Multi-frame synthesis exposure-ratio strategy: 0 fixed ratio, 1 automatic ratio |
| u16ExpRatioLS      | Long/short-frame exposure ratio, [16,4095] |
| u16ExpRatioSVS     | Short/very-short-frame exposure ratio, [16,4095] |
| u16ExpRatioMax     | Maximum exposure ratio in automatic-ratio mode, [0,16384] |
| u16ExpRatioMin     | Minimum exposure ratio in automatic-ratio mode, [0,u16ExpRatioMax] |
| u8ExpRatioSpeed    | Exposure-ratio adjustment speed in automatic-ratio mode, [0,255] |
| u8ExpHighlightCtrl | Highlight overexposure-suppression strength in automatic-ratio mode, [0,255] |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_ISP_GetAeAttr(AK_S32 s32GrpId, ISP_AE_ATTR_S *pstAeAttr);
    AK_S32 AK_MPI_ISP_SetAeAttr(AK_S32 s32GrpId, ISP_AE_ATTR_S *pstAeAttr);
```

<br/>

### **ISP_AE_ATTR_S**

&emsp;&emsp;【Description】

&emsp;&emsp;Automatic-exposure parameter structure.

&emsp;&emsp;【Definition】

```c
typedef struct akISP_AE_ATTR_S {
    AK_U32  u32ExpTimeMax;
    AK_U32  u32AGainMax;
    AK_U32  u32DGainMax;
    AK_U32  u32IspDGainMax;
    AK_U16  u16ExpTimeMin;
    AK_U16  u16AGainMin;
    AK_U16  u16DGainMin;
    AK_U16  u16IspDGainMin;
    AK_U16  u16BlacklightRateMax;
    AK_U16  u16BlacklightRateMin;
    AK_U16  u16ExpStep;
    AK_U8   u8ExpStableRange;
    AK_U8   u8ExpHoldRange;
    AK_U8   u8ExpSpeed;
    AK_U8   u8AntiFlickerTargetLumi;
    AK_U8   u8AntiFlickerStartExp;
    AK_U8   u8ExpLumiFilterPara;
    AK_U8   u8TtargetLumiance[12];
    AK_U8   u8BlacklightCompensationEn;
    AK_U8   u8BlacklightDetectScope;
    ISP_RAW_G_HIST_ATTR_S      stRawGHistAttr;
    ISP_RGB_HIST_ATTR_S        stRgbHistAttr;
    ISP_YUV_HIST_ATTR_S        stYuvHistAttr;
    AK_U16                      u16EnviGainRange[12][2];
    ISP_AE_EX_CONVER_ATTR_S    stAeExConvergencePara;
    ISP_AE_STRGY_MODEL_E       enAeStrgyType;
    ISP_AE_STRGY_ATTR_S        stAeStrgyPara[3];
    ISP_AE_ROUTE_ATTR_S        stExpRoutePara;
    ISP_WDR_AE_ATTR_S          stWdrAePara;
}ISP_AE_ATTR_S;
```

&emsp;&emsp;【Members】

| **Member**                     | **Description**           |
| -------------------------- | ---------------------- |
| u32ExpTimeMax              | Maximum exposure time, [1,65535] |
| u16ExpTimeMin              | Minimum exposure time, [1,65535] |
| u32DGainMax                | Maximum digital gain, [256,65535] |
| u16DGainMin                | Minimum digital gain, [256,65535] |
| u16IspDGainMin             | Minimum ISP digital gain, [256,65535] |
| u32IspDGainMax             | Maximum ISP digital gain, [256,65535] |
| AK_U32  u32ExpTimeMax;     | Maximum analog gain, [256,65535] |
| u16AGainMin                | Minimum analog gain, [256,65535] |
| u16ExpStep                 | Exposure-adjustment step, [1,65535] |
| u8ExpStableRange           | Inner AE-convergence threshold, [1,100] |
| u8ExpHoldRange             | Outer AE-convergence threshold, [1,100] |
| u8ExpSpeed                 | Convergence-speed control parameter, [1,100] |
| u8AntiFlickerTargetLumi    | Sub anti-flicker target luminance, [0,255] |
| u8AntiFlickerStartExp      | Exposure-time range in which sub anti-flicker takes effect, [1,10] |
| u8ExpLumiFilterPara        | Luminance-smoothing parameter, [1,100] |
| u8TtargetLumiance          | Target luminance for each EnX, [1,255] |
| u16EnviGainRange           | EnvX-range control parameter, [0,65535] |
| u8BlacklightCompensationEn | Backlight-compensation enable, [0,1] |
| u8BlacklightDetectScope    | Dark-region pixel-detection area, [0,255] |
| u16BlacklightRateMax       | Maximum proportion of dark backlight-region pixels, [1,128] |
| u16BlacklightRateMin       | Minimum proportion of dark backlight-region pixels, [1,128] |
| stRawGHistAttr             | RAW histogram |
| stRgbHistAttr              | RGB histogram |
| stYuvHistAttr              | YUV histogram |
| stAeExConvergencePara      | External automatic-exposure convergence-control parameters |
| enAeStrgyType              | Exposure-strategy mode |
| stAeStrgyPara              | Exposure-strategy parameters |
| stExpRoutePara             | Automatic-exposure route allocation |
| stWdrAePara                | WDR automatic-exposure parameters |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_ISP_GetAeAttr(AK_S32 s32GrpId, ISP_AE_ATTR_S *pstAeAttr);
    AK_S32 AK_MPI_ISP_SetAeAttr(AK_S32 s32GrpId, ISP_AE_ATTR_S *pstAeAttr);
```

<br/>

### **ISP_ME_ATTR_S**

&emsp;&emsp;【Description】

&emsp;&emsp;Manual-exposure parameter structure.

&emsp;&emsp;【Definition】

```c
typedef struct akISP_ME_ATTR_S {
    AK_U32   u32ExpTime;
    AK_U32   u32AGain;
    AK_U32   u32DGain;
    AK_U32   u32IspDGain;
} ISP_ME_ATTR_S;
```

&emsp;&emsp;【Members】

| **Member**      | **Description**        |
| ----------- | ------------------- |
| u32ExpTime  | Exposure time, [1,65535] |
| u32AGain    | Analog gain, [256,65535] |
| u32DGain    | Digital gain, [256,65535] |
| u32IspDGain | ISP digital gain, [256,65535] |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_ISP_GetMeAttr(AK_S32 s32GrpId, ISP_ME_ATTR_S *pstMeAttr);
    AK_S32 AK_MPI_ISP_SetMeAttr(AK_S32 s32GrpId, ISP_ME_ATTR_S *pstMeAttr);
```

<br/>

### **ISP_RAW_HIST_STAT_INFO_S**

&emsp;&emsp;【Description】

&emsp;&emsp;RAW-domain histogram statistics.

&emsp;&emsp;【Definition】

```c
typedef struct akISP_RAW_HIST_STAT_INFO_S {
    AK_U32  u32rawGHist[256];
    AK_U64  u32RawGTotal;
} ISP_RAW_HIST_STAT_INFO_S;
```

&emsp;&emsp;【Members】

| **Member**       | **Description** |
| ------------ | ----------- |
| u32rawGHist  | RAW-domain histogram statistics |
| u32RawGTotal | Total RAW-domain luminance |

&emsp;&emsp;【Related function interface】

```c
    ISP_AE_STAT_INFO_S
```

<br/>

### **ISP_RGB_HIST_STAT_INFO_S**

&emsp;&emsp;【Description】

&emsp;&emsp;RGB-domain histogram statistics.

&emsp;&emsp;【Definition】

```c
typedef struct akISP_RGB_HIST_STAT_INFO_S {
    AK_U32  u32RgbHist[256];
    AK_U64  u32RgbTotal;
} ISP_RGB_HIST_STAT_INFO_S;
```

&emsp;&emsp;【Members】

| **Member**      | **Description** |
| ----------- | ----------- |
| u32RgbHist  | RGB-domain histogram statistics |
| u32RgbTotal | Total RGB-domain luminance |

&emsp;&emsp;【Related function interface】

```c
    ISP_AE_STAT_INFO_S
```

<br/>

### **ISP_YUV_HIST_STAT_INFO_S**

&emsp;&emsp;【Description】

&emsp;&emsp;YUV-domain histogram statistics.

&emsp;&emsp;【Definition】

```c
typedef struct  akISP_YUV_HIST_STAT_INFO_S {
    AK_U32  u32YHist[256];
    AK_U64  u32YTotal;
} ISP_YUV_HIST_STAT_INFO_S;
```

&emsp;&emsp;【Members】

| **Member**    | **Description** |
| --------- | ----------- |
| u32YHist  | YUV-domain histogram statistics |
| u32YTotal | Total YUV-domain luminance |

&emsp;&emsp;【Related function interface】

```c
    ISP_AE_STAT_INFO_S
```

<br/>

### **ISP_WDR_HIST_STAT_INFO_S**

&emsp;&emsp;【Description】

&emsp;&emsp;Long/short-frame histogram statistics.

&emsp;&emsp;【Definition】

```c
typedef struct akISP_WDR_HIST_STAT_INFO_S{
    AK_U32  u32WdrHistShort[256];
    AK_U32    u32WdrHistLong[256];
} ISP_WDR_HIST_STAT_INFO_S;
```

&emsp;&emsp;【Members】

| **Member**          | **Description** |
| --------------- | --------- |
| u32WdrHistShort | Short-frame histogram statistics |
| u32WdrHistLong  | Long-frame histogram statistics |

&emsp;&emsp;【Related function interface】

```c
    ISP_AE_STAT_INFO_S
```

<br/>

### **ISP_AE_STAT_INFO_S**

&emsp;&emsp;【Description】

&emsp;&emsp;Automatic-exposure status information.

&emsp;&emsp;【Definition】

```c
typedef struct akISP_AE_STAT_INFO_S{
    ISP_RAW_HIST_STAT_INFO_S           stRawHistStatPara;
    ISP_RGB_HIST_STAT_INFO_S           stRgbHistStatPara;
    ISP_YUV_HIST_STAT_INFO_S           stYuvHistStatPara;
    ISP_WDR_HIST_STAT_INFO_S           stRawWdrCombStatPara;
} ISP_AE_STAT_INFO_S;
```

&emsp;&emsp;【Members】

| **Member**               | **Description** |
| -------------------- | -------- |
| stRawHistStatPara    | RAW histogram information |
| stRgbHistStatPara    | RGB histogram information |
| stYuvHistStatPara    | YUV histogram information |
| stRawWdrCombStatPara | Long/short-frame histogram information |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_ISP_GetAeRunInfo(AK_S32 s32GrpId, ISP_AE_RUN_INFO_S *pstAeRunInfo);
```

<br/>

### **ISP_AE_RUN_INFO_S**

&emsp;&emsp;【Description】

&emsp;&emsp;Automatic-exposure runtime-information structure.

&emsp;&emsp;【Definition】

```c
typedef struct akISP_AE_RUN_INFO_S {
    AK_U8    u8CurrentCalcAvgLumi;
    AK_U8    u8CurrentCalcAvgCompensationLumi;
    AK_U8    u8CurrentTargetLumi;
    AK_U8    u8IsStable;

    AK_U32  u32CurrentAGain;
    AK_U32  u32CurrentDGain;
    AK_U32  u32CurrentIspDGain;
    AK_U32  u32CurrentExpTime;

    AK_U32  u32CurrentAGainStep;
    AK_U32  u32CurrentDGainStep;
    AK_U32  u32CurrentIspDGainStep;
    AK_U32  u32CurrentExpTimeStep;

    AK_U32  u32CurrentRefExpRatio;
    AK_U32  u32CurrentLongExpTime;
    AK_U32  u32CurrentShortExpTime;
    AK_U8   u8CurrentShortAvgLumi;
    AK_U8   u8CurrentLongAvgLumi;

    ISP_AE_STAT_INFO_S stAeStatInfo;
} ISP_AE_RUN_INFO_S;
```

&emsp;&emsp;【Members】

| **Member**                           | **Description** |
| -------------------------------- | ----------- |
| u8CurrentCalcAvgLumi             | Average luminance |
| u8CurrentCalcAvgCompensationLumi | Average luminance after exposure compensation |
| u8CurrentTargetLumi              | Target luminance |
| u8IsStable                       | Exposure-stability flag |
| u32CurrentAGain                  | Current analog gain |
| u32CurrentDGain                  | Current digital gain |
| u32CurrentIspDGain               | Current ISP digital gain |
| u32CurrentExpTime                | Current exposure time |
| u32CurrentAGainStep              | Current analog-gain step |
| u32CurrentDGainStep              | Current digital-gain step |
| u32CurrentIspDGainStep           | Current ISP digital-gain step |
| u32CurrentExpTimeStep            | Current exposure-time step |
| u32CurrentRefExpRatio            | Reference exposure ratio |
| u32CurrentLongExpTime            | Current long-exposure-frame exposure time |
| u32CurrentShortExpTime           | Current short-exposure-frame exposure time |
| u8CurrentShortAvgLumi            | Current short-exposure-frame average luminance |
| u8CurrentLongAvgLumi             | Current long-exposure-frame average luminance |
| stAeStatInfo                     | Automatic-exposure status information |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_ISP_GetAeRunInfo(AK_S32 s32GrpId, ISP_AE_RUN_INFO_S *pstAeRunInfo);
```

<br/>

### **ISP_AWB_BLK_AVG_STAT_INFO_S**

&emsp;&emsp;【Description】

&emsp;&emsp;Per-region RGB-channel average statistics.

&emsp;&emsp;【Definition】

```c
typedef struct akISP_AWB_BLK_AVG_STAT_INFO_S{
    AK_U32 u32WbRavgStat[16][16];
    AK_U32 u32WbGavgStat[16][16];
    AK_U32 u32WbBavgStat[16][16];
} ISP_AWB_BLK_AVG_STAT_INFO_S;
```

&emsp;&emsp;【Members】

| **Member**        | **Description** |
| ------------- | ------------ |
| u32WbRavgStat | Per-region R-channel average statistics |
| u32WbGavgStat | Per-region G-channel average statistics |
| u32WbBavgStat | Per-region B-channel average statistics |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_ISP_GetAwbStatInfo(AK_S32 s32GrpId, ISP_AWB_STAT_INFO_S *pstAwbStatInfo);
```

<br/>

### **ISP_AWB_BLK_WP_STAT_INFO_S**

&emsp;&emsp;【Description】

&emsp;&emsp;Per-region RGB-channel white-point average statistics.

&emsp;&emsp;【Definition】

```c
typedef struct akISP_AWB_BLK_WP_STAT_INFO_S{
    AK_U32 u32WpRStat[16][16];
    AK_U32 u32WpGStat[16][16];
    AK_U32 u32WpBStat[16][16];
    AK_U32 u32WpCntStatics[16][16];
} ISP_AWB_BLK_WP_STAT_INFO_S;
```

&emsp;&emsp;【Members】

| **Member**          | **Description**   |
| --------------- | -------------- |
| u32WpRStat      | Per-region R-channel white-point average statistics |
| u32WpGStat      | Per-region G-channel white-point average statistics |
| u32WpBStat      | Per-region B-channel white-point average statistics |
| u32WpCntStatics | Total white-point count |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_ISP_GetAwbStatInfo(AK_S32 s32GrpId, ISP_AWB_STAT_INFO_S *pstAwbStatInfo);
```

<br/>

### **ISP_AWB_RUN_INFO_S**

&emsp;&emsp;【Description】

&emsp;&emsp;White-balance runtime-information structure.

&emsp;&emsp;【Definition】

```c
typedef struct akISP_AWB_RUN_INFO_S{
    AK_U16  u16RGain;
    AK_U16  u16GGain;
    AK_U16  u16BGain;
    AK_S16  s16ROffset;
    AK_S16  s16GOffset;
    AK_S16  s16BOffset;
    AK_U8   u8IsStable;
    AK_U8   u8CurrentColortempIndex;
    AK_U16  u16ColortempStableCnt[10];
    AK_U16  u16CurrentColortemp;
} ISP_AWB_RUN_INFO_S;
```

&emsp;&emsp;【Members】

| **Member**                  | **Description**         |
| ----------------------- | -------------------- |
| u16RGain                | Red-component gain |
| u16GGain                | Green-component gain |
| u16BGain                | Blue-component gain |
| s16ROffset              | Red-component offset |
| s16GOffset              | Green-component offset |
| s16BOffset              | Blue-component offset |
| u8IsStable              | Whether stable |
| u8CurrentColortempIndex | Ambient-color-temperature marker; an index of color-temperature parameters as the environment changes |
| u16ColortempStableCnt   | Count of stable frames for each color temperature |
| u16CurrentColortemp     | Ambient color temperature |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_ISP_GetAwbStatInfo(AK_S32 s32GrpId, ISP_AWB_STAT_INFO_S *pstAwbStatInfo);
```

<br/>

### **ISP_AWB_STAT_INFO_S**

&emsp;&emsp;【Description】

&emsp;&emsp;White-balance statistics structure.

&emsp;&emsp;【Definition】

```c
typedef struct akISP_AWB_STAT_INFO_S {
    AK_U32   u32TotalR[10];
    AK_U32   u32TotalG[10];
    AK_U32   u32TotalB[10];
    AK_U32   u32TotalCnt[10];
    ISP_AWB_BLK_AVG_STAT_INFO_S    stWbBlkAvgStat;
    ISP_AWB_BLK_WP_STAT_INFO_S     stWbBlkWpStat;
    ISP_AWB_RUN_INFO_S             stWbRunInfo;
} ISP_AWB_STAT_INFO_S;
```

<br/>

&emsp;&emsp;【Members】

| **Member**         | **Description**       |
| -------------- | ------------------ |
| u32TotalR      | R-component pixel values for each of 10 color temperatures |
| u32TotalG      | G-component pixel values for each of 10 color temperatures |
| u32TotalB      | B-component pixel values for each of 10 color temperatures |
| u32TotalCnt    | Number of pixels within the white-balance statistics parameter range |
| stWbBlkAvgStat | Per-region RGB-channel average statistics |
| stWbBlkWpStat  | Per-region RGB-channel white-point average statistics |
| stWbRunInfo    | White-balance runtime-information structure |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_ISP_GetAwbStatInfo(AK_S32 s32GrpId, ISP_AWB_STAT_INFO_S *pstAwbStatInfo);
```

<br/>

### **ISP_MWB_ATTR_S**

&emsp;&emsp;【Description】

&emsp;&emsp;Manual white-balance parameter structure.

&emsp;&emsp;【Definition】

```c
typedef struct  akISP_MWB_ATTR_S
{
    AK_U16    u16RGain;
    AK_U16    u16GGain;
    AK_U16    u16BGain;
    AK_S16    s16ROffset;
    AK_S16    s16GOffset;
    AK_S16    s16BOffset;
} ISP_MWB_ATTR_S;
```

&emsp;&emsp;【Members】

| **Member**     | **Description**      |
| ---------- | ----------------- |
| u16RGain   | R-channel gain, [0,4095] |
| u16GGain   | G-channel gain, [0,4095] |
| u16BGain   | B-channel gain, [0,4095] |
| s16ROffset | R-channel offset, [-512,511] |
| s16GOffset | G-channel offset, [-512,511] |
| s16BOffset | B-channel offset, [-512,511] |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_ISP_GetMwbAttr(AK_S32 s32GrpId, ISP_MWB_ATTR_S *pstMwbAttr);
    AK_S32 AK_MPI_ISP_SetMwbAttr(AK_S32 s32GrpId, ISP_MWB_ATTR_S *pstMwbAttr);
```

<br/>

### ISP_AWB_ALGO_TYPE_E

&emsp;&emsp;【Description】

&emsp;&emsp;Automatic white-balance algorithm type.

&emsp;&emsp;【Definition】

```c
typedef enum akISP_AWB_ALGO_TYPE_E{
    ISP_AWB_ALGO_DEFAULT = 0,
    ISP_AWB_ALGO_AVERAGE_WEIGHT = 1,
    ISP_AWB_ALGO_BLOCK_ASSIST,
    ISP_AWB_ALGO_GW,
    ISP_AWB_ALGO_BUTT,
} ISP_AWB_ALGO_TYPE_E;
```

&emsp;&emsp;【Members】

| **Member**                      | **Description** |
| --------------------------- | ----------- |
| ISP_AWB_ALGO_DEFAULT        | Default automatic white-balance algorithm |
| ISP_AWB_ALGO_AVERAGE_WEIGHT | Average-weighted automatic white-balance algorithm |
| ISP_AWB_ALGO_BLOCK_ASSIST   | Algorithm using white-balance block information |
| ISP_AWB_ALGO_GW             | Gray-world method |
| ISP_AWB_ALGO_BUTT           | Reserved method |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_ISP_GetAwbAttr(AK_S32 s32GrpId, ISP_AWB_ATTR_S *pstAwbAttr);
    AK_S32 AK_MPI_ISP_SetAwbAttr(AK_S32 s32GrpId, ISP_AWB_ATTR_S *pstAwbAttr);
```

<br/>

### **ISP_AWB_STAT_CALIB_PARA_S**

&emsp;&emsp;【Description】

&emsp;&emsp;Automatic white-balance statistics parameters.

&emsp;&emsp;【Definition】

```c
typedef struct akISP_AWB_STAT_CALIB_PARA_S{
    AK_U16     u16GrLow[10];            //gr_low[i]<=gr_high[i]
    AK_U16     u16GrHigh[10];
    AK_U16     u16GbLow[10];            //gb_low[i]<=gb_high[i]
    AK_U16     u16GbHigh[10];
    AK_U16     u16RbLow[10];           //rb_low[i]<=rb_high[i]
    AK_U16     u16RbHigh[10];
} ISP_AWB_STAT_CALIB_PARA_S;
```

&emsp;&emsp;【Members】

| **Member**                                                   | **Description**                                      |
| -------------------------------------------------------- | ------------------------------------------------- |
| u16GrLow, u16GbLow, u16GrHigh, u16GbHigh, u16RbLow, u16RbHigh | Indices 0-8 are the white-point statistics region ranges for white-balance calibration;<br/>index 9 is the R/G/B statistics region range for the current full image |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_ISP_GetAwbAttr(AK_S32 s32GrpId, ISP_AWB_ATTR_S *pstAwbAttr);
    AK_S32 AK_MPI_ISP_SetAwbAttr(AK_S32 s32GrpId, ISP_AWB_ATTR_S *pstAwbAttr);
```

<br/>

### **ISP_AWB_ATTR_S**

&emsp;&emsp;【Description】

&emsp;&emsp;Automatic white-balance parameter structure.

&emsp;&emsp;【Definition】

```c
typedef  struct akISP_AWB_ATTR_S {
    AK_U8                        u8GWeight[16];
    AK_U8                        u8YLow;                 //y_low<=y_high
    AK_U8                        u8YHigh;
    AK_U8                        u8ErrEst;
    AK_U8                        u8AwbIsoTrackEnable;
    AK_U8                        u8ColortempEnvi[10];
    ISP_AWB_STAT_CALIB_PARA_S  stAwbStatCalibPara[12];

    AK_U16                        u16AutoWbStep;
    AK_U16                        u16TotalCntThresh;
    AK_U16                        u16ColortempStableCntThresh;
    ISP_AWB_ALGO_TYPE_E        enAlgType;
} ISP_AWB_ATTR_S;
```

&emsp;&emsp;【Members】

| **Member**                      | **Description**                  |
| --------------------------- | ----------------------------- |
| u8GWeight                   | Weights for different luminances, changing their influence on white balance, [0,15] |
| u8YLow                      | Minimum luminance threshold for white-balance statistics, [0,255] |
| u8YHigh                     | Maximum luminance threshold for white-balance statistics, [0,255] |
| u8ErrEst                    | Error estimate, [0,255] |
| u8AwbIsoTrackEnable         | Enable for adjusting AWB statistics parameters with gain |
| stAwbStatCalibPara          | Automatic white-balance statistics parameters, [0,1023] |
| u16AutoWbStep               | White-balance step calculation, [0,255] |
| u16TotalCntThresh           | Pixel-count threshold, [0,65535] |
| u16ColortempStableCntThresh | Stable-frame count used to decide that ambient color temperature changed, [0,255] |
| u8ColortempEnvi             | [0,3], color-temperature environment corresponding to each parameter set, [0,8] |
| enAlgType                   | Automatic white-balance algorithm type |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_ISP_GetAwbAttr(AK_S32 s32GrpId, ISP_AWB_ATTR_S *pstAwbAttr);
    AK_S32 AK_MPI_ISP_SetAwbAttr(AK_S32 s32GrpId, ISP_AWB_ATTR_S *pstAwbAttr);
```

<br/>

### **ISP_HDR_S**

&emsp;&emsp;【Description】

&emsp;&emsp;WDR information.

&emsp;&emsp;【Definition】

```c
typedef struct akISP_HDR_S {
    AK_U8   u8HdrEnable;
    AK_U8   u8HdrUvAdjustEnable;
    AK_U16    u16HdrTh1;      //0-1023
    AK_U16    u16HdrTh2;      //0-1023
    AK_U16    u16HdrTh3;      //0-1023
    AK_U16    u16HdrTh4;      //0-1023
    AK_U16    u16HdrTh5;      //0-1023

    AK_U16    u16AreaTb1[65];
    AK_U16    u16AreaTb2[65];
    AK_U16    u16AreaTb3[65];
    AK_U16    u16AreaTb4[65];
    AK_U16    u16AreaTb5[65];
    AK_U16    u16AreaTb6[65];

    AK_U16    u16Area1Key[16];
    AK_U16    u16Area2Key[16];
    AK_U16    u16Area3Key[16];
    AK_U16    u16Area4Key[16];
    AK_U16    u16Area5Key[16];
    AK_U16    u16Area6Key[16];

    AK_U16  u16HdrCnoiseSuppressYth1;
    AK_U16    u16HdrCnoiseSuppressYth2;
    AK_U16  u16HdrC_cnoiseSuppressGain;
    AK_U8   u8HdrCnoiseSuppressSlop;
    AK_U8    u8HdrUvAdjustLevel;
    AK_U8    u8HdrSpatialfiltK;
}ISP_HDR_S;
```

&emsp;&emsp;【Members】

| **Member**                          | **Description**       |
| ------------------------------- | ------------------ |
| u8HdrEnable                     | Enable flag |
| u8HdrUvAdjustEnable             | UV-adjustment enable |
| u16HdrTh1~u16HdrTh5             | Five thresholds, [0,255] |
| u16AreaTb1[65]~u16AreaTb6[65]   | Six area curves, [0,1023] |
| u16Area1Key[16]~u16Area6Key[16] | Key-point information for six curves |
| u16HdrCnoiseSuppressYth1        | Chroma-noise luminance threshold 1, [0,1023] |
| u16HdrCnoiseSuppressYth2        | Chroma-noise luminance threshold 2, [0,1023] |
| u16HdrC_cnoiseSuppressGain      | Chroma-difference suppression, [0,1023] |
| u8HdrCnoiseSuppressSlop         | Suppression slope, [0,128] |
| u8HdrUvAdjustLevel              | UV-adjustment level, [0,31] |
| u8HdrSpatialfiltK               | Spatial-filter coefficient, [0,5] |

&emsp;&emsp;【Related function interface】

&emsp;&emsp;ISP_HDR_ATTR_S

<br/>

### **ISP_HDR_ATTR_S**

&emsp;&emsp;【Description】

&emsp;&emsp;WDR information structure.

&emsp;&emsp;【Definition】

```c
typedef struct akISP_HDR_ATTR_S
{
    ISP_OP_TYPE_E    enHdrMode;
    ISP_HDR_S        stManualHdr;
    ISP_HDR_S         stLinkageHdr[12];
} ISP_HDR_ATTR_S;
```

&emsp;&emsp;【Members】

| **Member**       | **Description**  |
| ------------ | ------------- |
| enHdrMode    | Mode selection: 0 manual, 1 linked |
| stManualHdr  | Manual WDR parameters |
| stLinkageHdr | Linked WDR parameters |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_ISP_GetHdrAttr(AK_S32 s32GrpId, ISP_HDR_ATTR_S *pstHdr);
    AK_S32 AK_MPI_ISP_SetHdrAttr(AK_S32 s32GrpId, ISP_HDR_ATTR_S *pstHdr);
```

<br/>

### **ISP_GAIN_STAT_E**

&emsp;&emsp;【Description】

&emsp;&emsp;Gain status.

&emsp;&emsp;【Definition】

```c
typedef enum akISP_GAIN_STAT_E {
    ISP_GAIN_NO_CHANGE_STAT = 0,
    ISP_GAIN_LOW_STAT,
    ISP_GAIN_HIGH_STAT,
    ISP_GAIN_MID_STAT,
} ISP_GAIN_STAT_E;
```

&emsp;&emsp;【Members】

| **Member**                  | **Description** |
| ----------------------- | ------ |
| ISP_GAIN_NO_CHANGE_STAT | Gain unchanged |
| ISP_GAIN_LOW_STAT       | Low-gain state |
| ISP_GAIN_HIGH_STAT      | High-gain state |
| ISP_GAIN_MID_STAT       | Medium-gain state |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_ISP_GetFpsCtrlStat(AK_S32 s32GrpId, ISP_GAIN_STAT_E *penStat, AK_S32 *ps32NeedFps);
```

<br/>

### **ISP_FPS_LEVEL_S**

&emsp;&emsp;【Description】

&emsp;&emsp;Three-level frame-rate structure.

&emsp;&emsp;【Definition】

```c
typedef struct akISP_FPS_LEVEL_S {
    AK_U32 u32HighFps;
    AK_U32 u32HighFpsExpTime;
    AK_U32 u32HighFpsToLowerFpsGain;

    AK_U32 u32MidFps;                //set 0 means no use middle fps
    AK_U32 u32MidFpsExpTime;         //set 0 means no use middle fps
    AK_U32 u32MidFpsToLowFpsGain;    //set 0 means no use middle fps

    AK_U32 u32LowFps;
    AK_U32 u32LowFpsExpTime;
    AK_U32 u32LowFpsToHigherFpsGain;
} ISP_FPS_LEVEL_S;
```

&emsp;&emsp;【Members】

| **Member**                   | **Description**                              |
| ------------------------ | ----------------------------------------- |
| u32HighFps               | High frame rate, [1,60] |
| u32HighFpsExpTime        | Maximum exposure time at the high frame rate, [100,65535] |
| u32HighFpsToLowerFpsGain | Gain threshold for switching from the high to a lower frame rate, [1,512] |
| u32MidFps                | Middle frame rate; set 0 to disable, [5,60] |
| u32MidFpsExpTime         | Maximum exposure time at the middle frame rate; set 0 to disable, [100,65535] |
| u32MidFpsToLowFpsGain    | Gain threshold for switching from the middle to the low frame rate; set 0 to disable, [1,512] |
| u32LowFps                | Low frame rate, [1,60] |
| u32LowFpsExpTime         | Maximum exposure time at the low frame rate, [100,65535] |
| u32LowFpsToHigherFpsGain | Gain threshold for switching from the low to a higher frame rate, [1,512] |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_ISP_SetFpsLevel(AK_S32 s32GrpId, ISP_FPS_LEVEL_S *pstFpsLevel);
    AK_S32 AK_MPI_ISP_GetFpsLevel(AK_S32 s32GrpId, ISP_FPS_LEVEL_S *pstFpsLevel);
```

<br/>

### **ISP_3DNR_S**

&emsp;&emsp;【Description】

&emsp;&emsp;3D noise-reduction information structure.

&emsp;&emsp;【Definition】

```c
typedef struct akISP_3DNR_S {
    AK_U8        u8TnrEnable;            //default:1(GUI edit)
    AK_U8        u8TnrRefFrameFormat;
    AK_U8         u8YnrDPCStr;                    //[0, 127]
    AK_U8         u8YnrDPCCap;                    //[0, 127]
    AK_U8         u8YnrDPCDiffGain[8];            //[0,7]
    AK_U8         u8YnrK;            //[0,15]
    AK_U8        u8YnrLumStr[32]; //[0, 15]
    AK_U8        u8YlpK1;            //[0, 15],default:7(GUI edit)
    AK_U8        u8YlpK2;            //[0, 15],default:0(GUI edit)
    AK_U8         u8YDiffUVWgt;        //[0, 15]
    AK_U8         u8YDiffEdgeWgt;    //[0, 15]
    AK_U8        u8TYLow1;        //[0,127]
    AK_U8        u8TYLow2;        //[0,127]
    AK_U8        u8TYK1;         //[0, 127],default:120(GUI edit)
    AK_U8        u8TYK2;         //[0, 127],default:120(GUI edit)
    AK_U8        u8TYExK;         //[0, 15]
    AK_U8        u8TYKslop1;         //[0, 127],default:32(GUI edit)
    AK_U8        u8TYKslop2;        //[0, 127]
    AK_U8        u8TYSrcChooseKTh;         //[0, 127]
    AK_U8        u8TYUpdateTh;

    AK_U8        u8UvnrK;         //[0, 15],default:8(GUI edit)
    AK_U8        u8UvlpK1;         //[0, 15],default:7(GUI edit)
    AK_U8        u8UvlpK2;         //[0, 15],default:0(GUI edit)
    AK_U8        u8TUvDiffScale;//[0, 15]
    AK_U8        u8TUvKLow1;        //[0, 127]
    AK_U8        u8TUvKLow2;    //[0, 127]
    AK_U8        u8TUvK1;         //[0, 127],default:120(GUI edit)
    AK_U8        u8TUvK2;         //[0, 127]
    AK_U8        u8TUvExK;         //[0, 15],
    AK_U8        u8TUvKslop1;         //[0, 127],default:32(GUI edit)
    AK_U8        u8TUvKslop2;         //[0, 127],default:32(GUI edit)
    AK_U8        u8TUvSrcChooseKTh; //[0, 127]

    AK_U8        u8MfactorKTh;             //[0, 127]
    AK_U8        u8MfactorSlop;         //[0, 15]
    AK_U8         u8MotionStatTh;            //[0, 15]
    AK_U8        u8SfactorStatTh;        //[0, 3]
    AK_U8         u8MotionFilter;            //[0,15]
    AK_U8         u8MotionAreaExpand;     //[0, 1]
    AK_U8         u8LumStr[32];                //[0, 15]
    AK_U16        u16TMfTh1;     //[0, 8191],default:300(GUI edit)
    AK_U16        u16TMfTh2;    //[0, 8191],default:500(GUI edit)
    AK_U16        u16YnrCalcK;        //[0,65535](GUI edit)
    AK_U16        u16YnrWeightTbl[17];//ynr_strength(GUI edit)
    AK_U16        u16TYTh1;        //[0, 511],default:48(GUI edit)
    AK_U16        u16TYTh2;        //[0, 511],default:16(GUI edit)
    AK_U16        u16YUvTh1;        //[0, 511],default:48(GUI edit)
    AK_U16        u16YUvTh2;        //[0, 511],default:16(GUI edit)
    AK_U16        u16MdTh;            //[0, 65535]
    AK_U16        u16Weight4_7X5;    //[0,8695]
    AK_U16      u16TnrMotionFlagTh;
}ISP_3DNR_S;
```

<br/>

&emsp;&emsp;【Members】

| **Member**              | **Description**                   |
| ------------------- | ------------------------------ |
| u8TnrEnable         | 3DNR enable: 0 disabled, 1 enabled |
| u8TnrRefFrameFormat | Reference-frame compression format, [0,2] |
| u8YnrDPCStr         | Filter-strength correlation coefficient, [0,127] |
| u8YnrDPCCap         | Maximum filter strength, [0,127] |
| u8YnrDPCDiffGain    | Filter-strength adjustment lookup table, [0,7] |
| u8YnrK              | Y-domain 2D-filter noise-reduction coefficient, [0,15] |
| u8YnrLumStr         | Noise-reduction strength lookup table by luminance, [0,15] |
| u8YlpK1             | Y-domain 5\*5-region mean-difference weight, [0,15] |
| u8YlpK2             | Y-domain 3\*3-region mean-difference weight, [0,15] |
| u8YDiffUVWgt        | UV auxiliary-component weight, [0,15] |
| u8YDiffEdgeWgt      | Gradient auxiliary-component weight, [0,15] |
| u8TYLow1            | Y-domain spatiotemporal filter-strength interpolation reference parameter 1, [0,127] |
| u8TYLow2            | Y-domain spatiotemporal filter-strength interpolation reference parameter 2, [0,127] |
| u8TYK1              | Maximum temporal-filter strength for static Y-domain regions, [0,127] |
| u8TYK2              | Maximum temporal-filter strength for moving Y-domain regions, [0,127] |
| u8TYExK             | Temporal-filter strength fine adjustment for static Y-domain regions, [0,15] |
| u8TYKslop1          | Spatiotemporal filter-weight interpolation for static Y-domain regions, [0,127] |
| u8TYKslop2          | Spatiotemporal filter-weight interpolation for moving Y-domain regions, [0,127] |
| u8TYSrcChooseKTh    | Y-domain temporal-filter base-selection threshold, [0,127] |
| u8TYUpdateTh        | Temporal-filter update threshold, [0,15] |
| u8UvnrK             | UV-domain 2D-filter noise-reduction coefficient, [0,15] |
| u8UvlpK1            | UV-domain 3*3-region mean-difference weight 1, [0,15] |
| u8UvlpK2            | UV-domain 3*3-region mean-difference weight 2, [0,15] |
| u8TUvDiffScale      | UV-domain regional frame-difference scaling threshold, [0,15] |
| u8TUvKLow1          | UV-domain spatiotemporal filter-strength interpolation reference parameter 1, [0,127] |
| u8TUvKLow2          | UV-domain spatiotemporal filter-strength interpolation reference parameter 2, [0,127] |
| u8TUvK1             | Maximum temporal-filter strength for static UV-domain regions, [0,127] |
| u8TUvK2             | Maximum temporal-filter strength for moving UV-domain regions, [0,127] |
| u8TUvExK            | Temporal-filter strength fine adjustment for static UV-domain regions, [0,15] |
| u8TUvKslop1         | Spatiotemporal filter-weight interpolation for static UV-domain regions, [0,127] |
| u8TUvKslop2         | Spatiotemporal filter-weight interpolation for moving UV-domain regions, [0,127] |
| u8TUvSrcChooseKTh   | UV-domain temporal-filter base-selection threshold, [0,127] |
| u8MfactorKTh        | Pixel-sharpening-factor adjustment reference threshold, [0,127] |
| u8MfactorSlop       | Sharpening-factor adjustment smoothing parameter, [0,15] |
| u8MotionStatTh      | Motion-statistics threshold, [0,15] |
| u8SfactorStatTh     | Texture-statistics threshold, [0,3] |
| u8MotionFilter      | Motion-detection result filtering parameter, [0,15] |
| u8MotionAreaExpand  | Motion-boundary region-expansion enable, [0,1] |
| u8LumStr            | Frame-difference adjustment lookup table, [0,15] |
| u16TMfTh1           | Static-block decision threshold, [0,8191] |
| u16TMfTh2           | Moving-block decision threshold, [0,8191] |
| u16YnrCalcK         | Gaussian-weight calculation parameter, [0,65535] |
| u16YnrWeightTbl     | Gaussian-weight table, [0,1023] |
| u16TYTh1            | Temporal-filter weight-selection threshold for static Y-domain regions, [0,511] |
| u16TYTh2            | Temporal-filter weight-selection threshold for moving Y-domain regions, [0,511] |
| u16YUvTh1           | Temporal-filter weight-selection threshold for static UV-domain regions, [0,511] |
| u16YUvTh2           | Temporal-filter weight-selection threshold for moving UV-domain regions, [0,511] |
| u16MdTh             | Motion-level parameter, [0,65535] |
| u16Weight4_7X5      | Center-pixel weight for 7*5-neighborhood noise reduction, [0,8695] |
| u16TnrMotionFlagTh  | Moving/static-block decision threshold, [0,1024] |

&emsp;&emsp;【Related function interface】

&emsp;&emsp;ISP_3DNR_ATTR_S

<br/>

### **ISP_3DNR_ATTR_S **

&emsp;&emsp;【Description】

&emsp;&emsp;3D noise-reduction attribute structure.

&emsp;&emsp;【Definition】

```c
typedef struct  akISP_3DNR_ATTR_S {
    AK_U8             u8TnrDebugOutput;    //[0,1]
    AK_U8           u8MainTnrEnable;
    ISP_OP_TYPE_E    en3dnrMode;

    ISP_3DNR_S      stManual3dnr;
    ISP_3DNR_S      stLinkage3dnr[12];
} ISP_3DNR_ATTR_S;
```

&emsp;&emsp;【Members】

| **Member**           | **Description**         |
| ---------------- | -------------------- |
| u8TnrDebugOutput | 3DNR debug-mode bit, [0,1] |
| u8MainTnrEnable  | Master 3DNR enable, [0,1] |
| en3dnrMode       | Mode selection: 0 manual, 1 linked |
| stManual3dnr     | Manual 3DNR parameters |
| stLinkage3dnr    | Linked 3DNR parameters |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_ISP_Get3dnrAttr(AK_S32 s32GrpId, ISP_3DNR_ATTR_S *pst3dnrAttr);
    AK_S32 AK_MPI_ISP_Set3dnrAttr(AK_S32 s32GrpId, ISP_3DNR_ATTR_S *pst3dnrAttr);
```

<br/>

### **ISP_LENS_COEF_S**

&emsp;&emsp;【Description】

&emsp;&emsp;Coefficient structure.

&emsp;&emsp;【Definition】

```c
typedef struct akISP_LENS_COEF_S
{
    AK_U16 u16CoefB[10];    //[0,255]
    AK_U16 u16CoefC[10];    //[0,1023]
} ISP_LENS_COEF_S;
```

&emsp;&emsp;【Members】

| **Member**   | **Description**      |
| -------- | ----------------- |
| u16CoefB | Slope of the piecewise fitted line B\*Rx+C |
| u16CoefC | Intercept of the piecewise fitted line B\*Rx+C |
| <br/>    |                   |

### **ISP_LSC_ATTR_S**

&emsp;&emsp;【Description】

&emsp;&emsp;Lens-shading-correction information structure.

&emsp;&emsp;【Definition】

```c
typedef struct akISP_LSC_ATTR_S
{
    AK_U8               u16LscMode;
    AK_U8               u16LinkageStrength[13];  //[0,1023]
    AK_U16                u16LscEnable;
    //the reference point of lens correction
    AK_U16                u16Xref;      //[0,4096]
    AK_U16                u16Yref;      //[0,4096]
    AK_U16                u16Lsc_shift;   //[0,15]
    ISP_LENS_COEF_S    stLscRCoef;
    ISP_LENS_COEF_S    stLscGrCoef;
    ISP_LENS_COEF_S    stLscGbCoef;
    ISP_LENS_COEF_S    stLscBCoef;
    //the range of ten segment
    AK_U16                u16Range[10];   //[0,1023]
} ISP_LSC_ATTR_S;
```

<br/>

&emsp;&emsp;【Members】

| **Member**             | **Description**              |
| ------------------ | ------------------------- |
| u16LscEnable       | LSC enable |
| u16Xref            | Horizontal coordinate of the luminance center |
| u16Yref            | Vertical coordinate of the luminance center |
| u16Lsc_shift       | Radius offset; the controlled radius has 10 valid bits |
| stLscRCoef         | R-channel piecewise fitted-line parameters |
| stLscGrCoef        | Gr-channel piecewise fitted-line parameters |
| stLscGbCoef        | Gb-channel piecewise fitted-line parameters |
| stLscBCoef         | B-channel piecewise fitted-line parameters |
| u16Range           | Radius range for piecewise LSC correction |
| u16LscMode         | LSC correction mode: 0 manual, 1 automatic |
| u16LinkageStrength | LSC correction-strength coefficient for each Env; larger values give stronger correction |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_ISP_GetLscAttr(AK_S32 s32GrpId, ISP_LSC_ATTR_S *pstLsc);
    AK_S32 AK_MPI_ISP_SetLscAttr(AK_S32 s32GrpId, ISP_LSC_ATTR_S *pstLsc);
```

<br/>

### **ISP_SENSOR_REG_INFO_S**

&emsp;&emsp;【Description】

&emsp;&emsp;Sensor-register information structure.

&emsp;&emsp;【Definition】

```c
typedef struct akISP_SENSOR_REG_INFO_S {
    AK_U16 u16RegAddr;
    AK_U16 u16Value;
} ISP_SENSOR_REG_INFO_S;
```

&emsp;&emsp;【Members】

| **Member**     | **Description** |
| ---------- | ------ |
| u16RegAddr | Register address |
| u16Value   | Register value |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_ISP_GetSensorReg(AK_S32 s32GrpId, ISP_SENSOR_REG_INFO_S *pstSensorRegInfo);
```

<br/>

### **ISP_EX_ZWEIGHT_ATTR_S**

&emsp;&emsp;【Description】

&emsp;&emsp;Extended-area weight structure.

&emsp;&emsp;【Definition】

```c
typedef struct akISP_EX_ZWEIGHT_ATTR_S {
    AK_U8    u8WinWeight[8][16];
    AK_U8    u8ExZoneWeightStr;
} ISP_EX_ZWEIGHT_ATTR_S;
```

&emsp;&emsp;【Members】

| **Member**            | **Description**                |
| ----------------- | --------------------------- |
| u8WinWeight       | Priority-region attribute, [0,1]: 0 non-priority, 1 priority |
| u8ExZoneWeightStr | Priority-region exposure-weight attribute, [0,15] |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_ISP_GetExZweightAttr(AK_S32 s32GrpId, ISP_EX_ZWEIGHT_ATTR_S *pstExZweight);
    AK_S32 AK_MPI_ISP_SetExZweightAttr(AK_S32 s32GrpId, ISP_EX_ZWEIGHT_ATTR_S *pstExZweight)
```

<br/>

### **ISP_EFFECT_ATTR_S**

&emsp;&emsp;【Description】

&emsp;&emsp;YUV-effect structure.

&emsp;&emsp;【Definition】

```c
typedef struct akISP_EFFECT_ATTR_S
{
    AK_U8   u8YuvOutEnable;
    AK_U8   u8DarkMarginEn;
    AK_U8   u8YA;      // [0, 255]
    AK_S8   s8YB;     //[-128, 127]
    AK_S16  s16UvA;    //[-256, 255]
    AK_S16  s16UvB;    //[-256, 255]
} ISP_EFFECT_ATTR_S;
```

&emsp;&emsp;【Members】

| **Member**         | **Description**           |
| -------------- | ---------------------- |
| u8YA           | Luminance-gain parameter, [0,255] |
| s8YB           | Luminance-offset parameter, [-128,127] |
| s16UvA         | UV-gain parameter, [-256,255] |
| s16UvB         | UV-offset parameter, [-256,255] |
| u8DarkMarginEn | Darkening enable: 0 disabled, 1 enabled |
| u8YuvOutEnable | YUV-output enable: 0 disabled, 1 enabled |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_ISP_SetYuvEffectAttr(AK_S32 s32GrpId, ISP_EFFECT_ATTR_S *pstYuvEffect);
    AK_S32 AK_MPI_ISP_GetYuvEffectAttr(AK_S32 s32GrpId, ISP_EFFECT_ATTR_S *pstYuvEffect)
```

<br/>

### **ISP_RGB_GAMMA_S**

&emsp;&emsp;【Description】

&emsp;&emsp;RGB gamma-curve structure.

&emsp;&emsp;【Definition】

```c
typedef struct akISP_RGB_GAMMA_S {
    AK_U16  u16RgbGammaEnable;
    AK_U16  u16RGamma[129];   //10bit
    AK_U16  u16GGamma[129];   //10bit
    AK_U16  u16BGamma [129];  //10bit
    AK_U16  u16RKey[16];
    AK_U16  u16GKey[16];
    AK_U16  u16BKey[16];
} ISP_RGB_GAMMA_S;
```

&emsp;&emsp;【Members】

| **Member**          | **Description**                      |
| ----------------- | --------------------------- |
| u16RGamma         | R-channel gamma curve, [0,1023] |
| u16GGamma         | G-channel gamma curve, [0,1023] |
| u16BGamma         | B-channel gamma curve, [0,1023] |
| u16RKey           | R-channel curve key points, [0,128] |
| u16GKey           | G-channel curve key points, [0,128] |
| u16BKey           | B-channel curve key points, [0,128] |
| u16RgbGammaEnable | RGB-gamma enable: 0 disabled, 1 enabled |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_ISP_SetRgbGammaAttr(AK_S32 s32GrpId, ISP_RGB_GAMMA_ATTR_S *pstRgbGamma);
    AK_S32 AK_MPI_ISP_GetRgbGammaAttr(AK_S32 s32GrpId, ISP_RGB_GAMMA_ATTR_S *pstRgbGamma);
```

<br/>

### **ISP_RGB_GAMMA_ATTR_S**

&emsp;&emsp;【Description】

&emsp;&emsp;RGB gamma-parameter structure.

&emsp;&emsp;【Definition】

```c
typedef struct akISP_RGB_GAMMA_ATTR_S {
    AK_U16      u16GainTh1;
    AK_U16      u16GainTh2;
    ISP_RGB_GAMMA_S  stLinkageRgbGamma[3];
} ISP_RGB_GAMMA_ATTR_S;
```

&emsp;&emsp;【Members】

| **Member**                 | **Description**       |
| ---------------------- | ------------------ |
| u16GainTh1, u16GainTh2 | Gamma-switching thresholds, [0,1023] |
| stLinkageRgbGamma      | Linked RGB gamma |

&emsp;&emsp;【Related function interface】

```c
     AK_S32 AK_MPI_ISP_SetRgbGammaAttr(AK_S32 s32GrpId, ISP_RGB_GAMMA_ATTR_S *pstRgbGamma);
    AK_S32 AK_MPI_ISP_GetRgbGammaAttr(AK_S32 s32GrpId, ISP_RGB_GAMMA_ATTR_S *pstRgbGamma);
```

<br/>

### **ISP_CONTRAST_S**

&emsp;&emsp;【Description】

&emsp;&emsp;Manual-contrast parameter structure.

&emsp;&emsp;【Definition】

```c
typedef struct  akISP_CONTRAST_S
{
     AK_U8   u8ContrastEnable;
     AK_U16  u16YContrast;  //[0,511]
     AK_S16  s16YShift;    //[0, 511]
} ISP_CONTRAST_S;
```

&emsp;&emsp;【Members】

| **Member**           | **Description**        |
| ---------------- | ------------------- |
| u8ContrastEnable | Manual-contrast enable |
| u16YContrast     | Manual contrast-enhancement coefficient, [0,511] |
| s16YShift        | Manual luminance black-balance offset coefficient, [0,511] |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_ISP_SetContrastAttr(AK_S32 s32GrpId, ISP_CONTRAST_ATTR_S *pstContrast);
    AK_S32 AK_MPI_ISP_GetContrastAttr(AK_S32 s32GrpId, ISP_CONTRAST_ATTR_S *pstContrast);
```

<br/>

### **ISP_AUTO_CONTRAST_S**

&emsp;&emsp;【Description】

&emsp;&emsp;Automatic-contrast parameter structure.

&emsp;&emsp;【Definition】

```c
typedef struct  akISP_AUTO_CONTRAST_S
{
    AK_U8   u8ContrastEnable;
    AK_U8   u8ShiftMax;    //[0, 127]
    AK_U16  u16DarkPixelArea; //[0, 511]
    AK_U16  u8DarkPixelRate;  //[1, 256]
} ISP_AUTO_CONTRAST_S;
```

&emsp;&emsp;【Members】

| **Member**           | **Description**         |
| ---------------- | -------------------- |
| u8ContrastEnable | Automatic-contrast enable |
| u16DarkPixelArea | Dark-luminance pixel region in the histogram, [0,511] |
| u8DarkPixelRate  | Dark-region pixel ratio, [1,256] |
| u8ShiftMax       | Maximum offset threshold, [0,127] |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_ISP_SetContrastAttr(AK_S32 s32GrpId, ISP_CONTRAST_ATTR_S *pstContrast);
    AK_S32 AK_MPI_ISP_GetContrastAttr(AK_S32 s32GrpId, ISP_CONTRAST_ATTR_S *pstContrast);
```

<br/>

### **ISP_CONTRAST_ATTR_S**

&emsp;&emsp;【Description】

&emsp;&emsp;Contrast-parameter structure.

&emsp;&emsp;【Definition】

```c
typedef struct  akISP_CONTRAST_ATTR_S
{
    ISP_OP_TYPE_E            enContrastMode;
    ISP_CONTRAST_S            stManualContrast;
    ISP_AUTO_CONTRAST_S    stLinkageContrast[12];
} ISP_CONTRAST_ATTR_S;
```

&emsp;&emsp;【Members】

| **Member**            | **Description**     |
| ----------------- | ---------------- |
| enContrastMode    | Contrast mode: 0 manual, 1 linked |
| stManualContrast  | Manual-contrast parameters |
| stLinkageContrast | Linked contrast-adjustment parameters |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_ISP_SetContrastAttr(AK_S32 s32GrpId, ISP_CONTRAST_ATTR_S *pstContrast);
    AK_S32 AK_MPI_ISP_GetContrastAttr(AK_S32 s32GrpId, ISP_CONTRAST_ATTR_S *pstContrast);
```

<br/>

### **ISP_LCE_S**

&emsp;&emsp;【Description】

&emsp;&emsp;Local-contrast-enhancement parameters.

&emsp;&emsp;【Definition】

```c
typedef struct akISP_LCE_S {
    AK_U8    u8LceEnable;
    AK_U8    u8LceUvAdjustEn;
    AK_U8   u8LceUvAdjustLevel;
    AK_U8    u8LceHeStr;
    AK_U8     u8LceHeStrLow;
    AK_U8   u8LceLumFilterK;//[0,8]
    AK_U8   u8LceSpatFilterK;//[0,8]
    AK_U8   u8LceTempFilterK;//[0,15]
    AK_U8   u8LceStrength[4][8];
} ISP_LCE_S;
```

&emsp;&emsp;【Members】

| **Member**             | **Description**             |
| ------------------ | ------------------------ |
| u8LceEnable        | Local-contrast-enhancement enable: 0 disabled, 1 enabled |
| u8LceUvAdjustEn    | UV-adjustment enable: 0 disabled, 1 enabled |
| u8LceUvAdjustLevel | UV-adjustment strength, [0,31] |
| u8LceHeStr         | Per-level luminance clipping threshold within a block, [0,255] |
| u8LceHeStrLow      | Dark-region luminance clipping threshold within a block, [0,255] |
| u8LceLumFilterK    | Luminance-filter coefficient, [0,8] |
| u8LceSpatFilterK   | Spatial-filter coefficient, [0,8] |
| u8LceTempFilterK   | Temporal-filter coefficient, [0,15] |
| u8LceStrength      | Local-contrast strength weight, [0,255] |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_ISP_SetLceAttr(AK_S32 s32GrpId, ISP_LCE_ATTR_S *pstLce);
    AK_S32 AK_MPI_ISP_GetLceAttr(AK_S32 s32GrpId, ISP_LCE_ATTR_S *pstLce);
```

<br/>

### **ISP_LCE_ATTR_S**

&emsp;&emsp;【Description】

&emsp;&emsp;Local-contrast-enhancement parameter structure.

&emsp;&emsp;【Definition】

```c
typedef struct akISP_LCE_ATTR_S{
    ISP_OP_TYPE_E  enLceMode;
    ISP_LCE_S      stManualLce;
    ISP_LCE_S      stLinkageLce[12];
} ISP_LCE_ATTR_S;
```

&emsp;&emsp;【Members】

| **Member**       | **Description**         |
| ------------ | -------------------- |
| enLceMode    | Local-contrast-enhancement mode: 0 manual, 1 linked |
| stManualLce  | Manual local-contrast enhancement |
| stLinkageLce | Linked local-contrast enhancement |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_ISP_SetLceAttr(AK_S32 s32GrpId, ISP_LCE_ATTR_S *pstLce);
    AK_S32 AK_MPI_ISP_GetLceAttr(AK_S32 s32GrpId, ISP_LCE_ATTR_S *pstLce);
```

<br/>

### **ISP_Y_GAMMA_ATTR_S**

&emsp;&emsp;【Description】

&emsp;&emsp;Y-gamma parameter structure.

&emsp;&emsp;【Definition】

```c
typedef struct akISP_Y_GAMMA_ATTR_S
{
    AK_U16  u16YgammaEnable;
    AK_U8   u8YgammaUvAdjustEnable;
    AK_U8   u8YgammaUvAdjustLevel;
    AK_U16  u16Ygamma[129];    //10bit
    AK_U16  u16YgammaKey[16];
    AK_U16  u16YgammaCnoiseYth1;
    AK_U16  u16YgammaCnoiseYth2 ;
    AK_U16  u16YgammaCnoiseGain ;
} ISP_Y_GAMMA_ATTR_S;
```

&emsp;&emsp;【Members】

| **Member**                 | **Description**                 |
| ---------------------- | ---------------------------- |
| u16Ygamma              | Y-gamma luminance lookup table, [0,1023] |
| u16YgammaKey           | Curve key points, [0,128] |
| u8YgammaUvAdjustEnable | Y-gamma UV-adjustment enable: 0 disabled, 1 enabled |
| u8YgammaUvAdjustLevel  | UV-adjustment strength, [0,31] |
| u16YgammaCnoiseYth1    | Chroma-difference suppression threshold 1, [0,1023] |
| u16YgammaCnoiseYth2    | Chroma-difference suppression threshold 2, [0,1023] |
| u16YgammaEnable        | Y-gamma enable: 0 disabled, 1 enabled |
| u16YgammaCnoiseGain    | UV-adjustment gain, [0,1023] |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_ISP_SetYgammaAttr(AK_S32 s32GrpId, ISP_Y_GAMMA_ATTR_S *pstYgamma);
    AK_S32 AK_MPI_ISP_GetYgammaAttr(AK_S32 s32GrpId, ISP_Y_GAMMA_ATTR_S *pstYgamma);
```

<br/>

### **ISP_DAY_NIGHT_MODE_E**

&emsp;&emsp;【Description】

&emsp;&emsp;Day/night mode.

&emsp;&emsp;【Definition】

```c
typedef enum akISP_DAY_NIGHT_MODE_E {
    MODE_DAY,
    MODE_NIGHT,
    MODE_USR_DEFINE_1,
    MODE_USR_DEFINE_2,
    MODE_USR_DEFINE_3,
    MODE_NUM
} ISP_DAY_NIGHT_MODE_E;
```

&emsp;&emsp;【Members】

| **Member**            | **Description** |
| ----------------- | ------ |
| MODE_DAY          | Day |
| MODE_NIGHT        | Night vision |
| MODE_USR_DEFINE_1 | User-defined 1 |
| MODE_USR_DEFINE_2 | User-defined 2 |
| MODE_USR_DEFINE_3 | User-defined 2 |
| MODE_NUM          | Total number of modes |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_ISP_SwitchMode(AK_S32 s32GrpId, ISP_DAY_NIGHT_MODE_E enMode);
```

<br/>

### **ISP_NIGHT_TYPE_E**

&emsp;&emsp;【Description】

&emsp;&emsp;Night-vision type.

&emsp;&emsp;【Definition】

```c
typedef enum akISP_NIGHT_TYPE_E {
    IR_LED_NIGHT,
    WHITE_LED_NIGHT,
    BLACKLIGHT_NIGHT,
    TYPE_NUM
} ISP_NIGHT_TYPE_E;
```

&emsp;&emsp;【Members】

| **Member**           | **Description** |
| ---------------- | ------ |
| IR_LED_NIGHT     | IR night vision |
| WHITE_LED_NIGHT  | White-light night vision |
| BLACKLIGHT_NIGHT | Black-light color night vision |
| TYPE_NUM         | Total number of types |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_ISP_SetSoftPsParam(AK_S32 s32GrpId, ISP_SOFT_PS_ATTR_S *pstParam);
```

<br/>

### **ISP_IR_LED_NIGHT_PARAM_S**

&emsp;&emsp;【Description】

&emsp;&emsp;IR night-vision software-photosensitivity parameters.

&emsp;&emsp;【Definition】

```c
typedef struct akISP_IR_LED_NIGHT_PARAM_S {
    AK_U32    u32DayToNightLum;    // day to night lum value
    AK_U32    u32NightToDayLum;    // night to day lum value
    AK_U32    u32AwbNightDisMin;
    AK_U32    u32AwbNightDisMax;
    AK_U32    u32GainR;
    AK_S32    s32OffsetR;
    AK_U32    u32GainB;
    AK_S32    s32OffsetB;
    AK_U32    u32GainRB;
    AK_S32    s32OffsetRB;
    AK_U32    u32BlkCheckFlag;
    AK_U32    u32LowLumiTh;
    AK_U32    u32HighLumiTh;
    AK_U32    u32NonInfraredRatioTh;
    AK_U32    u32RevisedDisMaxRatio;
} ISP_IR_LED_NIGHT_PARAM_S;
```

&emsp;&emsp;【Members】

| **Member**                | **Description**                                                                                                                                                          |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| u32DayToNightLum      | Luminance for switching from day to night vision. Above this threshold, luminance satisfies the night-vision condition. |
| u32NightToDayLum      | Luminance for switching from night vision to day. Below this threshold, luminance satisfies the day condition. |
| u32AwbNightDisMin     | Reserved; not currently used |
| u32AwbNightDisMax     | RGB-difference threshold for switching from night vision to day. Above this threshold, the RGB difference satisfies the day condition. |
| u32GainR              | R gain, default 1024. `u32GainR`, `s32OffsetR`, `u32GainB`, `s32OffsetB`, `u32GainRB`, and `s32OffsetRB` are linearization parameters. For sensors whose QE curves differ substantially under 850 nm infrared light, they linearize the responses to equalize the sensor output, making day/night decisions easier. |
| s32OffsetR            | R offset, default 0 |
| u32GainB              | B gain, default 1024 |
| s32OffsetB            | B offset, default 0 |
| u32GainRB             | RB gain, default 1024 |
| s32OffsetRB           | RB offset, default 0 |
| u32BlkCheckFlag       | Block-difference detection enable: 0 use whole-image difference detection, 1 enable block-difference detection |
| u32LowLumiTh          | Low-luminance threshold for valid blocks (block-difference detection), range [0,255] |
| u32HighLumiTh         | High-luminance threshold for valid blocks (block-difference detection), range (0,255] |
| u32NonInfraredRatioTh | Percentage threshold of valid blocks that are non-infrared (block-difference detection), range (0,100) |
| u32RevisedDisMaxRatio | DisMax increase ratio, range [0,1024] |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_ISP_SetSoftPsParam(AK_S32 s32GrpId, ISP_SOFT_PS_ATTR_S *pstParam);
```

<br/>

### **ISP_WHITE_LED_NIGHT_PARAM_S**

&emsp;&emsp;【Description】

&emsp;&emsp;White-light night-vision software-photosensitivity parameters.

&emsp;&emsp;【Definition】

```c
typedef struct akISP_WHITE_LED_NIGHT_PARAM_S {
    AK_U32    u32DayToNightLum;    // day to night lum value
    AK_U32    u32NightToDayLum;    // night to day lum value
    AK_U32    u32HighlightLumiTh;
    AK_U32    u32HighlightBlkCntMax;
} ISP_WHITE_LED_NIGHT_PARAM_S;
```

&emsp;&emsp;【Members】

| **Member**                | **Description**                  |
| --------------------- | ----------------------------- |
| u32DayToNightLum      | Luminance for switching from day to night vision; above this threshold, luminance satisfies the night-vision condition |
| u32NightToDayLum      | Luminance for switching from night vision to day; below this threshold, luminance satisfies the day condition |
| u32HighlightLumiTh    | Highlight-luminance threshold |
| u32HighlightBlkCntMax | Maximum number of highlight blocks |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_ISP_SetSoftPsParam(AK_S32 s32GrpId, ISP_SOFT_PS_ATTR_S *pstParam);
```

<br/>

### **ISP_BLACKLIGHT_NIGHT_PARAM_S**

&emsp;&emsp;【Description】

&emsp;&emsp;Black-light color-night-vision software-photosensitivity parameters.

&emsp;&emsp;【Definition】

```c
typedef struct akISP_BLACKLIGHT_NIGHT_PARAM_S {
    AK_U32  u32DayToNightAGain;
    AK_U32  u32DayToNightDGain;
    AK_U32  u32DayToNightIspDGain;
    AK_U32  u32DayToNightExpTime;
    AK_U32  u32DayToNightDarkPixelRate;
    AK_U32  u32NightToDayAGain;
    AK_U32  u32NightToDayDGain;
    AK_U32  u32NightToDayIspDGain;
    AK_U32  u32NightToDayExpTime;
    AK_U32  u32NightToDayDarkPixelRate;
} ISP_BLACKLIGHT_NIGHT_PARAM_S;
```

&emsp;&emsp;【Members】

| **Member**                     | **Description**      |
| -------------------------- | ----------------- |
| u32DayToNightAGain         | Analog gain for switching from day to night vision |
| u32DayToNightDGain         | Digital gain for switching from day to night vision |
| u32DayToNightIspDGain      | ISP digital gain for switching from day to night vision |
| u32DayToNightExpTime       | Exposure time for switching from day to night vision |
| u32DayToNightDarkPixelRate | Dark-region pixel ratio for switching from day to night vision |
| u32NightToDayAGain         | Analog gain for switching from night vision to day |
| u32NightToDayDGain         | Digital gain for switching from night vision to day |
| u32NightToDayIspDGain      | ISP digital gain for switching from night vision to day |
| u32NightToDayExpTime       | Exposure time for switching from night vision to day |
| u32NightToDayDarkPixelRate | Dark-region pixel ratio for switching from night vision to day |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_ISP_SetSoftPsParam(AK_S32 s32GrpId, ISP_SOFT_PS_ATTR_S *pstParam);
```

<br/>

### **ISP_SOFT_PS_ATTR_S**

&emsp;&emsp;【Description】

&emsp;&emsp;Day/night switching parameter structure without a photosensor (new algorithm).

&emsp;&emsp;【Definition】

```c
typedef struct akISP_SOFT_PS_ATTR_S {
    ISP_NIGHT_TYPE_E    enNightType;
    AK_U32              u32DayCheckFrameNum;
    AK_U32              u32NightCheckFrameNum;
    AK_U32              u32ExpStableCheckFrameNum;
    AK_S32              s32ExpStableTimeOutMs;
    AK_U32              u32LockCntTh;
    AK_U32              u32LockTimeMs;

    union
    {
        ISP_IR_LED_NIGHT_PARAM_S        stIrLedNightParm;
        ISP_WHITE_LED_NIGHT_PARAM_S     stWhiteLedNightParm;
        ISP_BLACKLIGHT_NIGHT_PARAM_S    stBlackLightNightParm;
    };
} ISP_SOFT_PS_ATTR_S;
```

&emsp;&emsp;【Members】

| **Member**                    | **Description**                                                                                                                                                               |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| enNightType               | Night-vision type |
| u32DayCheckFrameNum       | Detection-frame count in the day state |
| u32NightCheckFrameNum     | Detection-frame count in the night-vision state |
| u32ExpStableCheckFrameNum | Frame count for exposure-stability detection |
| s32ExpStableTimeOutMs     | Exposure-stability wait timeout, in milliseconds |
| u32LockCntTh              | Switching-count threshold. Every two minutes, the program counts day/night transitions (day-to-night and night-to-day each count once). If the count reaches this value, it locks in night vision immediately if already in night vision, or after the next switch to night vision if currently in day mode. If no switch to night vision occurs within two minutes, oscillation is considered to have stopped and no lock is applied. Setting either `lock_cnt_th` or `lock_time_ms` to 0 disables oscillation locking. |
| u32LockTimeMs             | Lock duration in ms. Switching resumes when this duration expires or EV changes by more than 10%. Setting either `lock_cnt_th` or `lock_time_ms` to 0 disables oscillation locking. |
| stIrLedNightParm          | IR night-vision software-photosensitivity parameters |
| stWhiteLedNightParm       | White-light night-vision software-photosensitivity parameters |
| stBlackLightNightParm     | Black-light color-night-vision software-photosensitivity parameters |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_ISP_SetSoftPsParam(AK_S32 s32GrpId, ISP_SOFT_PS_ATTR_S *pstParam);
```

<br/>

### **ISP_NON_INFRARED_RATIO_ATTR_S**

&emsp;&emsp;【Description】

&emsp;&emsp;Parameter structure for calculating the non-infrared ratio.

&emsp;&emsp;【Definition】

```c
typedef struct akISP_NON_INFRARED_RATIO_ATTR_S {
    AK_U32    u32AwbNightDisMax;
    AK_U32    u32GainR;
    AK_S32    s32OffsetR;
    AK_U32    u32GainB;
    AK_S32    s32OffsetB;
    AK_U32    u32GainRB;
    AK_S32    s32OffsetRB;
    AK_U32    u32LowLumiTh;
    AK_U32    u32HighLumiTh;
    AK_U32    u32RevisedDisMaxRatio;
}ISP_NON_INFRARED_RATIO_ATTR_S;
```

&emsp;&emsp;【Members】

| **Member**                | **Description**                                                                                                                                              |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| u32AwbNightDisMax     | RGB-difference threshold for switching from night vision to day; above it, the RGB difference satisfies the day condition |
| u32GainR              | R gain, default 1024. `gain_r`, `offset_r`, `gain_b`, `offset_b`, `gain_rb`, and `offset_rb` linearize differing sensor responses under 850 nm infrared light to make day/night decisions easier. |
| s32OffsetR            | R offset, default 0 |
| u32GainB              | B gain, default 1024 |
| s32OffsetB            | B offset, default 0 |
| u32GainRB             | RB gain, default 1280 |
| s32OffsetRB           | RB offset, default 0 |
| u32LowLumiTh          | Low-luminance threshold for valid blocks (block-difference detection), range [0,255] |
| u32HighLumiTh         | High-luminance threshold for valid blocks (block-difference detection), range (0,255] |
| u32RevisedDisMaxRatio | DisMax increase ratio, range [0,1024] |

&emsp;&emsp;【Related function interface】

```c
AK_S32 AK_MPI_ISP_GetNonInfraredRatio(AK_S32 s32GrpId,
    ISP_NON_INFRARED_RATIO_ATTR_S *pstNirAttr, AK_U32 *pu32NonInfraredRatio);
```

<br/>

### **ISP_3D_NR_REF_SIZE_STAT_INFO**

&emsp;&emsp;【Description】

&emsp;&emsp;3DNR buffer-usage statistics structure.

&emsp;&emsp;【Definition】

```c
typedef struct akISP_3D_NR_REF_SIZE_STAT_INFO{
    AK_U32  u32RefSizeStatis[3];/* 0-y used size; 1-u used size; 2-v used size*/
}ISP_3D_NR_REF_SIZE_STAT_INFO;
```

&emsp;&emsp;【Members】

| **Member**           | **Description**                                                  |
| ---------------- | ------------------------------------------------------------- |
| u32RefSizeStatis | 3DNR buffer usage. Index 0 is the Y-component size, index 1 the U-component size, and index 2 the V-component size. |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_ISP_Get3dnrRefSizeStat(AK_S32 s32GrpId, ISP_3D_NR_REF_SIZE_STAT_INFO *pstRefSize);
```

<br/>

## Get Version Information

### **AK_MPI_ISP_GetIspSdkVersion**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the ISP SDK library version.

&emsp;&emsp;【Syntax】

```c
    const char* AK_MPI_ISP_GetIspSdkVersion(AK_VOID);
```

&emsp;&emsp;【Return values】

| **Return value**     | **Description** |
| ----------- | ------ |
| ISP SDK library version | Success |
| NULL | Failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

<br/>

## Get MD/OD Information

### **AK_MPI_ISP_GetOdInfo**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the data required by OD. Higher layers can use the OD statistics to implement an occlusion-detection algorithm.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_GetOdInfo(AK_S32 s32GrpId, ISP_OD_INFO_S *pstOd);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**                                         | **Input/Output** |
| -------- | ---------------------------------------------- | --------- |
| s32GrpId | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| pstOd    | OD data information                                         | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

### **AK_MPI_ISP_GetMdStat**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets MD statistics. Higher layers can use them to implement a motion-detection algorithm.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_GetMdStat(AK_S32 s32GrpId, ISP_MD_INFO_S *pstMd);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**                                         | **Input/Output** |
| -------- | ---------------------------------------------- | --------- |
| s32GrpId | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| pstMd    | MD statistics                                         | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

## Set/Get Current Image Effects

### AK_MPI_ISP_SetEffect

&emsp;&emsp;【Description】

&emsp;&emsp;Sets an effect. Because the low-level ISP API is complex and has many parameters, the effect module provides a simple personalized-effect API similar to the controls on a television or monitor. Avoid using `AK_MPI_ISP_SetEffect` for flip/mirror settings; use `AK_MPI_ISP_SwitchFlipMirror` instead.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_SetEffect(AK_S32 s32GrpId, ISP_EFFECT_TYPE_E enType, AK_S32 s32Value);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**                                         | **Input/Output** |
| -------- | ---------------------------------------------- | --------- |
| s32GrpId | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| enType   | Effect type                                           | Input |
| s32Value | Effect value                                           | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description**   |
| -------------------------- | -------- |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Low-level device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

> **Note:** If Auto Y Gain is selected in the YUV effect module of the ISP configuration file, the Contrast parameter cannot be set.

<br/>

### **AK_MPI_ISP_GetEffect**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the effect.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_GetEffect(AK_S32 s32GrpId, ISP_EFFECT_TYPE_E enType, AK_S32 *ps32Value);
```

&emsp;&emsp;【Parameters】

| **Parameter**  | **Description**                                         | **Input/Output** |
| --------- | ---------------------------------------------- | --------- |
| s32GrpId  | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| enType    | Effect type                                           | Input |
| ps32Value | Effect value                                           | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                 | **Description** |
| ----------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

## Set/Get Privacy-Mask Parameters

### **AK_MPI_PP_MaskSetArea**

&emsp;&emsp;【Description】

&emsp;&emsp;Sets a mask area.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_PP_MaskSetArea(AK_S32 s32GrpId, AK_S32 s32ChnId, const PP_MASK_AREA_INFO_S *pstArea);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**                                               | **Input/Output** |
| -------- | ---------------------------------------------------- | --------- |
| s32GrpId | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID.       | Input |
| s32ChnId | VPSS channel ID, [0,1]. The main channel defaults to ChnId 0 and the secondary channel to ChnId 1. The third channel is not supported. | Input |
| pstArea  | Mask-area parameters                                             | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

### **AK_MPI_PP_MaskGetArea**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets a mask area.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_PP_MaskGetArea(AK_S32 s32GrpId, AK_S32 s32ChnId, PP_MASK_AREA_INFO_S *pstArea);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**                                               | **Input/Output** |
| -------- | ---------------------------------------------------- | --------- |
| s32GrpId | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID.       | Input |
| s32ChnId | VPSS channel ID, [0,1]. The main channel defaults to ChnId 0 and the secondary channel to ChnId 1. The third channel is not supported. | Input |
| pstArea  | Mask-area parameters                                             | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

### **AK_MPI_PP_MaskSetColor**

&emsp;&emsp;【Description】

&emsp;&emsp;Sets the mask color.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_PP_MaskSetColor(AK_S32 s32GrpId, const PP_MASK_COLOR_INFO_S *pstColor);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**                                         | **Input/Output** |
| -------- | ---------------------------------------------- | --------- |
| s32GrpId | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| pstColor | Mask-color parameters                                       | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

### **AK_MPI_PP_MaskGetColor**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the mask color.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_PP_MaskGetColor(AK_S32 s32GrpId, PP_MASK_COLOR_INFO_S *pstColor);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**                                         | **Input/Output** |
| -------- | ---------------------------------------------- | --------- |
| s32GrpId | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| pstColor | Mask-color parameters                                       | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

## Set Box-Drawing Parameters

### AK_MPI_PP_SetBoxColorTable

&emsp;&emsp;【Description】

&emsp;&emsp;Sets the box-drawing palette.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_PP_SetBoxColorTable(AK_S32 s32GrpId, AK_U32 *pu32ColorTable);
```

&emsp;&emsp;【Parameters】

| **Parameter**       | **Description**                                                                                                 | **Input/Output** |
| -------------- | ------------------------------------------------------------------------------------------------------ | --------- |
| s32GrpId       | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID.                                                         | Input |
| pu32ColorTable | Seven-entry box-drawing palette. Each color is 32 bits, ordered from low to high as R, G, B, A. A is opacity: 0 fully transparent, 255 opaque. R: bits 0-7, G: 8-15, B: 16-23, A: 24-31. | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

### **AK_MPI_PP_DrawBox**

&emsp;&emsp;【Description】

&emsp;&emsp;Sets box-drawing parameters.

&emsp;&emsp;【Syntax】

```c
    int AK_MPI_PP_DrawBox(AK_S32 s32GrpId, AK_S32 s32ChnId, PP_BOX_GROUP_S *pstBoxGroup);
```

&emsp;&emsp;【Parameters】

| **Parameter**    | **Description**                                               | **Input/Output** |
| ----------- | ---------------------------------------------------- | --------- |
| s32GrpId    | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID.       | Input |
| s32ChnId    | VPSS channel ID, [0,1]. The main channel defaults to ChnId 0 and the secondary channel to ChnId 1. The third channel is not supported. | Input |
| pstBoxGroup | Box-drawing parameters                                                 | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

## Get/Set Autofocus Parameters and Status

### **AK_MPI_ISP_SetAfAttr**

&emsp;&emsp;【Description】

&emsp;&emsp;Sets the autofocus structure.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_SetAfAttr(AK_S32 s32GrpId, ISP_AF_ATTR_S *pstAfAttr);
```

&emsp;&emsp;【Parameters】

| **Parameter**  | **Description**                                         | **Input/Output** |
| --------- | ---------------------------------------------- | --------- |
| s32GrpId  | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| pstAfAttr | AF structure information                                         | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.so and libplat_isp_sdk.so, or libplat_vpss.a and libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

### **AK_MPI_ISP_GetAfAttr**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the autofocus structure.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_GetAfAttr(AK_S32 s32GrpId, ISP_AF_ATTR_S *pstAfAttr);
```

&emsp;&emsp;【Parameters】

| **Parameter**  | **Description**                                         | **Input/Output** |
| --------- | ---------------------------------------------- | --------- |
| s32GrpId  | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| pstAfAttr | AF structure information                                         | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

### **AK_MPI_ISP_GetAfStat**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets autofocus statistics.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_GetAfStat(AK_S32 s32GrpId, ISP_AF_INFO_S *pstAfStat);
```

&emsp;&emsp;【Parameters】

| **Parameter**  | **Description**                                         | **Input/Output** |
| --------- | ---------------------------------------------- | --------- |
| s32GrpId  | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| pstAfStat | AF statistics                                         | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

## Get/Set Exposure Parameters and Status

### **AK_MPI_ISP_GetExpType**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets exposure-type information.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_GetExpType(AK_S32 s32GrpId, ISP_OP_TYPE_E *penExpType);
```

&emsp;&emsp;【Parameters】

| **Parameter**   | **Description**                                         | **Input/Output** |
| ---------- | ---------------------------------------------- | --------- |
| s32GrpId   | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| penExpType | Exposure-type information                                         | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

### **AK_MPI_ISP_SetExpType**

&emsp;&emsp;【Description】

&emsp;&emsp;Sets exposure-type information.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_SetExpType(AK_S32 s32GrpId, ISP_OP_TYPE_E enExpType);
```

&emsp;&emsp;【Parameters】

| **Parameter**  | **Description**                                         | **Input/Output** |
| --------- | ---------------------------------------------- | --------- |
| s32GrpId  | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| enExpType | Exposure-type information                                         | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

### **AK_MPI_ISP_GetAeRunInfo**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets automatic-exposure statistics.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_GetAeRunInfo(AK_S32 s32GrpId, ISP_AE_RUN_INFO_S *pstAeRunInfo);
```

&emsp;&emsp;【Parameters】

| **Parameter**     | **Description**                                         | **Input/Output** |
| ------------ | ---------------------------------------------- | --------- |
| s32GrpId     | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| pstAeRunInfo | Automatic-exposure statistics                                       | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

### **AK_MPI_ISP_GetAeAttr**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets automatic-exposure structure information.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_GetAeAttr(AK_S32 s32GrpId, ISP_AE_ATTR_S *pstAeAttr);
```

&emsp;&emsp;【Parameters】

| **Parameter**  | **Description**                                         | **Input/Output** |
| --------- | ---------------------------------------------- | --------- |
| s32GrpId  | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| pstAeAttr | Automatic-exposure structure information                                       | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

### **AK_MPI_ISP_SetAeAttr**

&emsp;&emsp;【Description】

&emsp;&emsp;Sets automatic-exposure structure information.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_SetAeAttr(AK_S32 s32GrpId, ISP_AE_ATTR_S *pstAeAttr);
```

&emsp;&emsp;【Parameters】

| **Parameter**  | **Description**                                         | **Input/Output** |
| --------- | ---------------------------------------------- | --------- |
| s32GrpId  | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| pstAeAttr | Automatic-exposure structure information                                       | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

### **AK_MPI_ISP_GetAeConvergenceRate**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the automatic-exposure convergence rate.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_GetAeConvergenceRate(AK_S32 s32GrpId, AK_U32 *pu32Value);
```

&emsp;&emsp;【Parameters】

| **Parameter**  | **Description**                                         | **Input/Output** |
| --------- | ---------------------------------------------- | --------- |
| s32GrpId  | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| pu32Value | Automatic-exposure convergence rate                                       | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

### **AK_MPI_ISP_SetAeConvergenceRate**

&emsp;&emsp;【Description】

&emsp;&emsp;Sets the automatic-exposure convergence rate.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_SetAeConvergenceRate(AK_S32 s32GrpId, AK_U32 u32Value);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**                                         | **Input/Output** |
| -------- | ---------------------------------------------- | --------- |
| s32GrpId | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| u32Value | Automatic-exposure convergence rate                                       | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

### **AK_MPI_ISP_CheckAeStable**

&emsp;&emsp;【Description】

&emsp;&emsp;Checks whether automatic exposure is stable.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_CheckAeStable(AK_S32 s32GrpId, AK_U32 *pu32Stable);
```

&emsp;&emsp;【Parameters】

| **Parameter**   | **Description**                                         | **Input/Output** |
| ---------- | ---------------------------------------------- | --------- |
| s32GrpId   | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| pu32Stable | Stability status: 0 unstable, 1 stable                                | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

### **AK_MPI_ISP_SetAeSuspend**

&emsp;&emsp;【Description】

&emsp;&emsp;Suspends or resumes AE.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_SetAeSuspend(AK_S32 s32GrpId,  AK_U32 u32AeSuspendFlag);
```

&emsp;&emsp;【Parameters】

| **Parameter**         | **Description**                                         | **Input/Output** |
| ---------------- | ---------------------------------------------- | --------- |
| s32GrpId         | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| u32AeSuspendFlag | AE suspend flag: 1 suspend, 0 resume                              | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

### **AK_MPI_ISP_GetMeAttr**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets manual-exposure structure information.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_GetMeAttr(AK_S32 s32GrpId, ISP_ME_ATTR_S *pstMeAttr);
```

&emsp;&emsp;【Parameters】

| **Parameter**  | **Description**                                         | **Input/Output** |
| --------- | ---------------------------------------------- | --------- |
| s32GrpId  | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| pstMeAttr | Manual-exposure structure information                                       | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

### **AK_MPI_ISP_SetMeAttr**

&emsp;&emsp;【Description】

&emsp;&emsp;Sets manual-exposure structure information.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_SetMeAttr(AK_S32 s32GrpId, ISP_ME_ATTR_S *pstMeAttr);
```

&emsp;&emsp;【Parameters】

| **Parameter**  | **Description**                                         | **Input/Output** |
| --------- | ---------------------------------------------- | --------- |
| s32GrpId  | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| pstMeAttr | Manual-exposure structure information                                       | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

## Set/Get Region Weight Coefficients

### **AK_MPI_ISP_GetExZweightAttr**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets extended weight-coefficient information.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_GetExZweightAttr(AK_S32 s32GrpId, ISP_EX_ZWEIGHT_ATTR_S *pstExZweight);
```

&emsp;&emsp;【Parameters】

| **Parameter**     | **Description**                                         | **Input/Output** |
| ------------ | ---------------------------------------------- | --------- |
| s32GrpId     | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| pstExZweight | Extended weight-coefficient information                                       | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

### **AK_MPI_ISP_SetExZweightAttr**

&emsp;&emsp;【Description】

&emsp;&emsp;Sets weight-coefficient information.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_SetExZweightAttr(AK_S32 s32GrpId, ISP_EX_ZWEIGHT_ATTR_S *pstExZweight);
```

&emsp;&emsp;【Parameters】

| **Parameter**     | **Description**                                         | **Input/Output** |
| ------------ | ---------------------------------------------- | --------- |
| s32GrpId     | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| pstExZweight | Extended weight-coefficient information                                       | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

## Set/Get White-Balance Parameters

### **AK_MPI_ISP_GetAwbStatInfo**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets white-balance statistics.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_GetAwbStatInfo(AK_S32 s32GrpId, ISP_AWB_STAT_INFO_S *pstAwbStatInfo);
```

&emsp;&emsp;【Parameters】

| **Parameter**       | **Description**                                         | **Input/Output** |
| -------------- | ---------------------------------------------- | --------- |
| s32GrpId       | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| pstAwbStatInfo | White-balance statistics                                        | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

### **AK_MPI_ISP_GetWbType**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets white-balance type information.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_GetWbType(AK_S32 s32GrpId, ISP_OP_TYPE_E *penWbType);
```

&emsp;&emsp;【Parameters】

| **Parameter**  | **Description**                                         | **Input/Output** |
| --------- | ---------------------------------------------- | --------- |
| s32GrpId  | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| penWbType | White-balance type information                                        | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

### **AK_MPI_ISP_SetWbType**

&emsp;&emsp;【Description】

&emsp;&emsp;Sets white-balance type information.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_SetWbType(AK_S32 s32GrpId, ISP_OP_TYPE_E enWbType);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**                                         | **Input/Output** |
| -------- | ---------------------------------------------- | --------- |
| s32GrpId | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| enWbType | White-balance type information                                        | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

### **AK_MPI_ISP_GetMwbAttr**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets manual white-balance structure information.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_GetMwbAttr(AK_S32 s32GrpId, ISP_MWB_ATTR_S *pstMwbAttr);
```

&emsp;&emsp;【Parameters】

| **Parameter**   | **Description**                                         | **Input/Output** |
| ---------- | ---------------------------------------------- | --------- |
| s32GrpId   | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| pstMwbAttr | Manual white-balance structure information                                      | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

### **AK_MPI_ISP_SetMwbAttr**

&emsp;&emsp;【Description】

&emsp;&emsp;Sets manual white-balance structure information.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_SetMwbAttr(AK_S32 s32GrpId, ISP_MWB_ATTR_S *pstMwbAttr);
```

&emsp;&emsp;【Parameters】

| **Parameter**   | **Description**                                         | **Input/Output** |
| ---------- | ---------------------------------------------- | --------- |
| s32GrpId   | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| pstMwbAttr | Manual white-balance structure information                                      | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

### **AK_MPI_ISP_GetAwbAttr**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets automatic white-balance structure information.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_GetAwbAttr(AK_S32 s32GrpId, ISP_AWB_ATTR_S *pstAwbAttr);
```

&emsp;&emsp;【Parameters】

| **Parameter**   | **Description**                                         | **Input/Output** |
| ---------- | ---------------------------------------------- | --------- |
| s32GrpId   | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| pstAwbAttr | Automatic white-balance structure information                                      | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

### **AK_MPI_ISP_SetAwbAttr**

&emsp;&emsp;【Description】

&emsp;&emsp;Sets automatic white-balance structure information.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_SetAwbAttr(AK_S32 s32GrpId, ISP_AWB_ATTR_S *pstAwbAttr);
```

&emsp;&emsp;【Parameters】

| **Parameter**   | **Description**                                         | **Input/Output** |
| ---------- | ---------------------------------------------- | --------- |
| s32GrpId   | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| pstAwbAttr | Automatic white-balance structure information                                      | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

## Set/Get WDR Parameters

### **AK_MPI_ISP_GetHdrAttr**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets WDR parameters.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_GetHdrAttr(AK_S32 s32GrpId, ISP_HDR_ATTR_S *pstHdr);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**                                         | **Input/Output** |
| -------- | ---------------------------------------------- | --------- |
| s32GrpId | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| pstHdr   | WDR parameters                                          | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description**    |
| -------------------------- | --------- |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL    | `p_wdr` is null |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

### **AK_MPI_ISP_SetHdrAttr**

&emsp;&emsp;【Description】

&emsp;&emsp;Sets WDR parameters.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_SetHdrAttr(AK_S32 s32GrpId, ISP_HDR_ATTR_S *pstHdr);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**                                         | **Input/Output** |
| -------- | ---------------------------------------------- | --------- |
| s32GrpId | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| pstHdr   | WDR parameters                                          | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description**    |
| -------------------------- | --------- |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL    | `p_wdr` argument is null |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

## Set/Get Day/Night Switching Parameters Without a Photosensor

### **AK_MPI_ISP_SetSoftPsParam**

&emsp;&emsp;【Description】

&emsp;&emsp;Sets day/night switching parameters without a photosensor.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_SetSoftPsParam(AK_S32 s32GrpId, ISP_SOFT_PS_ATTR_S *pstParam);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**                                         | **Input/Output** |
| -------- | ---------------------------------------------- | --------- |
| s32GrpId | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| pstParam | Day/night switching parameters without a photosensor                                      | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                     | **Description**        |
| --------------------------- | ------------- |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_FUNC_NOT_SUPPORT | Cannot be mixed with the old photosensor-free algorithm API |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

Parameter example:

```c
ISP_SOFT_PS_ATTR_S param = {0};

param.enNightType = IR_LED_NIGHT;
param.u32DayCheckFrameNum = 10;
param.u32NightCheckFrameNum = 10;
param.u32ExpStableCheckFrameNum = 10;
param.s32ExpStableTimeOutMs = -1;
param.u32LockCntTh = 5;
param.u32LockTimeMs = 60000;

param.stIrLedNightParm.u32DayToNightLum = 87961300;
param.stIrLedNightParm.u32NightToDayLum = 12000000;
param.stIrLedNightParm.u32AwbNightDisMax = 400;
param.stIrLedNightParm.u32AwbNightDisMin = 200;

param.stIrLedNightParm.u32GainR = 1024;
param.stIrLedNightParm.u32GainB = 1024;
param.stIrLedNightParm.u32GainRB = 1024;
param.stIrLedNightParm.s32OffsetR = 0;
param.stIrLedNightParm.s32OffsetB = 0;
param.stIrLedNightParm.s32OffsetRB = 0;
param.stIrLedNightParm.u32BlkCheckFlag = 1;
param.stIrLedNightParm.u32LowLumiTh = 12;
param.stIrLedNightParm.u32HighLumiTh = 252;
param.stIrLedNightParm.u32NonInfraredRatioTh = 35;
param.stIrLedNightParm.u32RevisedDisMaxRatio = 400;


AK_MPI_ISP_SetSoftPsParam(dev, &param);
```

<br/>

### **AK_MPI_ISP_GetSoftPsLevel**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the day/night level without a photosensor.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_GetSoftPsLevel(AK_S32 s32GrpId, AK_S32 s32PreIrLevel, AK_S32 *ps32NewIrLevel);
```

&emsp;&emsp;【Parameters】

| **Parameter**       | **Description**                                         | **Input/Output** |
| -------------- | ---------------------------------------------- | --------- |
| s32GrpId       | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| s32PreIrLevel  | Previous IRCUT level: 0 day, 1 night vision | Input |
| ps32NewIrLevel | New IRCUT level: 0 day, 1 night vision | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                 | **Description**                                    |
| ----------------------- | ----------------------------------------- |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_NOT_INIT     | Photosensor-free switching is not initialized (`ak_vpss_set_soft_ps_param` was not called) |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

```c
        /* Set the parameters first */
        AK_MPI_ISP_SetSoftPsParam(dev, &param);

        /* Create a thread that gets status periodically */
        while (1)
        {
            ret = AK_MPI_ISP_GetSoftPsLevel(dev, pre_status, &cur_status);

            if ((pre_status != cur_status) && (AK_SUCCESS == ret))
            {
                if (STATE_DAY == cur_status)
                {
                    /* Switch to day mode */
                    ...
                    pre_status = STATE_DAY;    /* store new state */
                }
                else
                {
                    /* Switch to night-vision mode */
                    ...
                    pre_status = STATE_NIGHT;    /* store new state */
                }
        }
        AK_BASE_SleepMs(100);
    }
```

<br/>

### **AK_MPI_ISP_SwitchMode**

&emsp;&emsp;【Description】

&emsp;&emsp;Switches day/night mode.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_SwitchMode(AK_S32 s32GrpId, ISP_DAY_NIGHT_MODE_E enMode);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**                                         | **Input/Output** |
| -------- | ---------------------------------------------- | --------- |
| s32GrpId | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| enMode   | Day/night status                                           | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                     | **Description**        |
| --------------------------- | ------------- |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_MALLOC_FAILED    | Memory allocation failed |
| ERROR_TYPE_FILE_READ_FAILED | Failed to read the ISP configuration file |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

## Set/Get Frame-Rate Parameters

### **AK_MPI_ISP_GetFpsCtrlStat**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the frame-rate control status.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_GetFpsCtrlStat(AK_S32 s32GrpId, ISP_GAIN_STAT_E *penStat, AK_S32 *ps32NeedFps);
```

&emsp;&emsp;【Parameters】

| **Parameter**    | **Description**                                         | **Input/Output** |
| ----------- | ---------------------------------------------- | --------- |
| s32GrpId    | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| penStat     | Gain status                                           | Output |
| ps32NeedFps | Required frame rate                                        | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                 | **Description**           |
| ----------------------- | ---------------- |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | `stat` or `need_fps` pointer is null |
| ERROR_TYPE_NOT_INIT     | Not initialized |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

> **Note:** To control frame-rate reduction under low light during the day, an application can create a thread that calls this API periodically. When a frame-rate change is required, call `AK_MPI_ISP_ChangeSensorFps`.

<br/>

### **AK_MPI_ISP_ChangeSensorFps**

&emsp;&emsp;【Description】

&emsp;&emsp;Switches the sensor frame rate.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_ChangeSensorFps(AK_S32 s32GrpId, AK_S32 s32NeedFps);
```

&emsp;&emsp;【Parameters】

| **Parameter**   | **Description**                                         | **Input/Output** |
| ---------- | ---------------------------------------------- | --------- |
| s32GrpId   | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| s32NeedFps | Required frame rate, obtained from `AK_MPI_ISP_GetFpsCtrlStat` | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                | **Description**           |
| ---------------------- | ---------------- |
| ERROR_TYPE_INVALID_ARG | Invalid `dev` or `need_fps` argument |
| ERROR_TYPE_NOT_INIT    | Not initialized |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

> **Note:** To control frame-rate reduction under low light during the day, an application can create a thread that periodically calls `ak_vpss_get_fps_ctrl_stat`. Call this API when a frame-rate change is required. Do not set the sensor frame rate arbitrarily; this API's `need_fps` value must come from `ak_vpss_get_fps_ctrl_stat`.

<br/>

### **AK_MPI_ISP_SetFpsLevel**

&emsp;&emsp;【Description】

&emsp;&emsp;Sets the sensor three-level frame-rate parameters.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_SetFpsLevel(AK_S32 s32GrpId, ISP_FPS_LEVEL_S *pstFpsLevel);
```

&emsp;&emsp;【Parameters】

| **Parameter**    | **Description**                                         | **Input/Output** |
| ----------- | ---------------------------------------------- | --------- |
| s32GrpId    | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| pstFpsLevel | Sensor three-level frame-rate parameters; see ISP_FPS_LEVEL_S                 | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description**   |
| -------------------------- | -------- |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL    | `fps` argument is null |
| ERROR_TYPE_DEV_CTRL_FAILED | Low-level driver operation failed |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

> **Note:** Call this API again after each day/night switch; otherwise the ISP parameter file overwrites the setting.

<br/>

### **AK_MPI_ISP_GetFpsLevel**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the sensor three-level frame-rate parameters.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_GetFpsLevel(AK_S32 s32GrpId, ISP_FPS_LEVEL_S *pstFpsLevel);
```

&emsp;&emsp;【Parameters】

| **Parameter**    | **Description**                                         | **Input/Output** |
| ----------- | ---------------------------------------------- | --------- |
| s32GrpId    | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| pstFpsLevel | Sensor three-level frame-rate parameters; see ISP_FPS_LEVEL_S                 | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                 | **Description**    |
| ----------------------- | --------- |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | `fps` argument is null |
| ERROR_TYPE_NOT_INIT     | Frame-rate parameters are not initialized |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

### **AK_MPI_ISP_SetSensorFps**

&emsp;&emsp;【Description】

&emsp;&emsp;Sets the sensor frame rate and adjusts the maximum exposure-time parameter.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_SetSensorFps(AK_S32 s32GrpId, AK_S32 s32Fps);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**                                         | **Input/Output** |
| -------- | ---------------------------------------------- | --------- |
| s32GrpId | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| s32Fps   | Sensor frame rate                                      | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description**   |
| -------------------------- | -------- |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL    | `fps` argument is null |
| ERROR_TYPE_DEV_CTRL_FAILED | Low-level driver operation failed |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

  Call only after the VPSS module is running normally.

### **AK_MPI_ISP_GetSensorFps**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the sensor frame rate.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_GetSensorFps(AK_S32 s32GrpId, AK_S32 *ps32Fps);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**                                         | **Input/Output** |
| -------- | ---------------------------------------------- | --------- |
| s32GrpId | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| ps32Fps  | Sensor frame rate                                      | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                 | **Description**    |
| ----------------------- | --------- |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | `fps` argument is null |
| ERROR_TYPE_NOT_INIT     | Frame-rate parameters are not initialized |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

  Call only after the VPSS module is running normally.

<br/>

## Set/Get 3D Noise-Reduction Parameters

### **AK_MPI_ISP_Get3dnrAttr**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the 3DNR structure.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_Get3dnrAttr(AK_S32 s32GrpId, ISP_3DNR_ATTR_S *pst3dnrAttr);
```

&emsp;&emsp;【Parameters】

| **Parameter**    | **Description**                                         | **Input/Output** |
| ----------- | ---------------------------------------------- | --------- |
| s32GrpId    | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| pst3dnrAttr | 3DNR structure information                                       | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

### **AK_MPI_ISP_Set3dnrAttr**

&emsp;&emsp;【Description】

&emsp;&emsp;Sets the 3DNR structure.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_Set3dnrAttr(AK_S32 s32GrpId, ISP_3DNR_ATTR_S *pst3dnrAttr);
```

&emsp;&emsp;【Parameters】

| **Parameter**    | **Description**                                         | **Input/Output** |
| ----------- | ---------------------------------------------- | --------- |
| s32GrpId    | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| pst3dnrAttr | 3DNR structure information                                       | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

## Set/Get Lens-Shading-Correction Parameters

### **AK_MPI_ISP_GetLscAttr**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets lens-shading-correction structure information.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_GetLscAttr(AK_S32 s32GrpId, ISP_LSC_ATTR_S *pstLsc);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**                                         | **Input/Output** |
| -------- | ---------------------------------------------- | --------- |
| s32GrpId | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| pstLsc   | Lens-shading-correction structure information                                       | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

### **AK_MPI_ISP_SetLscAttr**

&emsp;&emsp;【Description】

&emsp;&emsp;Sets lens-shading-correction structure information.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_SetLscAttr(AK_S32 s32GrpId, ISP_LSC_ATTR_S *pstLsc);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**                                         | **Input/Output** |
| -------- | ---------------------------------------------- | --------- |
| s32GrpId | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| pstLsc   | Lens-shading-correction structure information                                       | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

## Set/Get YUV-Effect Parameters

### **AK_MPI_ISP_GetYuvEffectAttr**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets YUV-effect structure information.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_GetYuvEffectAttr(AK_S32 s32GrpId, ISP_EFFECT_ATTR_S *pstYuvEffect);
```

&emsp;&emsp;【Parameters】

| **Parameter**     | **Description**                                         | **Input/Output** |
| ------------ | ---------------------------------------------- | --------- |
| s32GrpId     | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| pstYuvEffect | YUV-effect structure information                                      | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

### **AK_MPI_ISP_SetYuvEffectAttr**

&emsp;&emsp;【Description】

&emsp;&emsp;Sets YUV-effect structure information.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_SetYuvEffectAttr(AK_S32 s32GrpId, ISP_EFFECT_ATTR_S *pstYuvEffect);
```

&emsp;&emsp;【Parameters】

| **Parameter**     | **Description**                                         | **Input/Output** |
| ------------ | ---------------------------------------------- | --------- |
| s32GrpId     | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| pstYuvEffect | YUV-effect structure information                                      | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

## Set/Get Gamma-Related Parameters

### **AK_MPI_ISP_GetRgbGammaAttr**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets RGB-gamma structure information.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_GetRgbGammaAttr(AK_S32 s32GrpId, ISP_RGB_GAMMA_ATTR_S *pstRgbGamma);
```

<br/>&emsp;&emsp;【Parameters】

| **Parameter**    | **Description**                                         | **Input/Output** |
| ----------- | ---------------------------------------------- | --------- |
| s32GrpId    | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| pstRgbGamma | RGB-gamma structure information                                  | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

### **AK_MPI_ISP_SetRgbGammaAttr**

&emsp;&emsp;【Description】

&emsp;&emsp;Sets RGB-gamma structure information.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_SetRgbGammaAttr(AK_S32 s32GrpId, ISP_RGB_GAMMA_ATTR_S *pstRgbGamma);
```

<br/>&emsp;&emsp;【Parameters】

| **Parameter**    | **Description**                                         | **Input/Output** |
| ----------- | ---------------------------------------------- | --------- |
| s32GrpId    | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| pstRgbGamma | RGB-gamma structure information                                  | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

### **AK_MPI_ISP_GetYgammaAttr**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets Y-gamma structure information.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_GetYgammaAttr(AK_S32 s32GrpId, ISP_Y_GAMMA_ATTR_S *pstYgamma);
```

&emsp;&emsp;【Parameters】

| **Parameter**  | **Description**                                         | **Input/Output** |
| --------- | ---------------------------------------------- | --------- |
| s32GrpId  | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| pstYgamma | Y-gamma structure information                                    | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

### **AK_MPI_ISP_SetYgammaAttr**

&emsp;&emsp;【Description】

&emsp;&emsp;Sets Y-gamma structure information.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_SetYgammaAttr(AK_S32 s32GrpId, ISP_Y_GAMMA_ATTR_S *pstYgamma);
```

&emsp;&emsp;【Parameters】

| **Parameter**  | **Description**                                         | **Input/Output** |
| --------- | ---------------------------------------------- | --------- |
| s32GrpId  | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| pstYgamma | Y-gamma structure information                                    | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

## Set/Get Contrast-Related Parameters

### **AK_MPI_ISP_GetContrastAttr**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets contrast-structure information.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_GetContrastAttr(AK_S32 s32GrpId, ISP_CONTRAST_ATTR_S *pstContrast);
```

&emsp;&emsp;【Parameters】

| **Parameter**    | **Description**                                         | **Input/Output** |
| ----------- | ---------------------------------------------- | --------- |
| s32GrpId    | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| pstContrast | Contrast-structure information                                        | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

### **AK_MPI_ISP_SetContrastAttr**

&emsp;&emsp;【Description】

&emsp;&emsp;Sets contrast-structure information.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_SetContrastAttr(AK_S32 s32GrpId, ISP_CONTRAST_ATTR_S *pstContrast);
```

&emsp;&emsp;【Parameters】

| **Parameter**    | **Description**                                         | **Input/Output** |
| ----------- | ---------------------------------------------- | --------- |
| s32GrpId    | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| pstContrast | Contrast-structure information                                        | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

### **AK_MPI_ISP_GetLceAttr**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets local-contrast-enhancement structure information.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_GetLceAttr(AK_S32 s32GrpId, ISP_LCE_ATTR_S *pstLce);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**                                         | **Input/Output** |
| -------- | ---------------------------------------------- | --------- |
| s32GrpId | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| pstLce   | Local-contrast-enhancement structure information                                    | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

### **AK_MPI_ISP_SetLceAttr**

&emsp;&emsp;【Description】

&emsp;&emsp;Sets local-contrast-enhancement structure information.

&emsp;&emsp;【Syntax】

```c
   AK_S32 AK_MPI_ISP_SetLceAttr(AK_S32 s32GrpId, ISP_LCE_ATTR_S *pstLce);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**                                         | **Input/Output** |
| -------- | ---------------------------------------------- | --------- |
| s32GrpId | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| pstLce   | Local-contrast-enhancement structure information                                    | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

## Other APIs

### **AK_MPI_ISP_GetCurLumi**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets luminance.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_GetCurLumi(AK_S32 s32GrpId, AK_U32 *pu32Lumi);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**                                         | **Input/Output** |
| -------- | ---------------------------------------------- | --------- |
| s32GrpId | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| pu32Lumi | Luminance                                             | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

### **AK_MPI_ISP_SetForceAntiFlickerFlag**

&emsp;&emsp;【Description】

&emsp;&emsp;Sets the forced anti-flicker flag. In scenes affected by both daylight and artificial lighting, water-ripple artifacts may appear. Forced anti-flicker can correct these artifacts, but the image may be overexposed in a relatively bright environment. This API cannot be used together with `AK_MPI_ISP_SetAntiFlickerStrength`.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_SetForceAntiFlickerFlag(AK_S32 s32GrpId, AK_S32 s32ForceFlag);
```

&emsp;&emsp;【Parameters】

| **Parameter**     | **Description**                                         | **Input/Output** |
| ------------ | ---------------------------------------------- | --------- |
| s32GrpId     | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| s32ForceFlag | Forced anti-flicker flag: 0 disabled, 1 enabled | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

### **AK_MPI_ISP_GetForceAntiFlickerFlag**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the forced anti-flicker flag.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_GetForceAntiFlickerFlag(AK_S32 s32GrpId, AK_S32 *s32ForceFlag);
```

&emsp;&emsp;【Parameters】

| **Parameter**     | **Description**                                         | **Input/Output** |
| ------------ | ---------------------------------------------- | --------- |
| s32GrpId     | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| s32ForceFlag | Forced anti-flicker flag: 0 disabled, 1 enabled | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                 | **Description** |
| ----------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

**AK_MPI_ISP_SetAntiFlickerStrength**

&emsp;&emsp;【Description】

&emsp;&emsp;Sets the anti-flicker strength. In scenes affected by both daylight and artificial lighting, water-ripple artifacts may appear; setting the strength can correct them. This API cannot be used together with `AK_MPI_ISP_SetForceAntiFlickerFlag`.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_SetAntiFlickerStrength(AK_S32 s32GrpId, AK_U32 u32Strength);
```

&emsp;&emsp;【Parameters】

| **Parameter**    | **Description**                                         | **Input/Output** |
| ----------- | ---------------------------------------------- | --------- |
| s32GrpId    | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| u32Strength | Anti-flicker strength: 0 disabled, 1-100 enabled, with 100 the strongest | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

  Call only after the VPSS module is running normally.

### **AK_MPI_ISP_GetAntiFlickerStrength**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the anti-flicker strength.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_GetAntiFlickerStrength(AK_S32 s32GrpId, AK_U32 *pu32Strength);
```

&emsp;&emsp;【Parameters】

| **Parameter**     | **Description**                                         | **Input/Output** |
| ------------ | ---------------------------------------------- | --------- |
| s32GrpId     | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| pu32Strength | Anti-flicker strength: 0 disabled, 1-100 enabled, with 100 the strongest | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                 | **Description** |
| ----------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

  Call only after the VPSS module is running normally.

### **AK_MPI_ISP_GetRgbAverage**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the RGB average values.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_GetRgbAverage(AK_S32 s32GrpId,
        AK_U32 *u32RAvr, AK_U32 *u32GAvr, AK_U32 *u32BAvr);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**                                         | **Input/Output** |
| -------- | ---------------------------------------------- | --------- |
| s32GrpId | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| u32RAvr  | R average | Output |
| u32GAvr  | G average | Output |
| u32BAvr  | B average | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

### **AK_MPI_ISP_GetSensorReg**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets a sensor register value.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_GetSensorReg(AK_S32 s32GrpId, ISP_SENSOR_REG_INFO_S *pstSensorRegInfo);
```

&emsp;&emsp;【Parameters】

| **Parameter**         | **Description**                                         | **Input/Output**         |
| ---------------- | ---------------------------------------------- | ----------------- |
| s32GrpId         | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| pstSensorRegInfo | Sensor register information structure | The register address is input; the register value is output |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

### **AK_MPI_ISP_SwitchFlipMirror**

&emsp;&emsp;【Description】

&emsp;&emsp;Sets flip and mirror relative to the initial values in the ISP configuration file. Whenever possible, use `AK_MPI_ISP_SwitchFlipMirror` instead of `AK_MPI_ISP_SetEffect` to set flip and mirror.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_SwitchFlipMirror(AK_S32 s32GrpId, AK_U32 u32FlipEn, AK_U32 u32MirrorEn);
```

&emsp;&emsp;【Parameters】

| **Parameter**    | **Description**                                                    | **Input/Output** |
| ----------- | --------------------------------------------------------- | --------- |
| s32GrpId    | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID.            | Input |
| u32FlipEn   | Vertical-flip enable. Set to 0 for the same effect as the ISP configuration, or 1 for the opposite effect. | Input |
| u32MirrorEn | Horizontal-mirror enable. Set to 0 for the same effect as the ISP configuration, or 1 for the opposite effect. | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description**  |
| -------------------------- | ------- |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_NOT_INIT        | ISP is not initialized |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

### **AK_MPI_ISP_GetFlipMirror**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the flip and mirror status relative to the initial values in the ISP configuration file.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_GetFlipMirror(AK_S32 s32GrpId, AK_U32 *pu32FlipEn, AK_U32 *pu32MirrorEn);
```

&emsp;&emsp;【Parameters】

| **Parameter**     | **Description**                                                                                                                     | **Input/Output** |
| ------------ | -------------------------------------------------------------------------------------------------------------------------- | --------- |
| s32GrpId     | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID.                                                                             | Input |
| pu32FlipEn   | Vertical-flip enable. The value is 0 when the current effect matches the ISP configuration and 1 when it is the opposite. If `ak_vpss_switch_flip_mirror` has not been called to set flip or mirror since device initialization, this API returns 0. | Output |
| pu32MirrorEn | Horizontal-mirror enable. The value is 0 when the current effect matches the ISP configuration and 1 when it is the opposite. If `ak_vpss_switch_flip_mirror` has not been called to set flip or mirror since device initialization, this API returns 0. | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                 | **Description**  |
| ----------------------- | ------- |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL | Null argument |
| ERROR_TYPE_NOT_INIT     | ISP is not initialized |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

### **AK_MPI_ISP_WaitExpStable**

&emsp;&emsp;【Description】

&emsp;&emsp;Waits for exposure to stabilize.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_WaitExpStable(AK_S32 s32GrpId, AK_U32 u32ExpStableCheckFrameNum, AK_S32 s32TimeOutMs);
```

&emsp;&emsp;【Parameters】

| **Parameter**                  | **Description**                                         | **Input/Output** |
| ------------------------- | ---------------------------------------------- | --------- |
| s32GrpId                  | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| u32ExpStableCheckFrameNum | Number of frames used to check exposure stability | Input |
| s32TimeOutMs              | Wait timeout, in milliseconds | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL    | Invalid argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

### AK_MPI_ISP_GetEv

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the ambient EV value. Call this API after exposure stabilizes; otherwise the returned value may be unstable.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_GetEv(AK_S32 s32GrpId, AK_U32 *pu32Ev);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**                                         | **Input/Output** |
| -------- | ---------------------------------------------- | --------- |
| s32GrpId | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| pu32Ev   | Ambient EV value; a larger value indicates a darker environment | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL    | Invalid argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

### **AK_MPI_ISP_GetRgbDis**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the RGB difference value. Call this API after exposure stabilizes; otherwise the returned value may be unstable.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_GetRgbDis(AK_S32 s32GrpId, AK_U32 u32GainR, AK_S32 s32OffsetR,
        AK_U32 u32GainB, AK_S32 s32OffsetB, AK_U32 *pu32Dis);
```

&emsp;&emsp;【Parameters】

| **Parameter**   | **Description**                                                                                                                                  | **Input/Output** |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| s32GrpId   | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID.                                                                                          | Input |
| u32GainR   | R gain, default 1024. (`gain_r`, `offset_r`, `gain_b`, and `offset_b` are linearization parameters. They linearize the responses of sensors whose QE curves differ substantially under 850 nm infrared light so that the sensor output responses become equal, making day/night-vision detection easier.) | Input |
| s32OffsetR | R offset, default 0. | Input |
| u32GainB   | B gain, default 1024. | Input |
| s32OffsetB | B offset, default 0. | Input |
| pu32Dis    | RGB difference value; a larger value indicates more visible light in the environment | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL    | Invalid argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VPSS module is running normally.

<br/>

### AK_MPI_ISP_GetNonInfraredRatio

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the percentage of valid blocks that are non-infrared blocks.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_GetNonInfraredRatio(AK_S32 s32GrpId,
        ISP_NON_INFRARED_RATIO_ATTR_S *pstNirAttr, AK_U32 *pu32NonInfraredRatio);
```

&emsp;&emsp;【Parameters】

| **Parameter**             | **Description**                                         | **Input/Output** |
| -------------------- | ---------------------------------------------- | --------- |
| s32GrpId             | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| pstNirAttr           | Parameter structure required to calculate the non-infrared ratio | Input |
| pu32NonInfraredRatio | Percentage of non-infrared blocks | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL    | Invalid argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VI module is running normally.

<br/>

### AK_MPI_ISP_Get3dnrRefSizeStat

&emsp;&emsp;【Description】

&emsp;&emsp;Gets 3DNR buffer-usage statistics.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_ISP_Get3dnrRefSizeStat(AK_S32 s32GrpId, ISP_3D_NR_REF_SIZE_STAT_INFO *pstRefSize);
```

&emsp;&emsp;【Parameters】

| **Parameter**   | **Description**                                         | **Input/Output** |
| ---------- | ---------------------------------------------- | --------- |
| s32GrpId   | VPSS group ID, [0-4]. In a multi-camera system, each device corresponds to a different group ID. | Input |
| pstRefSize | 3DNR buffer-usage statistics structure | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description**     |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the value is an error code. |

&emsp;&emsp;【Error-code list】

| **Error code**                    | **Description** |
| -------------------------- | ------ |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_TYPE_POINTER_NULL    | Invalid argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Device-operation failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libplat_vpss.a, libplat_isp_sdk.a

&emsp;&emsp;Header: ak_vpss_isp.h

&emsp;&emsp;【Call flow】

&emsp;&emsp;Call only after the VI module is running normally.

<br/>

## VPSS Examples

### **Custom Effects: ak_vpss_effect_sample**

Before running this sample, use `insmod` to load `ak_vi.ko`, `sensor_xxx.ko`, `ak_vicap.ko`, `ak_isp.ko`, and `ak_pp.ko`. For the specific commands, see the description at the beginning of Chapter 7.

| **Input parameter** | **Description** |
| ------------ | ------------------------------------------------------------- |
| type         | Effect type: brightness/hue/sharp/contrast/saturation/wdr/flip_mirror |
| degree       | Effect value: flip_mirror [0, 3], all others [-50, 50]; default 0. |
| isp_cfg_path | Path to the ISP configuration file. Empty by default and must be specified. |
| path         | Path in which to save YUV image data |
| dev_cnt      | Number of devices [1, 2], default 1; use 2 for a dual-camera version |

<br/>

&emsp;&emsp;Output: YUV data before and after effect processing, saved in the specified `path` directory.

<br/>

### **Privacy Mask: ak_vpss_mask_sample**

Before running this sample, use `insmod` to load `ak_vi.ko`, `sensor_xxx.ko`, `ak_vicap.ko`, `ak_isp.ko`, and `ak_pp.ko`.

| **Input parameter** | **Description** |
| ------------ | ------------------------------------------------------------------------------------------- |
| rect0        | [x] [y] [width] [height/bitmap] [enable] [type] parameters for rect0; disabled by default. See the `PP_MASK_TYPE_E` enumeration for type. |
| rect1        | [x] [y] [width] [height/bitmap] [enable] [type] parameters for rect1; disabled by default. See the `PP_MASK_TYPE_E` enumeration for type. |
| rect2        | [x] [y] [width] [height/bitmap] [enable] [type] parameters for rect2; disabled by default. See the `PP_MASK_TYPE_E` enumeration for type. |
| rect3        | [x] [y] [width] [height/bitmap] [enable] [type] parameters for rect3; disabled by default. See the `PP_MASK_TYPE_E` enumeration for type. |
| alpha        | [0, 255], default 0 |
| color_r      | [0, 255], default 0 |
| color_g      | [0, 255], default 0 |
| color_b      | [0, 255], default 0 |
| isp_cfg_path | Path to the ISP configuration file. Empty by default and must be specified. |
| path         | Path in which to save YUV image data. |
| dev_cnt      | Number of devices [1, 2], default 1; use 2 for a dual-camera version |

<br/>

&emsp;&emsp;Output: YUV data before and after mask processing, saved in the specified `path` directory.

<br/>

### **Draw Box: ak_vpss_draw_box_sample**

Before running this sample, use `insmod` to load `ak_vi.ko`, `sensor_xxx.ko`, `ak_vicap.ko`, `ak_isp.ko`, and `ak_pp.ko`. For the specific commands, see the description at the beginning of Chapter 7.

| **Input parameter** | **Description** |
| ------------ | -------------------------------------------------------------------------------------------------------------------- |
| channel      | Channel number |
| rect0        | [x] [y] [width] [height/bitmap] [enable] [type] [color_id] [line_width] parameters for rect0; disabled by default. See the `PP_SHAPE_TYPE_E` enumeration for type. |
| rect1        | [x] [y] [width] [height/bitmap] [enable] [type] [color_id] [line_width] parameters for rect1; disabled by default. See the `PP_SHAPE_TYPE_E` enumeration for type. |
| rect2        | [x] [y] [width] [height/bitmap] [enable] [type] [color_id] [line_width] parameters for rect2; disabled by default. See the `PP_SHAPE_TYPE_E` enumeration for type. |
| rect3        | [x] [y] [width] [height/bitmap] [enable] [type] [color_id] [line_width] parameters for rect3; disabled by default. See the `PP_SHAPE_TYPE_E` enumeration for type. |
| isp_cfg_path | Path to the ISP configuration file. Empty by default and must be specified. |
| path         | Path in which to save YUV image data. |
| dev_cnt      | Number of devices [1, 2], default 1; use 2 for a dual-camera version |

<br/>

&emsp;&emsp;Output: YUV data before and after box drawing, saved in the specified `path` directory.

<br/>

### **Get MD Information: ak_vpss_md_sample**

Before running this sample, use `insmod` to load `ak_vi.ko`, `sensor_xxx.ko`, `ak_vicap.ko`, `ak_isp.ko`, and `ak_pp.ko`. For the specific commands, see the description at the beginning of Chapter 7.

| **Input parameter** | **Description** |
| ------------ | ------------------------------- |
| time         | Run time, default 20 seconds. |
| isp_cfg_path | Path to the ISP configuration file. Empty by default and must be specified. |
| path         | Path in which to save MD statistics data |
| dev_cnt      | Number of devices [1, 2], default 1; use 2 for a dual-camera version |

<br/>

&emsp;&emsp;Output: MD statistics data, saved in the specified `path` directory.

<br/>

### **Get OD Information: ak_vpss_od_sample**

Before running this sample, use `insmod` to load `ak_vi.ko`, `sensor_xxx.ko`, `ak_vicap.ko`, `ak_isp.ko`, and `ak_pp.ko`. For the specific commands, see the description at the beginning of Chapter 7.

| **Input parameter** | **Description** |
| ------------ | ------------------------------- |
| time         | Run time, default 20 seconds. |
| isp_cfg_path | Path to the ISP configuration file. Empty by default and must be specified. |
| path         | Path in which to save OD statistics data |
| dev_cnt      | Number of devices [1, 2], default 1; use 2 for a dual-camera version |

<br/>

&emsp;&emsp;Output: OD statistics data, saved in the specified `path` directory.

<br/>

### QR-Code Effect: ak_vpss_qr_sample

Before running this sample, use `insmod` to load `ak_vi.ko`, `sensor_xxx.ko`, `ak_vicap.ko`, `ak_isp.ko`, and `ak_pp.ko`. For the specific commands, see the description at the beginning of Chapter 7.

| **Input parameter** | **Description** |
| ------------ | ------------------------------- |
| isp_cfg_path | Path to the ISP configuration file. Empty by default and must be specified. |
| path         | Path in which to save YUV image data |
| dev_cnt      | Number of devices [1, 2], default 1; use 2 for a dual-camera version |

<br/>

&emsp;&emsp;Output: Three frames of YUV data, saved in the specified `path` directory. The first frame has the original image effect, the second is suitable for QR-code recognition, and the third restores the original image effect.

<br/>
