# manjaro tensorflow环境搭建 cuda cudnn nvidia显卡设置



因为之前安装了bumblebee来管理显卡

首先我们打开NVIDIA显卡

```
sudo tee /proc/acpi/bbswitch <<< ON
```

确认打开了

```
nvidia-smi
```

![深度截图_选择区域_20190821172814](/newdisk/new_start/mine/MYMD/linux/image/深度截图_选择区域_20190821172814.png)