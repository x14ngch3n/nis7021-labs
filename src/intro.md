# 使用说明

## 如何阅读本手册

本手册使用 [mdBook](https://rust-lang.github.io/mdBook/index.html) 编写，阅读方法可以参考[官方文档](https://rust-lang.github.io/mdBook/guide/reading.html)。

## 如何构建本手册

- 使用 [`mdbook serve`](https://rust-lang.github.io/mdBook/cli/serve.html) 进行本地阅览

```bash
cargo install mdbook
git clone https://github.com/cascades-sjtu/nis7021-labs.git
cd nis7021-labs
mdbook serve --open
```

- 使用 [`mdbook-pdf`](https://github.com/HollowMan6/mdbook-pdf/) 生成 PDF 文件

```bash
cargo install mdbook-pdf
git clone https://github.com/cascades-sjtu/nis7021-labs.git
cd nis7021-labs
mdbook build
open ./book/pdf/output.pdf
```

- 直接在 [Github Release](https://github.com/cascades-sjtu/nis7021-labs/releases) 中下载 PDF 文件

## 如何反馈手册 / 作业问题

- 点击右上角 `Suggest an edit` 键，进入 [`Github Issues`](https://github.com/cascades-sjtu/nis7021-labs/issues/new/choose)

PS：手册制作不易，有问题的地方请大家多多包涵，也欢迎批评交流，发现问题可酌情加分～
