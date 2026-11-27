# IPU Image Processing Unit

## Overview

&emsp;&emsp;The 2D Image Processing Unit (IPU) performs two-dimensional image processing, including format conversion, image compositing, scaling, rotation, blending, and distortion correction.

<br/>

## API Reference

&emsp;&emsp;This module provides the APIs listed below.

| **Data structure**         | **Description**           |
| ---------------- | ---------------- |
| IPU_COLOR_FMT_E | Color format |
| IPU_COLOR_TYPE_E | Color space |
| IPU_DITHER_E | Color-dithering type |
| IPU_ALPHA_CHN_E | Image alpha-channel selection |
| IPU_DIRECTION_E | Image preprocessing rotation and flip |
| IPU_ATTR_S | IPU device attributes |
| IPU_RECT_S | Operation-region rectangle |
| IPU_DMA_S | Structure describing IPU-allocated DMA memory |
| IPU_CMD_QUEUE_S | Management structure for one command queue |
| IPU_PLANE_S | Image mask information |
| IPU_SURFACE_S | Image-layer information |

<br/>

| **Function**                   | **Description**               |
| -------------------------- | -------------------- |
| AK_MPI_IPU_Open | Opens the IPU device. |
| AK_MPI_IPU_Close | Closes the IPU device. |
| AK_MPI_IPU_StartQue | Marks the start of a group of image-processing operations. |
| AK_MPI_IPU_EndQue | Completes and runs a group of commands. |
| AK_MPI_IPU_WaitForDone | Waits for an entire command queue to complete; optional. |
| AK_MPI_IPU_QuickFill | Fills a color block. |
| AK_MPI_IPU_QuickCopy | Copies a layer. |
| AK_MPI_IPU_CompositeResize | Scales a layer. |
| AK_MPI_IPU_Blend | Blends layers. |
| AK_MPI_IPU_Trans4 | Applies 4-point distortion correction. |

<br/>

## Data Structures

### IPU_COLOR_FMT_E

&emsp;&emsp;【Notes】

&emsp;&emsp;Color formats.

&emsp;&emsp;【Definition】

```c
typedef enum akIPU_COLOR_FMT_E
{
    IPU_COLOR_FMT_FULLPLANE_GREY  = 0X01, //Not support now
    IPU_COLOR_FMT_FULLPLANE_RGB   = 0X02,
    IPU_COLOR_FMT_FULLPLANE_YV24  = 0X03,
    IPU_COLOR_FMT_FULLPLANE_YV16  = 0X04,
    IPU_COLOR_FMT_FULLPLANE_YV12  = 0X05,

    IPU_COLOR_FMT_SEMIPLANE_NV24  = 0X10,
    IPU_COLOR_FMT_SEMIPLANE_NV42  = 0X11,
    IPU_COLOR_FMT_SEMIPLANE_NV16  = 0X12,
    IPU_COLOR_FMT_SEMIPLANE_NV61  = 0X13,
    IPU_COLOR_FMT_SEMIPLANE_NV12  = 0X14,
    IPU_COLOR_FMT_SEMIPLANE_NV21  = 0X15,

    IPU_COLOR_FMT_PACKED_ARGB32   = 0X20,
    IPU_COLOR_FMT_PACKED_ABGR32   = 0X21,
    IPU_COLOR_FMT_PACKED_BGRA32   = 0X22,
    IPU_COLOR_FMT_PACKED_RGBA32   = 0X23,
    IPU_COLOR_FMT_PACKED_RGB24    = 0X24,
    IPU_COLOR_FMT_PACKED_BGR24    = 0X25,
    IPU_COLOR_FMT_PACKED_RGB565   = 0X26,
    IPU_COLOR_FMT_PACKED_BGR565   = 0X27,
    IPU_COLOR_FMT_PACKED_RGB555   = 0X28,
    IPU_COLOR_FMT_PACKED_BGR555   = 0X29,

    IPU_COLOR_FMT_PACKED_AYUV     = 0X30,
    IPU_COLOR_FMT_PACKED_AVUY     = 0X31,
    IPU_COLOR_FMT_PACKED_VUYA     = 0X32,
    IPU_COLOR_FMT_PACKED_YUVA     = 0X33,
    IPU_COLOR_FMT_PACKED_YUV      = 0X34,
    IPU_COLOR_FMT_PACKED_VUY      = 0X35,
    IPU_COLOR_FMT_PACKED_IYU2     = 0X36,
    IPU_COLOR_FMT_PACKED_YUYV     = 0X37,
    IPU_COLOR_FMT_PACKED_YVYU     = 0X38,
    IPU_COLOR_FMT_PACKED_UYVY     = 0X39,
    IPU_COLOR_FMT_PACKED_VYUY     = 0X3A,
    IPU_COLOR_FMT_PACKED_IYU1     = 0X3B,

    IPU_COLOR_FMT_INDEX_1BIT      = 0X60, // input. Not support now
    IPU_COLOR_FMT_INDEX_2BITS     = 0X61, // input. Not support now
    IPU_COLOR_FMT_INDEX_4BITS     = 0X62, // input. Not support now
    IPU_COLOR_FMT_INDEX_8BITS     = 0X63, // input. Not support now

}IPU_COLOR_FMT_E;
```

<br/>

### IPU_COLOR_TYPE_E

&emsp;&emsp;【Notes】

&emsp;&emsp;Color-space standards.

&emsp;&emsp;【Definition】

```c
typedef enum akIPU_COLOR_TYPE_E
{
    IPU_COLOR_TYPE_UNKNOWN     = 0,
    IPU_COLOR_TYPE_RGB         = 1,
    IPU_COLOR_TYPE_YUV601_PC   = 2,
    IPU_COLOR_TYPE_YUV601_TV   = 3,
    IPU_COLOR_TYPE_YUV709_PC   = 4,
    IPU_COLOR_TYPE_YUV709_TV   = 5,
    IPU_COLOR_TYPE_YUV2020_PC  = 6,
    IPU_COLOR_TYPE_YUV2020_TV  = 7,

}IPU_COLOR_TYPE_E;
```

<br/>

### IPU_DITHER_E

&emsp;&emsp;【Notes】

&emsp;&emsp;Color-dithering types.
&emsp;&emsp;Controls whether dithering is used during color conversion.
&emsp;&emsp;For RGB565 input, this also controls whether dithering is used when converting to RGB888.

&emsp;&emsp;【Definition】

```c
    typedef enum akIPU_DITHER_E
    {
        IPU_DITHER_NONE   = 0,
        IPU_DITHER_BLUE16 = 1,

    }IPU_DITHER_E;
```

&emsp;&emsp;【Members】

| **Member**          | **Description**                 |
| ----------------- | ---------------------- |
| IPU_DITHER_NONE | No dithering |
| IPU_DITHER_BLUE16 | Ordered dithering (16x16 blue noise) |

<br/>

### IPU_ALPHA_CHN_E

&emsp;&emsp;【Notes】

&emsp;&emsp;Image alpha-channel selection.

&emsp;&emsp;【Definition】

```c
    typedef enum akIPU_ALPHA_CHN_E
    {
        IPU_ALPHA_CHN_NONE         = 0,
        IPU_ALPHA_CHN_PACKED       = 1,
        IPU_ALPHA_CHN_TRANS_IDX    = 2,
        IPU_ALPHA_CHN_PLANE_1BIT   = 4,
        IPU_ALPHA_CHN_PLANE_2BIT   = 5,
        IPU_ALPHA_CHN_PLANE_4BIT   = 6,
        IPU_ALPHA_CHN_PLANE_8BIT   = 7,
    }IPU_ALPHA_CHN_E;
```

&emsp;&emsp;【Members】

| **Member**                 | **Description**                                                                               |
| ------------------------ | ------------------------------------------------------------------------------------ |
| IPU_ALPHA_CHN_NONE | The image has no alpha channel or does not use it; alpha = 255 for every pixel. |
| IPU_ALPHA_CHN_PACKED | Uses the alpha channel in packed ARGB or the palette; for other formats, alpha = 255 for every pixel. |
| IPU_ALPHA_CHN_TRANS_IDX | Generates a mask from the index selected by Transparent Index. Pixels equal to the specified index have alpha=0; all other indexed pixels have alpha=255. Available only for indexed color. |
| IPU_ALPHA_CHN_PLANE_1BIT | Uses the 1-bit bitmap indicated by Plane 3 as the mask. |
| IPU_ALPHA_CHN_PLANE_2BIT | Uses the 2-bit bitmap indicated by Plane 3 as the mask. |
| IPU_ALPHA_CHN_PLANE_4BIT | Uses the 4-bit bitmap indicated by Plane 3 as the mask. |
| IPU_ALPHA_CHN_PLANE_8BIT | Uses the 8-bit bitmap indicated by Plane 3 as the mask. |

<br/>

### IPU_DIRECTION_E

&emsp;&emsp;【Notes】

&emsp;&emsp;Image preprocessing rotation and flip.

&emsp;&emsp;【Definition】

```c
    typedef enum akIPU_DIRECTION_E     // Image preprocessing rotation and flip
    {
        IPU_DIRECTION_UNCHANGE    = 0,
        IPU_DIRECTION_FLIP_VER    = 1,
        IPU_DIRECTION_FLIP_HOR    = 2,
        IPU_DIRECTION_ROTATE_180  = 3,
        IPU_DIRECTION_ROTATE_90   = 4,
        IPU_DIRECTION_ROTATE_270  = 5,

    }IPU_DIRECTION_E;
```

&emsp;&emsp;【Members】

| **Member**                 | **Description**    |
| ------------------------ | --------- |
| IPU_DIRECTION_UNCHANGE | Unchanged |
| IPU_DIRECTION_FLIP_VER | Flip vertically |
| IPU_DIRECTION_FLIP_HOR | Flip horizontally (mirror) |
| IPU_DIRECTION_ROTATE_180 | Rotate 180 degrees clockwise |
| IPU_DIRECTION_ROTATE_90 | Rotate 90 degrees clockwise |
| IPU_DIRECTION_ROTATE_270 | Rotate 270 degrees clockwise |

<br/>

### IPU_BLEND_OPT_TYPE_E

&emsp;&emsp;【Notes】

&emsp;&emsp;BLEND operation modes.

&emsp;&emsp;【Definition】

```c
    typedef enum akIPU_BLEND_OPT_TYPE_E
    {
        IPU_OPT_SOLID_COLOR_BLENDING     = 0x30,
        IPU_OPT_COLOR_KEY_BLENDING       = 0x31,
        IPU_OPT_SPECIFIED_ALPHA_BLENDING = 0x32,
        IPU_OPT_SOLID_BG_BLENDING        = 0x33,
        IPU_OPT_SOLID_FG_BLENDING        = 0x34,
        IPU_OPT_GRADIENT_BLENDING        = 0x35,
    }IPU_BLEND_OPT_TYPE_E;
```

&emsp;&emsp;【Members】

| **Member** | **Description**   |
| -------- | -------- |
| IPU_OPT_SOLID_COLOR_BLENDING | Foreground-to-solid-background blending. Places a foreground image (which may have an alpha channel) over a solid background image (without an alpha channel, or ignoring it) and outputs a solid image without an alpha channel. |
| IPU_OPT_COLOR_KEY_BLENDING | Color-key cutout. Specifies a color and tolerance for the foreground or background image (without an alpha channel, or ignoring it). Values within tolerance form the selected area; others form the inverse area. Separate alpha values are assigned to both areas for blending, producing an image without an alpha channel. |
| IPU_OPT_SPECIFIED_ALPHA_BLENDING | Proportional semitransparent-layer blending. Uses two global alpha values to blend layers A and B (which may have alpha channels), clamps the result, and outputs an image that may have an alpha channel. Input alpha values participate in global-alpha blending like color values. |
| IPU_OPT_SOLID_BG_BLENDING | Foreground with solid-color background. Blends an image that may have an alpha channel as the foreground with a solid background without alpha, producing output without an alpha channel. |
| IPU_OPT_SOLID_FG_BLENDING | Solid-color foreground with background image. Blends a solid foreground with an alpha value over an image without an alpha channel, producing output without an alpha channel. |
| IPU_OPT_GRADIENT_BLENDING | Foreground gradient over a solid background. Specifies opacity at 4 vertices and uses a linear gradient to place a solid foreground (without or ignoring alpha) over a solid background (without or ignoring alpha), producing a solid image without an alpha channel. |

<br/>

### IPU_BLEND_MODE_E

&emsp;&emsp;【Notes】

&emsp;&emsp;BLEND output effects.

&emsp;&emsp;【Definition】

```c
    typedef enum akIPU_BLEND_MODE_E
    {
        IPU_BLEND_MODE_NORMAL      = 0x00,
        IPU_BLEND_MODE_LIGHTEN     = 0x01,
        IPU_BLEND_MODE_DARKEN      = 0x02,
        IPU_BLEND_MODE_MULTIPLY    = 0x03,
        IPU_BLEND_MODE_AVERAGE     = 0x04,
        IPU_BLEND_MODE_DIFFERENCE  = 0x05,
        IPU_BLEND_MODE_NEGATION    = 0x06,
        IPU_BLEND_MODE_SCREEN      = 0x07,
        IPU_BLEND_MODE_EXCLUSION   = 0x08,
        IPU_BLEND_MODE_OVERLAY     = 0x09,
        IPU_BLEND_MODE_SOFTLIGHT   = 0x0A,
        IPU_BLEND_MODE_HARDLIGHT   = 0x0B,
        IPU_BLEND_MODE_LINEARDODGE = 0x0C,
        IPU_BLEND_MODE_LINEARBURN  = 0x0D,
        IPU_BLEND_MODE_LINEARLIGHT = 0x0E,
        IPU_BLEND_MODE_PINLIGHT    = 0x0F,
    }IPU_BLEND_MODE_E;
```

&emsp;&emsp;【Members】

| **Member** | **Description**   |
| -------- | -------- |
|IPU_BLEND_MODE_NORMAL | Normal |
|IPU_BLEND_MODE_LIGHTEN | Lighten |
|IPU_BLEND_MODE_DARKEN | Darken |
|IPU_BLEND_MODE_MULTIPLY | Multiply |
|IPU_BLEND_MODE_AVERAGE | Average |
|IPU_BLEND_MODE_DIFFERENCE | Difference |
|IPU_BLEND_MODE_NEGATION | Negation |
|IPU_BLEND_MODE_SCREEN | Screen |
|IPU_BLEND_MODE_EXCLUSION | Exclusion |
|IPU_BLEND_MODE_OVERLAY | Overlay |
|IPU_BLEND_MODE_SOFTLIGHT | Soft light |
|IPU_BLEND_MODE_HARDLIGHT | Hard light |
|IPU_BLEND_MODE_LINEARDODGE | Linear dodge |
|IPU_BLEND_MODE_LINEARBURN | Linear burn |
|IPU_BLEND_MODE_LINEARLIGHT | Linear light |
|IPU_BLEND_MODE_PINLIGHT | Pin light |

<br/>

### IPU_ATTR_S

&emsp;&emsp;【Notes】

&emsp;&emsp;IPU device-open attributes.

&emsp;&emsp;【Definition】

```c
    typedef struct akIPU_ATTR_S
    {
        AK_U32 au32QueSize[AK_IPU_MAX_QUE];
        AK_U32 u32RespSize;
        AK_U32 u32TransBlendQueSize;
    }IPU_ATTR_S;
```

&emsp;&emsp;【Members】

| **Member**                    | **Description**                      |
| --------------------------- | --------------------------- |
| au32QueSize[AK_IPU_MAX_QUE] | Memory size of the two queues |
| u32RespSize | Response-queue memory size |
| u32TransBlendQueSize | DMA memory required for distortion correction, estimated from conf size |

<br/>

### IPU_RECT_S

&emsp;&emsp;【Notes】

&emsp;&emsp;Operation-region rectangle.

&emsp;&emsp;【Definition】

```c
    typedef struct akIPU_RECT_S
    {
        AK_S32 s32X;
        AK_S32 s32Y;
        AK_U32 u32W;
        AK_U32 u32H;
    }IPU_RECT_S;
```

&emsp;&emsp;【Members】

| **Member** | **Description**   |
| -------- | -------- |
| s32X | Operation-region x-coordinate. |
| s32Y | Operation-region y-coordinate. |
| u32W | Operation-region width. |
| u32H | Operation-region height. |

<br/>

### IPU_DMA_S

&emsp;&emsp;【Notes】

&emsp;&emsp;Structure describing IPU-allocated DMA memory.

&emsp;&emsp;【Definition】

```c
    typedef struct akIPU_DMA_S
    {
        AK_U64 u64PhyAddr;
        AK_VOID *pvAddr;
        AK_U32 u32Len;
        AK_U32 u32PhyAddrLow;
        AK_U8 u8PhyAddrHigh;
        AK_U32 u32W;
        AK_U32 u32H;
        IPU_COLOR_FMT_E enColorFmt;
        AK_U32 u32PlantArrange;
        IPU_DIRECTION_E enDirection;
        AK_VOID *pvExt;
    }IPU_DMA_S;
```

&emsp;&emsp;【Members】

| **Member**        | **Description**              |
| --------------- | ------------------- |
| u64PhyAddr | Physical address |
| *pvAddr | Virtual address |
| u32Len | Memory length |
| u32PhyAddrLow | Low 32 bits of the physical address, used for distortion correction; optional |
| u8PhyAddrHigh | High 8 bits of the physical address, used for distortion correction; optional |
| u32W | Layer width; optional |
| u32H | Layer height; optional |
| enColorFmt | Layer image type; optional |
| u32PlantArrange | Layer color-component arrangement; optional |
| enDirection | Source-layer rotation direction; optional |
| *pvExt | Additional layer information; optional |

<br/>

### IPU_CMD_QUEUE_S

&emsp;&emsp;【Notes】

&emsp;&emsp;Management structure for one command queue.

&emsp;&emsp;【Definition】

```c
    typedef struct akIPU_CMD_QUEUE_S
    {
        AK_S32      s32InitFlag;
        AK_RWLOCK_T rwMutex;
        AK_VOID     *pvCmdStart;
        AK_VOID     *pvCmdOffset;
        AK_U32      u32LenCmd;
        IPU_DMA_S   stIpuAddrCmd;
        IPU_DMA_S   stIpuAddrResp;
        AK_U16      u16CmdId;
    }IPU_CMD_QUEUE_S;
```

&emsp;&emsp;【Members】

| **Member**      | **Description**                 |
| ------------- | ---------------------- |
| s32InitFlag | flag record init: initialization flag |
| rwMutex | rwlock: read-write lock |
| *pvCmdStart | Virtual address at which commands begin |
| *pvCmdOffset | Current command write-offset address |
| u32LenCmd | Command-buffer length |
| stIpuAddrCmd | Command-queue memory-description structure |
| stIpuAddrResp | Response-queue memory-description structure |
| u16CmdId | Command ID |

<br/>

### IPU_PLANE_S

&emsp;&emsp;【Notes】

&emsp;&emsp;Image mask information.

&emsp;&emsp;【Definition】

```c
    typedef struct akIPU_PLANE_S
    {
        AK_U64 u64PhyAddr;
        AK_U8  u8PixStride;
        AK_U32 u32PitchLine;
    }IPU_PLANE_S;
```

&emsp;&emsp;【Members】

| **Member**     | **Description**                                                                                                                             |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| u64PhyAddr | Image base address. Keep this field at 0 for an unused plane. |
| u8PixStride | Address offset between adjacent pixels on the same image row; the number corresponds to the Plane number. This unsigned value ranges from 1 to 4, representing 1 to 4 bytes. Keep it at 0 for an unused plane. |
| u32PitchLine | Address offset between the first pixels of adjacent image rows; the number corresponds to the Plane number. Enter this signed value in two's-complement form, in the range [-0x80000, 0x80000). If the Plane layout is vertically flipped, as in BMP, this value should be negative. Keep it at 0 for an unused plane. |

<br/>

### IPU_SURFACE_S

&emsp;&emsp;【Notes】

&emsp;&emsp;Image-layer information.

&emsp;&emsp;【Definition】

```c
    typedef struct akIPU_SURFACE_S
    {
        AK_U32           u32Width;
        AK_U32           u32Height;
        IPU_COLOR_FMT_E  enColorFmt;
        IPU_COLOR_TYPE_E enColorType;
        IPU_ALPHA_CHN_E  enAlphaChnChoice;
        IPU_DIRECTION_E  enDirection;
        AK_U8            u8ColorPadding;

        AK_U8            u8AlphaChnInv;
        AK_U8            u8AlphaDither;
        AK_U8            u8AlphaValue;
        AK_U16           u16PaletteOffset;
        AK_U16           u16PaletteTransp;
        IPU_PLANE_S      stPlant[4];

        AK_U32           u32Reserve1;
        AK_U32           u32Reserve2;
    }IPU_SURFACE_S;
```

&emsp;&emsp;【Members】

| **Member**         | **Description**                                                                          |
| ---------------- | ------------------------------------------------------------------------------- |
| u32Width | Layer width |
| 32Height | Layer height |
| enColorFmt | Pixel format. If the input and output pixel formats differ, image-format conversion is automatic. |
| enColorType | Color standard |
| enAlphaChnChoice | Alpha-channel selection |
| enDirection | Image preprocessing rotation and flip |
| u8ColorPadding | Handling of out-of-bounds image references: 0x0 copy edge; 0x1 black (Cache Color must be set accurately); 0x2 white (Cache Color must be set accurately). |
| u8AlphaChnInv | Inverts the Alpha or plane3 mask |
| u8AlphaDither | Whether to use dithering when input Plane 3 has fewer than 8 bits |
| u8AlphaValue | Alpha parameter |
| u16PaletteOffset | Offset of an indexed-color value in the shared palette |
| u16PaletteTransp | When alpha channel is 2, specifies an index; all pixels whose index equals it are treated as transparent |
| stPlant[4] | plane3 may contain mask data |
| u32Reserve1 | Reserved bit 1 |
| u32Reserve2 | Reserved bit 2 |

<br/>

### IPU_BLEND_OPT_S

&emsp;&emsp;【Notes】

&emsp;&emsp;Image-layer information.

&emsp;&emsp;【Definition】

```c
    typedef struct akIPU_BLEND_OPT_S
    {
        IPU_BLEND_OPT_TYPE_E enOpt;
        union
        {
            IPU_SOLID_COLOR_BLEND_ATTR_S stSolidColorBlendAttr;
            IPU_COLOR_SCOPE_BLEND_ATTR_S stColorScopeBlendAttr;
            IPU_SPECI_ALPHA_BLEND_ATTR_S stSpeciAlphaBlendAttr;
            IPU_SOLID_BG_BLEND_ATTR_S    stSolidBgBlendAttr;
            IPU_SOLID_FG_BLEND_ATTR_S    stSolidFgBlendAttr;
            IPU_GRADIENT_BLEND_ATTR_S    stGradientBlendAttr;
        };
    }IPU_BLEND_OPT_S;
```

&emsp;&emsp;【Members】

| **Member**         | **Description**                                                                          |
| ---------------- | ------------------------------------------------------------------------------- |
| enOpt | Blend operation mode |
| stSolidColorBlendAttr | Structure for foreground-to-solid-background blending |
| stColorScopeBlendAttr | Structure for color-key cutout |
| stSpeciAlphaBlendAttr | Structure for proportional semitransparent-layer blending |
| stSolidBgBlendAttr | Structure for foreground with solid-color background |
| stSolidFgBlendAttr | Structure for solid-color foreground with background image |
| stGradientBlendAttr | Structure for foreground gradient over a solid background |

<br/>

### IPU_SOLID_COLOR_BLEND_ATTR_S

&emsp;&emsp;【Notes】

&emsp;&emsp;Structure for foreground-to-solid-background blending.

&emsp;&emsp;【Definition】

```c
    typedef struct akIPU_SOLID_COLOR_BLEND_ATTR_S
    {
        IPU_BLEND_MODE_E enBlendMode;
        AK_U8 u8Opacity;
    }IPU_SOLID_COLOR_BLEND_ATTR_S;
```

&emsp;&emsp;【Members】

| **Member**         | **Description**                                                                          |
| ---------------- | ------------------------------------------------------------------------------- |
| enBlendMode | Blend-effect option |
| u8Opacity | Global foreground opacity; 255 is fully opaque |

<br/>

### IPU_COLOR_SCOPE_BLEND_ATTR_S

&emsp;&emsp;【Notes】

&emsp;&emsp;Structure for color-key cutout.

&emsp;&emsp;【Definition】

```c
    typedef struct akIPU_COLOR_SCOPE_BLEND_ATTR_S
    {
        AK_U8 u8OpacityPositive;
        AK_U8 u8OpacityNegative;
        IPU_LAYER_E enRefLayer;
        AK_U32 u32RefColor;
        AK_U8 u8Differ;
    }IPU_COLOR_SCOPE_BLEND_ATTR_S;
```

&emsp;&emsp;【Members】

| **Member**         | **Description**                                                                          |
| ---------------- | ------------------------------------------------------------------------------- |
|u8OpacityPositive| Opacity of the selected area. |
|u8OpacityNegative| Opacity of the inverse area. |
|enRefLayer| Layer used for color matching in the blend: 0x0 foreground; 0x1 background. |
|u32RefColor| Reference color for comparison. |
|u8Differ| A pixel whose difference from Ref. Color is no greater than Differ belongs to the selected area; otherwise it belongs to the inverse area. The difference uses Manhattan distance: the sum of the absolute differences of the three RGB or YUV components, up to 255. |
<br/>

### IPU_SPECI_ALPHA_BLEND_ATTR_S

&emsp;&emsp;【Notes】

&emsp;&emsp;Structure for proportional semitransparent-layer blending.

&emsp;&emsp;【Definition】

```c
    typedef struct akIPU_SPECI_ALPHA_BLEND_ATTR_S
    {
        AK_U8 u8gAlphaBg;
        AK_U8 u8gAlphaFg;
    }IPU_SPECI_ALPHA_BLEND_ATTR_S;
```

&emsp;&emsp;【Members】

| **Member**         | **Description**                                                                          |
| ---------------- | ------------------------------------------------------------------------------- |
| u8gAlphaFg | Weight of layer FG. |
| u8gAlphaBg | Weight of layer BG. |

<br/>

### IPU_SOLID_BG_BLEND_ATTR_S

&emsp;&emsp;【Notes】

&emsp;&emsp;Structure for foreground with solid-color background.

&emsp;&emsp;【Definition】

```c
    typedef struct akIPU_SOLID_BG_BLEND_ATTR_S
    {
        IPU_BLEND_MODE_E enBlendMode;
        AK_U32 u32ColorBG;
        AK_U8 u8Opacity;
    }IPU_SOLID_BG_BLEND_ATTR_S;
```

&emsp;&emsp;【Members】

| **Member**         | **Description**                                                                          |
| ---------------- | ------------------------------------------------------------------------------- |
| enBlendMode | Blend-effect option |
| u32ColorBG | Solid background color |
| u8Opacity | Global foreground opacity |

<br/>

### IPU_SOLID_FG_BLEND_ATTR_S

&emsp;&emsp;【Notes】

&emsp;&emsp;Structure for solid-color foreground with background image.

&emsp;&emsp;【Definition】

```c
    typedef struct akIPU_SOLID_FG_BLEND_ATTR_S
    {
        IPU_BLEND_MODE_E enBlendMode;
        AK_U32 u32ColorFG;
        AK_U8 u8Opacity;
    }IPU_SOLID_FG_BLEND_ATTR_S;
```

&emsp;&emsp;【Members】

| **Member**         | **Description**                                                                          |
| ---------------- | ------------------------------------------------------------------------------- |
| enBlendMode | Blend-effect option |
| u32ColorFG | Solid foreground color; specify an Alpha value in the color. |
| u8Opacity | Not currently used |
<br/>

### IPU_GRADIENT_BLEND_ATTR_S

&emsp;&emsp;【Notes】

&emsp;&emsp;Structure for foreground gradient over a solid background.

&emsp;&emsp;【Definition】

```c
    typedef struct akIPU_GRADIENT_BLEND_ATTR_S
    {
        IPU_BLEND_MODE_E enBlendMode;
        AK_U8 au8OpacityPoints[4];
    }IPU_GRADIENT_BLEND_ATTR_S;
```

&emsp;&emsp;【Members】

| **Member**         | **Description**                                                                          |
| ---------------- | ------------------------------------------------------------------------------- |
| enBlendMode | Blend-effect option |
| au8OpacityPoints | Global foreground opacity at 4 corners, in array order: upper-left, upper-right, lower-left, lower-right |

<br/>

## Getting Version Information

### AK_MPI_IPU_GetVersion

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the IPU library version number.

&emsp;&emsp;【Syntax】

```c
    const AK_CHAR* AK_MPI_IPU_GetVersion(void);
```

&emsp;&emsp;【Return Value】

| **Return value**  | **Description** |
| -------- | ------ |
| IPU module version number | Success     |
| NULL     | Failure     |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libmpi_ipu.a or libmpi_ipu.so

&emsp;&emsp;Header: ak_ipu.h

<br/>

## Opening and Closing the Module

### AK_MPI_IPU_Open

&emsp;&emsp;【Description】

&emsp;&emsp;Opens the IPU device.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_IPU_Open(const IPU_ATTR_S *pstIpuAttr);
```

&emsp;&emsp;【Parameters】

| **Parameter**   | **Description**     | **Value range** | **Input/Output** |
| ---------- | ---------- | -------- | --------- |
| pstIpuAttr | IPU configuration parameter structure | -        | Input        |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**   |
| ------- | -------- |
| 0       | Success       |
| Nonzero      | Failure; returns an error code. |

&emsp;&emsp;【Error Code List】

| **Error code**                | **Description**    |
| ---------------------- | --------- |
| ERROR_IPU_OPEN_FAILURE | Failed to open the IPU device |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libmpi_ipu.a or libmpi_ipu.so

&emsp;&emsp;Header: ak_ipu.h

> **Note:** This function is reentrant. If the IPU device is already open, it is not opened again; only the internal counter is incremented by 1. `AK_MPI_IPU_Open` and `AK_MPI_IPU_Close` must be called in pairs.

<br/>

### AK_MPI_IPU_Close

&emsp;&emsp;【Description】

&emsp;&emsp;Closes the IPU device.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_IPU_Close( AK_VOID );
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| -------- | ------ | -------- | --------- |
| AK_VOID  | -      | -        | -         |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**    |
| ------- | --------- |
| 0       | Success.       |
| Nonzero      | Failure; returns an error code. |

&emsp;&emsp;【Error Code List】

| **Error code**                       | **Description**   |
| ----------------------------- | -------- |
| ERROR_IPU_NOT_OPENED          | The IPU device is not open |
| ERROR_IPU_MUTEX_CLOSE_FAILURE | Failed to close the lock    |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libmpi_ipu.a or libmpi_ipu.so

&emsp;&emsp;Header: ak_ipu.h

> **Note:** This function is reentrant. `AK_MPI_IPU_Open` and `AK_MPI_IPU_Close` must be called in pairs.

<br/>

## Command Queue Management

### AK_MPI_IPU_StartQue

&emsp;&emsp;【Description】

&emsp;&emsp;Starts execution of a command queue group.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_IPU_StartQue( AK_S32 s32QueId );
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range**           | **Input/Output** |
| -------- | ------ | ------------------ | --------- |
| s32QueId | Queue ID   | 0-AK_IPU_MAX_QUE-1 | Input        |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**    |
| ------- | --------- |
| 0       | Success.       |
| Nonzero      | Failure; returns an error code. |

&emsp;&emsp;【Error Code List】

&emsp;&emsp;See the `akIPU_ERROR_E` function error-code list.

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libmpi_ipu.a or libmpi_ipu.so

&emsp;&emsp;Header: ak_ipu.h

<br/>

### AK_MPI_IPU_EndQue

&emsp;&emsp;【Description】

&emsp;&emsp;Completes assembly of a command group and runs it.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_IPU_EndQue( AK_S32 s32QueId, AK_BOOL bSync, AK_BOOL bBlock );
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**     | **Value range**           | **Input/Output** |
| -------- | ---------- | ------------------ | --------- |
| s32QueId | Queue ID       | 0-AK_IPU_MAX_QUE-1 | Input        |
| bSync    | Whether to execute asynchronously | 0-AK_IPU_MAX_QUE-1 | Input        |
| bBlock   | Whether to block until the command completes | 0-AK_IPU_MAX_QUE-1 | Input        |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**    |
| ------- | --------- |
| 0       | Success.       |
| Nonzero      | Failure; returns an error code. |

&emsp;&emsp;【Error Code List】

&emsp;&emsp;See the `akIPU_ERROR_E` function error-code list.

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libmpi_ipu.a or libmpi_ipu.so

&emsp;&emsp;Header: ak_ipu.h

<br/>

### AK_MPI_IPU_WaitForDone

&emsp;&emsp;【Description】

&emsp;&emsp;Waits for the entire command queue to finish executing. Calling this interface is optional. If several `endQue` command groups are set to non-blocking mode, this function can be called at the end to determine whether all commands in the queue have finished.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_IPU_WaitForDone(AK_S32 s32QueId, AK_U32 u32Timeout);
```

&emsp;&emsp;【Parameters】

| **Parameter**   | **Description**   | **Value range**           | **Input/Output** |
| ---------- | -------- | ------------------ | --------- |
| s32QueId   | Queue ID     | 0-AK_IPU_MAX_QUE-1 | Input        |
| u32Timeout | Timeout in ms | 10-5000            | Input        |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**    |
| ------- | --------- |
| 0       | Success.       |
| Nonzero      | Failure; returns an error code. |

&emsp;&emsp;【Error Code List】

&emsp;&emsp;See the `akIPU_ERROR_E` function error-code list.

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libmpi_ipu.a or libmpi_ipu.so

&emsp;&emsp;Header: ak_ipu.h

<br/>

## Image Processing Interfaces

### AK_MPI_IPU_QuickFill

&emsp;&emsp;【Description】

&emsp;&emsp;Performs a solid-color block fill.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_IPU_QuickFill(AK_S32 s32QueId,
                                IPU_SURFACE_S *pstDstImg,
                                IPU_RECT_S *pstDstRect,
                                AK_U32 u32FillColor);
```

&emsp;&emsp;【Parameters】

| **Parameter**     | **Description** | **Value range**           | **Input/Output** |
| ------------ | ------ | ------------------ | --------- |
| s32QueId     | Queue ID   | 0-AK_IPU_MAX_QUE-1 | Input        |
| pstDstImg    | Destination layer   | -                  | Input        |
| pstDstRect   | Destination coordinates   | -                  | Input        |
| u32FillColor | Color value    | 0x0 - 0xFFFFFFFF   | Input        |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**    |
| ------- | --------- |
| 0       | Success.       |
| Nonzero      | Failure; returns an error code. |

&emsp;&emsp;【Error Code List】

&emsp;&emsp;See the `akIPU_ERROR_E` function error-code list.

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libmpi_ipu.a or libmpi_ipu.so

&emsp;&emsp;Header: ak_ipu.h

<br/>

### AK_MPI_IPU_QuickCopy

&emsp;&emsp;【Description】

&emsp;&emsp;Copies a layer.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_IPU_QuickCopy( AK_S32 s32QueId,
                                 IPU_SURFACE_S *pstIpuSurfaceSrc,
                                 IPU_RECT_S *pstIpuRectSrc,
                                 IPU_SURFACE_S *pstIpuSurfaceDst,
                                 IPU_RECT_S *pstIpuRectDst );
```

&emsp;&emsp;【Parameters】

| **Parameter**         | **Description** | **Value range**           | **Input/Output** |
| ---------------- | ------ | ------------------ | --------- |
| s32QueId         | Queue ID   | 0-AK_IPU_MAX_QUE-1 | Input        |
| pstIpuSurfaceSrc | Source layer    | -                  | Input        |
| pstIpuRectSrc    | Source coordinates    | -                  | Input        |
| pstIpuSurfaceDst | Destination layer   | -                  | Input        |
| pstIpuRectDst    | Destination coordinates   | -                  | Input        |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**    |
| ------- | --------- |
| 0       | Success.       |
| Nonzero      | Failure; returns an error code. |

&emsp;&emsp;【Error Code List】

&emsp;&emsp;See the `akIPU_ERROR_E` function error-code list.

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libmpi_ipu.a or libmpi_ipu.so

&emsp;&emsp;Header: ak_ipu.h

<br/>

### AK_MPI_IPU_CompositeResize

&emsp;&emsp;【Description】

&emsp;&emsp;Resizes a layer.

&emsp;&emsp;【Syntax】

```c
AK_S32 AK_MPI_IPU_CompositeResize(AK_S32 s32QueId,
                                  IPU_SURFACE_S *pstSrcImg,
                                  IPU_RECT_S *pstSrcRect,
                                  IPU_SURFACE_S *pstDstImg,
                                  IPU_RECT_S *pstDstRect );
```

&emsp;&emsp;【Parameters】

| **Parameter**   | **Description** | **Value range**           | **Input/Output** |
| ---------- | ------ | ------------------ | --------- |
| s32QueId   | Queue ID   | 0-AK_IPU_MAX_QUE-1 | Input        |
| pstSrcImg  | Source layer    | -                  | Input        |
| pstSrcRect | Source coordinates    | -                  | Input        |
| pstDstImg  | Destination layer   | -                  | Input        |
| pstDstRect | Destination coordinates   | -                  | Input        |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**    |
| ------- | --------- |
| 0       | Success.       |
| Nonzero      | Failure; returns an error code. |

&emsp;&emsp;【Error Code List】

&emsp;&emsp;See the `akIPU_ERROR_E` function error-code list.

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libmpi_ipu.a or libmpi_ipu.so

&emsp;&emsp;Header: ak_ipu.h

<br/>

### AK_MPI_IPU_Blend

&emsp;&emsp;【Description】

&emsp;&emsp;Blends layers.

&emsp;&emsp;【Syntax】

```c
AK_S32 AK_MPI_IPU_Blend( AK_S32 s32QueId,
                         IPU_SURFACE_S *pstBackGround, IPU_RECT_S *pstBackGroundRect,
                         IPU_SURFACE_S *pstForeGround, IPU_RECT_S *pstForeGroundRect,
                         IPU_SURFACE_S *pstDst,        IPU_RECT_S *pstDstRect,
                         IPU_BLEND_OPT_S *pstBlendOpt );
```

&emsp;&emsp;【Parameters】

| **Parameter**          | **Description**  | **Value range**           | **Input/Output** |
| ----------------- | ------- | ------------------ | --------- |
| s32QueId          | Queue ID    | 0-AK_IPU_MAX_QUE-1 | Input        |
| pstBackGround     | Background layer    | -                  | Input        |
| pstBackGroundRect | Background-layer coordinates  | -                  | Input        |
| pstForeGround     | Foreground layer    | -                  | Input        |
| pstForeGroundRect | Foreground-layer coordinates  | -                  | Input        |
| pstDst            | Destination layer    | -                  | Input        |
| pstDstRect        | Destination-layer coordinates  | -                  | Input        |
| pstBlendOpt       | Blend-option structure | -                  | Input        |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**    |
| ------- | --------- |
| 0       | Success.       |
| Nonzero      | Failure; returns an error code. |

&emsp;&emsp;【Error Code List】

&emsp;&emsp;See the `akIPU_ERROR_E` function error-code list.

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libmpi_ipu.a or libmpi_ipu.so

&emsp;&emsp;Header: ak_ipu.h

<br/>

### AK_MPI_IPU_Trans4

&emsp;&emsp;【Description】

&emsp;&emsp;Performs four-point transformation for layer distortion correction.

&emsp;&emsp;【Syntax】

```c
AK_S32 AK_MPI_IPU_Trans4( AK_S32 s32QueId,
                          IPU_SURFACE_S *pstSrcImg,
                          IPU_SURFACE_S *pstDstImg,
                          IPU_DMA_S *pstIpuDmaBranch );
```

&emsp;&emsp;【Parameters】

| **Parameter**        | **Description** | **Value range**           | **Input/Output** |
| --------------- | ------ | ------------------ | --------- |
| s32QueId        | Queue ID   | 0-AK_IPU_MAX_QUE-1 | Input        |
| pstSrcImg       | Source layer    | -                  | Input        |
| pstDstImg       | Destination layer   | -                  | Input        |
| pstIpuDmaBranch | Distortion-correction command | -                  | Input        |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**    |
| ------- | --------- |
| 0       | Success.       |
| Nonzero      | Failure; returns an error code. |

&emsp;&emsp;【Error Code List】

&emsp;&emsp;See the `akIPU_ERROR_E` function error-code list.

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libmpi_ipu.a or libmpi_ipu.so

&emsp;&emsp;Header: ak_ipu.h

<br/>

### AK_MPI_IPU_SetColorTable

&emsp;&emsp;【Description】

&emsp;&emsp;Sets the global color table, which provides color support for 1-, 2-, 4-, and 8-bit bitmaps.

&emsp;&emsp;【Syntax】

```c

AK_S32 AK_MPI_IPU_SetColorTable( AK_U8 u8Num,
                                 AK_U8 u8Offset,
                                 AK_U32 *pu32Argb );

```

&emsp;&emsp;【Parameters】

| **Parameter**        | **Description** | **Value range**           | **Input/Output** |
| --------------- | ------ | ------------------ | --------- |
| u8Num        | Number of color-table entries   | 1-16 | Input        |
| u8Offset       | Offset within the color table    | 0-15                  | Input        |
| pu32Argb       | Start address of the input colors   | -                  | Input        |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**    |
| ------- | --------- |
| 0       | Success.       |
| Nonzero      | Failure; returns an error code. |

&emsp;&emsp;【Error Code List】

&emsp;&emsp;See the `akIPU_ERROR_E` function error-code list.

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libmpi_ipu.a or libmpi_ipu.so

&emsp;&emsp;Header: ak_ipu.h

<br/>

### AK_MPI_IPU_Reset

&emsp;&emsp;【Description】

&emsp;&emsp;Resets the IPU module.

&emsp;&emsp;【Syntax】

```c

AK_S32 AK_MPI_IPU_Reset( )

```

&emsp;&emsp;【Parameters】
None.
&emsp;&emsp;【Return Value】

| **Return value** | **Description**    |
| ------- | --------- |
| 0       | Success.       |
| Nonzero      | Failure; returns an error code. |

&emsp;&emsp;【Error Code List】

&emsp;&emsp;See the `akIPU_ERROR_E` function error-code list.

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libmpi_ipu.a or libmpi_ipu.so

&emsp;&emsp;Header: ak_ipu.h

<br/>

## ak_ipu_sample Usage Example

Before running this sample, first run `insmod /usr/modules/ak_ipu.ko`.

| **Input parameter**      | **Description**                                             |
| ------------- | ------------------------------------------------------ |
| -h, --help    | Prints help information                                                 |
| -a, --opt     | [OptCmd] [OptExtra]: IPU operation command and extra command data                     |
| -b, --file-s  | [Format] [w] [h] [Rotate] [Filename]: format, width, height, rotation mode, and source-image filename |
| -c, --file-d  | [Format] [w] [h] [Filename]: format, width, height, and destination-image filename              |
| -d, --rect-s  | x y w h\": source-image coordinate parameters                                       |
| -e, --rect-d  | x y w h\": destination-image coordinate parameters                                      |
| -f, --times   | [NUM]: number of repetitions                                           |
| -g, --no-save | Does not save the destination-image result                                               |

> **Source note:** The source contains the unmatched trailing `"` after `x y w h` for both rectangle options and does not state whether it is literal. Confirm the sample CLI syntax for the target SDK before using these options.

<br/>

## Error Codes

| Error code       | Macro                               | Meaning        |
| ---------- | --------------------------------- | --------- |
| 0x2c000000 | ERROR_IPU_OPEN_FAILURE            | Failed to open the IPU   |
| 0x2c000001 | ERROR_IPU_ALREADY_OPEN            | The IPU is already open   |
| 0x2c000002 | ERROR_IPU_NOT_OPENED              | The IPU is not open   |
| 0x2c000003 | ERROR_IPU_IPU_FLUSH_CACHE_FAILURE | Failed to flush the cache |
| 0x2c000004 | ERROR_IPU_CLOSE_FAILURE           | Failed to close the IPU   |
| 0x2c000005 | ERROR_IPU_MUTEX_INIT_FAILURE      | Failed to initialize the mutex  |
| 0x2c000006 | ERROR_IPU_MUTEX_CLOSE_FAILURE     | Failed to close the mutex   |
| 0x2c000007 | ERROR_IPU_IOCTL_FAILURE           | IOCTL failed   |
| 0x2c000008 | ERROR_IPU_QUEUE_NUM               | Invalid queue count    |
| 0x2c000009 | ERROR_IPU_VALUE_ILLEGAL           | Illegal value      |

<br/>
