# 作业描述

## 使用 Clang Static Analyzer 发现漏洞

假设我们处在软件开发上线的最后一个流程，现在需要你对源代码进行安全审计。如果是较小的代码库，可以采用规则匹配和人工分析的方式；但如果面对较大的代码库（例如 OpenSSL），则需要采用静态分析器了。

目前主流的 C/C++ 静态分析器[^1]有 Clang Static Analyzer，Facebook Infer 和 SVF-tools。相对来说，Clang Static Analyzer 更为新手友好，也更容易分析大型软件。

### 运行

使用如下命令查看 Clang Static Analyzer 内置的 checker：

```bash
clang -cc1 -analyzer-checker-help
```

使用 checker 可以检测代码中的问题，以如下代码为例：

```c
{{#include divide_zero.c}}
```

使用如下命令检测：

```bash
clang -cc1 -analyze -analyzer-checker=core.DivideZero zero.c
```

当面对真实项目的复杂代码仓库时，LLVM 还提供了 [`scan-build`](https://clang-analyzer.llvm.org/scan-build.html) 这样的命令行工具。它可以自动地识别构建过程中的编译命令，并透明地将静态分析器插入到编译的流程中，随后将可视化的分析结果集成到 html 页面当中。

### 要求

现在，需要你使用的 checker 检测出**真实世界**代码中的漏洞（表现为已经获取 CVE 编号的漏洞），并尽可能详细地分析漏洞的成因和 checker 的报告结果。

如果把代码分析工具比喻成锤子，把漏洞比喻为钉子，我们可以有以下两种寻找分析世界漏洞的思路：

- **先找锤子，再找钉子**：先选择自己熟悉的某一类漏洞，从 [Available Checkers](https://clang-analyzer.llvm.org/available_checks.html) 中找到合适的 checker，再从 [官方 CVE 列表](https://www.cve.org) 或者 [第三方 CVE 列表](https://ubuntu.com/security/cves) 中根据漏洞类型的关键词搜索到历史漏洞。
  - 以 core.DivideZero checker 为例
  - 先以 "divide by zero" 为关键词搜索，发现 [libtiff](https://gitlab.com/libtiff/libtiff) 最近披露的两个漏洞：[CVE-2022-0909](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0909) 和 [CVE-2022-2056](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2056)。使用 core.DivideZero checker 尝试进行分析发现对应的结果，发现与 CVE 所报告的漏洞位置对应（注意 `git checkout` 到对应的 `commit`）。
  - 分析同一函数 `computeOutputPixelOffsets()` 中的 [CVE-2022-2057](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2057) 和 [CVE-2022-2058](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-2058) 的类似漏洞，进一步思考造成漏报的原因。
  - 分析报告结果中没有被认定为 CVE 的问题代码，验证其是否为误报。
  - 分析的详细结果见 [libtiff.md](https://github.com/cascades-sjtu/nis7021-labs/blob/main/src/lab2/libtiff.md)

- **先找钉子，再找锤子**：使用 [Ubuntu Pro](https://ubuntu.com/pro) 查找系统中包含的带有未修复 CVE 漏洞的软件包，根据该软件包中的某个历史漏洞，针对性地选取 checker 进行分析，并对比打 patch 前后的分析结果。
  - 使用 Ubuntu Pro 官方[提供的步骤](https://ubuntu.com/pro/beta)配置
  - 扫描本机的安装包，发现 python 和 fish 两个软件包存在安全更新
  - 进一步通过 `apt source` 下载源代码查看 CVE 编号，分别为 [CVE-2022-20001](https://ubuntu.com/security/CVE-2022-20001)，[CVE-2021-4189](https://ubuntu.com/security/CVE-2021-4189)，[CVE-2022-0931](https://ubuntu.com/security/CVE-2022-0931)
  - 发现均为逻辑漏洞，且发生在 Python 和 fish shell 语言中，无法用 CSA 检测

每位同学都需要自行完成上述调研工作，并根据选好的漏洞 [**填写问卷**](https://wj.sjtu.edu.cn/q/msx7677i) 报给助教，避免雷同。当然，如果你志在发现 **0Day** 的漏洞或有相关经验，就不需要按照上面的流程，且会有酌情加分。

### 建议

- 按照命名和介绍来选择合适的 checker，先运行官方提供的测试代码，理解 checker 行为
- 使用 [`CodeChecker`](https://clang-analyzer.llvm.org/codechecker.html) 更加详细地展现 checker 的分析结果

## 使用 LLVM Pass 防护漏洞

我们已经学会了发现软件漏洞的方法，但这对于整个安全开发流程来说还远远不够。下一步，我们需要对发现的漏洞进行防护。当然，防护方案可以工作在不同的抽象层面，其可扩展性，运行阶段和开销也不同。考虑到和实验一的延续性，我们选择可以防护在 RISC-V 上运行的程序的方案。

PS：从技术的角度上来说，我们是通过程序插桩（Instrumentation）的技术来进行防护，从而以下的讨论也适用于插桩技术

AFAIK，软件防护（以及代表性工具）有以下三类：

- 源代码级别（**编译时防护**）：使用 [`clang-tidy`](https://clang.llvm.org/extra/clang-tidy/#clang-tidy) 提供的 `-fix` 参数，匹配 C/C++ 代码的 AST Nodes，对代码进行字符串级别的修改
- 中间语言（IR）级别（**编译时防护**）：使用 LLVM Transformation Pass，在 `Function` 或者 `Module` 级别操作 CFG 和 修改 IR，产生新的 IR 独立于后端架构
- 二进制级别（**运行时防护**）：Intel Pin / Valgrind / Dynamorio，针对特定的架构（如 x86_64）进行运行时防护，暂时没有针对 RISC-V 的类似工具（但有相关的移植工作）

以上方案中，LLVM Pass 可以说是相关资料最多，可扩展性最强的。LLVM Pass 主要分为 Analysis / Tranformation 两种，考虑到我们是用于软件防护，而不是程序分析，**所以使用 Transformation Pass 来修改原有的代码，添加我们用于防护的代码**。

### 运行

操作系统：Ubuntu-22.04 x86_64，软件环境与实验一类似（请使用包管理器安装的 `clang`）

#### 运行 LLVM Pass

Pass 的运行对象是 Clang 编译过程中产生的中间语言。以 [New Pass Manager](https://llvm.org/docs/NewPassManager.html) 为例，可以使用如下命令来运行一个 LLVM Pass：

```bash
# 生成文本格式的 LLVM IR，这里指定优化很关键
$LLVM_DIR/bin/clang -O1 -S -emit-llvm test.c -o test.ll
# 对 IR 运行以插件形式加载的 Pass，讲插桩后的 IR 保存到新的文件中
$LLVM_DIR/bin/opt -load-pass-plugin ./libHelloWorld.{so|dylib} -passes=hello-world test.ll -S -o test_instrumented.ll
```

#### 生成 RISC-V 架构的二进制文件

以编译 Juliet Test Suite（见下文）中的某一类漏洞的某一个源代码文件为例，我们先将其单独编译为 RISC-V 架构的二进制文件，查看程序的正常行为：

```bash
cd C/testcases/CWE457_Use_of_Uninitialized_Variable/s01
# clang 交叉编译
clang --static --target=riscv64-linux-gnu --sysroot=/usr/lib/riscv64-linux-gnu -DINCLUDEMAIN -I ../../../testcasesupport/ ../../../testcasesupport/io.c CWE457_Use_of_Uninitialized_Variable__int_01.c -o CWE457_Use_of_Uninitialized_Variable__int_01
```

运行结果如下：

```bash
# 使用 qemu-riscv64 运行
testcases/CWE457_Use_of_Uninitialized_Variable/s01 ❯ qemu-riscv64 CWE457_Use_of_Uninitialized_Variable__int_01
Calling good()...
5
5
Finished good()
Calling bad()...
0
Finished bad()
```

我们也可以先将源代码生成文本形式的 LLVM IR：

```bash
# 生成 IR 文件
clang -DINCLUDEMAIN -I ../../../testcasesupport/ -emit-llvm -S ../../../testcasesupport/io.c  CWE457_Use_of_Uninitialized_Variable__int_01.c
# 查看产生的 IR 文件
ll *.ll
```

此时，我们可以直接使用 [`lli`](https://www.llvm.org/docs/CommandGuide/lli.html) 以 JIT 的形式来运行 LLVM IR （运行多个 LLVM IR 文件时需要 [`wllvm`](https://github.com/travitch/whole-program-llvm) 的支持）；也可以在经过 LLVM Pass 的处理后进一步生成二进制程序

```bash
# 将 IR 文件转化为 RISC-V 汇编指令
llc --march=riscv64 --mcpu=generic-rv64 --mattr=+f,+d CWE457_Use_of_Uninitialized_Variable__int_01.ll
llc --march=riscv64 --mcpu=generic-rv64 --mattr=+f,+d io.ll
# 将汇编指令生成二进制程序
riscv64-linux-gnu-gcc --static CWE457_Use_of_Uninitialized_Variable__int_01.s io.s
```

类似地，通过 `qemu-riscv64` 来运行该二进制程序

### 要求

AFAIK，现在基于 RISC-V 架构开发的开源 C/C++ 项目不算多，所以我们将防护的对象放到人为构造的软件漏洞数据集上。

[Juliet Test Suite for C/C++](https://samate.nist.gov/SARD/test-suites/112)  是 NIST 推出的，用于评估源代码/二进制分析工具的数据集。Juliet 其按照通用漏洞类型 [CWE](https://cwe.mitre.org) 进行组织，并为每一类漏洞提供了大量的测试代码和编译脚本。

每位同学需要在 Juliet 中**选择一类漏洞中的某一个文件**进行防护（可以选择自己较为熟悉的漏洞）。防护的流程如下：

1. 先将测试文件编译成 LLVM IR
2. 对 LLVM IR 运行 LLVM Pass，生成新的 LLVM IR
3. 使用 [`llc`](https://www.llvm.org/docs/CommandGuide/llc.html) 将经过插桩后的 LLVM IR 生成 RISC-V 架构的汇编代码
4. 将汇编代码编译为二进制程序，使用实验一中的 `qemu-riscv64` 运行
5. 将运行的结果与直接编译生成的 RISC-V 程序进行对比，体现防护功能

PS：LLVM 还提供了 [MachineFunctionPass](https://llvm.org/doxygen/classllvm_1_1MachineFunctionPass.html) 供开发者在后端代码生成时进行插桩，感兴趣的同学可以深入研究

### 建议

- 使用助教提供的脚本自动生成 LLVM Pass 的模板，专注于代码逻辑而不是 Pass 的运行机制
- 学习 llvm-tutor 中的代码
- [学习 LLVM IR 的语法](https://github.com/Evian-Zhang/llvm-ir-tutorial)
- 阅读 LLVM 官方提供的 [Pass](https://github.com/llvm/llvm-project/tree/main/llvm/lib/Transforms)，它们已经被集成到了 `opt` 中，可以通过 `opt -h` 查看
- 学习现有的内存泄漏检测 / 系统防护机制，设计防护手段
- 一些使用 LLVM Pass 进行防护的例子：
  - [SafeStack](https://clang.llvm.org/docs/SafeStack.html#known-compatibility-limitations)
  - [Sanitizers](https://github.com/google/sanitizers)

{{#include ../star.md}}

[^1]: http://www.jos.org.cn/jos/article/abstract/6569
