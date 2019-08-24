# manjaro pacman基础命令

```
sudo pacman -Syy                   # 强制更新包数据

sudo pacman -Syyu                  # 强制更新包数据，同时更新软件

sudo pacman -Syu                   # 升级整个系统，y是更新数据库，yy是强制更新，u是升级软件

sudo pacman -Ss string             # 在包数据库中查询软件

sudo pacman -Si package_name       # 显示软件的详细信息

sudo pacman -Sc                    # 清除软件缓存，即/var/cache/pacman/pkg目录下的文件

sudo pacman -R package_name        # 删除单个软件

sudo pacman -Rs package_name       # 删除指定软件及其没有被其他已安装软件使用的依赖关系

sudo pacman -Qs string             # 查询已安装的软件包

sudo pacman -Qi package_name       # 查询本地安装包的详细信息

sudo pacman -Ql package_name       # 获取已安装软件所包含的文件的列表

sudo pacman -U package.tar.zx      # 从本地文件安装

sudo pactree package_name          # 显示软件的依赖树
```







```
yay -c  # 卸载所有无用的依赖。类比 apt-get autoremove
```







## 参考链接

- [Arch Linux Wiki - 中文](https://wiki.archlinux.org/index.php/Main_page_(简体中文))
- [AUR 仓库](https://aur.archlinux.org/packages)
- [Arch Linux 中文社区仓库](https://www.archlinuxcn.org/archlinux-cn-repo-and-mirror/)
- [yay - Yet another Yogurt - An AUR Helper written in Go](https://github.com/Jguer/yay)
- [安装Manjaro之后的配置](https://panqiincs.me/2019/06/05/after-installing-manjaro/)