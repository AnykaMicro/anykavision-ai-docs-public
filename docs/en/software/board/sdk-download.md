# SDK Download

The [public KM02G SDK](https://github.com/AnykaMicro/sdk-km02g) contains the Linux demo application, middleware headers and prebuilt libraries, and the scripts that generate the OTA package. On x86-64 Linux or Ubuntu under WSL2, clone the SDK into a path without spaces.

```bash
mkdir -p "$HOME/src"
cd "$HOME/src"
git clone https://github.com/AnykaMicro/sdk-km02g.git
cd sdk-km02g
```

Download the cross compiler separately. SiFli hosts the [original V1.00 toolchain archive](https://downloads.sifli.com/dl/riscv64-anyka-linux-musl.tar.gz). Follow [Build Environment Setup](build-environment.md) to verify and repack the archive, install the compiler and build the images.
