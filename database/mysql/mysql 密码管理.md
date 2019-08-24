# mysql 密码管理

+ 限制重复使用以前的密码

  

  看一下相关的变量

  ```
  show variables like 'password%';
  
  +--------------------------+-------+
  | Variable_name            | Value |
  +--------------------------+-------+
  | password_history         | 0     |
  | password_require_current | OFF   |
  | password_reuse_interval  | 0     |
  +--------------------------+-------+
  
  ```

  

传统启动：

```
vim  /etc/my.cnf

像这样直接加入：
password_history=3，

需要重启数据库服务器才能生效
```



直接启动：

+ (全局级别)

```
mysql> set persist password_history=6;
```

+ （用户级别）

```
alter user 'blime2'@'%' password history 3;

desc mysql.user;
select user, host, Password_reuse_history from mysql.user;
```



> 修改密码时需要提供当前密码

```
set persist password_require_current=on;

alter user user() identified by 'xxxx' replace 'xxx'
```

>#其实不知道为什么，直接不写replace 'xxx'，也是可以的。
>
>而且password_require_current确实变成了，on