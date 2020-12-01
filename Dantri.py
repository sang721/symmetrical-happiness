import scrapy

class Bao_Dantri(scrapy.Spider):
    name = "Dan tri"
    def start_requests(self):
        start_urls = "https://nhandan.com.vn/"
        return scrapy.Request(url = start_urls ,callback= self.parse,)
    def parse(self,response):
        pass
