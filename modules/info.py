from io import BytesIO
from typing import Union
import hikari
import lightbulb
from bot import SawshaBot
import utils
import miru

hm = utils.Plugin("hm")

@hm.command()
@lightbulb.option("user", description="The User To Get Info", type=hikari.Member, required=False)
@lightbulb.command("userinfo", "Gets Info About A User", pass_options=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def userinfo(ctx: utils.SlashContext, user: hikari.Member) -> None:
    user = user or ctx.member

    info = f"Username: {user.username}\nDiscriminator: {user.discriminator}\nCreation Date: {utils.date(user.created_at, ago=True)}\nAccount ID: {user.id}"
    await ctx.respond(info)
    
@hm.command()
@lightbulb.command("ping", "Gets The Bots Ping")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx: utils.SlashContext):
    return await ctx.respond(f"My Current Ping Is {round(ctx.app.heartbeat_latency * 1000)}ms")

@hm.command()
@lightbulb.command("test_group", "description")
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def foo(ctx: utils.SlashContext) -> None:
    pass



@foo.child
@lightbulb.command("bar", "test subcommand")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def bar(ctx:utils.SlashContext) -> None:
    await ctx.respond("invoked foo bar")  
    

def load(bot: SawshaBot) -> None:
    bot.add_plugin(hm)

def unload(bot: SawshaBot):
    bot.remove_plugin(hm)