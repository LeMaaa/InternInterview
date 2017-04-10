import scrapy
from scrapy.selector import Selector
import urlparse


from DecorMatters.items import DecorMattersItem

class Image_Spider(scrapy.Spider):

# override name, start_urls and parse 
	name = "DM_Spider"

	start_urls = [
	     "http://www.decormatters.com/index.php"
	]

	def parse(self,response):
		sel = Selector(response)

# extract images' relative urls
		image_url =sel.xpath("//img/@src").extract()

# define base_url string to get images' absolute url 
		base_url = "http://www.decormatters.com/"


		item = DecorMattersItem()
		
# call urljoin function to concatenate relative uls with base_url
		item['image_urls'] = [urlparse.urljoin(base_url,u) for u in image_url]

		yield item

		
