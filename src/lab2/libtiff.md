# 使用 Clang Static Analyzer 分析 libtiff 的 FPE 漏洞

分析命令如下：

```bash
export COMMIT_ID=xxxxxxxx
git checkout $COMMIT_ID && scan-build ./configure && scan-build -o $COMMIT_ID --keep-cc make -j8
```

分析结果：

| CVE ID        | commit   | file                            | function                      | Loc  | set ID |
| ------------- | -------- | ------------------------------- | ----------------------------- | ---- | ------ |
| CVE-2022-0909 | 5e180045 | tools/tiffcrop.c                | computeOutputPixelOffsets     | 5802 | 1      |
| CVE-2022-2056 | 9752dae8 | tools/tiffcrop.c                | computeOutputPixelOffsets     | 5818 | 3      |
| CVE-2022-2057 | 19db1d31 | tools/tiffcrop.c                | computeOutputPixelOffsets     | 5936 | 1      |
| CVE-2022-2058 | 19db1d31 | tools/tiffcrop.c                | computeOutputPixelOffsets     | 5941 | 2      |
| None          | 5e180045 | contrib/addtiffo/tif_overview.c | TIFF_DownSample_Subsampled516 | 516  | 4      |

按照 commit 的时间顺序，扫描结果如下所示。实际上每次扫描的结果都是一样的，只是代码位置发生了些许变化。

- 5e180045：

![Screenshot 2022-11-16 at 09.28.25](https://tva1.sinaimg.cn/large/008vxvgGly1h86q4yiw9pj3162072abt.jpg)

- 9752dae8：

![Screenshot 2022-11-16 at 09.27.18](https://tva1.sinaimg.cn/large/008vxvgGly1h86q4vik7xj3162072abt.jpg)

- 19db1d31：

![Screenshot 2022-11-16 at 09.29.06](https://tva1.sinaimg.cn/large/008vxvgGly1h86q4wp2fdj31620700ug.jpg)

总结下来，4个 CVE 编号实际为3处代码问题，还有一处报告未被人工发现，有待后续验证

具体的分析报告见：<https://github.com/cascades-sjtu/nis7021-labs/blob/main/src/lab2/libtiff-reports.zip>
