# 编译环境配置

以下步骤已在 x86-64 主机的 WSL2 Ubuntu 22.04 中验证，使用的 [KM02G SDK 提交为 `fd4d49a`](https://github.com/AnykaMicro/sdk-km02g/tree/fd4d49ac8a84e6fdcb46b53c22c523342812dacb)。按[SDK下载](sdk-download.md)获取源码后，在 SDK 根目录运行以下命令。

## 编译主机

工具链运行在 x86-64 Linux 上，SDK 和工具链的安装路径均应避开空格。使用 WSL2 时，可将源码放在 Linux 用户目录下，例如 `~/src/sdk-km02g`。Ubuntu 22.04 的依赖可一次安装。

```bash
sudo apt update
sudo apt install git ca-certificates wget python3 build-essential linux-libc-dev \
    bzip2 file cpio lz4 mtd-utils u-boot-tools xxd openssl
```

`build-essential` 提供主机编译器和 Make，`linux-libc-dev` 提供主机测试所需的头文件。生成镜像还要用到 `cpio`、`lz4`、`mkfs.jffs2`（`mtd-utils`）、`mkimage`（`u-boot-tools`）和 `xxd`。Ubuntu 18.04 或 20.04 可按 SDK README 使用 `liblz4-tool` 和 `vim-common`，并确认 `mkimage` 支持 `-A riscv`。

## 安装交叉工具链

思澈下载站提供的是 V1.00 原始包。`get_toolchain.sh` 校验重打包后的 SHA-256，直接把原包的下载地址设为 `TOOLCHAIN_URL` 会校验失败。下面的命令把两种包保存为不同文件，并用 SDK 自带的脚本转换。

```bash
wget -O tools/anyka-toolchain-v1.00-original.tar.gz \
    https://downloads.sifli.com/dl/riscv64-anyka-linux-musl.tar.gz
echo '9feed8ce46a44e9a892b50399fed49c6d17e221ebbddfb0f61fefadab21c3fb4  tools/anyka-toolchain-v1.00-original.tar.gz' | sha256sum -c -
python3 -I scripts/repack_toolchain.py \
    tools/anyka-toolchain-v1.00-original.tar.gz tools/riscv64-anyka-linux-musl.tar.gz
echo '13e7fbc62d87707572e252288f1c72623cb3595ae38bddc53bec11bb2a2da279  tools/riscv64-anyka-linux-musl.tar.gz' | sha256sum -c -
```

两项校验均显示 `OK` 后，安装到当前用户可写的目录。新开终端时重新执行 `export PATH` 这一行。

```bash
./scripts/get_toolchain.sh "$HOME/.local/opt"
export PATH="$HOME/.local/opt/riscv64-anyka-linux-musl/bin:$PATH"
riscv64-anyka-linux-musl-gcc -dumpfullversion
riscv64-anyka-linux-musl-gcc -dumpmachine
```

最后两行应分别输出 `12.2.0` 和 `riscv64-anyka-linux-musl`。

## 编译步骤

### 编译示例应用和运行主机测试

```bash
make app
file apps/ai_glass_demo/ai_glass_demo
make test
```

`make app` 生成适用于 KM02G 的 64 位 RISC-V 程序。主机上的两项测试分别输出 `list_test: PASS` 和 `uvc_test: PASS`。

### 生成 OTA 升级包

首次打包时，SDK 下载 [BusyBox 1.35.0](https://busybox.net/downloads/busybox-1.35.0.tar.bz2) 和 [mtd-utils 2.3.1](https://infraroot.at/pub/mtd/mtd-utils-2.3.1.tar.bz2)，校验后编译 BusyBox 和 `mtd_debug`。离线构建可提前将 `busybox-1.35.0.tar.bz2` 和 `mtd-utils-2.3.1.tar.bz2` 放入 `tools/`。也可以把 `SOURCES_URL` 指向同时提供这两个文件的镜像目录。SDK 会从源码生成 ramdisk。

默认配置锁定了 root。需要在设备控制台登录时，先为当前设备或构建设定独立密码。

```bash
mkdir -p rootfs/config.local
cp -n rootfs/config/shadow rootfs/config.local/shadow
openssl passwd -6
```

用编辑器将命令输出的哈希写入 `rootfs/config.local/shadow` 中 `root` 行的第二个字段。Git 会忽略 `rootfs/config.local/`，打包时该目录下的文件会覆盖默认配置。请保管好密码及其哈希。

如需启用调试 Wi-Fi，把 `apps/ai_glass_demo/common/config/app_main_config.ini` 复制到 `rootfs/config.local/`，在 `[DebugAp]` 中设置 `password=`（WPA2 密码，8 到 63 个字符）。留空会保持临时调试热点和 RTSP 服务关闭。请使用仅供本次开发调试的唯一密码，不要复用生产环境或公司 Wi-Fi 凭据。不要在值后面加注释：`=` 之后的全部内容都属于密码。`rootfs/config/` 中的其他 Wi-Fi 配置文件只包含占位值，应用在运行时写入 `hostapd.conf` 和 `wpa_supplicant.conf`。

```bash
make
ls -lh tools/ota/update.bin tools/ota/ramfs.img tools/ota/usr.jffs2
```

`ramfs.img` 是 ramdisk，`usr.jffs2` 是配置分区镜像，`update.bin` 将两者封装成 OTA 升级包。

只在主机验证打包时，可以跳过密码设置，保留 SDK 默认锁定的 root 账户，并运行下面这条命令。

```bash
ALLOW_LOCKED_ROOT=1 make
```

```{warning}
`update.bin` 会更新 KM02G 的 RAMFS 和 CONFIG 分区。把使用默认锁定账户打包的镜像用于现有设备，会锁定该设备的 root 登录。
```

`make install` 可以在 `make app` 之后单独打包。BusyBox 和 `mtd_debug` 的构建缓存位于 `rootfs/build/`，可用 `make distclean` 清除。

## 已知限制

- 只有 `apps/ai_glass_demo/common.mk` 中默认的功能开关组合可以编译；关闭 EIS、RTSP 或录像功能目前无法编译。
- mtd-utils 2.x 生成的 `usr.jffs2` 使用 8 KiB 擦除块（它不接受旧版内置工具使用的 4 KiB）。烧写后，请在开发板上确认配置分区挂载时没有 JFFS2 错误。

## 下一步

编译完成后，按[固件烧写](firmware-flashing.md)把 `update.bin` 升级到产品板。
