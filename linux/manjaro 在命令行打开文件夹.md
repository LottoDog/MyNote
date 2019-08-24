# manjaro 在命令行打开文件夹



命令行输入

```
dolphin .
```

就可以了。





为了方便。

我们把它写进～/.zshrc文件中（或者你的是 ～/.bashrc)

```
sudo vim ~/.zshrc

#加入下面这句，我们用open代替

alias open='dolphin .'

#然后激活

source ~/.zshrc
```

