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

现在，需要你找到合适的 checker 检测出如下代码中的问题，并尽可能详细地分析问题的成因和 checker 的报告结果

TODO: 添加被分析代码的链接

### 建议

- 按照命名和介绍来选择合适的 checker，先运行官方提供的测试代码，理解 checker 行为
- 使用 [`scan-build`](https://clang-analyzer.llvm.org/scan-build.html) 可视化地展现 checker 的分析流程

## 使用 Intel Pin 防护漏洞

### 运行

以 MyPinTool 为例编译一个 64 位的 PinTool，运行命令如下：

```bash
make -C source/tools/MyPinTool
./pin -t ./source/tools/MyPinTool/obj-intel64/MyPinTool.so -o MyPinTool.out -- /bin/ls
```

可以在 MyPinTool.out 中查看插桩分析结果：

```ascii
{{#include MyPinTool.out}}
```

后续的开发也可以直接在 MyPinTool.cpp 上进行

### 要求

根据 Clang Static Analyzer 发现的漏洞，编写你的 PinTool，进行防护

### 建议

- 阅读 [Tutorials](https://www.intel.com/content/www/us/en/developer/articles/tool/pin-a-dynamic-binary-instrumentation-tool.html#inpage-nav-5)，大概了解 Pin 的工作原理
- 参考其他内存检测工具 / 系统防护手段的原理，设计防护方案
- 阅读 Pin 官方提供的 [Example PinTools](https://software.intel.com/sites/landingpage/pintool/docs/98612/Pin/doc/html/index.html#EXAMPLES)，学习编写流程，熟悉 API 的使用，代码在 `source/tools/ManualExamples` 目录下
