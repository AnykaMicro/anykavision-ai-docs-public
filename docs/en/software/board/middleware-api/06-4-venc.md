# Video Encoding

## Overview

&emsp;&emsp;The video encoding module (VENC module) receives image data output by the VI module, encodes it according to the selected protocol, and outputs the corresponding bitstream.

&emsp;&emsp;The VENC module supports H.264, H.265, and MJPEG encoding. Supported formats vary by chip:

| **Chip family** | **H.264** | **H.265** | **MJPEG** |
| ----------- | --------- | --------- | --------- |
| KM02G-series chips | Supported | Supported | Supported |

&emsp;&emsp;The VENC module accepts multiple video-frame input formats. Supported input formats vary by chip:

| **Chip family** | **YUV420P** | **YUV422P** | **YUV400** | **YUV420SP** | **YUV422SP** |
| ----------- | ----------- | ----------- | ---------- | ------------ | ------------ |
| KM02G-series chips | Not supported | Not supported | Not supported | Supported | Not supported |

## API Reference

&emsp;&emsp;This module provides the following APIs.

| **Data structure**             | **Description**             |
| -------------------------- | ------------------------- |
| VENC_BITRATE_CTRL_MODE_E   | Bit-rate control mode |
| VENC_OUTPUT_TYPE_E         | Encoded-output type |
| VENC_PROFILE_MODE_E        | Profile mode |
| VENC_CHROMA_MODE_E         | Chroma encoding-input format |
| VENC_GDR_MODE_E            | GDR mode |
| VENC_ENCODE_LEVEL_E        | Encoding level |
| VENC_CU_BLOCK_SIZE_E       | CU block structure |
| VENC_SMART_MODE_E          | Smart-encoding mode |
| VENC_SPEC_PARAM_TYPE_E     | Special encoding-parameter setting |
| VENC_CHN_ATTRS_S           | Video-encoding parameter structure |
| VENC_ATTR_S                | Basic parameters used by an encoding channel |
| VENC_RC_ATTRS_S            | Encoding bit-rate control mode and parameters |
| VENC_EXT_ATTRS_S           | Extended parameter attributes |
| VENC_RC_AVC_HEVC_ADVANCE_S | Advanced parameter attributes |
| VENC_RC_AVC_HEVC_SMART_S   | Smart-encoding-mode parameters |
| VENC_H264_ATTR_S           | Basic H.264 encoding parameters |
| VENC_H265_ATTR_S           | Basic H.265 encoding parameters |
| VENC_RC_H264_CBR_S         | H.264 CBR rate-control parameters |
| VENC_RC_H264_VBR_S         | H.264 VBR rate-control parameters |
| VENC_RC_H264_CAPPED_VBR_S  | H.264 CAPPED_VBR rate-control parameters |
| VENC_RC_H264_CONST_QP_S    | H.264 CONST QP rate-control parameters |
| VENC_RC_MJPEG_S            | MJPEG rate-control parameters |
| VENC_RC_H265_CBR_S         | H.265 CBR rate-control parameters |
| VENC_RC_H265_VBR_S         | H.265 VBR rate-control parameters |
| VENC_RC_H265_CAPPED_VBR_S  | H.265 CAPPED_VBR rate-control parameters |
| VENC_RC_H265_AVBR_S        | H.265 AVBR rate-control parameters |
| VENC_RC_H265_CONST_QP_S    | H.265 CONST QP rate-control parameters |
| VENC_CROP_CFG_S            | Cropped-encoding configuration parameters |
| VENC_STAT_S                | Encoding-channel status information |
| VENC_SPEC_PARAM_S          | Special parameters |
| ROI_SVP_INFO_S             | Region-of-interest encoding attributes |
| AK_VENC_REQ_DMA_BLOCK      | DMA-block information |
| RATE_CTRL_PARAM_S          | External rate-control parameters |
| VENC_RC_STATUS_S           | External rate-control status parameters |
| RC_TYPE_E                  | Rate-control mode |
| USER_EXIF_TAG_TYPE         | Image-file-format tag type |
| USER_ExifRational          | User-specified numerator and denominator |
| EXIF_VALUE                 | Image-file-format value |
| EXIF_INFO                  | Image-file-format information structure |

<br/>

| **Function**                          | **Description**         |
| --------------------------------- | --------------------- |
| AK_MPI_VENC_GetVersion            | Gets the video-encoding library version |
| AK_MPI_VENC_GetEncLibVersion      | Gets the video-encoding algorithm-library version |
| AK_MPI_VENC_Open                  | Opens video encoding |
| AK_MPI_VENC_Close                 | Closes video encoding |
| AK_MPI_VENC_EncodeFrame           | Encodes a frame |
| AK_MPI_VENC_ReleaseStream         | Releases encoded output data |
| AK_MPI_VENC_SetAttr               | Sets VENC attribute parameters |
| AK_MPI_VENC_GetAttr               | Gets VENC attribute parameters |
| AK_MPI_VENC_RequestIdr            | Requests an I-frame |
| AK_MPI_VENC_SetQp                 | Sets the VENC QP range |
| AK_MPI_VENC_ResetQp               | Resets the VENC QP range to the values used at open time |
| AK_MPI_VENC_SetIframeParam        | Sets VENC I-frame parameters |
| AK_MPI_VENC_GetIframeParam        | Gets VENC I-frame parameters |
| AK_MPI_VENC_SetRoiMdinfo          | Sets ROI-related parameters |
| AK_MPI_VENC_SetRoiSvpInfo         | Sets ROI-region parameters |
| AK_MPI_VENC_StriclylimitFrameSize | Sets a hard frame-size limit |
| AK_MPI_VENC_GetStat               | Gets VENC statistics |
| AK_MPI_VENC_SetJpegSlice          | Configures JPEG slice encoding |
| AK_MPI_VENC_JpegSliceEncode       | Performs JPEG slice encoding |
| AK_MPI_VENC_SetFps                | Sets the encoding frame rate in slice mode |
| AK_MPI_VENC_GetCrop               | Gets cropped-encoding information for the current channel |
| AK_MPI_VENC_SetCrop               | Sets cropped-encoding information for a channel |
| AK_MPI_VENC_SetFunction           | Changes the dynamic-scene-switching logic |
| AK_MPI_VENC_GetFunction           | Gets the current dynamic-scene-switching logic |
| AK_MPI_VENC_SetRcType             | Sets the rate-control mode |
| AK_MPI_VENC_SetRcParam            | Sets external rate-control parameters |
| AK_MPI_VENC_GetRcStat             | Gets rate-control information |
| AK_MPI_VENC_SetStreamBufSize      | Sets the encoding library's internal stream-buffer size |
| AK_MPI_VENC_SetExifEnable         | Enables Exif |
| AK_MPI_VENC_SetExifInfo           | Sets Exif information |

## Data Structures

### VENC_BITRATE_CTRL_MODE_E

&emsp;&emsp;【Description】

&emsp;&emsp;Rate-control mode.

&emsp;&emsp;【Definition】

```c
    typedef enum akVENC_BITRATE_CTRL_MODE_E {
        VENC_RC_MODE_H264_CBR,
        VENC_RC_MODE_H264_VBR,
        VENC_RC_MODE_H264_CAPPED_VBR,
        VENC_RC_MODE_H264_AVBR,
        VENC_RC_MODE_H264_CONST_QP,
        VENC_RC_MODE_MJPEG,
        VENC_RC_MODE_H265_CBR,
        VENC_RC_MODE_H265_VBR,
        VENC_RC_MODE_H265_CAPPED_VBR,
        VENC_RC_MODE_H265_AVBR,
        VENC_RC_MODE_H265_CONST_QP,
        VENC_RC_MODE_TYPE_TOTAL
    }VENC_BITRATE_CTRL_MODE_E;
```

&emsp;&emsp;【Members】

| Member                           | Description      |
| ---------------------------- | -------------- |
| VENC_RC_MODE_H264_CBR        | Constant-bit-rate mode |
| VENC_RC_MODE_H264_VBR        | Variable-bit-rate mode |
| VENC_RC_MODE_H264_CAPPED_VBR | Capped variable-bit-rate mode |
| VENC_RC_MODE_H264_AVBR       | Advanced VBR mode |
| VENC_RC_MODE_H264_CONST_QP   | Fixed-QP mode |
| VENC_RC_MODE_MJPEG           | MJPEG encoded-size control mode |
| VENC_RC_MODE_H265_CBR        | Constant-bit-rate mode |
| VENC_RC_MODE_H265_VBR        | Variable-bit-rate mode |
| VENC_RC_MODE_H265_CAPPED_VBR | Capped variable-bit-rate mode |
| VENC_RC_MODE_H265_AVBR       | Advanced VBR mode |
| VENC_RC_MODE_H265_CONST_QP   | Fixed-QP mode |
| VENC_RC_MODE_TYPE_TOTAL      | Total number of rate-control modes |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_OUTPUT_TYPE_E

&emsp;&emsp;【Description】

&emsp;&emsp;Encoded-output format.

&emsp;&emsp;【Definition】

```c
    typedef enum akVENC_OUTPUT_TYPE_E {
        H264_ENC_TYPE,
        MJPEG_ENC_TYPE,
        HEVC_ENC_TYPE
    }VENC_OUTPUT_TYPE_E;
```

&emsp;&emsp;【Members】

| **Member**         | **Description** |
| -------------- | ------- |
| H264_ENC_TYPE  | H.264 format |
| MJPEG_ENC_TYPE | MJPEG format |
| HEVC_ENC_TYPE  | H.265 format |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_PROFILE_MODE_E

&emsp;&emsp;【Description】

&emsp;&emsp;Profile configuration selection.

&emsp;&emsp;【Definition】

```c
    typedef enum akVENC_PROFILE_MODE_E {
        VENC_PROFILE_MAIN,
        VENC_PROFILE_HIGH,
        VENC_PROFILE_BASE,
        VENC_PROFILE_C_BASE,
        VENC_PROFILE_HEVC_MAIN,
        VENC_PROFILE_HEVC_MAIN_STILL,
        VENC_PROFILE_HEVC_MAIN_INTRA,
        VENC_PROFILE_JPEG
    }VENC_PROFILE_MODE_E;
```

&emsp;&emsp;【Members】

| **Member**                       | **Description**              |
| ---------------------------- | -------------------------- |
| VENC_PROFILE_MAIN            | H.264 main profile |
| VENC_PROFILE_HIGH            | H.264 high profile |
| VENC_PROFILE_BASE            | H.264 base profile |
| VENC_PROFILE_C_BASE          | H.264 constrained-baseline profile |
| VENC_PROFILE_HEVC_MAIN       | H.265 main profile |
| VENC_PROFILE_HEVC_MAIN_STILL | H.265 main-still profile |
| VENC_PROFILE_HEVC_MAIN_INTRA | H.265 main-intra profile |
| VENC_PROFILE_JPEG            | JPEG profile |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_CHROMA_MODE_E

&emsp;&emsp;【Description】

&emsp;&emsp;Chroma encoding-input format selection.

&emsp;&emsp;【Definition】

```c
    typedef enum akVENC_CHROMA_MODE_E {
        VENC_CHROMA_MONO,
        VENC_CHROMA_YUV420
    }VENC_CHROMA_MODE_E;
```

&emsp;&emsp;【Members】

| **Member**             | **Description** |
| ------------------ | ------------- |
| VENC_CHROMA_MONO   | Grayscale image; JPEG only |
| VENC_CHROMA_YUV420 | Color image, YUV420SP |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_GDR_MODE_E

&emsp;&emsp;【Description】

&emsp;&emsp;GDR mode, which mitigates the bandwidth limitation caused by high-bit-rate I-frames.

&emsp;&emsp;【Definition】

```c
    typedef enum akVENC_GDR_MODE_E {
        VENC_GDR_OFF,
        VENC_GDR_VERTICAL,
        VENC_GDR_HORIZONTAL
    }VENC_GDR_MODE_E;
```

&emsp;&emsp;【Members】

| **Member**              | **Description** |
| ------------------- | ------- |
| VENC_GDR_OFF        | GDR off |
| VENC_GDR_VERTICAL   | Vertical GDR |
| VENC_GDR_HORIZONTAL | Horizontal GDR |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_ENCODE_LEVEL_E

&emsp;&emsp;【Description】

&emsp;&emsp;Encoding level.

&emsp;&emsp;【Definition】

```c
    typedef enum akVENC_ENCODE_LEVEL_E {
        VENC_HEVC_AVC_LEVEL_1   = 10,
        VENC_AVC_LEVEL_1_1      = 11, //only for avc
        VENC_AVC_LEVEL_1_2      = 12, //only for avc
        VENC_AVC_LEVEL_1_3      = 13, //only for avc
        VENC_HEVC_AVC_LEVEL_2     = 20,
        VENC_HEVC_AVC_LEVEL_2_1 = 21,
        VENC_AVC_LEVEL_2_2      = 22, //only for avc
        VENC_HEVC_AVC_LEVEL_3   = 30,
        VENC_HEVC_AVC_LEVEL_3_1 = 31,
        VENC_AVC_LEVEL_3_2      = 32, //only for avc
        VENC_HEVC_AVC_LEVEL_4   = 40,
        VENC_HEVC_AVC_LEVEL_4_1 = 41,
        VENC_AVC_LEVEL_4_2      = 42, //only for avc
        VENC_HEVC_AVC_LEVEL_5   = 50,
        VENC_HEVC_AVC_LEVEL_5_1 = 51,
        VENC_HEVC_AVC_LEVEL_5_2 = 52,
        VENC_HEVC_AVC_LEVEL_6   = 60,
        VENC_HEVC_AVC_LEVEL_6_1 = 61,
        VENC_HEVC_AVC_LEVEL_6_2 = 62
    }VENC_ENCODE_LEVEL_E;
```

  &emsp; 【Members】

| **Member**                  | **Description**         |
| ----------------------- | -------------------- |
| VENC_HEVC_AVC_LEVEL_1   | Level 10 for H.264/H.265 |
| VENC_AVC_LEVEL_1_1      | Level 11 for H.264 |
| VENC_AVC_LEVEL_1_2      | Level 12 for H.264 |
| VENC_AVC_LEVEL_1_3      | Level 13 for H.264 |
| VENC_HEVC_AVC_LEVEL_2   | Level 20 for H.264/H.265 |
| VENC_HEVC_AVC_LEVEL_2_1 | Level 21 for H.264/H.265 |
| VENC_AVC_LEVEL_2_2      | Level 22 for H.264 |
| VENC_HEVC_AVC_LEVEL_3   | Level 30 for H.264/H.265 |
| VENC_HEVC_AVC_LEVEL_3_1 | Level 31 for H.264/H.265 |
| VENC_AVC_LEVEL_3_2      | Level 32 for H.264 |
| VENC_HEVC_AVC_LEVEL_4   | Level 40 for H.264/H.265 |
| VENC_HEVC_AVC_LEVEL_4_1 | Level 41 for H.264/H.265 |
| VENC_AVC_LEVEL_4_2      | Level 42 for H.264 |
| VENC_HEVC_AVC_LEVEL_5   | Level 50 for H.264/H.265 |
| VENC_HEVC_AVC_LEVEL_5_1 | Level 51 for H.264/H.265 |
| VENC_HEVC_AVC_LEVEL_5_2 | Level 52 for H.264/H.265 |
| VENC_HEVC_AVC_LEVEL_6   | Level 60 for H.264/H.265 |
| VENC_HEVC_AVC_LEVEL_6_1 | Level 61 for H.264/H.265 |
| VENC_HEVC_AVC_LEVEL_6_2 | Level 62 for H.264/H.265 |

````{only} anyka_review
```{admonition} TODO
:class: warning

Image removed because it came from a third party; awaiting a replacement drawn by Anyka.

Figure removed: third-party source, pending redraw by Anyka.
```
````

The following are the general limits for each H.265 level, from Annex A of [ITU-T H.265](https://www.itu.int/rec/T-REC-H.265).

| Level | Maximum luma picture size (samples) | Maximum luma sample rate (samples/s) | Main-tier maximum bit rate (kbit/s) | High-tier maximum bit rate (kbit/s) | Minimum compression ratio |
| --- | --- | --- | --- | --- | --- |
| 1 | 36,864 | 552,960 | 128 | – | 2 |
| 2 | 122,880 | 3,686,400 | 1,500 | – | 2 |
| 2.1 | 245,760 | 7,372,800 | 3,000 | – | 2 |
| 3 | 552,960 | 16,588,800 | 6,000 | – | 2 |
| 3.1 | 983,040 | 33,177,600 | 10,000 | – | 2 |
| 4 | 2,228,224 | 66,846,720 | 12,000 | 30,000 | 4 |
| 4.1 | 2,228,224 | 133,693,440 | 20,000 | 50,000 | 4 |
| 5 | 8,912,896 | 267,386,880 | 25,000 | 100,000 | 6 |
| 5.1 | 8,912,896 | 534,773,760 | 40,000 | 160,000 | 8 |
| 5.2 | 8,912,896 | 1,069,547,520 | 60,000 | 240,000 | 8 |
| 6 | 35,651,584 | 1,069,547,520 | 60,000 | 240,000 | 8 |
| 6.1 | 35,651,584 | 2,139,095,040 | 120,000 | 480,000 | 8 |
| 6.2 | 35,651,584 | 4,278,190,080 | 240,000 | 800,000 | 6 |

​                                                                                Level reference table

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_CU_BLOCK_SIZE_E

&emsp;&emsp;【Description】

&emsp;&emsp;CU block size; supported only for H.265.

&emsp;&emsp;【Definition】

```c
typedef enum akVENC_CU_BLOCK_SIZE_E {
    VENC_CUSize32x32,          /*!< CU size 32x32, just for HEVC */
    VENC_CUSize16x16,          /*!< CU size 16x16, just for HEVC */
    VENC_CUSize8x8             /*!< CU size 8x8, just for HEVC */
}VENC_CU_BLOCK_SIZE_E;
```

&emsp;&emsp;【Members】

| **Member**           | **Description**          |
| ---------------- | --------------------- |
| VENC_CUSize32x32 | CU block size 32*32; supported only for H.265 |
| VENC_CUSize16x16 | CU block size 16*16; supported only for H.265 |
| VENC_CUSize8x8   | CU block size 8*8; supported only for H.265 |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_SMART_MODE_E

&emsp;&emsp;【Description】

&emsp;&emsp;Smart-encoding mode.

&emsp;&emsp;【Definition】

```c
    typedef enum akVENC_SMART_MODE_E {
        VENC_SMART_OFF,
        VENC_SMART_LTR,
        VENC_SMART_GOP_CHANGE,
        VENC_SMART_SKIP_REF,
        VENC_SMART_LTRC,
        VENC_SMART_SKIP_REF_LTRC
    }VENC_SMART_MODE_E;
```

&emsp;&emsp;【Members】

| **Member**                   | **Description** |
| ------------------------ | ----------- |
| VENC_SMART_OFF           | Disabled |
| VENC_SMART_LTR           | Long-term reference-frame mode |
| VENC_SMART_GOP_CHANGE    | Variable-GOP mode |
| VENC_SMART_SKIP_REF      | Skipped-frame reference mode |
| VENC_SMART_LTRC          | Long-term reference-frame candidate mode |
| VENC_SMART_SKIP_REF_LTRC | LTRC skipped-frame reference mode |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_SPEC_PARAM_TYPE_E

&emsp;&emsp;【Description】

&emsp;&emsp;Special encoding-parameter setting.

&emsp;&emsp;【Definition】

```c
    typedef enum akVENC_SPEC_PARAM_TYPE_E {
        VENC_SPEC_PARAM_START_TYPE,
        VENC_MAX_REORDER_PICS_NUM,
        VENC_SPEC_PARAM_END_TYPE
    }VENC_SPEC_PARAM_TYPE_E;
```

&emsp;&emsp;【Members】

| **Member**                     | **Description**          |
| -------------------------- | --------------------- |
| VENC_SPEC_PARAM_START_TYPE | Starting value |
| VENC_MAX_REORDER_PICS_NUM  | Sets the reorder-pictures count |
| VENC_SPEC_PARAM_END_TYPE   | Ending value |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_CHN_ATTRS_S

&emsp;&emsp;【Description】

&emsp;&emsp;Video-encoding parameter structure, passed to open/set-attribute operations.

&emsp;&emsp;【Definition】

```c
    typedef struct akVENC_CHN_ATTRS_S
    {
        VENC_ATTR_S stVencAttrs;
        VENC_RC_ATTRS_S stRcAttrs;
        VENC_EXT_ATTRS_S stExtAttrs;
    }VENC_CHN_ATTRS_S;
```

&emsp;&emsp;【Members】

| **Member**      | **Description** |
| ----------- | ----------- |
| stVencAttrs | Basic encoding-channel parameters |
| stRcAttrs   | Rate-control parameters |
| stExtAttrs  | Extended/advanced encoding attributes |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_ATTR_S

&emsp;&emsp;【Description】

&emsp;&emsp;Basic parameters used by an encoding channel.

&emsp;&emsp;【Definition】

```c
    typedef struct akVENC_ATTR_S
    {
        AK_U16 u16Width;
        AK_U16 u16Height;
        VENC_OUTPUT_TYPE_E enOutputType;
        AK_U32 u32MaxBufSize;
        AK_U32 u32MaxDMASize;
        VENC_CHROMA_MODE_E enChromaMode; //color formats
        AK_U32 u32Priority;
        union
        {
            VENC_H264_ATTR_S stH264Attr;
            VENC_H265_ATTR_S stH265Attr;
        };
    }VENC_ATTR_S;
```

&emsp;&emsp;【Members】

| **Member**        | **Description**        |
| ------------- | ------------------- |
| u16Width      | Encoding width |
| u16Height     | Encoding height |
| enOutputType  | Encoded-output type |
| u32MaxBufSize | Encoding-buffer size, in KBytes |
| u32MaxDMASize | DMA size used by the encoder, in KBytes |
| enChromaMode  | Image format supplied for encoding |
| u32Priority   | Encoding-channel priority |
| stH264Attr    | Parameters required for H.264 encoding |
| stH265Attr    | Parameters required for H.265 encoding |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_RC_ATTRS_S

&emsp;&emsp;【Description】

&emsp;&emsp;Encoding rate-control mode and parameters.

&emsp;&emsp;【Definition】

```c
    typedef struct akVENC_RC_ATTRS_S
    {
        VENC_BITRATE_CTRL_MODE_E enRcMode;
        union
        {
        VENC_RC_H264_CBR_S stH264Cbr;
        VENC_RC_H264_VBR_S stH264Vbr;
        VENC_RC_H264_CAPPED_VBR_S stH264CappedVbr;
        VENC_RC_H264_AVBR_S stH264Avbr;
        VENC_RC_H264_CONST_QP_S stH264ConstQp;
        VENC_RC_MJPEG_S stMjpegRc;
        VENC_RC_H265_CBR_S stH265Cbr;
        VENC_RC_H265_VBR_S stH265Vbr;
        VENC_RC_H265_CAPPED_VBR_S stH265CappedVbr;
        VENC_RC_H265_AVBR_S stH265Avbr;
        VENC_RC_H265_CONST_QP_S stH265ConstQp;
        };
    }VENC_RC_ATTRS_S;
```

&emsp;&emsp;【Members】

| **Member**          | **Description**        |
| --------------- | ------------------- |
| enRcMode        | Encoding rate-control mode |
| stH264Cbr       | H.264 CBR-mode parameters |
| stH264Vbr       | H.264 VBR-mode parameters |
| stH264CappedVbr | H.264 CAPPED_VBR-mode parameters |
| stH264Avbr      | H.264 AVBR-mode parameters |
| stH264ConstQp   | H.264 const-QP-mode parameters |
| stMjpegRc       | MJPEG rate-control parameters |
| stH265Cbr       | H.265 CBR-mode parameters |
| stH265Vbr       | H.265 VBR-mode parameters |
| stH265CappedVbr | H.265 CAPPED_VBR-mode parameters |
| stH265Avbr      | H.265 AVBR-mode parameters |
| stH265ConstQp   | H.265 const-QP-mode parameters |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_EXT_ATTRS_S

&emsp;&emsp;【Description】

&emsp;&emsp;Extended parameter attributes.

&emsp;&emsp;【Definition】

```c
typedef struct akVENC_EXT_ATTRS_S
{
    VENC_RC_AVC_HEVC_ADVANCE_S stAdvance;
    VENC_RC_AVC_HEVC_SMART_S stSmart;
}VENC_EXT_ATTRS_S;
```

&emsp;&emsp;【Members】

| **Member**    | **Description**           |
| --------- | ---------------------- |
| stAdvance | Advanced encoding parameters, which generally do not need to be set |
| stSmart   | Smart-encoding-mode parameters for H.264/H.265 |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_RC_AVC_HEVC_ADVANCE_S

&emsp;&emsp;【Description】

&emsp;&emsp;Advanced parameter attributes.

&emsp;&emsp;【Definition】

```c
typedef struct akVENC_RC_AVC_HEVC_ADVANCE_S
{
    VENC_CU_BLOCK_SIZE_E enCuBlock;
    AK_U16 u16MinQP[3];
    AK_U16 u16MaxQP[3];
    AK_S16 s16IPDelta;
    AK_U32 u32MaxPictureISize;
    AK_U32 u32MaxPicturePSize;
    AK_U32 u32MaxPictureBSize;
    AK_BOOL bEnableSRD;
    AK_U8 u8SRDThreshold;
    AK_BOOL bEnableMMA;
}VENC_RC_AVC_HEVC_ADVANCE_S;
```

&emsp;&emsp;【Members】

| **Member**             | **Description**                                 |
| ------------------ | -------------------------------------------- |
| enCuBlock          | Advanced encoding parameter; generally does not need to be set |
| u16MinQP           | Minimum QP for I/P/B frames; generally used in CBR and VBR modes, where QP cannot be set separately |
| u16MaxQP           | Maximum QP for I/P/B frames; generally used in CBR and VBR modes, where QP cannot be set separately |
| s16IPDelta         | Delta between I-frame and P-frame QP values |
| u32MaxPictureISize | Maximum I-frame size, in Kbits |
| u32MaxPicturePSize | Maximum P-frame size, in Kbits |
| u32MaxPictureBSize | Maximum B-frame size, in Kbits |
| bEnableSRD         | Enables static-region detection |
| u8SRDThreshold     | Static-region detection threshold |
| bEnableMMA         | Minimum Memory Allocation mode; the reference and reconstructed frames share one buffer |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_RC_AVC_HEVC_SMART_S

&emsp;&emsp;【Description】

&emsp;&emsp;Smart-encoding mode further reduces the bit rate for H.264 and H.265 encoding.

&emsp;&emsp;【Definition】

```c
typedef struct akVENC_RC_AVC_HEVC_SMART_S
{
    VENC_SMART_MODE_E enSmartMode;
    AK_U16 u16SmartGopLen;
    AK_U16 u16SmartQuality;
    AK_U16 u16StaticValue;
}VENC_RC_AVC_HEVC_SMART_S;
```

&emsp;&emsp;【Members】

| **Member**          | **Description** |
| --------------- | --------- |
| enSmartMode     | Smart-encoding mode |
| u16SmartGopLen  | Smart GOP length |
| u16SmartQuality | Smart-encoding quality |
| u16StaticValue  | Static threshold |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_H264_ATTR_S

&emsp;&emsp;【Description】

&emsp;&emsp;Basic H.264 encoding parameters.

&emsp;&emsp;【Definition】

```c
typedef struct akVENC_H264_ATTR_S
{
    AK_U16    u16Framerate;
    AK_U16    u16GopLen;
    VENC_GDR_MODE_E    enGdrMode;
    VENC_PROFILE_MODE_E    enProfileMode;
    VENC_ENCODE_LEVEL_E enEncLevel;
}VENC_H264_ATTR_S;
```

&emsp;&emsp;【Members】

| **Member**        | **Description**                                                                             |
| ------------- | ---------------------------------------------------------------------------------------- |
| u16Framerate  | Encoding frame rate.<br />Fractional frame rates are supported. The high 8 bits hold the denominator and the low 8 bits hold the numerator; a high-byte value of 0 or 1 means a denominator of 1. For example, for 12.5 fps, enter 0xA7D; the encoding library displays 12500/1000. |
| u16GopLen     | I-frame interval |
| enGdrMode     | GDR mode |
| enProfileMode | Profile mode |
| enEncLevel    | Encoding level |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_H265_ATTR_S

&emsp;&emsp;【Description】

&emsp;&emsp;Basic H.265 encoding parameters.

&emsp;&emsp;【Definition】

```c
typedef struct akVENC_H265_ATTR_S
{
    AK_U16    u16Framerate;
    AK_U16    u16GopLen;
    VENC_GDR_MODE_E    enGdrMode;
    VENC_PROFILE_MODE_E    enProfileMode;
    VENC_ENCODE_LEVEL_E enEncLevel;
}VENC_H265_ATTR_S;
```

&emsp;&emsp;【Members】

| **Member**        | **Description** |
| ------------- | --------- |
| u16Framerate  | Encoding frame rate |
| u16GopLen     | I-frame interval |
| enGdrMode     | GDR mode |
| enProfileMode | Profile mode |
| enEncLevel    | Encoding level |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_RC_H264_CBR_S

&emsp;&emsp;【Description】

&emsp;&emsp;H.264 CBR rate-control parameters.

&emsp;&emsp;【Definition】

```c
typedef struct akVENC_RC_H264_CBR_S
{
    AK_U16 u16TargetBitrate;
}VENC_RC_H264_CBR_S;
```

&emsp;&emsp;【Members】

| **Member**           | **Description** |
| ---------------- | -------- |
| u16TargetBitrate | Target bit rate, in kbit |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_RC_H264_VBR_S

&emsp;&emsp;【Description】

&emsp;&emsp;H.264 VBR rate-control parameters.

&emsp;&emsp;【Definition】

```c
typedef struct akVENC_RC_H264_VBR_S
{
    AK_U16 u16MaxBitrate;
    AK_U16 u16Quality;
}VENC_RC_H264_VBR_S;
```

&emsp;&emsp;【Members】

| **Member** | **Description** |
| ------------- | --------- |
| u16MaxBitrate | Maximum bit rate, in Kbits |
| u16Quality    | Encoding quality |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_RC_H264_CAPPED_VBR_S

&emsp;&emsp;【Description】

&emsp;&emsp;H.264 CAPPED_VBR rate-control parameters.

&emsp;&emsp;【Definition】

```c
typedef struct akVENC_RC_H264_CAPPED_VBR_S
{
    AK_U16 u16MinQP;
    AK_U16 u16MaxQP;
    AK_U16 u16MaxBitRate;
    AK_U16 u16ChangePos;  //[0, 100]
    AK_DOUBLE d64MinPSNR; //[0, 100]
    AK_DOUBLE d64MaxPSNR; //[0, 100]
}VENC_RC_H264_CAPPED_VBR_S;
```

&emsp;&emsp;【Members】

| **Member**        | **Description**                                  |
| ------------- | --------------------------------------------- |
| u16MinQP      | Minimum encoding QP |
| u16MaxQP      | Maximum encoding QP |
| u16MaxBitRate | Maximum bit rate, in Kbits |
| u16ChangePos  | Proportional factor in `targetBitrate = maxBitrate*changePos/100` |
| d64MinPSNR    | Minimum PSNR [0, 100] |
| d64MaxPSNR    | Maximum PSNR [0, 100] |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_RC_H264_AVBR_S

&emsp;&emsp;【Description】

&emsp;&emsp;H.264 AVBR rate-control parameters.

&emsp;&emsp;【Definition】

```c
typedef struct akVENC_RC_H264_AVBR_S
{
    AK_U16 u16MinQP;
    AK_U16 u16MaxQP;
    AK_U16 u16MaxBitrate;
    AK_U16 u16ChangePos;
}VENC_RC_H264_AVBR_S;
```

&emsp;&emsp;【Members】

| **Member** | **Description** |
| ------------- | --------------------------------------------- |
| u16MinQP | Minimum encoding QP |
| u16MaxQP | Maximum encoding QP |
| u16MaxBitrate | Maximum bit rate, in Kbits |
| u16ChangePos | Proportional factor in `targetBitrate = maxBitrate*changePos/100` |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_RC_H264_CONST_QP_S

&emsp;&emsp;【Description】

&emsp;&emsp;H.264 CONST QP rate-control parameters.

&emsp;&emsp;【Definition】

```c
typedef struct akVENC_RC_H264_CONST_QP_S
{
    AK_U16 u16QP;
}VENC_RC_H264_CONST_QP_S;
```

&emsp;&emsp;【Members】

| **Member**   | **Description** |
| -------- | ------ |
| u16QP    | Encoding QP |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_RC_MJPEG_S

&emsp;&emsp;【Description】

&emsp;&emsp;MJPEG rate-control parameters.

&emsp;&emsp;【Definition】

```c
typedef struct akVENC_RC_MJPEG_S
{
    AK_U16 u16Quality;
}VENC_RC_MJPEG_S;
```

&emsp;&emsp;【Members】

| **Member**     | **Description**           |
| ---------- | ---------------------- |
| u16Quality | Encoding quality, range [0, 100], recommended value 75 |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_RC_H265_CBR_S

&emsp;&emsp;【Description】

&emsp;&emsp;H.265 CBR rate-control parameters.

&emsp;&emsp;【Definition】

```c
typedef struct akVENC_RC_H265_CBR_S
{
    AK_U16 u16TargetBitrate;
}VENC_RC_H265_CBR_S;
```

&emsp;&emsp;【Members】

| **Member** | **Description** |
| ---------------- | -------- |
| u16TargetBitrate | Target bit rate, in kbit |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_RC_H265_VBR_S

&emsp;&emsp;【Description】

&emsp;&emsp;H.265 VBR rate-control parameters.

&emsp;&emsp;【Definition】

```c
typedef struct akVENC_RC_H265_VBR_S
{
    AK_U16 u16MaxBitrate;
    AK_U16 u16Quality;
}VENC_RC_H265_VBR_S;
```

&emsp;&emsp;【Members】

| **Member**        | **Description**                                             |
| ------------- | -------------------------------------------------------- |
| u16MaxBitrate | Maximum bit rate, in Kbits |
| u16Quality    | Encoding quality. MinQP formula: `MinQP = MaxQP - Quality*(MaxQP-MinQP)/100` |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_RC_H265_CAPPED_VBR_S

&emsp;&emsp;【Description】

&emsp;&emsp;H.265 CAPPED_VBR rate-control parameters.

&emsp;&emsp;【Definition】

```c
typedef struct akVENC_RC_H265_CAPPED_VBR_S
{
    AK_U16 u16MinQP;
    AK_U16 u16MaxQP;
    AK_U16 u16MaxBitRate;
    AK_U16 u16ChangePos;  //[0, 100]
    AK_DOUBLE d64MinPSNR; //[0, 100]
    AK_DOUBLE d64MaxPSNR; //[0, 100]
}VENC_RC_H265_CAPPED_VBR_S;
```

&emsp;&emsp;【Members】

| **Member** | **Description** |
| ------------- | --------------------------------------------- |
| u16MinQP | Minimum encoding QP |
| u16MaxQP | Maximum encoding QP |
| u16MaxBitRate | Maximum bit rate, in Kbits |
| u16ChangePos | Proportional factor in `targetBitrate = maxBitrate*changePos/100` |
| d64MinPSNR | Minimum PSNR [0, 100] |
| d64MaxPSNR | Maximum PSNR [0, 100] |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_RC_H265_AVBR_S

&emsp;&emsp;【Description】

&emsp;&emsp;H.265 AVBR rate-control parameters.

&emsp;&emsp;【Definition】

```c
typedef struct akVENC_RC_H265_AVBR_S
{
    AK_U16 u16MinQP;
    AK_U16 u16MaxQP;
    AK_U16 u16MaxBitrate;
    AK_U16 u16ChangePos;
}VENC_RC_H265_AVBR_S;
```

&emsp;&emsp;【Members】

| **Member** | **Description** |
| ------------- | --------------------------------------------- |
| u16MinQP | Minimum encoding QP |
| u16MaxQP | Maximum encoding QP |
| u16MaxBitrate | Maximum bit rate, in Kbits |
| u16ChangePos | Proportional factor in `targetBitrate = maxBitrate*changePos/100` |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_RC_H265_CONST_QP_S

&emsp;&emsp;【Description】

&emsp;&emsp;H.265 CONST QP rate-control parameters.

&emsp;&emsp;【Definition】

```c
typedef struct akVENC_RC_H265_CONST_QP_S
{
    AK_U16 u16QP;
}VENC_RC_H265_CONST_QP_S;
```

&emsp;&emsp;【Members】

| **Member** | **Description** |
| -------- | ------ |
| u16QP | Encoding QP |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

<br/>

### VENC_CROP_CFG_S

&emsp;&emsp;【Description】

&emsp;&emsp;Cropped-encoding configuration parameters.

&emsp;&emsp;【Definition】

```c
typedef struct RECT_S {
    AK_U32 u32Width;
    AK_U32 u32Height;
    AK_U32 u32X;
    AK_U32 u32Y;
}RECT_S;

typedef struct akVENC_CROP_CFG_S
{
    AK_BOOL bEnable;
    RECT_S stRect;
}VENC_CROP_CFG_S;
```

&emsp;&emsp;【Members】

| **Member**   | **Description** |
| -------- | -------- |
| bEnable  | Enables cropped-encoding parameters |
| stRect   | Crop coordinates, width, and height |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_VENC_SetCrop(AK_S32 s32ChnId, const VENC_CROP_CFG_S *pstCrop);
```

<br/>

### VENC_STAT_S

&emsp;&emsp;【Description】

&emsp;&emsp;Encoding-channel status information.

&emsp;&emsp;【Definition】

```c
typedef struct akVENC_STAT_S
{
    AK_U32 u32Fps;
    AK_U32 u32GopLen;
    AK_U64 u32Kbps;
    AK_U64 u64MaxPictureSize;
}VENC_STAT_S;
```

&emsp;&emsp;【Members】

| **Member**            | **Description** |
| ----------------- | -------- |
| u32Fps            | Actual encoding frame-rate statistic |
| u32GopLen         | GOP length |
| u32Kbps           | Actual encoding bit-rate statistic |
| u64MaxPictureSize | Maximum encoded-frame size |

&emsp;&emsp;【Related function interface】

```c
    AK_S32 AK_MPI_VENC_GetStat(AK_S32 s32ChnId, VENC_STAT_S *pstStat);
```

<br/>

### VENC_SPEC_PARAM_S

&emsp;&emsp;【Description】

&emsp;&emsp;Special parameters.

&emsp;&emsp;【Definition】

```c
typedef struct akVENC_SPEC_PARAM_S
{
    VENC_SPEC_PARAM_TYPE_E enSpecType;
    union{
        VENC_HEVC_SPEC_PARAM_S stHevcSpecReorder;
    };
}VENC_SPEC_PARAM_S;
```

&emsp;&emsp;【Members】

| **Member** | **Description** |
| ----------------- | -------- |
| enSpecType        | Special encoding-parameter enumeration |
| stHevcSpecReorder | Special parameter setting |

<br/>

### VENC_HEVC_SPEC_PARAM_S

&emsp;&emsp;【Description】

&emsp;&emsp;Special parameter setting.

&emsp;&emsp;【Definition】

```c
typedef struct akVENC_HEVC_SPEC_PARAM_S
{
    AK_U8 u8MaxNumReorderPics;
}VENC_HEVC_SPEC_PARAM_S;
```

&emsp;&emsp;【Members】

| **Member**              | **Description**                                                   |
| ------------------- | -------------------------------------------------------------- |
| u8MaxNumReorderPics | Sets the `vps_max_num_reorder_pics` and `sps_max_num_reorder_pics` parameters in the VPS and SPS |

<br/>

### ROI_SVP_INFO_S

&emsp;&emsp;【Description】

&emsp;&emsp;Region-of-interest encoding attributes.

&emsp;&emsp;【Definition】

```c
typedef struct akROI_SVP_INFO_S
{
    AK_U16 u16RoiNum;
    AK_U16 u16RoiLeft[10];
    AK_U16 u16RoiTop[10];
    AK_U32 u32RoiWidth[10];
    AK_U32 u32RoiHeigh[10];
    AK_S32 s32RoiQuality[10];
}ROI_SVP_INFO_S;
```

&emsp;&emsp;【Members】

| **Member**        | **Description**              |
| ------------- | ------------------------- |
| u16RoiNum     | Number of ROIs; maximum 10 |
| u16RoiLeft    | Starting X-coordinate pixel of the ROI |
| u16RoiTop     | Starting Y-coordinate pixel of the ROI |
| u32RoiWidth   | ROI width |
| u32RoiHeigh   | ROI height |
| s32RoiQuality | QP difference around the ROI, range [-15, 15] |

&emsp;&emsp;【Related function interface】

```c
AK_S32 AK_MPI_VENC_SetRoiSvpInfo(AK_S32 s32ChnId, ROI_SVP_INFO_S *pstRoiParam);
```

<br/>

### AK_VENC_REQ_DMA_BLOCK

&emsp;&emsp;【Description】

​        DMA-block information.

&emsp;&emsp;【Definition】

```c
    #define AK_VENC_MAX_DMA_BLOCK_NUM    20
    typedef struct ak_venc_req_dma_block{
        unsigned int block_num;
        unsigned int block_size[AK_VENC_MAX_DMA_BLOCK_NUM];
    }AK_VENC_REQ_DMA_BLOCK;
```

&emsp;&emsp;【Members】

| **Member**     | **Description** |
| ---------- | ------ |
| block_num  | Number of blocks |
| block_size | Block size |

<br/>

### RATE_CTRL_PARAM_S

&emsp;&emsp;【Description】

&emsp;&emsp;External rate-control parameters.

&emsp;&emsp;【Definition】

```c
typedef struct akRATE_CTRL_PARAM_S
{
    AK_U16 u16SliceQP;
}RATE_CTRL_PARAM_S;
```

&emsp;&emsp;【Members】

| **Member** | **Description** |
| ---------- | ------ |
| u16SliceQP | QP value |

&emsp;&emsp;【Related function interface】

```c
AK_S32 AK_MPI_VENC_SetRcParam(AK_S32 s32ChnId, RATE_CTRL_PARAM_S *pstRcParam);
```

<br/>

### VENC_RC_STATUS_S

&emsp;&emsp;【Description】

&emsp;&emsp;External rate-control status parameters.

&emsp;&emsp;【Definition】

```c
typedef struct akVENC_RC_STATUS_S
{
    AK_U32 u32SumCplx;
    VIDEO_FRAME_TYPE_E eSliceType;
}VENC_RC_STATUS_S;
```

&emsp;&emsp;【Members】

| **Member**     | **Description** |
| ---------- | ------- |
| u32SumCplx | Sum of LCU complexity values |
| eSliceType | Type of the next frame |

&emsp;&emsp;【Related function interface】

```c
AK_S32 AK_MPI_VENC_GetRcStat(AK_S32 s32ChnId, VENC_RC_STATUS_S *pstRcStatus);
```

<br/>

### CUR_QP_PARAM

&emsp;&emsp;【Description】

&emsp;&emsp;Structure for getting the current QP value.

&emsp;&emsp;【Definition】

```c
typedef struct CUR_QP_PARAM_S
{
    AK_S32 s32CurQp;
}CUR_QP_PARAM;
```

&emsp;&emsp;【Members】

| Member       | Description |
| -------- | ----- |
| s32CurQp | Current QP value |

&emsp;&emsp;【Related function interface】

```c
AK_S32 AK_MPI_VENC_GetCurQp(AK_S32 s32ChnId, CUR_QP_PARAM *pstCurQpParam);
```

<br/>

### QP_TABLE_PARAM_S

&emsp;&emsp;【Description】

&emsp;&emsp;QP-table structure.

&emsp;&emsp;【Definition】

```c
typedef struct  akQP_TABLE_PARAM_S
{
    AK_U32 u32NumLCUs;
    AK_U32 u32NumQPPerLCU;
    AK_U32 u32NumBytesPerLCU;
}QP_TABLE_PARAM_S;
```

&emsp;&emsp;【Members】

| Member                | Description           |
| ----------------- | ------------------- |
| u32NumLCUs        | Number of LCUs in one image frame |
| u32NumQPPerLCU    | Number of QP values in one LCU block |
| u32NumBytesPerLCU | Number of bytes occupied by one LCU in QpTable |

&emsp;&emsp;【Related function interface】

```c
AK_S32 AK_MPI_VENC_GetQpTableParam(AK_S32 s32ChnId, QP_TABLE_PARAM_S * pstQpTableParam);
```

<br/>

### RC_TYPE_E

&emsp;&emsp;【Description】

&emsp;&emsp;Rate-control mode.

&emsp;&emsp;【Definition】

```c
typedef enum akRC_TYPE_E
{
    INTERNAL = 0x00,  // Use internal Rate Ctrl of encoder lib.
    EXTERNAL = 0x01,  // Use external Rate Ctrl of user.
}RC_TYPE_E;
```

&emsp;&emsp;【Members】

| **Member** | **Description** |
| -------- | ------ |
| INTERNAL | Internal rate control |
| EXTERNAL | External rate control |

&emsp;&emsp;【Related function interface】

```c
AK_S32 AK_MPI_VENC_SetRcType(AK_S32 s32ChnId, RC_TYPE_E eRcType);
```

<br/>

### USER_EXIF_TAG_TYPE

&emsp;&emsp;【Description】

&emsp;&emsp;Image-file-format tag type.

&emsp;&emsp;【Definition】

```c
typedef enum {
    USER_EXIF_TAG_EXPOSURE_TIME = 0,    // Corresponds to driver-layer EXIF_TAG_EXPOSURE_TIME
    USER_EXIF_TAG_ISO_SPEED_RATINGS = 1, // Corresponds to driver-layer EXIF_TAG_ISO_SPEED_RATINGS
    USER_EXIF_TAG_MAX
} USER_EXIF_TAG_TYPE;
```

&emsp;&emsp;【Members】

| **Member**                          | **Description** |
| ------------------------------- | ------ |
| USER_EXIF_TAG_EXPOSURE_TIME     | Shutter |
| USER_EXIF_TAG_ISO_SPEED_RATINGS | ISO    |
| USER_EXIF_TAG_MAX               | Maximum value |

&emsp;&emsp;【Related function interface】

```c
AK_S32 AK_MPI_VENC_SetExifInfo(AK_S32 s32ChnId, EXIF_INFO* pstExifInfo);
```

<br/>

### USER_ExifRational

&emsp;&emsp;【Description】

&emsp;&emsp;User-specified numerator and denominator.

&emsp;&emsp;【Definition】

```c
typedef struct {
    AK_U32    numerator;
    AK_U32    denominator;
} USER_ExifRational;
```

&emsp;&emsp;【Members】

| Member          | Description |
| ----------- | --- |
| numerator   | Numerator |
| denominator | Denominator |

&emsp;&emsp;【Related function interface】

```c
AK_S32 AK_MPI_VENC_SetExifInfo(AK_S32 s32ChnId, EXIF_INFO* pstExifInfo);
```

<br/>

### EXIF_VALUE

&emsp;&emsp;【Description】

&emsp;&emsp;Exif value.

&emsp;&emsp;【Definition】

```c
typedef union {
    USER_ExifRational rational_value;
    AK_U16 short_value;
} EXIF_VALUE;
```

&emsp;&emsp;【Members】

| Member             | Description   |
| -------------- | ----------- |
| rational_value | User-specified numerator and denominator |
| short_value    | Numeric value |

&emsp;&emsp;【Related function interface】

```c
AK_S32 AK_MPI_VENC_SetExifInfo(AK_S32 s32ChnId, EXIF_INFO* pstExifInfo);
```

<br/>

### EXIF_INFO

&emsp;&emsp;【Description】

&emsp;&emsp;Exif information structure.

&emsp;&emsp;【Definition】

```c
typedef struct {
    USER_EXIF_TAG_TYPE user_tag;
    EXIF_VALUE value;
} EXIF_INFO;
```

&emsp;&emsp;【Members】

| Member       | Description |
| -------- | -------- |
| user_tag | Exif tag type |
| value    | Exif value |

&emsp;&emsp;【Related function interface】

```c
AK_S32 AK_MPI_VENC_SetExifInfo(AK_S32 s32ChnId, EXIF_INFO* pstExifInfo);
```

<br/>
## Get Version Information

### AK_MPI_VENC_GetVersion

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the video-encoding library version.

&emsp;&emsp;【Syntax】

```c
    const AK_CHAR* AK_MPI_VENC_GetVersion(void);
```

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| --------- | ------ |
| Video-encoding module version number | Success |
| NULL      | Failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_venc.so or libmpi_venc.a

&emsp;&emsp;Header: ak_venc.h

<br/>

### AK_MPI_VENC_GetEncLibVersion

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the video-encoding algorithm-library version.

&emsp;&emsp;【Syntax】

```c
    const AK_CHAR* AK_MPI_VENC_GetEncLibVersion(void);
```

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ---------- | ------ |
| Video-encoding algorithm-library version number | Success |
| NULL       | Failure |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_venc.so or libmpi_venc.a

&emsp;&emsp;Header: ak_venc.h

<br/>

## Open/Close the Module

### AK_MPI_VENC_Open

&emsp;&emsp;【Description】

&emsp;&emsp;Opens video encoding. Multiple encoding channels are supported, with one handle per encoder.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

&emsp;&emsp;【Parameters】

| **Parameter**   | **Description** | **Value range**         | **Input/Output** |
| ----------- | ---------- | ------------------- | --------- |
| s32ChnId    | Video-encoding module handle ID | [0,VENC_MAX_USER-1] | Input |
| pstChnAttrs | Video-encoding input parameters | See the structure | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ------- | ---------- |
| 0       | Success |
| Nonzero | Failure; the return value is an error code |

&emsp;&emsp;【Error-code list】

| **Error code**               | **Description** |
| ------------------------- | ---------- |
| ERROR_VENC_INVALID_PARAM  | Invalid argument |
| ERROR_VENC_INIT_LIB_ERROR | Failed to initialize the encoding library |
| ERROR_VENC_OPEN_TOO_MANY  | Maximum number of opens reached |
| ERROR_TYPE_MALLOC_FAILED  | Failed to allocate the buffer |
| ERROR_VENC_OPEN_LIB_ERROR | Failed to open the encoding library |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_venc.so or libmpi_venc.a

&emsp;&emsp;Header: ak_venc.h

&emsp;&emsp;【Call order】

```c
    AK_MPI_VENC_Open(s32ChnId, &stChnAttrs);
    while(1) {
      // get one frame
      AK_MPI_VENC_EncodeFrame(s32ChnId, &u8Frame, u32FrameLen, &vMdinfo, &stStream);
      // Do something
      AK_MPI_VENC_ReleaseStream(s32ChnId, &stStream);
    }
    AK_MPI_VENC_Close(s32ChnId);
```

&emsp;&emsp;【Paired APIs】

```c
    AK_S32 AK_MPI_VENC_Close(AK_S32 s32ChnId);
```

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

> **Note:** The function is reentrant; the VENC module may be opened multiple times.

<br/>

### AK_MPI_VENC_Close

&emsp;&emsp;【Description】

&emsp;&emsp;Closes video encoding.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_MPI_VENC_Close(AK_S32 s32ChnId);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range**         | **Input/Output** |
| -------- | ---------- | ------------------- | --------- |
| s32ChnId | Video-encoding module handle ID | [0,VENC_MAX_USER-1] | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the return value is an error code |

&emsp;&emsp;【Error-code list】

| **Error code**                     | **Description**     |
| ------------------------------- | ---------------- |
| ERROR_VENC_USER_NULL            | No user corresponds to `s32ChnId` |
| ERROR_VENC_DELETE_CHN_FAILED    | Failed to destroy the encoding channel |
| ERROR_VENC_DEL_DMA_BLOCK_FAILED | Failed to destroy the DMA pool |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_venc.so or libmpi_venc.a

&emsp;&emsp;Header: ak_venc.h

&emsp;&emsp;【Call order】

```c
    AK_MPI_VENC_Open(s32ChnId, &stChnAttrs);
    while(1) {
      // get one frame
      AK_MPI_VENC_EncodeFrame(s32ChnId, &u8Frame, u32FrameLen, &vMdinfo, &stStream);
      // Do something
      AK_MPI_VENC_ReleaseStream(s32ChnId, &stStream);
    }
    AK_MPI_VENC_Close(s32ChnId);
```

&emsp;&emsp;【Paired APIs】

```c
    AK_S32 AK_MPI_VENC_Open(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

<br/>

## Encoding Flow

### AK_MPI_VENC_EncodeFrame

&emsp;&emsp;【Description】

&emsp;&emsp;Encodes a frame.

&emsp;&emsp;【Syntax】

```C
AK_S32 AK_MPI_VENC_EncodeFrame(AK_S32 s32ChnId, const AK_U8 *pu8Frame,AK_U32 u32FrameLen,
                                AK_VOID *pvMdinfo, VIDEO_STREAM_S *pstStream);
```

&emsp;&emsp;【Parameters】

| **Parameter**   | **Description**  | **Value range**         | **Input/Output** |
| ----------- | ------------- | ------------------- | --------- |
| s32ChnId    | Video-encoding handle ID | [0,VENC_MAX_USER-1] | Input |
| pu8Frame    | One frame of YUV data to encode | Non-null | Input |
| u32FrameLen | Size of the `pu8Frame` data | - | Input |
| pvMdinfo    | MD statistics array | Non-null | Input |
| pstStream   | One encoded frame | - | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the return value is an error code |

&emsp;&emsp;【Error-code list】

| **Error code**              | **Description**         |
| ------------------------ | -------------------- |
| ERROR_VENC_USER_NULL     | No user corresponds to `s32ChnId` |
| ERROR_VENC_INVALID_PARAM | `pu8Frame` or `pstStream` is null |
| ERROR_TYPE_MALLOC_FAILED | Failed to allocate the data buffer |
| ERROR_TYPE_INVALID_ARG   | Invalid argument |
| ERROR_VENC_ENCODE_FAILED | Encoding error |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_venc.so or libmpi_venc.a

&emsp;&emsp;Header: ak_venc.h

&emsp;&emsp;【Call order】

```c
    AK_MPI_VENC_Open(s32ChnId, &stChnAttrs);
    while(1) {
      // get one frame
      AK_MPI_VENC_EncodeFrame(s32ChnId, &u8Frame, u32FrameLen, &vMdinfo, &stStream);
      // Do something
      AK_MPI_VENC_ReleaseStream(s32ChnId, &stStream);
    }
    AK_MPI_VENC_Close(s32ChnId);
```

&emsp;&emsp;【Paired APIs】

```c
    AK_S32 AK_MPI_VENC_ReleaseStream(AK_S32 s32ChnId, VIDEO_STREAM_S *pstStream);
```

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

<br/>

### AK_MPI_VENC_ReleaseStream

&emsp;&emsp;【Description】

&emsp;&emsp;Releases encoded output data.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_VENC_ReleaseStream(AK_S32 s32ChnId, VIDEO_STREAM_S *pstStream);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range**         | **Input/Output** |
| --------- | -------- | ------------------- | --------- |
| s32ChnId  | Video-encoding handle ID | [0,VENC_MAX_USER-1] | Input |
| pstStream | One encoded frame | - | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the return value is an error code |

&emsp;&emsp;【Error-code list】

| **Error code**                      | **Description**     |
| -------------------------------- | ---------------- |
| ERROR_VENC_INVALID_PARAM         | `pstStream` is null |
| ERROR_VENC_USER_NULL             | No user corresponds to `s32ChnId` |
| ERROR_VENC_RELEASE_STREAM_FAILED | Failed to release the encoded frame |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_venc.so or libmpi_venc.a

&emsp;&emsp;Header: ak_venc.h

&emsp;&emsp;【Call order】

```c
    AK_MPI_VENC_Open(s32ChnId, &stChnAttrs);
    while(1) {
      // get one frame
      AK_MPI_VENC_EncodeFrame(s32ChnId, &u8Frame, u32FrameLen, &vMdinfo, &stStream);
      // Do something
      AK_MPI_VENC_ReleaseStream(s32ChnId, &stStream);
    }
    AK_MPI_VENC_Close(s32ChnId);
```

&emsp;&emsp;【Paired APIs】

```C
AK_S32 AK_MPI_VENC_EncodeFrame(AK_S32 s32ChnId, const AK_U8 *pu8Frame,AK_U32 u32FrameLen,
                                AK_VOID *pvMdinfo, VIDEO_STREAM_S *pstStream);
```

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

<br/>

## Set/Get Parameters

### AK_MPI_VENC_SetAttr

&emsp;&emsp;【Description】

&emsp;&emsp;Sets VENC attribute parameters.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_VENC_SetAttr(AK_S32 s32ChnId, const VENC_CHN_ATTRS_S *pstChnAttrs);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ----------- | ---------- | ------------------- | --------- |
| s32ChnId    | Video-encoding handle ID | [0,VENC_MAX_USER-1] | Input |
| pstChnAttrs | VENC attribute-parameter structure | See `struct venc_param` | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the return value is an error code |

&emsp;&emsp;【Error-code list】

| **Error code**              | **Description**     |
| ------------------------ | ---------------- |
| ERROR_VENC_INVALID_PARAM | Invalid argument |
| ERROR_VENC_USER_NULL     | No user corresponds to `s32ChnId` |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_venc.so or libmpi_venc.a

&emsp;&emsp;Header: ak_venc.h

&emsp;&emsp;【Call order】

```c
    AK_MPI_VENC_Open(s32ChnId, &stChnAttrs);
    AK_MPI_VENC_SetAttr(s32ChnId, &stChnAttrs);
    while(1) {
      // get one frame
      AK_MPI_VENC_EncodeFrame(s32ChnId, &u8Frame, u32FrameLen, &vMdinfo, &stStream);
      // Do something
      AK_MPI_VENC_ReleaseStream(s32ChnId, &stStream);
    }
    AK_MPI_VENC_Close(s32ChnId);
```

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

<br/>

### AK_MPI_VENC_GetAttr

&emsp;&emsp;【Description】

&emsp;&emsp;Gets VENC attribute parameters.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_VENC_GetAttr(AK_S32 s32ChnId, VENC_CHN_ATTRS_S *pstChnAttrs);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ----------- | ---------- | ------------------- | --------- |
| s32ChnId    | Video-encoding handle ID | [0,VENC_MAX_USER-1] | Input |
| pstChnAttrs | VENC attribute-parameter structure | - | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the return value is an error code |

&emsp;&emsp;【Error-code list】

| **Error code** | **Description** |
| ------------------------ | ---------------- |
| ERROR_VENC_INVALID_PARAM | `pstChnAttrs` is null |
| ERROR_VENC_USER_NULL | No user corresponds to `s32ChnId` |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_venc.so or libmpi_venc.a

&emsp;&emsp;Header: ak_venc.h

&emsp;&emsp;【Call order】

```c
    AK_MPI_VENC_Open(s32ChnId, &stChnAttrs);
    AK_MPI_VENC_SetAttr(s32ChnId, &stChnAttrs);
    AK_MPI_VENC_GetAttr(s32ChnId, &stChnAttrs);
    AK_MPI_VENC_Close(s32ChnId);
```

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

<br/>

### AK_MPI_VENC_RequestIdr

&emsp;&emsp;【Description】

&emsp;&emsp;Requests an I-frame. This function is valid only for H.264/H.265; using it with another encoding format returns an error.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_VENC_RequestIdr(AK_S32 s32ChnId);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range**         | **Input/Output** |
| -------- | -------- | ------------------- | --------- |
| s32ChnId | Video-encoding handle ID | [0,VENC_MAX_USER-1] | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the return value is an error code |

&emsp;&emsp;【Error-code list】

| **Error code** | **Description** |
| -------------------- | ---------------- |
| ERROR_VENC_USER_NULL | No user corresponds to `s32ChnId` |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_venc.so or libmpi_venc.a

&emsp;&emsp;Header: ak_venc.h

&emsp;&emsp;【Call order】

```c
    AK_MPI_VENC_Open(s32ChnId, &stChnAttrs);
    AK_MPI_VENC_SetQp(s32ChnId, u32Minqp, u32Maxqp);
    AK_MPI_VENC_SetIframeParam(s32ChnId, u32Minqp, u32Maxqp,
                               u32MinFrameSize, u32MaxFrameSize);
    AK_MPI_VENC_RequestIdr(s32ChnId);
    while(1) {
      // get one frame
      AK_MPI_VENC_EncodeFrame(s32ChnId, &u8Frame, u32FrameLen, &vMdinfo, &stStream);
      // Do something
      AK_MPI_VENC_ReleaseStream(s32ChnId, &stStream);
    }
    AK_MPI_VENC_Close(s32ChnId);
```

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

<br/>

### AK_MPI_VENC_SetQp

&emsp;&emsp;【Description】

&emsp;&emsp;Sets the VENC QP range. This function is valid only for H.264/H.265; using it with another encoding format returns an error.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_VENC_SetQp(AK_S32 s32ChnId, AK_U32 u32Minqp, AK_U32 u32Maxqp);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| -------- | -------- | ------------------- | --------- |
| s32ChnId | Video-encoding handle ID | [0,VENC_MAX_USER-1] | Input |
| u32Minqp | Minimum QP | [10,51], generally 20-30 | Input |
| u32Maxqp | Maximum QP | [10,51], generally 40-50 | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the return value is an error code |

&emsp;&emsp;【Error-code list】

| **Error code** | **Description** |
| ------------------------ | ---------------- |
| ERROR_VENC_INVALID_PARAM | Invalid argument |
| ERROR_VENC_USER_NULL | No user corresponds to `s32ChnId` |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_venc.so or libmpi_venc.a

&emsp;&emsp;Header: ak_venc.h

&emsp;&emsp;【Call order】

```c
    AK_MPI_VENC_Open(s32ChnId, &stChnAttrs);
    AK_MPI_VENC_SetQp(s32ChnId, u32Minqp, u32Maxqp);
    while(1) {
      // get one frame
      AK_MPI_VENC_EncodeFrame(s32ChnId, &u8Frame, u32FrameLen, &vMdinfo, &stStream);
      // Do something
      AK_MPI_VENC_ReleaseStream(s32ChnId, &stStream);
    }
    AK_MPI_VENC_Close(s32ChnId);
```

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

> **Note:** This API has no effect when constant-QP mode is configured.

<br/>

### AK_MPI_VENC_ResetQp

&emsp;&emsp;【Description】

&emsp;&emsp;Resets the VENC QP range to its initial values at open time. This function is valid only for H.264/H.265; using it with another encoding format returns an error.

&emsp;&emsp;【Syntax】

```c
     AK_S32 AK_MPI_VENC_ResetQp(AK_S32 s32ChnId);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| -------- | -------- | ------------------- | --------- |
| s32ChnId | Video-encoding handle ID | [0,VENC_MAX_USER-1] | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the return value is an error code |

&emsp;&emsp;【Error-code list】

| **Error code** | **Description** |
| -------------------- | ---------------- |
| ERROR_VENC_USER_NULL | No user corresponds to `s32ChnId` |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_venc.so or libmpi_venc.a

&emsp;&emsp;Header: ak_venc.h

&emsp;&emsp;【Call order】

```c
    AK_MPI_VENC_Open(s32ChnId, &stChnAttrs);
    AK_MPI_VENC_SetQp(s32ChnId, u32Minqp, u32Maxqp);
    AK_MPI_VENC_ResetQp(s32ChnId);
    while(1) {
      // get one frame
      AK_MPI_VENC_EncodeFrame(s32ChnId, &u8Frame, u32FrameLen, &vMdinfo, &stStream);
      // Do something
      AK_MPI_VENC_ReleaseStream(s32ChnId, &stStream);
    }
    AK_MPI_VENC_Close(s32ChnId);
```

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

> **Note:** This API has no effect when constant-QP mode is configured.

<br/>

### AK_MPI_VENC_SetIframeParam

&emsp;&emsp;【Description】

&emsp;&emsp;Sets VENC I-frame parameters. This function is valid only for H.264/H.265; using it with another encoding format returns an error.

&emsp;&emsp;【Syntax】

```c
AK_S32 AK_MPI_VENC_SetIframeParam(AK_S32 s32ChnId, AK_U32 u32Minqp, AK_U32 u32Maxqp,
                                        AK_U32 u32MinFrameSize, AK_U32 u32MaxFrameSize);
```

&emsp;&emsp;【Parameters】

| **Parameter**       | **Description** | **Value range**                            | **Input/Output** |
| --------------- | -------- | -------------------------------------- | --------- |
| s32ChnId        | Video-encoding handle ID | [0,VENC_MAX_USER-1] | Input |
| u32Minqp        | Minimum I-frame QP | [10,51], generally 20-30; set 0 to use the encoding-library default | Input |
| u32Maxqp        | Maximum I-frame QP | [10,51], generally 40-50; set 0 to use the encoding-library default | Input |
| u32MinFrameSize | Minimum I-frame size | In KBytes; set 0 to use the encoding-library default | Input |
| u32MaxFrameSize | Maximum I-frame size | In KBytes; set 0 to use the encoding-library default | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the return value is an error code |

&emsp;&emsp;【Error-code list】

| **Error code** | **Description** |
| -------------------- | ---------------- |
| ERROR_VENC_USER_NULL | No user corresponds to `s32ChnId` |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_venc.so or libmpi_venc.a

&emsp;&emsp;Header: ak_venc.h

&emsp;&emsp;【Call order】

```c
    AK_MPI_VENC_Open(s32ChnId, &stChnAttrs);
    AK_MPI_VENC_SetIframeParam(s32ChnId, u32Minqp, u32Maxqp,
                               u32MinFrameSize, u32MaxFrameSize);
    AK_MPI_VENC_RequestIdr(s32ChnId);
    while(1) {
      // get one frame
      AK_MPI_VENC_EncodeFrame(s32ChnId, &u8Frame, u32FrameLen, &vMdinfo, &stStream);
      // Do something
      AK_MPI_VENC_ReleaseStream(s32ChnId, &stStream);
    }
    AK_MPI_VENC_Close(s32ChnId);
```

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

<br/>

### AK_MPI_VENC_GetIframeParam

&emsp;&emsp;【Description】

&emsp;&emsp;Gets VENC I-frame parameters. This function is valid only for H.264/H.265; using it with another encoding format returns an error.

&emsp;&emsp;【Syntax】

```c
AK_S32 AK_MPI_VENC_GetIframeParam(AK_S32 s32ChnId, AK_U32 *pu32Minqp, AK_U32 *pu32Maxqp,
                                    AK_U32 *u32MinFrameSize, AK_U32 *pu32MaxFrameSize);
```

&emsp;&emsp;【Parameters】

| **Parameter**        | **Description** | **Value range**         | **Input/Output** |
| ---------------- | -------- | ------------------- | --------- |
| s32ChnId         | Video-encoding handle ID | [0,VENC_MAX_USER-1] | Input |
| pu32Minqp        | Minimum I-frame QP | [10,51], generally 20-30 | Output |
| pu32Maxqp        | Maximum I-frame QP | [10,51], generally 40-50 | Output |
| u32MinFrameSize  | Minimum I-frame size | In KBytes | Output |
| pu32MaxFrameSize | Maximum I-frame size | In KBytes | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the return value is an error code |

&emsp;&emsp;【Error-code list】

| **Error code** | **Description** |
| ------------------------ | ---------------- |
| ERROR_VENC_USER_NULL | No user corresponds to `s32ChnId` |
| ERROR_VENC_INVALID_PARAM | Invalid argument |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_venc.so or libmpi_venc.a

&emsp;&emsp;Header: ak_venc.h

&emsp;&emsp;【Call order】

```c
    AK_MPI_VENC_Open(s32ChnId, &stChnAttrs);
    AK_MPI_VENC_SetIframeParam(s32ChnId, u32Minqp, u32Maxqp,
                               u32MinFrameSize, u32MaxFrameSize);
    AK_MPI_VENC_GetIframeParam(s32ChnId, u32Minqp, u32Maxqp,
                               u32MinFrameSize, u32MaxFrameSize);
    AK_MPI_VENC_RequestIdr(s32ChnId);
    while(1) {
      // get one frame
      AK_MPI_VENC_EncodeFrame(s32ChnId, &u8Frame, u32FrameLen, &vMdinfo, &stStream);
      // Do something
      AK_MPI_VENC_ReleaseStream(s32ChnId, &stStream);
    }
    AK_MPI_VENC_Close(s32ChnId);
```

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

<br/>

### AK_MPI_VENC_SetRoiMdinfo

&emsp;&emsp;【Description】

&emsp;&emsp;Sets ROI-related parameters. ROI reduces noise in night-vision images. This function is valid only for H.264/H.265; using it with another encoding format returns an error.

> **Note:** AK3918EV200L does not support this API.

&emsp;&emsp;【Syntax】

```c
AK_S32 AK_MPI_VENC_SetRoiMdinfo(AK_S32 s32ChnId, AK_U32 u32Threshold, AK_S32 u32Quality,                         AK_S32 u32RecoverStep, AK_U32 u32WaitIntra, AK_U32 u32WaitSkip);
```

&emsp;&emsp;【Parameters】

| **Parameter**      | **Description**                                    | **Value range**                       | **Input/Output** |
| -------------- | ------------------------------------------------- | --------------------------------- | --------- |
| s32ChnId       | Video-encoding handle ID | [0,VENC_MAX_USER-1] | Input |
| u32Threshold   | Motion-detection threshold for distinguishing moving/static regions | [0,65535] | Input |
| u32Quality     | Maximum QP increment | 0 < current QP + u32Quality <= 51 | Input |
| u32RecoverStep | QP decrement applied on each recovery step | u32RecoverStep <= u32Quality | Input |
| u32WaitIntra   | Frame count at which forced intra coding begins; 0 disables forced intra coding | Generally no greater than u32Quality/u32RecoverStep+1 | Input |
| u32WaitSkip    | Frame count at which forced skipping begins; 0 disables forced skipping.<br/>A skipped frame uses reference-frame data without encoding. | Generally no greater than u32Quality/u32RecoverStep+1 | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the return value is an error code |

&emsp;&emsp;【Error-code list】

| **Error code** | **Description** |
| -------------------- | ---------------- |
| ERROR_VENC_USER_NULL | No user corresponds to `s32ChnId` |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_venc.so or libmpi_venc.a

&emsp;&emsp;Header: ak_venc.h

&emsp;&emsp;【Call order】

```c
    AK_MPI_VENC_Open(s32ChnId, &stChnAttrs);
    AK_MPI_VENC_SetRoiMdinfo(s32ChnId, u32Threshold, u32Quality,
                             RecoverStep, u32WaitIntra, u32WaitSkip);
    while(1) {
      // get one frame
      AK_MPI_VENC_EncodeFrame(s32ChnId, &u8Frame, u32FrameLen, &vMdinfo, &stStream);
      // Do something
      AK_MPI_VENC_ReleaseStream(s32ChnId, &stStream);
    }
    AK_MPI_VENC_Close(s32ChnId);
```

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

<br/>

### AK_MPI_VENC_SetRoiSvpInfo

&emsp;&emsp;【Description】

&emsp;&emsp;Sets ROI-region parameters.

&emsp;&emsp;【Syntax】

```c
AK_S32 AK_MPI_VENC_SetRoiSvpInfo(AK_S32 s32ChnId, ROI_SVP_INFO_S *pstRoiParam);
```

&emsp;&emsp;【Parameters】

| **Parameter**   | **Description** | **Value range**         | **Input/Output** |
| ----------- | -------- | ------------------- | --------- |
| s32ChnId    | Video-encoding handle ID | [0,VENC_MAX_USER-1] | Input |
| pstRoiParam | ROI parameters | - | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the return value is an error code |

&emsp;&emsp;【Error-code list】

| **Error code** | **Description** |
| ------------------------ | ------ |
| ERROR_VENC_INVALID_PARAM | Invalid argument |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_venc.so or libmpi_venc.a

&emsp;&emsp;Header: ak_venc.h

&emsp;&emsp;【Call order】

```c
    AK_MPI_VENC_Open(s32ChnId, &stChnAttrs);
    AK_MPI_VENC_SetRoiSvpInfo(s32ChnId, &stRoiParam);
    while(1) {
      // get one frame
      AK_MPI_VENC_EncodeFrame(s32ChnId, &u8Frame, u32FrameLen, &vMdinfo, &stStream);
      // Do something
      AK_MPI_VENC_ReleaseStream(s32ChnId, &stStream);
    }
    AK_MPI_VENC_Close(s32ChnId);
```

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

<br/>

### AK_MPI_VENC_StriclylimitFrameSize

&emsp;&emsp;【Description】

&emsp;&emsp;Sets a hard frame-size limit. This function is valid only for H.264/H.265; using it with another encoding format returns an error. Do not set the limit too low, as this can cause severe image loss and a breathing artifact.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_VENC_StriclylimitFrameSize(AK_S32 s32ChnId, AK_U32 u32MaxSize);
```

&emsp;&emsp;【Parameters】

| **Parameter**  | **Description** | **Value range**         | **Input/Output** |
| ---------- | ------------ | ------------------- | --------- |
| s32ChnId   | Video-encoding handle ID | [0,VENC_MAX_USER-1] | Input |
| u32MaxSize | Frame size, in KBytes | - | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the return value is an error code |

&emsp;&emsp;【Error-code list】

| **Error code** | **Description** |
| ------------------------ | ---------------- |
| ERROR_VENC_USER_NULL | No user corresponds to `s32ChnId` |
| ERROR_VENC_INVALID_PARAM | `u32MaxSize` is less than 0 |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_venc.so or libmpi_venc.a

&emsp;&emsp;Header: ak_venc.h

&emsp;&emsp;【Call order】

```c
    AK_MPI_VENC_Open(s32ChnId, &stChnAttrs);
    AK_MPI_VENC_StriclylimitFrameSize(s32ChnId, u32MaxSize);
    while(1) {
      // get one frame
      AK_MPI_VENC_EncodeFrame(s32ChnId, &u8Frame, u32FrameLen, &vMdinfo, &stStream);
      // Do something
      AK_MPI_VENC_ReleaseStream(s32ChnId, &stStream);
    }
    AK_MPI_VENC_Close(s32ChnId);
```

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

<br/>

### AK_MPI_VENC_GetStat

&emsp;&emsp;【Description】

&emsp;&emsp;Gets VENC statistics. This function is meaningful only for H.264/H.265.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_VENC_GetStat(AK_S32 s32ChnId, VENC_STAT_S *pstStat);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**   | **Value range**         | **Input/Output** |
| -------- | -------------- | ------------------- | --------- |
| s32ChnId | Video-encoding handle ID | [0,VENC_MAX_USER-1] | Input |
| pstStat  | Pointer to a VENC-statistics structure | See the structure | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the return value is an error code |

&emsp;&emsp;【Error-code list】

| **Error code** | **Description** |
| ------------------------ | ---------------- |
| ERROR_VENC_USER_NULL | No user corresponds to `s32ChnId` |
| ERROR_VENC_INVALID_PARAM | `pstStat` is a null pointer |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_venc.so or libmpi_venc.a

&emsp;&emsp;Header: ak_venc.h

&emsp;&emsp;【Call order】

```c
   AK_MPI_VENC_Open(s32ChnId, &stChnAttrs);
   AK_MPI_VENC_GetStat(s32ChnId, &stStat);
   AK_MPI_VENC_Close(s32ChnId);
```

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

<br/>

### AK_MPI_VENC_SetJpegSlice

&emsp;&emsp;【Description】

&emsp;&emsp;Sets JPEG slice-encoding parameters. Slice encoding divides the data into sections and sends one section at a time to the encoder. It is primarily used when memory is insufficient or the image data to encode is large.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_VENC_SetJpegSlice(AK_S32 s32ChnId, AK_U32 u32PicHeight,
                                                        AK_U32 u32FirstSliceHeight);
```

&emsp;&emsp;【Parameters】

| **Parameter**           | **Description** | **Value range**            | **Input/Output** |
| ------------------- | -------- | ---------------------- | --------- |
| s32ChnId            | Video-encoding handle ID | [0,VENC_MAX_USER-1] | Input |
| u32PicHeight        | Total frame height | Greater than 0, in pixel rows | Input |
| u32FirstSliceHeight | Height of the first slice | Slice height must be a multiple of 16, in pixel rows | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the return value is an error code |

&emsp;&emsp;【Error-code list】

| **Error code**              | **Description**                       |
| ------------------------ | ---------------------------------- |
| ERROR_VENC_USER_NULL     | No user corresponds to `s32ChnId` |
| ERROR_VENC_INVALID_PARAM | `u32PicHeight` or `u32FirstSliceHeight` is 0 |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_venc.so or libmpi_venc.a

&emsp;&emsp;Header: ak_venc.h

&emsp;&emsp;【Call order】

```c
    AK_MPI_VENC_Open(s32ChnId, &stChnAttrs);
    AK_MPI_VENC_SetJpegSlice(s32ChnId, u32PicHeight, u32FirstSliceHeight);
    for(int i = 0; i < u32PicHeight / u32FirstSliceHeight; i++)
    {   u32SliceIdx = i;
        AK_MPI_VENC_JpegSliceEncode(s32ChnId, pu8Frame, u32FrameLen,
                                    u32SliceIdx, u32SliceHeight, pstStream);
    }
   // Do something
   AK_MPI_VENC_ReleaseStream(s32ChnId, &stStream);
   AK_MPI_VENC_Close(s32ChnId);
```

&emsp;&emsp;【Paired APIs】

```c
AK_S32  AK_MPI_VENC_JpegSliceEncode(AK_S32 s32ChnId, const AK_U8 *pu8Frame,
                        AK_U32 u32FrameLen, AK_U32 u32SliceIdx, AK_U32 u32SliceHeight,
                                                    VIDEO_STREAM_S  *pstStream);
```

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

<br/>

### AK_MPI_VENC_JpegSliceEncode

&emsp;&emsp;【Description】

&emsp;&emsp;Performs JPEG slice encoding.

&emsp;&emsp;【Syntax】

```c
AK_S32  AK_MPI_VENC_JpegSliceEncode(AK_S32 s32ChnId, const AK_U8 *pu8Frame,
                        AK_U32 u32FrameLen, AK_U32 u32SliceIdx, AK_U32 u32SliceHeight,
                                                    VIDEO_STREAM_S  *pstStream);
```

&emsp;&emsp;【Parameters】

| **Parameter**      | **Description** | **Value range**                                  | **Input/Output** |
| -------------- | --------- | -------------------------------------------- | --------- |
| s32ChnId       | Video-encoding handle ID | [0,VENC_MAX_USER-1] | Input |
| pu8Frame       | One frame of data to encode | - | Input |
| u32FrameLen    | Length of the frame data to encode | - | Input |
| u32SliceIdx    | Slice sequence number | Greater than 0 | Input |
| u32SliceHeight | Slice height | The first slice height must be a multiple of 16 and the last a multiple of 8, in pixel rows | Input |
| pstStream      | One encoded frame | See the structure | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the return value is an error code |

&emsp;&emsp;【Error-code list】

| **Error code**              | **Description**           |
| ------------------------ | ---------------------- |
| ERROR_VENC_USER_NULL     | No user corresponds to `s32ChnId` |
| ERROR_VENC_INVALID_PARAM | `pu8Frame` or `pstStream` is a null pointer |
| ERROR_TYPE_MALLOC_FAILED | `malloc` failed |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_venc.so or libmpi_venc.a

&emsp;&emsp;Header: ak_venc.h

&emsp;&emsp;【Call order】

```c
    AK_MPI_VENC_Open(s32ChnId, &stChnAttrs);
    AK_MPI_VENC_SetJpegSlice(s32ChnId, u32PicHeight, u32FirstSliceHeight);
    for(int i = 0; i < u32PicHeight / u32FirstSliceHeight; i++)
    {   u32SliceIdx = i;
        AK_MPI_VENC_JpegSliceEncode(s32ChnId, pu8Frame, u32FrameLen,
                                    u32SliceIdx, u32SliceHeight, pstStream);
    }
   // Do something
   AK_MPI_VENC_ReleaseStream(s32ChnId, &stStream);
   AK_MPI_VENC_Close(s32ChnId);
```

&emsp;&emsp;【Paired APIs】

```c
    AK_S32 AK_MPI_VENC_SetJpegSlice(AK_S32 s32ChnId, AK_U32 u32PicHeight,
                                                        AK_U32 u32FirstSliceHeight);
```

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

<br/>

### AK_MPI_VENC_SetFps

&emsp;&emsp;【Description】

&emsp;&emsp;Sets the encoding frame rate in slice mode.

> **Note:** This API is supported only during slice-mode encoding.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_VENC_SetFps(AK_S32 s32ChnId, AK_U32 u32Fps);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| -------- | -------- | ------------------- | --------- |
| s32ChnId | Video-encoding handle ID | [0,VENC_MAX_USER-1] | Input |
| u32Fps   | Frame rate | - | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the return value is an error code |

&emsp;&emsp;【Error-code list】

| **Error code** | **Description** |
| ------------------------ | ---------------- |
| ERROR_VENC_INVALID_PARAM | Invalid argument |
| ERROR_VENC_USER_NULL | No user corresponds to `s32ChnId` |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_venc.so or libmpi_venc.a

&emsp;&emsp;Header: ak_venc.h

> **Note:** This API is supported only during slice-mode encoding.

<br/>

### AK_MPI_VENC_GetCrop

&emsp;&emsp;【Description】

&emsp;&emsp;Gets cropped-encoding information for the current channel.

&emsp;&emsp;【Syntax】

```c
     AK_S32 AK_MPI_VENC_GetCrop(AK_S32 s32ChnId, VENC_CROP_CFG_S *pstCrop);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| -------- | -------- | ------------------- | --------- |
| s32ChnId | Video-encoding handle ID | [0,VENC_MAX_USER-1] | Input |
| pstCrop  | Crop-box information | - | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the return value is an error code |

&emsp;&emsp;【Error-code list】

| **Error code**              | **Description** |
| ------------------------ | ------------ |
| ERROR_VENC_INVALID_PARAM | Invalid argument |
| ERROR_VENC_USER_NULL     | No channel corresponds to the encoding handle |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_venc.so or libmpi_venc.a

&emsp;&emsp;Header: ak_venc.h

> **Note:** After `AK_MPI_VENC_SetCrop`, encode one frame to apply the latest crop parameters. Call this API only after encoding that frame to obtain the correct crop information.

<br/>

### AK_MPI_VENC_SetCrop

&emsp;&emsp;【Description】

&emsp;&emsp;Sets cropped-encoding information for the current channel.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_VENC_SetCrop(AK_S32 s32ChnId, const VENC_CROP_CFG_S *pstCrop);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range**                                          | **Input/Output** |
| -------- | -------- | ---------------------------------------------------- | --------- |
| s32ChnId | Video-encoding handle ID | [0,VENC_MAX_USER-1] | Input |
| pstCrop  | Crop-box information | Width and height must be greater than 8 and below their maxima; the starting X coordinate must be a multiple of 32, the starting Y coordinate a multiple of 2, and both starting coordinates at least 0 | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the return value is an error code |

&emsp;&emsp;【Error-code list】

| **Error code** | **Description** |
| ------------------------ | ------------ |
| ERROR_VENC_INVALID_PARAM | Invalid argument |
| ERROR_VENC_USER_NULL | No channel corresponds to the encoding handle |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_venc.so or libmpi_venc.a

&emsp;&emsp;Header: ak_venc.h

<br/>

### AK_MPI_VENC_SetFunction

&emsp;&emsp;【Description】

&emsp;&emsp;Dynamic-scene-switching enable logic and other function-enable logic.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_VENC_SetFunction(AK_S32 s32ChnId,AK_U32 u32Function);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ----------- | ------------- | ------------------- | --------- |
| s32ChnId | Video-encoding handle ID | [0,VENC_MAX_USER-1] | Input |
| u32Function | Value with the function-enable bit set | Greater than 0 and at most 1023 | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the return value is an error code |

&emsp;&emsp;【Error-code list】

| **Error code** | **Description** |
| ------------------------ | ------------ |
| ERROR_VENC_INVALID_PARAM | Invalid argument |
| ERROR_VENC_USER_NULL | No channel corresponds to the encoding handle |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_venc.so or libmpi_venc.a

&emsp;&emsp;Header: ak_venc.h

<br/>

### AK_MPI_VENC_GetFunction

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the currently selected dynamic-scene-switching logic.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_VENC_GetFunction(AK_S32 s32ChnId,AK_U32 *pu32Function);
```

&emsp;&emsp;【Parameters】

| **Parameter**    | **Description** | **Value range**         | **Input/Output** |
| ------------ | ------------ | ------------------- | --------- |
| s32ChnId     | Video-encoding handle ID | [0,VENC_MAX_USER-1] | Input |
| pu32Function | Receives the value with the function-enable bit set | - | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the return value is an error code |

&emsp;&emsp;【Error-code list】

| **Error code** | **Description** |
| ------------------------ | ------------ |
| ERROR_VENC_INVALID_PARAM | Invalid argument |
| ERROR_VENC_USER_NULL | No channel corresponds to the encoding handle |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_venc.so or libmpi_venc.a

&emsp;&emsp;Header: ak_venc.h

<br/>

### AK_MPI_VENC_SetRcType

&emsp;&emsp;【Description】

&emsp;&emsp;Sets the rate-control mode.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_VENC_SetRcType(AK_S32 s32ChnId, RC_TYPE_E eRcType);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range**             | **Input/Output** |
| -------- | -------- | ----------------------- | --------- |
| s32ChnId | Video-encoding handle ID | [0,VENC_MAX_USER-1] | Input |
| eRcType  | Rate-control mode | 0: internal rate control; 1: external rate control | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the return value is an error code |

&emsp;&emsp;【Error-code list】

| **Error code** | **Description** |
| ------------------------ | ------------ |
| ERROR_VENC_INVALID_PARAM | Invalid argument |
| ERROR_VENC_USER_NULL | No channel corresponds to the encoding handle |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_venc.so or libmpi_venc.a

&emsp;&emsp;Header: ak_venc.h

<br/>

### AK_MPI_VENC_SetRcParam

&emsp;&emsp;【Description】

&emsp;&emsp;Sets external rate-control parameters.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_VENC_SetRcParam(AK_S32 s32ChnId, RATE_CTRL_PARAM_S *pstRcParam);
```

&emsp;&emsp;【Parameters】

| **Parameter**  | **Description** | **Value range**         | **Input/Output** |
| ---------- | -------- | ------------------- | --------- |
| s32ChnId   | Video-encoding handle ID | [0,VENC_MAX_USER-1] | Input |
| pstRcParam | External rate-control parameters | - | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the return value is an error code |

&emsp;&emsp;【Error-code list】

| **Error code** | **Description** |
| ------------------------ | ------------ |
| ERROR_VENC_INVALID_PARAM | Invalid argument |
| ERROR_VENC_USER_NULL | No channel corresponds to the encoding handle |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_venc.so or libmpi_venc.a

&emsp;&emsp;Header: ak_venc.h

<br/>

### AK_MPI_VENC_GetRcStat

&emsp;&emsp;【Description】

&emsp;&emsp;Gets rate-control information.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_VENC_GetRcStat(AK_S32 s32ChnId, VENC_RC_STATUS_S *pstRcStatus);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ----------- | -------- | ------------------- | --------- |
| s32ChnId | Video-encoding handle ID | [0,VENC_MAX_USER-1] | Input |
| pstRcStatus | Rate-control information | - | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the return value is an error code |

&emsp;&emsp;【Error-code list】

| **Error code** | **Description** |
| ------------------------ | ------------ |
| ERROR_VENC_INVALID_PARAM | Invalid argument |
| ERROR_VENC_USER_NULL | No channel corresponds to the encoding handle |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_venc.so or libmpi_venc.a

&emsp;&emsp;Header: ak_venc.h

<br/>

### AK_MPI_VENC_SetStreamBufSize

&emsp;&emsp;【Description】

&emsp;&emsp;Sets the encoding library's internal stream-buffer size.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_VENC_SetStreamBufSize(AK_S32 s32ChnId, AK_U32 u32Size);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range**         | **Input/Output** |
| -------- | ------------ | ------------------- | --------- |
| s32ChnId | Video-encoding handle ID | [0,VENC_MAX_USER-1] | Input |
| u32Size  | Stream-buffer size | >0, in KBytes | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the return value is an error code |

&emsp;&emsp;【Error-code list】

| **Error code** | **Description** |
| ------------------------ | ------------ |
| ERROR_VENC_INVALID_PARAM | Invalid argument |
| ERROR_VENC_USER_NULL | No channel corresponds to the encoding handle |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_venc.so or libmpi_venc.a

&emsp;&emsp;Header: ak_venc.h

<br/>

### AK_MPI_VENC_SetQpTable

&emsp;&emsp;【Description】

&emsp;&emsp;Sets the QP table.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_VENC_SetQpTable(AK_S32 s32ChnId, AK_U8 * pu8QpTable, AK_S32 s32QpTableSize, bool bRelativeQp, bool bAutoQp, bool bQpTableEnable);
```

&emsp;&emsp;【Parameters】

| **Parameter**      | **Description**     | **Value range**          | **Input/Output** |
| -------------- | ---------------- | -------------------- | --------- |
| s32ChnId       | Video-encoding handle ID | [0,VENC_MAX_USER-1] | Input |
| pu8QpTable     | Pointer to the QP table | - | Input |
| s32QpTableSize | QP-table size | - | Input |
| bRelativeQp    | Whether the QP table contains relative QP values | 0: absolute QP, 1: relative QP | Input |
| bAutoQp        | Whether to enable automatic QP | 0: disabled, 1: enabled | Input |
| bQpTableEnable | Whether to enable the QpTable function | 0: disabled, 1: enabled | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the return value is an error code |

&emsp;&emsp;【Error-code list】

| **Error code**          | **Description**      |
| -------------------- | ----------------- |
| ERROR_VENC_USER_NULL | No user corresponds to `handle_id` |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_venc.so or libmpi_venc.a

&emsp;&emsp;Header: ak_venc.h

### AK_MPI_VENC_GetQpTableParam

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the QP table.

&emsp;&emsp;【Syntax】

```c
AK_S32 AK_MPI_VENC_GetQpTableParam(AK_S32 s32ChnId, QP_TABLE_PARAM_S * pstQpTableParam);
```

&emsp;&emsp;【Parameters】

| **Parameter**       | **Description**  | **Value range**         | **Input/Output** |
| --------------- | ------------- | ------------------- | --------- |
| s32ChnId        | Video-encoding handle ID | [0,VENC_MAX_USER-1] | Input |
| pstQpTableParam | Pointer to a QP-table structure | | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the return value is an error code |

&emsp;&emsp;【Error-code list】

| **Error code** | **Description** |
| -------------------- | ----------------- |
| ERROR_VENC_USER_NULL | No user corresponds to `handle_id` |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_venc.so or libmpi_venc.a

&emsp;&emsp;Header: ak_venc.h

### AK_MPI_VENC_GetCurQp

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the current QP value.

&emsp;&emsp;【Syntax】

```c
AK_S32 AK_MPI_VENC_GetCurQp(AK_S32 s32ChnId, CUR_QP_PARAM *pstCurQpParam);
```

&emsp;&emsp;【Parameters】

| **Parameter**     | **Description** | **Value range**         | **Input/Output** |
| ------------- | -------- | ------------------- | --------- |
| s32ChnId      | Video-encoding handle ID | [0,VENC_MAX_USER-1] | Input |
| pstCurQpParam | QP value | | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the return value is an error code |

&emsp;&emsp;【Error-code list】

| **Error code** | **Description** |
| -------------------- | ----------------- |
| ERROR_VENC_USER_NULL | No user corresponds to `handle_id` |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_venc.so or libmpi_venc.a

&emsp;&emsp;Header: ak_venc.h

### AK_MPI_VENC_GetStream

&emsp;&emsp;【Description】

&emsp;&emsp;Gets an encoded frame from the buffer pool so that a fast-start application can retrieve an already encoded frame directly.

&emsp;&emsp;【Syntax】

```c
AK_S32 AK_MPI_VENC_GetStream(AK_S32 s32ChnId, VIDEO_STREAM_S *pstStream);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| --------- | -------- | ------------------- | --------- |
| s32ChnId  | Video-encoding handle ID | [0,VENC_MAX_USER-1] | Input |
| pstStream | Bitstream structure | | Output |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the return value is an error code |

&emsp;&emsp;【Error-code list】

| **Error code** | **Description** |
| -------------------- | ----------------- |
| ERROR_VENC_USER_NULL | No user corresponds to `handle_id` |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_venc.so or libmpi_venc.a

&emsp;&emsp;Header: ak_venc.h

<br/>

### AK_MPI_VENC_SetExifEnable

&emsp;&emsp;【Description】

&emsp;&emsp;Enables Exif.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_VENC_SetExifEnable(AK_S32 s32ChnId, bool bExifEnable);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ----------- | -------- | ------------------- | --------- |
| s32ChnId | Video-encoding handle ID | [0,VENC_MAX_USER-1] | Input |
| bExifEnable | Exif enable switch | 0: disabled; 1: enabled | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the return value is an error code |

&emsp;&emsp;【Error-code list】

| **Error code** | **Description** |
| -------------------- | ---------------- |
| ERROR_VENC_USER_NULL | No user corresponds to `s32ChnId` |
| AK_FAILED            | Failed to set |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_venc.so or libmpi_venc.a

&emsp;&emsp;Header: ak_venc.h

<br/>

### AK_MPI_VENC_SetExifInfo

&emsp;&emsp;【Description】

&emsp;&emsp;Sets Exif information.

&emsp;&emsp;【Syntax】

```c
    AK_S32 AK_MPI_VENC_SetExifInfo(AK_S32 s32ChnId, EXIF_INFO* pstExifInfo);
```

&emsp;&emsp;【Parameters】

| **Parameter**   | **Description** | **Value range**         | **Input/Output** |
| ----------- | --------- | ------------------- | --------- |
| s32ChnId    | Video-encoding handle ID | [0,VENC_MAX_USER-1] | Input |
| pstExifInfo | Exif information structure | - | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ------- | ---------- |
| 0 | Success |
| Nonzero | Failure; the return value is an error code |

&emsp;&emsp;【Error-code list】

| **Error code** | **Description** |
| -------------------- | ---------------- |
| ERROR_VENC_USER_NULL | No user corresponds to `s32ChnId` |
| AK_FAILED | Failed to set |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libmpi_venc.so or libmpi_venc.a

&emsp;&emsp;Header: ak_venc.h

<br/>
## API Usage Scenarios

| **Function**                         | **H.264** | **H.265** | **MJPEG** |
| --------------------------------- | --------- | --------- | --------- |
| AK_MPI_VENC_GetVersion            | Supported | Supported        | Supported |
| AK_MPI_VENC_GetEncLibVersion      | Supported | Supported        | Supported |
| AK_MPI_VENC_Open                  | Supported | Supported        | Supported |
| AK_MPI_VENC_Close                 | Supported | Supported        | Supported |
| AK_MPI_VENC_EncodeFrame           | Supported | Supported        | Supported |
| AK_MPI_VENC_ReleaseStream         | Supported | Supported        | Supported |
| AK_MPI_VENC_SetAttr               | Supported | Supported        | Supported |
| AK_MPI_VENC_GetAttr               | Supported | Supported        | Supported |
| AK_MPI_VENC_RequestIdr            | Supported | Supported        | Not supported |
| AK_MPI_VENC_SetQp                 | Supported | Supported        | Not supported |
| AK_MPI_VENC_ResetQp               | Supported | Supported        | Not supported |
| AK_MPI_VENC_SetIframeParam        | Supported | Supported        | Not supported |
| AK_MPI_VENC_GetIframeParam        | Supported | Supported        | Not supported |
| AK_MPI_VENC_SetRoiMdinfo          | Supported | Supported        | Not supported |
| AK_MPI_VENC_SetRoiSvpInfo         | Supported | Supported        | Not supported |
| AK_MPI_VENC_StriclylimitFrameSize | Supported | Supported        | Not supported |
| AK_MPI_VENC_GetStat               | Supported | Supported        | Supported |
| AK_MPI_VENC_SetJpegSlice          | Not supported | Not supported       | Supported |
| AK_MPI_VENC_JpegSliceEncode       | Not supported | Not supported       | Supported |
| AK_MPI_VENC_SetRcType             | Supported | Supported        | Not supported |
| AK_MPI_VENC_SetRcParam            | Supported | Supported        | Not supported |
| AK_MPI_VENC_GetRcStat             | Supported | Supported        | Not supported |
| AK_MPI_VENC_SetStreamBufSize      | Supported | Supported        | Supported |

<br/>

## ak_venc_sample Usage Example

Before running the sample, use `insmod` to load `ak_vi.ko`, `sensor_xxx.ko`, `ak_vicap.ko`, `ak_isp.ko`, `ak_pp.ko`, `ak_venc_adapter.ko`, and `ak_venc_bridge.ko`. For the exact commands, see the description at the start of Chapter 7.

| **Input parameter** | **Description**                                                                                                                                                                                                                                                                                                                                |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| frame-num      | Number of frames captured from VI. |
| data-output    | Encoded-output format: h264, h265, or jpeg. |
| br_mode        | Rate-control mode: 0 cbr, 1 vbr. This parameter is not needed for JPEG. |
| target_kbps    | Target bit rate. This parameter is not needed for JPEG. |
| frame-rate     | Frame rate. This parameter is not needed for JPEG. |
| main-res       | Main-channel resolution, [0, 17].<br/>[0 - 17] 0 - 320\*184; 1 - 320\*240; 2 - 640\*360; 3 - 640\*480; 4 - 736\*756; 5 - 1280\*720; 6 - 1280\*960; 7 - 1920\*1080; 8 - 2304\*1296; 9 - 2048\*1536; 10 - 2560\*1440; 11 - 2688\*1520; 12 - 2880\*1624; 13 - 2560\*1920; 14 - 2944\*1664; 15 - 3072\*1728; 16 - 3072\*2048; 17 - 3840\*2160. |
| sub-res        | Secondary-channel resolution [0, 3], no greater than the main-channel resolution.<br/>[0 - 3] 0 - 320\*184; 1 - 320\*240; 2 - 640\*360; 3 - 640\*480. |
| third_res      | Third-channel resolution [0, 3].<br/>[0 - 3] 0 - 320\*184; 1 - 320\*240; 2 - 640\*360; 3 - 640\*480. |
| save-path      | Path in which the encoded bitstream is saved |
| channel        | VI channel: 0 main channel, 1 secondary channel. |
| input-mode     | YUV data-input mode: 0 VI, 1 read from a file |
| input-path     | Input-source path. For VI capture, this is the ISP configuration path; for file input, it is the directory containing the file. AK37E chips do not require an ISP configuration. |
| dev_cnt        | Number of devices [1, 2]; default 1, or 2 for the binocular version |
| cycle          | Number of cycles; default 1 |
| save_file_flag | Save flag: 0 do not save, 1 save; default 1. |

<br/>

&emsp;&emsp;Output: an encoded video-bitstream file saved in the specified `path` directory.

<br/>

## /var/platform Description

The `/var/platform` directory exposes the current module's configuration parameters and status. Its parameters are described below.

### param

| Parameter                | Description   |
| ---------------------- | ----------- |
| venc0_width            | Encoding width |
| venc0_height           | Encoding height |
| venc0_enc_type         | Encoding type |
| venc0_fps              | Encoding frame rate |
| venc0_goplen           | GOP length |
| venc0_enc_level        | Encoding level |
| venc0_profile          | Encoding profile |
| venc0_chroma_mode      | chroma mode |
| venc0_max_picture_size | External-buffer size |
| venc0_br_mode          | Rate-control mode |

### stat

| Parameter                  | Description           |
| ------------------------ | ------------------- |
| version                  | VENC middleware version |
| akv_enc_version          | Encoding-library version |
| "venc0":        "opened" | Encoding-channel status: open / close |

<br/>

## Error Codes

| Error code | Macro                                  | Meaning          |
| ---------- | ----------------------------------- | -------------- |
| 0x0d000000 | ERROR_VENC_INIT_LIB_ERROR           | Library initialization error |
| 0x0d000001 | ERROR_VENC_OPEN_LIB_ERROR           | Library open error |
| 0x0d000002 | ERROR_VENC_OPEN_TOO_MANY            | Opened too many times |
| 0x0d000003 | ERROR_VENC_INVALID_PARAM            | Group already created |
| 0x0d000004 | ERROR_VENC_USER_NULL                | Module is not running |
| 0x0d000005 | ERROR_VENC_PARAM_CANNOT_DYNAMIC_SET | Parameter cannot be set dynamically |
| 0x0d000006 | ERROR_VENC_ENCODE_FAILED            | Encoding failed |
| 0x0d000007 | ERROR_VENC_DEV_OPEN_FAILED          | Group already enabled |
| 0x0d000008 | ERROR_VENC_CREATE_CHN_FAILED        | Failed to create the channel |
| 0x0d000009 | ERROR_VENC_DELETE_CHN_FAILED        | Failed to delete the channel |
| 0x0d00000a | ERROR_VENC_QUERY_DMA_INFO_FAILED    | Failed to query DMA information |
| 0x0d00000b | ERROR_VENC_SET_DMA_BLOCK_FAILED     | Failed to set the DMA block |
| 0x0d00000c | ERROR_VENC_DEL_DMA_BLOCK_FAILED     | Failed to delete the DMA block |
| 0x0d00000d | ERROR_VENC_GET_STREAM_FAILED        | Failed to get the stream |
| 0x0d00000e | ERROR_VENC_RELEASE_STREAM_FAILED    | Failed to release the stream |
| 0x0d00000f | ERROR_VENC_CLEAN_STREAM_FAILED      | Failed to clear the stream |
| 0x0d000010 | ERROR_VENC_SET_JPEG_SLICE_FAILED    | Failed to configure JPEG slice encoding |
| 0x0d000011 | ERROR_VENC_DMA_NO_ENOUGH            | Insufficient DMA |
| 0x0d000012 | ERROR_VENC_SET_ATTR_ERROR           | Attribute-structure setting error |

<br/>
