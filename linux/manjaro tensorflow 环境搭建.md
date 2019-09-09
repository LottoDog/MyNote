# manjaro tensorflow 环境搭建

我们的配置是：

- CUDA-8.0
- cuDNN-6
- tensorflow-gpu 1.4

## 1. 双显卡切换为独显

独显必须一直保持开着的状态，才可以稳定运行cuda等程序，我们通过`bbswitch`切换独显

```
sudo tee /proc/acpi/bbswitch <<< ‘ON’
```

注意，如果`nvidia-smi -pm`为1的话上述方法是无效的，必须变为0，即实时切换状态

```
nvidia-smi -pm 0
```

## 2. 安装CUDA

### 2.1 yaourt 安装

```
yaourt -S cuda-8.0
```

如果遇到yaourt报告空间不够，则：

1. 打开`/etc/yaourtrc`
2. 将 `#TMPDIR="/tmp"` 改为`TMPDIR="/home/$USER/tmp"即可`

### 2.2 加入环境变量

通过安装日志可以发现，yaourt将安装包迁移到了`/opt`中，因此我们在 `.bashrc`或`.zshrc`、以及`/etc/profile`中加入：

```
export CUDA_HOME=/opt/cuda
export PATH=/opt/cuda/bin:$PATH
export LD_LIBRARY_PATH=/opt/cuda/lib64:$LD_LIBRARY_PATH
```

### 2.3 验证安装

查看CUDA版本

```
nvcc -V
```

编译samples，CUDA安装时自带了samples文件夹，进入该文件夹后直接编译（gcc啥的都给你装好了），但是一定记得用sudo，否则报错

```
cd /opt/cuda/samples

sudo make
```

查看编译结果：

```
cd bin/x86_64/linux/release


./deviceQuery    # 最后如果返回pass，则通过

./bandwidthTest    # 最后如果返回pass，则通过

reboot            # 最好重启一下
```

恭喜你，到了这一步，CUDA已经顺利安装完成啦！！

## 3. cuDNN安装

cuDNN是nivida提供的深度学习GPU库，在manjaro下非常好安装：

```
# 先确定独显是开着的
sudo tee /proc/acpi/bbswitch <<< ‘ON’

yaourt -S cudnn6
```

装好之后，将cudnn文件拷贝到cuda中：

```
sudo cp /opt/cudnn6/include/cudnn.h /opt/cuda/include
sudo cp cudnn6/lib64/libcudnn* /opt/cuda/lib64

# 增加权限
sudo chmod a+r cuda/include/cudnn.h
sudo chmod a+r cuda/include/cudnn.h
```

恭喜，至此你已经完成了准备工作啦！

## 4. 安装tensorflow-gpu版本

为了跟CUDA8兼容，我们安装1.4版本的tensorflow-gpu

```
pip install tensorflow-gpu==1.4
```

**重启，很关键***

```
reboot 
```

重启之后，打开ipython，输入命令进行测试：

```
import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
```

如果提示中不包含`ERROR`或`FAIL`字样，且包含了你的独显名称，那么就是正确安装了。

最后设置CPU按需求使用，在每次导入tf时：

```
# 设置tendorflow对显存使用按需增长。
import tensorflow as tf
config  = tf.ConfigProto()
config.gpu_options.allow_growth = True
session = tf.Session(config=config)
```

## 5. 安装keras

```
pip install keras
```

keras默认使用tensorflow后端，并且会直接调用其GPU，因此无需做任何改动











## 现实我使用的方法是：

```
sudo pacman -S bazel
```

```
sudo conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
sudo conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
sudo conda config --set show_channel_urls yes
```

```
conda install cudatoolkit==10.0.130 
conda install cudnn==7.6.0
conda install tensorflow-gpu==1.13.1 
```



































