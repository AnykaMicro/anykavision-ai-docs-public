# Motion Detection Algorithm

## Overview

&emsp;&emsp;The motion detection algorithm module (MRD module) supports configuration of parameters such as the sensitivity threshold and moving-block-count threshold.

<br/>

## API Reference

&emsp;&emsp;This module provides the following APIs.

| **Library interface**              | **Description**             |
| ---------------------------------- | --------------------------- |
| MD_SIZE                            | Horizontal size of the VPSS MD statistics array |
| MAX_CAP                            | Maximum number of moving regions in a detection result |
| MRD_RECTANGLE                      | Structure for a moving region in a detection result |
| ak_mrd_get_version                 | Gets the MRD algorithm-library version |
| ak_mrd_init                        | Initializes the MRD module |
| ak_mrd_destroy                     | Destroys the MRD module |
| ak_mrd_set_filters                 | Sets the detection thresholds |
| ak_mrd_set_motion_region_size      | Sets the detection-area size |
| ak_mrd_set_mode                    | Sets single-frame or multi-frame detection mode |
| ak_mrd_set_floating_wadding_params | Sets multi-frame filtering parameters |
| ak_mrd                             | Main detection API |
<br/>

## Data Structures

### MD_SIZE

&emsp;&emsp;【Description】

&emsp;&emsp;Horizontal size of the VPSS MD statistics array.

&emsp;&emsp;【Definition】

```c
    #define MD_SIZE  64
```

<br/>

### MAX_CAP

&emsp;&emsp;【Description】

&emsp;&emsp;Maximum number of moving regions in a detection result.

&emsp;&emsp;【Definition】

```c
    #define MAX_CAP  20
```

<br/>

###  MRD_RECTANGLE

&emsp;&emsp;【Description】

&emsp;&emsp;Structure for a moving region in a detection result.

&emsp;&emsp;【Definition】

```C
typedef struct
{
	int left;
	int top;
	int right;
	int bottom;
	int count;
}MRD_RECTANGLE;
```

&emsp;&emsp;【Members】

| **Member**    | **Description**                                       |
| ------------- | ----------------------------------------------------- |
| left          | Horizontal coordinate of the region's upper-left corner (coordinates are relative to 32\*24/32\*16; the same applies below) |
| top           | Vertical coordinate of the region's upper-left corner |
| right         | Horizontal coordinate of the region's lower-right corner |
| bottom        | Vertical coordinate of the region's lower-right corner |
| count         | Number of moving regions |

&emsp;&emsp;【Related API】

```C
    int ak_mrd(void *mrd_handle, unsigned short md[][MD_SIZE], int len, MRD_RECTANGLE boxes[MAX_CAP]);
```

<br/>

## Get Version Information

###  ak_mrd_get_version

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the version number of the MRD library.

&emsp;&emsp;【Syntax】

```C
    char* ak_mrd_get_version();
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------- | --------- | ------------- | -------------- |
| None          | -         | -             |                |

&emsp;&emsp;【Return values】

| **Return value**        | **Description** |
| ----------------------- | --------- |
| Pointer to the MRD module version string | Success |
| NULL                    | Failure   |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libak_mrd.a or libak_mrd.so

&emsp;&emsp;Header: ak_mrd.h

<br/>

## Motion Detection Flow

###  ak_mrd_init

&emsp;&emsp;【Description】

&emsp;&emsp;Initializes the MRD module and returns a pointer to the MRD handle.

&emsp;&emsp;【Syntax】

```C
    void *ak_mrd_init(void);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------- | --------- | ------------- | -------------- |
| void          | -         | -             | -              |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ----------- | ----------- |
| Non-NULL    | Pointer to the MRD handle |
| NULL        | Failure     |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libak_mrd.a or libak_mrd.so

&emsp;&emsp;Header: ak_mrd.h

<br/>

###  ak_mrd_destroy

&emsp;&emsp;【Description】

&emsp;&emsp;Destroys the MRD module.

&emsp;&emsp;【Syntax】

```C
    int ak_mrd_destroy(void *mrd_handle);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------- | ----------- | ------------- | -------------- |
| mrd_handle    | Pointer to the MRD handle | - | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ----------- | --------- |
| 0           | Success.  |
| -1          | Failure   |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libak_mrd.a or libak_mrd.so

&emsp;&emsp;Header: ak_mrd.h

<br/>

###  ak_mrd

&emsp;&emsp;【Description】

&emsp;&emsp;Main motion detection API.

&emsp;&emsp;【Syntax】

```C
    int ak_mrd(void *mrd_handle, unsigned short md[][MD_SIZE], int len, MRD_RECTANGLE boxes[MAX_CAP]);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**   | **Value range** | **Input/Output** |
| ------------- | ----------------- | ------------- | -------------- |
| mrd_handle    | Pointer to the MRD handle | -       | Input          |
| md            | `vpss_md` array   |               | Input          |
| len           | Height of the `vpss_md` array | 24 or 32 | Input       |
| boxes         | Coordinates of moving regions |         | Output      |

&emsp;&emsp;【Return values】

| **Return value** | **Description**        |
| ----------- | ---------------------- |
| -1          | Failure                |
| Other       | Number of moving regions detected |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libak_mrd.a or libak_mrd.so

&emsp;&emsp;Header: ak_mrd.h

<br/>

## Parameter Configuration

### ak_mrd_set_filters

&emsp;&emsp;【Description】

&emsp;&emsp;Sets the detection thresholds.

&emsp;&emsp;【Syntax】

```C
    int ak_mrd_set_filters(void *mrd_handle, unsigned short flt_big, unsigned short flt_small);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------- | ----------- | ------------- | -------------- |
| mrd_handle    | Pointer to the MRD handle | - | Input |
| flt_big       | Larger threshold | [0, 65535] | Input |
| flt_small     | Smaller threshold | [0, 65535] | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ----------- | --------- |
| 0           | Success.    |
| -1          | Failure     |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libak_mrd.a or libak_mrd.so

&emsp;&emsp;Header: ak_mrd.h

<br/>

### ak_mrd_set_motion_region_size

&emsp;&emsp;【Description】

&emsp;&emsp;Sets the detection-area size.

&emsp;&emsp;【Syntax】

```C
    int ak_mrd_set_motion_region_size(void *mrd_handle, int size_min, int size_max);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**  | **Value range** | **Input/Output** |
| ------------- | ---------------- | ------------- | -------------- |
| mrd_handle    | Pointer to the MRD handle | - | Input |
| size_min      | Minimum detection-area size | [1, size_max] | Input |
| size_max      | Maximum detection-area size | [1, 768] | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ----------- | --------- |
| 0           | Success.    |
| -1          | Failure     |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libak_mrd.a or libak_mrd.so

&emsp;&emsp;Header: ak_mrd.h

<br/>

### ak_mrd_set_mode

&emsp;&emsp;【Description】

&emsp;&emsp;Sets the detection mode (multi-frame or single-frame mode).

&emsp;&emsp;【Syntax】

```C
    int ak_mrd_set_mode(void *mrd_handle, unsigned char mode);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range**                    | **Input/Output** |
| ------------- | ----------- | ----------------------------------- | -------------- |
| mrd_handle    | Pointer to the MRD handle | -                         | Input |
| mode          | Detection mode | [0, 255]; 0: multi-frame mode; other values: single-frame mode | Input |

&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ----------- | --------- |
| 0           | Success.    |
| -1          | Failure     |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libak_mrd.a or libak_mrd.so

&emsp;&emsp;Header: ak_mrd.h

<br/>

### ak_mrd_set_floating_wadding_params

&emsp;&emsp;【Description】

&emsp;&emsp;Sets the multi-frame filtering parameters.

&emsp;&emsp;【Syntax】

```C
    int ak_mrd_set_floating_wadding_params(void *mrd_handle, int m_frames, int s_frames, int extra_frames,
	int dis, int m_width, int m_height);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**                | **Value range**  | **Input/Output** |
| ------------- | ------------------------------ | ---------------- | -------------- |
| mrd_handle    | Pointer to the MRD handle      | -                | Input |
| m_frames      | Number of consecutive moving frames | [2, 10]     | Input |
| s_frames      | Number of moving frames that need not be consecutive | [1,extra_frames] | Input |
| extra_frames  | Additional frames allowed for satisfying the `s_frames` condition | [1, 20] | Input |
| dis           | Square of the maximum valid motion distance | [1, 64] | Input |
| m_width       | Minimum detection width        | [1, 32]          | Input |
| m_height      | Minimum detection height       | [1, 24]          | Input |
&emsp;&emsp;【Return values】

| **Return value** | **Description** |
| ----------- | --------- |
| 0           | Success.    |
| -1          | Failure     |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Libraries: libak_mrd.a or libak_mrd.so

&emsp;&emsp;Header: ak_mrd.h

<br/>
