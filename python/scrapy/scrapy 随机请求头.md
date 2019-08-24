# scrapy 随机请求头

+ 在middlewares.py中加入

  ```
  class UserAgentDownloadMiddleware(object):
      USER_AGENTS = [
          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
          'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36',
          'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
          'Mozilla/5.0 (X11; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0',
          'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0',
          'Mozilla/5.0 (X11; Linux i586; rv:63.0) Gecko/20100101 Firefox/63.0',
          'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:63.0) Gecko/20100101 Firefox/63.0',
          'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.10; rv:62.0) Gecko/20100101 Firefox/62.0',
          'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
      ]
  
      def process_request(self, request, spider):
          user_agent = random.choice(self.USER_AGENTS)
          request.headers['User-Agent'] = user_agent
  ```

  这里面的User-Agent是在[这个网站](http://www.useragentstring.com/pages/useragentstring.php)中拿到的

  

+ 在settings.py中添加

  ```
  DOWNLOADER_MIDDLEWARES = {
     'useragent_demo.middlewares.UserAgentDownloadMiddleware': 543,
  }
  ```

  

