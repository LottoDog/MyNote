# linux 命令行翻译工具

[github网址](https://github.com/afc163/fanyi)

+ 安装npm

  ```
  sudo pacman -S npm
  # 这里是manjaro,其他linux发行版自行下载
  ```

+ 安装fanyi

  ```
  npm install fanyi -g
  ```

+ 使用

  ```
  fy word
  fanyi apple
  # 用fanyi或者fy都可以，这里习惯用fy
  fy '句子'
  ```

![深度截图_选择区域_20190719203649](/newdisk/new_start/mine/MYMD/linux/image/深度截图_选择区域_20190719203649.png)











+ 如果有报错  **Error: spawn festival ENOENT**

  ![深度截图_选择区域_20190719203756](/newdisk/new_start/mine/MYMD/linux/image/深度截图_选择区域_20190719203756.png)

  ```
  sudo pacman -S festival
  #manjaro
  #ubuntu的话就输入
  sudo apt-get install festival festvox-kallpc16k
  ```