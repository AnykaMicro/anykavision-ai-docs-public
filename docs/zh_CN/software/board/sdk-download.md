# SDK下载

KM02G 的 Linux 示例应用、中间件头文件和预编译库，以及生成 OTA 升级包的脚本均在[公开 SDK 仓库](https://github.com/AnykaMicro/sdk-km02g)。在 x86-64 Linux 或 WSL2 的 Ubuntu 终端中，将源码克隆到不含空格的路径。

```bash
mkdir -p "$HOME/src"
cd "$HOME/src"
git clone https://github.com/AnykaMicro/sdk-km02g.git
cd sdk-km02g
```

交叉编译器单独下载。思澈下载站提供 [V1.00 原始工具链](https://downloads.sifli.com/dl/riscv64-anyka-linux-musl.tar.gz)。下载后，按[编译环境配置](build-environment.md)中的命令校验、重打包并安装工具链，再生成镜像。
