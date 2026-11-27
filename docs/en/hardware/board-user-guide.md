# Product Board User Guide

## About This Document

This document uses the AI camera-glasses product board as an example to introduce the board's technical specifications and the reference materials used during its hardware design. It is intended for hardware engineers and solution-selection personnel who need a quick overview of the board specifications and design references.

## Product Board Information

The AI camera-glasses product board uses KM02G-series and AK1090-series controller chips. Developers can use it to prototype AI-enabled camera glasses. For details about these chips, see [KM02G-Series Chip Introduction](chips/km02g.md) and [AK1090-Series Chip Introduction](chips/ak1090.md).

## Product Board Specifications

| **Category** | **Description** |
| ------------ | --------------- |
| Controller platform | Anyka KM02G-series chip + AK1090-series chip |
| Storage | 4 GiB SD NAND flash; 16 MiB SPI NOR flash |
| Connectivity | Wi-Fi (2.4 GHz/5 GHz, Altobeam ATBM6162 Wi-Fi chip) + AK1090-series chip |
| Imaging | Supports the 13 MP GC13B0 CIS module |
| Audio | One open-ear speaker + three silicon microphones (one AMIC and two DMICs) |
| Charging | Type-C charging port, maximum charging current 180 mA |

## Functional Block Diagram

![Product-board functional block diagram](../../zh_CN/hardware/img/board-function-block-diagram.png)

> The labels embedded in this source figure are in Chinese.

## Application Development

This section describes the hardware and software setup, how to flash firmware to the product board, and how to develop applications.

### Hardware Preparation

- 1 x KM02G-series + AK1090-series product board
- 1 x USB 2.0 cable (standard Type-A to Type-C)
- 1 x computer (Windows or Linux)
- 1 x Android phone for the Anyka_Glasses app. The app has not yet been released and may be supplied in a later version.

### Connection and Flashing

Connect the product board's Type-C port to the computer with a USB 2.0 cable, then upgrade the firmware by following [Firmware Flashing](../software/board/firmware-flashing.md).

For more detailed configuration, see [Application Development Instructions](../software/board/app-development.md).

## Product Board Hardware-Design References

See the [Product Board Design Guide](board-design-guide.md).

| <div style ="min-width: 200px">**Reference**</div> | **Description** |
| --------------------------------------------------- | --------------- |
| AI camera-glasses product-board design guide | Product-board circuit-design guide (including controller-circuit, peripheral-device, and interface-circuit design) and PCB-design guide. |
| SC7U22 datasheet | Gyroscope datasheet, including precautions for gyroscope circuit design and assembly. Obtain it from the component manufacturer. |
| DF1527 application guide | PMIC power-management circuit-design guide, including key circuit- and PCB-design considerations. Obtain it from the component manufacturer. |
| ATBM6162 product specification | Wi-Fi chip datasheet, including device specifications, package information, and circuit-design guidance. Obtain it from the component manufacturer. |
| | |

## Obtaining the Materials

The product-board hardware-design materials have not yet been released. They may be supplied and this section updated in a later version.

Obtain the third-party component datasheets (SC7U22, DF1527, and ATBM6162) from their respective manufacturers.
