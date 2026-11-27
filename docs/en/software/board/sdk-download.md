# SDK Download

<<<<<<< prepare/developer-kit-1.0.0
The first 1.0.0 developer draft publishes the core KM02G SDK source and the upstream source archives needed by its build on this repository's Releases page. The SDK and support-source links below are live. The table also identifies inputs that remain gated or unavailable.

Release base: `https://github.com/Anyka-Micro/anykavision-ai-docs-public/releases/download/1.0.0/`

## Included, required and pending inputs

| Input | 1.0.0 state | Use |
|---|---|---|
| `anykavision-km02g-sdk-1.00.tar.gz` and `SHA256SUMS` | Published first-draft assets; package and release checksums verified | Core KM02G SDK source, build scripts, middleware headers/libraries and demo application. Extracts to `anykavision-km02g-sdk-1.00/`; the unresolved legacy `rootfs/skeleton/etc/format_tool` artifact is removed |
| `busybox-1.35.0.tar.bz2`, `busybox-1.35.0.tar.bz2.sig`, `busybox-1.35.0.config`, `mtd-utils-2.3.1.tar.bz2`, `mtd-utils-2.3.1.tar.bz2.asc` | Published support assets; checksums verified, but detached signatures not independently verified because the public keys were unavailable during preparation | Put the two source archives in the SDK's `tools/` directory. The SDK source already contains the build config it uses |
| `riscv64-anyka-linux-musl.tar.gz` | Required to build, but not approved for public redistribution yet | Obtain the exact checksum-matched archive from Anyka and put it in the SDK's `tools/` directory. A public download can be added only after corresponding-source and licence checks pass |
| Licensed vendor formatter supplied through `FORMAT_TOOL_BIN` | Required for full ramdisk and firmware images; not included | Obtain the approved V1.00 executable separately from Anyka under appropriate licence terms. It must be executable, use an absolute path and have SHA-256 `6e608235637406349c5da89b0657ee9e3386ba55ee9175140c586d7718f01603`. The default fallback is `rootfs/vendor/format_tool`; the build rejects any other byte hash and copies the approved file to image path `/etc/format_tool` |
| `ramfs.img` | Optional reference image; not part of the build input and not approved for publication yet | The clean public SDK cannot build it without the separately supplied licensed vendor formatter. Provenance/licence review and build validation must pass before a prebuilt image is published |
| Factory APP-partition scripts | Required for the factory USB update/UVC environment, but not supplied by this SDK | `/usr/sbin/usb_udc_g.sh` and `/usr/sbin/uvc.sh` must come from matching factory firmware |
| Anyka_Glasses app/source, AK1090 firmware and board design files | Pending | Not included in the first 1.0.0 developer draft; the developer can add them later |

Clean-source packaging and source-export review passed. In an internal, offline Ubuntu 22.04 x86-64 environment, `make test` (`list_test` plus `uvc_test` under ASan/UBSan) and the RISC-V `make app` build passed using an existing withheld toolchain. This does not approve the toolchain for public redistribution; its licensing gate remains pending. With no licensed formatter supplied, full `ALLOW_LOCKED_ROOT=1 make` stopped before image creation as intended. Full images, flashing, OTA, Wi-Fi and USB webcam operation remain unverified.

## Developer quick start

Use an x86-64 Linux host. Download and verify the published source archive and the two upstream source archives. The commands stop before extraction if a download, manifest entry or checksum is wrong:

<!-- sdk-download-example:start -->
```bash
set -euo pipefail
release_base=https://github.com/Anyka-Micro/anykavision-ai-docs-public/releases/download/1.0.0
assets=(anykavision-km02g-sdk-1.00.tar.gz busybox-1.35.0.tar.bz2 mtd-utils-2.3.1.tar.bz2)
for asset in SHA256SUMS "${assets[@]}"; do
  curl --fail --location --remote-name "$release_base/$asset"
done
cat > SHA256SUMS.required <<'EOF'
6e269573adc50dd2ed11e3bc6f22bd0dca481bde2b58c1794bcbdf6fad9a4b22  anykavision-km02g-sdk-1.00.tar.gz
faeeb244c35a348a334f4a59e44626ee870fb07b6884d68c10ae8bc19f83a694  busybox-1.35.0.tar.bz2
03d9dc58ad10ea3549d9528f6b17a44d8944e18e96c0f31474f9f977078b83dc  mtd-utils-2.3.1.tar.bz2
EOF
while IFS= read -r expected; do grep --fixed-strings --line-regexp "$expected" SHA256SUMS; done < SHA256SUMS.required
sha256sum --check SHA256SUMS.required
tar -xzf anykavision-km02g-sdk-1.00.tar.gz
mv busybox-1.35.0.tar.bz2 mtd-utils-2.3.1.tar.bz2 anykavision-km02g-sdk-1.00/tools/
cd anykavision-km02g-sdk-1.00
```
<!-- sdk-download-example:end -->

Obtain the required checksum-matched toolchain archive from Anyka while its public redistribution gate remains pending, then place it at `tools/riscv64-anyka-linux-musl.tar.gz`. Follow [Build Environment Setup](build-environment.md) to install it, run the host tests and build the application:

```bash
./scripts/get_toolchain.sh
export PATH="$PATH:/opt/riscv64-anyka-linux-musl/bin"
make test
make app
```

This public path does not produce firmware images. Full `make` and `make install` additionally require all full-image inputs and the separately supplied approved V1.00 formatter. Check that it is executable and has the required byte hash before passing its absolute path:

```bash
format_tool=/absolute/path/to/licensed/format_tool
test -f "$format_tool" && test -x "$format_tool"
printf '%s  %s\n' 6e608235637406349c5da89b0657ee9e3386ba55ee9175140c586d7718f01603 "$format_tool" | sha256sum --check -
FORMAT_TOOL_BIN="$format_tool" make
```

The SDK performs the same executable and SHA-256 checks, then copies the approved formatter to image path `/etc/format_tool`; its default fallback is `rootfs/vendor/format_tool`. Any resulting `update.bin`, `ramfs.img` and `usr.jffs2` remain unverified development outputs until they pass the required board validation.
=======
- [KM02G SDK source](https://github.com/AnykaMicro/sdk-km02g) includes the Linux demo application, middleware and OTA packaging scripts.
- [V1.00 RISC-V cross toolchain](https://downloads.sifli.com/dl/riscv64-anyka-linux-musl.tar.gz) runs on x86-64 Linux hosts.

For a first build, follow [Build Environment Setup](build-environment.md) to clone the SDK, install the compiler and generate the OTA package.
>>>>>>> main
