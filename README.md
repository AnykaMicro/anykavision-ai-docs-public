# AnykaVision AI Documentation

English | [简体中文](#anykavision-ai-文档)

Documentation for **AnykaVision AI V1.00**, a development platform for AI camera glasses built on Anyka's KM02G series (image SoC) and AK1090 series (Bluetooth audio SoC) chips.

- **Documentation release:** 1.0.0
- **Website:** <https://anyka-micro.github.io/anykavision-ai-docs-public/> (pending; Pages deployment is disabled)
- **Languages:** Simplified Chinese (complete) and English (translation in progress)

## Repository layout

```
docs/
├── conf.py        Sphinx configuration shared by both languages
├── _templates/    language switcher and hreflang links
├── index.html     language picker at the site root
├── glossary.md    Chinese → English terms for translators
├── zh_CN/         Chinese source, the reference version
└── en/            English translation, same file paths as zh_CN
tools/
├── check_links.py           relative-link check (run in CI after the build)
└── check_api_vs_headers.py  compares the API reference with the SDK headers (report only)
requirements.in    top-level dependencies; requirements.txt is the hash-locked install set
```

English pages reuse the images under `docs/zh_CN`, so each image is stored once.

## Build locally

```bash
python3 -m venv .venv
.venv/bin/pip install --require-hashes -r requirements.txt
.venv/bin/sphinx-build -W -c docs -D language=en docs/en _build/html/en
.venv/bin/sphinx-build -W -c docs -D language=zh_CN docs/zh_CN _build/html/zh_CN
cp docs/index.html _build/html/
python3 tools/check_links.py . _build/html
```

Then open `_build/html/index.html`. Build both languages: the language switcher links between them. Content still waiting for Anyka (removed figures, text that needs a rewrite) is kept in the sources but left out of the site; add `-t anyka_review` to the `sphinx-build` commands to see it. GitHub Actions runs the same build and link check on every pull request and every push to `main`. Deployment to GitHub Pages is switched off until launch; once it is on, only the Chinese site is deployed until a named reviewer signs the English translation off (`PUBLISH_LANGS` in `.github/workflows/pages.yml`).

## Translating

1. Pick a page marked "Translation pending" in `docs/en`.
2. Translate it from the same path in `docs/zh_CN`, using the terms in [docs/glossary.md](docs/glossary.md).
3. Keep headings, code blocks, tables and anchors in the same structure as the Chinese page.

## Related packages

The [KM02G SDK](https://github.com/AnykaMicro/sdk-km02g) contains the Linux demo application and OTA build scripts. Follow [Build Environment Setup](docs/en/software/board/build-environment.md) to download the original V1.00 cross toolchain from SiFli, verify it and build the images.

The Anyka_Glasses companion app, the AK1090 firmware and the reference board's hardware design files have not been published with this release. They can be added in a later release when the developer makes them available.

## Licence

[Apache License 2.0](LICENSE)

---

# AnykaVision AI 文档

[English](#anykavision-ai-documentation) | 简体中文

**AnykaVision AI V1.00** 文档。AnykaVision AI 是基于安凯 KM02G 系列（图像 SoC）与 AK1090 系列（蓝牙音频 SoC）芯片的 AI 拍摄眼镜开发平台。

- **文档版本：** 1.0.0
- **网站：** <https://anyka-micro.github.io/anykavision-ai-docs-public/>（待发布；Pages 部署目前处于关闭状态）
- **语言：** 简体中文（完整）与英文（翻译中）

## 仓库结构

```
docs/
├── conf.py        两种语言共用的 Sphinx 配置
├── _templates/    语言切换及 hreflang 链接
├── index.html     站点根目录的语言选择页
├── glossary.md    中英术语表（供翻译使用）
├── zh_CN/         中文源文档（基准版本）
└── en/            英文翻译，文件路径与 zh_CN 一致
tools/
├── check_links.py           相对链接检查（CI 在构建后运行）
└── check_api_vs_headers.py  对比 API 参考与 SDK 头文件（仅输出报告）
requirements.in    顶层依赖；requirements.txt 为带哈希的锁定安装列表
```

英文页面直接引用 `docs/zh_CN` 下的图片，每张图片只保存一份。

## 本地构建

```bash
python3 -m venv .venv
.venv/bin/pip install --require-hashes -r requirements.txt
.venv/bin/sphinx-build -W -c docs -D language=en docs/en _build/html/en
.venv/bin/sphinx-build -W -c docs -D language=zh_CN docs/zh_CN _build/html/zh_CN
cp docs/index.html _build/html/
python3 tools/check_links.py . _build/html
```

然后打开 `_build/html/index.html`。请同时构建两种语言，语言切换链接依赖两者。仍待安凯处理的内容（已移除的图片、需要改写的文字）保留在源文件中，但不会出现在站点上；在 `sphinx-build` 命令中加上 `-t anyka_review` 即可查看。GitHub Actions 会在每个拉取请求以及推送到 `main` 时执行相同的构建和链接检查。在正式发布前，GitHub Pages 部署处于关闭状态；开启后，在英文翻译经指定审阅人确认之前只部署中文站点（见 `.github/workflows/pages.yml` 中的 `PUBLISH_LANGS`）。

## 参与翻译

1. 在 `docs/en` 中选择标记为“Translation pending”的页面。
2. 对照 `docs/zh_CN` 中相同路径的页面进行翻译，术语请参考 [docs/glossary.md](docs/glossary.md)。
3. 标题、代码块、表格和锚点的结构须与中文页面保持一致。

## 相关软件包

[KM02G SDK](https://github.com/AnykaMicro/sdk-km02g) 已公开，包含 Linux 示例应用和 OTA 打包脚本。思澈下载站提供 V1.00 原始交叉工具链，下载、校验和生成镜像的命令见[编译环境配置](docs/zh_CN/software/board/build-environment.md)。

Anyka_Glasses 配套 APP、AK1090 固件以及产品板硬件设计资料尚未随本次版本发布。开发者提供这些资料后，可在后续版本中补充。

## 许可证

[Apache License 2.0](LICENSE)
