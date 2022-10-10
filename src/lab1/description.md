# 作业描述

## RISC-V 汇编

使用编写一段 RISC-V 汇编代码，实现下面的 C 语言程序功能，并能够运行在 `qemu-riscv64` 中

```c
{{#include inner_product.c}}
```

运行环境：Ubuntu-20.04 x86_64

运行代码：

```bash
riscv64-linux-gnu-gcc -static inner_product.s -o inner_product
qemu-riscv64 ./inner_product
echo $?
```

要求：

- 基于递归
- 在汇编语言层面上实现函数的 prologue 和 epilogue，实现 stack 内存管理

建议：

- 先使用在线编译工具，理解 x86_64 下汇编实现的原理，然后改写成 RISC-V 指令
- 不建议直接编译得到 RISC-V 汇编代码，因为你对代码的理解将会体现在你的报告中
- ~~当然，如果你直接编译得到 RISC-V 汇编代码，助教也暂时没法儿自动检测出来~~

[![godbolt](godbolt.png)](https://godbolt.org/z/E3nsTYxqs)

## RISC-V 逆向
