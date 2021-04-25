from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def amazon_message(product):


    message = ""

    message += f"<a href='{product.get_image()}'>​​​​​​​​​​</a>\n"

    message += f"📌{product.get_title()}\n\n"

    if product.get_price().pvp.value != None:
        message += f"💰Price: ❌{product.get_price().pvp.value} ✅{product.get_price().price.value}\n\n"

    elif product.get_price().price.value != None:
        message += f"💰Price: {product.get_price().price.value}\n\n"

    else:
        message += "💰Price: Not available\n\n"

    message += f"🔗Link: <a href=\"{product.return_url()}\">Click Here</a>\n\n"

    buttons = InlineKeyboardMarkup([[InlineKeyboardButton(text='🛒AMAZON🛒', url=product.return_url())]])

    return [message, buttons]
