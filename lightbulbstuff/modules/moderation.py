import calendar
import datetime
from typing import Sequence, Union
import hikari
import lightbulb
from bot import SkyeBot
import utils

ma = utils.Plugin("Moderation","Descrip")


@ma.command()
@lightbulb.option("user", description=f"User To Ban",autocomplete=True)
@lightbulb.command("unban", "Bans A user", pass_options=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def unban(ctx: utils.SlashContext, user: hikari.User):
    
    try:    
        user = await lightbulb.UserConverter(ctx).convert(user)
    except Exception as e:
        embed = hikari.Embed(title="Error!", description="No user found! Please try this cmd again but with their full username including their discriminator or try their ID with this.")
        return await ctx.respond(embed=embed)

    await ctx.get_guild().unban(user, reason=f"Responsible moderator: {ctx.author}")
    date = datetime.datetime.utcnow()
    utc_time = calendar.timegm(date.utctimetuple())
        
        
    embed = hikari.Embed(title=f"Succesfully unbanned: {user}!", description=f"Responsible moderator: {ctx.author}\nMember unbanned at <t:{utc_time}:F>")
    await ctx.respond(embed=embed)


@unban.autocomplete("user")  # Name of the option you want to autocomplete
async def foo_autocomplete(
    opt: hikari.AutocompleteInteractionOption, inter: hikari.AutocompleteInteraction
) -> Union[str, Sequence[str], hikari.CommandChoice, Sequence[hikari.CommandChoice]]:
    
    bans = [str(bans.user) for bans in await inter.app.rest.fetch_bans(inter.guild_id)]
    if opt.value == '':
        return [str(bans) for bans in bans]

    return [str(bans) for bans in bans if opt.value in bans]
    


def load(bot: SkyeBot) -> None:
    bot.add_plugin(ma)

def unload(bot: SkyeBot):
    bot.remove_plugin(ma)