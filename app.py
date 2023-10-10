from webex_bot.webex_bot import WebexBot
import json
import os
from webex_bot.webex_bot import Command
from gpt import gpt
bot = os.environ.get("ACCESS_TOKEN")
bot = WebexBot(access_token = bot)
bot.commands.clear()
bot.run()