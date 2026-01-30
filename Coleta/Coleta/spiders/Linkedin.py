import scrapy


class LinkedinSpider(scrapy.Spider):
    name = "Linkedin"
    allowed_domains = ["www.linkedin.com"]
    start_urls = ["https://www.linkedin.com/jobs/search/?currentJobId=4292226001"]

    def parse(self, response):
        pass
