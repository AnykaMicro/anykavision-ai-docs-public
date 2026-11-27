# 编译环境配置

使用 x86-64 Ubuntu 22.04，Windows 用户可使用 WSL2 的 Ubuntu 终端。源码和工具链的安装路径应避开空格。

## 安装依赖并下载 SDK

```bash
sudo apt update
sudo apt install git wget ca-certificates python3 build-essential bzip2 file \
    cpio lz4 mtd-utils u-boot-tools xxd openssl
```

首次使用时克隆源码。已有 SDK 的读者直接进入自己的 `sdk-km02g` 目录。

```bash
mkdir -p "$HOME/src"
git clone https://github.com/AnykaMicro/sdk-km02g.git "$HOME/src/sdk-km02g"
cd "$HOME/src/sdk-km02g"
```

## 安装交叉工具链

在 SDK 根目录依次执行以下命令。

```bash
wget -O tools/toolchain-v1.00.tar.gz \
    https://downloads.sifli.com/dl/riscv64-anyka-linux-musl.tar.gz
python3 -I scripts/repack_toolchain.py \
    tools/toolchain-v1.00.tar.gz tools/riscv64-anyka-linux-musl.tar.gz
./scripts/get_toolchain.sh "$HOME/.local/opt"
export PATH="$HOME/.local/opt/riscv64-anyka-linux-musl/bin:$PATH"
```

新开终端后，重新执行最后一行 `export PATH`，或将它加入 `~/.bashrc`。

## 编译示例应用

只需要示例程序时，运行 `make app`。可执行文件位于 `apps/ai_glass_demo/ai_glass_demo`。

## 生成 OTA 升级包

完整打包会同时编译应用。首次打包需要联网。离线编译时，先将 [busybox-1.35.0.tar.bz2](https://busybox.net/downloads/busybox-1.35.0.tar.bz2) 和 [mtd-utils-2.3.1.tar.bz2](https://infraroot.at/pub/mtd/mtd-utils-2.3.1.tar.bz2) 放入 SDK 的 `tools/` 目录。

**设备需要 root 登录时**，先运行以下命令，按提示输入设备密码。

```bash
mkdir -p rootfs/config.local
cp -n rootfs/config/shadow rootfs/config.local/shadow
openssl passwd -6
```

打开 `rootfs/config.local/shadow`，把输出的密码哈希填入 `root` 行的第二个字段（前两个冒号之间）。保存后在 SDK 根目录编译。

```bash
make
```

**设备需要锁定 root 时**，保留 SDK 默认的 `shadow` 配置，直接运行 `ALLOW_LOCKED_ROOT=1 make`。用这个包升级会锁定目标设备的 root 登录。

生成的 OTA 升级包为 `tools/ota/update.bin`。同目录中的 `ramfs.img` 和 `usr.jffs2` 分别是 ramdisk 和配置分区镜像。将升级包写入设备的步骤见[固件烧写](firmware-flashing.md)。
