import logging
import json # for config
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
# Amazon Stuff
from amazon.tools import get_asin # Get asin from url
from utils.create_message import amazon_message # Create HTML template for amazon
from utils.product_amazon import Product
from utils.tools import  check_domain

with open('config/credentials.json') as config_file:
    config = json.load(config_file)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def start(update, context):
    update.message.reply_text('Send me links from Amazon! I will give you back a nice post.')


def message_url(update, context):

    amazon_valid_urls = ['www.amzn.to', 'amzn.to',
                         'www.amazon.', 'amazon.']

    url = update.message.text
    domain = check_domain(update.message.text)

    if domain.startswith(tuple(amazon_valid_urls)):

        if 'amzn.to/' in domain:
            url = requests.get(url).url

        product = Product(get_asin(url))
        message = amazon_message(product, update)
        context.bot.send_message(update.message.chat_id, message[0] , reply_markup=message[1], parse_mode='HTML')
        context.bot.delete_message(update.message.chat_id, update.message.message_id)


def main():
    updater = Updater(config['BOT-TOKEN'], use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    dispatcher.add_handler(MessageHandler(Filters.regex('(?i)((?:https?://|www\d{0,3}[.])?[a-z0-9.\-]+[.](?:(?:com.br/)|(?:ca/)|(?:com.mx/)|(?:com/)|(?:cn/)|(?:in/)|(?:co.jp/)|(?:sg/)|(?:com.tr/)|(?:ae/)|(?:sa/)|(?:fr/)|(?:de/)|(?:it/)|(?:nl/)|(?:pl/)|(?:es/)|(?:se/)|(?:co.uk/)|(?:com.au/))(?:/[^\s()<>]+[^\s`!()\[\]{};:\'".,<>?\xab\xbb\u201c\u201d\u2018\u2019])?)'), message_url))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
