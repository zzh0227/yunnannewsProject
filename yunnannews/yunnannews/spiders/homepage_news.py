import scrapy


class HomepageNewsSpider(scrapy.Spider):
    name = 'homepage_news'
    allowed_domains = ['yunnan.cn']
    start_urls = ['https://yn.yunnan.cn/sz/']
    # 如果你访问不了，可以在这里改User-Agent https://user-agents.net/random
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; G301) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse, headers=self.headers)

    def parse(self, response):
        hrefs = response.xpath('//div[@class="xx ohd clear"]//a/@href').extract()
        for href in hrefs:
            print(href)
        pass
