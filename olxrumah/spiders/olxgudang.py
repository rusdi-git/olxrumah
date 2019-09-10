import scrapy
from scrapy.http import HtmlResponse
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..items import OlxrumahItem

class OlxSpider(scrapy.Spider):
    name = 'olxgudang'
    start_urls = ['https://www.olx.co.id/bandung-kota_g4000018/disewakan-bangunan-komersil_c5156/q-Gudang']
    index = 0
    items = 0

    def get_number(self,text):
        result=''
        try:
            iter(text)
        except TypeError:
            return None
        for i in text:
            try:
                result+=str(int(i))
            except ValueError:
                continue
        return int(result)

    def parse(self,response):
        list_rumah = response.css('ul[data-aut-id="itemsList"]')
        for url in list_rumah.css('a::attr(href)'):
            yield response.follow(url, callback=self.parse_detail)

    def parse_detail(self,response):
        item = OlxrumahItem()
        price = response.css('span[data-aut-id="itemPrice"]::text').get()
        item['price'] = self.get_number(price)
        item['address'] = response.css('div[data-aut-id="itemLocation"]').css('span::text').get()
        item['supplyImageUrls'] = response.css('div.slick-track').css('img::attr(src)').get()
        luastanah = response.css('span[data-aut-id="value_p_sqr_land"]::text').get()
        item['luastanah']= self.get_number(luastanah)
        luasbangunan = response.css('span[data-aut-id="value_p_sqr_building"]::text').get()
        item['luasbangunan']= self.get_number(luasbangunan)
        item['fasilitas'] = response.css('span[data-aut-id="value_p_facility_0"]::text').get()
        item['title'] = response.css('h1[data-aut-id="itemTitle"]::text').get()
        item['url'] = response.url
        yield item