# json 中的ensure_ascii=False

[转载自](https://www.jianshu.com/p/86d66257de41)

在使用json.dumps时要注意一个问题

```
>>> import json
>>> print json.dumps('中国')
"\u4e2d\u56fd"
```

输出的会是
 '中国' 中的ascii 字符码，而不是真正的中文。

这是因为json.dumps 序列化时对中文默认使用的ascii编码.想输出真正的中文需要指定ensure_ascii=False：

```
>>> import json
>>> print json.dumps('中国')
"\u4e2d\u56fd"
>>> print json.dumps('中国',ensure_ascii=False)
"中国"
>>> 
```

