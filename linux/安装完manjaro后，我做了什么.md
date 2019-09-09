# 安装完manjaro后，我做了什么

我安装的是kde版

manjaro安装之后,很好看，很完善，相比ubuntu简直太完美了

[参考链接：知乎](https://zhuanlan.zhihu.com/p/43442012)

[参考链接：简书](https://www.jianshu.com/p/21c39bc4dd31)

1. 更改国内源

   ```
   sudo pacman-mirrors -i -c China -m rank
   ```

2. 更新源

   ```
   sudo pacman -Syy
   ```

3. yaourt

   ```
   sudo pacman -S yaourt
   ```

4. 中文输入法

   [链接](https://blog.csdn.net/weixin_37906376/article/details/86738124)

   这里十分不推荐使用Google拼音，因为不好用

   直接

   ```
   yaourt -S fcitx-qt4
   ```

5. 更新所有应用

   ```
   sudo pacman -Syu
   ```

6. 安装微信,tim,typora

   其他方式安装qq，都是闪退的，就下面的可以

   还可以远程操控，完美

   ```
   yaourt deepin-wine-wechat
   yaourt deepin-wine-tim
   ```

   ```
   yaourt typora
   ```

7. 下载XDM

   - 开始下载：https://sourceforge.net/projects/xdman/
   - 解压后，使用终端进入该目录， 输入**sudo ./install.sh**
   - 安装完成后打开，有个安装浏览器扩展的界面（浏览器监视），然后安装相应的浏览器的扩展
   - 将软件界面语言设置为简体中文 tool----language
   - 然后这里要按一下左上角的 exit 再次打开才会变成中文
   - 设置线程为32，工具----选项----网络设置----下载线程数32
   - 有需要也可以自己设置一下下载存放位置
   - 其他设置默认即可

8. 下载jetbrains全家桶

   [jetbrains官网](https://www.jetbrains.com/?utm_source=baidu&utm_medium=cpc&utm_campaign=cn-bai-br-brand-ex-pc&utm_content=brand-pure&utm_term=jetbrains)

   用学生帐号免费注册

   获得正版授权，下载jetbrains-toolbox

   别再找盗版注册码了，正版不要钱

   

9.  安装NVIDIA显卡驱动

   在确保能进入桌面的情况下安装：

   ```
   sudo pacman -S bumblebee bbswitch
   ```

   把用户添加到bumblebee组里：

   ```
   sudo gpasswd -a XXX bumblebee    //XXX是用户名
   ```

   启动bumblebeed服务

   ```
   sudo systemctl enable bumblebeed.service
   ```

   安装依赖

   ```
   sudo pacman -S bumblebee nvidia opencl-nvidia lib32-nvidia-utils lib32-opencl-nvidia mesa lib32-mesa-libgl xf86-video-intel
   ```

   配置bumblebee： 
   编辑`/etc/bumblebee/bumblebee.conf`，修改以下内容：

   ```
   Driver=nvidia    # 指定nvidia
   [driver-nvidia]
   PMMethod=bbswitch    # 电源管理指定bbswitch
   ```

   重启

   

10. 下载docker

- 安装docker

  ```
   sudo pacman -S docker 
  ```

- 将自己添加到docker组

  ```
   sudo gpasswd -a yourname docker
  ```

- 更新用户组

  ```
  newgrp docker
  ```

- 启动服务

  ```
   sudo systemctl start docker
  ```

- 加入开机启动

  ```
   sudo systemctl enable docker 
  ```

- 安装nvidia-docker

  ```
   sudo pacman -S yay 
   yay -S nvidia-docker 
   下载超时，科学上网以后再搞吧
  ```

- 配置docker镜像源

  ```
   sudo nano /etc/docker/daemon.json
   加入
    ”registry-mirrors”: [“http://hub-mirror.c.163.com”]
  ```

- 安装tensorflow容器

- [剩下的看链接吧](https://www.jianshu.com/p/d67ed3f95d5e)

