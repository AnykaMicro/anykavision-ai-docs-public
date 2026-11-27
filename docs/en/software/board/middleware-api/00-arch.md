# Architecture
## System Architecture

&emsp;&emsp;The system layers are shown in Figure 1-1:

![Figure 1-1 System layers](../../../../zh_CN/software/board/middleware-api/img/system-layers.png)

> The labels embedded in this source figure are in Chinese.

| **Main system layer** | **Description** |
| ---------------- | ------------------------------------------------------------ |
| Application layer | Application software developed by the user on top of the platform and other drivers. |
| Middleware interface layer | Controls the chip to perform the corresponding media-processing functions and provides upper-layer application programming interfaces. |
| Independent driver layer | The corresponding driver modules. |
| Operating-system layer | Supports an RTOS or Linux. |
| Hardware layer | Consists of the chip and necessary peripherals, including Flash, Ethernet, Wi-Fi, and LCD devices. |

<br/>

## Middleware Overview

&emsp;&emsp;The middleware interface layer supports rapid application development. It hides complex chip-specific low-level processing from application software and directly provides upper-layer programming interfaces for the required functions. Its main functions include common services, memory management, multithreading, logging, audio and video processing, video overlays, a 2D image engine, demuxing, and muxing.

| **Module** | **Description** |
| ------------ | ------------------------------------------------- |
| Common | Provides basic cross-platform functions, such as date and time functions. |
| Memory | Provides general management of memory pools, circular buffers, and DMA operations. |
| Thread | Provides cross-platform thread operations. |
| Log | Provides logging functions. |
| Audio | Provides audio-device input/output, audio effects, and codec operations. |
| Video | Provides video input/output, image processing, and codec operations. |

<br/>
