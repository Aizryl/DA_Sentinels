import scrapy
class ZipperURL(scrapy.Spider):
    name = "Zip"
    start_urls = ['http://192.168.84.128/zipper']
    def parse(self, response):
        css_selector ='img'
        for x in response.css(css_selector):
            newsel = '@src'
            yield {
                'Image Link': x.xpath(newsel).extract_first(),
            }
