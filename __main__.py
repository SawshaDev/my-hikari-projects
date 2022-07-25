import hikari
import lightbulb
from bot import SawshaBot
import miru

bot = SawshaBot()
miru.load(bot)

bot.run()