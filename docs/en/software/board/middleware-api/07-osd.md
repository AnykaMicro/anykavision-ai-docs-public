# Video Overlay Display

## Overview

&emsp;&emsp;The video overlay display module (OSD module).

<br/>

The basic OSD canvas, region, and channel concepts are:

- **Canvas:**

- An area established at a specified position in an image, in which the user can freely draw required characters. Memory allocation and usage must be considered.

- **Region:**

- All bitmaps within a canvas are managed with regions. A region is a virtual concept that partitions bitmap data within the canvas.

- **Channel:**

  - A VPSS channel. OSD supports the main and secondary channels.

The binding relationships are shown below:

![OSD binding relationships](../../../../zh_CN/software/board/middleware-api/img/osd-binding.jpg)

The labels embedded in the source image are Chinese. From left to right, they mean: (1) create a canvas, (2) create a region, (3) attach the region to the canvas, and (4) bind the canvas to the channel.

The main OSD workflow is shown below:

![OSD module workflow](../../../../zh_CN/software/board/middleware-api/img/osd-workflow.jpg)

English legend for the Chinese labels embedded in the source image: bitmap sources include a font file, line data, or a special bitmap such as an image. Load the data and extract its glyph bitmap; if conversion is required, convert it to a supported format. The resulting bitmap data then follows the OSD flow: initialize (set the color mode), create a canvas (`OSD_CANVAS_INFO_S`), create a region (`REGION_ATTR`), attach the region to the canvas, bind the canvas to an output channel, fill/update the canvas (`OSD_BITMAP_INFO_S`), and issue the command that displays the canvas in the image. The bottom portion of the diagram is the driver layer leading to the ISP.

## API Reference

&emsp;&emsp;This module provides the following APIs.

| Data structure         | Description        |
| ---------------------- | ------------------ |
| OSD_COLOR_MODE_E       | Image-mode enumeration |
| OSD_COLOR_TYPE_E       | Color-type enumeration |
| OSD_ATTR_S             | OSD attribute structure |
| OSD_VECTOR_S           | OSD position structure |
| OSD_CANVAS_INFO_S      | Canvas attribute structure |
| OSD_REGION_ATTR_S      | OSD region attributes |
| OSD_REGION_DATA_S      | OSD region data |
| OSD_REG_TYPE_E         | OSD region-type enumeration |
| OSD_BITMAP_ATTR_S      | Bitmap attribute structure |
| OSD_BITMAP_INFO_S      | Bitmap information structure |
| OSD_FONT_ATTR_S        | Font attribute structure |
| LINE_POSITION_ATTR_S   | Line-data structure |
| OSD_BIND_TYPE_E        | Binding-type enumeration |
| OSD_BIND_CANVAS_INFO_S | Canvas-binding information |
| OSD_BIND_REGION_INFO_S | Region-binding information |
| OSD_BIND_INFO_S        | Binding-query information structure |

<br/>

| **Function**              | **Description**                                 |
| ---------------------------- | --------------------------------------------------- |
| AK_MPI_OSD_Init          | Initializes OSD |
| AK_MPI_OSD_CreateCanvas  | Creates a canvas |
| AK_MPI_OSD_CreateRegion  | Creates a region |
| AK_MPI_OSD_AttachRegion  | Attaches a region to a canvas |
| AK_MPI_OSD_DetachRegion  | Detaches a region from a canvas |
| AK_MPI_OSD_BindVi        | Binds a canvas to a channel |
| AK_MPI_OSD_UnbindVi      | Unbinds a canvas from a channel |
| AK_MPI_OSD_UpdateRegion  | Updates region data |
| AK_MPI_OSD_ShowCanvas    | Displays canvas content |
| AK_MPI_OSD_SetRegionAttr | Sets region attributes |
| AK_MPI_OSD_GetRegionAttr | Gets region attributes |
| AK_MPI_OSD_DestroyRegion | Destroys a region |
| AK_MPI_OSD_CleanCanvas   | Clears canvas content |
| AK_MPI_OSD_DestroyCanvas | Destroys a canvas |
| AK_MPI_OSD_Destroy       | Exits OSD |
| AK_MPI_OSD_GetCanvasAttr | Gets canvas attributes |
| AK_MPI_OSD_SetCanvasAttr | Sets canvas attributes |
| AK_MPI_OSD_GetStrBmp     | Converts a string to a bitmap |
| AK_MPI_OSD_ReleaseBmpBuf | Releases a bitmap buffer |
| AK_MPI_OSD_GetBindInfo   | Gets canvas/region binding information |
<br/>

## Data Structures

### **OSD_COLOR_MODE_E**

  【Description】

  Image-mode enumeration.

  【Definition】

```c
typedef enum akOSD_COLOR_MODE_E
{
    AK_OSD_COLOR_FMT_YUV = 0,
    AK_OSD_COLOR_FMT_RGB,
    AK_OSD_COLOR_FMT_SUPPORT_NUM
}OSD_COLOR_MODE_E;
```

  【Members】

| **Member**                   | **Description** |
| ---------------------------- | ---------- |
| AK_OSD_COLOR_FMT_YUV         | YUV format |
| AK_OSD_COLOR_FMT_RGB         | RGB format |
| AK_OSD_COLOR_FMT_SUPPORT_NUM | Number supported |

  【Related function interface】

```c
   AK_S32 AK_MPI_OSD_Init(OSD_ATTR_S *pstOsdAttrValue);
```

### **OSD_COLOR_TYPE_E**

  【Description】

  Color-type enumeration.

  【Definition】

```c
typedef enum akOSD_COLOR_TYPE_E
{
    AK_OSD_TYPE_COLOR = 0,
    AK_OSD_TYPE_MONO,
    AK_OSD_TYPE_SUPPORT_NUM
}OSD_COLOR_TYPE_E;
```

  【Members】

| **Member**              | **Description**                                 |
| ----------------------- | ----------------------------------------------- |
| AK_OSD_TYPE_COLOR       | Color mode |
| AK_OSD_TYPE_MONO        | Monochrome mode (supported only by AK3918AV100 and AK3918EV300L chips) |
| AK_OSD_TYPE_SUPPORT_NUM | Number supported |

  【Related function interface】

```c
   AK_S32 AK_MPI_OSD_Init(OSD_ATTR_S *pstOsdAttrValue);
```

### **OSD_ATTR_S**

  【Description】

  OSD attribute structure.

  【Definition】

```c
typedef struct akOSD_ATTR_S
{
    OSD_COLOR_MODE_E enColorModeIndex;
    AK_U32 *pu32ColorTable;
    OSD_COLOR_TYPE_E enColorType;
}OSD_ATTR_S;
```

  【Members】

| **Member**       | **Description**                                               |
| ---------------- | ------------------------------------------------------------ |
| enColorModeIndex | Color format of `u32ColorTable`; supports YUV and RGB888 |
| pu32ColorTable   | `u32ColorTable` is a 16-entry color-table array, with one color per entry. For `u32ColorTable` colors, the highest 8 bits are unused on V330; on AV100 they hold the alpha value, where 0 is fully transparent and 255 is fully opaque. If `color_table` is null, the default color table is used. |
| enColorType      | Color type: color or monochrome; color by default. |

  【Related function interface】

```c
   AK_S32 AK_MPI_OSD_Init(OSD_ATTR_S *pstOsdAttrValue);
```

### OSD_VECTOR_S

  【Description】

  OSD position structure.

  【Definition】

```c
typedef struct akOSD_VECTOR_S
{
    AK_U32 u32X;
    AK_U32 u32Y;
}OSD_VECTOR_S;
```

  【Members】

| **Member**   | **Description**          |
| ------------ | ----------------------- |
| u32X         | Horizontal coordinate, aligned to 2 pixels |
| u32Y         | Vertical coordinate |

  【Related function interface】

```c
AK_S32 AK_MPI_OSD_CreateCanvas(AK_S32 s32CanvasId, OSD_CANVAS_INFO_S *pstOsdCanvasInfo);
```

### **OSD_CANVAS_INFO_S**

  【Description】

  Canvas attribute structure.

  【Definition】

```c
typedef struct akOSD_CANVAS_INFO_S
{
    OSD_VECTOR_S stPosInYuv;      //position in yuv
    AK_S32 s32CanvasSizeHeight;   //height of canvas
    AK_S32 s32CanvasSizeWidth;    //width of canvas
    AK_S32 s32CanvasColorIndex;   //background color of canvas
    AK_S32 s32Alpha;              //unsupport
    AK_S32 s32BitWidth;           //bitwidth
}OSD_CANVAS_INFO_S;
```

  【Members】

| **Member**          | **Description**                                               |
| ------------------- | ------------------------------------------------------------ |
| stPosInYuv          | See the vector structure |
| s32CanvasColorIndex | Canvas background color; the maximum color ID is determined by `bit_width`. |
| s32Alpha            | Canvas opacity; this parameter is not currently supported |
| s32CanvasSizeHeight | Canvas height, in pixels |
| s32CanvasSizeWidth  | Canvas width, in pixels |
| s32BitWidth         | Bit width; supports 1, 2, and 4, with a default of 4. In color mode, the first 2/4/16 colors in the color table are available according to `bit_width`. Monochrome mode does not use `color_table`. The meaning of color data is determined by `bit_width`. At 1 bit, 0x0 means black and 0x1 means white; this can implement black-and-white text with a background color. At 2 bits, bit [0] has the same definition as in 1-bit mode; bit [1] is 0 for fully transparent and 1 for opaque. This can implement outlined black-and-white text. At 4 bits, bit [0] has the same definition as in 1-bit mode; bits [3:1] are an 8-level alpha channel, where 0 is fully transparent and 7 is fully opaque. This can implement antialiased black-and-white text. |

  【Related function interface】

```c
AK_S32 AK_MPI_OSD_CreateCanvas(AK_S32 s32CanvasId, OSD_CANVAS_INFO_S *pstOsdCanvasInfo);
```

### **OSD_REGION_ATTR_S**

  【Description】

  OSD region attributes.

  【Definition】

```c
typedef struct akOSD_REGION_ATTR_S{
    AK_S32 s32Priority;                         //priority of cover region
    AK_S32 s32Width;                            //width of region
    AK_S32 s32Height;                           //hegiht of region
}OSD_REGION_ATTR_S;
```

  【Members】

| **Member**   | **Description**                                               |
| ------------ | ------------------------------------------------------------ |
| s32Priority  | Overlapping-region priority; applies only to overlapping regions. For example, priorities 1, 2, and 3 for region0, region1, and region2 mean that region0 is displayed first, then region1, then region2. For overlapping regions, only one region may be bound to a canvas. |
| s32Width     | Region width |
| s32Height    | Region height |

  【Related function interface】

```c
AK_S32 AK_MPI_OSD_CreateRegion(AK_S32 s32RegionId,OSD_REGION_ATTR_S *pstRegionAttr);
```

### **OSD_REGION_DATA_S**

  【Description】

  OSD region data.

  【Definition】

```c
typedef struct akOSD_REGION_DATA_S{
    OSD_REG_TYPE_E enType;                   //OSD region type
    AK_S32 s32ForceWriteFlag;                //force write font data when the bitmap size bigger than canvas size.
    union{
        OSD_BITMAP_INFO_S stOsdBitmapInfo;          //bitmap data
        OSD_FONT_ATTR_S stFontAttr;                 //string data
        LINE_POSITION_ATTR_S stLinePositionAttr;    //line data
    }data;
}OSD_REGION_DATA_S;
```

  【Members】

| **Member**         | **Description**                                               |
| ------------------ | ------------------------------------------------------------ |
| enType             | OSD region enumeration type |
| s32ForceWriteFlag  | Forced-write flag [1: force the write, 0: do not force it], valid only for character data. When character data extends beyond the canvas, forcing the last character to be written may produce garbled output. Without forcing, the last character is not written, preserving the complete characters that fit. |
| stOsdBitmapInfo    | Bitmap data |
| stFontAttr         | Font data |
| stLinePositionAttr | Line data |

  【Related function interface】

```c
AK_S32 AK_MPI_OSD_UpdateRegion(AK_S32 s32RegionId, AK_S32 s32Status, OSD_REGION_DATA_S *pstRegionData);
```

### **OSD_REG_TYPE_E**

  【Description】

  OSD region-type enumeration.

  【Definition】

```c
typedef enum akOSD_REG_TYPE_E {
    OSD_REG_INV = 0,     //undefine
    OSD_REG_LINE = 1,    //line
    OSD_REG_FONT = 2,    //font
    OSD_REG_BITMAP = 3,  //bitmap
}OSD_REG_TYPE_E;
```

  【Members】

| **Member**     | **Description** |
| -------------- | -------------- |
| OSD_REG_INV    | Undefined; reserved |
| OSD_REG_LINE   | Line type |
| OSD_REG_FONT   | Character type |
| OSD_REG_BITMAP | Bitmap-image type |

  【Related function interface】

```c
AK_S32 AK_MPI_OSD_UpdateRegion(AK_S32 s32RegionId, AK_S32 s32Status, OSD_REGION_DATA_S *pstRegionData);
```

### **OSD_BITMAP_ATTR_S**

  【Description】

  Bitmap attribute structure.

  【Definition】

```c
typedef struct akOSD_BITMAP_ATTR_S
{
    AK_S32 s32BitmapHeight;
    AK_S32 s32BitmapWidth;
    AK_S32 s32BitPerPixel;
}OSD_BITMAP_ATTR_S;
```

  【Members】

| **Member**      | **Description**   |
| --------------- | ---------------- |
| s32BitmapHeight | Bitmap height |
| s32BitmapWidth  | Bitmap width |
| s32BitPerPixel  | Bitmap pixel bit width |

  【Related function interface】

```c
AK_S32 AK_MPI_OSD_UpdateRegion(AK_S32 s32RegionId, AK_S32 s32Status, OSD_REGION_DATA_S *pstRegionData);
```

### **OSD_BITMAP_INFO_S**

  【Description】

  Bitmap information structure.

  【Definition】

```c
typedef struct akOSD_BITMAP_INFO_S
{
    AK_U8                   *pu8Buffer;
    AK_U32                  u32BufferLength;
    OSD_BITMAP_ATTR_S       stOsdBmpAttr;
}OSD_BITMAP_INFO_S;
```

  【Members】

| **Member** | **Description** |
| --------------- | ---------------- |
| pu8Buffer       | Bitmap buffer |
| u32BufferLength | Bitmap-buffer length |
| stOsdBmpAttr    | Bitmap attributes |

  【Related function interface】

```c
AK_S32 AK_MPI_OSD_UpdateRegion(AK_S32 s32RegionId, AK_S32 s32Status, OSD_REGION_DATA_S *pstRegionData);
```

### OSD_CHANGE_FONT_COLOR_S

  【Description】

  Font-color structure.

  【Definition】

```c
typedef struct akOSD_CHANGE_FONT_COLOR_S{
    AK_S32 s32FontColor;            //font color
    AK_S32 s32BgColor;              //font background color
    AK_S32 s32EdgeColor;            //font edge color
}OSD_CHANGE_FONT_COLOR_S;
```

  【Members】

| **Member**   | **Description** |
| ------------ | ---------- |
| s32FontColor | Font color |
| s32BgColor   | Font background color |
| s32EdgeColor | Edge color |

  【Related function interface】

```c
AK_S32 AK_MPI_OSD_UpdateRegion(AK_S32 s32RegionId, AK_S32 s32Status, OSD_REGION_DATA_S *pstRegionData);
```

### **OSD_FONT_ATTR_S**

  【Description】

  Font attribute structure.

  【Definition】

```c
typedef struct akOSD_FONT_ATTR_S{
    AK_S32 s32FontFileSize;         //font file size
    const AK_CHAR *pcfile;          //font file path
    AK_S32 s32FontSize;             //font size in screen
    AK_S32 s32FontInterval;         //font interval
    const AK_U16 *pu16Str;          //font string
    AK_S32 s32StrLen;               //string len
    OSD_CHANGE_FONT_COLOR_S *pstFontColor; //font color
}OSD_FONT_ATTR_S;
```

  【Members】

| **Member**      | **Description**                                               |
| --------------- | ------------------------------------------------------------ |
| s32FontColor    | Font color |
| s32BgColor      | Font background color |
| s32EdgeColor    | Edge color |
| s32FontFileSize | Font size in the font file |
| pcfile          | Font-file path |
| s32FontSize     | Font size |
| s32FontInterval | Character spacing |
| pu16Str         | String data |
| s32StrLen       | String length |
| pstFontColor    | Font-color structure used to specify the color of each character in a string. `pstFontColor` has `s32StrLen` entries. |

  【Related function interface】

```c
AK_S32 AK_MPI_OSD_UpdateRegion(AK_S32 s32RegionId, AK_S32 s32Status, OSD_REGION_DATA_S *pstRegionData);
```

### **LINE_POSITION_ATTR_S**

  【Description】

  Line-data structure. This feature is not supported.

  【Definition】

```c
typedef struct akLINE_POSITION_ATTR_S{
    AK_S32          s32Num;
    OSD_VECTOR_S    *pstPoint;
    AK_S32          s32Color;
    AK_S32          s32Thickness;
}LINE_POSITION_ATTR_S;
```

  【Members】

| **Member**   | **Description**                         |
| ------------ | -------------------------------------- |
| s32Num       | Total number of coordinates |
| pstPoint     | Position coordinates. The points are connected in order to form line segments. |
| s32Color     | Line-segment color |
| s32Thickness | Line-segment thickness |

  【Related function interface】

```c
AK_S32 AK_MPI_OSD_UpdateRegion(AK_S32 s32RegionId, AK_S32 s32Status, OSD_REGION_DATA_S *pstRegionData);
```

### **OSD_BIND_TYPE_E**

  【Description】

  Binding-type enumeration.

  【Definition】

```c
typedef enum akOSD_BIND_TYPE_E
{
    OSD_BIND_TYPE_CAVNVAS = 0,
    OSD_BIND_TYPE_REGION,
}OSD_BIND_TYPE_E;
```

  【Members】

| **Member**            | **Description** |
| --------------------- | -------- |
| OSD_BIND_TYPE_CAVNVAS | Canvas |
| OSD_BIND_TYPE_REGION  | Region |

  【Related function interface】

```c
	AK_S32 AK_MPI_OSD_GetBindInfo(AK_S32 s32Id,OSD_BIND_INFO_S *pstOsdBindInfo);
```

### **OSD_BIND_CANVAS_INFO_S**

  【Description】

  Canvas-binding information.

  【Definition】

```c
typedef struct akOSD_BIND_CANVAS_INFO_S
{
    AK_S32  s32CanvasId;          //canvas id
    AK_S32  s32BindRegionNum;     //total region number
    AK_S32  s32BindChannelNum;    //total channel number
    AK_S32  s32BindRgionId[64];   //region id
    OSD_BIND_CHN_INFO_S stBindChnInfo[64]; //bind info
}OSD_BIND_CANVAS_INFO_S;
```

  【Members】

| **Member**        | **Description**           |
| ----------------- | ------------------------ |
| s32CanvasId       | ID of the canvas to query |
| s32BindRegionNum  | Total number of regions on the canvas |
| s32BindChannelNum | Total number of channels bound to the canvas |
| s32BindRgionId    | IDs of regions already on the canvas |
| stBindChnInfo     | Channel IDs and device IDs bound to the canvas |

  【Related function interface】

```c
	AK_S32 AK_MPI_OSD_GetBindInfo(AK_S32 s32Id,OSD_BIND_INFO_S *pstOsdBindInfo);
```

### **OSD_BIND_REGION_INFO_S**

  【Description】

  Region-binding information.

  【Definition】

```c
typedef struct akOSD_BIND_REGION_INFO_S
{
    AK_S32  s32RegionId;          //region id that want to query
    AK_S32  s32BindCanvasNum;     //total canvas number that had been bind
    AK_S32  s32CoverRegionNum;    //total cover region number
    AK_S32  s32BindCanvasId[64];  //canvas id of region bind
    AK_S32  s32CoverRegionId[64]; //cover region id
    OSD_VECTOR_S stPos;           //region location
}OSD_BIND_REGION_INFO_S;
```

  【Members】

| **Member**        | **Description**             |
| ----------------- | -------------------------- |
| s32RegionId       | ID of the region to query |
| s32BindCanvasNum  | Total number of bound canvases |
| s32CoverRegionNum | Total number of overlapping regions |
| s32BindCanvasId   | Canvas to which this region is bound |
| s32CoverRegionId  | IDs of regions that overlap this region |
| stPos             | Coordinates of the region to query |

  【Related function interface】

```c
	AK_S32 AK_MPI_OSD_GetBindInfo(AK_S32 s32Id,OSD_BIND_INFO_S *pstOsdBindInfo);
```

### **OSD_BIND_INFO_S**

  【Description】

  Binding-query information structure.

  【Definition】

```c
typedef struct akOSD_BIND_INFO_S{
    OSD_BIND_TYPE_E     enType; //type: canvas/region
    union{
        OSD_BIND_CANVAS_INFO_S stCanvasBindInfo; //canvas bind info
        OSD_BIND_REGION_INFO_S stRegionBindInfo; //region bind info
    }info;
}OSD_BIND_INFO_S;
```

  【Members】

| **Member**       | **Description** |
| ---------------- | -------------- |
| enType           | Type of binding to query |
| stCanvasBindInfo | Canvas-binding information |
| stRegionBindInfo | Region-binding information |

  【Related function interface】

```c
	AK_S32 AK_MPI_OSD_GetBindInfo(AK_S32 s32Id,OSD_BIND_INFO_S *pstOsdBindInfo);
```

## Get Version Information

### **AK_MPI_OSD_GetVersion**

  【Description】

  Gets the version number of the OSD library.

  【Syntax】

```c
  const AK_CHAR* AK_MPI_OSD_GetVersion(AK_VOID);
```

  【Return values】

| **Return value** | **Description** |
| ------------- | -------- |
| OSD module version number | Success |
| NULL          | Failure |

  【Requirements】

  Library: libmpi_osd.a

  Header: ak_osd.h

<br/>

## API Description

### **AK_MPI_OSD_Init**

  【Description】

  Initializes OSD defaults and configures the color mode and color table.

  【Syntax】

```c
   AK_S32 AK_MPI_OSD_Init(OSD_ATTR_S *pstOsdAttrValue);
```

  【Parameters】

| **Parameter**   | **Description** | **Input/Output** |
| --------------- | ------------- | ------------- |
| pstOsdAttrValue | OSD attribute setting | Input |

  【Return values】

| **Return value** | **Description**     |
| ---------- | -------------------- |
| 0          | Success.              |
| Nonzero    | Failure; the value is an error code. |

  【Error-code list】

| **Error code**             | **Description**      |
| -------------------------- | ------------------- |
| ERROR_TYPE_POINTER_NULL    | `pstOsdAttrValue` is null |
| ERROR_TYPE_INVALID_ARG     | Invalid argument |
| ERROR_TYPE_DEV_CTRL_FAILED | Low-level runtime error |

  【Requirements】

  Library: libmpi_osd.a

  Header: ak_osd.h

### **AK_MPI_OSD_CreateCanvas**

  【Description】

  Creates a canvas.

  【Syntax】

```c
AK_S32 AK_MPI_OSD_CreateCanvas(AK_S32 s32CanvasId, OSD_CANVAS_INFO_S *pstOsdCanvasInfo);
```

  【Parameters】

| **Parameter**    | **Description** | **Value range** | **Input/Output** |
| ---------------- | -------------- | ------------ | ------------- |
| s32CanvasId      | Canvas ID | [0, 15] | Input |
| pstOsdCanvasInfo | Canvas attribute structure | - | Input |

  【Return values】

| **Return value** | **Description**       |
| ---------- | ---------------------- |
| 0          | Success                |
| Nonzero    | Failure; the return value is an error code. |

 【Error-code list】

| **Error code**                 | **Description**  |
| ------------------------------ | --------------- |
| ERROR_TYPE_INVALID_ARG         | Invalid argument |
| ERROR_OSD_NOT_INIT             | OSD module is not initialized |
| ERROR_OSD_CREATE_CANVAS_FAILED | Failed to create the canvas |
| ERROR_OSD_SET_COLOR_FAILED     | Failed to set the color |

【Requirements】

  Library: libmpi_osd.a

  Header: ak_osd.h

【Call flow】

```c
    AK_MPI_OSD_Init(&stOsdAttrValue);
    AK_MPI_OSD_CreateCanvas(s32CanvasId,&stOsdCanvasInfo);
```

### **AK_MPI_OSD_CreateRegion**

  【Description】

  Creates a region.

  【Syntax】

```c
AK_S32 AK_MPI_OSD_CreateRegion(AK_S32 s32RegionId,OSD_REGION_ATTR_S *pstRegionAttr);
```

  【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------- | -------------- | ------------ | ------------- |
| s32RegionId   | Region ID | > 0 | Input |
| pstRegionAttr | Region attribute structure | - | Input |

  【Return values】

| **Return value** | **Description** |
| ---------- | ---------------------- |
| 0 | Success |
| Nonzero | Failure; the return value is an error code. |

​		【Requirements】

  Library: libmpi_osd.a

  Header: ak_osd.h

​		【Call flow】

```c
    AK_MPI_OSD_Init(&stOsdAttrValue);
    AK_MPI_OSD_CreateCanvas(s32CanvasId,&stOsdCanvasInfo);
    AK_MPI_OSD_CreateRegion(s32RegionId,&stRegionAttr);
```

### **AK_MPI_OSD_AttachRegion**

  【Description】

  Attaches a canvas and a region.

  【Syntax】

```c
AK_S32 AK_MPI_OSD_AttachRegion(OSD_VECTOR_S stPos,AK_S32 s32RegionId,AK_S32 s32CanvasId);
```

  【Parameters】

| **Parameter** | **Description**           | **Value range** | **Input/Output** |
| ------------ | ------------------------- | ------------ | ------------- |
| stPos        | Region coordinates (x,y) within the canvas | > 0 | Input |
| s32RegionId  | Region ID | > 0 | Input |
| s32CanvasId  | Canvas ID | [0, 15] | Input |

  【Return values】

| **Return value** | **Description** |
| ---------- | ---------------------- |
| 0 | Success |
| Nonzero | Failure; the return value is an error code. |

​       【Requirements】

  Library: libmpi_osd.a

  Header: ak_osd.h

  【Call flow】

```c
    AK_MPI_OSD_Init(&stOsdAttrValue);
    AK_MPI_OSD_CreateCanvas(s32CanvasId,&stOsdCanvasInfo);
    AK_MPI_OSD_CreateRegion(s32RegionId,&stRegionAttr);
    AK_MPI_OSD_AttachRegion(s32RegionId,s32CanvasId);
```

### **AK_MPI_OSD_DetachRegion**

  【Description】

  Detaches a canvas and a region.

  【Syntax】

```c
 AK_S32 AK_MPI_OSD_DetachRegion(AK_S32 s32RegionId,AK_S32 s32CanvasId);
```

  【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------ | -------- | ------------ | ------------- |
| s32RegionId  | Region ID | > 0 | Input |
| s32CanvasId  | Canvas ID | [0, 15] | Input |

  【Return values】

| **Return value** | **Description** |
| ---------- | ---------------------- |
| 0 | Success |
| Nonzero | Failure; the return value is an error code. |

​      【Requirements】

  Library: libmpi_osd.a

  Header: ak_osd.h

  【Call flow】

```c
    AK_MPI_OSD_Init(&stOsdAttrValue);
    AK_MPI_OSD_CreateCanvas(s32CanvasId,&stOsdCanvasInfo);
    AK_MPI_OSD_CreateRegion(s32RegionId,&stRegionAttr);
    AK_MPI_OSD_AttachRegion(s32RegionId,s32CanvasId);
    AK_MPI_OSD_DetachRegion(s32RegionId,s32CanvasId);
```

### **AK_MPI_OSD_BindVi**

  【Description】

Binds a VI channel to a canvas.

  【Syntax】

```c
 AK_S32 AK_MPI_OSD_BindVi(AK_S32 s32CanvasId, AK_S32 s32ChannelId, AK_S32 s32DeviceId);
```

  【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------ | -------- | ------------ | ------------- |
| s32CanvasId  | Canvas ID | > 0 | Input |
| s32ChannelId | Channel ID | > 0 | Input |
| s32DeviceId  | Device ID | > 0 | Input |

  【Return values】

| **Return value** | **Description** |
| ---------- | ---------------------- |
| 0 | Success |
| <0         | Failure; the return value is an error code. |

【Requirements】

  Library: libmpi_osd.a

  Header: ak_osd.h

  【Call flow】

```c
    AK_MPI_OSD_Init(&stOsdAttrValue);
    AK_MPI_OSD_CreateCanvas(s32CanvasId,&stOsdCanvasInfo);
    AK_MPI_OSD_BindVi(s32CanvasId,s32ChannelId,s32DeviceId);
```

### **AK_MPI_OSD_UnbindVi**

  【Description】

Unbinds a VI channel from a canvas.

  【Syntax】

```c
 AK_S32 AK_MPI_OSD_UnbindVi(AK_S32 s32CanvasId, AK_S32 s32ChannelId, AK_S32 s32DeviceId);
```

  【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------ | -------- | ------------ | ------------- |
| s32CanvasId | Canvas ID | > 0 | Input |
| s32ChannelId | Channel ID | > 0 | Input |
| s32DeviceId  | Device ID | >0 | Input |

  【Return values】

| **Return value** | **Description** |
| ---------- | ---------------------- |
| 0 | Success |
| <0 | Failure; the return value is an error code. |

【Requirements】

  Library: libmpi_osd.a

  Header: ak_osd.h

  【Call flow】

```c
    AK_MPI_OSD_Init(&stOsdAttrValue);
    AK_MPI_OSD_CreateCanvas(s32CanvasId,&stOsdCanvasInfo);
    AK_MPI_OSD_BindVi(s32CanvasId,s32ChannelId,s32DeviceId);
	AK_MPI_OSD_UnbindVi(s32CanvasId,s32ChannelId,s32DeviceId);
```

### **AK_MPI_OSD_UpdateRegion**

  【Description】

  Updates OSD region data.

  【Syntax】

```
AK_S32 AK_MPI_OSD_UpdateRegion(AK_S32 s32RegionId, AK_S32 s32Status, OSD_REGION_DATA_S *pstRegionData);
```

  【Parameters】

| **Parameter** | **Description**     | **Value range** | **Input/Output** |
| ------------- | ------------------ | ------------ | ------------- |
| s32RegionId   | Region ID | > 0 | Input |
| s32Status     | 1: display, 0: do not display | [0, 1] | Input |
| pstRegionData | Region attribute data | - | Input |

  【Return values】

| **Return value** | **Description** |
| ---------- | ---------------------- |
| 0 | Success |
| Nonzero | Failure; the return value is an error code. |

【Requirements】

  Library: libmpi_osd.a

  Header: ak_osd.h

  【Call flow】

```c
    AK_MPI_OSD_Init(&stOsdAttrValue);
    AK_MPI_OSD_CreateCanvas(s32CanvasId,&stOsdCanvasInfo);
    AK_MPI_OSD_CreateRegion(s32RegionId,&stRegionAttr);
    AK_MPI_OSD_BindVi(s32CanvasId,s32ChannelId,s32DeviceId);
    AK_MPI_OSD_AttachRegion(s32RegionId,s32CanvasId);
    AK_MPI_OSD_UpdateRegion(s32RegionId,u32Status,&stRegionData);
```

### **AK_MPI_OSD_ShowCanvas**

  【Description】

  Displays canvas content.

  【Syntax】

```c
	AK_S32 AK_MPI_OSD_ShowCanvas(AK_S32 s32CanvasId);
```

  【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------ | -------- | ------------ | ------------- |
| s32CanvasId | Canvas ID | [0, 15] | Input |

  【Return values】

| **Return value** | **Description** |
| ---------- | ---------------------- |
| 0 | Success |
| Nonzero | Failure; the return value is an error code. |

【Requirements】

  Library: libmpi_osd.a

  Header: ak_osd.h

  【Call flow】

```c
    AK_MPI_OSD_Init(&stOsdAttrValue);
    AK_MPI_OSD_CreateCanvas(s32CanvasId,&stOsdCanvasInfo);
    AK_MPI_OSD_CreateRegion(s32RegionId,&stRegionAttr);
    AK_MPI_OSD_BindVi(s32CanvasId,s32ChannelId,s32DeviceId);
    AK_MPI_OSD_AttachRegion(s32RegionId,s32CanvasId);
    AK_MPI_OSD_UpdateRegion(s32RegionId,u32Status,&stRegionData);
    AK_MPI_OSD_ShowCanvas(s32CanvasId);
```

### **AK_MPI_OSD_SetRegionAttr**

  【Description】

  Sets OSD region attributes.

  【Syntax】

```c
AK_S32 AK_MPI_OSD_SetRegionAttr(AK_S32 s32RegionId, OSD_REGION_ATTR_S *pstRegionAttr);
```

  【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------- | -------------- | ------------ | ------------- |
| s32RegionId | Region ID | > 0 | Input |
| pstRegionAttr | Region attribute structure | - | Input |

  【Return values】

| **Return value** | **Description** |
| ---------- | ---------------------- |
| 0 | Success |
| Nonzero | Failure; the return value is an error code. |

【Requirements】

  Library: libmpi_osd.a

  Header: ak_osd.h

  【Call flow】

```c
	AK_MPI_OSD_Init(&stOsdAttrValue);
	AK_MPI_OSD_CreateRegion(s32RegionId,&stRegionAttr);
	AK_MPI_OSD_SetRegionAttr(s32RegionId,&stRegionAttr);
```

### **AK_MPI_OSD_GetRegionAttr**

  【Description】

  Gets OSD region attributes.

  【Syntax】

```c
AK_S32 AK_MPI_OSD_GetRegionAttr(AK_S32 s32RegionId, OSD_REGION_ATTR_S *pstRegionAttr);
```

  【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------- | -------------- | ------------ | ------------- |
| s32RegionId | Region ID | > 0 | Input |
| pstRegionAttr | Region attribute structure | - | Input |

  【Return values】

| **Return value** | **Description** |
| ---------- | ---------------------- |
| 0 | Success |
| Nonzero | Failure; the return value is an error code. |

【Requirements】

  Library: libmpi_osd.a

  Header: ak_osd.h

  【Call flow】

```c
	AK_MPI_OSD_Init(&stOsdAttrValue);
	AK_MPI_OSD_CreateRegion(s32RegionId,&stRegionAttr);
	AK_MPI_OSD_GetRegionAttr(s32RegionId,&stRegionAttr);
```

### **AK_MPI_OSD_DestroyRegion**

  【Description】

Destroys an OSD region.

  【Syntax】

```c
	AK_S32 AK_MPI_OSD_DestroyRegion(AK_S32 s32RegionId);
```

  【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------ | -------- | ------------ | ------------- |
| s32RegionId | Region ID | > 0 | Input |

  【Return values】

| **Return value** | **Description** |
| ---------- | ---------------------- |
| 0 | Success |
| Nonzero | Failure; the return value is an error code. |

【Requirements】

  Library: libmpi_osd.a

  Header: ak_osd.h

  【Call flow】

```c
	AK_MPI_OSD_Init(&stOsdAttrValue);
	AK_MPI_OSD_CreateRegion(s32RegionId,&stRegionAttr);
	AK_MPI_OSD_DestroyRegion(s32RegionId);
```

### **AK_MPI_OSD_CleanCanvas**

  【Description】

  Clears the specified canvas.

  【Syntax】

```c
	AK_S32 AK_MPI_OSD_CleanCanvas(AK_S32 s32CanvasId);
```

  【Parameters】

| **Parameter** | **Description** | **Input/Output** |
| ------------ | -------- | ------------- |
| s32CanvasId  | Canvas ID | Input |

  【Return values】

| **Return value** | **Description** |
| ---------- | -------------------- |
| 0 | Success. |
| Nonzero | Failure; the value is an error code. |

  【Error-code list】

| **Error code**         | **Description**  |
| ---------------------- | --------------- |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_OSD_NOT_INIT     | OSD module is not initialized |

  【Requirements】

  Library: libmpi_osd.a

  Header: ak_osd.h

  【Call flow】

```c
    AK_MPI_OSD_Init(&stOsdAttrValue);
    AK_MPI_OSD_CreateCanvas(s32CanvasId,&stOsdCanvasInfo);
    AK_MPI_OSD_BindVi(s32CanvasId,s32ChannelId,s32DeviceId);
        AK_MPI_OSD_CleanCanvas(s32CanvasId);
        AK_MPI_OSD_ShowCanvas(s32CanvasId);
```

### **AK_MPI_OSD_DestroyCanvas**

  【Description】

  Destroys the specified canvas.

  【Syntax】

```c
	AK_S32 AK_MPI_OSD_DestroyCanvas(AK_S32 s32CanvasId);
```

  【Parameters】

| **Parameter** | **Description** | **Input/Output** |
| ------------ | -------- | ------------- |
| s32CanvasId | Canvas ID | Input |

  【Return values】

| **Return value** | **Description** |
| ---------- | -------------------- |
| 0 | Success. |
| Nonzero | Failure; the value is an error code. |

  【Error-code list】

| **Error code** | **Description** |
| ---------------------- | --------------- |
| ERROR_TYPE_INVALID_ARG | Invalid argument |
| ERROR_OSD_NOT_INIT | OSD module is not initialized |

  【Requirements】

  Library: libmpi_osd.a

  Header: ak_osd.h

  【Call flow】

```c
    AK_MPI_OSD_Init(&stOsdAttrValue);
    AK_MPI_OSD_CreateCanvas(s32CanvasId,&stOsdCanvasInfo);
    AK_MPI_OSD_DestroyCanvas(s32CanvasId);
```

### **AK_MPI_OSD_Destroy**

  【Description】

  Releases resources occupied by the module.

  【Syntax】

```c
	AK_S32 AK_MPI_OSD_Destroy(AK_VOID);
```

  【Parameters】

  None.

  【Return values】

| **Return value** | **Description** |
| ---------- | ---------------------- |
| 0 | Success |
| Nonzero | Failure; the return value is an error code. |

 【Error-code list】

| **Error code**     | **Description**  |
| ------------------ | --------------- |
| ERROR_OSD_NOT_INIT | OSD module is not initialized |

【Requirements】

  Library: libmpi_osd.a

  Header: ak_osd.h

  【Call flow】

```c
    AK_MPI_OSD_Init(&stOsdAttrValue);
    AK_MPI_OSD_CreateCanvas(s32CanvasId,&stOsdCanvasInfo);
    AK_MPI_OSD_CreateRegion(s32RegionId,&stRegionAttr);
    AK_MPI_OSD_BindVi(s32CanvasId,s32ChannelId,s32DeviceId);
    AK_MPI_OSD_AttachRegion(s32RegionId,s32CanvasId);
    AK_MPI_OSD_UpdateRegion(s32RegionId,u32Status,&stRegionData);
    AK_MPI_OSD_ShowCanvas(s32CanvasId);
	AK_MPI_OSD_Destroy();
```

### **AK_MPI_OSD_GetCanvasAttr**

  【Description】

  Gets canvas attributes.

  【Syntax】

```c
AK_S32 AK_MPI_OSD_GetCanvasAttr(AK_S32 s32CanvasId, OSD_CANVAS_INFO_S *pstCanvasInfo);
```

  【Parameters】 

| **Parameter** | **Description** | **Input/Output** |
| ------------- | -------------- | ------------- |
| s32CanvasId   | Canvas ID | Input |
| pstCanvasInfo | Canvas attribute structure | Output |

  【Return values】

| **Return value** | **Description** |
| ---------- | ---------------------- |
| 0 | Success |
| Nonzero | Failure; the return value is an error code. |

【Requirements】

  Library: libmpi_osd.a

  Header: ak_osd.h

  【Call flow】

```c
    AK_MPI_OSD_Init(&stOsdAttrValue);
    AK_MPI_OSD_CreateCanvas(s32CanvasId, &stOsdCanvasInfo);
	AK_MPI_OSD_GetCanvasAttr(s32CanvasId, &stOsdCanvasInfo);
```

### **AK_MPI_OSD_SetCanvasAttr**

  【Description】

  Sets canvas attributes.

  【Syntax】

```c
AK_S32 AK_MPI_OSD_SetCanvasAttr(AK_S32 s32CanvasId, OSD_CANVAS_INFO_S *pstCanvasInfo);
```

  【Parameters】

| **Parameter** | **Description** | **Input/Output** |
| ------------- | -------------- | ------------- |
| s32CanvasId | Canvas ID | Input |
| pstCanvasInfo | Canvas attribute structure | Input |

  【Return values】

| **Return value** | **Description** |
| ---------- | ---------------------- |
| 0 | Success |
| Nonzero | Failure; the return value is an error code. |

&emsp;&emsp;【Requirements】

  Library: libmpi_osd.a

  Header: ak_osd.h

  【Call flow】

```c
    AK_MPI_OSD_Init(&stOsdAttrValue);
    AK_MPI_OSD_CreateCanvas(s32CanvasId, &stOsdCanvasInfo);
	AK_MPI_OSD_SetCanvasAttr(s32CanvasId, &stOsdCanvasInfo);
```

### **AK_MPI_OSD_GetStrBmp**

  【Description】

  Converts a string to a bitmap.

  【Syntax】

```c
AK_S32 AK_MPI_OSD_GetStrBmp(OSD_FONT_ATTR_S *pstFontAttr, OSD_BITMAP_INFO_S *pstOutBitmapInfo);
```

  【Parameters】

| **Parameter**    | **Description**     | **Value range**               | **Input/Output** |
| ---------------- | ------------------ | ----------------------------- | ------------- |
| pstFontAttr      | Font data | - | Input |
| pstOutBitmapInfo | Pointer to a bitmap-information structure | Array of structure pointers with length `str_len` | Output |

  【Return values】

| **Return value** | **Description** |
| ---------- | ---------------------- |
| 0 | Success |
| Nonzero | Failure; the return value is an error code. |

​		【Error-code list】

| **Error code**           | **Description**     |
| ------------------------ | ------------------ |
| ERROR_TYPE_INVALID_ARG   | Invalid argument |
| ERROR_TYPE_MALLOC_FAILED | Failed to allocate the bitmap buffer |

【Requirements】

  Library: libmpi_osd.a

  Header: ak_osd.h

  【Call flow】

```c
    AK_MPI_OSD_Init(&stOsdAttrValue);

    OSD_BITMAP_INFO_S pstBitmapInfo[20] = {0};
    AK_MPI_OSD_GetStrBmp(&stFontAttr, &stBitmapInfo);
    AK_MPI_OSD_ReleaseBmpBuf(pstBitmapInfo,20);

    AK_MPI_OSD_Destroy();
```

### **AK_MPI_OSD_ReleaseBmpBuf**

  【Description】

  Releases a bitmap buffer.

  【Syntax】

```c
AK_S32 AK_MPI_OSD_ReleaseBmpBuf(OSD_BITMAP_INFO_S *pstOutBitmapInfo, AK_S32 s32Len);
```

  【Parameters】

| **Parameter**    | **Description**     | **Value range** | **Input/Output** |
| ---------------- | ------------------ | ------------ | ------------- |
| pstOutBitmapInfo | Pointer to a bitmap-information structure | - | Input |
| s32Len           | Size of `bmp_info` | - | Input |

  【Return values】

| **Return value** | **Description** |
| ---------- | ---------------------- |
| 0 | Success |
| Nonzero | Failure; the return value is an error code. |

​      【Error-code list】

| **Error code**          | **Description** |
| ----------------------- | -------- |
| ERROR_TYPE_POINTER_NULL | Null argument |

【Requirements】

  Library: libmpi_osd.a

  Header: ak_osd.h

  【Call flow】

```c
    AK_MPI_OSD_Init(&stOsdAttrValue);

    OSD_BITMAP_INFO_S pstBitmapInfo[20] = {0};
    AK_MPI_OSD_GetStrBmp(&stFontAttr, &stBitmapInfo);
    AK_MPI_OSD_ReleaseBmpBuf(pstBitmapInfo,20);

    AK_MPI_OSD_Destroy();
```

### **AK_MPI_OSD_GetBindInfo**

  【Description】

  Gets binding information.

  【Syntax】

```c
	AK_S32 AK_MPI_OSD_GetBindInfo(AK_S32 s32Id,OSD_BIND_INFO_S *pstOsdBindInfo);
```

  【Parameters】

| **Parameter**  | **Description**        | **Input/Output** |
| -------------- | --------------------- | ------------- |
| s32Id          | Number of the canvas/region to query | Input |
| pstOsdBindInfo | Binding-information structure | Input |

  【Return values】

| **Return value** | **Description** |
| ---------- | ---------------------- |
| 0 | Success |
| Nonzero | Failure; the return value is an error code. |

【Requirements】

  Library: libmpi_osd.a

  Header: ak_osd.h

  【Call flow】

```c
    AK_MPI_OSD_Init(&stOsdAttrValue);
    AK_MPI_OSD_CreateCanvas(s32CanvasId,&stOsdCanvasInfo);
    AK_MPI_OSD_CreateRegion(s32RegionId,&stRegionAttr);
    AK_MPI_OSD_BindVi(s32CanvasId,s32ChannelId,s32DeviceId);
    AK_MPI_OSD_AttachRegion(s32RegionId,s32CanvasId);
	/* get canvas bind info */
	AK_MPI_OSD_GetBindInfo(s32CanvasId,&stOsdBindInfo);
    /* get region bind info */
	AK_MPI_OSD_GetBindInfo(s32RegionId,&stOsdBindInfo);
```

## OSD Examples

### **ak_osd_sample Usage Example**

Before running this sample, use `insmod` to load `ak_vi.ko`, `sensor_xxx.ko`, `ak_vicap.ko`, `ak_isp.ko`, and `ak_pp.ko`. This is normally done by running a script. For a GC5603 CIS, see `gc5603.sh`; the commands are:

​        insmod /usr/modules/ak_vi.ko

​        insmod /usr/modules/sensor_gc5603.ko

​        insmod /usr/modules/ak_vicap.ko

​        insmod /usr/modules/ak_isp.ko

​        insmod /usr/modules/ak_pp.ko

​        For another CIS, see its corresponding `xxx.sh` loading script.

| **Input parameter** | **Description**                                      |
| ------------ | ---------------------------------------------------------- |
| cfg          | ISP configuration-file path; empty by default and must be specified |
| path         | Path in which YUV image data is saved |
| logo         | Logo-file path; use `anyka.bmp` from the OSD sample directory in the PDK |
| dev_cnt      | Number of devices [1, 2]; default 1, or 2 for the binocular version |
| color_type   | Color type: 0 indexed color, 1 monochrome; default 0 |
| bit_width    | Bit width: 1, 2, or 4; default 4 |
| font_color | Font color, range:<br/>[0, 15] when `bit_width` is 4;<br/>[0, 3] when `bit_width` is 2;<br/>[0, 1] when `bit_width` is 1. |
| bg_color | Background color, range:<br/>[0, 15] when `bit_width` is 4;<br/>[0, 3] when `bit_width` is 2;<br/>[0, 1] when `bit_width` is 1. |

<br/>

&emsp;&emsp;Output: YUV data with the OSD logo overlaid, saved in the specified `path` directory.

<br/>

### **ak_osd_ex_sample Usage Example**

Before running this sample, use `insmod` to load `ak_vi.ko`, `sensor_xxx.ko`, `ak_vicap.ko`, `ak_isp.ko`, and `ak_pp.ko`. This is normally done by running a script. For a GC5603 CIS, see `gc5603.sh`; the commands are:

​        insmod /usr/modules/ak_vi.ko

​        insmod /usr/modules/sensor_gc5603.ko

​        insmod /usr/modules/ak_vicap.ko

​        insmod /usr/modules/ak_isp.ko

​        insmod /usr/modules/ak_pp.ko

​        For another CIS, see its corresponding `xxx.sh` loading script.

| **Input parameter** | **Description**                                        |
| ------------ | ------------------------------------------------------------ |
| cfg          | ISP configuration-file path; empty by default and must be specified |
| path         | Path in which YUV image data is saved |
| font         | Font-library file path; use `ak_font_16.bin` from the `osd_ex` sample directory in the PDK |
| dev_cnt      | Number of devices [1, 2]; default 1, or 2 for the binocular version |
| color_type | Color type: 0 indexed color, 1 monochrome; default 0 |
| bit_width | Bit width: 1, 2, or 4; default 4 |
| font_color | Font color, range:<br/>[0, 15] when `bit_width` is 4;<br/>[0, 3] when `bit_width` is 2;<br/>[0, 1] when `bit_width` is 1. |
| bg_color | Background color, range:<br/>[0, 15] when `bit_width` is 4;<br/>[0, 3] when `bit_width` is 2;<br/>[0, 1] when `bit_width` is 1. |
| edge_color | Font-outline color, range:<br/>[0, 15] when `bit_width` is 4;<br/>[0, 3] when `bit_width` is 2;<br/>[0, 1] when `bit_width` is 1. Must differ from the font color. |
| font_interval | Character spacing, not less than 0;<br/>divisible by 2 when `bit_width` is 4;<br/>divisible by 4 when `bit_width` is 2;<br/>divisible by 8 when `bit_width` is 1. |

<br/>

&emsp;&emsp;Output: YUV data with the OSD string overlaid, saved in the specified `path` directory.

<br/>

## Error Codes

| Error code | Macro                           | Meaning       |
| ---------- | ------------------------------- | ------------- |
| 0x11000000 | ERROR_OSD_NOT_INIT              | OSD is not initialized |
| 0x11000001 | ERROR_OSD_CREATE_CANVAS_FAILED  | Failed to create the canvas |
| 0x11000002 | ERROR_OSD_CREATE_REGIONS_FAILED | Failed to create the region |
| 0x11000003 | ERROR_OSD_SET_COLOR_FAILED      | Failed to set the color |
| 0x11000004 | ERROR_OSD_BIND_FAILED           | Binding failed |
| 0x11000005 | ERROR_OSD_UPDATE_FAILED         | Refresh failed |

<br/>
