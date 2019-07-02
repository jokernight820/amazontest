import scrapy

class FirstSpider(scrapy.Spider):
    name = "reviewer"
#scrapy crawl reviewer -o a.json
    start_urls=[
        'https://www.amazon.com/AhaStyle-Upgrade-Protective-Silicone-Compatible/product-reviews/B077187F2R/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
    ]

    def parse(self, response):
               for div in response.xpath('//div[@class="a-section celwidget"]'):
                    name=div.xpath('div[@class="a-row a-spacing-mini"]/a/div/span/text()').extract_first()
                    id=div.xpath('div[@class="a-row a-spacing-mini"]/a/@href').re("\\w{28}")[0]
                    star=div.xpath('div[@class="a-row"]/a/i/span/text()').extract_first()
                    verified=div.xpath('div[@class="a-row a-spacing-mini review-data review-format-strip"]/span/a/span/text()').extract_first()
                    date=div.xpath('span[@class="a-size-base a-color-secondary review-date"]/text()').extract_first()
                    #print(name+' '+star+' '+id+' '+verified+' '+date)
                    yield {
                        'name':name,
                        'id':id,

                        'rating':star,
                        'verified status':verified,
                        'date':date
                    }

               next="https://www.amazon.com"+response.xpath('//li[@class="a-last"]/a/@href').extract_first()
               yield scrapy.Request(next)

               #next='https://www.amazon.com'+response.xpath('//li[@class="a-last"]/a/@href').extract_first()
               #print(next)
               #yield scrapy.Request(next)










