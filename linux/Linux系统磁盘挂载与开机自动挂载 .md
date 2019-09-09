# Linux系统磁盘挂载与开机自动挂载

## 挂载磁盘

+ 列出所有磁盘

  ```
  fdisk -l
  #根据磁盘大小判断那块磁盘是新加需要挂载的磁盘
  ```

+ 格式化新加磁盘--------**不一定，有数据可以不用格式化！！！！！**

  ```
  mkfs.ext4 /dev/sdb6
  #/dev/sdb6 这是个例子，假如挂载的是/dev/sdb6
  ```

+ 建立挂载点

  ```
  sudo mkdir /newdisk
  ```

+ 挂载

  ```
  sudo mount /dev/sdb6 /newdisk/
  ```

## 开机自动挂载

+ 查看磁盘UUID信息

  ```
  sudo blkid
  ```

  ![深度截图_选择区域_20190719174258](/newdisk/new_start/mine/MYMD/linux/image/深度截图_选择区域_20190719174258.png)

  这里的/dev/sdb6的UUID是：8c3c58dd-ea6a-48ef-8d05-284756eec0e5

  复制下来，顺便记下文件类型：ext4

+ 将新加磁盘添加到 /etc/fstab文件中，即可实现开机自动挂载

  ```
  sudo vim /etc/fstab
  ```

  在该文件末尾添加 UUID=8c3c58dd-ea6a-48ef-8d05-284756eec0e5 /newdisk  ext4    defaults 0 0
  就可以了

  ![深度截图_选择区域_20190719174741](/newdisk/new_start/mine/MYMD/linux/image/深度截图_选择区域_20190719174741.png)