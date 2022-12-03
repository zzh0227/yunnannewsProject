import scrapy
import requests
from lxml import etree
class HomepageNewsSpider(scrapy.Spider):
    name = 'homepage_news'
    allowed_domains = ['www.yunnan.cn']
    start_urls = ['http://www.yunnan.cn/']
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56 "
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse, headers=self.headers)

    def parse(self, response):
        hrefs = response.xpath('//div[@class="tt clearfix"]//a/@href').extract()
        print(hrefs)
        n = 0
        for href in hrefs:
            try:
                resp = requests.get('http:'+href)
                html = etree.HTML(resp.text)
                title = html.xpath('//*[@id="layer213"]/text()').pop()
                time = html.xpath('/html/body/div[6]/div[1]/div[3]/div/span[2]/span[1]/text()').pop()
                source = html.xpath('/html/body/div[6]/div[1]/div[3]/div/span[2]/span[2]/text()').pop()
                ps = html.xpath('//*[@id="layer216"]/p')
                file = open("ynnews/" + title + '.txt', 'a', encoding='utf-8')
                file.write(time)
                file.write(source)
                for p in ps:
                    text = p.xpath('strong/text()')
                    if (not text):
                        text = p.xpath('./text()')
                    print(text)
                    if (text):
                        text = text.pop()
                        file.write(text)
                        file.write('\n')
                file.close()
                n = n+1
                print('第 %d 篇!!'%n)
            except:
                print("Error: 没有找到文件或读取文件失败")
            else:
                print("内容写入文件成功")
                file.close()
        pass

