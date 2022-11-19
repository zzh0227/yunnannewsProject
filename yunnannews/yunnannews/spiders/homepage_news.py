import scrapy


class HomepageNewsSpider(scrapy.Spider):
    name = 'homepage_news'
    allowed_domains = ['www.yunnan.cn']
    start_urls = ['http://www.yunnan.cn/']
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42 "
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse, headers=self.headers)

    def parse(self, response):
        hrefs = response.xpath('//div[@class="tt clearfix"]//a/@href').extract()
        print(hrefs)
        pass
