# AmazonBot

🤖Fast and simple bot to transform links from Amazon into a nice post with your referral link in Telegram 🛒

### Prerequisites

* You need Python 3.8 or higher

```
python3 -m pip install -r requirements.txt
```

### Setup

In order to setup the bot you need to copy `example_credentials.json` to `credentials.json` in `config/example_credentials.json`.
Then add Bot Token (get it from [@BotFather](https://t.me/Botfather)) and Amazon configuration to the file `credentials.json`.
### Running

```
#If you want just run the bot
python3 main.py

# Or maybe run forever in to a VPS in linux
nohup python3 main.py &
```

### Customizing the message ✏️

Now customizing is more easy, you can go to `utils/create_message.py` and edit the variable `message` to put in whatever you want

![](https://telegra.ph/file/4d9dc08b6415986161fdd.png)
### Changelog

```
Version 1.2.0
  New features:
      - Show the percentage if the item is discounted
  Updated: 
      - python-amazon-paapi 3.3.2 --> 4.2.1
      - Some functions were updated due to the module upgrade

Version 1.1.0
  New features:
      - Remove message from user when post is submitted successfully
      - Added update object to utils/create_message to create more personalized message  
  Updated:
      - Updated regex top-domains

  Other:
      - Code cleaning
      
Version 1.0.0
  - Initial Release
```

## Built With

* [python-amazon-paapi](https://github.com/sergioteula/python-amazon-paapi)
* [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)

## License

This project is licensed under the MIT License - see the [LICENSE.MD](LICENSE.MD) file for details
