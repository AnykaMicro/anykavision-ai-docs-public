# 快速入门

欢迎开发者使用AnykaVision AI。AnykaVision AI面向芯片及系统开发者，提供一站式技术资源和交流平台，帮助开发者高效完成产品设计与应用开发。平台围绕硬件、软件及系统应用，构建完整的技术支持体系。同时，AnykaVision AI还汇集了丰富的技术文档，包括开发指南、接口说明、常见问题等，帮助开发者降低学习成本，提高开发效率。

## 快速上手

按以下顺序完成从获取 SDK 到在产品板上运行固件的全过程：

1. **获取 SDK**：[SDK下载](../software/board/sdk-download.md)
2. **编译**：[编译环境配置](../software/board/build-environment.md)
3. **烧写**：[固件烧写](../software/board/firmware-flashing.md)
4. **应用开发**：[应用开发说明](../software/board/app-development.md)

配套的 Anyka_Glasses 手机 APP 尚未随本次版本发布，[APP开发](../software/app/index.md)中的页面仅供参考；开发者可在后续版本中补充安装包。

如需先了解整体流程和产品板的基本操作，请阅读[快速开发指南](../software/board/quick-development.md)。

## 适用人群

AnykaVision AI适合以下开发者使用：

- **软件开发者**：提供驱动、示例代码、开发工具以及开发指南，帮助开发者快速搭建和验证应用方案。
- **硬件开发者**：提供芯片规格说明、参考设计、产品板资料等，帮助开发者快速理解与使用芯片能力。

## 内容结构

**1. 软件开发**

- [产品板开发](../software/board/index.md)
  - [快速开发指南](../software/board/quick-development.md)：提供给开发者能够快速上手的操作说明。
  - [SDK下载](../software/board/sdk-download.md)：提供AI拍摄眼镜方案软件开发包的获取方法。
  - [编译环境配置](../software/board/build-environment.md)：说明编译主机要求、编译步骤和注意事项。
  - [固件烧写](../software/board/firmware-flashing.md)：提供将编译好的固件升级到产品板的操作说明。
  - [应用开发说明](../software/board/app-development.md)：提供开发者基于SDK开发AI拍摄眼镜应用程序的完整指导，涵盖核心功能调用、开发流程及示例代码说明。
  - [AI拍摄眼镜通信协议](../software/board/communication-protocol.md)：提供KM02G系列芯片、AK1090系列芯片以及APP之间的通信协议说明，包含通信格式和命令说明。
  - [中间件接口说明](../software/board/middleware-api/index.md)：提供中间件软件的API使用方法、相关数据结构定义及错误码说明。
- [APP开发](../software/app/index.md)：Anyka_Glasses APP 的使用、打包与代码说明。该 APP 尚未随本次版本发布，可在后续版本中补充；相关页面仅供参考。
- [Git操作指南](../software/git-guide.md)：提供开发者参与开源项目所需的Git基础操作与协作流程说明。

**2. 硬件开发**

- [产品板使用指南](../hardware/board-user-guide.md)：提供产品板技术参数及硬件设计参考资料，面向硬件工程师与方案选型人员。
- [产品板设计指南](../hardware/board-design-guide.md)：提供产品板的硬件设计指南、电路设计建议、PCB布局规范和电源管理等说明。
- [芯片介绍](../hardware/chips/index.md)：KM02G系列芯片和AK1090系列芯片的功能框图与规格。

**3. [FAQ](../faq.md)**

- 汇总拍摄模式、通信指令、陀螺仪摆放及串口配置等常见问题及其解决方法。

## 使用建议

**1. 关键词搜索**

- 如果您不确定所需内容的位置，请使用搜索功能。
- 输入关键词，例如功能名称、接口名称或硬件模块名称，快速定位相关内容。

**2. 示例代码学习**

- AnykaVision AI包含大量示例代码，建议结合实际项目进行实践，以加深对文档内容的理解。

**3. 内容更新**

- [SDK下载](../software/board/sdk-download.md)列出了 KM02G 源码仓库和交叉工具链的下载地址。

## 技术支持

如果您在使用AnykaVision AI的过程中遇到问题，建议您：

- 查阅[FAQ](../faq.md)，这里列出了常见问题及其解决方法。
- 文档问题可在本说明文档仓库提交 issue。如需 SDK 或硬件支持，请通过已有渠道联系安凯。

---

感谢您选择并使用AnykaVision AI！您的支持与参与是我们持续进步的动力。
