# mysql 用户管理

![深度截图_选择区域_20190806085304](/newdisk/new_start/mine/MYMD/database/mysql/image/深度截图_选择区域_20190806085304.png)

+ 创一个测试数据库

+ 创一个测试表

  ```
  create database testdb;
  create table testdb.t1(id int);
  ```

  

+ 创建一个角色

+ 看一下角色到底是什么                 

  ```
  create role 'write_role';
  select host,user,authentication_string from mysql.user;
  ```

  > 发现角色其实是没有密码的用户



+ 对角色进行授权

  ```
  grant insert,update,delete on testdb.* to 'write_role';
  grant select on testdb.* to 'write_role';
  ```

+ 创建一个新用户

+ 将角色授权给用户

  ```
  create user 'user1' identified by 'user1';
  grant 'write_role' to 'user1';
  ```

  

+ 查看用户都有什么权限

  ```
  show grants for 'user1' ;
  show grants for 'user1' using 'write_role';
  ```

+ 使用新用户user1查看是否成功

  ```
  mysql -uuser1 -p
  select * from testdb.t1;
  ```

  > ERROR 1142 (42000): SELECT command denied to user 'user1'@'localhost' for table 't1'

+ 不成功，看看是什么原因

  ```
  select current_role();
  ```

  >current_role() 
  >NONE   
  >
  >原因：角色未激活        

+ 激活角色

  ```
  set role 'write_role';
  select current_role();
  select * from testdb.t1;
  ```

  > 成功

  

+ 也可以在root中就给用户设置默认的角色

  ```
  mysql -uroot -p
  set default role 'write_role' to 'user1';
  set default role all to 'user1';
  ```

  //

  ```
  select * from mysql.default_roles;
  select * from mysql.role_edges;
  ```





+ 撤销权限

  ```
  revoke insert,update,delete on testdb.* from 'write_role';
  show grants for 'write_role';
  show grants for user1 using 'write_role';
  ```

  