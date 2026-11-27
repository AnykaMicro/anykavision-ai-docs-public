# Build Environment Setup

<<<<<<< prepare/developer-kit-1.0.0
This page explains the SDK build steps and their caveats. The exact commands are in the README inside the SDK source archive; this page does not repeat them. See [SDK Download](sdk-download.md) for the published asset list and remaining release gates.
=======
Use x86-64 Ubuntu 22.04. On Windows, open an Ubuntu terminal in WSL2. Choose paths without spaces for the SDK and toolchain.
>>>>>>> main

## Install the host packages and get the SDK

<<<<<<< prepare/developer-kit-1.0.0
- x86-64 Linux, Ubuntu 18.04 or later. The toolchain runs only there; on macOS or Windows use a Linux VM or container. The packages to install are listed under **Host requirements** in the SDK README.
- Extract the SDK into a path **without spaces**: the Makefiles cannot handle them.
- `make test` (host-side unit tests) needs the host packages `gcc`, `libc6-dev` and `linux-libc-dev`.
=======
```bash
sudo apt update
sudo apt install git wget ca-certificates python3 build-essential bzip2 file \
    cpio lz4 mtd-utils u-boot-tools xxd openssl
```
>>>>>>> main

For a first build, clone the SDK. If you already have a checkout, enter its `sdk-km02g` directory.

```bash
mkdir -p "$HOME/src"
git clone https://github.com/AnykaMicro/sdk-km02g.git "$HOME/src/sdk-km02g"
cd "$HOME/src/sdk-km02g"
```

<<<<<<< prepare/developer-kit-1.0.0
1. **Install the toolchain**: public redistribution of the toolchain remains gated. Obtain the exact checksum-matched `riscv64-anyka-linux-musl.tar.gz` from Anyka, put it in `tools/`, then run `./scripts/get_toolchain.sh`. The script checks its SHA-256 and unpacks it to `/opt`. Then add `/opt/riscv64-anyka-linux-musl/bin` to your `PATH`. To install elsewhere, pass the directory as the first argument; the script relocates the toolchain there.
2. **For full images, prepare the ramdisk sources**: put the verified `busybox-1.35.0.tar.bz2` and `mtd-utils-2.3.1.tar.bz2` release assets in `tools/`. Full `make` checks them and builds the ramdisk from those sources, `rootfs/skeleton/` and your `ai_glass_demo`. You can also set `SOURCES_URL` to an approved mirror.
3. **For full images, supply the licensed formatter**: the clean public archive removes the unresolved legacy `rootfs/skeleton/etc/format_tool` artifact. Obtain the approved V1.00 formatter separately from Anyka. It must be an executable file, passed by absolute path, with SHA-256 `6e608235637406349c5da89b0657ee9e3386ba55ee9175140c586d7718f01603`; the build rejects any other byte hash. For example, use `FORMAT_TOOL_BIN=/absolute/path/to/licensed/format_tool make`. The default fallback is `rootfs/vendor/format_tool`; the build copies the approved tool to image path `/etc/format_tool`.
4. **For full images, set a root password**: the shipped configuration locks root, so image packaging stops until you set a password. Copy `rootfs/config/shadow` to `rootfs/config.local/` first, then put the password hash in the second field of its `root` line; do not edit the tracked `rootfs/config/shadow`. Files in `rootfs/config.local/` replace those of `rootfs/config/` in the config image, and git ignores the folder, so the hash is never committed. Use a unique strong password for each device or build, never ship a shared development password, and never commit or share the hash.
5. **Optional for full images: set the debug Wi-Fi password**: copy `apps/ai_glass_demo/common/config/app_main_config.ini` to `rootfs/config.local/` and set `password=` under `[DebugAp]` (a WPA2 passphrase, 8 to 63 characters). Leaving it empty keeps the temporary debug AP and RTSP service disabled. Use a unique development-only passphrase rather than a production or corporate Wi-Fi credential. Don't put a comment after the value: everything after `=` is part of it. The other Wi-Fi files in `rootfs/config/` hold placeholders only; the app writes `hostapd.conf` and `wpa_supplicant.conf` at run time.
6. **Test and build the application**: run `make test`, then `make app`. Run `make install` or full `make` only after the separately supplied licensed formatter and all full-image inputs are present. Full-image results are written under `tools/ota/`: `update.bin` (OTA package), `ramfs.img` and `usr.jffs2`. BusyBox and `mtd_debug` are built once and kept in `rootfs/build/`; `make distclean` removes them.
=======
## Install the cross toolchain
>>>>>>> main

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

<<<<<<< prepare/developer-kit-1.0.0
Only after the licensed formatter is present and a full image has been built and validated, follow [Firmware Flashing](firmware-flashing.md) to update the reference board with `update.bin`.
=======
- Only the default feature switches in `apps/ai_glass_demo/common.mk` compile; disabling EIS, RTSP, or video recording does not currently build.
- `mtd-utils` 2.x builds `usr.jffs2` with 8 KiB erase blocks (it refuses the 4 KiB used by older bundled tools). After flashing, verify in the serial console log that the config partition mounts without JFFS2 errors.
>>>>>>> main
