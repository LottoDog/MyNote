# jupyter的使用

+ #### jupyter多内核

  + java

  > ```
  > jupyter kernelspec list
  > ```
  >
  > 安装[IJAVA](https://github.com/SpencerPark/IJava)
  >
  > ```
  > git clone https://github.com/SpencerPark/IJava.git
  > cd IJava/
  > ```
  >
  > Linux/Unix:
  >
  > ```
  > chmod u+x gradlew && ./gradlew installKernel
  > ```
  >
  > Windows:
  >
  > ```
  > gradlew installKernel
  > ```

  + c++

  >[参考文档](https://xeus-cling.readthedocs.io/en/latest/installation.html#using-the-conda-package)
  >
  >```
  >conda install -c conda-forge xeus-cling
  >```
  
+ #### 快捷键

  - **命令模式 (按键 Esc 开启)**

    >- D,D : 删除选中的单元
    >
    >- Z : 恢复删除的最后一个单元
    >- Shift-M : 合并选中的单元
    >- A: 在上方插入新单元
    >- B: 在下方插入新单元

  - **编辑模式 ( Enter 键启动)**

    > + Tab : 代码补全或缩进
    > + Shift-Tab : 提示

+ #### jupyter lab