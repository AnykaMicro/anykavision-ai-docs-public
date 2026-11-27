# Multithreading

## Overview

&emsp;&emsp;The Thread module wraps the underlying thread-operation functions and thread-communication mechanisms. It provides a unified upper-layer interface to simplify later software porting.

<br/>

## API Reference

&emsp;&emsp;This module provides the APIs listed below:

| **Library interface** | **Description** |
| ------------------------------- | ------------------------------------------------------------ |
| AK_BASE_ThreadGetVersion | Gets thread-module version information. |
| AK_BASE_ThreadCreate | Creates a thread. |
| AK_BASE_ThreadJoin | Waits for a thread to finish. |
| AK_BASE_ThreadDetach | Detaches a thread. |
| AK_BASE_ThreadDetach | Cancels thread execution. |
| AK_BASE_ThreadExit | Terminates thread execution. |
| AK_BASE_ThreadGetTid | Gets the thread ID. |
| AK_BASE_ThreadSetName | Sets the thread name. |
| AK_BASE_ThreadMutexInit | Initializes a mutex. |
| AK_BASE_ThreadMutexLock | Acquires a mutex. |
| AK_BASE_ThreadMutexUnlock | Releases a mutex. |
| AK_BASE_ThreadMutexDestroy | Destroys a mutex. |
| AK_BASE_ThreadMutexattrInit | Initializes a mutex-attribute variable. |
| AK_BASE_ThreadMutexattrDestroy | Destroys a mutex-attribute variable. |
| AK_BASE_ThreadMutexattrSettype | Sets the value of a mutex-attribute variable. |
| AK_BASE_ThreadMutexattrGettype | Gets the value of a mutex-attribute variable. |
| AK_BASE_ThreadSemInit | Initializes a semaphore. |
| AK_BASE_ThreadSemPost | Increments a semaphore by 1. |
| AK_BASE_ThreadSemWait | Decrements a semaphore by 1 when it is greater than 0; blocks when it is 0. |
| AK_BASE_ThreadSemDestroy | Destroys a semaphore. |
| AK_BASE_ThreadSemTrywait | Tries to acquire a semaphore: if it is greater than 0, decrements it by 1 and returns 0; if it is 0, returns -1. |
| AK_BASE_ThreadSemTimeWait | Acquires a semaphore, blocking until it is available or the timeout expires. |
| AK_BASE_ThreadCondInit | Initializes a condition variable. |
| AK_BASE_ThreadCondDestroy | Destroys a condition variable. |
| AK_BASE_ThreadCondWait | Waits for a condition variable, blocking until its condition is satisfied. |
| AK_Base_ThreadCondTimewait | Waits for a condition variable until its condition is satisfied or the timeout expires. |
| AK_BASE_ThreadCondSignal | Signals that a condition variable's condition is satisfied. |
| AK_BASE_ThreadCondBroadcast | Broadcasts that a condition variable's condition is satisfied. |
| AK_BASE_ThreadRWlockInit | Initializes a read-write lock. |
| AK_BASE_ThreadRWlockDestroy | Destroys a read-write lock. |
| AK_BASE_ThreadRWlockRDlock | Acquires a read lock. |
| AK_BASE_ThreadRWlockWRlock | Acquires a write lock. |
| AK_BASE_ThreadRWlockTryRDlock | Tries to acquire a read lock. |
| AK_BASE_ThreadRWlockTryWRlock | Tries to acquire a write lock. |
| AK_BASE_ThreadRWlockUnlock | Releases a read-write lock. |
| AK_BASE_ThreadRWlockattrInit | Initializes read-write-lock attributes. |
| AK_BASE_ThreadRWlockattrDestroy | Destroys read-write-lock attributes. |
| AK_BASE_ThreadRWlockattrGetPshared | Gets the process-shared attribute. |
| AK_BASE_ThreadRWlockattrSetPshared | Sets the process-shared attribute. |

> **Source note:** The second `AK_BASE_ThreadDetach` row in the source describes thread cancellation. The declared cancellation API is `AK_BASE_ThreadCancel`.

<br/>

## Getting Version Information

### **AK_BASE_ThreadGetVersion**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets thread-module version information.

&emsp;&emsp;【Syntax】

```C
    const AK_CHAR* AK_BASE_ThreadGetVersion(AK_VOID);
```

&emsp;&emsp;【Return Value】

| **Return value** | **Description**         |
| ---------------- | ---------------------- |
| const AK_CHAR* | Thread-module version information. |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_thread.a

&emsp;&emsp;Header: ak_thread.h

<br/>

## Thread Control

### **AK_BASE_ThreadCreate**

&emsp;&emsp;【Description】

&emsp;&emsp;Creates a thread.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_ThreadCreate(AK_PTHREAD_T *ptId, pfnBASE_ThreadFunc func, AK_VOID *pvArg, AK_S32 s32StackSize, AK_S32 s32Priority);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| ptId | Thread ID | - | Output |
| func | Thread entry address | - | Input |
| pvArg | Argument passed to the thread | - | Input |
| s32StackSize | Thread stack size | - | Input |
| s32Priority | Thread priority | If s32Priority is -1, the scheduling policy is SCHED_OTHER and the thread is non-real-time. If s32Priority is in [1, 99], the policy is SCHED_RR round-robin real-time scheduling; a larger s32Priority value has higher priority. | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0                | Success           |
| -1               | Failure           |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_thread.a

&emsp;&emsp;Header: ak_thread.h

<br/>

### **AK_BASE_ThreadJoin**

&emsp;&emsp;【Description】

&emsp;&emsp;Waits for a thread to finish.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_ThreadJoin(AK_PTHREAD_T tId);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| tId | Thread ID | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0                | Success           |
| Nonzero | Failure |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_thread.a

&emsp;&emsp;Header: ak_thread.h

<br/>

### **AK_BASE_ThreadDetach**

&emsp;&emsp;【Description】

&emsp;&emsp;Detaches a thread.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_ThreadDetach(AK_PTHREAD_T tId);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| tId | Thread ID | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0                | Success           |
| Nonzero | Failure |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_thread.a

&emsp;&emsp;Header: ak_thread.h

<br/>

### **AK_BASE_ThreadCancel**

&emsp;&emsp;【Description】

&emsp;&emsp;Cancels thread execution.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_ThreadCancel(AK_PTHREAD_T tId);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| tId | Thread ID | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0                | Success           |
| Nonzero | Failure |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_thread.a

&emsp;&emsp;Header: ak_thread.h

<br/>

### **AK_BASE_ThreadExit**

&emsp;&emsp;【Description】

&emsp;&emsp;Terminates thread execution.

&emsp;&emsp;【Syntax】

```C
    AK_VOID AK_BASE_ThreadExit(AK_VOID);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| -                | -         | -                  | -                                    |

&emsp;&emsp;【Return Value】

None.

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_thread.a

&emsp;&emsp;Header: ak_thread.h

<br/>

### **AK_BASE_ThreadGetTid**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the thread ID.

&emsp;&emsp;【Syntax】

```C
    AK_S64 AK_BASE_ThreadGetTid(AK_VOID);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| AK_VOID        | -              | -                  | -                                       |

&emsp;&emsp;【Return Value】

| **Return value** | **Description**       |
| ---------------- | -------------------- |
| AK_S64 | ID of the thread that called the function |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_thread.a

&emsp;&emsp;Header: ak_thread.h

<br/>

### **AK_BASE_ThreadSetName**

&emsp;&emsp;【Description】

&emsp;&emsp;Sets the thread name.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_ThreadSetName(const AK_CHAR *pcName);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| pcName | Thread name | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0                | Success           |
| -1               | Failure           |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_thread.a

&emsp;&emsp;Header: ak_thread.h

<br/>

## Mutexes

### **AK_BASE_ThreadMutexInit**

&emsp;&emsp;【Description】

&emsp;&emsp;Initializes a mutex.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_ThreadMutexInit(AK_MUTEX_T *ptMutex, AK_MUTEXATTR_T *ptAttr);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| ptMutex | Mutex to initialize | - | Output |
| ptAttr | Mutex attributes | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0                | Success           |
| Nonzero | Failure |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_thread.a

&emsp;&emsp;Header: ak_thread.h

<br/>

### **AK_BASE_ThreadMutexLock**

&emsp;&emsp;【Description】

&emsp;&emsp;Acquires a mutex.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_ThreadMutexLock(AK_MUTEX_T *ptMutex);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| ptMutex | Mutex to operate on | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0                | Success           |
| Nonzero | Failure |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_thread.a

&emsp;&emsp;Header: ak_thread.h

<br/>

### **AK_BASE_ThreadMutexUnlock**

&emsp;&emsp;【Description】

&emsp;&emsp;Releases a mutex.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_ThreadMutexUnlock(AK_MUTEX_T *ptMutex);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| ptMutex | Mutex to operate on | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0                | Success           |
| Nonzero | Failure |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_thread.a

&emsp;&emsp;Header: ak_thread.h

<br/>

### **AK_BASE_ThreadMutexDestroy**

&emsp;&emsp;【Description】

&emsp;&emsp;Destroys a mutex.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_ThreadMutexDestroy(AK_MUTEX_T *ptMutex);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| ptMutex | Mutex to operate on | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0                | Success           |
| Nonzero | Failure |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_thread.a

&emsp;&emsp;Header: ak_thread.h

<br/>

### **AK_BASE_ThreadMutexattrInit**

&emsp;&emsp;【Description】

&emsp;&emsp;Initializes a mutex-attribute variable.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_ThreadMutexattrInit(AK_MUTEXATTR_T *ptAttr);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**     | **Value range** | **Input/Output** |
| ------------------ | ------------------ | ------------------ | --------------------------------------- |
| ptAttr | Pointer to the mutex-attribute variable | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0                | Success           |
| Nonzero | Failure |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_thread.a

&emsp;&emsp;Header: ak_thread.h

<br/>

### **AK_BASE_ThreadMutexattrDestroy**

&emsp;&emsp;【Description】

&emsp;&emsp;Destroys a mutex-attribute variable.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_ThreadMutexattrDestroy(AK_MUTEXATTR_T *ptAttr);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**     | **Value range** | **Input/Output** |
| ------------------ | ------------------ | ------------------ | --------------------------------------- |
| ptAttr | Pointer to the mutex-attribute variable | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0                | Success           |
| Nonzero | Failure |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_thread.a

&emsp;&emsp;Header: ak_thread.h

<br/>

### **AK_BASE_ThreadMutexattrSettype**

&emsp;&emsp;【Description】

&emsp;&emsp;Sets the value of a mutex-attribute variable.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_ThreadMutexattrSettype(AK_MUTEXATTR_T *ptAttr, AK_S32 s32Kind);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**         | **Value range** | **Input/Output** |
| ------------------ | ---------------------- | ------------------ | --------------------------------------- |
| ptAttr | Pointer to the mutex-attribute variable to operate on | - | Input |
| s32Kind | Mutex type | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0                | Success           |
| Nonzero | Failure |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_thread.a

&emsp;&emsp;Header: ak_thread.h

<br/>

### **AK_BASE_ThreadMutexattrGettype**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the value of a mutex-attribute variable.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_ThreadMutexattrGettype(const AK_MUTEXATTR_T *ptAttr, AK_S32 *ps32Kind);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**         | **Value range** | **Input/Output** |
| ------------------ | ---------------------- | ------------------ | --------------------------------------- |
| ptAttr | Pointer to the mutex-attribute variable to operate on | - | Input |
| ps32Kind | Value obtained from the mutex-attribute variable | - | Output |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0                | Success           |
| Nonzero | Failure |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_thread.a

&emsp;&emsp;Header: ak_thread.h

<br/>

## Semaphores

### **AK_BASE_ThreadSemInit**

&emsp;&emsp;【Description】

&emsp;&emsp;Initializes a semaphore.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_ThreadSemInit(AK_SEM_T *ptSem, AK_U32 u32Value);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| ptSem | Semaphore to operate on | - | Output |
| u32Value | Initial semaphore value | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0                | Success           |
| -1               | Failure           |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_thread.a

&emsp;&emsp;Header: ak_thread.h

<br/>

### **AK_BASE_ThreadSemPost**

&emsp;&emsp;【Description】

&emsp;&emsp;Increments a semaphore by 1.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_ThreadSemPost(AK_SEM_T *ptSem);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| ptSem | Semaphore to operate on | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0                | Success           |
| -1               | Failure           |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_thread.a

&emsp;&emsp;Header: ak_thread.h

<br/>

### **AK_BASE_ThreadSemWait**

&emsp;&emsp;【Description】

&emsp;&emsp;When the semaphore is greater than 0, decrements it by 1; when it is 0, blocks.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_ThreadSemWait(AK_SEM_T *ptSem);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| ptSem | Semaphore to operate on | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0                | Success           |
| -1               | Failure           |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_thread.a

&emsp;&emsp;Header: ak_thread.h

<br/>

### **AK_BASE_ThreadSemDestroy**

&emsp;&emsp;【Description】

&emsp;&emsp;Destroys a semaphore.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_ThreadSemDestroy(AK_SEM_T *ptSem);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| ptSem | Semaphore to destroy | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0                | Success           |
| -1               | Failure           |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_thread.a

&emsp;&emsp;Header: ak_thread.h

<br/>

### **AK_BASE_ThreadSemTrywait**

&emsp;&emsp;【Description】

&emsp;&emsp;Tries to acquire a semaphore. If it is greater than 0, decrements it by 1 and returns 0; if it is 0, returns -1.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_ThreadSemTrywait(AK_SEM_T *ptSem);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| ptSem | Semaphore to operate on | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0                | Success           |
| -1               | Failure           |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_thread.a

&emsp;&emsp;Header: ak_thread.h

<br/>

### **AK_BASE_ThreadSemTimeWait**

&emsp;&emsp;【Description】

&emsp;&emsp;Acquires a semaphore, blocking until it is available or the timeout expires.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_ThreadSemTimeWait(AK_SEM_T *ptSem, const struct timespec *abs_timeout);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| ptSem | Semaphore to operate on | - | Input |
| abs_timeout | Timeout | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0                | Success           |
| -1               | Failure           |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_thread.a

&emsp;&emsp;Header: ak_thread.h

<br/>

## Condition Variables

### **AK_BASE_ThreadCondInit**

&emsp;&emsp;【Description】

&emsp;&emsp;Initializes a condition variable.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_ThreadCondInit(AK_COND_T *ptCond);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| ptCond | Pointer to the condition variable | - | Output |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0                | Success           |
| Nonzero | Failure |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_thread.a

&emsp;&emsp;Header: ak_thread.h

<br/>

### **AK_BASE_ThreadCondDestroy**

&emsp;&emsp;【Description】

&emsp;&emsp;Destroys a condition variable.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_ThreadCondDestroy(AK_COND_T *ptCond);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| ptCond | Pointer to the condition variable | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0                | Success           |
| Nonzero | Failure |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_thread.a

&emsp;&emsp;Header: ak_thread.h

<br/>

### **AK_BASE_ThreadCondWait**

&emsp;&emsp;【Description】

&emsp;&emsp;Waits for a condition variable, blocking until its condition is satisfied.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_ThreadCondWait(AK_COND_T *ptCond, AK_MUTEX_T *ptMutex);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**             | **Value range** | **Input/Output** |
| ------------------ | -------------------------- | ------------------ | --------------------------------------- |
| ptCond | Pointer to the condition variable | - | Input |
| ptMutex | Pointer to the mutex associated with the condition variable | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0                | Success           |
| Nonzero | Failure |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_thread.a

&emsp;&emsp;Header: ak_thread.h

<br/>

### **AK_Base_ThreadCondTimewait**

&emsp;&emsp;【Description】

&emsp;&emsp;Waits for a condition variable until its condition is satisfied or the timeout expires.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_Base_ThreadCondTimewait(AK_COND_T *ptCond,
        AK_MUTEX_T *ptMutex, const struct timespec *abstime);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**             | **Value range** | **Input/Output** |
| ------------------ | -------------------------- | ------------------ | --------------------------------------- |
| ptCond | Pointer to the condition variable | - | Input |
| ptMutex | Pointer to the mutex associated with the condition variable | - | Input |
| abstime | Timeout | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0                | Success           |
| Nonzero | Failure |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_thread.a

&emsp;&emsp;Header: ak_thread.h

<br/>

### **AK_BASE_ThreadCondSignal**

&emsp;&emsp;【Description】

&emsp;&emsp;Signals that a condition variable's condition is satisfied.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_ThreadCondSignal(AK_COND_T *ptCond);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| ptCond | Pointer to the condition variable | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0                | Success           |
| Nonzero | Failure |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_thread.a

&emsp;&emsp;Header: ak_thread.h

<br/>

### **AK_BASE_ThreadCondBroadcast**

&emsp;&emsp;【Description】

&emsp;&emsp;Broadcasts that a condition variable's condition is satisfied.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_ThreadCondBroadcast(AK_COND_T *ptCond);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| ptCond | Pointer to the condition variable | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0                | Success           |
| Nonzero | Failure |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_thread.a

&emsp;&emsp;Header: ak_thread.h

<br/>

## Read-Write Locks

### **AK_BASE_ThreadRWlockInit**

&emsp;&emsp;【Description】

&emsp;&emsp;Initializes a read-write lock.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_ThreadRWlockInit(AK_RWLOCK_T *ptRWlock, AK_RWLOCKATTR_T *ptRWlockattr);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**   | **Value range** | **Input/Output** |
| ------------------ | ---------------- | ------------------ | --------------------------------------- |
| ptRWlock | Read-write lock to initialize | - | Input |
| ptRWlockattr | Read-write-lock attributes | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0                | Success           |
| Nonzero | Failure |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_thread.a

&emsp;&emsp;Header: ak_thread.h

<br/>

### **AK_BASE_ThreadRWlockDestroy**

&emsp;&emsp;【Description】

&emsp;&emsp;Destroys a read-write lock.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_ThreadRWlockDestroy(AK_RWLOCK_T *ptRWlock);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| ptRWlock | Read-write lock to operate on | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0                | Success           |
| Nonzero | Failure |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_thread.a

&emsp;&emsp;Header: ak_thread.h

<br/>

### **AK_BASE_ThreadRWlockRDlock**

&emsp;&emsp;【Description】

&emsp;&emsp;Acquires a read lock.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_ThreadRWlockRDlock(AK_RWLOCK_T *ptRWlock);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| ptRWlock | Read-write lock to operate on | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0                | Success           |
| Nonzero | Failure |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_thread.a

&emsp;&emsp;Header: ak_thread.h

<br/>

### **AK_BASE_ThreadRWlockWRlock**

&emsp;&emsp;【Description】

&emsp;&emsp;Acquires a write lock.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_ThreadRWlockWRlock(AK_RWLOCK_T *ptRWlock);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| ptRWlock | Read-write lock to operate on | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0                | Success           |
| Nonzero | Failure |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_thread.a

&emsp;&emsp;Header: ak_thread.h

<br/>

### **AK_BASE_ThreadRWlockTryRDlock**

&emsp;&emsp;【Description】

&emsp;&emsp;Tries to acquire a read lock.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_ThreadRWlockTryRDlock(AK_RWLOCK_T *ptRWlock);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| ptRWlock | Read-write lock to operate on | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0                | Success           |
| Nonzero | Failure |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_thread.a

&emsp;&emsp;Header: ak_thread.h

<br/>

### **AK_BASE_ThreadRWlockTryWRlock**

&emsp;&emsp;【Description】

&emsp;&emsp;Tries to acquire a write lock.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_ThreadRWlockTryWRlock(AK_RWLOCK_T *ptRWlock);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| ptRWlock | Read-write lock to operate on | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0                | Success           |
| Nonzero | Failure |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_thread.a

&emsp;&emsp;Header: ak_thread.h

<br/>

### **AK_BASE_ThreadRWlockUnlock**

&emsp;&emsp;【Description】

&emsp;&emsp;Releases a read-write lock.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_ThreadRWlockUnlock(AK_RWLOCK_T *ptRWlock);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description** | **Value range** | **Input/Output** |
| ------------------ | -------------- | ------------------ | --------------------------------------- |
| ptRWlock | Read-write lock to operate on | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0                | Success           |
| Nonzero | Failure |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_thread.a

&emsp;&emsp;Header: ak_thread.h

<br/>

### **AK_BASE_ThreadRWlockattrInit**

&emsp;&emsp;【Description】

&emsp;&emsp;Initializes read-write-lock attributes.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_ThreadRWlockattrInit(AK_RWLOCKATTR_T * ptRWlockattr);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**     | **Value range** | **Input/Output** |
| ------------------ | ------------------ | ------------------ | --------------------------------------- |
| ptRWlockattr | Read-write-lock attributes to operate on | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0                | Success           |
| Nonzero | Failure |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_thread.a

&emsp;&emsp;Header: ak_thread.h

<br/>

### **AK_BASE_ThreadRWlockattrDestroy**

&emsp;&emsp;【Description】

&emsp;&emsp;Destroys read-write-lock attributes.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_ThreadRWlockattrDestroy(AK_RWLOCKATTR_T * ptRWlockattr);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**     | **Value range** | **Input/Output** |
| ------------------ | ------------------ | ------------------ | --------------------------------------- |
| ptRWlockattr | Read-write-lock attributes to operate on | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0                | Success           |
| Nonzero | Failure |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_thread.a

&emsp;&emsp;Header: ak_thread.h

<br/>

### **AK_BASE_ThreadRWlockattrGetPshared**

&emsp;&emsp;【Description】

&emsp;&emsp;Gets the process-shared attribute.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_ThreadRWlockattrGetPshared(AK_RWLOCKATTR_T * ptRWlockattr, AK_S32 *ps32Value);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**     | **Value range** | **Input/Output** |
| ------------------ | ------------------ | ------------------ | --------------------------------------- |
| ptRWlockattr | Read-write-lock attributes to operate on | - | Input |
| ps32Value | Process-shared attribute value | - | Output |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0                | Success           |
| Nonzero | Failure |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_thread.a

&emsp;&emsp;Header: ak_thread.h

<br/>

### **AK_BASE_ThreadRWlockattrSetPshared**

&emsp;&emsp;【Description】

&emsp;&emsp;Sets the process-shared attribute.

&emsp;&emsp;【Syntax】

```C
    AK_S32 AK_BASE_ThreadRWlockattrSetPshared(AK_RWLOCKATTR_T * ptRWlockattr, AK_S32 s32Value);
```

&emsp;&emsp;【Parameters】

| **Parameter** | **Description**     | **Value range** | **Input/Output** |
| ------------------ | ------------------ | ------------------ | --------------------------------------- |
| ptRWlockattr | Read-write-lock attributes to operate on | - | Input |
| s32Value | Process-shared attribute value | - | Input |

&emsp;&emsp;【Return Value】

| **Return value** | **Description** |
| ---------------- | -------------- |
| 0                | Success           |
| Nonzero | Failure |

&emsp;&emsp;【Error Code List】

| **Error code** | **Description** |
| ---------------- | -------------- |
| -                | -              |

&emsp;&emsp;【Requirements】

&emsp;&emsp;Library: libplat_thread.a

&emsp;&emsp;Header: ak_thread.h

<br/>

### /var/platform Description

The /var/platform directory exposes the current module configuration parameters and status. Its parameters are described below.

#### stat

| Parameter | Description |
| ------- | -------------- |
| Version | THREAD library version |
