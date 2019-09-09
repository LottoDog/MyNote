# manjaro 科学上网，zsh,oh-my-zsh



### 安装zsh

```
sudo  pacman -S zsh
```

### 安装lantern

```
yaourt lantern
```

因为oh-my-zsh安装需要科学上网一下，用lantern帮帮忙

### 安装 oh-my-zsh

```
wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh
sh install.sh
```





### 查看已有的shell

```
cat /etc/shells
```

### 查看当前shell

```
echo $SHELL
```

### 使用zsh替换bash（重新打开终端生效）

```
chsh -s /bin/zsh
```

### 查看zsh版本

```
zsh --version
```

### ——还原bash（需要重启）

```
chsh -s /bin/bash
```

[剩下的](https://blog.csdn.net/weixin_43968923/article/details/86663001#_zsh_2)

