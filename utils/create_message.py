from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def amazon_message(product, update):

    first_name = update.message.from_user['first_name']

    if product.get_price().pvp.value != None:
        price = f"❌{product.get_price().pvp.value} ✅{product.get_price().price.value}"

    elif product.get_price().price.value != None:
        price = f"{product.get_price().price.value}"

    else:
        price = "Not available"

    message = f"""<a href='{product.get_image()}'>​​​​​​​​​​</a>
📌{product.get_title()}

💰Price: {price}

🔗Link: <a href=\"{product.return_url()}\">Click Here</a>

🗣 Post by: {first_name}
"""

    buttons = InlineKeyboardMarkup([[InlineKeyboardButton(text='🛒AMAZON🛒', url=product.return_url())]])

    return [message, buttons]
