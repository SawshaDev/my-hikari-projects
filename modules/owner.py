import lightbulb
import hikari
from bot import SawshaBot
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


@owner.command()
@lightbulb.add_checks(lightbulb.owner_only)
@lightbulb.option("status", "Status to  status lolllll", modifier=lightbulb.OptionModifier.CONSUME_REST)
@lightbulb.command("status", "changes status", pass_options=True)
@lightbulb.implements(lightbulb.PrefixCommand)
async def status(ctx: utils.PrefixContext, *,status: str):
    await ctx.bot.update_presence(status=hikari.Status.IDLE, activity=hikari.Activity(name=ctx.options.status))

    await ctx.respond(f"Updated Status To {status}")

    


def load(bot: SawshaBot) -> None:
    bot.add_plugin(owner)


def unload(bot: SawshaBot):
    bot.remove_plugin(owner)