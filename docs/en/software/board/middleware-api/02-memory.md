# Memory Management

## Overview

&emsp;&emsp;The memory-management module (MEM) is part of the platform software infrastructure and is independent of the underlying operating system.

&emsp;&emsp;It manages and traces memory while software is running and configures related functions.

<br/>

## API Reference

&emsp;&emsp;This module provides the APIs listed below.

| **Library interface** | **Description** |
| ----------------------------------- | ---------------------------------------------------- |
| AK_BASE_MemAlloc | Allocates memory and records the allocation. |
| AK_BASE_MemFree | Frees memory. |
| AK_BASE_MemPoolInit | Initializes a memory pool. |
| AK_BASE_MemPoolDestroy | Destroys a memory pool and frees all of its blocks. |
| AK_BASE_MemPoolAlloc | Gets a block from a specified memory pool, automatically expanding the pool if necessary. |
| AK_BASE_MemPoolFree | Returns a block obtained from a memory pool. |
| AK_BASE_MemRbInit | Initializes a circular buffer. |
| AK_BASE_MemRbDestroy | Frees a circular buffer. |
| AK_BASE_MemRbReset | Resets a circular buffer. |
| AK_BASE_MemRbWrite | Writes data to a circular buffer. |
| AK_BASE_MemRbReadRequest | Gets a read pointer from a circular buffer. |
| AK_BASE_MemRbReadCancel | Marks a read pointer as unused. |
| AK_BASE_MemRbRead | Reads data from a circular buffer. |
| AK_BASE_MemRbGetDataSize | Gets the amount of data in a circular buffer. |
| AK_BASE_MemDmaAlloc | Allocates DMA memory. |
| AK_BASE_MemDmaFree | Frees DMA memory. |
| AK_BASE_MemDmaVaddr2Paddr | Converts a virtual address to a physical address. |
| AK_BASE_MemDmaPoolCreate | Creates a DMA memory pool. |
| AK_BASE_MemDmaPoolActivate | Initializes a DMA memory pool. |
| AK_BASE_MemDmaPoolExit | Exits a DMA memory pool. |
| AK_BASE_MemDmaPoolGetUsedMem | Gets the used size of a DMA memory pool. |
| AK_BASE_MemDmaPoolGetFreeMem | Gets the free size of a DMA memory pool. |
| AK_BASE_MemDmaPoolSetThreshold | Sets a DMA memory-pool allocation threshold. |
| AK_BASE_MemDmaPoolCreateReservedObj | Creates a specific reserved-memory object in a DMA memory pool. |
| AK_BASE_MemGetVersion | Gets memory-management module version information. |
| AK_BASE_MemGetUsedDetail | Queries details of allocated memory blocks. |
| AK_BASE_MemReleaseUsedDetail | Frees the linked list used to record memory-block usage details. |
| AK_BASE_MemGetUsedTotal | Queries the total memory allocated by a module, in bytes. |
| AK_BASE_MemDmaGetUsed | Queries the total DMA memory allocated by a module, in bytes. |
| AK_BASE_MemDmaGetReservedSize | Queries the system reserved-memory size, in bytes. |
| AK_BASE_MemGetTotalSize | Queries the total system-memory size, in bytes. |

<br/>

## Data Structures

### **USED_MEM_INFO_S**

&emsp;&emsp;【Notes】

&emsp;&emsp;Details of an allocated memory block.

&emsp;&emsp;【Definition】

```c
typedef struct akUSED_MEM_INFO_S {
    AK_S32 s32ModuleId;
    AK_CHAR acFunc[20];
    AK_S64 s64Time;
    AK_U32 u32Size;
    AK_VOID* pvAddr;
    struct akUSED_MEM_INFO_S *pstNext;
}USED_MEM_INFO_S;
```

&emsp;&emsp;【Members】

| **Member** | **Description**                           |
| ------------ | ---------------------------------- |
| s32ModuleId | Module ID that allocated the block |
| acFunc[20] | Name of the function that allocated the block |
| s64Time | Time at which the block was allocated |
| u32Size | Allocated block size in bytes |
| pvAddr | Address of the allocated block |
| pstNext | Pointer to the next memory-block record |

&emsp;&emsp;【Related Functions】

```c
    AK_S32 AK_BASE_MemGetUsedDetail(AK_S32 s32ModuleId, USED_MEM_INFO_S **ppstMemUsed);
```

<br/>

## Basic Interfaces

### **AK_BASE_MemAlloc**

&emsp;&emsp;【Description】

&emsp;&emsp;Allocates memory and records the allocation.

&emsp;&emsp;【Syntax】

```C
    AK_VOID* AK_BASE_MemAlloc(AK_S32 s32ModuleId, AK_U32 u32Size);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**           | **Value range** | **Input/Output** |
| ------------ | ------------------ | ------------ | ------------- |
| s32ModuleId | ID of the module allocating the block | - | Input |
| u32Size | Size of each memory block | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**                                         |
| ---------- | ------------------------------------------------ |
| AK_VOID\* | Start address of the allocated block on success; NULL on failure. |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_mem.a or libplat_mem.so

&emsp;&emsp;Header: ak_mem.h

&emsp;&emsp;The macro-wrapped interface is:

```c
    #define AK_BASE_MemAlloc(s32ModuleId, u32Size) \
    AK_BASE_MemAlloc_(s32ModuleId, u32Size, __FUNCTION__, AK_BASE_GetOsTimeStamp())
```
> **Note:** This interface does not clear successfully allocated memory. Call memset if zero initialization is required.

<br/>

### **AK_BASE_MemFree**

&emsp;&emsp;【Description】

&emsp;&emsp;Frees memory.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_MemFree(AK_VOID *pvPtr);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**           | **Value range** | **Input/Output** |
| ------------ | ------------------ | ------------ | ------------- |
| pvPtr | Start address of the memory to free | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**               |
| ---------- | ---------------------- |
| 0          | Success                   |
| Nonzero | Failure; the return value is an error code. |

&emsp;&emsp;【Error Code List】

| **Error code**             | **Description** |
| ---------------------- | -------- |
| ERROR_TYPE_INVALID_ARG | Invalid parameter |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_mem.a or libplat_mem.so

&emsp;&emsp;Header: ak_mem.h

<br/>

## Memory-Pool Management

### **AK_BASE_MemPoolInit**

&emsp;&emsp;【Description】

&emsp;&emsp;Initializes a memory pool. This interface is wrapped by a macro.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_MemPoolInit(AK_S32 *ps32PoolId, AK_S32 s32ModuleId, \
    AK_U32 u32Nmemb, AK_U32 u32Size);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**                       | **Value range** | **Input/Output** |
| ------------ | ------------------------------ | ------------ | ------------- |
| ps32PoolId | Allocated memory-pool ID | - | Output |
| s32ModuleId | ID of the module allocating the memory pool | - | Input |
| u32Nmemb | Number of blocks in the allocated memory pool | - | Input |
| u32Size | Size of each block, in bytes | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**           |
| ---------- | ------------------ |
| 0          | Success               |
| Nonzero | Failure; returns an error code. |

&emsp;&emsp;【Error Code List】

| **Error code**                    | **Description** |
| ----------------------------- | -------- |
| ERROR_TYPE_POINTER_NULL | Null pointer |
| ERROR_TYPE_INVALID_ARG        | Invalid parameter |
| ERROR_TYPE_NO_ENOUGH_RESOURCE | Insufficient resources |
| ERROR_TYPE_MALLOC_FAILED | Allocation failed |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_mem.a or libplat_mem.so

&emsp;&emsp;Header: ak_mem.h

<br/>

### **AK_BASE_MemPoolDestroy**

&emsp;&emsp;【Description】

&emsp;&emsp;Destroys a memory pool and frees all blocks in it.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_MemPoolDestroy(AK_S32 s32MemPoolId);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**         | **Value range** | **Input/Output** |
| ------------ | ---------------- | ------------ | ------------- |
| s32MemPoolId | ID of the memory pool to destroy | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**           |
| ---------- | ------------------ |
| 0          | Success               |
| Nonzero | Failure; returns an error code. |

&emsp;&emsp;【Error Code List】

| **Error code**             | **Description** |
| ---------------------- | -------- |
| ERROR_TYPE_INVALID_ARG | Invalid parameter |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_mem.a or libplat_mem.so

&emsp;&emsp;Header: ak_mem.h

<br/>

### **AK_BASE_MemPoolAlloc**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets a block from a specified memory pool, automatically expanding the pool if necessary.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_MemPoolAlloc(AK_VOID **ppMemBlk, AK_S32 s32MemPoolId);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**                       | **Value range** | **Input/Output** |
| ------------ | ------------------------------ | ------------ | ------------- |
| ppMemBlk | Start address of the block allocated from the pool | - | Output |
| s32MemPoolId | Memory-pool ID | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**           |
| ---------- | ------------------ |
| 0          | Success               |
| Nonzero | Failure; returns an error code. |

&emsp;&emsp;【Error Code List】

| **Error code**                    | **Description** |
| ----------------------------- | -------- |
| ERROR_TYPE_INVALID_ARG        | Invalid parameter |
| ERROR_TYPE_NO_ENOUGH_RESOURCE | Insufficient resources |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_mem.a or libplat_mem.so

&emsp;&emsp;Header: ak_mem.h

<br/>

### **AK_BASE_MemPoolFree**

&emsp;&emsp;【Description】

&emsp;&emsp;Returns memory obtained from a memory pool.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_MemPoolFree(AK_VOID *pvPtr, AK_S32 s32MemPoolId);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**             | **Value range** | **Input/Output** |
| ------------ | -------------------- | ------------ | ------------- |
| pvPtr | Start address of the block to return | Non-NULL | Input |
| s32MemPoolId | Memory-pool ID | [0-8] | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**           |
| ---------- | ------------------ |
| 0          | Success               |
| Nonzero | Failure; returns an error code. |

&emsp;&emsp;【Error Code List】

| **Error code**              | **Description** |
| ----------------------- | -------- |
| ERROR_TYPE_POINTER_NULL | Null pointer |
| ERROR_TYPE_INVALID_ARG  | Invalid parameter |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_mem.a or libplat_mem.so

&emsp;&emsp;Header: ak_mem.h

<br/>

## Circular-Buffer Management

### **AK_BASE_MemRbInit**

&emsp;&emsp;【Description】

&emsp;&emsp;Initializes a circular buffer.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_MemRbInit(AK_S32 *ps32RbId, AK_S32 s32ModuleId, AK_U32 u32Size);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**               | **Value range** | **Input/Output** |
| ------------ | ---------------------- | ------------ | ------------- |
| ps32RbId | Allocated circular-buffer ID | - | Output |
| s32ModuleId | ID of the module allocating the circular buffer | - | Input |
| u32Size | Allocated circular-buffer size | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**             |
| ---------- | -------------------- |
| 0          | Success                 |
| Nonzero | Failure; returns an error code. |

&emsp;&emsp;【Error Code List】

| **Error code**                    | **Description** |
| ----------------------------- | -------- |
| ERROR_TYPE_INVALID_ARG        | Invalid parameter |
| ERROR_TYPE_NO_ENOUTH_RESOURCE | Insufficient resources |
| ERROR_TYPE_MALLOC_FAILED | Allocation failed |

> **Source note:** `ERROR_TYPE_NO_ENOUTH_RESOURCE` is a source typo; the supplied common header declares `ERROR_TYPE_NO_ENOUGH_RESOURCE`.

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_mem.a or libplat_mem.so

&emsp;&emsp;Header: ak_mem.h

<br/>

### **AK_BASE_MemRbDestroy**

&emsp;&emsp;【Description】

&emsp;&emsp;Frees a circular buffer.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_MemRbDestroy(AK_S32 s32RbId);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**              | **Value range** | **Input/Output** |
| ------------ | --------------------- | ------------ | ------------- |
| s32RbId | ID of the circular buffer to free | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**           |
| ---------- | ------------------ |
| 0          | Success               |
| Nonzero | Failure; returns an error code. |

&emsp;&emsp;【Error Code List】

| **Error code**             | **Description** |
| ---------------------- | -------- |
| ERROR_TYPE_INVALID_ARG | Invalid parameter |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_mem.a or libplat_mem.so

&emsp;&emsp;Header: ak_mem.h

<br/>

### **AK_BASE_MemRbReset**

&emsp;&emsp;【Description】

&emsp;&emsp;Resets a circular buffer.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_MemRbReset(AK_S32 s32RbId);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**              | **Value range** | **Input/Output** |
| ------------ | --------------------- | ------------ | ------------- |
| s32RbId | ID of the circular buffer to reset | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**           |
| ---------- | ------------------ |
| 0          | Success               |
| Nonzero | Failure; returns an error code. |

&emsp;&emsp;【Error Code List】

| **Error code**             | **Description** |
| ---------------------- | -------- |
| ERROR_TYPE_INVALID_ARG | Invalid parameter |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_mem.a or libplat_mem.so

&emsp;&emsp;Header: ak_mem.h

<br/>

### **AK_BASE_MemRbWrite**

&emsp;&emsp;【Description】

&emsp;&emsp;Writes data to a circular buffer.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_MemRbWrite(AK_S32 s32RbId, AK_U8 *pu8From, AK_S32 s32WriteLen);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**              | **Value range** | **Input/Output** |
| ------------ | --------------------- | ------------ | ------------- |
| s32RbId | ID of the circular buffer to write | - | Input |
| pu8From | Start address of the source buffer | - | Input |
| s32WriteLen | Length of the data to write | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**           |
| ---------- | ------------------ |
| 0          | Success               |
| Nonzero | Failure; returns an error code. |

&emsp;&emsp;【Error Code List】

| **Error code**               | **Description** |
| ------------------------ | -------- |
| ERROR_TYPE_NO_LEFT_SPACE | Insufficient space |
| ERROR_TYPE_INVALID_ARG   | Invalid parameter |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_mem.a or libplat_mem.so

&emsp;&emsp;Header: ak_mem.h

<br/>

### **AK_BASE_MemRbReadRequest**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets a read pointer from a circular buffer.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_MemRbReadRequest(AK_S32 s32RbId, AK_S32 *ps32ReadptrId);
```

&emsp;&emsp;【Parameters】

| **Parameter**  | **Description**                   | **Value range** | **Input/Output** |
| ------------- | -------------------------- | ------------ | ------------- |
| s32RbId | ID of the circular buffer to process | - | Input |
| ps32ReadptrId | Allocated circular-buffer read-pointer ID | - | Output |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**           |
| ---------- | ------------------ |
| 0          | Success               |
| Nonzero | Failure; returns an error code. |

&emsp;&emsp;【Error Code List】

| **Error code**                    | **Description** |
| ----------------------------- | -------- |
| ERROR_TYPE_NO_ENOUGH_RESOURCE | Insufficient resources |
| ERROR_TYPE_INVALID_ARG        | Invalid parameter |
| ERROR_TYPE_POINTER_NULL | Null pointer |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_mem.a or libplat_mem.so

&emsp;&emsp;Header: ak_mem.h

<br/>

### **AK_BASE_MemRbReadCancel**

&emsp;&emsp;【Description】

&emsp;&emsp;Marks a read pointer as unused.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_MemRbReadCancel(AK_S32 s32RbId, AK_S32 s32ReadptrId);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**              | **Value range** | **Input/Output** |
| ------------ | --------------------- | ------------ | ------------- |
| s32RbId | ID of the circular buffer to process | - | Input |
| s32ReadptrId | Read-pointer index | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**           |
| ---------- | ------------------ |
| 0          | Success               |
| Nonzero | Failure; returns an error code. |

&emsp;&emsp;【Error Code List】

| **Error code**             | **Description** |
| ---------------------- | -------- |
| ERROR_TYPE_INVALID_ARG | Invalid parameter |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_mem.a or libplat_mem.so

&emsp;&emsp;Header: ak_mem.h

<br/>

### **AK_BASE_MemRbRead**

&emsp;&emsp;【Description】

&emsp;&emsp;Reads data from a circular buffer.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_MemRbRead(AK_S32 s32RbId, AK_S32 s32ReadptrId, AK_U8 *pu8To, \
    AK_S32 s32ReadLen, AK_S32 *ps32Result);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**              | **Value range** | **Input/Output** |
| ------------ | --------------------- | ------------ | ------------- |
| s32RbId | ID of the circular buffer to read | - | Input |
| s32ReadptrId | Read-pointer index | - | Input |
| pu8To | Start address of the output buffer | - | Output |
| s32ReadLen | Length of data to read | - | Input |
| ps32Result | Length of data successfully read | - | Output |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**           |
| ---------- | ------------------ |
| 0          | Success               |
| Nonzero | Failure; returns an error code. |

&emsp;&emsp;【Error Code List】

| **Error code**             | **Description** |
| ---------------------- | -------- |
| ERROR_TYPE_INVALID_ARG | Invalid parameter |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_mem.a or libplat_mem.so

&emsp;&emsp;Header: ak_mem.h

<br/>

### **AK_BASE_MemRbGetDataSize**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the amount of data in a circular buffer.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_MemRbGetDataSize(AK_S32 s32RbId, AK_S32 *ps32Size);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**              | **Value range** | **Input/Output** |
| ------------ | --------------------- | ------------ | ------------- |
| s32RbId | ID of the circular buffer to query | - | Input |
| ps32Size | Amount of data in the circular buffer | - | Output |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**         |
| ---------- | ---------------- |
| 0          | Success             |
| Nonzero | Failure; returns an error code. |

&emsp;&emsp;【Error Code List】

| **Error code**             | **Description** |
| ---------------------- | -------- |
| ERROR_TYPE_INVALID_ARG | Invalid parameter |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_mem.a or libplat_mem.so

&emsp;&emsp;Header: ak_mem.h

<br/>

## DMA Memory Operations

### **AK_BASE_MemDmaAlloc**

&emsp;&emsp;【Description】

&emsp;&emsp;Allocates a block of DMA memory.

&emsp;&emsp;【Syntax】

```C
    AK_VOID * AK_BASE_MemDmaAlloc(AK_S32 s32ModuleId, AK_U32 u32Size);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**            | **Value range** | **Input/Output** |
| ------------ | ------------------- | ------------ | ------------- |
| s32ModuleId | ID of the module allocating DMA memory | - | Input |
| u32Size | Size of the block to allocate | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**                                           |
| ---------- | -------------------------------------------------- |
| AK_VOID | Start address of the allocated block on success; NULL on failure. |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------- | -------- |
| -          | -        |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_mem.a or libplat_mem.so

&emsp;&emsp;Header: ak_mem.h

<br/>

### **AK_BASE_MemDmaFree**

&emsp;&emsp;【Description】

&emsp;&emsp;Frees DMA memory.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_MemDmaFree(AK_VOID *pvPtr);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**              | **Value range** | **Input/Output** |
| ------------ | --------------------- | ------------ | ------------- |
| pvPtr | Start address of the DMA memory to free | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**           |
| ---------- | ------------------ |
| 0          | Success               |
| Nonzero | Failure; returns an error code. |

&emsp;&emsp;【Error Code List】

| **Error code**             | **Description** |
| ---------------------- | -------- |
| ERROR_TYPE_INVALID_ARG | Invalid parameter |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_mem.a or libplat_mem.so

&emsp;&emsp;Header: ak_mem.h

<br/>

### **AK_BASE_MemDmaVaddr2Paddr**

&emsp;&emsp;【Description】

&emsp;&emsp;Converts a virtual address to a physical address.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_MemDmaVaddr2Paddr(AK_VOID *pvPtr, AK_U64 *pu64Paddr);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**           | **Value range** | **Input/Output** |
| ------------ | ------------------ | ------------ | ------------- |
| pvPtr | Virtual address to convert | - | Input |
| pu64Paddr | Output physical-memory address | - | Output |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**           |
| ---------- | ------------------ |
| 0          | Success               |
| Nonzero | Failure; returns an error code. |

&emsp;&emsp;【Error Code List】

| **Error code**              | **Description** |
| ----------------------- | -------- |
| ERROR_TYPE_POINTER_NULL | Null pointer |
| ERROR_TYPE_INVALID_ARG  | Invalid parameter |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_mem.a or libplat_mem.so

&emsp;&emsp;Header: ak_mem.h

<br/>

### **AK_BASE_MemDmaPoolCreate**

&emsp;&emsp;【Description】

&emsp;&emsp;Creates a DMA memory pool.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_MemDmaPoolCreate(MODULE_ID_E enMid, AK_U32 u32Size);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**              | **Value range** | **Input/Output** |
| ------------ | --------------------- | ------------ | ------------- |
| enMid | ID of the module allocating the DMA memory pool | - | Input |
| u32Size | DMA memory-pool size | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**        |
| ---------- | --------------- |
| AK_S32 | 0 on success; -1 on failure. |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------- | -------- |
| -          | -        |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_mem.a or libplat_mem.so

&emsp;&emsp;Header: ak_mem.h

<br/>

### **AK_BASE_MemDmaPoolActivate**

&emsp;&emsp;【Description】

&emsp;&emsp;Initializes a DMA memory pool.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_MemDmaPoolActivate(AK_VOID);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------ | -------- | ------------ | ------------- |
| -            | -        | -            | -             |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**        |
| ---------- | --------------- |
| AK_S32 | 0 on success; -1 on failure. |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_mem.a or libplat_mem.so

&emsp;&emsp;Header: ak_mem.h

<br/>

### **AK_BASE_MemDmaPoolExit**

&emsp;&emsp;【Description】

&emsp;&emsp;Exits a DMA memory pool.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_MemDmaPoolExit(AK_VOID);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------ | -------- | ------------ | ------------- |
| -            | -        | -            | -             |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**         |
| ---------- | ---------------- |
| int | 0; always succeeds. |
&emsp;&emsp;【Error Code List】

| **Error code** | **Description**        |
| ------------ | -------- |
| -                        | -               |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_mem.a or libplat_mem.so

&emsp;&emsp;Header: ak_mem.h

<br/>

### **AK_BASE_MemDmaPoolGetUsedMem**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets information about the used size of a DMA memory pool.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_MemDmaPoolGetUsedMem(MODULE_ID_E enMid, AK_U64 *pu64Total);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**              | **Value range** | **Input/Output** |
| ------------ | --------------------- | ------------ | ------------- |
| enMid | ID of the module allocating the DMA memory pool | - | Input |
| pu64Total | Total amount used in the DMA memory pool | - | Output |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**        |
| ---------- | --------------- |
| AK_S32 | 0 on success; -1 on failure. |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------- | -------- |
| -          | -        |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_mem.a or libplat_mem.so

&emsp;&emsp;Header: ak_mem.h

<br/>

### **AK_BASE_MemDmaPoolGetFreeMem**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets information about the free size of a DMA memory pool.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_MemDmaPoolGetFreeMem(MODULE_ID_E enMid, AK_U64 *pu64Total);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**              | **Value range** | **Input/Output** |
| ------------ | --------------------- | ------------ | ------------- |
| enMid | ID of the module allocating the DMA memory pool | - | Input |
| pu64Total | Total amount free in the DMA memory pool | - | Output |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**        |
| ---------- | --------------- |
| AK_S32 | 0 on success; -1 on failure. |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_mem.a or libplat_mem.so

&emsp;&emsp;Header: ak_mem.h

<br/>

### **AK_BASE_MemDmaPoolSetThreshold**

&emsp;&emsp;【Description】

&emsp;&emsp;Sets the DMA memory-pool allocation threshold.

&emsp;&emsp;When ak_mem_dma_alloc\_ is greater than the threshold, memory is allocated from the module's DMA memory pool; otherwise, it is allocated from the remaining DMA memory.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_MemDmaPoolSetThreshold(MODULE_ID_E enMid, AK_U64 u64Threshold);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**              | **Value range** | **Input/Output** |
| ------------ | --------------------- | ------------ | ------------- |
| enMid | ID of the module allocating the DMA memory pool | - | Input |
| u64Threshold | DMA memory-pool allocation threshold | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**        |
| ---------- | --------------- |
| AK_S32 | 0 on success; -1 on failure. |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_mem.a or libplat_mem.so

&emsp;&emsp;Header: ak_mem.h

<br/>

### **AK_BASE_MemDmaPoolCreateReservedObj**

&emsp;&emsp;【Description】

&emsp;&emsp;Creates specific reserved memory in a DMA memory pool.

&emsp;&emsp;When ak_mem_dma_alloc\_ is greater than the threshold, memory is allocated from the specific reserved memory in this DMA memory pool; otherwise, ordinary memory is allocated from the module's DMA memory pool.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_MemDmaPoolCreateReservedObj(MODULE_ID_E enMid, \
    AK_U64 u64Size, AK_U64 u64AllocThreshold);
```

&emsp;&emsp;【Parameters】

| **Parameter**      | **Description**              | **Value range** | **Input/Output** |
| ----------------- | --------------------- | ------------ | ------------- |
| enMid | ID of the module allocating the DMA memory pool | - | Input |
| u64Size | Reserved-memory size | - | Input |
| u64AllocThreshold | Reserved-memory allocation threshold | | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**        |
| ---------- | --------------- |
| AK_S32 | 0 on success; -1 on failure. |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_mem.a or libplat_mem.so

&emsp;&emsp;Header: ak_mem.h

<br/>

## Getting Version Information

### **AK_BASE_MemGetVersion**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets memory-management module version information.

&emsp;&emsp;【Syntax】

```C
    const AK_CHAR* AK_BASE_MemGetVersion(AK_VOID);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------ | -------- | ------------ | ------------- |
| AK_VOID      | -        | -            | -             |

&emsp;&emsp;【Return Value】

| **Return value**      | **Description**                     |
| --------------- | ---------------------------- |
| const AK_CHAR * | Memory-management library version information. |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_mem.a or libplat_mem.so

&emsp;&emsp;Header: ak_mem.h

<br/>

## Memory-Usage Queries

### **AK_BASE_MemGetUsedDetail**

&emsp;&emsp;【Description】

&emsp;&emsp;Queries details of allocated memory blocks.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_MemGetUsedDetail(AK_S32 s32ModuleId, USED_MEM_INFO_S **ppstMemUsed);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**                   | **Value range**                  | **Input/Output** |
| ------------ | -------------------------- | ----------------------------- | ------------- |
| s32ModuleId | ID of the module whose memory usage is queried | See enum module_id | Input |
| ppstMemUsed | Output structure containing allocation information | See s_used_mem_info; initially null | Output |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**         |
| ---------- | ---------------- |
| 0          | Success             |
| Nonzero | Failure; returns an error code. |

&emsp;&emsp;【Error Code List】

| **Error code**                  | **Description**                             |
| --------------------------- | ------------------------------------ |
| ERROR_TYPE_FUNC_NOT_SUPPORT | Function not supported because memory tracing is disabled |
| ERROR_TYPE_INVALID_ARG      | Invalid parameter                             |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_mem.a or libplat_mem.so

&emsp;&emsp;Header: ak_mem.h

&emsp;&emsp;【Call Sequence】

```c
    AK_BASE_MemGetUsedDetail(s32ModuleId, &pstMemUsed);
    AK_BASE_MemReleaseUsedDetail(pstMemUsed);
```

&emsp;&emsp;【Paired Interface】

```c
    AK_S32 AK_BASE_MemReleaseUsedDetail(USED_MEM_INFO_S *pstMemUsed);
```

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

<br/>

### **AK_BASE_MemReleaseUsedDetail**

&emsp;&emsp;【Description】

&emsp;&emsp;Frees the linked list used to record memory-block usage details.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_MemReleaseUsedDetail(USED_MEM_INFO_S *pstMemUsed);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**                 | **Value range** | **Input/Output** |
| ------------ | ------------------------ | ------------ | ------------- |
| pstMemUsed | Linked list of memory details to free | Non-null | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**           |
| ---------- | ------------------ |
| 0          | Success.             |
| Nonzero | Failure; returns an error code. |

&emsp;&emsp;【Error Code List】

| **Error code**              | **Description** |
| ----------------------- | -------- |
| ERROR_TYPE_POINTER_NULL | Null parameter |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_mem.a or libplat_mem.so

&emsp;&emsp;Header: ak_mem.h

&emsp;&emsp;【Call Sequence】

```c
    AK_BASE_MemGetUsedDetail(s32ModuleId, &pstMemUsed);
    AK_BASE_MemReleaseUsedDetail(pstMemUsed);
```

&emsp;&emsp;【Paired Interface】

```c
    AK_S32 AK_BASE_MemGetUsedDetail(AK_S32 s32ModuleId, USED_MEM_INFO_S **ppstMemUsed);
```

&emsp;&emsp;【Reentrancy】

&emsp;&emsp;The function is reentrant.

> **Note:** After querying memory-block usage details with ak_mem_get_used_detai, call this interface (ak_mem_release_used_detail) to free the linked list that records those details; otherwise, a memory leak may occur.

<br/>

### **AK_BASE_MemGetUsedTotal**

&emsp;&emsp;【Description】

&emsp;&emsp;Queries the total memory allocated by a module, in bytes.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_MemGetUsedTotal(AK_S32 s32ModuleId, AK_U64 *pu64TotalUsed);
```

&emsp;&emsp;【Parameters】

| **Parameter**  | **Description**                         | **Value range** | **Input/Output** |
| ------------- | -------------------------------- | ------------ | ------------- |
| s32ModuleId | ID of the module whose memory usage is queried | - | Input |
| pu64TotalUsed | Query result: total memory used, in bytes | - | Output |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**           |
| ---------- | ------------------ |
| 0          | Success               |
| Nonzero | Failure; returns an error code. |

&emsp;&emsp;【Error Code List】

| **Error code**                  | **Description**                             |
| --------------------------- | ------------------------------------ |
| ERROR_TYPE_FUNC_NOT_SUPPORT | Function not supported because memory tracing is disabled |
| ERROR_TYPE_INVALID_ARG      | Invalid parameter                             |
| ERROR_TYPE_POINTER_NULL     | Null parameter                             |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_mem.a or libplat_mem.so

&emsp;&emsp;Header: ak_mem.h

<br/>

### **AK_BASE_MemDmaGetUsed**

&emsp;&emsp;【Description】

&emsp;&emsp;Queries the total DMA memory allocated by a module, in bytes.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_MemDmaGetUsed(AK_S32 s32ModuleId, AK_U64 *pu64TotalUsed);
```

&emsp;&emsp;【Parameters】

| **Parameter**  | **Description**                            | **Value range** | **Input/Output** |
| ------------- | ----------------------------------- | ------------ | ------------- |
| s32ModuleId | ID of the module whose DMA-memory usage is queried | - | Input |
| pu64TotalUsed | Query result: total DMA memory used, in bytes | - | Output |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**           |
| ---------- | ------------------ |
| 0          | Success               |
| Nonzero | Failure; returns an error code. |

&emsp;&emsp;【Error Code List】

| **Error code**                  | **Description**                           |
| --------------------------- | ---------------------------------- |
| ERROR_TYPE_FUNC_NOT_SUPPORT | Function not supported because memory tracing is disabled |
| ERROR_TYPE_INVALID_ARG      | Invalid parameter                           |
| ERROR_TYPE_POINTER_NULL     | Null parameter                           |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_mem.a or libplat_mem.so

&emsp;&emsp;Header: ak_mem.h

<br/>

### **AK_BASE_MemDmaGetReservedSize**

&emsp;&emsp;【Description】

&emsp;&emsp;Queries the system reserved-memory size, in bytes.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_MemDmaGetReservedSize(AK_U64 *pu64Size);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**                         | **Value range** | **Input/Output** |
| ------------ | -------------------------------- | ------------ | ------------- |
| pu64Size | Query result: total reserved memory, in bytes | - | Output |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------- | -------- |
| 0          | Success     |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_mem.a or libplat_mem.so

&emsp;&emsp;Header: ak_mem.h

<br/>

### **AK_BASE_MemGetTotalSize**

&emsp;&emsp;【Description】

&emsp;&emsp;Queries the total system-memory size, in bytes.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_MemGetTotalSize(AK_U64 *pu64Size);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**                           | **Value range** | **Input/Output** |
| ------------ | ---------------------------------- | ------------ | ------------- |
| pu64Size | Query result: total system-memory size, in bytes | - | Output |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------- | -------- |
| 0          | Success     |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_mem.a or libplat_mem.so

&emsp;&emsp;Header: ak_mem.h

<br/>

### /var/platform Description

The /var/platform directory exposes the current module configuration parameters and status. Its parameters are described below.

#### stat

| Parameter | Description |
| ------- | ----------- |
| Version | MEM library version |
