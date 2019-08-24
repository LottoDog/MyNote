# mysql 用户创建和授权



+ 登录

```
mysql -uroot -p
```

+ 参看版本

```
\s

mysql  Ver 8.0.16 for Linux on x86_64 (Source distribution)
```

+ 查看默认安装的用户

```
select user,host from mysql.user;
```

+ 创建并授权一个新用户

  > 8.0之后，用户创建和授权要分开。不然会报错

```
create user 'blime2'@'%' identified by 'pls';
grant all privileges on *.* to 'blime2'@'%';
```