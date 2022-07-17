
import datetime
import aiohttp
import crescent
import requests
import hikari
from crescent.ext import docstrings
from typing import Optional
import roblox


plugin = crescent.Plugin()

@plugin.load_hook
def on_load() -> None:
    print(f"LOADED")

@plugin.include
@docstrings.parse_doc
@crescent.command
async def ban(ctx: crescent.Context, member: Optional[hikari.User]=None, reason: Optional[str] = "No Reason Specified"):
    """Ban"""


    if ctx.guild_id is None:
        return 

    if member is None:
        return

    if ctx.member is None:
        return

    new_member = ctx.app.cache.get_member(ctx.guild_id, member) or await ctx.app.rest.fetch_member(ctx.guild_id, member)



    if ctx.member.get_top_role().position <= new_member.get_top_role().position: 
        return await ctx.respond("You cannot ban people of the same role!", ephemeral=True)


    await ctx.guild.ban(new_member, reason=reason)

    await ctx.respond(f"Member {new_member.mention} was succesfully banned!") 

def format_dt(dt: datetime.datetime, style: Optional[str] = None) -> str:
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=datetime.timezone.utc)

    if style is None:
        return f'<t:{int(dt.timestamp())}>'
    return f'<t:{int(dt.timestamp())}:{style}>'


@plugin.include
@docstrings.parse_doc
@crescent.command
async def userinfo(ctx: crescent.Context, user: str):
    idk = roblox.Client()
    user = await idk.get_user_by_username(user, expand=True)
    user_thumbnails = await idk.thumbnails.get_user_avatar_thumbnails(
        users=[user],
        type=roblox.thumbnails.AvatarThumbnailType.full_body,
        size=(420, 420)
    )

    if len(user_thumbnails) > 0:
        user_thumbnail = user_thumbnails[0]

    description = user.description

    if len(description) < 1:
        description = "None"


    embed = hikari.Embed(description=f"**Info About: [{user.name}](https://www.roblox.com/users/{user.id}/profile)**")

    embed.set_thumbnail(user_thumbnail.image_url)
        
    embed.add_field(name="Information", value=f"Display Name: {user.display_name}\nID: {user.id}\nBanned: {user.is_banned}")
    embed.add_field(name="Social", value=f"Followers: {await user.get_follower_count()}\nFollowing: {await user.get_following_count()}\nFriends: {await user.get_friend_count()}\nGroups: {len(await user.get_group_roles())}")
    embed.add_field(name="Description", value=f"**{description!r}**", inline=False)


    await ctx.respond(embed)




