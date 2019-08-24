# manjaro 安装deb

+ 安装debtap并更新到最新版本

  ```
  yaourt -S debtap
  sudo debtap -u
  ```

  

+ 使用方法

  ```
  sudo debtap  xxxx.deb
  ```

  > 安装时会提示输入包名，以及license。包名随意，license就填`GPL`吧
  > 上述操作完成后会在`deb`包同级目录生成`×.tar.xz`文件，直接用`pacman`安装即可

  ```
  sudo pacman -U x.tar.xz
  ```

  

