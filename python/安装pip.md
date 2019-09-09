# 安装pip 

不知道为什么pip 不见了

然后重新安装一下

[官网](https://pip.pypa.io/en/stable/installing/#installing-with-get-pip-py)

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py --user
```

> WARNING: The script wheel is installed in '/home/blime/.local/bin' which is not on PATH.
>   Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.

然后将/home/blime/.local/bin 加入到环境变量中

```
sudo vim ~/.zshrc
```

```
export PATH=/home/blime/.local/bin:$PATH
```

```
source ~/.zshrc
```

