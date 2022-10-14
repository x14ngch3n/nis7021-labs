# 前置知识

## RISC-V 汇编

- RISC-V 汇编语言基础：
  - [RISC-V Instruction Set Manual](https://github.com/riscv/riscv-isa-manual)
  - [RISC-V Assembly Programmer's Manual](https://github.com/riscv-non-isa/riscv-asm-manual/blob/master/riscv-asm.md)
- 如何编写一个 RISC-V 程序：
  - [RISC-V Support](https://marketplace.visualstudio.com/items?itemName=zhwu95.riscv)
  - [Compiler Explorer](https://godbolt.org/)
- 如何编译一个 RISC-V 程序：
  - [RISC-V GNU Compiler Toolchain](https://github.com/riscv-collab/riscv-gnu-toolchain)
  - [Ubuntu Package: gcc-riscv64-linux-gnu](https://packages.ubuntu.com/search?keywords=gcc-riscv64-linux-gnu)
- 如何运行一个 RISC-V 程序：
  - [emulsiV - Simulator for Virgule, a minimal processor based on the RISC-V architecture](http://tice.sea.eseo.fr/riscv/)
  - [QEMU User Mode Emulation](https://qemu.readthedocs.io/en/latest/user/index.html)

## RISC-V 逆向

- 如何静态分析一个 RISC-V 程序：
  - [`file`](https://www.man7.org/linux/man-pages/man1/file.1.html)
  - [Ubuntu Package: binutils-riscv64-linux-gnu](https://packages.ubuntu.com/bionic/binutils-riscv64-linux-gnu)
  - [Ghidra](https://ghidra-sre.org)
- 如何动态分析一个 RISC-V 程序：
  - [`qemu-riscv64 -g`](https://www.qemu.org/docs/master/user/main.html?highlight=gdb#command-line-options)
  - [`riscv64-unknown-elf-gdb`](https://sourceware.org/gdb/onlinedocs/gdb/Connecting.html)
