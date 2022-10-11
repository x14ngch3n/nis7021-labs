# nis7021-labs

Homepage for SJTU NIS7021 labs documentation

## Usage

Reading Books: <https://rust-lang.github.io/mdBook/guide/reading.html>

## Deployment

Use [`mdbook serve`](https://rust-lang.github.io/mdBook/cli/serve.html) to view the book locally.

```bash
cargo install mdbook
git clone https://github.com/cascades-sjtu/nis7021-labs.git
cd nis7021-labs
mdbook serve --open
```

Or use [`mdbook-pdf`](https://github.com/HollowMan6/mdbook-pdf/) to generate the PDF version of book.

```bash
cargo install mdbook-pdf
git clone https://github.com/cascades-sjtu/nis7021-labs.git
cd nis7021-labs
mdbook build
open ./book/pdf/output.pdf
```

Or just download the PDF from [Github Release](https://github.com/cascades-sjtu/nis7021-labs/releases).
