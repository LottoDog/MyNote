# go 拓展包离线安装 【简单有用】

1. ## 获取golang.org/x/tools包

```
git clone https://github.com/golang/tools $GOPATH/src/golang.org/x/tools
```

2. ## git clone 拓展包

```bash
cd $GOPATH/src/

# git clone 要下载的包 ，下面举几个例子

git clone https://github.com/bytbox/golint.git
go install golint/

# 完成
```





补充

| 安装的组件                                                  | 默认安装状态 | 组件备注                                         | github.com->golang.org          |
| ----------------------------------------------------------- | ------------ | ------------------------------------------------ | ------------------------------- |
| go get -u -v github.com/nsf/gocode                          | SUCCEEDED    | 自动补全                                         |                                 |
| go get -u -v github.com/uudashr/gopkgs/cmd/gopkgs           | SUCCEEDED    | 自动补全未导入的包                               |                                 |
| go get -u -v github.com/ramya-rao-a/go-outline              | SUCCEEDED    | 当前文件中按符号搜索                             | https://github.com/golang/tools |
| go get -u -v github.com/acroca/go-symbols                   | SUCCEEDED    | 当前workspace中按符号搜索                        |                                 |
| go get -u -v golang.org/x/tools/cmd/guru                    | SUCCEEDED    | 查找所有引用组件                                 |                                 |
| go get -u -v golang.org/x/tools/cmd/gorename                | SUCCEEDED    | 重命名符号                                       |                                 |
| go get -u -v github.com/fatih/gomodifytags                  | SUCCEEDED    | 修改结构上的标签                                 |                                 |
| go get -u -v github.com/haya14busa/goplay/cmd/goplay        | SUCCEEDED    | for running current file in the Go playground    |                                 |
| go get -u -v github.com/josharian/impl                      | SUCCEEDED    | for generating stubs for interfaces              |                                 |
| go get -u -v github.com/davidrjenni/reftools/cmd/fillstruct | SUCCEEDED    | for filling a struct literal with default values |                                 |
| go get -u -v github.com/rogpeppe/godef                      | SUCCEEDED    | 转到定义2                                        |                                 |
| go get -u -v golang.org/x/tools/cmd/godoc                   | SUCCEEDED    | 鼠标悬停显示文档注释2                            |                                 |
| go get -u -v sourcegraph.com/sqs/goreturns                  | SUCCEEDED    | 格式化代码2                                      |                                 |
| go get -u -v github.com/golang/lint/golint                  | SUCCEEDED    | for linting                                      | https://github.com/golang/lint  |
| go get -u -v github.com/cweill/gotests/...                  | SUCCEEDED    | 生成单元测试                                     |                                 |
| go get -u -v github.com/derekparker/delve/cmd/dlv           | SUCCEEDED    | 调试                                             |                                 |
| go get -u -v github.com/zmb3/gogetdoc                       |              | 转到定义2/鼠标悬停显示注释2                      |                                 |
| go get -u -v golang.org/x/tools/cmd/goimports               |              | 格式化代码2                                      |                                 |





[参考链接](https://www.cnblogs.com/justdoyou/p/9853520.html)





```
go get -u -v github.com/ramya-rao-a/go-outline
go get -u -v github.com/acroca/go-symbols
go get -u -v github.com/mdempsky/gocode
go get -u -v github.com/rogpeppe/godef

go get -u -v github.com/zmb3/gogetdoc

go get -u -v github.com/fatih/gomodifytags

go get -u -v github.com/cweill/gotests/...

go get -u -v github.com/josharian/impl
go get -u -v github.com/haya14busa/goplay/cmd/goplay
go get -u -v github.com/uudashr/gopkgs/cmd/gopkgs
go get -u -v github.com/davidrjenni/reftools/cmd/fillstruct
go get -u -v github.com/alecthomas/gometalinter
gometalinter --install
```

