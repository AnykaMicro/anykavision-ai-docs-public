# Build Environment Setup

Use x86-64 Ubuntu 22.04. On Windows, open an Ubuntu terminal in WSL2. Choose paths without spaces for the SDK and toolchain.

## Install the host packages and get the SDK

```bash
sudo apt update
sudo apt install git wget ca-certificates python3 build-essential bzip2 file \
    cpio lz4 mtd-utils u-boot-tools xxd openssl
```

For a first build, clone the SDK. If you already have a checkout, enter its `sdk-km02g` directory.

```bash
mkdir -p "$HOME/src"
git clone https://github.com/AnykaMicro/sdk-km02g.git "$HOME/src/sdk-km02g"
cd "$HOME/src/sdk-km02g"
```

## Install the cross toolchain

Run these commands from the SDK root.

```bash
wget -O tools/toolchain-v1.00.tar.gz \
    https://downloads.sifli.com/dl/riscv64-anyka-linux-musl.tar.gz
python3 -I scripts/repack_toolchain.py \
    tools/toolchain-v1.00.tar.gz tools/riscv64-anyka-linux-musl.tar.gz
./scripts/get_toolchain.sh "$HOME/.local/opt"
export PATH="$HOME/.local/opt/riscv64-anyka-linux-musl/bin:$PATH"
riscv64-anyka-linux-musl-gcc --version
```

The last command should print the compiler version. Run the `export PATH` line in each new terminal, or add it to `~/.bashrc`.

## Build the demo application

For the demo executable alone, run `make app`. The output is `apps/ai_glass_demo/ai_glass_demo`.

## Build the OTA package

The full build also compiles the application. The first build needs internet access. For an offline build, place [busybox-1.35.0.tar.bz2](https://busybox.net/downloads/busybox-1.35.0.tar.bz2) and [mtd-utils-2.3.1.tar.bz2](https://infraroot.at/pub/mtd/mtd-utils-2.3.1.tar.bz2) in the SDK's `tools/` directory first.

**To enable root login on the device**, run the following commands and enter the device password when prompted.

```bash
mkdir -p rootfs/config.local
cp -n rootfs/config/shadow rootfs/config.local/shadow
openssl passwd -6
```

Open `rootfs/config.local/shadow` and paste the password hash into the second field of the `root` line (between the first two colons, replacing `*`, e.g. `root:$6$...:3652:0:99999:7:::`). Keep Unix (LF) line endings: CRLF line endings cause the packaging script to fail.

Git ignores `rootfs/config.local/`; any files placed there override same-named files from `rootfs/config/` in the configuration image (including local debug overrides such as `app_main_config.ini`). Save the file and build the image from the SDK root:

```bash
make
```

**To keep root locked**, leave the SDK's default `shadow` configuration in place and run `ALLOW_LOCKED_ROOT=1 make`.

```{warning}
`update.bin` carries both the RAMFS and CONFIG partitions. Applying an update built with `ALLOW_LOCKED_ROOT=1 make` locks root console login on the target device.
```

The OTA package is `tools/ota/update.bin`. The same directory contains the ramdisk (`ramfs.img`) and the configuration partition image (`usr.jffs2`). To install the update on the device, follow [Firmware Flashing](firmware-flashing.md).

## Known limitations

- Only the default feature switches in `apps/ai_glass_demo/common.mk` compile; disabling EIS, RTSP, or video recording does not currently build.
- `mtd-utils` 2.x builds `usr.jffs2` with 8 KiB erase blocks (it refuses the 4 KiB used by older bundled tools). After flashing, verify in the serial console log that the config partition mounts without JFFS2 errors.
