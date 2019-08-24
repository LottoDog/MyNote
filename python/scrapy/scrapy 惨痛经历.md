# scrapy 惨痛经历



2019.7.28

## 使用内置的ImagesPipeline下载图片

item.py

```
image_urls = scrapy.Field()
images = scrapy.Field()
这两个东西不能拼写错误，不然不会下载
```

