# Build Environment Setup

These steps were verified on an x86-64 host running Ubuntu 22.04 under WSL2, using [KM02G SDK commit `fd4d49a`](https://github.com/AnykaMicro/sdk-km02g/tree/fd4d49ac8a84e6fdcb46b53c22c523342812dacb). Follow [SDK Download](sdk-download.md) to obtain the source, then run the commands from the SDK root.

## Build host

The toolchain runs on x86-64 Linux. Use paths without spaces for the SDK and the toolchain. Under WSL2, a directory such as `~/src/sdk-km02g` keeps the source on the Linux filesystem. Install the following packages on Ubuntu 22.04.

```bash
sudo apt update
sudo apt install git ca-certificates wget python3 build-essential linux-libc-dev \
    bzip2 file cpio lz4 mtd-utils u-boot-tools xxd openssl
```

`build-essential` provides the host compiler and Make. The host tests use headers from `linux-libc-dev`. Packaging uses `cpio`, `lz4`, `mkfs.jffs2` (from `mtd-utils`), `mkimage` (from `u-boot-tools`) and `xxd`. For Ubuntu 18.04 or 20.04, the SDK README lists `liblz4-tool` and `vim-common`. Check that your version of `mkimage` supports `-A riscv`.

## Install the cross toolchain

SiFli hosts the original V1.00 archive. `get_toolchain.sh` checks the SHA-256 of the repacked archive, so setting `TOOLCHAIN_URL` to the original download URL fails verification. Save the two files under different names and convert the original with the script included in the SDK.

```bash
wget -O tools/anyka-toolchain-v1.00-original.tar.gz \
    https://downloads.sifli.com/dl/riscv64-anyka-linux-musl.tar.gz
echo '9feed8ce46a44e9a892b50399fed49c6d17e221ebbddfb0f61fefadab21c3fb4  tools/anyka-toolchain-v1.00-original.tar.gz' | sha256sum -c -
python3 -I scripts/repack_toolchain.py \
    tools/anyka-toolchain-v1.00-original.tar.gz tools/riscv64-anyka-linux-musl.tar.gz
echo '13e7fbc62d87707572e252288f1c72623cb3595ae38bddc53bec11bb2a2da279  tools/riscv64-anyka-linux-musl.tar.gz' | sha256sum -c -
```

Once both checks report `OK`, install the compiler in a user-writable directory. Repeat the `export PATH` line when you open a new terminal.

```bash
./scripts/get_toolchain.sh "$HOME/.local/opt"
export PATH="$HOME/.local/opt/riscv64-anyka-linux-musl/bin:$PATH"
riscv64-anyka-linux-musl-gcc -dumpfullversion
riscv64-anyka-linux-musl-gcc -dumpmachine
```

The last two commands should print `12.2.0` and `riscv64-anyka-linux-musl`, respectively.

## Build steps

### Build the demo application and run the host tests

```bash
make app
file apps/ai_glass_demo/ai_glass_demo
make test
```

`make app` builds a 64-bit RISC-V executable for the KM02G. The host tests should report `list_test: PASS` and `uvc_test: PASS`.

### Build the OTA package

On the first image build, the SDK downloads [BusyBox 1.35.0](https://busybox.net/downloads/busybox-1.35.0.tar.bz2) and [mtd-utils 2.3.1](https://infraroot.at/pub/mtd/mtd-utils-2.3.1.tar.bz2), verifies the archives and builds BusyBox and `mtd_debug`. For an offline build, place `busybox-1.35.0.tar.bz2` and `mtd-utils-2.3.1.tar.bz2` in `tools/` in advance. You can also point `SOURCES_URL` at a mirror directory that serves both files. The SDK builds the ramdisk from source.

The default configuration locks the root account. For console login on the device, set a unique password for the device or build.

```bash
mkdir -p rootfs/config.local
cp -n rootfs/config/shadow rootfs/config.local/shadow
openssl passwd -6
```

In an editor, put the resulting hash in the second field of the `root` entry in `rootfs/config.local/shadow`. Git ignores `rootfs/config.local/`, and files there override the defaults during packaging. Keep the password and its hash private.

To enable debug Wi-Fi, copy `apps/ai_glass_demo/common/config/app_main_config.ini` to `rootfs/config.local/` and set `password=` under `[DebugAp]` (a WPA2 passphrase, 8 to 63 characters). Leaving it empty keeps the temporary debug AP and RTSP service disabled. Use a unique development-only passphrase rather than a production or corporate Wi-Fi credential. Don't put a comment after the value: everything after `=` is part of it. The other Wi-Fi files in `rootfs/config/` hold placeholders only; the app writes `hostapd.conf` and `wpa_supplicant.conf` at run time.

```bash
make
ls -lh tools/ota/update.bin tools/ota/ramfs.img tools/ota/usr.jffs2
```

`ramfs.img` contains the ramdisk and `usr.jffs2` contains the configuration partition. `update.bin` packages both images for OTA updates.

For a host-only packaging check, you can skip the password setup, keep the default locked account and run the following command.

```bash
ALLOW_LOCKED_ROOT=1 make
```

```{warning}
`update.bin` updates the KM02G RAMFS and CONFIG partitions. Applying an image that uses the default locked account to an existing device locks root login on that device.
```

After `make app`, you can run `make install` to package the images separately. BusyBox and `mtd_debug` are cached in `rootfs/build/` until you run `make distclean`.

## Known limitations

- Only the default feature switches in `apps/ai_glass_demo/common.mk` compile; turning EIS, RTSP or recording off does not build yet.
- mtd-utils 2.x builds `usr.jffs2` with 8 KiB erase blocks (it refuses the 4 KiB that the old bundled tool used). After flashing, check on your board that the config partition mounts without JFFS2 errors.

## Next step

When the build finishes, follow [Firmware Flashing](firmware-flashing.md) to update the reference board with `update.bin`.
