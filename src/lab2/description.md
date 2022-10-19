# 作业描述

## 使用 Clang Static Analyzer 发现漏洞

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

### 要求

现在，需要你使用的 checker 检测出**真实世界**代码中的漏洞，并尽可能详细地分析漏洞的成因和 checker 的报告结果

如果把代码分析工具比喻成锤子，把漏洞比喻为钉子，我们可以有以下两种寻找分析世界漏洞的思路：

- **先找锤子，再找钉子**：先选择自己熟悉的某一类漏洞，从 [Available Checkers](https://clang-analyzer.llvm.org/available_checks.html) 中找到合适的 checker，再从 [官方 CVE 列表](https://www.cve.org) 或者 [第三方 CVE 列表](https://ubuntu.com/security/cves) 中根据漏洞类型的关键词搜索到历史漏洞
- **先找钉子，再找锤子**：使用 [Ubuntu Pro](https://ubuntu.com/pro) 查找系统中包含的带有未修复 CVE 漏洞的软件包，根据该软件包中的某个历史漏洞，针对性地选取 checker 进行分析，并对比打 Patch 前后的分析结果

每位同学都需要自行完成上述调研工作，并根据选好的漏洞 [**填写问卷**](https://wj.sjtu.edu.cn/q/msx7677i) 报给助教，避免雷同

TODO: 两种方法都添加一个例子，规定自选漏洞类别

### 建议

- 按照命名和介绍来选择合适的 checker，先运行官方提供的测试代码，理解 checker 行为
- 使用 [`scan-build`](https://clang-analyzer.llvm.org/scan-build.html) 或者 [`CodeChecker`](https://clang-analyzer.llvm.org/codechecker.html) 来分析整个项目的代码，并可视化地展现 checker 的分析流程

## 使用 Intel Pin 防护漏洞

### 运行

以 MyPinTool 为例编译一个 64 位的 PinTool，运行命令如下：

```bash
make -C source/tools/MyPinTool
./pin -t ./source/tools/MyPinTool/obj-intel64/MyPinTool.so -o MyPinTool.out -- /bin/ls
```

可以在 MyPinTool.out 中查看插桩分析结果：

```ascii
===============================================
MyPinTool analysis results:
Number of instructions: 406205
Number of basic blocks: 77720
Number of threads: 1
===============================================
```

后续的开发也可以直接在 MyPinTool.cpp 上进行

### 要求

针对 Clang Static Analyzer 发现的漏洞，编写你的 PinTool，进行防护

### 建议

- 阅读 [Tutorials](https://www.intel.com/content/www/us/en/developer/articles/tool/pin-a-dynamic-binary-instrumentation-tool.html#inpage-nav-5)，大概了解 Pin 的工作原理
- 参考其他内存检测工具 / 系统防护手段的原理，设计防护方案
- 阅读 Pin 官方提供的 [Example PinTools](https://software.intel.com/sites/landingpage/pintool/docs/98612/Pin/doc/html/index.html#EXAMPLES)，学习编写流程，熟悉 API 的使用，代码在 `source/tools/ManualExamples` 目录下

{{#include ../star.md}}
