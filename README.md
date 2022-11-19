### 此项目为爬取云南网的爬虫

### 安装python

直接从官网下载安装 https://www.python.org/ 。请用安装器，以免还要设置路径。

### 安装scrapy

```shell
pip install scrapy
```

### 在pycharm中运行

首先打开项目文件。然后设置一个项目脚本运行。

[![zKpPDx.md.png](https://s1.ax1x.com/2022/11/19/zKpPDx.md.png)](https://imgse.com/i/zKpPDx)

点击edit configuration

[![zKpE5D.md.png](https://s1.ax1x.com/2022/11/19/zKpE5D.md.png)](https://imgse.com/i/zKpE5D)

按照按照上图所示设置项目脚本

### 用命令行运行
到`yunnannews/yunnannews/spiders`目录下，运行下面那个命令行。这里不一定是这个文件，你可以自己设置。

```shell
scrapy runspider homepage_news.py
```

### 参考资料

[scrapy实战案例之 — 抓取腾讯新闻（手把手带你练习）](https://www.bilibili.com/video/BV14s411w75R/)

[How to obtain href values from a div using xpath?](https://stackoverflow.com/questions/4064177/how-to-obtain-href-values-from-a-div-using-xpath)
