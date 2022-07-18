import os
import crescent
import hikari
import config as config

bot = crescent.Bot(config.token, intents=hikari.Intents.ALL)

exts = [
    f"cogs.{ext if not ext.endswith('.py') else ext[:-3]}"
    for ext in os.listdir("cogs")
    if not ext.startswith("_")
]
for ext in exts:
    bot.plugins.load(ext)


bot.run()