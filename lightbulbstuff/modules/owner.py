import lightbulb
import hikari
from bot import SkyeBot
import utils

owner = utils.Plugin("owner")


@owner.command()
@lightbulb.add_checks(lightbulb.owner_only)
@lightbulb.option("module", "The Module To Reload")
@lightbulb.command("reload", "Reloads a module")
@lightbulb.implements(lightbulb.SlashCommand)
async def reload(ctx: utils.SlashContext):
    try:
        ctx.app.unload_extensions(ctx.options.module)
        ctx.app.load_extensions(ctx.options.module)
        await ctx.respond(f"Succesfully reloaded: {ctx.options.module}")
    except Exception as e:
        return await ctx.respond(f"There was an error!\nError Type: {e.__class__.__name__}\n```py\n{e}```")

def load(bot: SkyeBot) -> None:
    bot.add_plugin(owner)


def unload(bot: SkyeBot):
    bot.remove_plugin(owner)