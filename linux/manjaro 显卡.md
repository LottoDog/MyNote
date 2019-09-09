# manjaro 显卡

# 双显卡驱动

manjaro装机之后的显卡驱动切换程序：Bumblebee还是有点问题，我们重新安装

## 1. 安装

```
# 依赖
sudo pacman -S virtualgl lib32-virtualgl lib32-primus primus

# 安装双显卡切换程序bumblebee
sudo mhwd -f -i pci video-hybrid-intel-nvidia-bumblebee

# 允许服务
sudo systemctl enable bumblebeed

# 添加用户
sudo gpasswd -a $USER bumblebee
```

## 2. 防止启动后无法进入图形界面

1. 打开 /etc/default/grub
2. 找到并且改为：GRUB_CMLINE_LINUX_DEFAULT="quiet **acpi_osi=! acpi_osi=Linux acpi_osi=’Windows 2015’ pcie_port_pm=off** resume=..."
3. 运行sudo update-grub，重启

## 3. 测试

```
# 安装测试软件
sudo pacman -S mesa-demos

# 集成显卡性能
glxgears -info

# 独显性能
optirun glxgears -info
# 或者
primusrun glxgears -info
```

之后所有需要用独显允许的程序，前面都要加上optirun或者primusrun允许

```
# 打开nvida面板
optirun -b none nvidia-settings -c :8

# 不依赖Bumblebee来使用CUDA
sudo tee /proc/acpi/bbswitch <<< 'ON'

# 使用完CUDA 停止NVIDIA显卡
sudo rmmod nvidia_uvm nvidia && sudo tee /proc/acpi/bbswitch <<< OFF
inxi -G # 查看显卡情况

optirun nvidia-smi # 查看CPU情况
```

## 4. 两种用法

1. 用bumblebee切换：
    命令前面加上 optirun 或者primusrun运行
2. 用bbswitch:

```
# 一直开启独显
sudo tee /proc/acpi/bbswitch <<< 'ON'
# 一直禁用独显
sudo tee /proc/acpi/bbswitch <<< 'OFF'
```