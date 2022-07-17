import aiohttp
import hikari
import lightbulb
from subclasses import Context, SlashContext, MyCustomBot
from io import BytesIO
from config import token


bot = MyCustomBot(token, intents=hikari.Intents.ALL)



bot.load_extensions_from('modules/')


bot.run()