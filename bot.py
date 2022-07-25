import hikari
import lightbulb
import aiohttp
import asyncpg
import os
import asyncpg
from dotenv import load_dotenv

load_dotenv()

class SawshaBot(lightbulb.BotApp):
    def __init__(self) -> None:
        super().__init__(
            prefix="s",
            token=os.environ['TOKEN'],
            intents=hikari.Intents.ALL,
        )
        self.subscribe(hikari.StartingEvent, self.on_starting)
        self.subscribe(hikari.StoppedEvent, self.on_stopped)

    async def on_starting(self, _: hikari.StartedEvent) -> None:
        self.session = aiohttp.ClientSession()
        
        self.load_extensions_from("./modules")

    async def on_stopped(self, _: hikari.StoppedEvent) -> None:
        await self.session.close()