from io import BytesIO
import hikari
import lightbulb
import subclasses

hm = subclasses.Plugin("hm")

@hm.command()
@lightbulb.command("hm", "aaa")
@lightbulb.implements(lightbulb.SlashCommand)
async def a(ctx: subclasses.SlashContext) -> None:
    await ctx.respond("hm!")

@hm.command()
@lightbulb.command("api_test", "description!")
@lightbulb.implements(lightbulb.SlashCommand)
async def ass(ctx: subclasses.SlashContext):
    async with ctx.bot.session.get("https://i.thino.pics/qag0pjhwu0w71.jpg") as request:
        image = BytesIO(await request.read())

    await ctx.respond(attachment=image)


def load(bot: subclasses.MyCustomBot) -> None:
    bot.add_plugin(hm)