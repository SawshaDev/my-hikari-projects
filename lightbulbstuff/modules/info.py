from io import BytesIO
from typing import Union
import hikari
import lightbulb
from bot import SkyeBot
import utils

hm = utils.Plugin("hm")

@hm.command()
@lightbulb.option("user", description="The User To Get Info", type=hikari.Member, required=False)
@lightbulb.command("userinfo", "Gets Info About A User", pass_options=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def userinfo(ctx: utils.SlashContext, user: hikari.Member) -> None:
    embed = hikari.Embed(description=f"Info About {user.mention}")
    embed.set_author(name=f"{user}", icon=user.avatar_url)

    show_roles = ", ".join(
            [f"<@&{x.id}>" for x in sorted(user.get_roles(), key=lambda x: x.position, reverse=True)]
    ) if len(user.get_roles()) > 1 else "No Roles"
    

    embed.add_field(name=f"Creation Date",value=utils.date(user.created_at, ago=True), inline=True)
    embed.add_field(name="Roles", value=show_roles, inline=True)

    await ctx.respond(embed)
    



def load(bot: SkyeBot) -> None:
    bot.add_plugin(hm)