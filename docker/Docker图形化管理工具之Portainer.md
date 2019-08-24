# Docker图形化管理工具之Portainer

[参考链接](https://blog.51cto.com/bovin/2170723)

+ **这里演示单机安装**

  ```
   docker volume create portainer_data
   docker run -d -p 9000:9000 --name portainer --restart always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer
  ```

+ 然后打开浏览器 http://localhost:9000

+ 第一次要创建一个帐号，填一下用户名，密码就好了