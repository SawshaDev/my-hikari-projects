import hikari
from bot import SawshaBot
import utils as utils
import lightbulb

eh = utils.Plugin("Eh")


@eh.listener(lightbulb.CommandErrorEvent)
async def on_error(event: lightbulb.CommandErrorEvent) -> None:
    if isinstance(event.exception, lightbulb.CommandInvocationError):
        await event.context.respond(f"Something went wrong during invocation of command `{event.context.command.name}`.")
        raise event.exception

    # Unwrap the exception to get the original cause
    exception = event.exception.__cause__ or event.exception

    if isinstance(exception, lightbulb.NotOwner):
        await event.context.respond("You are not the owner of this bot.")
    elif isinstance(exception, lightbulb.CommandIsOnCooldown):
        await event.context.respond(f"This command is on cooldown. Retry in `{exception.retry_after:.2f}` seconds.")
    elif ...:
        ...
    else:
        raise exception



def load(bot: SawshaBot) -> None:
    bot.add_plugin(eh)

def unload(bot: SawshaBot):
    bot.remove_plugin(eh)