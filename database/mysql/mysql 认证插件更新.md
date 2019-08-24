# mysql 认证插件更新



```
show variables like 'default_authentication%';


+-------------------------------+-----------------------+
| Variable_name                 | Value                 |
+-------------------------------+-----------------------+
| default_authentication_plugin | caching_sha2_password |
+-------------------------------+-----------------------+

```



>  也可以用回之前版本旧的验证插件：mysql_native_password

```
alter user 'blime2'@'%' identified with mysql_native_password by 'xxx';
```

