# conda 更改镜像源

添加国内源：

```
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/freeconda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/mainconda config --set show_channel_urls yes
```

换回默认源：

```
conda config --remove-key channels
```

在执行conda config 命令的时候
会在当前用户目录下创建 .condarc  文件，可以查看更换源前后该文件内容的变化。

