# django 链接postgresql

在项目的 settings.py 文件中的配置代码如下: 

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'testdb',  # 数据库名字(需要先创建)
        'USER': 'postgres',  # 登录用户名
        'PASSWORD': '123456',  # 密码
        'HOST': '',  # 数据库IP地址,留空默认为localhost
        'PORT': '5432',  # 端口
    }
}
```

