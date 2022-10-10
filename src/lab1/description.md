# 作业描述

## RISC-V 汇编

编写一段 RISC-V 汇编代码，实现下面的 C 语言程序功能，并运行在 `qemu-riscv64` 中

```c
{{#include inner_product.c}}
```

### 运行

操作系统：Ubuntu-20.04 x86_64

编写的汇编代码保存在 `inner_product.s` 中，运行命令如下：

```bash
riscv64-linux-gnu-gcc -static inner_product.s -o inner_product
qemu-riscv64 ./inner_product
echo $?
```

### 要求

- 基于递归
- 在汇编语言层面上实现函数的 prologue 和 epilogue，实现 stack 内存管理

### 建议

- 先使用在线编译工具，理解 x86_64 下汇编实现的原理，然后改写成 RISC-V 指令
- 不建议直接编译得到 RISC-V 汇编代码，因为你对代码的理解将会体现在你的报告中
- ~~当然，如果你直接编译得到 RISC-V 汇编代码，助教也暂时没法儿自动检测出来~~

[![godbolt](godbolt.png)](https://godbolt.org/z/E3nsTYxqs)

## RISC-V 逆向

给定二进制代码，分析其包含的加解密函数，编写功能相同的 C 代码，并运行在 `qemu-riscv64` 中

二进制文件地址：<https://github.com/cascades-sjtu/nis7021-labs/blob/main/src/lab1/libcrypto.a>

### 运行

操作系统：Ubuntu-20.04 x86_64

编写的源代码保存在 crypto.c 中，测试代码 crytpo_test.c 由助教提供，代码如下：

```c
{{#include crypto_test.c}}
```

运行命令如下：

```bash
riscv64-linux-gnu-gcc -c -o crypto.o crypto.c
riscv64-linux-gnu-ar crv libcrypto.a crypto.o
riscv64-linux-gnu-gcc -static -o crypto_test crypto_test.c -L. -lcrypto
qemu-riscv64 ./crypto_test
```

### 要求

- 仔细分析汇编指令的功能，体现在报告中

### 建议

- 加解密函数参考：<https://github.com/B-Con/crypto-algorithms>
