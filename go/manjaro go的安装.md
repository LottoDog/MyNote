# manjaro go的安装

[TOC]

[参考链接](https://blog.csdn.net/ggq89/article/details/82682171#2__Go__35)

> 挺感谢上面的链接的

## 1.手动安装 Go

- 1.下载Go发行版

从官方地址：https://golang.org/dl/ 上下载合适的 二进制发行版 (例如: go1.10.7.linux-amd64)：

```
wget https://dl.google.com/go/go1.12.7.linux-amd64.tar.gz
```

>【2019.8.6】
>
>会超级无敌慢到不行，连接超时，需要科学上网

这里是我上传到百度网盘的分享，有[pandownload](https://pan.baiduwp.com/)下载有奇速

链接: https://pan.baidu.com/s/14GjsNpLxgNPs0JFmCc_weg 提取码: 1234 



+ 2.提取压缩包

提取压缩包到合适的目录(例如官方推荐的: /usr/local )：

```
sudo tar -xzf go1.10.7.linux-amd64.tar.gz -C /usr/local
```



+ 3.建立软链接

```
sudo ln -s /usr/local/go/bin/* /usr/bin/
```

可以运行如下命令，验证是否安装成功：

```
go version
```

正常输出则说明安装成功，同时可以检查版本是否安装正确。



## 2. 设置 Go 开发环境

使用 vi 编辑环境变量配置文件 $HOME/.bashrc ：

sudo vim $HOME/.bashrc

> 如果是zsh,就把/.bashrc 改成 /.zshrc

```bash
sudo vim $HOME/.bashrc
```

进入编辑界面后 Shift+G 跳转至尾行，按 o 新插入一行，输入如下：

```bash
export GOROOT=/usr/local/go  #设置为go安装的路径，有些安装包会自动设置默认的goroot
export GOPATH=$HOME/go-work   #默认安装包的路径
export PATH=$PATH:$GOROOT/bin:$GOPATH/bin
```

之后按 Esc 键，: wq 保存退出。使配置文件生效：

```bash
source $HOME/.bashrc　　#注：这里不要用sudo执行，sudo无该命令
```

可运行 go env 查看gol环境变量：

```bash
go env
```

正常输出则说明配置成功，同时可对环境变量设置进行校验：

>GOARCH="amd64"
>GOBIN=""
>GOCACHE="/home/blime/.cache/go-build"
>GOEXE=""
>GOFLAGS=""
>GOHOSTARCH="amd64"
>GOHOSTOS="linux"
>GOOS="linux"
>GOPATH="/home/blime/go-work"
>GOPROXY=""
>GORACE=""
>GOROOT="/usr/local/go"
>GOTMPDIR=""
>GOTOOLDIR="/usr/local/go/pkg/tool/linux_amd64"
>GCCGO="gccgo"
>CC="gcc"
>CXX="g++"
>CGO_ENABLED="1"
>GOMOD="/home/blime/go.mod"
>CGO_CFLAGS="-g -O2"
>CGO_CPPFLAGS=""
>CGO_CXXFLAGS="-g -O2"
>CGO_FFLAGS="-g -O2"
>CGO_LDFLAGS="-g -O2"
>PKG_CONFIG="pkg-config"
>GOGCCFLAGS="-fPIC -m64 -pthread -fmessage-length=0 -fdebug-prefix-map=/tmp/go-build988083162=/tmp/go-build -gno-reco
>rd-gcc-switches"



## 3. 测试 Go 源码实例

通过构建一个简单的程序来检查Go的安装是否正确，具体操作如下：

首先创建一个名为 hello.go 的文件，并将以下代码保存在其中：

```go
package main

import "fmt"

func main() {
    fmt.Printf("hello, world\n")
}
```

接着通过 go 工具运行它：

```bash
go run hello.go
```

若看到了“hello, world”信息，那么Go已被正确安装。





## 4.卸载 Go

卸载Go，其实就是将前面安装Go的东西全部删除：

+ 1.删除 go 目录：

    sudo rm -rf /usr/local/go

+ 2.删除软链接：

    sudo rm -rf /usr/bin/go



## 5.升级 Go 版本

升级 Go 版本其实就是， 按照前面的步骤:

+ 卸载之前安装的旧版本Go
+ 再安装新版本的Go。