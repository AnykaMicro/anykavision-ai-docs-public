# 快速开发指南

## 第一章 概述

本文档介绍AI眼镜SDK的方案参考设计，目的是供您在开发过程中快速编译、烧写并运行眼镜程序。

### 1.1 产品版本

与本文档相对应的产品版本如下。

| 芯片简介  | 操作系统     |
| ----- | --------- |
| KM02G系列芯片 | Linux+RTT |

### 1.2 硬件版本

| 硬件名称 | 芯片            | 说明  |
| ---- | ------------- | --- |
| 产品板  | KM02G系列芯片+AK1090系列芯片 |     |

### 1.3 缩写说明

本文会用到如下缩写词：

- **APP**：眼镜手机端 Anyka_Glasses 程序
- **BT**：蓝牙模块（AK1090系列芯片）
- **RTT**：运行在 KM02G系列芯片 上的 RT-Thread 系统
- **LINUX**：运行在 KM02G系列芯片 上的 Linux 系统

---

## 第二章 环境搭建

按[编译环境配置](build-environment.md)下载 KM02G SDK、安装交叉工具链并设置设备的 root 登录方式。

---

## 第三章 固件编译

在 SDK 根目录运行 `make`，生成 `tools/ota/update.bin`。使用 SDK 默认锁定的 root 配置时，运行 `ALLOW_LOCKED_ROOT=1 make`。

<<<<<<< prepare/developer-kit-1.0.0
按[SDK下载](sdk-download.md)和[编译环境配置](build-environment.md)完成以下准备，具体命令见 SDK README：

1. 从 1.0.0 Release 下载并校验已发布的 SDK 源码包和 BusyBox、mtd-utils 源码包；把 SDK 解压到不含空格的路径。
2. 把校验通过的 BusyBox 和 mtd-utils 源码包放入 SDK 的 `tools/` 目录。
3. 工具链公开再分发门禁通过前，请向安凯获取校验和匹配的工具链压缩包并放入 `tools/`；然后运行 `./scripts/get_toolchain.sh`，并把 `/opt/riscv64-anyka-linux-musl/bin` 加入 `PATH`。
4. 清洁公开源码包已移除来源和许可未解决的旧版 `rootfs/skeleton/etc/format_tool` 文件。生成完整 ramdisk 和固件镜像前，须按适当的许可条款另行向安凯获取已批准的 V1.00 格式化工具，满足[SDK下载](sdk-download.md)所列的可执行权限和 SHA-256 要求，再通过 `FORMAT_TOOL_BIN=/absolute/path/to/licensed/format_tool` 传入；默认回退路径为 `rootfs/vendor/format_tool`。缺少时不要运行完整 `make` 或 `make install`。
5. 仅在生成完整镜像时，把 `rootfs/config/shadow` 复制到 `rootfs/config.local/`，在副本的 `root` 行中设置密码哈希（`openssl passwd -6`），不要修改受 git 跟踪的 `rootfs/config/shadow`。每台设备或每个构建使用唯一的强密码，不要在设备上发布共用的开发密码，也不要提交或共享密码哈希。

### 3.2 编译程序

公开源码包可运行主机端测试并编译应用：

```bash
make clean        # 清除
make test         # 运行主机端测试
make app          # 编译 app
```
=======
只修改示例程序时，运行 `make app` 即可生成 `apps/ai_glass_demo/ai_glass_demo`。
>>>>>>> main

只有在另行提供的已获许可厂商格式化工具和全部完整镜像输入就绪后，才能运行 `FORMAT_TOOL_BIN=/absolute/path/to/licensed/format_tool make` 或相应的 `make install`。SDK 会把选定工具复制到镜像内的 `/etc/format_tool`。由此生成的 `update.bin`、`ramfs.img` 和 `usr.jffs2` 位于 `tools/ota`，并须通过所需的开发板验证。

## 第四章 固件烧写

完整镜像构建并验证后，U 盘升级和恢复出厂设置的步骤见[固件烧写](firmware-flashing.md)。

---

## 第五章 功能说明

```{note}
以下涉及手机 APP 的操作（录像时长设置、AI识图、图库导入、实时视频预览）需要 Anyka_Glasses APP。该 APP 尚未随本次版本发布，开发者可在后续版本中补充安装包。
```

### 5.1 拍照

**操作方式：** 短按一下功能键\
**提示音：** 拍照开始播放"滴"，拍照完成播放"咔嚓"\
**后续操作：** 拍照结束后关机KM02G系列芯片

### 5.2 录像

**操作方式：** 长按功能键3秒开始录像，短按一下功能键结束录像\
**提示音：** 录像开始播放"叮"，录像完成播放"叮叮"\
**默认录像时长：** 1分钟（如需不同时长，快速按5次APP版本号，在录像定时时长处输入1-600，单位秒。设备端接受任意正数时长，小于或等于0时按600秒录像）\
**后续操作：** 录像结束后关机KM02G系列芯片

### 5.3 AI识图

**前提条件：** 手机绑定好眼镜\
**操作方式：** 打开手机APP，进入AI识图界面，短按两下功能键，图片显示在APP识图界面，识别结果文字可显示在识图界面，并且可通过眼镜喇叭播放识别结果\
**后续操作：** 识图结束后关机KM02G系列芯片

### 5.4 开关机

操作方式：长按开关键3秒表示关机，短按1下开关机键表示开机。
提示音：关机播报“关机”，开机播报“开机”。

### 5.5 查看眼镜拍摄的录像与图片

操作方式1：眼镜通过USB线连接电脑，眼镜会以U盘方式呈现在电脑端。录像路径：U盘根目录/Videos/; 拍照路径：U盘根目录/Pictures/。

**操作方式2：** 打开手机APP，绑定眼镜设备后，进入图库管理界面，可将录像和照片导入到手机上。

### 5.6 实时视频预览

打开手机APP，绑定眼镜设备之后，进入视频直播界面，可查看设备实时视频。
