import scrapy


class IndeedSpider(scrapy.Spider):
    name = "Indeed"
    allowed_domains = ["br.indeed.com"]
    start_urls = ["https://br.indeed.com/jobs?q=analista+de+dados"]

    def parse(self, response):
        pass
