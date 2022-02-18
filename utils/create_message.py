from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def amazon_message(product, update):

    first_name = update.message.from_user['first_name']

    if product.get_price().savings != None:
        price = f"❌{product.get_price().amount + product.get_price().savings.amount} ✅{product.get_price().amount} {product.get_price().currency} (-{product.get_price().savings.percentage}%) "
    
    elif product.get_price().amount != None:
        price = f"{product.get_price().amount} "

    else:
        price = "Not available"

    message = f"""<a href='{product.get_image()}'>​​​​​​​​​​</a>
📌<b>{product.get_title()}</b>

💰Price: {price} 

🔗Link: <a href=\"{product.return_url()}\">Click Here</a>

🗣 Post by: {first_name}
"""

    buttons = InlineKeyboardMarkup([[InlineKeyboardButton(text='🛒AMAZON🛒', url=product.return_url())]])

    return [message, buttons]
