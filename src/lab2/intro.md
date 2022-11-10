# Lab2 软件漏洞分析 / 防范

本实验参考 [2021 年秋季学期 NIS7021 作业二实验一](https://notes.sjtu.edu.cn/s/Y08NaP_QS)，有以下改动：

- 分析真实世界的漏洞，灵感来自于 [《Ubuntu Pro 现在免费为你提供 10 年的安全更新》](https://linux.cn/article-15120-1.html)
- 使用 LLVM Pass 在 LLVM IR 层面进行代码防护，从而支持防护 RISC-V 架构的程序
