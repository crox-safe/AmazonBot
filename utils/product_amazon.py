
import json
from amazon_paapi import AmazonApi
from .tools import check_domain # To return url with asin

with open('config/credentials.json') as config_file:
    config = json.load(config_file)

amz_config = config['amazon']
amazon = AmazonApi  (amz_config['KEY'], amz_config['SECRET'], amz_config['TAG'], amz_config['COUNTRY'])


class Product():

    def __init__(self, asin):
        self.asin = asin
        self.product = amazon.get_items(asin)[0]

    def get_title(self):
        return self.product.item_info.title.display_value

    def get_price(self):
        return self.product.offers.listings[0].price

    def get_image(self):
        return self.product.images.primary.large.url

    def get_info(self):
        return self.product

    def return_url(self):
        url = self.product.detail_page_url
        return 'https://' + check_domain(url) + 'dp/' + self.asin + '/?tag=' + amz_config['TAG']
