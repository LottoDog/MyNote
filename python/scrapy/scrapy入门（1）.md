# scrapy入门（1）

我们准备做个小例子：爬取一下[豆瓣最受欢迎的影评](https://movie.douban.com/review/best/)



+ ### step 1:安装scrapy

  ```
  pip install scrapy --user
  ```

  

+ ### step 2:创建第一个项目，这里就叫做apple

  ```
  scrapy startproject apple 
  ```

  >You can start your first spider with:
  >    cd apple
  >    scrapy genspider example example.com

  

+ ### step 3:进入项目，创建一个爬虫 banana

  ```
  cd apple
  code .        #在vscode中打开
  scrapy genspider banana 'https://movie.douban.com/'     #创建爬虫banana，然后设置域名为’豆瓣‘
  ```

  （这里，如果不设置域名，就会提示以下错误）

  >scrapy genspider banana
  >
  >\# Usage
  >
  > scrapy genspider [options] <name> <domain>
  >
  >

  现在的目录结构就是这样了：

  ![深度截图_选择区域_20190725150011](/newdisk/new_start/mine/MYMD/python/scrapy/image/深度截图_选择区域_20190725150011.png)

  

+ ### step 4:初始URL

  然后把初始URL设置为，豆瓣最受欢迎的影评的URL：https://movie.douban.com/review/best/

  一会我们再来写parse这个函数。

  

+ ### step 5：items.py

  在items.py设置一下，我们想爬的内容，放在AppleItem，这个类中，

  这里我们想爬一下，影评的标题，作者，文章内容，和点赞数，和文章的URL。我们就先爬这么多吧。

  items.py

  ```
  import scrapy
  
  
  class AppleItem(scrapy.Item):
      # define the fields for your item here like:
      # name = scrapy.Field()
      title = scrapy.Field()
      author = scrapy.Field()
      content = scrapy.Field()
      like = scrapy.Field()
  ```

  

+ ### step 6：parse解析函数

  我们回到banana.py中，写一下parse这个解析函数。

  我们先在网页中看看我们想爬的东西，用xpath匹配爬取下来

  

+ 

  

