# No module named 'tensorflow.models' 解决方法

[参考链接](https://blog.csdn.net/RineZ/article/details/81671382)





1. 下载models

   ```bash
   git clone https://github.com/tensorflow/models
   ```

   有点慢，然后fork到码云下载了

   ```bash
   git clone https://gitee.com/blime/models.git
   ```

2. 复制到tensorflow的文件夹下

   如果不知道tensorflow的文件夹在哪里，可以通过以下方式查询

   ```bash
   python
   Python 3.7.3 (default, Mar 27 2019, 22:11:17) 
   [GCC 7.3.0] :: Anaconda, Inc. on linux
   Type "help", "copyright", "credits" or "license" for more information.
   >>> import tensorflow as tf
   >>> tf.__path__
   ['/home/blime/anaconda3/lib/python3.7/site-packages/tensorflow_estimator/python/estimator/api', '/home/blime/anaconda3/lib/python3.7/site-packages/tensorflow', '/home/blime/anaconda3/lib/python3.7/site-packages/tensorflow/_api/v1']
   ```

   接着利用cp指令赋值。因为涉及到usr文件夹，所以要用管理员权限。需要注意的是models文件夹下面还有文件夹，需要加上-r参数递归赋值

   ```bash
   sudo cp -r /home/blime/gitclone/models/ /home/blime/anaconda3/lib/python3.7/site-packages/tensorflow/
   ```

3. 修改路径

   将原来的from tensorflow.models.image.cifar10 import cifar10，根据实际文件夹的分布改成

   ```bash
   from tensorflow.models.tutorials.image.cifar10 import cifar10
   ```

   

