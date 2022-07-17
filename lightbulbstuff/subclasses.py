
from __future__ import annotations
import abc

import typing as t
import aiohttp

import hikari
import lightbulb

class MyCustomBot(lightbulb.BotApp):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    async def on_starting(self, _: hikari.StartingEvent) -> None:
        self.session = aiohttp.ClientSession()


class Plugin(lightbulb.Plugin):
    @property
    def bot(self) -> MyCustomBot:
        return t.cast(MyCustomBot, self.app)


class Context(lightbulb.Context):
    @property
    def bot(self) -> MyCustomBot:
        return t.cast(MyCustomBot, self.app)

    @property
    def session(self) -> aiohttp.ClientSession:
        return t.cast(self.bot.session, self.session)

class SlashContext(Context, lightbulb.SlashContext):
    ...
